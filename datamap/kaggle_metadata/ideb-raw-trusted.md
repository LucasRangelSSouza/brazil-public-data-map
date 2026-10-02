# IDEB (INEP): Raw and Trusted

16 tables, 1,925,765 rows, snapshot 2026-09-30. Observed IDEB against targets by school, municipality, state, region and Brazil, every two years. IDEB is the SAEB proficiency score times the flow indicator.

## Where the data comes from

- **Publisher:** Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP)
- **Official source:** https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/ideb
- **How it is fetched:** Spreadsheets published by INEP on the IDEB page, one set per edition.
- **Grain and keys:** School, municipality, state, region or Brazil by edition.

## How the files are organised

Every table is one Parquet file at the dataset root, named `<layer>__<table>.parquet`. `raw` is the source snapshot as delivered; `trusted` is typed, deduplicated and consistently named. `release_manifest.json` holds the SHA-256 and size of every file, `schemas.json` the schema of every table and `audit.json` the export counts.

## Documentation, field by field

- Interactive data map (search, lineage, joins): https://rangeltech.net/datamap/#/dataset/ideb-raw-trusted
- Data dictionary of this dataset, every column: https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/docs/datamap/ideb-raw-trusted.md
- How the raw layer is obtained from the official source (notebook): https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/notebooks/sources/ideb.ipynb
- Code and release contracts: https://github.com/LucasRangelSSouza/brazil-public-data-map

Column descriptions come from the source lake's catalogue, in Portuguese; a share is marked there as AI generated. They are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns |
|---|---|---:|---:|
| raw | `inep_ideb_brasil_anos_finais` | 15 | 122 |
| raw | `inep_ideb_brasil_anos_iniciais` | 16 | 133 |
| raw | `inep_ideb_brasil_ensino_medio` | 14 | 122 |
| raw | `inep_ideb_escola_anos_finais` | 48,020 | 126 |
| raw | `inep_ideb_escola_anos_iniciais` | 66,153 | 137 |
| raw | `inep_ideb_escola_ensino_medio` | 22,184 | 60 |
| raw | `inep_ideb_municipio_anos_finais` | 14,428 | 124 |
| raw | `inep_ideb_municipio_anos_iniciais` | 14,533 | 135 |
| raw | `inep_ideb_municipio_ensino_medio` | 11,765 | 58 |
| raw | `inep_ideb_regioes_ufs_anos_finais` | 141 | 122 |
| raw | `inep_ideb_regioes_ufs_anos_iniciais` | 142 | 133 |
| raw | `inep_ideb_regioes_ufs_ensino_medio` | 109 | 122 |
| trusted | `inep_ideb_brasil` | 154 | 13 |
| trusted | `inep_ideb_escola` | 1,366,823 | 21 |
| trusted | `inep_ideb_municipio` | 377,396 | 19 |
| trusted | `inep_ideb_regioes_ufs` | 3,872 | 15 |

## Read a table

```python
import kagglehub, pandas as pd
path = kagglehub.dataset_download("lucasrangelss/ideb-raw-trusted", path="raw__inep_ideb_brasil_anos_finais.parquet")
df = pd.read_parquet(path)
```

Values are published as held in the snapshot, without masking. Source terms apply; credit the original publisher.

My portfolio: https://rangeltech.net
