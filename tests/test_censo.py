from __future__ import annotations

from pathlib import Path
import tempfile
import unittest
import zipfile

import pyarrow as pa
import pyarrow.parquet as pq

from brazil_data_map.censo import enrich_siope_records, extract_enrollment_rows


def workbook(path: Path, code: str = "1100015", total: str = "4985", title: str = "Numero de Matriculas da Educacao Basica segundo o Municipio") -> None:
    files = {
        "xl/workbook.xml": f'<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets><sheet name="1.2" sheetId="1" r:id="rId1"/></sheets></workbook>',
        "xl/_rels/workbook.xml.rels": '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Target="worksheets/sheet1.xml" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet"/></Relationships>',
        "xl/worksheets/sheet1.xml": f'''<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheetData>
<row r="4"><c r="A4" t="inlineStr"><is><t>{title}</t></is></c></row>
<row r="6"><c r="D6" t="inlineStr"><is><t>Codigo do Municipio</t></is></c></row>
<row r="11"><c r="D11" t="inlineStr"><is><t>{code}</t></is></c><c r="E11"><v>{total}</v></c></row>
<row r="12"><c r="D12" t="inlineStr"><is><t> </t></is></c><c r="E12"><v>999</v></c></row>
</sheetData></worksheet>''',
    }
    with zipfile.ZipFile(path, "w") as archive:
        for name, content in files.items():
            archive.writestr(name, content)


class CensoTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name) / "source.xlsx"

    def tearDown(self):
        self.tmp.cleanup()

    def test_extracts_only_a_municipality_total(self):
        workbook(self.path)
        self.assertEqual(extract_enrollment_rows(self.path, 2023, "2026-09-27T00:00:00Z"), [{
            "id": "1100015-2023", "updated_at": "2026-09-27T00:00:00Z", "year": 2023,
            "municipality_code": "1100015", "basic_education_enrollment_total": 4985,
            "source_table": "1.2", "source_year": 2023,
        }])

    def test_rejects_invalid_enrollment(self):
        workbook(self.path, total="-1")
        with self.assertRaisesRegex(ValueError, "invalid enrolment"):
            extract_enrollment_rows(self.path, captured_at="2026-09-27T00:00:00Z")

    def test_rejects_a_changed_table(self):
        workbook(self.path, title="Other table")
        with self.assertRaisesRegex(ValueError, "approved 2023 aggregate layout"):
            extract_enrollment_rows(self.path, captured_at="2026-09-27T00:00:00Z")

    def test_enrichment_requires_every_siope_2023_key_and_reports_extras(self):
        base = self.path.with_name("base.parquet")
        censo = self.path.with_name("censo.jsonl")
        pq.write_table(pa.Table.from_pylist([
            {"id": "1100015-2023", "year": 2023, "municipality_code": "1100015", "updated_at": "2026-01-01T00:00:00Z"},
            {"id": "1100015-2022", "year": 2022, "municipality_code": "1100015", "updated_at": "2025-01-01T00:00:00Z"},
        ]), base)
        censo.write_text('{"id":"1100015-2023","basic_education_enrollment_total":4985,"source_table":"1.2","source_year":2023}\n{"id":"9999999-2023","basic_education_enrollment_total":1,"source_table":"1.2","source_year":2023}\n', encoding="utf-8")
        records, report = enrich_siope_records(base, censo)
        self.assertEqual(records[0]["basic_education_enrollment_total"], 4985)
        self.assertNotIn("basic_education_enrollment_total", records[1])
        self.assertEqual(report, {"base_records": 2, "matched_2023_records": 1, "unmatched_censo_records": 1})
        censo.write_text('', encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "has no approved Censo aggregate"):
            enrich_siope_records(base, censo)
