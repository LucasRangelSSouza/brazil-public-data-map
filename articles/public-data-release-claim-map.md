# Claim-to-evidence map: public data release boundary

| Claim | Evidence | Status |
|---|---|---|
| PNCP exposes open-data access intended for consultation and download. | [PNCP open-data page](https://www.gov.br/pncp/pt-br/acesso-a-informacao/dados-abertos) describes public access without login for consultations. | supported |
| Public availability does not remove a publisher's privacy responsibilities. | [INEP microdata guidance](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados) describes privacy controls and restrictions on releases that can identify people. | supported |
| This repository rejects direct identifiers before constructing layers. | `brazil_data_map/privacy.py`, `brazil_data_map/audit.py`, and the passing fixture tests. | supported |
| A valid local manifest records source lineage and package hashes. | `brazil_data_map/release.py` and `tests/test_manifest.py`. | supported |
| The repository is a legal certification or a published historical dataset. | No evidence. The article explicitly does not make this claim. | excluded |
