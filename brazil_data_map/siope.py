"""Municipality-year education finance from the public FNDE SIOPE OData service.

SIOPE identifies municipalities by the six-digit IBGE code without its check
digit. The IBGE locality API supplies the seven-digit code, name, and state used
as the join vocabulary for every other source in this repository.
"""

from __future__ import annotations

import gzip
import json
from pathlib import Path
import time
from typing import Any, Callable, Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

SIOPE_ODATA_URL = "https://www.fnde.gov.br/olinda-ide/servico/DADOS_ABERTOS_SIOPE/versao/v1/odata"
IBGE_MUNICIPALITIES_URL = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios"
ANNUAL_PERIOD = 6  # sixth bimester: the full-year declaration
STATES = (
    "AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", "MG", "MS", "MT", "PA",
    "PB", "PE", "PI", "PR", "RJ", "RN", "RO", "RR", "RS", "SC", "SE", "SP", "TO",
)
GENERAL_FIELDS = ("TIPO", "NUM_ANO", "COD_MUNI", "NUM_POPU", "VAL_RECE_REAL", "VAL_DESP_PAGA", "DAT_DECL")

# Statutory and comparative indicators kept in release v0.1, keyed by SIOPE COD_INDI.
INDICATORS: dict[int, str] = {
    24: "mde_minimum_share_pct",
    67: "fundeb_remuneration_share_pct",
    27: "fundeb_unspent_share_pct",
    35: "education_share_of_total_expenditure_pct",
    56: "investment_per_basic_education_student",
}
GZIP_MAGIC = bytes((0x1F, 0x8B))

Opener = Callable[..., Any]


def get_json(url: str, retries: int = 3, opener: Opener = urlopen, sleeper: Callable[[float], None] = time.sleep) -> Any:
    request = Request(url, headers={"Accept": "application/json", "User-Agent": "brazil-public-data-map/0.2"})
    for attempt in range(retries + 1):
        try:
            with opener(request, timeout=120) as response:
                body = response.read()
            # The IBGE service can gzip a response that did not request it.
            if body[:2] == GZIP_MAGIC:
                body = gzip.decompress(body)
            return json.loads(body.decode("utf-8"))
        except (HTTPError, URLError, TimeoutError, json.JSONDecodeError, UnicodeDecodeError) as error:
            if attempt == retries:
                raise RuntimeError(f"public source request failed after {retries + 1} attempts: {url.split('?')[0]}") from error
            sleeper(min(2 ** attempt, 16))
    raise AssertionError("unreachable")


def _function_url(function: str, year: int, state: str, select: Iterable[str], extra_filter: str | None = None) -> str:
    query = (
        f"@Ano_Consulta={year}&@Num_Peri={ANNUAL_PERIOD}&@Sig_UF='{state}'"
        f"&$format=json&$select={','.join(select)}"
    )
    if extra_filter:
        query += "&$filter=" + quote(extra_filter)
    return f"{SIOPE_ODATA_URL}/{function}(Ano_Consulta=@Ano_Consulta,Num_Peri=@Num_Peri,Sig_UF=@Sig_UF)?{query}"


def fetch_state_year(year: int, state: str, fetch: Callable[[str], Any] = get_json) -> list[dict[str, Any]]:
    """Return one normalized capture row per municipality declaration for a state-year."""
    general = fetch(_function_url("Dados_Gerais_Siope", year, state, GENERAL_FIELDS, "TIPO eq 'Municipal'"))["value"]
    indicator_filter = "TIPO eq 'Municipal' and (" + " or ".join(f"COD_INDI eq {code}" for code in INDICATORS) + ")"
    indicators = fetch(_function_url("Indicadores_Siope", year, state, ("COD_MUNI", "COD_INDI", "VAL_INDI"), indicator_filter))["value"]
    by_municipality: dict[int, dict[str, Any]] = {}
    for row in indicators:
        by_municipality.setdefault(row["COD_MUNI"], {})[INDICATORS[row["COD_INDI"]]] = row["VAL_INDI"]
    return [
        {
            "state": state,
            "year": row["NUM_ANO"],
            "siope_municipality_code": row["COD_MUNI"],
            "population": row["NUM_POPU"],
            "total_revenue_realized": row["VAL_RECE_REAL"],
            "total_expenditure_paid": row["VAL_DESP_PAGA"],
            "declared_at": row["DAT_DECL"],
            "indicators": by_municipality.get(row["COD_MUNI"], {}),
        }
        for row in general
    ]


