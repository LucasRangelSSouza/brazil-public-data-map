import unittest

from brazil_data_map.layers import build_layers, validate_layers


class LayerTests(unittest.TestCase):
    def test_layers_preserve_lineage_and_remove_direct_supplier_identifiers(self) -> None:
        records = [{"id": "a", "updated_at": "2026-01-02", "supplier_document": "12.345.678/0001-95", "item": "paper"}]

        layers = build_layers(records, "pncp")

        validate_layers(layers)
        self.assertEqual(layers["raw"][0]["source_id"], "pncp")
        self.assertNotIn("supplier_document", layers["trusted"][0])
        self.assertEqual(layers["semantic"][0]["natural_key"], "a")

    def test_free_text_identifiers_are_redacted_before_release(self) -> None:
        records = [{"id": "a", "updated_at": "2026-01-02", "item": "contact 123.456.789-09 or person@example.org"}]
        layers = build_layers(records, "pncp")
        self.assertEqual(layers["raw"][0]["item"], "contact [REDACTED_IDENTIFIER] or [REDACTED_EMAIL]")


if __name__ == "__main__":
    unittest.main()
