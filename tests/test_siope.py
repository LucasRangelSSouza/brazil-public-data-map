import gzip
import io
import json
from pathlib import Path
import tempfile
import unittest
from urllib.error import URLError

from brazil_data_map.pipeline import build_public_release
from brazil_data_map.siope import SIOPE_ODATA_URL, build_records, capture, get_json

IBGE = [
    {"id": 1200013, "nome": "Acrelandia", "microrregiao": {"mesorregiao": {"UF": {"sigla": "AC"}}}},
    {"id": 1200054, "nome": "Assis Brasil", "microrregiao": None,
     "regiao-imediata": {"regiao-intermediaria": {"UF": {"sigla": "AC"}}}},
]


def general_row(code, declared, revenue="100.5"):
    return {"TIPO": "Municipal", "NUM_ANO": 2023, "COD_MUNI": code, "NUM_POPU": 1000,
            "VAL_RECE_REAL": revenue, "VAL_DESP_PAGA": "90", "DAT_DECL": declared}


def fake_fetch(general):
    def fetch(url):
        if "localidades" in url:
            return IBGE
        if "Dados_Gerais_Siope" in url:
            return {"value": general}
        return {"value": [
            {"COD_MUNI": 120001, "COD_INDI": 24, "VAL_INDI": "27.06"},
            {"COD_MUNI": 120001, "COD_INDI": 56, "VAL_INDI": "9903.37"},
        ]}
    return fetch


class SiopeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_capture_joins_ibge_and_pivots_indicators(self):
        capture([2023], self.dir, states=["AC"], fetch=fake_fetch([general_row(120001, "2024-04-29"), general_row(120005, "2024-05-01")]))
        records = build_records(self.dir)
        self.assertEqual([r["id"] for r in records], ["1200013-2023", "1200054-2023"])
        first = records[0]
        self.assertEqual(first["state_code"], "AC")
        self.assertEqual(first["total_revenue_realized"], 100.5)
        self.assertEqual(first["mde_minimum_share_pct"], 27.06)
        self.assertIsNone(first["fundeb_remuneration_share_pct"])
        self.assertEqual(records[1]["state_code"], "AC")

    def test_latest_declaration_wins(self):
        capture([2023], self.dir, states=["AC"], fetch=fake_fetch([
            general_row(120001, "2024-04-29", "1"), general_row(120001, "2025-01-10", "2"),
        ]))
        self.assertEqual(build_records(self.dir)[0]["total_revenue_realized"], 2.0)

    def test_capture_resumes_without_refetching(self):
        capture([2023], self.dir, states=["AC"], fetch=fake_fetch([general_row(120001, "2024-04-29")]))
        result = capture([2023], self.dir, states=["AC"], fetch=lambda url: self.fail("refetched"))
        self.assertEqual(result, {"fetched_state_years": 0, "skipped_state_years": 1, "capture_dir": str(self.dir)})

    def test_unmatched_municipality_blocks_the_build(self):
        capture([2023], self.dir, states=["AC"], fetch=fake_fetch([general_row(999999, "2024-04-29")]))
        with self.assertRaisesRegex(ValueError, "no IBGE municipality match"):
            build_records(self.dir)

    def test_release_is_deterministic_and_passes_the_privacy_gate(self):
        capture([2023], self.dir, states=["AC"], fetch=fake_fetch([general_row(120001, "2024-04-29")]))
        records = build_records(self.dir)
        first = build_public_release(records, self.dir / "a", "fnde-siope", SIOPE_ODATA_URL, "2026-09-25T00:00:00Z", "abc")
        second = build_public_release(records, self.dir / "b", "fnde-siope", SIOPE_ODATA_URL, "2026-09-25T00:00:00Z", "abc")
        self.assertEqual(first["manifest"], second["manifest"])
        self.assertEqual(first["audit"]["privacy_gate"], "passed")


class Response(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False


class GetJsonTests(unittest.TestCase):
    def test_gzip_body_is_decoded(self):
        body = gzip.compress(json.dumps({"ok": 1}).encode())
        self.assertEqual(get_json("https://x", opener=lambda request, timeout: Response(body)), {"ok": 1})

    def test_retries_then_fails_clearly(self):
        calls = []

        def opener(request, timeout):
            calls.append(1)
            raise URLError("down")

        with self.assertRaisesRegex(RuntimeError, "failed after 3 attempts"):
            get_json("https://x?secret=1", retries=2, opener=opener, sleeper=lambda seconds: None)
        self.assertEqual(len(calls), 3)


if __name__ == "__main__":
    unittest.main()
