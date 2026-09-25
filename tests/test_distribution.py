import unittest

from brazil_data_map.distribution import validate_distribution_profile


class DistributionProfileTests(unittest.TestCase):
    def test_pending_profile_needs_intended_slugs_only(self) -> None:
        validate_distribution_profile({"schema_version": "1.0", "distribution_status": "pending", "datasets": [{"intended_slug": "example"}]})

    def test_ready_profile_requires_published_release_evidence(self) -> None:
        with self.assertRaisesRegex(ValueError, "release evidence"):
            validate_distribution_profile({"schema_version": "1.0", "distribution_status": "ready", "datasets": [{"intended_slug": "example"}]})

    def test_mixed_profile_records_a_released_dataset_and_a_pending_dataset(self) -> None:
        validate_distribution_profile({
            "schema_version": "1.0",
            "distribution_status": "mixed",
            "datasets": [
                {"intended_slug": "education", "distribution_status": "pending"},
                {"intended_slug": "pncp", "distribution_status": "ready", "published_slug": "owner/pncp", "version": 1, "review_approval": "docs/evidence/pncp.md"},
            ],
        })
