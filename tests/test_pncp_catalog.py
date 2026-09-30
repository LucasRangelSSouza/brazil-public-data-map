from copy import deepcopy
from pathlib import Path
import unittest

from brazil_data_map.pncp_catalog import load_pncp_table_catalog, validate_pncp_table_catalog


class PncpTableCatalogTests(unittest.TestCase):
    def test_repository_catalog_points_related_reference_tables_to_one_bundle(self) -> None:
        catalog = load_pncp_table_catalog(Path("sources/pncp_table_catalog.json"))
        self.assertEqual(catalog["counts_by_layer"], {"raw": 13, "trusted": 28, "semantic": 6})
        self.assertEqual(catalog["expected_table_count"], 47)
        self.assertEqual(catalog["release_status"], "inventory-only")
        reference_tables = [table for table in catalog["tables"] if table["domain"] == "reference-codes"]
        self.assertEqual(len(reference_tables), 12)
        self.assertEqual({table["kaggle_slug"] for table in reference_tables}, {"pncp-reference-codes-data"})
        self.assertEqual({table["release_status"] for table in reference_tables}, {"ready"})
        self.assertEqual(len({table["kaggle_slug"] for table in catalog["tables"]}), 14)

    def test_inventory_cannot_claim_a_release_or_duplicate_a_slug(self) -> None:
        catalog = load_pncp_table_catalog(Path("sources/pncp_table_catalog.json"))
        invalid = deepcopy(catalog)
        invalid["release_status"] = "complete"
        with self.assertRaisesRegex(ValueError, "must not claim release completion"):
            validate_pncp_table_catalog(invalid)

        invalid = deepcopy(catalog)
        invalid["tables"][0]["kaggle_slug"] = "pncp-trusted-dom-modalidades"
        invalid["tables"][1]["kaggle_slug"] = "pncp-trusted-dom-modalidades"
        with self.assertRaisesRegex(ValueError, "duplicate Kaggle slug"):
            validate_pncp_table_catalog(invalid)

    def test_shared_bundle_slug_cannot_mix_release_statuses(self) -> None:
        catalog = load_pncp_table_catalog(Path("sources/pncp_table_catalog.json"))
        references = [table for table in catalog["tables"] if table["domain"] == "reference-codes"]
        for table in references:
            table["kaggle_slug"] = "pncp-reference-codes-data"

        invalid = deepcopy(catalog)
        invalid["tables"][next(i for i, table in enumerate(invalid["tables"]) if table["domain"] == "reference-codes")]["release_status"] = "inventory-only"
        with self.assertRaisesRegex(ValueError, "shared Kaggle bundle slug has inconsistent release status"):
            validate_pncp_table_catalog(invalid)

    def test_catalog_rejects_a_slug_over_the_platform_limit(self) -> None:
        catalog = load_pncp_table_catalog(Path("sources/pncp_table_catalog.json"))
        invalid = deepcopy(catalog)
        invalid["tables"][0]["kaggle_slug"] = "pncp-raw-" + "x" * 60
        with self.assertRaisesRegex(ValueError, "invalid Kaggle slug"):
            validate_pncp_table_catalog(invalid)

    def test_ready_table_requires_publication_and_clean_download_evidence(self) -> None:
        catalog = load_pncp_table_catalog(Path("sources/pncp_table_catalog.json"))
        modalities = next(table for table in catalog["tables"] if table["table_id"] == "pncp_dom_modalidades")
        modalities["release_status"] = "ready"
        modalities.pop("release_evidence")
        with self.assertRaisesRegex(ValueError, "ready table requires release_evidence"):
            validate_pncp_table_catalog(catalog)

        modalities["release_evidence"] = {
            "dataset_url": "https://www.kaggle.com/datasets/lucasrangelss/pncp-reference-codes-data",
            "data_cutoff": catalog["data_cutoff"],
            "row_count": 19,
            "manifest_sha256": "a" * 64,
            "verified_at": "2026-09-29T18:25:00Z",
            "clean_download": {"status": "passed", "files_checked": 5, "hash_mismatches": 0},
        }
        validate_pncp_table_catalog(catalog)

    def test_ready_table_rejects_incomplete_download_evidence(self) -> None:
        catalog = load_pncp_table_catalog(Path("sources/pncp_table_catalog.json"))
        modalities = next(table for table in catalog["tables"] if table["table_id"] == "pncp_dom_modalidades")
        modalities["release_status"] = "ready"
        modalities["release_evidence"] = {
            "dataset_url": "https://www.kaggle.com/datasets/lucasrangelss/pncp-reference-codes-data",
            "data_cutoff": catalog["data_cutoff"],
            "row_count": 19,
            "manifest_sha256": "a" * 64,
            "verified_at": "2026-09-29T18:25:00Z",
            "clean_download": {"status": "passed", "files_checked": 5, "hash_mismatches": 1},
        }
        with self.assertRaisesRegex(ValueError, "clean-download verification must pass"):
            validate_pncp_table_catalog(catalog)


if __name__ == "__main__":
    unittest.main()
