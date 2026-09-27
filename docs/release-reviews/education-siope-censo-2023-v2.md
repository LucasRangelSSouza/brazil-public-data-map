# Release approval: Brazil Education Data Lake, version 2

## Candidate and provenance

This candidate extends the published education version 1 with one approved municipal aggregate from the 2023 INEP Statistical Synopsis of Basic Education. It retains the version-1 records and adds `basic_education_enrollment_total`, `censo_source_table`, and `censo_source_year`. The new fields are populated only for 2023.

| Input | Identity |
|---|---|
| Published base manifest | SHA-256 `44f259602a688432dddbae6b0306a6957514a634d57d94a0abd3cff30f4b3506` |
| INEP 2023 ZIP | SHA-256 `6a29e549ea381ccb74a8b0aeec8b7fd1e4ec00c43bb83eae3ecc5c91bd7a88f5` |
| Candidate manifest | SHA-256 `311ffebae83b6ccac3d423703b77acb96e6de5ca7c4a86cc9c82881b719caa86d` |
| INEP source | https://download.inep.gov.br/dados_abertos/sinopses_estatisticas/sinopse_estatistica_censo_escolar_2023.zip |
| Extraction table | `1.2`, municipality total basic-education enrolment |

## Controls and result

The extractor validates the XLSX ZIP and the approved worksheet layout, then accepts only seven-digit municipal codes and non-negative integer totals. It does not read school, student, teacher, contact, address, or free-text fields.

The source reconciliation matched 5,566 SIOPE municipality-year records in 2023. Four Censo aggregate rows had no SIOPE record and were not added. All other release years carry explicit nulls for the new fields. Each raw, trusted, and semantic layer contains 27,830 records. The privacy audit passed.

Two independent candidate builds must have identical manifests before upload. The final release package must include this approval, the candidate manifest, the privacy audit, and the three Parquet layers. After upload, a clean Kaggle download must match every manifest hash before the dataset card or consumer pins are updated.

## Decision

Approved by the release owner, Lucas Rangel, under the standing portfolio-delivery authorization, for the narrowly defined candidate above. This approval does not authorize additional INEP fields, a later Censo edition, or a model claim. Any such change requires a new review.
