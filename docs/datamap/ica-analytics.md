# Literate Child Indicator (INEP): Analytics

Dataset: [lucasrangelss/ica-analytics](https://www.kaggle.com/datasets/lucasrangelss/ica-analytics) · snapshot 2026-09-30 · 2 tables · 43,908 rows

**Source:** Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP), [https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais](https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais)

Share of children literate at the right age, with the targets agreed up to 2030, by municipality (municipal network) and by state and Brazil (public network).

**Grain and keys:** Municipality by edition (wide format in trusted, long series in semantic); one row per state plus a Brazil row.

**Layers.** `raw` is the source snapshot as delivered. `trusted` is typed, deduplicated and named consistently. `semantic` joins and reshapes trusted tables for analysis. Every table is a Parquet file named `<layer>__<table>.parquet` at the root of the dataset.

The full interactive map (lineage, joins, search) is at [https://lucas.rangeltech.net/datamap/](https://lucas.rangeltech.net/datamap/). Column descriptions come from the source lake's catalogue and are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns | Described | Upstream |
|---|---|---:|---:|---:|---|
| semantic | [`obt_ica_municipio_ano`](#semantic-obt-ica-municipio-ano) | 43,719 | 16 | 0 | `obt_ibge_municipio`, `inep_ica_municipios` |
| semantic | [`obt_ica_uf_ano`](#semantic-obt-ica-uf-ano) | 189 | 15 | 0 | `inep_ica_ufs` |

## semantic · obt_ica_municipio_ano

File `semantic__obt_ica_municipio_ano.parquet` · 43,719 rows · 16 columns

Indicador Crianca Alfabetizada (INEP) por municipio e ano: resultado, meta e se a meta foi atingida, com a geografia do IBGE. Serie longa a partir do formato largo publicado pelo INEP.

**Built from:** `semantic/obt_ibge_municipio`, `trusted/inep_ica_municipios`

| Column | Type | Description |
|---|---|---|
| `codigo_municipio` | INTEGER |  |
| `nome_municipio` | STRING |  |
| `sigla_uf` | STRING |  |
| `nome_uf` | STRING |  |
| `nome_regiao` | STRING |  |
| `ano` | INTEGER |  |
| `rede` | STRING |  |
| `pc_alfabetizado` | FLOAT |  |
| `meta` | FLOAT |  |
| `tem_resultado` | BOOLEAN |  |
| `tem_meta` | BOOLEAN |  |
| `atingiu_meta` | BOOLEAN |  |
| `distancia_da_meta` | FLOAT |  |
| `pc_avaliados_lp` | FLOAT |  |
| `edicao` | INTEGER |  |
| `dt_construcao` | TIMESTAMP |  |

## semantic · obt_ica_uf_ano

File `semantic__obt_ica_uf_ano.parquet` · 189 rows · 15 columns

Indicador Crianca Alfabetizada (INEP) por UF e Brasil, por ano: resultado, meta e se a meta foi atingida. Rede PUBLICA (municipal + estadual) -- nao comparavel linha a linha com a OBT de municipio, que e rede municipal.

**Built from:** `trusted/inep_ica_ufs`

| Column | Type | Description |
|---|---|---|
| `co_uf` | INTEGER |  |
| `sg_uf` | STRING |  |
| `nome_uf` | STRING |  |
| `e_brasil` | BOOLEAN |  |
| `ano` | INTEGER |  |
| `rede` | STRING |  |
| `pc_alfabetizado` | FLOAT |  |
| `meta` | FLOAT |  |
| `tem_resultado` | BOOLEAN |  |
| `tem_meta` | BOOLEAN |  |
| `atingiu_meta` | BOOLEAN |  |
| `distancia_da_meta` | FLOAT |  |
| `pc_avaliados_lp` | FLOAT |  |
| `edicao` | INTEGER |  |
| `dt_construcao` | TIMESTAMP |  |
