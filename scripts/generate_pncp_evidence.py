from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


NAVY = "#003366"
BLUE = "#006699"
LIGHT = "#E8F0F5"
GREEN = "#2E8B57"
GREY = "#5F6B76"


def metric(ax, x, label, value, color):
    ax.add_patch(FancyBboxPatch((x, 1.45), 2.5, 1.85, boxstyle="round,pad=0.03,rounding_size=0.1", linewidth=1.5, edgecolor=color, facecolor=LIGHT))
    ax.text(x + 1.25, 2.65, label, ha="center", va="center", fontsize=10, color=GREY)
    ax.text(x + 1.25, 2.05, value, ha="center", va="center", fontsize=28, color=NAVY, fontweight="bold")


def main() -> None:
    figure, axis = plt.subplots(figsize=(12, 4.5), dpi=200)
    figure.patch.set_facecolor("white")
    axis.set_xlim(0, 12)
    axis.set_ylim(0, 4.5)
    axis.axis("off")
    axis.text(0.55, 3.95, "PNCP publication adapter: local evidence", color=NAVY, fontsize=19, fontweight="bold")
    axis.text(0.55, 3.52, "2026-09-23 · one publication date · modality code 6 · official public endpoint", color=GREY, fontsize=9.5)
    metric(axis, 0.75, "Raw records", "25", BLUE)
    metric(axis, 4.75, "Trusted records", "25", BLUE)
    metric(axis, 8.75, "Semantic records", "25", BLUE)
    ax = axis
    ax.add_patch(FancyBboxPatch((0.75, 0.42), 10.5, 0.55, boxstyle="round,pad=0.03,rounding_size=0.08", linewidth=1.2, edgecolor=GREEN, facecolor="#F4FBF6"))
    ax.text(6.0, 0.69, "Privacy audit: passed · 0 reported violations · bounded access check only", ha="center", va="center", color=GREEN, fontsize=10.5, fontweight="bold")
    output = Path("docs/evidence/pncp-publication-run-2026-09-23.png")
    output.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(output, bbox_inches="tight", facecolor="white")


if __name__ == "__main__":
    main()
