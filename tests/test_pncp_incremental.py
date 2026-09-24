import unittest
from datetime import date
from io import BytesIO
from urllib.error import HTTPError, URLError

from brazil_data_map.pncp import fetch_publications, incremental_snapshot


class Response(BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.close()


class PncpIncrementalTests(unittest.TestCase):
    def test_publications_client_retries_paginates_and_minimizes_response_fields(self) -> None:
        pages = [
            URLError("temporary"),
            b'{"data":[{"numeroControlePNCP":"source-1","dataAtualizacao":"2026-01-02T00:00:00Z","dataPublicacaoPncp":"2026-01-02","objetoCompra":"paper","modalidadeId":6,"valorTotalEstimado":10,"orgaoEntidade":{"cnpj":"12345678000195","razaoSocial":"Public body"},"usuarioNome":"must not pass"}],"paginasRestantes":1}',
            b'{"data":[{"numeroControlePNCP":"source-2","dataAtualizacaoGlobal":"2026-01-03T00:00:00Z","objetoCompra":"pens","modalidadeId":6,"orgaoEntidade":{} }],"paginasRestantes":0}',
        ]

        def opener(*_, **__):
            response = pages.pop(0)
            if isinstance(response, Exception):
                raise response
            return Response(response)

        records = fetch_publications(date(2026, 1, 1), date(2026, 1, 2), 6, page_size=10, opener=opener)

        self.assertEqual([record["id"] for record in records], ["source-1", "source-2"])
        self.assertEqual(records[0]["contracting_organization_id"], "12345678000195")
        self.assertNotIn("usuarioNome", records[0])

    def test_rate_limit_uses_retry_after_before_retrying(self) -> None:
        calls = [HTTPError("https://example.test", 429, "rate limit", {"Retry-After": "3"}, None), b'{"data":[],"paginasRestantes":0}']
        delays = []

        def opener(*_, **__):
            item = calls.pop(0)
            if isinstance(item, Exception):
                raise item
            return Response(item)

        self.assertEqual(fetch_publications(date(2026, 1, 1), date(2026, 1, 1), 6, page_size=10, opener=opener, sleeper=delays.append), [])
        self.assertEqual(delays, [3.0])
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
