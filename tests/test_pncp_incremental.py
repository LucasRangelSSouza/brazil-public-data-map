import unittest
from datetime import date
from io import BytesIO
from urllib.error import HTTPError, URLError

from brazil_data_map.pncp import enrich_procurement_items, fetch_procurement_items, fetch_publications, incremental_snapshot, normalize_publication


class Response(BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.close()


class PncpIncrementalTests(unittest.TestCase):
    def test_item_enrichment_carries_only_approved_parent_context(self) -> None:
        parent = {
            "id": "source-1", "updated_at": "2026-01-02T00:00:00Z", "published_at": "2026-01-01",
            "proposal_deadline_at": "2026-01-10T18:00:00-03:00", "procurement_year": 2026,
            "procurement_sequence": 42, "modality_id": 6, "estimated_value": 100,
            "contracting_organization_id": "12345678000195", "contracting_organization_name": "Public body",
            "item": "source text must not pass",
        }

        def item_fetcher(*_):
            return [{"id": "source-1:item:2", "procurement_id": "source-1", "item_number": 2, "item_kind": "S", "item_quantity": 3.0, "item_unit": "licenca", "item_category": "technology"}]

        records = enrich_procurement_items([parent], item_fetcher=item_fetcher)

        self.assertEqual(records[0]["id"], "source-1:item:2")
        self.assertEqual(records[0]["proposal_deadline_at"], "2026-01-10T18:00:00-03:00")
        self.assertNotIn("item", records[0])

    def test_item_enrichment_blocks_a_parent_without_item_route_keys(self) -> None:
        with self.assertRaisesRegex(ValueError, "organization id"):
            enrich_procurement_items([{"id": "source-1", "updated_at": "2026-01-02T00:00:00Z", "procurement_year": 2026, "procurement_sequence": 42}])

    def test_item_client_paginates_and_emits_a_safe_item_grain(self) -> None:
        pages = [
            b'{"data":[{"numeroItem":2,"materialOuServico":"S","descricao":"software educacional","quantidade":3,"unidadeMedida":"licenca"}],"paginasRestantes":1}',
            b'{"data":[{"numeroItem":3,"materialOuServico":"M","descricao":"paper","quantidade":10,"unidadeMedida":"caixa"}],"paginasRestantes":0}',
        ]

        def opener(*_, **__):
            return Response(pages.pop(0))

        records = fetch_procurement_items(
            "12345678000195", 2026, 42, "source-1", page_size=10, opener=opener
        )

        self.assertEqual([record["id"] for record in records], ["source-1:item:2", "source-1:item:3"])
        self.assertEqual(records[0]["item_category"], "technology")
        self.assertEqual(records[0]["item_kind"], "S")
        self.assertNotIn("descricao", records[0])

    def test_item_client_rejects_identifier_like_units(self) -> None:
        def opener(*_, **__):
            return Response(b'{"data":[{"numeroItem":1,"materialOuServico":"M","descricao":"paper","quantidade":1,"unidadeMedida":"person@example.org"}],"paginasRestantes":0}')

        with self.assertRaisesRegex(ValueError, "item unit"):
            fetch_procurement_items("12345678000195", 2026, 42, "source-1", page_size=10, opener=opener)

    def test_item_client_accepts_a_direct_list_response(self) -> None:
        def opener(*_, **__):
            return Response(b'[{"numeroItem":1,"materialOuServico":"M","descricao":"paper","quantidade":1,"unidadeMedida":"box"}]')

        records = fetch_procurement_items("12345678000195", 2026, 42, "source-1", page_size=10, opener=opener)

        self.assertEqual(records[0]["id"], "source-1:item:1")

    def test_publication_normalization_keeps_a_proposal_deadline_without_source_links(self) -> None:
        record = normalize_publication({
            "numeroControlePNCP": "source-1",
            "dataAtualizacao": "2026-01-02T00:00:00Z",
            "dataEncerramentoProposta": "2026-01-10T18:00:00-03:00",
            "orgaoEntidade": {"cnpj": "12345678000195"},
            "linkSistemaOrigem": "https://example.invalid/private-process",
        })

        self.assertEqual(record["proposal_deadline_at"], "2026-01-10T18:00:00-03:00")
        self.assertNotIn("source_record_url", record)

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
