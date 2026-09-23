from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs" / "assets" / "pncp-backfill-flow.png"
NAVY = "#003366"
BLUE = "#006699"
TEAL = "#4A90A4"
LIGHT = "#E8F0F5"
GREEN = "#2E8B57"
GREY = "#5C6770"


def box(axis, x, y, label, color=LIGHT):
    axis.add_patch(FancyBboxPatch((x, y), 2.55, 1.05, boxstyle="round,pad=0.08", linewidth=1.3, edgecolor=NAVY, facecolor=color))
    axis.text(x + 1.275, y + 0.525, label, ha="center", va="center", fontsize=9.2, color=NAVY, wrap=True, weight="semibold")


def arrow(axis, start, end, color=GREY):
    axis.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=14, linewidth=1.4, color=color))


def main() -> None:
    figure, axis = plt.subplots(figsize=(13.5, 5.4))
    figure.patch.set_facecolor("white")
    axis.set_xlim(0, 15)
    axis.set_ylim(0, 6)
    axis.axis("off")
    axis.text(0.35, 5.45, "Checkpointed PNCP backfill", fontsize=18, weight="bold", color=NAVY)
    axis.text(0.35, 5.05, "A local, resumable path from bounded public-source windows to a reviewable release candidate", fontsize=10, color=GREY)

    box(axis, 0.45, 3.1, "Date × modality\nwindow", "#DCEAF2")
    box(axis, 3.35, 3.1, "Official PNCP\npublication route", "#DCEAF2")
    box(axis, 6.25, 3.1, "Normalized local\ncapture (ignored)", "#DCEAF2")
    box(axis, 9.15, 3.1, "Latest update\nper source ID", "#DCEAF2")
    box(axis, 12.05, 3.1, "Privacy-gated\nrelease candidate", "#D8EEE3")
    for x in (3.0, 5.9, 8.8, 11.7):
        arrow(axis, (x, 3.63), (x + 0.28, 3.63))

    box(axis, 6.25, 1.05, "Checkpoint JSON\ncompleted windows\n(day:modality)", "#FFF3DD")
    arrow(axis, (7.52, 3.05), (7.52, 2.16), BLUE)
    arrow(axis, (6.2, 1.58), (1.78, 3.0), BLUE)
    axis.text(0.45, 0.35, "The command writes no publication and no data is committed to the repository. Review coverage, terms, schema, audit, and manifest before distribution.", fontsize=9.2, color=GREY)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(OUTPUT, dpi=200, bbox_inches="tight", facecolor="white")


if __name__ == "__main__":
    main()
