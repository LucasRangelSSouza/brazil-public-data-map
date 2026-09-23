from __future__ import annotations

import json
from datetime import date
from pathlib import Path
from typing import Any


REQUIRED_SOURCE_FIELDS = {
    "id",
    "publisher",
    "official_url",
    "grain",
    "refresh",
    "public_release_assessment",
    "accessed_at",
    "coverage",
    "join_keys",
    "terms_note",
}


def load_registry(path: Path) -> dict[str, Any]:
    registry = json.loads(path.read_text(encoding="utf-8"))
    validate_registry(registry)
    return registry


def validate_registry(registry: dict[str, Any]) -> None:
    if registry.get("schema_version") != "1.0":
        raise ValueError("registry schema_version must be 1.0")

    sources = registry.get("sources")
    if not isinstance(sources, list) or not sources:
        raise ValueError("registry requires at least one source")

    seen: set[str] = set()
    for source in sources:
        missing = sorted(REQUIRED_SOURCE_FIELDS - source.keys())
        if missing:
            raise ValueError(f"source missing required fields: {', '.join(missing)}")
        source_id = source["id"]
        if not isinstance(source_id, str) or not source_id:
            raise ValueError("source id must be a non-empty string")
        if source_id in seen:
            raise ValueError(f"duplicate source id: {source_id}")
        seen.add(source_id)
        if not str(source["official_url"]).startswith("https://"):
            raise ValueError(f"source {source_id} must use an HTTPS official URL")
        try:
            date.fromisoformat(source["accessed_at"])
        except (TypeError, ValueError) as error:
            raise ValueError(f"source {source_id} requires an ISO accessed_at date") from error
        if not isinstance(source["join_keys"], list) or not source["join_keys"]:
            raise ValueError(f"source {source_id} requires at least one documented join key")
