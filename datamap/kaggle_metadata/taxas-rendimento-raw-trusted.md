# School flow and distortion rates (INEP): Raw and Trusted

11 tables, 218,331,656 rows, snapshot 2026-10-02. Approval, failure and dropout rates and the age-grade distortion rate by school, municipality, state, region and Brazil, per year.

## Where the data comes from

- **Publisher:** Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP)
- **Official source:** https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais
- **How it is fetched:** Spreadsheets published by INEP in the educational indicators area.
- **Grain and keys:** School, municipality, state, region or Brazil by year.

## How the files are organised

Every table is one Parquet file at the dataset root, named `<layer>__<table>.parquet`. `raw` is the source snapshot as delivered; `trusted` is typed, deduplicated and consistently named. `release_manifest.json` holds the SHA-256 and size of every file, `schemas.json` the schema of every table and `audit.json` the export counts.

## Documentation, field by field

- Interactive data map (search, lineage, joins): https://lucas.rangeltech.net/datamap/#/dataset/taxas-rendimento-raw-trusted
- Data dictionary of this dataset, every column: https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/docs/datamap/taxas-rendimento-raw-trusted.md
- How the raw layer is obtained from the official source (notebook): https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/notebooks/sources/taxas-rendimento.ipynb
- Code and release contracts: https://github.com/LucasRangelSSouza/brazil-public-data-map

Column descriptions come from the source lake's catalogue, in Portuguese; a share is marked there as AI generated. They are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns |
|---|---|---:|---:|
| raw | `inep_taxa_distorcao_brasil_regioes_ufs` | 7,404 | 43 |
| raw | `inep_taxa_distorcao_escolas` | 2,148,217 | 48 |
| raw | `inep_taxa_distorcao_municipios` | 982,518 | 45 |
| raw | `inep_taxas_rendimento_escolar` | 3,974,168 | 71 |
| raw | `inep_taxas_rendimento_escolar_arquivos` | 54 | 11 |
| trusted | `inep_taxa_distorcao_brasil_regioes_ufs` | 7,356 | 24 |
| trusted | `inep_taxa_distorcao_escolas` | 2,148,183 | 27 |
| trusted | `inep_taxa_distorcao_municipios` | 982,486 | 25 |
| trusted | `inep_taxas_rendimento_escolar` | 3,974,168 | 71 |
| trusted | `inep_taxas_rendimento_escolar_long` | 204,107,094 | 25 |
| trusted | `inep_taxas_rendimento_escolar_qualidade` | 8 | 28 |

## Read a table

```python
import kagglehub, pandas as pd
path = kagglehub.dataset_download("lucasrangelss/taxas-rendimento-raw-trusted", path="raw__inep_taxa_distorcao_brasil_regioes_ufs.parquet")
df = pd.read_parquet(path)
```

Values are published as held in the snapshot, without masking. Source terms apply; credit the original publisher.

My portfolio: https://lucas.rangeltech.net
