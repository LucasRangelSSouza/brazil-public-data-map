# IBGE geography: Raw and Trusted

Dataset: [lucasrangelss/ibge-raw-trusted](https://www.kaggle.com/datasets/lucasrangelss/ibge-raw-trusted) · snapshot 2026-09-30 · 4 tables · 11,196 rows

**Source:** Instituto Brasileiro de Geografia e Estatística (IBGE), [https://servicodados.ibge.gov.br/api/docs/localidades](https://servicodados.ibge.gov.br/api/docs/localidades)

States and municipalities with their IBGE codes: the key that joins almost every education table.

**Grain and keys:** One row per municipality or state.

**Layers.** `raw` is the source snapshot as delivered. `trusted` is typed, deduplicated and named consistently. `semantic` joins and reshapes trusted tables for analysis. Every table is a Parquet file named `<layer>__<table>.parquet` at the root of the dataset.

The full interactive map (lineage, joins, search) is at [https://rangeltech.net/datamap/](https://rangeltech.net/datamap/). Column descriptions come from the source lake's catalogue and are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns | Described | Upstream |
|---|---|---:|---:|---:|---|
| raw | [`ibge_estados`](#raw-ibge-estados) | 27 | 7 | 7 | source |
| raw | [`ibge_municipios`](#raw-ibge-municipios) | 5,571 | 24 | 24 | source |
| trusted | [`ibge_estados`](#trusted-ibge-estados) | 27 | 7 | 7 | `ibge_estados` |
| trusted | [`ibge_municipios`](#trusted-ibge-municipios) | 5,571 | 13 | 13 | `ibge_municipios` |

## raw · ibge_estados

File `raw__ibge_estados.parquet` · 27 rows · 7 columns

Tabela de dimensão geográfica contendo o mapeamento de Unidades da Federação (UF) e Regiões do Brasil, utilizada para regionalização e análises espaciais dos dados educacionais.

**Feeds:** `trusted/ibge_estados`

| Column | Type | Description |
|---|---|---|
| `id_uf` | INTEGER | Código identificador numérico da Unidade da Federação (padrão IBGE). |
| `sigla_uf` | STRING | Sigla de duas letras que representa a Unidade da Federação (ex: RO, AC). |
| `nome_uf` | STRING | Nome completo da Unidade da Federação brasileira. |
| `id_regiao` | INTEGER | Código identificador numérico da região geográfica brasileira (padrão IBGE). |
| `sigla_regiao` | STRING | Sigla representativa da região geográfica (ex: N, NE, S, SE, CO). |
| `nome_regiao` | STRING | Nome completo da região geográfica brasileira. |
| `dt_ingestao_lake` | STRING | Data e hora no formato ISO 8601 com fuso horário que indica quando o dado foi carregado no data lake. — descrição gerada por IA. |

## raw · ibge_municipios

File `raw__ibge_municipios.parquet` · 5,571 rows · 24 columns

Tabela de dimensão geográfica contendo o mapeamento político-administrativo e regional dos municípios brasileiros (padrão IBGE), utilizada para cruzamento e regionalização de dados educacionais do data lake.

**Feeds:** `trusted/ibge_municipios`

| Column | Type | Description |
|---|---|---|
| `id_municipio` | INTEGER | Código IBGE de 7 dígitos que identifica unicamente o município brasileiro. |
| `nome_municipio` | STRING | Nome oficial do município brasileiro. |
| `id_microrregiao` | FLOAT | Código numérico identificador da microrregião geográfica estabelecida pelo IBGE. |
| `nome_microrregiao` | STRING | Nome da microrregião geográfica à qual o município pertence. |
| `id_mesorregiao` | FLOAT | Código numérico identificador da mesorregião geográfica estabelecida pelo IBGE. |
| `nome_mesorregiao` | STRING | Nome da mesorregião geográfica à qual o município pertence. |
| `id_uf` | FLOAT | Código numérico identificador da Unidade da Federação (Estado). |
| `sigla_uf` | STRING | Sigla de duas letras da Unidade da Federação (ex: RO, SP). |
| `nome_uf` | STRING | Nome completo da Unidade da Federação (Estado). |
| `id_regiao` | FLOAT | Código numérico identificador da grande região geográfica brasileira (ex: 1 para Norte). |
| `sigla_regiao` | STRING | Sigla da grande região geográfica brasileira (ex: N, NE, SE). |
| `nome_regiao` | STRING | Nome completo da grande região geográfica brasileira (ex: Norte, Sudeste). |
| `regiao-imediata_id` | INTEGER | Código identificador da Região Geográfica Imediata (divisão regional do IBGE de 2017). |
| `regiao-imediata_nome` | STRING | Nome da Região Geográfica Imediata do município. |
| `regiao-imediata_regiao-intermediaria_id` | INTEGER | Código identificador da Região Geográfica Intermediária à qual a região imediata pertence. |
| `regiao-imediata_regiao-intermediaria_nome` | STRING | Nome da Região Geográfica Intermediária. |
| `regiao-imediata_regiao-intermediaria_UF_id` | INTEGER | Código numérico da UF associada à Região Geográfica Intermediária. |
| `regiao-imediata_regiao-intermediaria_UF_sigla` | STRING | Sigla da UF associada à Região Geográfica Intermediária. |
| `regiao-imediata_regiao-intermediaria_UF_nome` | STRING | Nome da UF associada à Região Geográfica Intermediária. |
| `regiao-imediata_regiao-intermediaria_UF_regiao_id` | INTEGER | Código da grande região associada à Região Geográfica Intermediária. |
| `regiao-imediata_regiao-intermediaria_UF_regiao_sigla` | STRING | Sigla da grande região associada à Região Geográfica Intermediária. |
| `regiao-imediata_regiao-intermediaria_UF_regiao_nome` | STRING | Nome da grande região associada à Região Geográfica Intermediária. |
| `microrregiao` | FLOAT | Objeto ou campo auxiliar estruturado com dados adicionais da microrregião (pode conter nulos). |
| `dt_ingestao_lake` | STRING | Data e hora no formato ISO 8601 em que o registro foi carregado no Data Lake. — descrição gerada por IA. |

## trusted · ibge_estados

File `trusted__ibge_estados.parquet` · 27 rows · 7 columns

Estados brasileiros (UFs) conforme IBGE API de Localidades. Grão: 1 linha/UF (codigo_uf INT64, 2 dígitos). 27 linhas. Inclui região. codigo_uf/codigo_regiao INT64 para join padronizado. Origem raw: raw_zone.ibge_estados. Fonte: IBGE API de Localidades (servicodados.ibge.gov.br/api/v1/localidades/estados). Atualização: anual ou sob demanda.

**Built from:** `raw/ibge_estados`

**Feeds:** `semantic/obt_ibge_uf`

| Column | Type | Description |
|---|---|---|
| `codigo_uf` | INTEGER | Código IBGE da UF (INT64, 2 dígitos). PK. |
| `sigla_uf` | STRING | Sigla da UF. Ex: SP, RJ, MG. |
| `nome_uf` | STRING | Nome completo da UF. |
| `codigo_regiao` | INTEGER | Código IBGE da região geográfica (INT64, 1 dígito). |
| `sigla_regiao` | STRING | Sigla da região. Ex: N, NE, SE, S, CO. |
| `nome_regiao` | STRING | Nome da região geográfica. |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC de quando os dados foram extraídos da API IBGE. |

## trusted · ibge_municipios

File `trusted__ibge_municipios.parquet` · 5,571 rows · 13 columns

Municípios brasileiros conforme IBGE API de Localidades. Grão: 1 linha/município (codigo_municipio INT64, 7 dígitos). ~5.570 linhas. Inclui hierarquia completa: município → microrregião → mesorregião → UF → região. codigo_municipio/codigo_uf/codigo_regiao são INT64 para join padronizado com todas as tabelas educacionais. UF/região usam COALESCE com fallback para estrutura regiao-imediata (cobre municípios novos com gap na API). Origem raw: raw_zone.ibge_municipios. Fonte: IBGE API de Localidades (servicodados.ibge.gov.br/api/v1/localidades/municipios). Atualização: anual ou sob demanda.

**Built from:** `raw/ibge_municipios`

**Feeds:** `semantic/obt_ibge_municipio`

| Column | Type | Description |
|---|---|---|
| `codigo_municipio` | INTEGER | Código IBGE do município (INT64, 7 dígitos). PK. FK universal: JOIN com qualquer tabela educacional via USING(codigo_municipio). |
| `nome_municipio` | STRING | Nome oficial do município conforme IBGE. |
| `codigo_microrregiao` | INTEGER | Código IBGE da microrregião geográfica (INT64). |
| `nome_microrregiao` | STRING | Nome da microrregião geográfica IBGE. |
| `codigo_mesorregiao` | INTEGER | Código IBGE da mesorregião geográfica (INT64). |
| `nome_mesorregiao` | STRING | Nome da mesorregião geográfica IBGE. |
| `codigo_uf` | INTEGER | Código IBGE da UF (INT64, 2 dígitos). FK para trusted_zone.ibge_estados. |
| `sigla_uf` | STRING | Sigla da UF. Ex: SP, RJ, MG. |
| `nome_uf` | STRING | Nome completo da UF. |
| `codigo_regiao` | INTEGER | Código IBGE da região geográfica (INT64, 1 dígito). 1=Norte, 2=Nordeste, 3=Sudeste, 4=Sul, 5=Centro-Oeste. |
| `sigla_regiao` | STRING | Sigla da região. Ex: N, NE, SE, S, CO. |
| `nome_regiao` | STRING | Nome da região geográfica. |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC de quando os dados foram extraídos da API IBGE. |
