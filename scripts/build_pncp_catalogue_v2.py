"""Build the global Kaggle catalogue for the 11-subject / 31-dataset release (2026-10-01 reorg).

Replaces build_pncp_catalogue.py, which depended on a per-table publication plan and
per-dataset release_manifest.json files that do not exist under the new scheme (one
dataset per subject x layer, not one dataset per table).

Sources, in priority order, for each of the 31 published slugs:
1. `kaggle datasets list --mine --csv` (always available: size in bytes, last update, votes).
2. Export-host ledger.jsonl files (candidates/subjects/ledger.jsonl on the VPS and on
   vertex-mi-prd) when the publishing host is still reachable: exact row_count and
   publish timestamp.
3. A manual override table for datasets whose publishing VM was already deleted
   before this script was written, mined by hand from poller/STATE.md narration
   (each value cross-referenced against at least one explicit "PUBLICADO (N rows)"
   line in STATE.md on 2026-10-01). Marked `row_count_source: "state_md"` so a future
   run can replace it with a ledger value if one ever resurfaces.

Row counts that could not be confirmed from either a live ledger or STATE.md are left
`null` with `row_count_source: "unknown"` rather than guessed.

Output: sources/pncp_kaggle_catalogue.json (schema_version 2.0) and
docs/pncp-kaggle-catalogue.md.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OWNER = "lucasrangelss"

SUBJECTS = {
    "ibge": ["ibge-raw-trusted", "ibge-analytics"],
    "ica": ["ica-raw-trusted", "ica-analytics"],
    "qedu": ["qedu-raw-trusted"],
    "ideb": ["ideb-raw-trusted", "ideb-analytics"],
    "fundeb": ["fundeb-raw-trusted", "fundeb-analytics"],
    "fnde-salario-educacao": [
        "fnde-salario-educacao-raw-trusted-part-1",
        "fnde-salario-educacao-raw-trusted-part-2",
        "fnde-salario-educacao-analytics",
    ],
    "pncp": ["pncp-raw-trusted-part-1", "pncp-raw-trusted-part-2", "pncp-analytics"],
    "taxas-rendimento": ["taxas-rendimento-raw-trusted", "taxas-rendimento-analytics"],
    "saeb": [
        "saeb-raw-trusted-part-1",
        "saeb-raw-trusted-part-2",
        "saeb-raw-trusted-part-3",
        "saeb-raw-trusted-part-4",
        "saeb-analytics",
    ],
    "siope": [
        "siope-raw-trusted-part-1",
        "siope-raw-trusted-part-2",
        "siope-raw-trusted-part-3",
        "siope-raw-trusted-part-4",
        "siope-analytics",
    ],
    "censo-escolar": [
        "censo-escolar-raw-trusted-part-1",
        "censo-escolar-raw-trusted-part-2",
        "censo-escolar-raw-trusted-part-3",
        "censo-escolar-analytics",
    ],
}

# Mined by hand from poller/STATE.md 2026-10-01 entries, after the publishing VM
# (export-tmp / export-tmp2 / lake-stg) had already been deleted and its ledger lost.
# Each row_count below has an explicit "PUBLICADO (N rows ...)" line in STATE.md.
STATE_MD_ROW_COUNTS = {
    "pncp-raw-trusted-part-2": 817211,          # STATE.md ~17:40 UTC: "PUBLICADO (817.211 rows, 17:32:44Z)"
    "censo-escolar-raw-trusted-part-1": 3103787,   # STATE.md ~21:15 UTC: "PUBLICOU as 21:08:37Z (3.103.787 rows)"
    "censo-escolar-raw-trusted-part-2": 4831642,   # STATE.md ~22:15 UTC: "PUBLICOU as 22:03:35Z (4.831.642 rows)"
    "censo-escolar-raw-trusted-part-3": 55639423,  # STATE.md ~23:50 UTC: "PUBLICOU as 23:42:01Z (55.639.423 rows)"
    "siope-raw-trusted-part-2": 519024963,      # STATE.md ~18:40 UTC: "PUBLICOU (519.024.963 rows, 18:23:42Z)"
    "siope-raw-trusted-part-4": 448537682,      # STATE.md ~20:10 UTC: "PUBLICADO (448.537.682 rows, 19:45:11Z)"
}


def load_kaggle_csv(path: Path) -> dict[str, dict]:
    out = {}
    with path.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            ref = row["ref"]
            if not ref.startswith(OWNER + "/"):
                continue
            slug = ref.split("/", 1)[1]
            out[slug] = {
                "title": row["title"],
                "size_bytes": int(row["size"]) if row["size"] else None,
                "last_updated": row["lastUpdated"],
                "vote_count": int(row["voteCount"]) if row["voteCount"] else 0,
            }
    return out


def load_ledgers(paths: list[Path]) -> dict[str, dict]:
    out = {}
    for path in paths:
        if not path.exists():
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            entry = json.loads(line)
            if entry.get("status") == "published" and "rows" in entry:
                out[entry["key"]] = {"row_count": entry["rows"], "published_at": entry.get("at")}
    return out


def build(kaggle: dict[str, dict], ledgers: dict[str, dict]) -> dict:
    entries = []
    for subject, slugs in SUBJECTS.items():
        for slug in slugs:
            meta = kaggle.get(slug)
            ledger = ledgers.get(slug)
            if ledger:
                row_count, row_count_source = ledger["row_count"], "ledger"
                published_at = ledger["published_at"]
            elif slug in STATE_MD_ROW_COUNTS:
                row_count, row_count_source = STATE_MD_ROW_COUNTS[slug], "state_md"
                published_at = meta["last_updated"] if meta else None
            else:
                row_count, row_count_source = None, "unknown"
                published_at = meta["last_updated"] if meta else None
            entries.append({
                "subject": subject,
                "dataset": f"{OWNER}/{slug}",
                "dataset_url": f"https://www.kaggle.com/datasets/{OWNER}/{slug}",
                "state": "published" if meta else "missing",
                "size_bytes": meta["size_bytes"] if meta else None,
                "last_updated": published_at,
                "row_count": row_count,
                "row_count_source": row_count_source,
            })
    published = [e for e in entries if e["state"] == "published"]
    known_rows = [e["row_count"] for e in published if e["row_count"] is not None]
    return {
        "schema_version": "2.0",
        "generated_from": "kaggle datasets list --mine --csv + export-host ledgers + STATE.md overrides",
        "datasets": len(entries),
        "published": len(published),
        "missing": len(entries) - len(published),
        "rows_published_known": sum(known_rows),
        "rows_unknown_count": len(published) - len(known_rows),
        "entries": entries,
    }


def render_markdown(catalogue: dict) -> str:
    lines = [
        "# Kaggle catalogue — PNCP + 10 other public-data subjects",
        "",
        f"{catalogue['published']} of {catalogue['datasets']} datasets published; "
        f"{catalogue['missing']} missing. Row counts known for "
        f"{catalogue['published'] - catalogue['rows_unknown_count']} of {catalogue['published']} "
        f"published datasets ({catalogue['rows_published_known']:,} rows total; "
        f"{catalogue['rows_unknown_count']} dataset(s) have an unconfirmed count because the "
        "publishing VM was deleted before its ledger could be read).",
        "",
        "| Subject | Dataset | Rows | Row source | Size | Last updated | State |",
        "|---|---|---:|---|---:|---|---|",
    ]
    for e in catalogue["entries"]:
        rows = f"{e['row_count']:,}" if e["row_count"] is not None else "unknown"
        size = f"{e['size_bytes'] / 1e9:.2f} GB" if e.get("size_bytes") else "-"
        lines.append(
            f"| {e['subject']} | [{e['dataset'].split('/')[1]}]({e['dataset_url']}) | {rows} | "
            f"{e['row_count_source']} | {size} | {e['last_updated'] or '-'} | {e['state']} |"
        )
    lines += ["", "Generated 2026-10-01 by `build_pncp_catalogue_v2.py` after the Kaggle reorg into 2 datasets per subject (raw+trusted / analytics)."]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kaggle-csv", type=Path, required=True)
    parser.add_argument("--ledger", type=Path, action="append", default=[])
    args = parser.parse_args()
    kaggle = load_kaggle_csv(args.kaggle_csv)
    ledgers = load_ledgers(args.ledger)
    catalogue = build(kaggle, ledgers)
    (ROOT / "sources" / "pncp_kaggle_catalogue.json").write_text(
        json.dumps(catalogue, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (ROOT / "docs" / "pncp-kaggle-catalogue.md").write_text(render_markdown(catalogue), encoding="utf-8")
    print(json.dumps({k: catalogue[k] for k in ("datasets", "published", "missing", "rows_published_known", "rows_unknown_count")}))


if __name__ == "__main__":
    main()
