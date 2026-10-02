# IBGE geography: Analytics

Dataset: [lucasrangelss/ibge-analytics](https://www.kaggle.com/datasets/lucasrangelss/ibge-analytics) · snapshot 2026-10-01 · 2 tables · 5,598 rows

**Source:** Instituto Brasileiro de Geografia e Estatística (IBGE), [https://servicodados.ibge.gov.br/api/docs/localidades](https://servicodados.ibge.gov.br/api/docs/localidades)

States and municipalities with their IBGE codes: the key that joins almost every education table.

**Grain and keys:** One row per municipality or state.

**Layers.** `raw` is the source snapshot as delivered. `trusted` is typed, deduplicated and named consistently. `semantic` joins and reshapes trusted tables for analysis. Every table is a Parquet file named `<layer>__<table>.parquet` at the root of the dataset.

The full interactive map (lineage, joins, search) is at [https://rangeltech.net/datamap/](https://rangeltech.net/datamap/). Column descriptions come from the source lake's catalogue and are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns | Described | Upstream |
|---|---|---:|---:|---:|---|
| semantic | [`obt_ibge_municipio`](#semantic-obt-ibge-municipio) | 5,571 | 13 | 13 | `ibge_municipios` |
| semantic | [`obt_ibge_uf`](#semantic-obt-ibge-uf) | 27 | 7 | 7 | `ibge_estados` |

## semantic · obt_ibge_municipio

File `semantic__obt_ibge_municipio.parquet` · 5,571 rows · 13 columns

Cadastro de municípios brasileiros do IBGE. Grão: 1 linha/município (codigo_municipio INT64, 7 dígitos). ~5.570 linhas. FK universal de geografia para todos os OBTs single-domain do datalake educacional: use LEFT JOIN obt_ibge_municipio USING(codigo_municipio) para enriquecer com nome/UF/região. Não contém métricas educacionais. Origem: trusted/ibge_municipios. Fonte: IBGE API de Localidades (servicodados.ibge.gov.br/api/v1/localidades/municipios).

**Built from:** `trusted/ibge_municipios`

**Feeds:** `semantic/obt_api_olinda_siope_indicadores_municipio_ano`, `semantic/obt_api_saeb_boletim`, `semantic/obt_fnde_fundeb_cronograma_vaat_municipio_ano`, `semantic/obt_fnde_fundeb_distribuicao_municipio_mes`, `semantic/obt_fnde_fundeb_indicadores_siope_municipio_ano`, `semantic/obt_fnde_fundeb_municipio_ano`, `semantic/obt_fnde_salario_educacao_distribuido_municipio_mes`, `semantic/obt_fnde_salario_educacao_previsto_municipio_ano`, `semantic/obt_fnde_siope_dados_gerais_municipio_ano`, `semantic/obt_fnde_siope_despesa_educacao_municipio_ano`, `semantic/obt_fnde_siope_despesa_funcao_municipio_ano`, `semantic/obt_fnde_siope_indicador_municipio_ano` …

| Column | Type | Description |
|---|---|---|
| `codigo_municipio` | INTEGER | Código IBGE do município (INT64, 7 dígitos). PK. FK para join com qualquer tabela educacional: LEFT JOIN obt_ibge_municipio USING(codigo_municipio). |
| `nome_municipio` | STRING | Nome oficial do município conforme IBGE. |
| `codigo_microrregiao` | INTEGER | Código IBGE da microrregião geográfica (INT64). |
| `nome_microrregiao` | STRING | Nome da microrregião geográfica IBGE. |
| `codigo_mesorregiao` | INTEGER | Código IBGE da mesorregião geográfica (INT64). |
| `nome_mesorregiao` | STRING | Nome da mesorregião geográfica IBGE. |
| `codigo_uf` | INTEGER | Código IBGE da UF (INT64, 2 dígitos). FK para obt_ibge_uf. |
| `sigla_uf` | STRING | Sigla da UF. Ex: SP, RJ, MG. |
| `nome_uf` | STRING | Nome completo da UF. |
| `codigo_regiao` | INTEGER | Código IBGE da região geográfica (INT64, 1 dígito). 1=Norte, 2=Nordeste, 3=Sudeste, 4=Sul, 5=Centro-Oeste. |
| `sigla_regiao` | STRING | Sigla da região. Ex: N, NE, SE, S, CO. |
| `nome_regiao` | STRING | Nome da região geográfica. Ex: Norte, Nordeste, Sudeste, Sul, Centro-Oeste. |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC de quando os dados foram extraídos da API IBGE. |

## semantic · obt_ibge_uf

File `semantic__obt_ibge_uf.parquet` · 27 rows · 7 columns

Cadastro de UFs (estados) brasileiros do IBGE. Grão: 1 linha/UF (codigo_uf INT64, 2 dígitos). 27 linhas. FK universal de UF para OBTs de grão UF/região/brasil no datalake educacional: use LEFT JOIN obt_ibge_uf USING(codigo_uf) para enriquecer com sigla/nome. Origem: trusted/ibge_estados. Fonte: IBGE API de Localidades (servicodados.ibge.gov.br/api/v1/localidades/estados).

**Built from:** `trusted/ibge_estados`

**Feeds:** `semantic/obt_api_olinda_siope_indicadores_uf_ano`, `semantic/obt_api_olinda_siope_indicadores_uf_bimestre`, `semantic/obt_inep_ideb_regiao_ano`, `semantic/obt_inep_saeb_indicadores_estado_ano`, `semantic/obt_inep_saeb_indicadores_historico_estado_ano`, `semantic/obt_inep_saeb_indicadores_municipio_ano`, `semantic/obt_inep_saeb_micro_escola_ano`, `semantic/obt_inep_saeb_micro_municipio_ano`, `semantic/obt_rreo_siope_uf_ano`, `semantic/obt_rreo_siope_uf_bimestre`

| Column | Type | Description |
|---|---|---|
| `codigo_uf` | INTEGER | Código IBGE da UF (INT64, 2 dígitos). PK. |
| `sigla_uf` | STRING | Sigla da UF. Ex: SP, RJ, MG. |
| `nome_uf` | STRING | Nome completo da UF. |
| `codigo_regiao` | INTEGER | Código IBGE da região geográfica (INT64, 1 dígito). 1=Norte, 2=Nordeste, 3=Sudeste, 4=Sul, 5=Centro-Oeste. |
| `sigla_regiao` | STRING | Sigla da região. Ex: N, NE, SE, S, CO. |
| `nome_regiao` | STRING | Nome da região geográfica. |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC de quando os dados foram extraídos da API IBGE. |
