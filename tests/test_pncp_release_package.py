from __future__ import annotations

import hashlib
import json
from pathlib import Path
import unittest

import pyarrow as pa
import pyarrow.parquet as pq

from brazil_data_map.pncp_catalog import validate_pncp_release_package


class PncpReleasePackageTests(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path("tests/fixtures/pncp-modality-package")
        self.root.mkdir(parents=True, exist_ok=True)

    def tearDown(self) -> None:
        for path in self.root.iterdir():
            path.unlink()
        self.root.rmdir()

    def write_package(self) -> tuple[dict, Path]:
        table = pa.Table.from_pylist(
            [{
                "id": 1,
                "nome": "Pregão",
                "descricao": "Procedimento público de aquisição",
                "statusAtivo": True,
                "dataInclusao": "1900-01-01T00:00:00Z",
                "dataAtualizacao": "2026-02-24T15:29:21Z",
            }]
        )
        data = self.root / "pncp_dom_modalidades.parquet"
        pq.write_table(table, data)
        schema = self.root / "schema.json"
        schema.write_text(json.dumps({"fields": table.schema.names}), encoding="utf-8")
        audit = self.root / "privacy-audit.json"
        audit.write_text(
            json.dumps({"status": "passed", "rows_scanned": 1, "rows_released": 1, "direct_identifier_matches": 0}),
            encoding="utf-8",
        )
        (self.root / "README.md").write_text("Reproducible public snapshot.\n", encoding="utf-8")
        files = []
        for path in (data, schema, audit):
            files.append(
                {
                    "path": path.name,
                    "bytes": path.stat().st_size,
                    "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                }
            )
        manifest = {
            "schema_version": "1.0",
            "dataset_slug": "pncp-trusted-dom-modalidades",
            "table_id": "pncp_dom_modalidades",
            "layer": "trusted",
            "data_cutoff": "2026-07-31T23:59:59.999999Z",
            "row_count": 1,
            "schema_sha256": hashlib.sha256(schema.read_bytes()).hexdigest(),
            "automated_scan": {
                "status": "passed",
                "rows_scanned": 1,
                "rows_released": 1,
                "direct_identifier_matches": 0,
            },
            "files": files,
        }
        (self.root / "release_manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
        catalog = {
            "data_cutoff": "2026-07-31T23:59:59Z",
            "tables": [
                {
                    "table_id": "pncp_dom_modalidades",
                    "layer": "trusted",
                    "kaggle_slug": "pncp-reference-codes-data",
                    "legacy_publication": {"dataset_slug": "pncp-trusted-dom-modalidades"},
                }
            ],
        }
        return catalog, self.root

    def test_valid_clean_download_package_matches_catalogue_contract(self) -> None:
        catalog, package = self.write_package()

        result = validate_pncp_release_package(catalog, "pncp-trusted-dom-modalidades", package)

        self.assertEqual(result["status"], "passed")
        self.assertEqual(result["row_count"], 1)
        self.assertEqual(result["files_checked"], 5)
        self.assertEqual(result["hash_mismatches"], 0)

    def test_package_rejects_tampered_data_file(self) -> None:
        catalog, package = self.write_package()
        (package / "pncp_dom_modalidades.parquet").write_bytes(b"changed")

        with self.assertRaisesRegex(ValueError, "file hash or size mismatch"):
            validate_pncp_release_package(catalog, "pncp-trusted-dom-modalidades", package)

    def test_package_rejects_manifest_for_another_dataset(self) -> None:
        catalog, package = self.write_package()
        manifest_path = package / "release_manifest.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest["dataset_slug"] = "pncp-raw-some-other-table"
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

        with self.assertRaisesRegex(ValueError, "does not match the catalogue entry"):
            validate_pncp_release_package(catalog, "pncp-trusted-dom-modalidades", package)


if __name__ == "__main__":
    unittest.main()
