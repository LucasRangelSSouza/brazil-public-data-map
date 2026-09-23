from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class PortabilityTests(unittest.TestCase):
    def test_dag_template_has_no_environment_specific_configuration(self) -> None:
        content = (ROOT / "dags" / "pncp_incremental_update.py").read_text(encoding="utf-8").lower()
        for forbidden in ("kaggle", "token", "bucket", "project_id", "bigquery"):
            self.assertNotIn(forbidden, content)


if __name__ == "__main__":
    unittest.main()
