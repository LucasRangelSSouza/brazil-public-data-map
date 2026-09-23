from __future__ import annotations

from datetime import datetime
from typing import Any


REQUIRED_FIELDS = {"id", "updated_at"}


def validate_records(records: list[dict[str, Any]]) -> None:
    seen: set[str] = set()
    for index, record in enumerate(records):
        missing = sorted(REQUIRED_FIELDS - record.keys())
        if missing:
            raise ValueError(f"record {index} missing required fields: {', '.join(missing)}")
        record_id = record["id"]
        if not isinstance(record_id, str) or not record_id:
            raise ValueError(f"record {index} has an invalid id")
        if record_id in seen:
            raise ValueError(f"duplicate id: {record_id}")
        seen.add(record_id)
        try:
            datetime.fromisoformat(str(record["updated_at"]).replace("Z", "+00:00"))
        except ValueError as error:
            raise ValueError(f"record {index} has an invalid updated_at timestamp") from error


def validate_reconciliation(layers: dict[str, list[dict[str, Any]]]) -> None:
    raw = layers["raw"]
    trusted = layers["trusted"]
    semantic = layers["semantic"]
    if len(trusted) > len(raw):
        raise ValueError("trusted layer cannot contain more records than raw")
    if len(semantic) != len(trusted):
        raise ValueError("semantic and trusted layer counts must match")
    validate_records(raw)
    validate_records(trusted)
    validate_records(semantic)
