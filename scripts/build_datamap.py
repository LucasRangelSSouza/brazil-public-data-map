"""Build the data map: one catalogue of every table in every published Kaggle dataset.

Inputs
  datamap/data/manifests/<slug>/release_manifest.json   the manifest published inside each dataset
  datamap/subjects.json                                  curated source facts (publisher, official URL, how to fetch)
  the source lake (BigQuery), read-only                  table and column descriptions, types, and query lineage

Outputs (all generated, all committed so readers need no access to the lake)
  datamap/data/catalog.json            the whole map, one file, for tools
  datamap/site/data/index.json         small index the site loads first
  datamap/site/data/datasets/<slug>.json   one file per dataset with every table and column
  docs/datamap/<slug>.md               one Markdown data dictionary per dataset, field by field
  docs/datamap/README.md               the index of those dictionaries
  datamap/dictionaries/<slug>/DATA_DICTIONARY.md  and  data_dictionary.json   the files shipped inside each Kaggle dataset

Usage
  python scripts/build_datamap.py [--no-lake]     --no-lake rebuilds from the committed lake extract only
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DM = ROOT / "datamap"
MANIFESTS = DM / "data" / "manifests"
LAKE_EXTRACT = DM / "data" / "lake_extract.json"
OWNER = "lucasrangelss"
ZONE = {"raw": "raw_zone", "trusted": "trusted_zone", "semantic": "semantic_zone"}
NOISE_COLUMNS = {"payload_json", "json_bruto"}
# Columns removed from the releases because they pointed at internal storage, internal URLs or local paths of the source system.
WITHHELD_COLUMNS = {"gcs_uri_pdf", "url_download_pdf", "url_download_pdf_vigente", "url_download_pdf_base", "caminho_local", "caminho_extraido",
                    "caminho_conteudo", "raw_table", "pdf_path"}
TECH_TABLE = re.compile(r"(__rebuild|_bak|_old|_tmp|_backup|_copy|_test)")


# Internal names that must not appear in a public dictionary. The descriptions are kept otherwise verbatim.
SCRUB = [
    (re.compile(r"Data Lake Educacional d[aeo] MindLab", re.I), "educational data lake"),
    (re.compile(r"d[aeo] MindLab", re.I), "of the source lake"),
    (re.compile(r"MindLab", re.I), "the source lake"),
    (re.compile(r"Mente Inovadora", re.I), "the source organization"),
    (re.compile(r"Neolude", re.I), "the platform vendor"),
    (re.compile(r"(raw|trusted|semantic)_zone\.", re.I), r"/"),
    (re.compile(r"gs://[^\s,;)]+", re.I), "<storage URI>"),
    (re.compile(r"https://api-datalake[^\s,;)]+", re.I), "<download URL>"),
]


def scrub(text: str) -> str:
    for pattern, repl in SCRUB:
        text = pattern.sub(repl, text or "")
    return text


def load_subjects() -> dict:
    return json.loads((DM / "subjects.json").read_text(encoding="utf-8"))


def dataset_subject(slug: str) -> str:
    return re.sub(r"-(raw-trusted|analytics)(-part-\d+)?$", "", slug)


def dataset_kind(slug: str) -> str:
    return "analytics" if slug.endswith("-analytics") else "raw-trusted"


def read_manifests() -> dict[str, dict]:
    out = {}
    for path in sorted(MANIFESTS.glob("*/release_manifest.json")):
        out[path.parent.name] = json.loads(path.read_text(encoding="utf-8"))
    return out


# ---- source lake extract ---------------------------------------------------------------------------------------

def extract_lake(manifests: dict[str, dict]) -> dict:
    """Read descriptions, types and lineage from the lake. Needs GOOGLE_APPLICATION_CREDENTIALS and EXPORT_PROJECT."""
    from google.cloud import bigquery

    project = os.environ["EXPORT_PROJECT"]
    client = bigquery.Client(project=project)
    wanted = {(t["layer"], t["table_id"]) for m in manifests.values() for t in m["tables"]}

    def one(key):
        layer, table_id = key
        try:
            t = client.get_table(f"{project}.{ZONE[layer]}.{table_id}")
        except Exception as exc:  # noqa: BLE001
            return key, {"error": str(exc)[:120]}
        cols = []

        def walk(fields, prefix=""):
            for f in fields:
                cols.append({"name": prefix + f.name, "type": f.field_type, "mode": f.mode, "description": f.description or ""})
                if f.field_type == "RECORD":
                    walk(f.fields, prefix + f.name + ".")

        walk(t.schema)
        return key, {"description": t.description or "", "columns": cols, "partitioning": t.time_partitioning.type_ if t.time_partitioning else None,
                     "clustering": list(t.clustering_fields or [])}

    with ThreadPoolExecutor(16) as pool:
        tables = dict(pool.map(one, sorted(wanted)))

    zone_to_layer = {v: k for k, v in ZONE.items()}
    jobs = client.query(
        """
        select destination_table.dataset_id d, destination_table.table_id t, rt.dataset_id rd, rt.table_id rt, count(*) n
        from `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT j, unnest(referenced_tables) rt
        where creation_time > timestamp_sub(current_timestamp(), interval 170 day)
          and job_type = 'QUERY' and state = 'DONE' and error_result is null
          and destination_table.dataset_id in ('raw_zone', 'trusted_zone', 'semantic_zone')
        group by 1, 2, 3, 4
        """
    ).result()
    edges = []
    for r in jobs:
        a, b = (zone_to_layer.get(r.rd), r.rt), (zone_to_layer.get(r.d), r.t)
        if a[0] and b[0] and a != b and a in wanted and b in wanted:
            edges.append({"from": {"layer": a[0], "table": a[1]}, "to": {"layer": b[0], "table": b[1]}, "jobs": r.n})
    return {"tables": {f"{k[0]}/{k[1]}": v for k, v in tables.items()}, "edges": edges}


# ---- catalogue -------------------------------------------------------------------------------------------------

def build(manifests: dict[str, dict], lake: dict, subjects: dict) -> dict:
    datasets, table_index = [], {}
    for slug, m in sorted(manifests.items()):
        subject = dataset_subject(slug)
        info = subjects["subjects"].get(subject, {})
        parquet_bytes = {f["path"]: f["bytes"] for f in m["files"]}
        tables = []
        for t in sorted(m["tables"], key=lambda x: (x["layer"], x["table_id"])):
            meta = lake["tables"].get(f"{t['layer']}/{t['table_id']}", {})
            columns = [c for c in meta.get("columns", []) if (c["name"] not in NOISE_COLUMNS or t["layer"] == "raw") and c["name"] not in WITHHELD_COLUMNS]
            entry = {
                "id": f"{t['layer']}/{t['table_id']}", "layer": t["layer"], "table": t["table_id"], "file": t["parquet"], "rows": t["rows"],
                "bytes": parquet_bytes.get(t["parquet"], 0), "description": scrub(meta.get("description", "")), "columns": [dict(c, description=scrub(c["description"])) for c in columns],
                "column_count": len(columns), "described_columns": sum(1 for c in columns if c["description"]),
                "ai_described_columns": sum(1 for c in columns if "gerada por IA" in c["description"]),
                "dataset": slug, "subject": subject, "upstream": [], "downstream": [],
            }
            tables.append(entry)
            table_index[entry["id"]] = entry
        datasets.append({
            "slug": slug, "owner": OWNER, "url": f"https://www.kaggle.com/datasets/{OWNER}/{slug}", "subject": subject, "kind": dataset_kind(slug),
            "title": f"{info.get('title', subject)}: {'Analytics' if dataset_kind(slug) == 'analytics' else 'Raw and Trusted'}",
            "snapshot_date": m["snapshot_date"], "tables": tables, "table_count": len(tables), "rows": sum(t["rows"] for t in tables),
            "bytes": sum(t["bytes"] for t in tables),
        })
    edges = []
    for e in lake["edges"]:
        a, b = f"{e['from']['layer']}/{e['from']['table']}", f"{e['to']['layer']}/{e['to']['table']}"
        if a in table_index and b in table_index and not TECH_TABLE.search(e["from"]["table"] + e["to"]["table"]):
            table_index[a]["downstream"].append(b)
            table_index[b]["upstream"].append(a)
            edges.append({"from": a, "to": b, "kind": f"{e['from']['layer']}->{e['to']['layer']}", "jobs": e["jobs"]})
    # Most raw->trusted loads are Python jobs, invisible to query lineage: a trusted table that shares its name with a raw table is its typed copy.
    existing = {(e["from"], e["to"]) for e in edges}
    for tid, t in table_index.items():
        if t["layer"] == "trusted" and f"raw/{t['table']}" in table_index and (f"raw/{t['table']}", tid) not in existing:
            raw_id = f"raw/{t['table']}"
            table_index[raw_id]["downstream"].append(tid)
            t["upstream"].append(raw_id)
            edges.append({"from": raw_id, "to": tid, "kind": "raw->trusted", "jobs": 0, "inferred": True})
    for t in table_index.values():
        t["upstream"] = sorted(set(t["upstream"]))
        t["downstream"] = sorted(set(t["downstream"]))
    return {"datasets": datasets, "edges": edges, "joins": join_keys(table_index), "subjects": subjects["subjects"]}


def join_keys(table_index: dict[str, dict]) -> list[dict]:
    """Columns that appear in tables of more than one subject are the practical joins between sources."""
    seen = defaultdict(lambda: {"tables": [], "subjects": set(), "types": set()})
    for t in table_index.values():
        if t["layer"] == "raw":
            continue
        for c in t["columns"]:
            if c["name"] in NOISE_COLUMNS or "." in c["name"]:
                continue
            e = seen[c["name"]]
            e["tables"].append(t["id"])
            e["subjects"].add(t["subject"])
            e["types"].add(c["type"])
    out = []
    for name, e in seen.items():
        if len(e["subjects"]) >= 2 and len(e["tables"]) >= 3 and re.search(r"(codigo|cod_|co_|id_|_id$|cnpj|numero_controle|ano|uf|sigla)", name):
            out.append({"column": name, "subjects": sorted(e["subjects"]), "types": sorted(e["types"]), "table_count": len(e["tables"]), "tables": sorted(e["tables"])[:60]})
    return sorted(out, key=lambda x: (-len(x["subjects"]), -x["table_count"], x["column"]))


# ---- renderers -------------------------------------------------------------------------------------------------

def fmt(n: int) -> str:
    return f"{n:,}"


def esc(text: str) -> str:
    return (text or "").replace("|", "\\|").replace("\n", " ").strip()


def render_dictionary(ds: dict, catalog: dict) -> str:
    info = catalog["subjects"].get(ds["subject"], {})
    lines = [f"# {ds['title']}", "", f"Dataset: [{ds['owner']}/{ds['slug']}]({ds['url']}) · snapshot {ds['snapshot_date']} · {ds['table_count']} tables · {fmt(ds['rows'])} rows", ""]
    lines += [f"**Source:** {info.get('publisher', '')}, [{info.get('official_url', '')}]({info.get('official_url', '')})", "",
              info.get("summary", ""), "",
              f"**Grain and keys:** {info.get('grain', 'see each table')}", "",
              "**Layers.** `raw` is the source snapshot as delivered. `trusted` is typed, deduplicated and named consistently. `semantic` joins and reshapes trusted tables for analysis. "
              "Every table is a Parquet file named `<layer>__<table>.parquet` at the root of the dataset.", "",
              f"The full interactive map (lineage, joins, search) is at [{catalog['site_url']}]({catalog['site_url']}). "
              "Column descriptions come from the source lake's catalogue and are a reading aid, not a legal definition.", ""]
    lines += ["## Tables", "", "| Layer | Table | Rows | Columns | Described | Upstream |", "|---|---|---:|---:|---:|---|"]
    for t in ds["tables"]:
        up = ", ".join(f"`{u.split('/', 1)[1]}`" for u in t["upstream"][:4]) + (" …" if len(t["upstream"]) > 4 else "")
        lines.append(f"| {t['layer']} | [`{t['table']}`](#{t['layer']}-{re.sub(r'[^a-z0-9]+', '-', t['table'].lower())}) | {fmt(t['rows'])} | {t['column_count']} | {t['described_columns']} | {up or 'source'} |")
    for t in ds["tables"]:
        lines += ["", f"## {t['layer']} · {t['table']}", "", f"File `{t['file']}` · {fmt(t['rows'])} rows · {t['column_count']} columns"]
        if t["description"]:
            lines += ["", t["description"].strip()]
        if t["upstream"]:
            lines += ["", "**Built from:** " + ", ".join(f"`{u}`" for u in t["upstream"])]
        if t["downstream"]:
            lines += ["", "**Feeds:** " + ", ".join(f"`{d}`" for d in t["downstream"][:12]) + (" …" if len(t["downstream"]) > 12 else "")]
        lines += ["", "| Column | Type | Description |", "|---|---|---|"]
        for c in t["columns"]:
            lines.append(f"| `{c['name']}` | {c['type']} | {esc(c['description'])} |")
    return "\n".join(lines) + "\n"


def kaggle_description(ds: dict, catalog: dict) -> str:
    """Markdown shown on the Kaggle dataset page. The full column-level dictionary lives in the repository and the map."""
    info = catalog["subjects"].get(ds["subject"], {})
    site = catalog["site_url"]
    repo = "https://github.com/LucasRangelSSouza/brazil-public-data-map"
    layers = sorted({t["layer"] for t in ds["tables"]})
    lines = [f"# {ds['title']}", "",
             f"{ds['table_count']} tables, {fmt(ds['rows'])} rows, snapshot {ds['snapshot_date']}. {info.get('summary', '')}", "",
             "## Where the data comes from", "",
             f"- **Publisher:** {info.get('publisher', '')}",
             f"- **Official source:** {info.get('official_url', '')}",
             f"- **How it is fetched:** {info.get('how_to_fetch', '')}",
             f"- **Grain and keys:** {info.get('grain', '')}", "",
             "## How the files are organised", "",
             "Every table is one Parquet file at the dataset root, named `<layer>__<table>.parquet`. "
             + ("`raw` is the source snapshot as delivered; `trusted` is typed, deduplicated and consistently named. " if "raw" in layers or "trusted" in layers else "")
             + ("`semantic` tables join and reshape trusted tables for analysis; build them from the matching raw-and-trusted dataset. " if "semantic" in layers else "")
             + "`release_manifest.json` holds the SHA-256 and size of every file, `schemas.json` the schema of every table and `audit.json` the export counts.", "",
             "## Documentation, field by field", "",
             f"- Interactive data map (search, lineage, joins): {site}#/dataset/{ds['slug']}",
             f"- Data dictionary of this dataset, every column: {repo}/blob/main/docs/datamap/{ds['slug']}.md",
             f"- How the raw layer is obtained from the official source (notebook): {repo}/blob/main/notebooks/sources/{info.get('notebook', ds['subject'])}.ipynb",
             f"- Code and release contracts: {repo}", "",
             "Column descriptions come from the source lake's catalogue, in Portuguese; a share is marked there as AI generated. They are a reading aid, not a legal definition.", "",
             "## Tables", "", "| Layer | Table | Rows | Columns |", "|---|---|---:|---:|"]
    for t in ds["tables"]:
        lines.append(f"| {t['layer']} | `{t['table']}` | {fmt(t['rows'])} | {t['column_count']} |")
    lines += ["", "## Read a table", "", "```python", "import kagglehub, pandas as pd",
              f"path = kagglehub.dataset_download(\"{ds['owner']}/{ds['slug']}\", path=\"{ds['tables'][0]['file']}\")", "df = pd.read_parquet(path)", "```", "",
              "Values are published as held in the snapshot, without masking. Source terms apply; credit the original publisher.", "",
              "My portfolio: https://rangeltech.net", ""]
    return "\n".join(lines)


