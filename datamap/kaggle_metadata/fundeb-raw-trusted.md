# FUNDEB: Raw and Trusted

14 tables, 10,107,275 rows, snapshot 2026-09-30. The FUNDEB panel: complementation by VAAF, VAAT and VAAR, distribution, qualification and indicators per entity and year.

## Where the data comes from

- **Publisher:** Fundo Nacional de Desenvolvimento da Educação (FNDE)
- **Official source:** https://www.fnde.gov.br/
- **How it is fetched:** Published by FNDE as the FUNDEB panel; the raw tables are the panel exports as delivered.
- **Grain and keys:** One row per federal entity (state or municipality) and year for the panel tables.

## How the files are organised

Every table is one Parquet file at the dataset root, named `<layer>__<table>.parquet`. `raw` is the source snapshot as delivered; `trusted` is typed, deduplicated and consistently named. `release_manifest.json` holds the SHA-256 and size of every file, `schemas.json` the schema of every table and `audit.json` the export counts.

## Documentation, field by field

- Interactive data map (search, lineage, joins): https://rangeltech.net/datamap/#/dataset/fundeb-raw-trusted
- Data dictionary of this dataset, every column: https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/docs/datamap/fundeb-raw-trusted.md
- How the raw layer is obtained from the official source (notebook): https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/notebooks/sources/fundeb.ipynb
- Code and release contracts: https://github.com/LucasRangelSSouza/brazil-public-data-map

Column descriptions come from the source lake's catalogue, in Portuguese; a share is marked there as AI generated. They are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns |
|---|---|---:|---:|
| raw | `fnde_fundeb_painel_complementacao` | 106,300 | 25 |
| raw | `fnde_fundeb_painel_cronograma_vaat` | 23,246 | 23 |
| raw | `fnde_fundeb_painel_dim_entes` | 27,980 | 14 |
| raw | `fnde_fundeb_painel_distribuicao` | 4,362,779 | 12 |
| raw | `fnde_fundeb_painel_hab_vaar` | 268,712 | 10 |
| raw | `fnde_fundeb_painel_hab_vaat` | 55,955 | 9 |
| raw | `fnde_fundeb_painel_indicadores` | 983,302 | 10 |
| trusted | `fundeb_painel_complementacao` | 83,916 | 25 |
| trusted | `fundeb_painel_cronograma_vaat` | 13,030 | 23 |
| trusted | `fundeb_painel_dim_entes` | 5,570 | 14 |
| trusted | `fundeb_painel_distribuicao` | 3,382,306 | 15 |
| trusted | `fundeb_painel_habilitacao_vaar` | 134,352 | 11 |
| trusted | `fundeb_painel_habilitacao_vaat` | 33,571 | 10 |
| trusted | `fundeb_painel_indicadores_siope` | 626,256 | 10 |

## Read a table

```python
import kagglehub, pandas as pd
path = kagglehub.dataset_download("lucasrangelss/fundeb-raw-trusted", path="raw__fnde_fundeb_painel_complementacao.parquet")
df = pd.read_parquet(path)
```

Values are published as held in the snapshot, without masking. Source terms apply; credit the original publisher.

My portfolio: https://rangeltech.net
