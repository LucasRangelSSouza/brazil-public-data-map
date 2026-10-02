# IDEB (INEP): Analytics

4 tables, 981,919 rows, snapshot 2026-09-30. Observed IDEB against targets by school, municipality, state, region and Brazil, every two years. IDEB is the SAEB proficiency score times the flow indicator.

## Where the data comes from

- **Publisher:** Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP)
- **Official source:** https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/ideb
- **How it is fetched:** Spreadsheets published by INEP on the IDEB page, one set per edition.
- **Grain and keys:** School, municipality, state, region or Brazil by edition.

## How the files are organised

Every table is one Parquet file at the dataset root, named `<layer>__<table>.parquet`. `semantic` tables join and reshape trusted tables for analysis; build them from the matching raw-and-trusted dataset. `release_manifest.json` holds the SHA-256 and size of every file, `schemas.json` the schema of every table and `audit.json` the export counts.

## Documentation, field by field

- Interactive data map (search, lineage, joins): https://lucas.rangeltech.net/datamap/#/dataset/ideb-analytics
- Data dictionary of this dataset, every column: https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/docs/datamap/ideb-analytics.md
- How the raw layer is obtained from the official source (notebook): https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/notebooks/sources/ideb.ipynb
- Code and release contracts: https://github.com/LucasRangelSSouza/brazil-public-data-map

Column descriptions come from the source lake's catalogue, in Portuguese; a share is marked there as AI generated. They are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns |
|---|---|---:|---:|
| semantic | `obt_inep_ideb_brasil_ano` | 55 | 21 |
| semantic | `obt_inep_ideb_escola_ano` | 798,779 | 24 |
| semantic | `obt_inep_ideb_municipio_ano` | 181,677 | 31 |
| semantic | `obt_inep_ideb_regiao_ano` | 1,408 | 29 |

## Read a table

```python
import kagglehub, pandas as pd
path = kagglehub.dataset_download("lucasrangelss/ideb-analytics", path="semantic__obt_inep_ideb_brasil_ano.parquet")
df = pd.read_parquet(path)
```

Values are published as held in the snapshot, without masking. Source terms apply; credit the original publisher.

My portfolio: https://lucas.rangeltech.net
