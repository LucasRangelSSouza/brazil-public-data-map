import json
from pathlib import Path
import unittest

from brazil_data_map.privacy import apply_identifier_policy


FIXTURE = Path(__file__).parent / "fixtures" / "pncp_records.json"


class IdentifierReleaseGateTests(unittest.TestCase):
    def test_only_organizations_receive_a_golden_identifier(self) -> None:
        records = json.loads(FIXTURE.read_text(encoding="utf-8"))
        released, audit = apply_identifier_policy(records)

        self.assertEqual(len(released), 1)
        self.assertIn("golden_organization_id", released[0])
        self.assertNotIn("supplier_document", released[0])
        self.assertEqual(audit["excluded_by_classification"], {"natural_person": 1, "unknown": 1})

    def test_direct_identifier_column_blocks_a_release(self) -> None:
        with self.assertRaisesRegex(ValueError, "direct identifier"):
            apply_identifier_policy([{"supplier_document": "12.345.678/0001-95", "email": "x@example.org"}])

    def test_procurement_record_without_supplier_identifier_remains_eligible(self) -> None:
        released, audit = apply_identifier_policy([{"id": "pncp-1", "updated_at": "2026-01-01T00:00:00Z", "item": "paper"}])

        self.assertEqual(released[0]["identifier_classification"], "not_present")
        self.assertNotIn("golden_organization_id", released[0])
        self.assertEqual(audit["released_without_supplier_identifier"], 1)


if __name__ == "__main__":
    unittest.main()
