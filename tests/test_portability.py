from pathlib import Path
import importlib.util
import unittest


ROOT = Path(__file__).resolve().parents[1]
DAGS = sorted((ROOT / "dags").glob("*.py"))


class PortabilityTests(unittest.TestCase):
    def test_dag_templates_have_no_environment_specific_configuration(self) -> None:
        self.assertGreaterEqual(len(DAGS), 2)
        for path in DAGS:
            content = path.read_text(encoding="utf-8").lower()
            for forbidden in ("kaggle", "token", "bucket", "project_id", "bigquery"):
                self.assertNotIn(forbidden, content, f"{path.name} mentions {forbidden}")

    def test_dag_templates_import_without_airflow(self) -> None:
        for path in DAGS:
            spec = importlib.util.spec_from_file_location(path.stem, path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

    def test_education_template_is_unscheduled_and_paused(self) -> None:
        content = (ROOT / "dags" / "education_siope_annual_update.py").read_text(encoding="utf-8")
        self.assertIn("schedule=None", content)
        self.assertIn("is_paused_upon_creation=True", content)


if __name__ == "__main__":
    unittest.main()
