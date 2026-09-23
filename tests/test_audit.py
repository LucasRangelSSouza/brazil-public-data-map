import unittest

from brazil_data_map.audit import audit_release_layers


class ReleaseAuditTests(unittest.TestCase):
    def test_audit_returns_counts_for_clean_layers(self) -> None:
        layers = {
            "raw": [{"id": "a", "golden_organization_id": "hash"}],
            "trusted": [{"id": "a", "golden_organization_id": "hash"}],
            "semantic": [{"id": "a", "natural_key": "a", "golden_organization_id": "hash"}],
        }
        audit = audit_release_layers(layers)
        self.assertEqual(audit["privacy_gate"], "passed")
        self.assertEqual(audit["record_counts"]["semantic"], 1)

    def test_audit_rejects_identifiers_in_key_or_value(self) -> None:
        with self.assertRaisesRegex(ValueError, "privacy audit failed"):
            audit_release_layers({"raw": [{"note": "contact someone@example.org"}]})

        with self.assertRaisesRegex(ValueError, "privacy audit failed"):
            audit_release_layers({"trusted": [{"cpf": "12345678901"}]})
