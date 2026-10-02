"""Write the generated page, tags, provenance, file descriptions and column descriptors onto every Kaggle dataset.
Metadata only: no data file is touched. (`kaggle datasets version` replaces the whole file set, so it must not be used for this.)

Usage: python scripts/push_kaggle_metadata.py [--no-covers] [slug ...]     (Kaggle CLI logged in as the dataset owner)
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OWNER = "lucasrangelss"
TYPES = {"STRING": "string", "INT64": "integer", "INTEGER": "integer", "FLOAT64": "number", "FLOAT": "number", "NUMERIC": "number", "BIGNUMERIC": "number",
         "BOOL": "boolean", "BOOLEAN": "boolean", "DATE": "datetime", "DATETIME": "datetime", "TIMESTAMP": "datetime", "TIME": "string"}
COMMON_TAGS = ["brazil", "government"]
SUBJECT_TAGS = {
    "pncp": ["business", "law"], "siope": ["education", "finance"], "fundeb": ["education", "finance"], "fnde-salario-educacao": ["education", "finance"],
    "censo-escolar": ["education"], "saeb": ["education"], "ideb": ["education"], "ica": ["education"], "taxas-rendimento": ["education"],
    "ibge": ["geography"], "qedu": ["education"],
}
FILE_NOTES = {
    "README.md": "What this dataset contains and how it is organised.",
    "DATA_DICTIONARY.md": "Field-by-field dictionary of every table in this dataset.",
    "release_manifest.json": "SHA-256 and size of every file, row counts per table and the snapshot date.",
    "schemas.json": "Schema (column names and types) of every table.",
    "audit.json": "Export counts per table: rows scanned and rows released.",
}


def kaggle(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, "-m", "kaggle", *args], capture_output=True, text=True, encoding="utf-8", errors="replace")


def resources(ds: dict) -> list[dict]:
    out = []
    for t in ds["tables"]:
        out.append({"path": t["file"], "description": f"{t['layer']} table `{t['table']}`. {t['description'][:600]}".strip(),
                    "schema": {"fields": [{"name": c["name"], "description": (c["description"] or "")[:1000], "type": TYPES.get(c["type"], "string")} for c in t["columns"]]}})
    return out


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    covers = "--no-covers" not in sys.argv
    catalog = json.loads((ROOT / "datamap" / "data" / "catalog.json").read_text(encoding="utf-8"))
    for ds in catalog["datasets"]:
        slug = ds["slug"]
        if args and slug not in args:
            continue
        info = catalog["subjects"][ds["subject"]]
        with tempfile.TemporaryDirectory() as tmp:
            got = kaggle("datasets", "metadata", f"{OWNER}/{slug}", "-p", tmp)
            path = Path(tmp) / "dataset-metadata.json"
            if not path.exists():
                print(slug, "FAILED to read metadata:", (got.stdout + got.stderr)[-200:])
                continue
            meta = json.loads(path.read_text(encoding="utf-8"))
            meta_info = meta["info"]
            meta_info["description"] = (ROOT / "datamap" / "kaggle_metadata" / f"{slug}.md").read_text(encoding="utf-8")
            meta_info["subtitle"] = f"{ds['table_count']} tables, {ds['rows']:,} rows, documented to the column"[:80]
            meta_info["keywords"] = COMMON_TAGS + SUBJECT_TAGS.get(ds["subject"], [])
            meta_info["expectedUpdateFrequency"] = "never"  # each dataset is a dated snapshot; a refresh is published as a new version
            meta_info["userSpecifiedSources"] = f"{info['publisher']}: {info['official_url']}"
            meta_info["resources"] = resources(ds)
            cover = ROOT / "datamap" / "covers" / f"{slug}.png"
            if covers and cover.exists():
                shutil.copyfile(cover, Path(tmp) / "cover.png")
                meta_info["image"] = "cover.png"
            path.write_text(json.dumps(meta), encoding="utf-8")
            done = kaggle("datasets", "metadata", f"{OWNER}/{slug}", "-p", tmp, "--update")
            print(slug, "ok" if done.returncode == 0 else "FAILED", (done.stdout + done.stderr).strip()[-300:].replace("\n", " | "))


if __name__ == "__main__":
    main()