def render_index(catalog: dict) -> str:
    lines = ["# Data dictionary", "",
             f"{len(catalog['datasets'])} datasets, {sum(d['table_count'] for d in catalog['datasets'])} tables, {fmt(sum(d['rows'] for d in catalog['datasets']))} rows, "
             "every field documented where the source lake carries a description. Each dictionary also ships inside its Kaggle dataset as `DATA_DICTIONARY.md` and `data_dictionary.json`.", "",
             f"Interactive map: {catalog['site_url']}", "", "| Source | Dataset | Tables | Rows |", "|---|---|---:|---:|"]
    for d in catalog["datasets"]:
        lines.append(f"| {catalog['subjects'].get(d['subject'], {}).get('title', d['subject'])} | [{d['slug']}]({d['slug']}.md) | {d['table_count']} | {fmt(d['rows'])} |")
    return "\n".join(lines) + "\n"


def write_outputs(catalog: dict) -> None:
    (DM / "data").mkdir(parents=True, exist_ok=True)
    (DM / "data" / "catalog.json").write_text(json.dumps(catalog, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    site_data = DM / "site" / "data"
    shutil.rmtree(site_data, ignore_errors=True)
    (site_data / "datasets").mkdir(parents=True)
    index = {
        "generated_at": catalog["generated_at"], "site_url": catalog["site_url"], "subjects": catalog["subjects"], "edges": catalog["edges"], "joins": catalog["joins"],
        "datasets": [{k: v for k, v in d.items() if k != "tables"} | {"tables": [{k: v for k, v in t.items() if k != "columns"} for t in d["tables"]]} for d in catalog["datasets"]],
    }
    (site_data / "index.json").write_text(json.dumps(index, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    search = [[t["id"], c["name"], c["type"], c["description"][:140]] for d in catalog["datasets"] for t in d["tables"] for c in t["columns"]]
    (site_data / "columns.json").write_text(json.dumps(search, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    docs = ROOT / "docs" / "datamap"
    shutil.rmtree(docs, ignore_errors=True)
    docs.mkdir(parents=True)
    ship = DM / "dictionaries"
    shutil.rmtree(ship, ignore_errors=True)
    for d in catalog["datasets"]:
        (site_data / "datasets" / f"{d['slug']}.json").write_text(json.dumps(d, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        md = render_dictionary(d, catalog)
        (docs / f"{d['slug']}.md").write_text(md, encoding="utf-8")
        (ship / d["slug"]).mkdir(parents=True)
        (ship / d["slug"] / "DATA_DICTIONARY.md").write_text(md, encoding="utf-8")
        (ship / d["slug"] / "data_dictionary.json").write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
    (docs / "README.md").write_text(render_index(catalog), encoding="utf-8")
    meta_dir = DM / "kaggle_metadata"
    shutil.rmtree(meta_dir, ignore_errors=True)
    meta_dir.mkdir()
    for d in catalog["datasets"]:
        description = kaggle_description(d, catalog)
        (meta_dir / f"{d['slug']}.md").write_text(description, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-lake", action="store_true", help="reuse datamap/data/lake_extract.json instead of reading the lake")
    args = parser.parse_args()
    manifests = read_manifests()
    if args.no_lake:
        lake = json.loads(LAKE_EXTRACT.read_text(encoding="utf-8"))
    else:
        lake = extract_lake(manifests)
        LAKE_EXTRACT.write_text(json.dumps(lake, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    subjects = load_subjects()
    catalog = build(manifests, lake, subjects)
    from datetime import datetime, timezone

    catalog["generated_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    catalog["site_url"] = subjects["site_url"]
    write_outputs(catalog)
    tables = [t for d in catalog["datasets"] for t in d["tables"]]
    print(f"datasets {len(catalog['datasets'])}, tables {len(tables)}, columns {sum(t['column_count'] for t in tables)}, "
          f"described {sum(t['described_columns'] for t in tables)}, lineage edges {len(catalog['edges'])}, join keys {len(catalog['joins'])}")


if __name__ == "__main__":
    main()
