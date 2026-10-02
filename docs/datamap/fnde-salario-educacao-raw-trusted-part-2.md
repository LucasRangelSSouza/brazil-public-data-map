# FNDE education contribution: Raw and Trusted

Dataset: [lucasrangelss/fnde-salario-educacao-raw-trusted-part-2](https://www.kaggle.com/datasets/lucasrangelss/fnde-salario-educacao-raw-trusted-part-2) · snapshot 2026-09-30 · 6 tables · 455,943 rows

**Source:** Fundo Nacional de Desenvolvimento da Educação (FNDE), [https://www.fnde.gov.br/](https://www.fnde.gov.br/)

Collection and distribution of the education contribution (salário-educação) published by FNDE.

**Grain and keys:** See each table.

**Layers.** `raw` is the source snapshot as delivered. `trusted` is typed, deduplicated and named consistently. `semantic` joins and reshapes trusted tables for analysis. Every table is a Parquet file named `<layer>__<table>.parquet` at the root of the dataset.

The full interactive map (lineage, joins, search) is at [https://rangeltech.net/datamap/](https://rangeltech.net/datamap/). Column descriptions come from the source lake's catalogue and are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns | Described | Upstream |
|---|---|---:|---:|---:|---|
| raw | [`fnde_salario_educacao_realizado_2023`](#raw-fnde-salario-educacao-realizado-2023) | 5,595 | 21 | 21 | source |
| raw | [`fnde_salario_educacao_realizado_2024`](#raw-fnde-salario-educacao-realizado-2024) | 5,595 | 21 | 21 | source |
| raw | [`fnde_salario_educacao_realizado_2025`](#raw-fnde-salario-educacao-realizado-2025) | 5,595 | 21 | 21 | source |
| raw | [`fnde_salario_educacao_realizado_2026`](#raw-fnde-salario-educacao-realizado-2026) | 5,596 | 21 | 21 | source |
| trusted | [`fnde_salario_educacao_distribuido_mensal`](#trusted-fnde-salario-educacao-distribuido-mensal) | 338,835 | 12 | 12 | source |
| trusted | [`fnde_salario_educacao_previsto`](#trusted-fnde-salario-educacao-previsto) | 94,727 | 11 | 11 | `obt_ibge_municipio` |

## raw · fnde_salario_educacao_realizado_2023

File `raw__fnde_salario_educacao_realizado_2023.parquet` · 5,595 rows · 21 columns

Salário-Educação (FNDE) — distribuído/realizado por ente federado, camada raw anual. 1 linha por ano x ente federado na publicação oficial do FNDE, com colunas mensais preservadas. Ano específico: 2023.

| Column | Type | Description |
|---|---|---|
| `ano` | STRING | Ano de referência do distribuído (raw). |
| `uf` | STRING | Sigla da UF do ente. |
| `ente_federado` | STRING | Nome do ente federado. |
| `cod_ibge` | STRING | Código IBGE do ente ou identificador agregado histórico. |
| `esfera` | STRING | Esfera administrativa do ente. |
| `competencias_com_valor` | STRING | Quantidade de meses no ano em que foram efetuados repasses de recursos. — descrição gerada por IA. |
| `vl_distribuido_total` | STRING | Valor total distribuído como texto/normalizado. |
| `source_url` | STRING | URL do PDF oficial de origem. |
| `vl_mes_01` | STRING | Valor distribuído da competência 01. |
| `vl_mes_02` | STRING | Valor distribuído da competência 02. |
| `vl_mes_03` | STRING | Valor distribuído da competência 03. |
| `vl_mes_04` | STRING | Valor distribuído da competência 04. |
| `vl_mes_05` | STRING | Valor distribuído da competência 05. |
| `vl_mes_06` | STRING | Valor distribuído da competência 06. |
| `vl_mes_07` | STRING | Valor distribuído da competência 07. |
| `vl_mes_08` | STRING | Valor distribuído da competência 08. |
| `vl_mes_09` | STRING | Valor distribuído da competência 09. |
| `vl_mes_10` | STRING | Valor distribuído da competência 10. |
| `vl_mes_11` | STRING | Valor distribuído da competência 11. |
| `vl_mes_12` | STRING | Valor distribuído da competência 12. |
| `dt_ingestao_lake` | STRING | Timestamp UTC da ingestão no lake. |

## raw · fnde_salario_educacao_realizado_2024

File `raw__fnde_salario_educacao_realizado_2024.parquet` · 5,595 rows · 21 columns

Salário-Educação (FNDE) — distribuído/realizado por ente federado, camada raw anual. 1 linha por ano x ente federado na publicação oficial do FNDE, com colunas mensais preservadas. Ano específico: 2024.

| Column | Type | Description |
|---|---|---|
| `ano` | STRING | Ano de referência do distribuído (raw). |
| `uf` | STRING | Sigla da UF do ente. |
| `ente_federado` | STRING | Nome do ente federado. |
| `cod_ibge` | STRING | Código IBGE do ente ou identificador agregado histórico. |
| `esfera` | STRING | Esfera administrativa do ente. |
| `competencias_com_valor` | STRING | Quantidade de meses no ano que tiveram valor distribuído registrado. — descrição gerada por IA. |
| `vl_distribuido_total` | STRING | Valor total distribuído como texto/normalizado. |
| `source_url` | STRING | URL do PDF oficial de origem. |
| `vl_mes_01` | STRING | Valor distribuído da competência 01. |
| `vl_mes_02` | STRING | Valor distribuído da competência 02. |
| `vl_mes_03` | STRING | Valor distribuído da competência 03. |
| `vl_mes_04` | STRING | Valor distribuído da competência 04. |
| `vl_mes_05` | STRING | Valor distribuído da competência 05. |
| `vl_mes_06` | STRING | Valor distribuído da competência 06. |
| `vl_mes_07` | STRING | Valor distribuído da competência 07. |
| `vl_mes_08` | STRING | Valor distribuído da competência 08. |
| `vl_mes_09` | STRING | Valor distribuído da competência 09. |
| `vl_mes_10` | STRING | Valor distribuído da competência 10. |
| `vl_mes_11` | STRING | Valor distribuído da competência 11. |
| `vl_mes_12` | STRING | Valor distribuído da competência 12. |
| `dt_ingestao_lake` | STRING | Timestamp UTC da ingestão no lake. |

## raw · fnde_salario_educacao_realizado_2025

File `raw__fnde_salario_educacao_realizado_2025.parquet` · 5,595 rows · 21 columns

Salário-Educação (FNDE) — distribuído/realizado por ente federado, camada raw anual. 1 linha por ano x ente federado na publicação oficial do FNDE, com colunas mensais preservadas. Ano específico: 2025.

| Column | Type | Description |
|---|---|---|
| `ano` | STRING | Ano de referência do distribuído (raw). |
| `uf` | STRING | Sigla da UF do ente. |
| `ente_federado` | STRING | Nome do ente federado. |
| `cod_ibge` | STRING | Código IBGE do ente ou identificador agregado histórico. |
| `esfera` | STRING | Esfera administrativa do ente. |
| `competencias_com_valor` | STRING | Número total de meses (competências) no ano que registraram distribuição financeira. — descrição gerada por IA. |
| `vl_distribuido_total` | STRING | Valor total distribuído como texto/normalizado. |
| `source_url` | STRING | URL do PDF oficial de origem. |
| `vl_mes_01` | STRING | Valor distribuído da competência 01. |
| `vl_mes_02` | STRING | Valor distribuído da competência 02. |
| `vl_mes_03` | STRING | Valor distribuído da competência 03. |
| `vl_mes_04` | STRING | Valor distribuído da competência 04. |
| `vl_mes_05` | STRING | Valor distribuído da competência 05. |
| `vl_mes_06` | STRING | Valor distribuído da competência 06. |
| `vl_mes_07` | STRING | Valor distribuído da competência 07. |
| `vl_mes_08` | STRING | Valor distribuído da competência 08. |
| `vl_mes_09` | STRING | Valor distribuído da competência 09. |
| `vl_mes_10` | STRING | Valor distribuído da competência 10. |
| `vl_mes_11` | STRING | Valor distribuído da competência 11. |
| `vl_mes_12` | STRING | Valor distribuído da competência 12. |
| `dt_ingestao_lake` | STRING | Timestamp UTC da ingestão no lake. |

## raw · fnde_salario_educacao_realizado_2026

File `raw__fnde_salario_educacao_realizado_2026.parquet` · 5,596 rows · 21 columns

Salário-Educação (FNDE) — distribuição mensal por ente federado, exercício 2026, camada RAW (tudo STRING). 1 linha por ente com as 12 competências e o total. O documento do exercício corrente é republicado a cada mês, então esta tabela é substituída integralmente todo dia.

| Column | Type | Description |
|---|---|---|
| `ano` | STRING | Ano de exercício da distribuição. |
| `uf` | STRING | Sigla da UF do ente. |
| `ente_federado` | STRING | Nome do ente: município ou GOVERNO ESTADUAL. |
| `cod_ibge` | STRING | Código IBGE do município (7 dígitos) ou UF_<sigla> na quota estadual. |
| `esfera` | STRING | 'municipal' ou 'estadual'. |
| `competencias_com_valor` | STRING | Quantidade de meses com repasse no documento. Menor que 12 = exercício ainda em curso. |
| `vl_distribuido_total` | STRING | Total distribuído ao ente no exercício até a publicação (R$). |
| `source_url` | STRING | URL do PDF oficial de origem. |
| `dt_ingestao_lake` | STRING | Timestamp UTC da ingestão. |
| `vl_mes_01` | STRING | Valor distribuído na competência 01 (R$). Nulo se o mês ainda não foi repassado. |
| `vl_mes_02` | STRING | Valor distribuído na competência 02 (R$). Nulo se o mês ainda não foi repassado. |
| `vl_mes_03` | STRING | Valor distribuído na competência 03 (R$). Nulo se o mês ainda não foi repassado. |
| `vl_mes_04` | STRING | Valor distribuído na competência 04 (R$). Nulo se o mês ainda não foi repassado. |
| `vl_mes_05` | STRING | Valor distribuído na competência 05 (R$). Nulo se o mês ainda não foi repassado. |
| `vl_mes_06` | STRING | Valor distribuído na competência 06 (R$). Nulo se o mês ainda não foi repassado. |
| `vl_mes_07` | STRING | Valor distribuído na competência 07 (R$). Nulo se o mês ainda não foi repassado. |
| `vl_mes_08` | STRING | Valor distribuído na competência 08 (R$). Nulo se o mês ainda não foi repassado. |
| `vl_mes_09` | STRING | Valor distribuído na competência 09 (R$). Nulo se o mês ainda não foi repassado. |
| `vl_mes_10` | STRING | Valor distribuído na competência 10 (R$). Nulo se o mês ainda não foi repassado. |
| `vl_mes_11` | STRING | Valor distribuído na competência 11 (R$). Nulo se o mês ainda não foi repassado. |
| `vl_mes_12` | STRING | Valor distribuído na competência 12 (R$). Nulo se o mês ainda não foi repassado. |

## trusted · fnde_salario_educacao_distribuido_mensal

File `trusted__fnde_salario_educacao_distribuido_mensal.parquet` · 338,835 rows · 12 columns

Salario-Educacao (FNDE) - distribuicao efetiva das quotas por ente federado, camada TRUSTED. Grao: 1 linha por ente x ano x mes de competencia, com o consolidado anual repetido em vl_distribuido_total. Eras da fonte: 2022+ tem detalhe mensal por municipio; 2020-2021 traz so o total anual por municipio (mes_competencia nulo); ate 2019 o FNDE publicava apenas agregado por UF x esfera, sem municipio.

**Feeds:** `semantic/obt_fnde_salario_educacao_distribuido_municipio_mes`

| Column | Type | Description |
|---|---|---|
| `ano` | INTEGER | Ano de exercicio da distribuicao. |
| `uf` | STRING | Sigla da UF do ente. |
| `ente_federado` | STRING | Nome do municipio, 'GOVERNO ESTADUAL' ou o agregado de rede das eras antigas. |
| `cod_ibge` | STRING | Codigo IBGE do municipio (7 digitos); 'UF_<sigla>' na quota estadual; 'MUN_<sigla>' no agregado municipal por UF publicado ate 2019. |
| `esfera` | STRING | 'municipal' ou 'estadual'. |
| `mes_competencia` | INTEGER | Mes de competencia do repasse (1-12). NULO nos exercicios 2020-2021, cujo documento traz so o total anual. |
| `vl_distribuido_mes` | FLOAT | Valor repassado ao ente na competencia (R$). NULO quando o documento nao abre por mes. |
| `vl_distribuido_total` | FLOAT | Total distribuido ao ente no exercicio ate a publicacao (R$). Repetido em todas as linhas do ente: e o consolidado do ano. |
| `competencias_com_valor` | INTEGER | Meses com repasse no documento. Menor que 12 indica exercicio em curso; 0 indica documento sem abertura mensal. |
| `flag_exercicio_fechado` | BOOLEAN | TRUE quando o total cobre o exercicio inteiro: 12 competencias, ou documento anual sem detalhe mensal. FALSE no ano corrente, publicado parcial. |
| `source_url` | STRING | URL do PDF oficial de origem. |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC da ingestao na raw de origem. |

## trusted · fnde_salario_educacao_previsto

File `trusted__fnde_salario_educacao_previsto.parquet` · 94,727 rows · 11 columns

Salario-Educacao (FNDE) - estimativa das quotas estaduais e municipais por ente federado, camada TRUSTED. Grao: 1 linha por ente x ano. A fonte e ANUAL: o FNDE nao publica abertura mensal da estimativa. Fonte: PDFs 'Estimativa das quotas ... por ente federado' da pagina de Consultas.

**Built from:** `semantic/obt_ibge_municipio`

**Feeds:** `semantic/obt_fnde_salario_educacao_previsto_municipio_ano`

| Column | Type | Description |
|---|---|---|
| `ano` | INTEGER | Ano de exercicio da estimativa. |
| `uf` | STRING | Sigla da UF do ente. |
| `ente_federado` | STRING | Nome do municipio ou 'GOVERNO ESTADUAL' (quota estadual). |
| `cod_ibge` | STRING | Codigo IBGE do municipio (7 digitos) ou 'UF_<sigla>' na quota estadual. Resolvido por nome no historico, cujos PDFs nao imprimem o codigo. |
| `esfera` | STRING | 'municipal' ou 'estadual'. |
| `coeficiente` | FLOAT | Coeficiente de distribuicao do ente (fracao do total nacional). |
| `vl_previsto_receita` | FLOAT | Estimativa oficial de receita do ente no exercicio (R$). Valor ANUAL: a fonte nao abre por mes. |
| `portaria` | STRING | Portaria FNDE que publicou a estimativa. |
| `source_url` | STRING | URL do PDF oficial de origem. |
| `pdf_hash` | STRING | Hash do PDF ingerido. |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC da ingestao na raw de origem. |
