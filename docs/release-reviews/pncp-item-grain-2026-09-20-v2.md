# Release approval: Brazil PNCP Procurement History, version 3

## Candidate and provenance

This candidate adds a second, explicitly bounded package to the existing Kaggle dataset. It covers PNCP publications dated **2026-09-20**, modality **6**, at procurement-item grain. It contains 25 deduplicated parent procurements and 513 item records in each of the raw, trusted, and semantic layers. It does not claim historical completeness, procurement eligibility, supplier suitability, or a production recommendation result.

| Input | Identity |
| --- | --- |
| Candidate manifest | SHA-256 `15610ca71e2b23c5c622272c8f38d2fc276b20d229e5709b58ad47467935528f` |
| Source input digest | SHA-256 `7eb9d048ec5681664e90b6b0c60621ae8ad951828dbc4c3915816c123e80bc82` |
| Extractor revision | `1cb4316` |
| Official sources | PNCP public publication and documented item routes |
| Retrieval timestamp | `2026-09-28T00:00:00Z` |

The candidate retains only an item identifier, controlled material-or-service code, non-negative quantity, bounded unit, controlled category, and selected procurement context, including proposal deadline where supplied. It excludes the source item description, notice objects, URLs, documents, contacts, addresses, supplier-result data, and any direct personal identifier.

## Source and redistribution assessment

The PNCP FAQ, checked on 2026-09-28, identifies PNCP information as public and freely accessible, and identifies open-data resources for consultation, reuse, and technical integration. The federal open-data policy defines open data as data under an open licence that permits free use, consumption, or combination subject only to crediting authorship or source; it also provides for free use of federal-government data and active-transparency information. See the [PNCP FAQ](https://www.gov.br/pncp/pt-br/pncp/perguntas-e-respostas/) and [Decree 8,777/2016](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2016/decreto/d8777.htm).

This is a source-specific, limited release decision for the fields and coverage above. The Kaggle package uses the `other` licence setting, credits PNCP as the source, and asserts no new licence over PNCP data. Apache-2.0 applies only to this repository's code and documentation. The release does not redistribute unreviewed documents or free text.

## Controls and result

The privacy audit found zero violations. The first candidate build retained an ignored normalized-item capture only after the complete bounded run. A second build reused that local normalized capture without a live item request and produced the same manifest and every declared file hash. The supporting record is [PNCP v2 item candidate evidence](../evidence/pncp-v2-item-candidate-2026-09-28.md).

Before the dataset card or any consumer pin is changed, the release package must contain this approval, the candidate manifest, privacy audit, and all three Parquet layers. After upload, a clean unauthenticated Kaggle download must reproduce every manifest hash.

## Decision

Approved by the release owner, Lucas Rangel, under the standing portfolio-delivery authorization, for this narrow Kaggle version. This decision does not approve another date, modality, source field, source route, or model claim. Any change requires a new candidate, privacy audit, deterministic comparison, and release review.
