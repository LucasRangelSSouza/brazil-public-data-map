# SIOPE education finance: Analytics

16 tables, 365,591,796 rows, snapshot 2026-10-02. Education revenue, expenditure and indicators reported by municipalities and states, from the SIOPE open-data API (Olinda), the FNDE SIOPE exports, and the budget execution report (RREO) PDFs parsed into tables.

## Where the data comes from

- **Publisher:** Fundo Nacional de Desenvolvimento da Educação (FNDE)
- **Official source:** https://www.fnde.gov.br/siope/
- **How it is fetched:** The open-data API is an OData service at https://www.fnde.gov.br/olinda-ide/servico/DADOS_ABERTOS_SIOPE/versao/v1/odata. The RREO reports are PDFs published by FNDE and parsed into tables.
- **Grain and keys:** Municipality (or state) by year and reporting period. Indicator rows repeat by `num_periodo`, so analyses keep the latest period per municipality and year. Municipality joins to IBGE through `codigo_municipio`.

## How the files are organised

Every table is one Parquet file at the dataset root, named `<layer>__<table>.parquet`. `semantic` tables join and reshape trusted tables for analysis; build them from the matching raw-and-trusted dataset. `release_manifest.json` holds the SHA-256 and size of every file, `schemas.json` the schema of every table and `audit.json` the export counts.

## Documentation, field by field

- Interactive data map (search, lineage, joins): https://lucas.rangeltech.net/datamap/#/dataset/siope-analytics
- Data dictionary of this dataset, every column: https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/docs/datamap/siope-analytics.md
- How the raw layer is obtained from the official source (notebook): https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/notebooks/sources/siope.ipynb
- Code and release contracts: https://github.com/LucasRangelSSouza/brazil-public-data-map

Column descriptions come from the source lake's catalogue, in Portuguese; a share is marked there as AI generated. They are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns |
|---|---|---:|---:|
| semantic | `obt_api_olinda_siope_comparativo_municipio_par_anos` | 1,984,229 | 159 |
| semantic | `obt_api_olinda_siope_comparativo_uf_par_anos` | 9,073 | 158 |
| semantic | `obt_api_olinda_siope_indicadores_municipio_ano` | 105,073 | 51 |
| semantic | `obt_api_olinda_siope_indicadores_municipio_bimestre` | 316,538 | 25 |
| semantic | `obt_api_olinda_siope_indicadores_uf_ano` | 491 | 50 |
| semantic | `obt_api_olinda_siope_indicadores_uf_bimestre` | 1,433 | 21 |
| semantic | `obt_fnde_siope_dados_gerais_municipio_ano` | 166,293 | 29 |
| semantic | `obt_fnde_siope_despesa_educacao_municipio_ano` | 135,140,891 | 18 |
| semantic | `obt_fnde_siope_despesa_funcao_municipio_ano` | 1,191,974 | 13 |
| semantic | `obt_fnde_siope_indicador_municipio_ano` | 6,411,059 | 12 |
| semantic | `obt_fnde_siope_info_complementar_municipio_ano` | 8,322,693 | 11 |
| semantic | `obt_fnde_siope_receita_municipio_ano` | 14,236,762 | 14 |
| semantic | `obt_rreo_siope_municipio_ano` | 42,649,158 | 16 |
| semantic | `obt_rreo_siope_municipio_bimestre` | 154,132,717 | 17 |
| semantic | `obt_rreo_siope_uf_ano` | 197,542 | 16 |
| semantic | `obt_rreo_siope_uf_bimestre` | 725,870 | 17 |

## Read a table

```python
import kagglehub, pandas as pd
path = kagglehub.dataset_download("lucasrangelss/siope-analytics", path="semantic__obt_api_olinda_siope_comparativo_municipio_par_anos.parquet")
df = pd.read_parquet(path)
```

Values are published as held in the snapshot, without masking. Source terms apply; credit the original publisher.

My portfolio: https://lucas.rangeltech.net
