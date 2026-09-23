from __future__ import annotations

import hashlib
import re
from typing import Any


BLOCKING_FIELDS = {"cpf", "email", "phone", "address"}
EXCLUDED_FIELDS = {"supplier_document", "supplier_name", "name"}


def digits(value: object) -> str:
    return re.sub(r"\D", "", str(value))


def classify(document: object) -> str:
    value = digits(document)
    if len(value) == 14:
        return "organization"
    if len(value) == 11:
        return "natural_person"
    return "unknown"


def apply_identifier_policy(records: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    released: list[dict[str, Any]] = []
    excluded = {"natural_person": 0, "unknown": 0}
    released_without_supplier_identifier = 0
    for record in records:
        forbidden = BLOCKING_FIELDS & record.keys()
        if forbidden:
            raise ValueError(f"direct identifier field blocks release: {sorted(forbidden)[0]}")
        if "supplier_document" not in record:
            sanitized = {key: value for key, value in record.items() if key not in EXCLUDED_FIELDS}
            sanitized["identifier_classification"] = "not_present"
            released.append(sanitized)
            released_without_supplier_identifier += 1
            continue
        classification = classify(record["supplier_document"])
        if classification != "organization":
            excluded[classification] += 1
            continue
        normalized = digits(record["supplier_document"])
        sanitized = {key: value for key, value in record.items() if key not in EXCLUDED_FIELDS}
        sanitized["identifier_classification"] = classification
        sanitized["golden_organization_id"] = hashlib.sha256(f"cnpj:{normalized}".encode()).hexdigest()
        released.append(sanitized)
    return released, {
        "excluded_by_classification": excluded,
        "released_organizations": sum(record["identifier_classification"] == "organization" for record in released),
        "released_without_supplier_identifier": released_without_supplier_identifier,
    }
