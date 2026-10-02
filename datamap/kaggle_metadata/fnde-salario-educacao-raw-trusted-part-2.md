# FNDE education contribution: Raw and Trusted

6 tables, 455,943 rows, snapshot 2026-10-02. Collection and distribution of the education contribution (salário-educação) published by FNDE.

## Where the data comes from

- **Publisher:** Fundo Nacional de Desenvolvimento da Educação (FNDE)
- **Official source:** https://www.fnde.gov.br/
- **How it is fetched:** Published by FNDE; the raw tables are the exports as delivered.
- **Grain and keys:** See each table.

## How the files are organised

Every table is one Parquet file at the dataset root, named `<layer>__<table>.parquet`. `raw` is the source snapshot as delivered; `trusted` is typed, deduplicated and consistently named. `release_manifest.json` holds the SHA-256 and size of every file, `schemas.json` the schema of every table and `audit.json` the export counts.

## Documentation, field by field

- Interactive data map (search, lineage, joins): https://lucas.rangeltech.net/datamap/#/dataset/fnde-salario-educacao-raw-trusted-part-2
- Data dictionary of this dataset, every column: https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/docs/datamap/fnde-salario-educacao-raw-trusted-part-2.md
- How the raw layer is obtained from the official source (notebook): https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/notebooks/sources/fnde-salario-educacao.ipynb
- Code and release contracts: https://github.com/LucasRangelSSouza/brazil-public-data-map

Column descriptions come from the source lake's catalogue, in Portuguese; a share is marked there as AI generated. They are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns |
|---|---|---:|---:|
| raw | `fnde_salario_educacao_realizado_2023` | 5,595 | 21 |
| raw | `fnde_salario_educacao_realizado_2024` | 5,595 | 21 |
| raw | `fnde_salario_educacao_realizado_2025` | 5,595 | 21 |
| raw | `fnde_salario_educacao_realizado_2026` | 5,596 | 21 |
| trusted | `fnde_salario_educacao_distribuido_mensal` | 338,835 | 12 |
| trusted | `fnde_salario_educacao_previsto` | 94,727 | 11 |

## Read a table

```python
import kagglehub, pandas as pd
path = kagglehub.dataset_download("lucasrangelss/fnde-salario-educacao-raw-trusted-part-2", path="raw__fnde_salario_educacao_realizado_2023.parquet")
df = pd.read_parquet(path)
```

Values are published as held in the snapshot, without masking. Source terms apply; credit the original publisher.

My portfolio: https://lucas.rangeltech.net
