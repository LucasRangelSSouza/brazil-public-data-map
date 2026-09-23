from __future__ import annotations

import re
from typing import Any


PROHIBITED_KEYS = {"address", "cpf", "email", "phone", "supplier_document", "supplier_name", "name"}
CPF_PATTERN = re.compile(r"(?<!\d)\d{3}[.\s-]?\d{3}[.\s-]?\d{3}[-\s]?\d{2}(?!\d)")
EMAIL_PATTERN = re.compile(r"\b[^\s@]+@[^\s@]+\.[^\s@]+\b")


def audit_release_layers(layers: dict[str, list[dict[str, Any]]]) -> dict[str, Any]:
    violations: list[str] = []
    record_counts: dict[str, int] = {}
    for layer, records in layers.items():
        record_counts[layer] = len(records)
        for index, record in enumerate(records):
            for key, value in record.items():
                if key.casefold() in PROHIBITED_KEYS:
                    violations.append(f"{layer}[{index}].{key}")
                if isinstance(value, str) and (CPF_PATTERN.search(value) or EMAIL_PATTERN.search(value)):
                    violations.append(f"{layer}[{index}].{key}: direct identifier-like value")
    if violations:
        raise ValueError(f"privacy audit failed: {', '.join(violations)}")
    return {"privacy_gate": "passed", "record_counts": record_counts, "violations": []}
