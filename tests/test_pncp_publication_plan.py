from copy import deepcopy
import json
from pathlib import Path
import unittest

from brazil_data_map.pncp_catalog import load_pncp_publication_plan, validate_pncp_publication_plan


class PncpPublicationPlanTests(unittest.TestCase):
    def test_catalogue_groups_raw_and_trusted_together_and_semantic_separately(self) -> None:
        root = Path("sources")
        catalogue = json.loads((root / "pncp_table_catalog.json").read_text(encoding="utf-8"))
        plan = load_pncp_publication_plan(root / "pncp_publication_plan.json", catalogue)

        item_group = next(group for group in plan["subjects"] if group["subject_id"] == "procurement-items")
        data_bundle = next(bundle for bundle in item_group["datasets"] if bundle["kind"] == "data")
        self.assertEqual(data_bundle["kaggle_slug"], "pncp-procurement-items-data")
        self.assertCountEqual(data_bundle["table_layers"], [
            {"table_id": "pncp_contratacoes_itens", "layer": "raw"},
            {"table_id": "pncp_contratacoes_itens", "layer": "trusted"},
            {"table_id": "pncp_contratacoes_itens_resultados", "layer": "raw"},
            {"table_id": "pncp_contratacoes_itens_resultados", "layer": "trusted"},
        ])

        semantic_group = next(group for group in plan["subjects"] if group["subject_id"] == "procurement-search")
        semantic_bundle = next(bundle for bundle in semantic_group["datasets"] if bundle["kind"] == "semantic")
        self.assertEqual(semantic_bundle["kaggle_slug"], "pncp-procurement-search-semantic")
        self.assertTrue(all(entry["layer"] == "semantic" for entry in semantic_bundle["table_layers"]))

    def test_plan_covers_every_catalogue_table_layer_exactly_once(self) -> None:
        root = Path("sources")
        catalogue = json.loads((root / "pncp_table_catalog.json").read_text(encoding="utf-8"))
        plan = load_pncp_publication_plan(root / "pncp_publication_plan.json", catalogue)
        planned = [
            (entry["table_id"], entry["layer"])
            for group in plan["subjects"]
            for bundle in group["datasets"]
            for entry in bundle["table_layers"]
        ]
        expected = [(table["table_id"], table["layer"]) for table in catalogue["tables"]]
        self.assertCountEqual(planned, expected)
        self.assertEqual(len(planned), len(set(planned)))

    def test_plan_rejects_cross_layer_semantic_bundle_or_duplicate_table(self) -> None:
        root = Path("sources")
        catalogue = json.loads((root / "pncp_table_catalog.json").read_text(encoding="utf-8"))
        plan = load_pncp_publication_plan(root / "pncp_publication_plan.json", catalogue)
        invalid = deepcopy(plan)
        semantic = next(
            bundle for group in invalid["subjects"] for bundle in group["datasets"] if bundle["kind"] == "semantic"
        )
        semantic["table_layers"].append({"table_id": "pncp_contratacoes_itens", "layer": "trusted"})
        with self.assertRaisesRegex(ValueError, "bundle kind does not match table layer"):
            validate_pncp_publication_plan(invalid, catalogue)

    def test_plan_rejects_slug_collisions_and_limits_above_kaggle_cap(self) -> None:
        root = Path("sources")
        catalogue = json.loads((root / "pncp_table_catalog.json").read_text(encoding="utf-8"))
        plan = load_pncp_publication_plan(root / "pncp_publication_plan.json", catalogue)
        invalid = deepcopy(plan)
        invalid["subjects"][1]["datasets"][0]["kaggle_slug"] = invalid["subjects"][0]["datasets"][0]["kaggle_slug"]
        with self.assertRaisesRegex(ValueError, "duplicate Kaggle dataset slug"):
            validate_pncp_publication_plan(invalid, catalogue)

        invalid = deepcopy(plan)
        invalid["size_limit_bytes"] += 1
        with self.assertRaisesRegex(ValueError, "must not exceed Kaggle's 200 GB cap"):
            validate_pncp_publication_plan(invalid, catalogue)

    def test_plan_requires_catalogue_targets_to_match_subject_bundle_slugs(self) -> None:
        root = Path("sources")
        catalogue = json.loads((root / "pncp_table_catalog.json").read_text(encoding="utf-8"))
        plan = load_pncp_publication_plan(root / "pncp_publication_plan.json", catalogue)
        invalid_catalogue = deepcopy(catalogue)
        entry = next(table for table in invalid_catalogue["tables"] if table["table_id"] == "pncp_dom_modalidades")
        entry["kaggle_slug"] = "pncp-trusted-dom-modalidades"

        with self.assertRaisesRegex(ValueError, "table catalogue target does not match its publication plan"):
            validate_pncp_publication_plan(plan, invalid_catalogue)


if __name__ == "__main__":
    unittest.main()
