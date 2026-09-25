from __future__ import annotations

from typing import Any
import unicodedata


# Public release fields only. Input-only identifiers may be used by the privacy
# policy and never reach a written layer.
PUBLIC_FIELDS: dict[str, frozenset[str]] = {
    "pncp": frozenset({
        "id", "updated_at", "published_at", "procurement_year",
        "procurement_sequence", "procurement_category", "modality_id", "estimated_value",
        "contracting_organization_id", "contracting_organization_name",
    }),
    "fnde-siope": frozenset({
        "id", "year", "municipality_code", "state_code", "population",
        "revenue_realized", "education_expenditure_paid",
    }),
}


def procurement_category(subject: object) -> str:
    """Map a notice subject to a small, non-identifying public taxonomy."""
    normalized = unicodedata.normalize("NFKD", str(subject or "")).encode("ascii", "ignore").decode("ascii").casefold()
    categories = {
        "education": ("educacao", "escola", "ensino", "livro", "didatic", "aluno"),
        "health": ("saude", "hospital", "medic", "farmac", "odont"),
        "technology": ("software", "computador", "informat", "tecnolog", "internet"),
        "works_and_maintenance": ("obra", "construc", "reforma", "manutenc", "engenharia"),
        "transport": ("veiculo", "transporte", "combust", "pneu"),
    }
    for category, keywords in categories.items():
        if any(keyword in normalized for keyword in keywords):
            return category
    return "other"


def apply_public_allowlist(records: list[dict[str, Any]], source_id: str) -> list[dict[str, Any]]:
    """Keep only fields approved for a public source release."""
    allowed = PUBLIC_FIELDS.get(source_id)
    if allowed is None:
        raise ValueError(f"no public field allowlist for source: {source_id}")
    approved: list[dict[str, Any]] = []
    for record in records:
        item = {key: value for key, value in record.items() if key in allowed or key == "supplier_document"}
        if source_id == "pncp":
            item["procurement_category"] = procurement_category(record.get("item"))
        approved.append(item)
    return approved
