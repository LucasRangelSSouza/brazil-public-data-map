# PNCP public procurement: Raw and Trusted

Dataset: [lucasrangelss/pncp-raw-trusted-part-2](https://www.kaggle.com/datasets/lucasrangelss/pncp-raw-trusted-part-2) · snapshot 2026-10-01 · 1 tables · 817,211 rows

**Source:** Portal Nacional de Contratações Públicas (PNCP), [https://pncp.gov.br/api/consulta/v1](https://pncp.gov.br/api/consulta/v1)

Procurement notices (including editais), contracts, price-registration records (atas) and annual procurement plans (PCA) with their items, published through the PNCP consultation API.

**Grain and keys:** One row per natural key, keeping the latest version by `dataAtualizacaoGlobal`: `numero_controle_pncp` for notices and contracts, `numero_controle_pncp_ata` for atas, `id_pca_pncp` for plans. Municipality is reachable through `unidade_codigo_ibge` (IBGE code).

**Layers.** `raw` is the source snapshot as delivered. `trusted` is typed, deduplicated and named consistently. `semantic` joins and reshapes trusted tables for analysis. Every table is a Parquet file named `<layer>__<table>.parquet` at the root of the dataset.

The full interactive map (lineage, joins, search) is at [https://rangeltech.net/datamap/](https://rangeltech.net/datamap/). Column descriptions come from the source lake's catalogue and are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns | Described | Upstream |
|---|---|---:|---:|---:|---|
| trusted | [`pncp_pca_itens`](#trusted-pncp-pca-itens) | 817,211 | 23 | 0 | `pncp_pca_atualizacao` |

## trusted · pncp_pca_itens

File `trusted__pncp_pca_itens.parquet` · 817,211 rows · 23 columns

PNCP — Itens do Plano de Contratacoes Anual (explodido do array itens). Grao: id_pca_pncp + numero_item. Fonte: raw/pncp_pca_atualizacao.

**Built from:** `raw/pncp_pca_atualizacao`

**Feeds:** `semantic/obt_pncp_pca_itens`

| Column | Type | Description |
|---|---|---|
| `id_pca_pncp` | STRING |  |
| `numero_item` | INTEGER |  |
| `descricao_item` | STRING |  |
| `codigo_item` | STRING |  |
| `categoria_item_pca_nome` | STRING |  |
| `nome_classificacao_catalogo` | STRING |  |
| `classificacao_catalogo_id` | INTEGER |  |
| `classificacao_superior_codigo` | STRING |  |
| `classificacao_superior_nome` | STRING |  |
| `grupo_contratacao_codigo` | STRING |  |
| `grupo_contratacao_nome` | STRING |  |
| `pdm_codigo` | STRING |  |
| `pdm_descricao` | STRING |  |
| `unidade_fornecimento` | STRING |  |
| `unidade_requisitante` | STRING |  |
| `quantidade_estimada` | FLOAT |  |
| `valor_unitario` | FLOAT |  |
| `valor_total` | FLOAT |  |
| `valor_orcamento_exercicio` | FLOAT |  |
| `data_desejada` | DATE |  |
| `data_inclusao` | TIMESTAMP |  |
| `data_atualizacao` | TIMESTAMP |  |
| `dt_ingestao_lake` | TIMESTAMP |  |
