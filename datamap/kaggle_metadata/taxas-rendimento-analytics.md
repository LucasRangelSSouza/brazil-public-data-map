# School flow and distortion rates (INEP): Analytics

10 tables, 5,003,248 rows, snapshot 2026-10-01. Approval, failure and dropout rates and the age-grade distortion rate by school, municipality, state, region and Brazil, per year.

## Where the data comes from

- **Publisher:** Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP)
- **Official source:** https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais
- **How it is fetched:** Spreadsheets published by INEP in the educational indicators area.
- **Grain and keys:** School, municipality, state, region or Brazil by year.

## How the files are organised

Every table is one Parquet file at the dataset root, named `<layer>__<table>.parquet`. `semantic` tables join and reshape trusted tables for analysis; build them from the matching raw-and-trusted dataset. `release_manifest.json` holds the SHA-256 and size of every file, `schemas.json` the schema of every table and `audit.json` the export counts.

## Documentation, field by field

- Interactive data map (search, lineage, joins): https://rangeltech.net/datamap/#/dataset/taxas-rendimento-analytics
- Data dictionary of this dataset, every column: https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/docs/datamap/taxas-rendimento-analytics.md
- How the raw layer is obtained from the official source (notebook): https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/notebooks/sources/taxas-rendimento.ipynb
- Code and release contracts: https://github.com/LucasRangelSSouza/brazil-public-data-map

Column descriptions come from the source lake's catalogue, in Portuguese; a share is marked there as AI generated. They are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns |
|---|---|---:|---:|
| semantic | `obt_inep_taxa_distorcao_brasil_ano` | 90 | 20 |
| semantic | `obt_inep_taxa_distorcao_escola_ano` | 2,148,183 | 31 |
| semantic | `obt_inep_taxa_distorcao_municipio_ano` | 81,730 | 26 |
| semantic | `obt_inep_taxa_distorcao_regiao_ano` | 300 | 22 |
| semantic | `obt_inep_taxa_distorcao_uf_ano` | 3,332 | 23 |
| semantic | `obt_inep_taxa_rendimento_brasil_ano` | 342 | 16 |
| semantic | `obt_inep_taxa_rendimento_escola_ano` | 2,652,720 | 25 |
| semantic | `obt_inep_taxa_rendimento_municipio_ano` | 105,799 | 21 |
| semantic | `obt_inep_taxa_rendimento_regiao_ano` | 1,710 | 18 |
| semantic | `obt_inep_taxa_rendimento_uf_ano` | 9,042 | 19 |

## Read a table

```python
import kagglehub, pandas as pd
path = kagglehub.dataset_download("lucasrangelss/taxas-rendimento-analytics", path="semantic__obt_inep_taxa_distorcao_brasil_ano.parquet")
df = pd.read_parquet(path)
```

Values are published as held in the snapshot, without masking. Source terms apply; credit the original publisher.

My portfolio: https://rangeltech.net
