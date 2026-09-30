from __future__ import annotations

import hashlib
import json
from pathlib import Path
import tempfile
import unittest

import pyarrow as pa
import pyarrow.parquet as pq

from brazil_data_map.pncp_catalog import load_pncp_publication_plan, validate_pncp_release_bundle


class PncpReleaseBundleTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.catalog = json.loads(Path("sources/pncp_table_catalog.json").read_text(encoding="utf-8"))
        self.plan = load_pncp_publication_plan(Path("sources/pncp_publication_plan.json"), self.catalog)
        self.slug = "pncp-procurement-items-data"

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def write_bundle(self) -> Path:
        expected = [
            {"table_id": table_id, "layer": layer}
            for table_id in ("pncp_contratacoes_itens", "pncp_contratacoes_itens_resultados")
            for layer in ("raw", "trusted")
        ]
        tables = []
        files = []
        for index, entry in enumerate(expected):
            table_id, layer = entry["table_id"], entry["layer"]
            parquet_rel = f"{layer}__{table_id}.parquet"
            schema_rel = f"schema__{table_id}__{layer}.json"
            audit_rel = f"privacy-audit__{table_id}__{layer}.json"
            parquet_path = self.root / parquet_rel
            pq.write_table(pa.Table.from_pylist([{"id": index, "description": f"public item {index}"}]), parquet_path)
            schema_path = self.root / schema_rel
            schema_path.write_text(json.dumps({"fields": ["id", "description"]}), encoding="utf-8")
            audit_path = self.root / audit_rel
            audit_path.write_text(json.dumps({"status": "passed", "rows_scanned": 1, "rows_released": 1, "direct_identifier_matches": 0}), encoding="utf-8")
            tables.append({
                **entry,
                "row_count": 1,
                "parquet_path": parquet_rel,
                "schema_path": schema_rel,
                "schema_sha256": hashlib.sha256(schema_path.read_bytes()).hexdigest(),
                "privacy_audit_path": audit_rel,
                "privacy_audit_sha256": hashlib.sha256(audit_path.read_bytes()).hexdigest(),
            })

        (self.root / "README.md").write_text("PNCP procurement item bundle.\n", encoding="utf-8")
        (self.root / "dataset-metadata.json").write_text(
            json.dumps({"id": f"lucasrangelss/{self.slug}"}), encoding="utf-8"
        )
        for path in sorted(self.root.rglob("*")):
            if path.is_file() and path.name not in {"release_manifest.json", "dataset-metadata.json"}:
                rel = path.relative_to(self.root).as_posix()
                files.append({"path": rel, "bytes": path.stat().st_size, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
        manifest = {
            "schema_version": "2.0",
            "dataset_slug": self.slug,
            "subject_id": "procurement-items",
            "bundle_kind": "data",
            "data_cutoff": "2026-07-31T23:59:59Z",
            "kaggle_metadata_sha256": hashlib.sha256((self.root / "dataset-metadata.json").read_bytes()).hexdigest(),
            "tables": tables,
            "files": files,
        }
        (self.root / "release_manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
        return self.root

    def test_complete_subject_bundle_verifies_raw_and_trusted_together(self) -> None:
        package = self.write_bundle()

        result = validate_pncp_release_bundle(self.catalog, self.plan, self.slug, package)

        self.assertEqual(result["status"], "passed")
        self.assertEqual(result["subject_id"], "procurement-items")
        self.assertEqual(result["table_layers_checked"], 4)
        self.assertEqual(result["row_count"], 4)
        self.assertEqual(result["hash_mismatches"], 0)

    def test_clean_kaggle_download_verifies_without_upload_control_metadata(self) -> None:
        package = self.write_bundle()
        (package / "dataset-metadata.json").unlink()

        result = validate_pncp_release_bundle(self.catalog, self.plan, self.slug, package)

        self.assertEqual(result["status"], "passed")
        self.assertEqual(result["files_checked"], 14)

    def test_bundle_rejects_a_missing_table_layer(self) -> None:
        package = self.write_bundle()
        manifest_path = package / "release_manifest.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest["tables"].pop()
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

        with self.assertRaisesRegex(ValueError, "bundle table coverage does not match publication plan"):
            validate_pncp_release_bundle(self.catalog, self.plan, self.slug, package)

    def test_bundle_rejects_files_over_kaggle_size_limit(self) -> None:
        package = self.write_bundle()
        constrained_plan = json.loads(json.dumps(self.plan))
        constrained_plan["size_limit_bytes"] = 1

        with self.assertRaisesRegex(ValueError, "exceeds Kaggle's configured size limit"):
            validate_pncp_release_bundle(self.catalog, constrained_plan, self.slug, package)


if __name__ == "__main__":
    unittest.main()
