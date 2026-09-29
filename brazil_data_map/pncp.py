from __future__ import annotations

from copy import deepcopy
from datetime import date
from decimal import Decimal, InvalidOperation
import json
from typing import Any, Callable
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from .allowlists import procurement_category
from .privacy import redact_direct_identifiers


PNCP_PUBLICATIONS_URL = "https://pncp.gov.br/api/consulta/v1/contratacoes/publicacao"
PNCP_API_BASE_URL = "https://pncp.gov.br/api/pncp/v1"


def normalize_publication(record: dict[str, Any]) -> dict[str, Any]:
    organization = record.get("orgaoEntidade") or {}
    updated_at = record.get("dataAtualizacaoGlobal") or record.get("dataAtualizacao") or record.get("dataPublicacaoPncp")
    source_id = record.get("numeroControlePNCP")
    if not source_id or not updated_at:
        raise ValueError("PNCP publication requires numeroControlePNCP and an update timestamp")
    return {
        "id": str(source_id),
        "updated_at": str(updated_at),
        "published_at": record.get("dataPublicacaoPncp"),
        "proposal_deadline_at": record.get("dataEncerramentoProposta"),
        "procurement_year": record.get("anoCompra"),
        "procurement_sequence": record.get("sequencialCompra"),
        "item": record.get("objetoCompra"),
        "modality_id": record.get("modalidadeId"),
        "estimated_value": record.get("valorTotalEstimado"),
        "contracting_organization_id": organization.get("cnpj"),
        "contracting_organization_name": organization.get("razaoSocial"),
    }


def fetch_publications(
    start: date,
    end: date,
    modality_id: int,
    page_size: int = 50,
    retries: int = 2,
    opener: Callable[..., object] = urlopen,
    sleeper: Callable[[float], None] = time.sleep,
) -> list[dict[str, Any]]:
    """Retrieve and normalize a public PNCP publication window without credentials."""
    if end < start:
        raise ValueError("end date must not precede start date")
    if page_size < 10:
        raise ValueError("page_size must be at least 10")

    records: list[dict[str, Any]] = []
    page = 1
    while True:
        query = urlencode({
            "dataInicial": start.strftime("%Y%m%d"),
            "dataFinal": end.strftime("%Y%m%d"),
            "codigoModalidadeContratacao": modality_id,
            "pagina": page,
            "tamanhoPagina": page_size,
        })
        request = Request(f"{PNCP_PUBLICATIONS_URL}?{query}", headers={"Accept": "application/json", "User-Agent": "brazil-public-data-map/0.1"})
        for attempt in range(retries + 1):
            try:
                with opener(request, timeout=30) as response:
                    payload = json.loads(response.read().decode("utf-8"))
                break
            except (HTTPError, URLError, json.JSONDecodeError) as error:
                if attempt == retries:
                    raise RuntimeError(f"PNCP publication request failed after {retries + 1} attempts for page {page}") from error
                retry_after = error.headers.get("Retry-After") if isinstance(error, HTTPError) and error.headers else None
                delay = float(retry_after) if retry_after and retry_after.isdigit() else min(2 ** attempt, 8)
                sleeper(delay)

        page_records = payload.get("data")
        if not isinstance(page_records, list):
            raise ValueError("PNCP response must contain a data list")
        records.extend(normalize_publication(record) for record in page_records)
        remaining = payload.get("paginasRestantes")
        if not page_records or remaining in (0, "0", None):
            break
        page += 1
    return records


def _normalize_item(source_id: str, item: dict[str, Any]) -> dict[str, Any]:
    item_number = item.get("numeroItem")
    if isinstance(item_number, bool) or not isinstance(item_number, int) or item_number < 1:
        raise ValueError("PNCP item requires a positive integer numeroItem")
    item_kind = item.get("materialOuServico")
    if item_kind not in {"M", "S"}:
        raise ValueError("PNCP item requires materialOuServico M or S")
    try:
        quantity = Decimal(str(item.get("quantidade")))
    except (InvalidOperation, TypeError, ValueError) as error:
        raise ValueError("PNCP item requires a numeric quantity") from error
    if not quantity.is_finite() or quantity < 0:
        raise ValueError("PNCP item quantity must be non-negative")
    unit = item.get("unidadeMedida")
    if not isinstance(unit, str) or not (normalized_unit := unit.strip()) or len(normalized_unit) > 30:
        raise ValueError("PNCP item unit must be a non-empty string up to 30 characters")
    if redact_direct_identifiers(normalized_unit) != normalized_unit:
        raise ValueError("PNCP item unit contains a direct identifier")
    return {
        "id": f"{source_id}:item:{item_number}",
        "procurement_id": source_id,
        "item_number": item_number,
        "item_kind": item_kind,
        "item_quantity": float(quantity),
        "item_unit": normalized_unit,
        "item_category": procurement_category(item.get("descricao")),
    }


