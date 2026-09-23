import unittest

from brazil_data_map.pncp import incremental_snapshot


class PncpIncrementalTests(unittest.TestCase):
    def test_pagination_retry_and_natural_key_deduplication_converge(self) -> None:
        pages = [
            [{"id": "a", "updated_at": "2026-01-01", "value": 1}, {"id": "b", "updated_at": "2026-01-01", "value": 2}],
            RuntimeError("temporary rate limit"),
            [{"id": "a", "updated_at": "2026-01-02", "value": 3}],
            [],
        ]

        def fetch(_: str):
            result = pages.pop(0)
            if isinstance(result, Exception):
                raise result
            return result

        raw, trusted, semantic, checkpoint = incremental_snapshot(fetch, "2025-12-31")

        self.assertEqual(len(raw), 3)
        self.assertEqual(trusted, [{"id": "a", "updated_at": "2026-01-02", "value": 3}, {"id": "b", "updated_at": "2026-01-01", "value": 2}])
        self.assertEqual(semantic[0]["natural_key"], "a")
        self.assertEqual(checkpoint, "2026-01-02")


if __name__ == "__main__":
    unittest.main()
