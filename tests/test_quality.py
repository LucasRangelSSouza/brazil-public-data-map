import unittest

from brazil_data_map.quality import validate_records, validate_reconciliation


class QualityTests(unittest.TestCase):
    def test_records_require_unique_ids_and_parseable_timestamps(self) -> None:
        with self.assertRaisesRegex(ValueError, "duplicate id"):
            validate_records([
                {"id": "a", "updated_at": "2026-01-01T00:00:00Z"},
                {"id": "a", "updated_at": "2026-01-02T00:00:00Z"},
            ])
        with self.assertRaisesRegex(ValueError, "invalid updated_at"):
            validate_records([{"id": "a", "updated_at": "not-a-date"}])

    def test_reconciliation_requires_matching_trusted_and_semantic_counts(self) -> None:
        layers = {
            "raw": [{"id": "a", "updated_at": "2026-01-01T00:00:00Z"}],
            "trusted": [{"id": "a", "updated_at": "2026-01-01T00:00:00Z"}],
            "semantic": [],
        }
        with self.assertRaisesRegex(ValueError, "counts must match"):
            validate_reconciliation(layers)
