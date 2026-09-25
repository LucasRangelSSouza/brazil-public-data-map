import json
from pathlib import Path
import tempfile
import unittest

import pyarrow.parquet as pq

from brazil_data_map.pipeline import build_public_release


class PublicReleasePipelineTests(unittest.TestCase):
    def test_pipeline_writes_audited_layers_and_manifest(self) -> None:
        records = [{"id": "a", "updated_at": "2026-01-02", "supplier_document": "12.345.678/0001-95", "item": "paper"}]
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            result = build_public_release(records, root, "pncp", "https://www.gov.br/pncp/pt-br/acesso-a-informacao/dados-abertos")
            manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
            raw = pq.read_table(root / "raw" / "records.parquet").to_pylist()

        self.assertEqual(result["audit"]["privacy_gate"], "passed")
        self.assertEqual(manifest["privacy_gate"], "passed")
        self.assertEqual([entry["path"] for entry in manifest["files"]], ["privacy-audit.json", "raw/records.parquet", "semantic/records.parquet", "trusted/records.parquet"])
        self.assertNotIn("supplier_document", raw[0])
        self.assertIn("golden_organization_id", raw[0])

    def test_repository_fixture_builds_a_local_release_candidate(self) -> None:
        records = json.loads(Path("tests/fixtures/pncp_records.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as temporary_directory:
            result = build_public_release(records, Path(temporary_directory), "pncp", "https://www.gov.br/pncp/pt-br/acesso-a-informacao/dados-abertos")

        self.assertEqual(result["audit"]["record_counts"], {"raw": 1, "trusted": 1, "semantic": 1})

    def test_fixed_retrieval_time_produces_identical_release_hashes(self) -> None:
        records = [{"id": "a", "updated_at": "2026-01-02", "supplier_document": "12.345.678/0001-95", "item": "paper"}]
        with tempfile.TemporaryDirectory() as first_directory, tempfile.TemporaryDirectory() as second_directory:
            first = build_public_release(records, Path(first_directory), "pncp", "https://www.gov.br/pncp/pt-br/acesso-a-informacao/dados-abertos", "2026-01-03T00:00:00Z")
            second = build_public_release(records, Path(second_directory), "pncp", "https://www.gov.br/pncp/pt-br/acesso-a-informacao/dados-abertos", "2026-01-03T00:00:00Z")

        self.assertEqual(first["manifest"], second["manifest"])

    def test_pipeline_excludes_unapproved_source_fields_before_writing(self) -> None:
        records = [{"id": "a", "updated_at": "2026-01-02", "item": "livros para escola", "internal_note": "do not release"}]
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            build_public_release(records, root, "pncp", "https://pncp.gov.br/api/consulta")
            raw = pq.read_table(root / "raw" / "records.parquet").to_pylist()

        self.assertNotIn("internal_note", raw[0])
        self.assertNotIn("item", raw[0])
        self.assertEqual(raw[0]["procurement_category"], "education")