def _state_of(row: dict[str, Any]) -> str:
    micro = row.get("microrregiao")
    if micro:
        return micro["mesorregiao"]["UF"]["sigla"]
    return row["regiao-imediata"]["regiao-intermediaria"]["UF"]["sigla"]


def fetch_municipality_reference(fetch: Callable[[str], Any] = get_json) -> list[dict[str, Any]]:
    return [
        {"municipality_code": str(row["id"]), "municipality_name": row["nome"], "state_code": _state_of(row)}
        for row in fetch(IBGE_MUNICIPALITIES_URL)
    ]


def capture(
    years: Iterable[int],
    output_dir: Path,
    states: Iterable[str] = STATES,
    fetch: Callable[[str], Any] = get_json,
) -> dict[str, Any]:
    """Write a resumable local capture: one JSONL file per state-year plus the IBGE reference."""
    output_dir.mkdir(parents=True, exist_ok=True)
    reference_path = output_dir / "ibge-municipalities.json"
    if not reference_path.exists():
        reference_path.write_text(json.dumps(fetch_municipality_reference(fetch), ensure_ascii=False, sort_keys=True), encoding="utf-8")
    fetched = skipped = 0
    for year in years:
        for state in states:
            path = output_dir / f"siope-{year}-{state}.jsonl"
            if path.exists():
                skipped += 1
                continue
            rows = fetch_state_year(year, state, fetch)
            partial = path.with_suffix(".partial")
            partial.write_text("".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows), encoding="utf-8")
            partial.replace(path)
            fetched += 1
    return {"fetched_state_years": fetched, "skipped_state_years": skipped, "capture_dir": str(output_dir)}


def _number(value: Any) -> float | None:
    if value in (None, ""):
        return None
    return float(value)


def build_records(capture_dir: Path) -> list[dict[str, Any]]:
    """Join the capture to IBGE codes and keep the latest declaration per municipality-year."""
    reference = json.loads((capture_dir / "ibge-municipalities.json").read_text(encoding="utf-8"))
    by_prefix = {row["municipality_code"][:6]: row for row in reference}
    latest: dict[str, dict[str, Any]] = {}
    unmatched = 0
    for path in sorted(capture_dir.glob("siope-*.jsonl")):
        for line in path.read_text(encoding="utf-8").splitlines():
            row = json.loads(line)
            municipality = by_prefix.get(str(row["siope_municipality_code"]))
            if municipality is None:
                unmatched += 1
                continue
            record_id = f"{municipality['municipality_code']}-{row['year']}"
            record = {
                "id": record_id,
                "updated_at": row["declared_at"],
                "year": int(row["year"]),
                "municipality_code": municipality["municipality_code"],
                "municipality_name": municipality["municipality_name"],
                "state_code": municipality["state_code"],
                "population": row["population"],
                "total_revenue_realized": _number(row["total_revenue_realized"]),
                "total_expenditure_paid": _number(row["total_expenditure_paid"]),
                **{field: _number(row["indicators"].get(field)) for field in INDICATORS.values()},
            }
            if record_id not in latest or str(record["updated_at"]) >= str(latest[record_id]["updated_at"]):
                latest[record_id] = record
    if unmatched:
        raise ValueError(f"{unmatched} SIOPE rows have no IBGE municipality match")
    return [latest[key] for key in sorted(latest)]
