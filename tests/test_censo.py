from __future__ import annotations

from pathlib import Path
import tempfile
import unittest
import zipfile

from brazil_data_map.censo import extract_enrollment_rows


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
