# Censo Escolar aggregate candidate for education release version 2

## Decision

Version 2 will use the municipality-level INEP Statistical Synopsis of Basic Education. The source can enrich the SIOPE municipality-year release without distributing school, student, teacher, contact, or address records.

The first candidate is 2023 table **1.2**, `Number of enrollments in Basic Education by location and administrative dependency`. It provides `basic_education_enrollment_total` from the total-enrollment column. The semantic key remains `<municipality_code>-<year>`.

## Why the synopsis is the source boundary

INEP's public microdata catalogue lists annual Censo Escolar packages. Its broader microdata page explains that publication applies privacy controls because the underlying collections contain detailed records. The 2023 statistical synopsis is a published table set organised by region, state, and municipality and available in ODS and XLSX formats.

The published municipal aggregate avoids processing or redistributing detailed source records. It still needs the same release gate as every other candidate.

## Source record

| Item | Value |
|---|---|
| Publisher | Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP) |
| Landing page | https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/sinopses-estatisticas/educacao-basica |
| 2023 package | https://download.inep.gov.br/dados_abertos/sinopses_estatisticas/sinopse_estatistica_censo_escolar_2023.zip |
| Package content | ODS and XLSX workbook |
| Candidate worksheet | `1.2` |
| Source grain | municipality and reporting year |
| Capture check | 2026-09-27; HTTP `Content-Length` 151,568,286 bytes; ZIP archive listing verified |

## Proposed field contract

| Output field | Source location | Rule |
|---|---|---|
| `year` | package edition | fixed to 2023 for this candidate |
| `municipality_code` | worksheet `1.2`, `Código do Município` | normalize to the seven-digit IBGE code; reject missing or non-municipal aggregate rows |
| `basic_education_enrollment_total` | worksheet `1.2`, `Total` under `Número de Matrículas da Educação Básica` | require a non-negative integer |
| `source_table` | pipeline constant | `1.2` |
| `source_year` | pipeline constant | `2023` |

The builder may add lineage fields already used by the education release. It must not add names, addresses, school codes, school characteristics, teacher counts, demographic breakdowns, free text, or a field not listed in the approved allowlist.

## Acceptance gates

1. Download the package with an expected byte count and validate the ZIP before parsing.
2. Read the exact worksheet by name and reject a changed title, missing columns, duplicate municipal code, malformed code, or negative enrollment count.
3. Keep only municipal rows. National, regional, and state totals must fail the municipality record validator so they cannot enter the output.
4. Join only on the canonical IBGE municipality code. A missing or ambiguous join blocks the build.
5. Produce raw, trusted, and semantic layers from the same reviewed capture. Compare two builds for identical manifests and file hashes.
6. Run the release privacy audit and a field-level schema diff. Publish nothing until a new approval record and clean-download verification exist.

## Limits and follow-up

The first candidate covers 2023 only. It is not a backfill for 2019 through 2022, an estimate of enrollment, or a claim about educational quality. Earlier editions require their own workbook compatibility check because sheet names and layouts can change. A later version may add a small number of additional aggregate fields only after an explicit contract and review.

## Evidence links

- [INEP Statistical Synopsis landing page](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/sinopses-estatisticas/educacao-basica)
- [2023 synopsis catalogue entry](https://riep.inep.gov.br/items/cff7bc02-c5c3-4b21-b73e-2fcf78f9405c)
- [INEP Censo Escolar microdata catalogue](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar)
