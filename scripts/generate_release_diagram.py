from pathlib import Path
import textwrap

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


NAVY = "#003366"
BLUE = "#006699"
TEAL = "#4A90A4"
LIGHT = "#E8F0F5"
ORANGE = "#E8871E"
GREEN = "#2E8B57"
GREY = "#5F6B76"


def box(ax, x, y, width, height, title, detail, color):
    ax.add_patch(FancyBboxPatch((x, y), width, height, boxstyle="round,pad=0.03,rounding_size=0.08", linewidth=1.5, edgecolor=color, facecolor=LIGHT))
    ax.text(x + width / 2, y + height * 0.65, title, ha="center", va="center", color=NAVY, fontsize=12, fontweight="bold")
    ax.text(x + width / 2, y + height * 0.31, textwrap.fill(detail, width=29), ha="center", va="center", color=GREY, fontsize=8.5, linespacing=1.35)


def arrow(ax, start, end, color=BLUE):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=14, linewidth=1.5, color=color))


def main() -> None:
    figure, axis = plt.subplots(figsize=(14, 7), dpi=200)
    axis.set_xlim(0, 14)
    axis.set_ylim(0, 7)
    axis.axis("off")
    figure.patch.set_facecolor("white")

    axis.text(0.4, 6.45, "Public-source release boundary", fontsize=21, color=NAVY, fontweight="bold")
    axis.text(0.4, 6.0, "A portable local pipeline. Distribution remains pending until an independently reviewed release exists.", fontsize=10, color=GREY)

    box(axis, 0.7, 3.85, 3.45, 1.55, "Official sources", "Registry records the official HTTPS endpoint and release assessment.", TEAL)
    box(axis, 5.3, 3.85, 3.45, 1.55, "Local extraction", "Portable incremental job with a checkpoint supplied by the deployer.", BLUE)
    box(axis, 9.9, 3.85, 3.45, 1.55, "Privacy gate", "Organization-only linkage. Direct personal fields and identifier-like values fail.", ORANGE)
    box(axis, 3.0, 1.45, 3.45, 1.55, "Data layers", "Raw, trusted, and semantic layers retain lineage without direct supplier fields.", GREEN)
    box(axis, 7.6, 1.45, 3.45, 1.55, "Release evidence", "Manifest, hashes, audit, and reviewer decision.", NAVY)
    arrow(axis, (4.15, 4.63), (5.3, 4.63))
    arrow(axis, (8.75, 4.63), (9.9, 4.63))
    arrow(axis, (11.62, 3.85), (6.45, 3.0))
    arrow(axis, (6.45, 2.22), (7.6, 2.22))

    axis.add_patch(FancyBboxPatch((1.0, 0.15), 12.0, 0.75, boxstyle="round,pad=0.03,rounding_size=0.08", linewidth=1.2, edgecolor=NAVY, facecolor="#F7FAFC"))
    axis.text(1.3, 0.58, "Boundary", color=NAVY, fontsize=10.5, fontweight="bold")
    axis.text(2.65, 0.58, "No credentials, private infrastructure identifiers, direct supplier documents, personal data, or unreviewed distribution automation.", color=GREY, fontsize=9.5)

    output = Path("docs/assets/public-release-boundary.png")
    output.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(output, bbox_inches="tight", facecolor="white")


if __name__ == "__main__":
    main()
