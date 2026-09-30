"""Build the global PNCP Kaggle catalogue from the per-dataset release manifests.

Input: the publication plan and a directory of verified per-dataset `release_manifest.json` files
(named `<dataset-slug>.release_manifest.json`).
Output: `sources/pncp_kaggle_catalogue.json` and `docs/pncp-kaggle-catalogue.md`.

Every planned table-layer appears exactly once, with one state: `published` (manifest present) or
`pending`. Nothing is omitted silently.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OWNER = "lucasrangelss"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def build(plan: dict, manifests: dict[str, dict], hashes: dict[str, str]) -> dict:
    entries = []
    for subject in plan["subjects"]:
        for dataset in subject["datasets"]:
            slug = dataset["kaggle_slug"]
            manifest = manifests.get(slug)
            by_key = {(t["table_id"], t["layer"]): t for t in (manifest or {}).get("tables", [])}
            file_hash = {f["path"]: f["sha256"] for f in (manifest or {}).get("files", [])}
            for planned in dataset["table_layers"]:
                key = (planned["table_id"], planned["layer"])
                row = by_key.get(key)
                entry = {
                    "subject": subject["subject_id"],
                    "dataset": f"{OWNER}/{slug}",
                    "dataset_url": f"https://www.kaggle.com/datasets/{OWNER}/{slug}",
                    "kind": dataset["kind"],
                    "table_id": planned["table_id"],
                    "layer": planned["layer"],
                    "state": "published" if row else "pending",
                }
                if row:
                    entry.update({
                        "source_endpoint": row["source_endpoint"],
                        "data_cutoff": row["data_cutoff"],
                        "row_count": row["row_count"],
                        "parquet_path": row["parquet_path"],
                        "parquet_sha256": file_hash.get(row["parquet_path"]),
                        "schema_path": row["schema_path"],
                        "schema_sha256": row["schema_sha256"],
                        "privacy_audit_path": row["privacy_audit_path"],
                        "release_manifest_sha256": hashes[slug],
                        "semantic_vectors": planned["table_id"] in {"obt_pncp_editais_semantico", "pncp_editais_embeddings"},
                    })
                entries.append(entry)
    published = [e for e in entries if e["state"] == "published"]
    return {
        "schema_version": "1.0",
        "data_cutoff": plan["data_cutoff"],
        "table_layers": len(entries),
        "published": len(published),
        "pending": len(entries) - len(published),
        "rows_published": sum(e["row_count"] for e in published),
        "entries": entries,
    }


def render_markdown(catalogue: dict) -> str:
    lines = [
        "# PNCP Kaggle catalogue",
        "",
        f"Cutoff: `{catalogue['data_cutoff']}`. {catalogue['published']} of {catalogue['table_layers']} table-layer files are published; "
        f"{catalogue['pending']} are pending. Each dataset ships a `release_manifest.json` with the SHA-256 of every file.",
        "",
        "| Subject | Layer | Table | Dataset | Rows | Parquet SHA-256 | State |",
        "|---|---|---|---|---:|---|---|",
    ]
    for e in catalogue["entries"]:
        rows = f"{e['row_count']:,}" if "row_count" in e else "-"
        digest = f"`{e['parquet_sha256'][:12]}`" if e.get("parquet_sha256") else "-"
        lines.append(f"| {e['subject']} | {e['layer']} | `{e['table_id']}` | [{e['dataset'].split('/')[1]}]({e['dataset_url']}) | {rows} | {digest} | {e['state']} |")
    lines += ["", "Values are published exactly as held in the snapshot. The PNCP source can change after the cutoff; the manifest identifies the snapshot."]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--plan", type=Path, default=ROOT / "sources" / "pncp_publication_plan.json")
    parser.add_argument("--manifests", type=Path, required=True)
    args = parser.parse_args()
    plan = json.loads(args.plan.read_text(encoding="utf-8"))
    manifests, hashes = {}, {}
    for path in sorted(args.manifests.glob("*.release_manifest.json")):
        slug = path.name.removesuffix(".release_manifest.json")
        manifests[slug] = json.loads(path.read_text(encoding="utf-8"))
        hashes[slug] = sha256_bytes(path.read_bytes())
    catalogue = build(plan, manifests, hashes)
    (ROOT / "sources" / "pncp_kaggle_catalogue.json").write_text(json.dumps(catalogue, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (ROOT / "docs" / "pncp-kaggle-catalogue.md").write_text(render_markdown(catalogue), encoding="utf-8")
    print(json.dumps({k: catalogue[k] for k in ("table_layers", "published", "pending", "rows_published")}))


if __name__ == "__main__":
    main()
