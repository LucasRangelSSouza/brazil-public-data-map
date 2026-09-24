from __future__ import annotations

from copy import deepcopy
from datetime import date
import json
from typing import Any, Callable
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


PNCP_PUBLICATIONS_URL = "https://pncp.gov.br/api/consulta/v1/contratacoes/publicacao"


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
        "procurement_year": record.get("anoCompra"),
        "procurement_sequence": record.get("sequencialCompra"),
        "item": record.get("objetoCompra"),
        "modality_id": record.get("modalidadeId"),
        "estimated_value": record.get("valorTotalEstimado"),
        "contracting_organization_id": organization.get("cnpj"),
        "contracting_organization_name": organization.get("razaoSocial"),
        "source_record_url": record.get("linkSistemaOrigem"),
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
