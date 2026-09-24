# Source catalog

The catalog records a source's public entry point and analytical grain. It is not a promise that every source can be redistributed in the same form. A release owner records the source version, retrieval window, terms review, and field-level treatment before distributing a package.

| Source | Official entry point | Intended analytical grain | Release treatment |
|---|---|---|---|
| IBGE localities | [IBGE locality API](https://servicodados.ibge.gov.br/api/docs/localidades) | Municipality reference | Reference metadata; record version and retrieval time. |
| INEP School Census | [School Census microdata](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar) | Documented municipality-year aggregate | Do not assume person-level fields are releasable. Apply the publisher's privacy guidance. |
| INEP SAEB | [SAEB microdata](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/saeb) | Documented aggregate by period and geography | Keep the original documentation with each reviewed release. |
| FNDE SIOPE | [SIOPE portal](https://www.fnde.gov.br/siope/) | Municipality-year finance | Record the reporting period and definitions used by the extraction. |
| PNCP | [PNCP open data](https://www.gov.br/pncp/pt-br/acesso-a-informacao/dados-abertos) | Contracting unit, item, and publication date | Run the identifier policy, privacy audit, and release contract. |

The registry also records separate INEP IDEB and SAEB indicator sources. Their releases require methodology, coverage, aggregation, and redistribution review before they enter a public dataset. The registry does not treat published source availability as a blanket permission to redistribute raw files.

## Source review checklist

Before a release, confirm the current official URL, the applicable terms, the retrieval window, the grain, expected keys, and data fields that must be removed. Do not carry assumptions from an earlier release into a newer source version.

## PNCP publication adapter

The local PNCP adapter calls the documented public publication route, `GET /api/consulta/v1/contratacoes/publicacao`, with a bounded date range, modality code, page, and page size. The [official PNCP manuals](https://www.gov.br/pncp/pt-br/pncp/manuais) remain the authority for route behavior and fields. The adapter normalizes a selected analytical subset, paginates according to the response, and keeps no credential path.
