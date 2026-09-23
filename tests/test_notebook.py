import json
from pathlib import Path
import unittest


class NotebookTests(unittest.TestCase):
    def test_walkthrough_notebook_is_valid_and_uses_only_synthetic_input(self) -> None:
        notebook = json.loads(Path("notebooks/01_local_release_walkthrough.ipynb").read_text(encoding="utf-8"))
        source = "".join(line for cell in notebook["cells"] for line in cell.get("source", []))

        self.assertEqual(notebook["nbformat"], 4)
        self.assertIn("tests/fixtures/pncp_records.json", source)
        self.assertNotIn("api_key", source.casefold())
        self.assertNotIn("password", source.casefold())
