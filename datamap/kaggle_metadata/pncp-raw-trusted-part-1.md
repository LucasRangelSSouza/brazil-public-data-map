# PNCP public procurement: Raw and Trusted

40 tables, 213,700,826 rows, snapshot 2026-09-30. Procurement notices (including editais), contracts, price-registration records (atas) and annual procurement plans (PCA) with their items, published through the PNCP consultation API.

## Where the data comes from

- **Publisher:** Portal Nacional de Contratações Públicas (PNCP)
- **Official source:** https://pncp.gov.br/api/consulta/v1
- **How it is fetched:** Public REST API, no key. Four domains are read through the `/atualizacao` axis so a window returns everything that entered or changed: `contratacoes/atualizacao`, `contratos/atualizacao`, `atas/atualizacao`, `pca/atualizacao`. Notices require the modality code (loop 1..19) and a page size of at most 50; the plan endpoint uses `dataInicio`/`dataFim`.
- **Grain and keys:** One row per natural key, keeping the latest version by `dataAtualizacaoGlobal`: `numero_controle_pncp` for notices and contracts, `numero_controle_pncp_ata` for atas, `id_pca_pncp` for plans. Municipality is reachable through `unidade_codigo_ibge` (IBGE code).

## How the files are organised

Every table is one Parquet file at the dataset root, named `<layer>__<table>.parquet`. `raw` is the source snapshot as delivered; `trusted` is typed, deduplicated and consistently named. `release_manifest.json` holds the SHA-256 and size of every file, `schemas.json` the schema of every table and `audit.json` the export counts.

## Documentation, field by field

- Interactive data map (search, lineage, joins): https://lucas.rangeltech.net/datamap/#/dataset/pncp-raw-trusted-part-1
- Data dictionary of this dataset, every column: https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/docs/datamap/pncp-raw-trusted-part-1.md
- How the raw layer is obtained from the official source (notebook): https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/notebooks/sources/pncp.ipynb
- Code and release contracts: https://github.com/LucasRangelSSouza/brazil-public-data-map

Column descriptions come from the source lake's catalogue, in Portuguese; a share is marked there as AI generated. They are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns |
|---|---|---:|---:|
| raw | `pncp_atas_atualizacao` | 2,723,277 | 10 |
| raw | `pncp_contratacoes_arquivos` | 4,045,882 | 7 |
| raw | `pncp_contratacoes_atualizacao` | 7,719,898 | 10 |
| raw | `pncp_contratacoes_historico` | 68,610,105 | 7 |
| raw | `pncp_contratacoes_itens` | 25,595,585 | 7 |
| raw | `pncp_contratacoes_itens_resultados` | 4,004,953 | 7 |
| raw | `pncp_contratacoes_proposta` | 74,088 | 6 |
| raw | `pncp_contratos_atualizacao` | 10,275,091 | 10 |
| raw | `pncp_contratos_termos` | 382,798 | 7 |
| raw | `pncp_instrumentos_cobranca` | 769,359 | 6 |
| raw | `pncp_orgaos` | 45,594 | 7 |
| raw | `pncp_orgaos_unidades` | 409,469 | 7 |
| raw | `pncp_pca_atualizacao` | 147,425 | 10 |
| trusted | `pncp_atas` | 1,078,249 | 25 |
| trusted | `pncp_contratacoes` | 3,768,885 | 43 |
| trusted | `pncp_contratacoes_arquivos` | 3,289,351 | 9 |
| trusted | `pncp_contratacoes_historico` | 51,038,072 | 10 |
| trusted | `pncp_contratacoes_itens` | 20,890,388 | 15 |
| trusted | `pncp_contratacoes_itens_resultados` | 3,393,191 | 13 |
| trusted | `pncp_contratacoes_proposta` | 70 | 19 |
| trusted | `pncp_contratos` | 3,435,513 | 50 |
| trusted | `pncp_contratos_termos` | 310,593 | 13 |
| trusted | `pncp_dom_amparos_legais` | 183 | 12 |
| trusted | `pncp_dom_catalogos` | 2 | 8 |
| trusted | `pncp_dom_categoria_item_pca` | 8 | 7 |
| trusted | `pncp_dom_criterios_julgamento` | 9 | 7 |
| trusted | `pncp_dom_fontes_orcamentarias` | 6 | 7 |
| trusted | `pncp_dom_modalidades` | 19 | 7 |
| trusted | `pncp_dom_modos_disputa` | 6 | 7 |
| trusted | `pncp_dom_portes_empresa` | 6 | 7 |
| trusted | `pncp_dom_tipos_contrato` | 12 | 7 |
| trusted | `pncp_dom_tipos_documento` | 20 | 10 |
| trusted | `pncp_dom_tipos_instrumento_cobranca` | 1 | 7 |
| trusted | `pncp_dom_tipos_instrumento_convocatorio` | 5 | 9 |
| trusted | `pncp_dom_tipos_parte_envolvida` | 3 | 4 |
| trusted | `pncp_editais_embeddings` | 1,249,424 | 8 |
| trusted | `pncp_instrumentos_cobranca` | 262,529 | 9 |
| trusted | `pncp_orgaos` | 19,126 | 9 |
| trusted | `pncp_orgaos_unidades` | 154,097 | 9 |
| trusted | `pncp_pca` | 7,534 | 9 |

## Read a table

```python
import kagglehub, pandas as pd
path = kagglehub.dataset_download("lucasrangelss/pncp-raw-trusted-part-1", path="raw__pncp_atas_atualizacao.parquet")
df = pd.read_parquet(path)
```

Values are published as held in the snapshot, without masking. Source terms apply; credit the original publisher.

My portfolio: https://lucas.rangeltech.net
