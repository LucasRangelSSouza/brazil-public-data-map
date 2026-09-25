import json
from datetime import date
from pathlib import Path
import tempfile
import unittest

from brazil_data_map.backfill import deduplicate_latest, rebuild_capture_release, run_backfill


class BackfillTests(unittest.TestCase):
    def test_deduplicates_to_latest_update_deterministically(self) -> None:
        records = [
            {"id": "b", "updated_at": "2026-01-01T00:00:00Z"},
            {"id": "a", "updated_at": "2026-01-01T00:00:00Z"},
            {"id": "a", "updated_at": "2026-01-02T00:00:00Z"},
        ]
        self.assertEqual(
            deduplicate_latest(records),
            [
                {"id": "a", "updated_at": "2026-01-02T00:00:00Z"},
                {"id": "b", "updated_at": "2026-01-01T00:00:00Z"},
            ],
        )

    def test_resumes_completed_windows_and_writes_lineage(self) -> None:
        calls: list[tuple[date, int]] = []

        def fetcher(day: date, _: date, modality_id: int):
            calls.append((day, modality_id))
            return [{"id": f"{day}:{modality_id}", "updated_at": "2026-01-02T00:00:00Z", "item": "paper"}]

        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            first = run_backfill(date(2026, 1, 1), date(2026, 1, 2), [6], root, fetcher=fetcher, retrieved_at="2026-01-03T00:00:00Z", git_commit="abc123")
            second = run_backfill(date(2026, 1, 1), date(2026, 1, 2), [6], root, fetcher=fetcher, retrieved_at="2026-01-03T00:00:00Z", git_commit="abc123")
            manifest = json.loads((root / "release" / "manifest.json").read_text(encoding="utf-8"))

        self.assertEqual(first["fetched_windows"], 2)
        self.assertEqual(second["fetched_windows"], 0)
        self.assertEqual(len(calls), 2)
        self.assertEqual(first["deduplicated_records"], 2)
        self.assertEqual(manifest["git_commit"], "abc123")
        self.assertEqual(manifest["row_counts"], {"raw": 2, "semantic": 2, "trusted": 2})
        self.assertEqual(len(manifest["source_input_sha256"]), 64)

    def test_partial_failure_still_refreshes_the_checkpointed_release(self) -> None:
        def fetcher(day: date, _: date, __: int):
            if day == date(2026, 1, 2):
                raise RuntimeError("rate limited")
            return [{"id": "a", "updated_at": "2026-01-01T00:00:00Z", "item": "paper"}]

        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            with self.assertRaisesRegex(RuntimeError, "checkpointed release"):
                run_backfill(date(2026, 1, 1), date(2026, 1, 2), [6], root, fetcher=fetcher)
            manifest = json.loads((root / "release" / "manifest.json").read_text(encoding="utf-8"))

        self.assertEqual(manifest["row_counts"], {"raw": 1, "semantic": 1, "trusted": 1})

    def test_rebuilds_a_capture_with_current_release_controls(self) -> None:
        records = [
            {"id": "a", "updated_at": "2026-01-01T00:00:00Z", "item": "older", "internal_note": "exclude"},
            {"id": "a", "updated_at": "2026-01-02T00:00:00Z", "item": "latest", "internal_note": "exclude"},
            {"id": "b", "updated_at": "2026-01-01T00:00:00Z", "item": "paper"},
        ]
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            capture = root / "capture.jsonl"
            capture.write_text("\n".join(json.dumps(record) for record in records) + "\n", encoding="utf-8")
            result = rebuild_capture_release(capture, root / "release", retrieved_at="2026-01-03T00:00:00Z", git_commit="abc123")

        self.assertEqual(result["deduplicated_records"], 2)
        self.assertEqual(result["manifest"]["row_counts"], {"raw": 2, "semantic": 2, "trusted": 2})
        self.assertEqual(result["manifest"]["git_commit"], "abc123")


if __name__ == "__main__":
    unittest.main()
