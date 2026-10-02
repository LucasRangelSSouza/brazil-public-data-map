"""Publish one public quickstart notebook per Kaggle dataset, attached to it (a public notebook is part of Kaggle's credibility score).

Each notebook reads the dataset's own manifest, lists its tables, verifies a few files against the SHA-256 recorded in the manifest and
reads the smallest table. Usage: python scripts/push_kaggle_notebooks.py [slug ...]   (Kaggle CLI logged in as the dataset owner)
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OWNER = "lucasrangelss"
MAP = "https://lucas.rangeltech.net/datamap/"
REPO = "https://github.com/LucasRangelSSouza/brazil-public-data-map"


def md(t): return {"cell_type": "markdown", "metadata": {}, "source": t.strip("\n").splitlines(True)}
def code(t): return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": t.strip("\n").splitlines(True)}


def notebook(ds: dict, info: dict) -> dict:
    slug = ds["slug"]
    cells = [
        md(f"# Quickstart: {ds['title']}\n\n{info['summary']}\n\n**Source:** {info['publisher']}, <{info['official_url']}>  \n**Grain and keys:** {info['grain']}\n\n"
           f"This notebook lists the {ds['table_count']} tables of the dataset, verifies files against the SHA-256 in `release_manifest.json` and reads the smallest table. "
           f"Every column is described in the [data map]({MAP}#/dataset/{slug}) and in the [data dictionary]({REPO}/blob/main/docs/datamap/{slug}.md)."),
        code(f'''
import json, hashlib
from pathlib import Path
import pandas as pd

root = Path("/kaggle/input/{slug}")
manifest = json.loads((root / "release_manifest.json").read_text(encoding="utf-8"))
tables = pd.DataFrame(manifest["tables"])
print(manifest["snapshot_date"], "|", len(tables), "tables |", f"{{tables.rows.sum():,}} rows")
tables.sort_values("rows", ascending=False).head(20)
'''),
        md("## Verify files against the manifest\n\nThe manifest records the size and SHA-256 of every file. Check the three smallest data files (checking all of them is the same loop)."),
        code('''
def sha256(path, block=8 << 20):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(block), b""):
            h.update(chunk)
    return h.hexdigest()

data_files = sorted((f for f in manifest["files"] if f["path"].endswith(".parquet")), key=lambda f: f["bytes"])[:3]
for f in data_files:
    ok = sha256(root / f["path"]) == f["sha256"]
    print("OK " if ok else "BAD", f["path"], f"{f['bytes']:,} bytes")
'''),
        md("## Read the smallest table"),
        code('''
smallest = data_files[0]["path"]
df = pd.read_parquet(root / smallest)
print(smallest, df.shape)
df.head()
'''),
        md(f"## Next\n\nOpen the [interactive map]({MAP}#/dataset/{slug}) to see lineage and the keys that join this dataset to the others. The notebook that shows how the raw layer is obtained from the official source is "
           f"[`notebooks/sources/{info.get('notebook', ds['subject'])}.ipynb`]({REPO}/blob/main/notebooks/sources/{info.get('notebook', ds['subject'])}.ipynb)."),
    ]
    return {"cells": cells, "nbformat": 4, "nbformat_minor": 5, "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}, "language_info": {"name": "python"}}}


def main() -> None:
    wanted = set(sys.argv[1:])
    cat = json.loads((ROOT / "datamap" / "data" / "catalog.json").read_text(encoding="utf-8"))
    for ds in cat["datasets"]:
        slug = ds["slug"]
        if wanted and slug not in wanted:
            continue
        info = cat["subjects"][ds["subject"]]
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            (tmp / "quickstart.ipynb").write_text(json.dumps(notebook(ds, info)), encoding="utf-8")
            # Kaggle caps titles at 50 characters and derives the notebook slug from the title.
            short = slug.replace("salario-educacao", "salario-edu") if len(f"Quickstart {slug}") > 50 else slug
            title = f"Quickstart {short}"
            (tmp / "kernel-metadata.json").write_text(json.dumps({
                "id": f"{OWNER}/quickstart-{short}", "title": title, "code_file": "quickstart.ipynb", "language": "python", "kernel_type": "notebook",
                "is_private": "false", "enable_gpu": "false", "enable_internet": "false", "dataset_sources": [f"{OWNER}/{slug}"], "competition_sources": [], "kernel_sources": [], "model_sources": [],
            }), encoding="utf-8")
            r = subprocess.run([sys.executable, "-m", "kaggle", "kernels", "push", "-p", str(tmp)], capture_output=True, text=True, encoding="utf-8", errors="replace")
            out = (r.stdout + r.stderr).strip()
            print(slug, "ok" if r.returncode == 0 else "FAILED", out[-220:].replace("\n", " | "), flush=True)
            if "429" in out:  # Kaggle is rate limiting public notebooks for this account: stop instead of hammering the API
                print("stopped on HTTP 429; run again later")
                break


if __name__ == "__main__":
    main()
