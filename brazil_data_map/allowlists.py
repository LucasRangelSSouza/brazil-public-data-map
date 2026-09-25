from __future__ import annotations

from typing import Any


# Public release fields only. Input-only identifiers may be used by the privacy
# policy and never reach a written layer.
PUBLIC_FIELDS: dict[str, frozenset[str]] = {
    "pncp": frozenset({
        "id", "updated_at", "published_at", "procurement_year",
        "procurement_sequence", "item", "modality_id", "estimated_value",
        "contracting_organization_id", "contracting_organization_name",
    }),
    "fnde-siope": frozenset({
        "id", "year", "municipality_code", "state_code", "population",
        "revenue_realized", "education_expenditure_paid",
    }),
}


def apply_public_allowlist(records: list[dict[str, Any]], source_id: str) -> list[dict[str, Any]]:
    """Keep only fields approved for a public source release."""
    allowed = PUBLIC_FIELDS.get(source_id)
    if allowed is None:
        raise ValueError(f"no public field allowlist for source: {source_id}")
    return [{key: value for key, value in record.items() if key in allowed or key == "supplier_document"} for record in records]
