import json
from pathlib import Path
import tempfile
import unittest

from brazil_data_map.registry import load_registry, validate_registry


class RegistryTests(unittest.TestCase):
    def test_repository_registry_is_valid(self) -> None:
        registry = load_registry(Path("sources/registry.json"))
        self.assertEqual(len(registry["sources"]), 4)

    def test_registry_rejects_duplicate_source_ids_and_non_https_urls(self) -> None:
        registry = {
            "schema_version": "1.0",
            "sources": [
                {
                    "id": "pncp",
                    "publisher": "Publisher",
                    "official_url": "http://example.org",
                    "grain": "item",
                    "refresh": "daily",
                    "public_release_assessment": "review",
                },
                {
                    "id": "pncp",
                    "publisher": "Publisher",
                    "official_url": "https://example.org",
                    "grain": "item",
                    "refresh": "daily",
                    "public_release_assessment": "review",
                },
            ],
        }
        with self.assertRaisesRegex(ValueError, "HTTPS"):
            validate_registry(registry)

        registry["sources"][0]["official_url"] = "https://example.org"
        with self.assertRaisesRegex(ValueError, "duplicate"):
            validate_registry(registry)

    def test_load_registry_rejects_invalid_json_contract(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            path = Path(temporary_directory) / "registry.json"
            path.write_text(json.dumps({"schema_version": "1.0", "sources": []}), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "at least one"):
                load_registry(path)
