# FNDE education contribution: Raw and Trusted

40 tables, 112,836 rows, snapshot 2026-09-30. Collection and distribution of the education contribution (salário-educação) published by FNDE.

## Where the data comes from

- **Publisher:** Fundo Nacional de Desenvolvimento da Educação (FNDE)
- **Official source:** https://www.fnde.gov.br/
- **How it is fetched:** Published by FNDE; the raw tables are the exports as delivered.
- **Grain and keys:** See each table.

## How the files are organised

Every table is one Parquet file at the dataset root, named `<layer>__<table>.parquet`. `raw` is the source snapshot as delivered; `trusted` is typed, deduplicated and consistently named. `release_manifest.json` holds the SHA-256 and size of every file, `schemas.json` the schema of every table and `audit.json` the export counts.

## Documentation, field by field

- Interactive data map (search, lineage, joins): https://rangeltech.net/datamap/#/dataset/fnde-salario-educacao-raw-trusted-part-1
- Data dictionary of this dataset, every column: https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/docs/datamap/fnde-salario-educacao-raw-trusted-part-1.md
- How the raw layer is obtained from the official source (notebook): https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/notebooks/sources/fnde-salario-educacao.ipynb
- Code and release contracts: https://github.com/LucasRangelSSouza/brazil-public-data-map

Column descriptions come from the source lake's catalogue, in Portuguese; a share is marked there as AI generated. They are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns |
|---|---|---:|---:|
| raw | `fnde_salario_educacao_previsto_2010` | 5,589 | 11 |
| raw | `fnde_salario_educacao_previsto_2011` | 5,589 | 11 |
| raw | `fnde_salario_educacao_previsto_2012` | 5,590 | 11 |
| raw | `fnde_salario_educacao_previsto_2013` | 5,590 | 11 |
| raw | `fnde_salario_educacao_previsto_2014` | 5,595 | 11 |
| raw | `fnde_salario_educacao_previsto_2015` | 5,595 | 11 |
| raw | `fnde_salario_educacao_previsto_2016` | 5,595 | 11 |
| raw | `fnde_salario_educacao_previsto_2017` | 5,595 | 11 |
| raw | `fnde_salario_educacao_previsto_2018` | 5,595 | 11 |
| raw | `fnde_salario_educacao_previsto_2019` | 5,595 | 11 |
| raw | `fnde_salario_educacao_previsto_2020` | 5,595 | 11 |
| raw | `fnde_salario_educacao_previsto_2021` | 5,595 | 11 |
| raw | `fnde_salario_educacao_previsto_2022` | 5,595 | 11 |
| raw | `fnde_salario_educacao_previsto_2023` | 5,595 | 11 |
| raw | `fnde_salario_educacao_previsto_2024` | 5,595 | 11 |
| raw | `fnde_salario_educacao_previsto_2025` | 5,595 | 11 |
| raw | `fnde_salario_educacao_previsto_2026` | 5,596 | 11 |
| raw | `fnde_salario_educacao_realizado_2000` | 24 | 21 |
| raw | `fnde_salario_educacao_realizado_2001` | 23 | 21 |
| raw | `fnde_salario_educacao_realizado_2002` | 24 | 21 |
| raw | `fnde_salario_educacao_realizado_2003` | 24 | 21 |
| raw | `fnde_salario_educacao_realizado_2004` | 54 | 21 |
| raw | `fnde_salario_educacao_realizado_2005` | 54 | 21 |
| raw | `fnde_salario_educacao_realizado_2006` | 54 | 21 |
| raw | `fnde_salario_educacao_realizado_2007` | 54 | 21 |
| raw | `fnde_salario_educacao_realizado_2008` | 54 | 21 |
| raw | `fnde_salario_educacao_realizado_2009` | 52 | 21 |
| raw | `fnde_salario_educacao_realizado_2010` | 54 | 21 |
| raw | `fnde_salario_educacao_realizado_2011` | 54 | 21 |
| raw | `fnde_salario_educacao_realizado_2012` | 54 | 21 |
| raw | `fnde_salario_educacao_realizado_2013` | 54 | 21 |
| raw | `fnde_salario_educacao_realizado_2014` | 54 | 21 |
| raw | `fnde_salario_educacao_realizado_2015` | 54 | 21 |
| raw | `fnde_salario_educacao_realizado_2016` | 54 | 21 |
| raw | `fnde_salario_educacao_realizado_2017` | 54 | 21 |
| raw | `fnde_salario_educacao_realizado_2018` | 54 | 21 |
| raw | `fnde_salario_educacao_realizado_2019` | 54 | 21 |
| raw | `fnde_salario_educacao_realizado_2020` | 5,594 | 21 |
| raw | `fnde_salario_educacao_realizado_2021` | 5,596 | 21 |
| raw | `fnde_salario_educacao_realizado_2022` | 5,595 | 21 |

## Read a table

```python
import kagglehub, pandas as pd
path = kagglehub.dataset_download("lucasrangelss/fnde-salario-educacao-raw-trusted-part-1", path="raw__fnde_salario_educacao_previsto_2010.parquet")
df = pd.read_parquet(path)
```

Values are published as held in the snapshot, without masking. Source terms apply; credit the original publisher.

My portfolio: https://rangeltech.net
