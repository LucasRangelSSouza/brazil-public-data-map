# SAEB assessment (INEP): Analytics

8 tables, 1,682,209 rows, snapshot 2026-10-01. SAEB results: aggregated proficiency indicators, the school report-card API (boletim) for 2011 onward, and the assessment microdata tables released without student-level records.

## Where the data comes from

- **Publisher:** Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP)
- **Official source:** https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/saeb
- **How it is fetched:** Indicators up to 2023 are `.rar` files named `planilha_de_resultados_{year}.rar` on download.inep.gov.br/saeb/resultados/; from 2025 a single `.xlsx`. The link for each edition is on that year's sub-page of the SAEB results page.
- **Grain and keys:** Indicators: school, municipality, state or Brazil by edition. Boletim: school by edition. The publication format changes between editions, so each edition is validated against the live source.

## How the files are organised

Every table is one Parquet file at the dataset root, named `<layer>__<table>.parquet`. `semantic` tables join and reshape trusted tables for analysis; build them from the matching raw-and-trusted dataset. `release_manifest.json` holds the SHA-256 and size of every file, `schemas.json` the schema of every table and `audit.json` the export counts.

## Documentation, field by field

- Interactive data map (search, lineage, joins): https://lucas.rangeltech.net/datamap/#/dataset/saeb-analytics
- Data dictionary of this dataset, every column: https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/docs/datamap/saeb-analytics.md
- How the raw layer is obtained from the official source (notebook): https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/notebooks/sources/saeb.ipynb
- Code and release contracts: https://github.com/LucasRangelSSouza/brazil-public-data-map

Column descriptions come from the source lake's catalogue, in Portuguese; a share is marked there as AI generated. They are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns |
|---|---|---:|---:|
| semantic | `obt_api_saeb_boletim` | 603,449 | 69 |
| semantic | `obt_inep_saeb_indicadores_brasil_ano` | 453 | 176 |
| semantic | `obt_inep_saeb_indicadores_estado_ano` | 9,917 | 180 |
| semantic | `obt_inep_saeb_indicadores_historico_brasil_ano` | 24 | 80 |
| semantic | `obt_inep_saeb_indicadores_historico_estado_ano` | 714 | 85 |
| semantic | `obt_inep_saeb_indicadores_municipio_ano` | 540,927 | 116 |
| semantic | `obt_inep_saeb_micro_escola_ano` | 461,283 | 23 |
| semantic | `obt_inep_saeb_micro_municipio_ano` | 65,442 | 21 |

## Read a table

```python
import kagglehub, pandas as pd
path = kagglehub.dataset_download("lucasrangelss/saeb-analytics", path="semantic__obt_api_saeb_boletim.parquet")
df = pd.read_parquet(path)
```

Values are published as held in the snapshot, without masking. Source terms apply; credit the original publisher.

My portfolio: https://lucas.rangeltech.net
