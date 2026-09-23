from __future__ import annotations

from copy import deepcopy
from typing import Any

from .audit import audit_release_layers
from .privacy import apply_identifier_policy


def build_layers(records: list[dict[str, Any]], source_id: str) -> dict[str, list[dict[str, Any]]]:
    released, _ = apply_identifier_policy(records)
    raw = [{**record, "source_id": source_id} for record in released]
    trusted = sorted(deepcopy(released), key=lambda item: item["id"])
    semantic = [{**item, "natural_key": item["id"]} for item in trusted]
    return {"raw": raw, "trusted": trusted, "semantic": semantic}


def validate_layers(layers: dict[str, list[dict[str, Any]]]) -> None:
    if set(layers) != {"raw", "trusted", "semantic"}:
        raise ValueError("release requires raw, trusted, and semantic layers")
    for layer, records in layers.items():
        for record in records:
            if "supplier_document" in record or "supplier_name" in record:
                raise ValueError(f"direct supplier field in {layer}")
    if any("natural_key" not in record for record in layers["semantic"]):
        raise ValueError("semantic layer requires natural_key")
    audit_release_layers(layers)
