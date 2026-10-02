"""Cover images for the Kaggle datasets, one per source and kind. Output: datamap/covers/<slug>.png (1280x640)."""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "datamap" / "covers"
COLORS = {"raw": "#f0a04b", "trusted": "#4fd1c5", "semantic": "#9aa0ff"}


def main() -> None:
    cat = json.loads((ROOT / "datamap" / "data" / "catalog.json").read_text(encoding="utf-8"))
    OUT.mkdir(parents=True, exist_ok=True)
    for ds in cat["datasets"]:
        info = cat["subjects"][ds["subject"]]
        fig = plt.figure(figsize=(12.8, 6.4), dpi=100, facecolor="#0f1013")
        ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 1280); ax.set_ylim(0, 640); ax.axis("off")
        layers = sorted({t["layer"] for t in ds["tables"]}, key=["raw", "trusted", "semantic"].index)
        for i, layer in enumerate(["raw", "trusted", "semantic"]):
            on = layer in layers
            ax.add_patch(FancyBboxPatch((90 + i * 140, 500 - i * 50), 110, 90, boxstyle="round,pad=0,rounding_size=18", fc=COLORS[layer] if on else "#23252b", ec="none", alpha=1 if on else .6))
            ax.text(145 + i * 140, 545 - i * 50, layer, ha="center", va="center", fontsize=15, fontweight="bold", color="#0f1013" if on else "#6a6d75")
        ax.text(90, 330, info["title"], fontsize=44, fontweight="bold", color="#ece8dd", va="center")
        ax.text(90, 262, ("Analytics layer" if ds["kind"] == "analytics" else "Raw and trusted layers") + (f" · part {ds['slug'].rsplit('-', 1)[1]}" if "-part-" in ds["slug"] else ""), fontsize=24, color="#9a958a", va="center")
        ax.text(90, 150, f"{ds['table_count']} tables · {ds['rows']:,} rows · documented to the column", fontsize=22, color="#ece8dd", va="center")
        ax.text(90, 100, info["publisher"][:78], fontsize=15, color="#9a958a", va="center")
        ax.text(90, 52, "Brazil Public Data Map · rangeltech.net/datamap", fontsize=15, color="#7aa2ff", va="center")
        fig.savefig(OUT / f"{ds['slug']}.png", facecolor=fig.get_facecolor())
        plt.close(fig)
    print("covers", len(cat["datasets"]))


if __name__ == "__main__":
    main()
