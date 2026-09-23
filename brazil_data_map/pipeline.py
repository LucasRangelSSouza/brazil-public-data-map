from __future__ import annotations

import json
from pathlib import Path
import hashlib
from typing import Any

import pyarrow as pa
import pyarrow.parquet as pq

from .audit import audit_release_layers
from .layers import build_layers, validate_layers
from .quality import validate_reconciliation
from .release import build_manifest


def build_public_release(
    records: list[dict[str, Any]],
    output_root: Path,
    source_id: str,
    source_url: str,
    retrieved_at: str | None = None,
    git_commit: str | None = None,
    distribution_version: str | None = None,
) -> dict[str, Any]:
    """Build a locally reviewable release candidate from approved source records."""
    layers = build_layers(records, source_id)
    validate_layers(layers)
    validate_reconciliation(layers)
    audit = audit_release_layers(layers)

    release_files: list[Path] = []
    for layer, layer_records in layers.items():
        destination = output_root / layer / "records.parquet"
        destination.parent.mkdir(parents=True, exist_ok=True)
        pq.write_table(pa.Table.from_pylist(layer_records), destination, compression="zstd", version="2.6")
        release_files.append(destination)

    audit_path = output_root / "privacy-audit.json"
    audit_path.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    release_files.append(audit_path)
    manifest = build_manifest(
        output_root,
        source_id,
        source_url,
        {"privacy_gate": audit["privacy_gate"]},
        retrieved_at=retrieved_at,
        files=release_files,
        source_input_sha256=hashlib.sha256(
            json.dumps(records, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
        ).hexdigest(),
        row_counts=audit["record_counts"],
        git_commit=git_commit,
        distribution_version=distribution_version,
    )
    (output_root / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return {"layers": layers, "audit": audit, "manifest": manifest}
