"""Read the approved municipality aggregate from an INEP synopsis workbook.

The parser deliberately reads only table 1.2, municipality code, and total
basic-education enrolment. It is not a generic Censo Escolar microdata reader.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import re
from typing import Iterable
from xml.etree import ElementTree as ET
import zipfile

import pyarrow.parquet as pq

SHEET_NAME = "1.2"
CODE_COLUMN = "D"
TOTAL_COLUMN = "E"
NS = {"main": "http://schemas.openxmlformats.org/spreadsheetml/2006/main", "rel": "http://schemas.openxmlformats.org/officeDocument/2006/relationships", "pkg": "http://schemas.openxmlformats.org/package/2006/relationships"}


def _plain(value: str) -> str:
    return "".join(character for character in value.upper() if character.isalnum() or character == " ")


def _strings(archive: zipfile.ZipFile) -> list[str]:
    if "xl/sharedStrings.xml" not in archive.namelist():
        return []
    root = ET.fromstring(archive.read("xl/sharedStrings.xml"))
    return ["".join(node.text or "" for node in item.iter(f"{{{NS['main']}}}t")) for item in root]


def _sheet_path(archive: zipfile.ZipFile) -> str:
    workbook = ET.fromstring(archive.read("xl/workbook.xml"))
    sheet = next((item for item in workbook.findall("main:sheets/main:sheet", NS) if item.attrib.get("name") == SHEET_NAME), None)
    if sheet is None:
        raise ValueError(f"approved worksheet {SHEET_NAME} is missing")
    relation_id = sheet.attrib[f"{{{NS['rel']}}}id"]
    relations = ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
    relation = next((item for item in relations if item.attrib.get("Id") == relation_id), None)
    if relation is None:
        raise ValueError(f"worksheet relation for {SHEET_NAME} is missing")
    return "xl/" + relation.attrib["Target"].lstrip("/")


def _cell_value(cell: ET.Element, shared: list[str]) -> str | None:
    value = cell.find("main:v", NS)
    if cell.attrib.get("t") == "inlineStr":
        inline = cell.find("main:is", NS)
        if inline is None:
            return None
        return "".join(node.text or "" for node in inline.iter(f"{{{NS['main']}}}t"))
    if value is None or value.text is None:
        return None
    if cell.attrib.get("t") == "s":
        return shared[int(value.text)]
    return value.text


def extract_enrollment_rows(workbook_path: Path, year: int = 2023, captured_at: str | None = None) -> list[dict[str, object]]:
    """Return approved municipality-year aggregate records from a checked XLSX file."""
    if not zipfile.is_zipfile(workbook_path):
        raise ValueError("INEP workbook is not a valid XLSX ZIP archive")
    with zipfile.ZipFile(workbook_path) as archive:
        shared = _strings(archive)
        root = ET.fromstring(archive.read(_sheet_path(archive)))
    rows: dict[int, dict[str, str]] = {}
    for cell in root.findall(".//main:c", NS):
        reference = cell.attrib.get("r", "")
        match = re.fullmatch(r"([A-Z]+)([0-9]+)", reference)
        if match is None or match.group(1) not in {CODE_COLUMN, TOTAL_COLUMN, "A"}:
            continue
        value = _cell_value(cell, shared)
        if value is not None:
            rows.setdefault(int(match.group(2)), {})[match.group(1)] = value
    title = rows.get(4, {}).get("A", "")
    header = rows.get(6, {})
    normalized_title = _plain(title)
    normalized_code_header = _plain(header.get(CODE_COLUMN, ""))
    # The publisher's 2023 workbook occasionally exposes accented strings through
    # a legacy encoding path. These stable stems validate the table identity without
    # accepting a different table.
    if "MATR" not in normalized_title or "EDUCA" not in normalized_title or "MUNIC" not in normalized_title or "DIGO" not in normalized_code_header or "MUNIC" not in normalized_code_header:
        raise ValueError("worksheet 1.2 does not match the approved 2023 aggregate layout")
    timestamp = captured_at or datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    result: list[dict[str, object]] = []
    for row_number in sorted(rows):
        code = rows[row_number].get(CODE_COLUMN, "").strip()
        total = rows[row_number].get(TOTAL_COLUMN)
        if not re.fullmatch(r"[0-9]{7}", code) or total is None:
            continue
        numeric = float(total)
        if numeric < 0 or not numeric.is_integer():
            raise ValueError(f"invalid enrolment count for municipality {code}")
        result.append({"id": f"{code}-{year}", "updated_at": timestamp, "year": year, "municipality_code": code, "basic_education_enrollment_total": int(numeric), "source_table": SHEET_NAME, "source_year": year})
    if not result:
        raise ValueError("worksheet 1.2 contains no municipality aggregate rows")
    if len({record["id"] for record in result}) != len(result):
        raise ValueError("worksheet 1.2 contains duplicate municipality codes")
    return result


def enrich_siope_records(base_semantic_path: Path, censo_jsonl_path: Path) -> tuple[list[dict[str, object]], dict[str, int]]:
    """Join approved Censo totals to matching municipality-year SIOPE records."""
    base = pq.read_table(base_semantic_path).to_pylist()
    censo = [__import__("json").loads(line) for line in censo_jsonl_path.read_text(encoding="utf-8").splitlines() if line]
    by_id = {str(record["id"]): record for record in censo}
    result: list[dict[str, object]] = []
    matched = 0
    for record in base:
        item = {key: value for key, value in record.items() if key not in {"source_id", "natural_key", "identifier_classification"}}
        if item["year"] == 2023:
            addition = by_id.get(str(item["id"]))
            if addition is None:
                raise ValueError(f"SIOPE municipality-year has no approved Censo aggregate: {item['id']}")
            item["basic_education_enrollment_total"] = addition["basic_education_enrollment_total"]
            item["censo_source_table"] = addition["source_table"]
            item["censo_source_year"] = addition["source_year"]
            matched += 1
        result.append(item)
    return result, {"base_records": len(base), "matched_2023_records": matched, "unmatched_censo_records": len(set(by_id) - {str(row['id']) for row in base})}
