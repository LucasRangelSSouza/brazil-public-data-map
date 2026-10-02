# FNDE education contribution: Analytics

Dataset: [lucasrangelss/fnde-salario-educacao-analytics](https://www.kaggle.com/datasets/lucasrangelss/fnde-salario-educacao-analytics) · snapshot 2026-09-30 · 2 tables · 433,562 rows

**Source:** Fundo Nacional de Desenvolvimento da Educação (FNDE), [https://www.fnde.gov.br/](https://www.fnde.gov.br/)

Collection and distribution of the education contribution (salário-educação) published by FNDE.

**Grain and keys:** See each table.

**Layers.** `raw` is the source snapshot as delivered. `trusted` is typed, deduplicated and named consistently. `semantic` joins and reshapes trusted tables for analysis. Every table is a Parquet file named `<layer>__<table>.parquet` at the root of the dataset.

The full interactive map (lineage, joins, search) is at [https://rangeltech.net/datamap/](https://rangeltech.net/datamap/). Column descriptions come from the source lake's catalogue and are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns | Described | Upstream |
|---|---|---:|---:|---:|---|
| semantic | [`obt_fnde_salario_educacao_distribuido_municipio_mes`](#semantic-obt-fnde-salario-educacao-distribuido-municipio-mes) | 338,835 | 16 | 16 | `obt_ibge_municipio`, `fnde_salario_educacao_distribuido_mensal` |
| semantic | [`obt_fnde_salario_educacao_previsto_municipio_ano`](#semantic-obt-fnde-salario-educacao-previsto-municipio-ano) | 94,727 | 14 | 14 | `obt_ibge_municipio`, `fnde_salario_educacao_previsto` |

## semantic · obt_fnde_salario_educacao_distribuido_municipio_mes

File `semantic__obt_fnde_salario_educacao_distribuido_municipio_mes.parquet` · 338,835 rows · 16 columns

Salario-Educacao (FNDE) - OBT da distribuicao efetiva das quotas por ente federado. Grao: 1 linha por ente x ano x mes de competencia; cada linha carrega tambem o consolidado do exercicio em vl_salario_educacao_distribuido_ano. Exercicios 2020-2021 entram com mes_competencia nulo (a fonte so publicou o total anual) e ate 2019 so ha agregado por UF x esfera, sem municipio. Fonte: trusted/fnde_salario_educacao_distribuido_mensal.

**Built from:** `semantic/obt_ibge_municipio`, `trusted/fnde_salario_educacao_distribuido_mensal`

**Feeds:** `semantic/obt_api_olinda_siope_indicadores_municipio_ano`, `semantic/obt_api_olinda_siope_indicadores_uf_ano`

| Column | Type | Description |
|---|---|---|
| `ano` | INTEGER | Ano de exercicio da distribuicao. |
| `uf` | STRING | Sigla da UF do ente. |
| `ente_federado` | STRING | Nome do ente conforme publicacao do FNDE. |
| `cod_ibge` | STRING | Codigo IBGE do municipio (7 digitos); 'UF_<sigla>' na quota estadual; 'MUN_<sigla>' no agregado por UF publicado ate 2019. |
| `cod_ibge_int` | INTEGER | Codigo IBGE do municipio como inteiro - chave de join com a dimensao geografica. |
| `esfera` | STRING | 'municipal' ou 'estadual'. |
| `mes_competencia` | INTEGER | Mes de competencia do repasse (1-12). NULO em 2020-2021, cuja fonte traz so o total anual. |
| `vl_salario_educacao_distribuido_mes` | FLOAT | Valor repassado ao ente na competencia (R$). |
| `vl_salario_educacao_distribuido_ano` | FLOAT | Consolidado do exercicio ate a publicacao (R$), repetido em todas as linhas do ente. |
| `competencias_com_valor` | INTEGER | Meses com repasse no documento. Menor que 12 indica exercicio em curso. |
| `flag_exercicio_fechado` | BOOLEAN | TRUE quando o consolidado cobre o exercicio inteiro. FALSE no ano corrente, publicado parcial. |
| `source_url` | STRING | URL do PDF oficial de origem. |
| `nome_municipio` | STRING | Nome do municipio no cadastro IBGE. |
| `nome_uf` | STRING | Nome da UF segundo o IBGE. |
| `nome_regiao` | STRING | Nome da regiao segundo o IBGE. |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC de geracao da OBT. |

## semantic · obt_fnde_salario_educacao_previsto_municipio_ano

File `semantic__obt_fnde_salario_educacao_previsto_municipio_ano.parquet` · 94,727 rows · 14 columns

Salario-Educacao (FNDE) - OBT do previsto/estimativa das quotas por ente federado. Grao: 1 linha por ente x ano. Valor ANUAL: a fonte nao publica abertura mensal da estimativa. Fonte: trusted/fnde_salario_educacao_previsto.

**Built from:** `semantic/obt_ibge_municipio`, `trusted/fnde_salario_educacao_previsto`

**Feeds:** `semantic/obt_api_olinda_siope_indicadores_municipio_ano`, `semantic/obt_api_olinda_siope_indicadores_uf_ano`

| Column | Type | Description |
|---|---|---|
| `ano` | INTEGER | Ano de exercicio da estimativa. |
| `uf` | STRING | Sigla da UF do ente. |
| `ente_federado` | STRING | Nome do ente conforme publicacao do FNDE. |
| `cod_ibge` | STRING | Codigo IBGE do municipio (7 digitos) ou 'UF_<sigla>' na quota estadual. |
| `cod_ibge_int` | INTEGER | Codigo IBGE do municipio como inteiro - chave de join com a dimensao geografica. |
| `esfera` | STRING | 'municipal' ou 'estadual'. |
| `coeficiente` | FLOAT | Coeficiente oficial de distribuicao do ente. |
| `vl_salario_educacao_previsto` | FLOAT | Estimativa oficial de receita do ente no exercicio (R$), valor anual. |
| `portaria` | STRING | Portaria FNDE que publicou a estimativa. |
| `source_url` | STRING | URL do PDF oficial de origem. |
| `nome_municipio` | STRING | Nome do municipio no cadastro IBGE. |
| `nome_uf` | STRING | Nome da UF segundo o IBGE. |
| `nome_regiao` | STRING | Nome da regiao segundo o IBGE. |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC de geracao da OBT. |
