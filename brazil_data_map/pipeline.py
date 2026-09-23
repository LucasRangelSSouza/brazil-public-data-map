from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .audit import audit_release_layers
from .layers import build_layers, validate_layers
from .release import build_manifest


def build_public_release(
    records: list[dict[str, Any]],
    output_root: Path,
    source_id: str,
    source_url: str,
) -> dict[str, Any]:
    """Build a locally reviewable release candidate from approved source records."""
    layers = build_layers(records, source_id)
    validate_layers(layers)
    audit = audit_release_layers(layers)

    for layer, layer_records in layers.items():
        destination = output_root / layer / "records.json"
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(json.dumps(layer_records, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    audit_path = output_root / "privacy-audit.json"
    audit_path.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    manifest = build_manifest(output_root, source_id, source_url, {"privacy_gate": audit["privacy_gate"]})
    (output_root / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return {"layers": layers, "audit": audit, "manifest": manifest}
