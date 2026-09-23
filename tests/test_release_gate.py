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


if __name__ == "__main__":
    unittest.main()
