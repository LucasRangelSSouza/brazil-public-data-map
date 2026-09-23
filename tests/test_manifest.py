import json
from pathlib import Path
import tempfile
import unittest

from brazil_data_map.release import build_manifest, validate_manifest


class ReleaseManifestTests(unittest.TestCase):
    def test_manifest_records_hashes_lineage_and_privacy_approval(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            layer = root / "trusted" / "organizations.json"
            layer.parent.mkdir()
            layer.write_text('[{"golden_organization_id":"demo"}]\n', encoding="utf-8")
            manifest = build_manifest(root, "pncp", "https://pncp.gov.br/api/consulta", {"privacy_gate": "passed"})

        validate_manifest(manifest)
        self.assertEqual(manifest["source_id"], "pncp")
        self.assertEqual(manifest["files"][0]["path"], "trusted/organizations.json")
        self.assertEqual(manifest["privacy_gate"], "passed")

    def test_manifest_rejects_missing_privacy_approval(self) -> None:
        manifest = {"source_id": "pncp", "source_url": "https://pncp.gov.br", "files": []}
        with self.assertRaisesRegex(ValueError, "privacy_gate"):
            validate_manifest(manifest)


if __name__ == "__main__":
    unittest.main()