def fetch_procurement_items(
    organization_cnpj: str,
    procurement_year: int,
    procurement_sequence: int,
    source_id: str,
    page_size: int = 50,
    retries: int = 2,
    opener: Callable[..., object] = urlopen,
    sleeper: Callable[[float], None] = time.sleep,
) -> list[dict[str, Any]]:
    """Fetch one procurement's items and discard unbounded source descriptions."""
    if not organization_cnpj.isdigit() or len(organization_cnpj) != 14:
        raise ValueError("organization_cnpj must contain 14 digits")
    if procurement_year < 1 or procurement_sequence < 1:
        raise ValueError("procurement_year and procurement_sequence must be positive")
    if page_size < 10:
        raise ValueError("page_size must be at least 10")

    records: list[dict[str, Any]] = []
    page = 1
    while True:
        query = urlencode({"pagina": page, "tamanhoPagina": page_size})
        url = f"{PNCP_API_BASE_URL}/orgaos/{organization_cnpj}/compras/{procurement_year}/{procurement_sequence}/itens?{query}"
        http_request = Request(url, headers={"Accept": "application/json", "User-Agent": "brazil-public-data-map/0.1"})
        for attempt in range(retries + 1):
            try:
                with opener(http_request, timeout=30) as response:
                    payload = json.loads(response.read().decode("utf-8"))
                break
            except (HTTPError, URLError, json.JSONDecodeError) as error:
                if attempt == retries:
                    raise RuntimeError(f"PNCP item request failed after {retries + 1} attempts for page {page}") from error
                retry_after = error.headers.get("Retry-After") if isinstance(error, HTTPError) and error.headers else None
                delay = float(retry_after) if retry_after and retry_after.isdigit() else min(2 ** attempt, 8)
                sleeper(delay)

        page_items = payload.get("data", payload.get("itens"))
        if not isinstance(page_items, list):
            raise ValueError("PNCP item response must contain a data or itens list")
        records.extend(_normalize_item(source_id, item) for item in page_items)
        remaining = payload.get("paginasRestantes")
        if not page_items or remaining in (0, "0", None):
            break
        page += 1
    return records


def enrich_procurement_items(
    publications: list[dict[str, Any]],
    item_fetcher: Callable[[str, int, int, str], list[dict[str, Any]]] = fetch_procurement_items,
) -> list[dict[str, Any]]:
    """Create an item-grain candidate from normalized procurement publications.

    A parent without the identifiers required by the documented item route blocks the
    candidate. Silent partial enrichment would make its coverage impossible to assess.
    """
    parent_fields = (
        "updated_at", "published_at", "proposal_deadline_at", "procurement_year",
        "procurement_sequence", "modality_id", "estimated_value",
        "contracting_organization_id", "contracting_organization_name",
    )
    records: list[dict[str, Any]] = []
    for parent in publications:
        source_id = parent.get("id")
        organization_id = parent.get("contracting_organization_id")
        if not isinstance(source_id, str) or not source_id:
            raise ValueError("PNCP parent requires an id")
        if not isinstance(organization_id, str) or not organization_id.isdigit() or len(organization_id) != 14:
            raise ValueError(f"PNCP parent {source_id} requires a 14-digit organization id for the item route")
        year, sequence = parent.get("procurement_year"), parent.get("procurement_sequence")
        if isinstance(year, bool) or not isinstance(year, int) or isinstance(sequence, bool) or not isinstance(sequence, int):
            raise ValueError(f"PNCP parent {source_id} requires integer procurement year and sequence")
        for item in item_fetcher(organization_id, year, sequence, source_id):
            record = {field: parent.get(field) for field in parent_fields}
            record.update(item)
            records.append(record)
    return records


def incremental_snapshot(fetch_page: Callable[[str], list[dict[str, Any]]], watermark: str, retries: int = 2):
    raw: list[dict[str, Any]] = []
    while True:
        for attempt in range(retries + 1):
            try:
                page = fetch_page(watermark)
                break
            except RuntimeError:
                if attempt == retries:
                    raise
        if not page:
            break
        raw.extend(deepcopy(page))
        watermark = max(watermark, *(item["updated_at"] for item in page))

    latest: dict[str, dict[str, Any]] = {}
    for item in raw:
        if item["updated_at"] >= latest.get(item["id"], {}).get("updated_at", ""):
            latest[item["id"]] = item
    trusted = [latest[key] for key in sorted(latest)]
    semantic = [{**item, "natural_key": item["id"]} for item in trusted]
    return raw, trusted, semantic, watermark
