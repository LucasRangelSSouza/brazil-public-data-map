# FNDE education contribution: Raw and Trusted

Dataset: [lucasrangelss/fnde-salario-educacao-raw-trusted-part-1](https://www.kaggle.com/datasets/lucasrangelss/fnde-salario-educacao-raw-trusted-part-1) · snapshot 2026-09-30 · 40 tables · 112,836 rows

**Source:** Fundo Nacional de Desenvolvimento da Educação (FNDE), [https://www.fnde.gov.br/](https://www.fnde.gov.br/)

Collection and distribution of the education contribution (salário-educação) published by FNDE.

**Grain and keys:** See each table.

**Layers.** `raw` is the source snapshot as delivered. `trusted` is typed, deduplicated and named consistently. `semantic` joins and reshapes trusted tables for analysis. Every table is a Parquet file named `<layer>__<table>.parquet` at the root of the dataset.

The full interactive map (lineage, joins, search) is at [https://rangeltech.net/datamap/](https://rangeltech.net/datamap/). Column descriptions come from the source lake's catalogue and are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns | Described | Upstream |
|---|---|---:|---:|---:|---|
| raw | [`fnde_salario_educacao_previsto_2010`](#raw-fnde-salario-educacao-previsto-2010) | 5,589 | 11 | 11 | source |
| raw | [`fnde_salario_educacao_previsto_2011`](#raw-fnde-salario-educacao-previsto-2011) | 5,589 | 11 | 11 | source |
| raw | [`fnde_salario_educacao_previsto_2012`](#raw-fnde-salario-educacao-previsto-2012) | 5,590 | 11 | 11 | source |
| raw | [`fnde_salario_educacao_previsto_2013`](#raw-fnde-salario-educacao-previsto-2013) | 5,590 | 11 | 11 | source |
| raw | [`fnde_salario_educacao_previsto_2014`](#raw-fnde-salario-educacao-previsto-2014) | 5,595 | 11 | 11 | source |
| raw | [`fnde_salario_educacao_previsto_2015`](#raw-fnde-salario-educacao-previsto-2015) | 5,595 | 11 | 11 | source |
| raw | [`fnde_salario_educacao_previsto_2016`](#raw-fnde-salario-educacao-previsto-2016) | 5,595 | 11 | 11 | source |
| raw | [`fnde_salario_educacao_previsto_2017`](#raw-fnde-salario-educacao-previsto-2017) | 5,595 | 11 | 11 | source |
| raw | [`fnde_salario_educacao_previsto_2018`](#raw-fnde-salario-educacao-previsto-2018) | 5,595 | 11 | 11 | source |
| raw | [`fnde_salario_educacao_previsto_2019`](#raw-fnde-salario-educacao-previsto-2019) | 5,595 | 11 | 11 | source |
| raw | [`fnde_salario_educacao_previsto_2020`](#raw-fnde-salario-educacao-previsto-2020) | 5,595 | 11 | 11 | source |
| raw | [`fnde_salario_educacao_previsto_2021`](#raw-fnde-salario-educacao-previsto-2021) | 5,595 | 11 | 11 | source |
| raw | [`fnde_salario_educacao_previsto_2022`](#raw-fnde-salario-educacao-previsto-2022) | 5,595 | 11 | 11 | source |
| raw | [`fnde_salario_educacao_previsto_2023`](#raw-fnde-salario-educacao-previsto-2023) | 5,595 | 11 | 11 | source |
| raw | [`fnde_salario_educacao_previsto_2024`](#raw-fnde-salario-educacao-previsto-2024) | 5,595 | 11 | 11 | source |
| raw | [`fnde_salario_educacao_previsto_2025`](#raw-fnde-salario-educacao-previsto-2025) | 5,595 | 11 | 11 | source |
| raw | [`fnde_salario_educacao_previsto_2026`](#raw-fnde-salario-educacao-previsto-2026) | 5,596 | 11 | 11 | source |
| raw | [`fnde_salario_educacao_realizado_2000`](#raw-fnde-salario-educacao-realizado-2000) | 24 | 21 | 21 | source |
| raw | [`fnde_salario_educacao_realizado_2001`](#raw-fnde-salario-educacao-realizado-2001) | 23 | 21 | 21 | source |
| raw | [`fnde_salario_educacao_realizado_2002`](#raw-fnde-salario-educacao-realizado-2002) | 24 | 21 | 21 | source |
| raw | [`fnde_salario_educacao_realizado_2003`](#raw-fnde-salario-educacao-realizado-2003) | 24 | 21 | 21 | source |
| raw | [`fnde_salario_educacao_realizado_2004`](#raw-fnde-salario-educacao-realizado-2004) | 54 | 21 | 21 | source |
| raw | [`fnde_salario_educacao_realizado_2005`](#raw-fnde-salario-educacao-realizado-2005) | 54 | 21 | 21 | source |
| raw | [`fnde_salario_educacao_realizado_2006`](#raw-fnde-salario-educacao-realizado-2006) | 54 | 21 | 21 | source |
| raw | [`fnde_salario_educacao_realizado_2007`](#raw-fnde-salario-educacao-realizado-2007) | 54 | 21 | 21 | source |
| raw | [`fnde_salario_educacao_realizado_2008`](#raw-fnde-salario-educacao-realizado-2008) | 54 | 21 | 21 | source |
| raw | [`fnde_salario_educacao_realizado_2009`](#raw-fnde-salario-educacao-realizado-2009) | 52 | 21 | 21 | source |
| raw | [`fnde_salario_educacao_realizado_2010`](#raw-fnde-salario-educacao-realizado-2010) | 54 | 21 | 21 | source |
| raw | [`fnde_salario_educacao_realizado_2011`](#raw-fnde-salario-educacao-realizado-2011) | 54 | 21 | 21 | source |
| raw | [`fnde_salario_educacao_realizado_2012`](#raw-fnde-salario-educacao-realizado-2012) | 54 | 21 | 21 | source |
| raw | [`fnde_salario_educacao_realizado_2013`](#raw-fnde-salario-educacao-realizado-2013) | 54 | 21 | 21 | source |
| raw | [`fnde_salario_educacao_realizado_2014`](#raw-fnde-salario-educacao-realizado-2014) | 54 | 21 | 21 | source |
| raw | [`fnde_salario_educacao_realizado_2015`](#raw-fnde-salario-educacao-realizado-2015) | 54 | 21 | 21 | source |
| raw | [`fnde_salario_educacao_realizado_2016`](#raw-fnde-salario-educacao-realizado-2016) | 54 | 21 | 21 | source |
| raw | [`fnde_salario_educacao_realizado_2017`](#raw-fnde-salario-educacao-realizado-2017) | 54 | 21 | 21 | source |
| raw | [`fnde_salario_educacao_realizado_2018`](#raw-fnde-salario-educacao-realizado-2018) | 54 | 21 | 21 | source |
| raw | [`fnde_salario_educacao_realizado_2019`](#raw-fnde-salario-educacao-realizado-2019) | 54 | 21 | 21 | source |
| raw | [`fnde_salario_educacao_realizado_2020`](#raw-fnde-salario-educacao-realizado-2020) | 5,594 | 21 | 21 | source |
| raw | [`fnde_salario_educacao_realizado_2021`](#raw-fnde-salario-educacao-realizado-2021) | 5,596 | 21 | 21 | source |
| raw | [`fnde_salario_educacao_realizado_2022`](#raw-fnde-salario-educacao-realizado-2022) | 5,595 | 21 | 21 | source |

## raw · fnde_salario_educacao_previsto_2010

File `raw__fnde_salario_educacao_previsto_2010.parquet` · 5,589 rows · 11 columns

Salário-Educação (FNDE) — previsto/estimativa por ente federado, camada raw anual. 1 linha por ano x ente federado na publicação oficial do FNDE. Ano específico: 2010.

| Column | Type | Description |
|---|---|---|
| `ano` | STRING | Ano de exercício do previsto (raw). |
| `uf` | STRING | Sigla da UF do ente. |
| `ente_federado` | STRING | Nome do ente federado. |
| `cod_ibge` | STRING | Código IBGE do ente ou identificador agregado histórico. |
| `esfera` | STRING | Esfera administrativa do ente. |
| `coeficiente` | STRING | Coeficiente oficial como texto bruto. |
| `vl_previsto_receita` | STRING | Valor previsto bruto como texto/normalizado. |
| `portaria` | STRING | Portaria FNDE identificada na origem. |
| `source_url` | STRING | URL do PDF oficial de origem. |
| `pdf_hash` | STRING | Hash do PDF processado. |
| `dt_ingestao_lake` | STRING | Timestamp UTC da ingestão no lake. |

## raw · fnde_salario_educacao_previsto_2011

File `raw__fnde_salario_educacao_previsto_2011.parquet` · 5,589 rows · 11 columns

Salário-Educação (FNDE) — previsto/estimativa por ente federado, camada raw anual. 1 linha por ano x ente federado na publicação oficial do FNDE. Ano específico: 2011.

| Column | Type | Description |
|---|---|---|
| `ano` | STRING | Ano de exercício do previsto (raw). |
| `uf` | STRING | Sigla da UF do ente. |
| `ente_federado` | STRING | Nome do ente federado. |
| `cod_ibge` | STRING | Código IBGE do ente ou identificador agregado histórico. |
| `esfera` | STRING | Esfera administrativa do ente. |
| `coeficiente` | STRING | Coeficiente oficial como texto bruto. |
| `vl_previsto_receita` | STRING | Valor previsto bruto como texto/normalizado. |
| `portaria` | STRING | Portaria FNDE identificada na origem. |
| `source_url` | STRING | URL do PDF oficial de origem. |
| `pdf_hash` | STRING | Hash do PDF processado. |
| `dt_ingestao_lake` | STRING | Timestamp UTC da ingestão no lake. |

## raw · fnde_salario_educacao_previsto_2012

File `raw__fnde_salario_educacao_previsto_2012.parquet` · 5,590 rows · 11 columns

Salário-Educação (FNDE) — previsto/estimativa por ente federado, camada raw anual. 1 linha por ano x ente federado na publicação oficial do FNDE. Ano específico: 2012.

| Column | Type | Description |
|---|---|---|
| `ano` | STRING | Ano de exercício do previsto (raw). |
| `uf` | STRING | Sigla da UF do ente. |
| `ente_federado` | STRING | Nome do ente federado. |
| `cod_ibge` | STRING | Código IBGE do ente ou identificador agregado histórico. |
| `esfera` | STRING | Esfera administrativa do ente. |
| `coeficiente` | STRING | Coeficiente oficial como texto bruto. |
| `vl_previsto_receita` | STRING | Valor previsto bruto como texto/normalizado. |
| `portaria` | STRING | Portaria FNDE identificada na origem. |
| `source_url` | STRING | URL do PDF oficial de origem. |
| `pdf_hash` | STRING | Hash do PDF processado. |
| `dt_ingestao_lake` | STRING | Timestamp UTC da ingestão no lake. |

## raw · fnde_salario_educacao_previsto_2013

File `raw__fnde_salario_educacao_previsto_2013.parquet` · 5,590 rows · 11 columns

Salário-Educação (FNDE) — previsto/estimativa por ente federado, camada raw anual. 1 linha por ano x ente federado na publicação oficial do FNDE. Ano específico: 2013.

| Column | Type | Description |
|---|---|---|
| `ano` | STRING | Ano de exercício do previsto (raw). |
| `uf` | STRING | Sigla da UF do ente. |
| `ente_federado` | STRING | Nome do ente federado. |
| `cod_ibge` | STRING | Código IBGE do ente ou identificador agregado histórico. |
| `esfera` | STRING | Esfera administrativa do ente. |
| `coeficiente` | STRING | Coeficiente oficial como texto bruto. |
| `vl_previsto_receita` | STRING | Valor previsto bruto como texto/normalizado. |
| `portaria` | STRING | Portaria FNDE identificada na origem. |
| `source_url` | STRING | URL do PDF oficial de origem. |
| `pdf_hash` | STRING | Hash do PDF processado. |
| `dt_ingestao_lake` | STRING | Timestamp UTC da ingestão no lake. |

## raw · fnde_salario_educacao_previsto_2014

File `raw__fnde_salario_educacao_previsto_2014.parquet` · 5,595 rows · 11 columns

Salário-Educação (FNDE) — previsto/estimativa por ente federado, camada raw anual. 1 linha por ano x ente federado na publicação oficial do FNDE. Ano específico: 2014.

| Column | Type | Description |
|---|---|---|
| `ano` | STRING | Ano de exercício do previsto (raw). |
| `uf` | STRING | Sigla da UF do ente. |
| `ente_federado` | STRING | Nome do ente federado. |
| `cod_ibge` | STRING | Código IBGE do ente ou identificador agregado histórico. |
| `esfera` | STRING | Esfera administrativa do ente. |
| `coeficiente` | STRING | Coeficiente oficial como texto bruto. |
| `vl_previsto_receita` | STRING | Valor previsto bruto como texto/normalizado. |
| `portaria` | STRING | Portaria FNDE identificada na origem. |
| `source_url` | STRING | URL do PDF oficial de origem. |
| `pdf_hash` | STRING | Hash do PDF processado. |
| `dt_ingestao_lake` | STRING | Timestamp UTC da ingestão no lake. |

## raw · fnde_salario_educacao_previsto_2015

File `raw__fnde_salario_educacao_previsto_2015.parquet` · 5,595 rows · 11 columns

Salário-Educação (FNDE) — previsto/estimativa por ente federado, camada raw anual. 1 linha por ano x ente federado na publicação oficial do FNDE. Ano específico: 2015.

| Column | Type | Description |
|---|---|---|
| `ano` | STRING | Ano de exercício do previsto (raw). |
| `uf` | STRING | Sigla da UF do ente. |
| `ente_federado` | STRING | Nome do ente federado. |
| `cod_ibge` | STRING | Código IBGE do ente ou identificador agregado histórico. |
| `esfera` | STRING | Esfera administrativa do ente. |
| `coeficiente` | STRING | Coeficiente oficial como texto bruto. |
| `vl_previsto_receita` | STRING | Valor previsto bruto como texto/normalizado. |
| `portaria` | STRING | Portaria FNDE identificada na origem. |
| `source_url` | STRING | URL do PDF oficial de origem. |
| `pdf_hash` | STRING | Hash do PDF processado. |
| `dt_ingestao_lake` | STRING | Timestamp UTC da ingestão no lake. |

## raw · fnde_salario_educacao_previsto_2016

File `raw__fnde_salario_educacao_previsto_2016.parquet` · 5,595 rows · 11 columns

Salário-Educação (FNDE) — previsto/estimativa por ente federado, camada raw anual. 1 linha por ano x ente federado na publicação oficial do FNDE. Ano específico: 2016.

| Column | Type | Description |
|---|---|---|
| `ano` | STRING | Ano de exercício do previsto (raw). |
| `uf` | STRING | Sigla da UF do ente. |
| `ente_federado` | STRING | Nome do ente federado. |
| `cod_ibge` | STRING | Código IBGE do ente ou identificador agregado histórico. |
| `esfera` | STRING | Esfera administrativa do ente. |
| `coeficiente` | STRING | Coeficiente oficial como texto bruto. |
| `vl_previsto_receita` | STRING | Valor previsto bruto como texto/normalizado. |
| `portaria` | STRING | Portaria FNDE identificada na origem. |
| `source_url` | STRING | URL do PDF oficial de origem. |
| `pdf_hash` | STRING | Hash do PDF processado. |
| `dt_ingestao_lake` | STRING | Timestamp UTC da ingestão no lake. |

## raw · fnde_salario_educacao_previsto_2017

File `raw__fnde_salario_educacao_previsto_2017.parquet` · 5,595 rows · 11 columns

Salário-Educação (FNDE) — previsto/estimativa por ente federado, camada raw anual. 1 linha por ano x ente federado na publicação oficial do FNDE. Ano específico: 2017.

| Column | Type | Description |
|---|---|---|
| `ano` | STRING | Ano de exercício do previsto (raw). |
| `uf` | STRING | Sigla da UF do ente. |
| `ente_federado` | STRING | Nome do ente federado. |
| `cod_ibge` | STRING | Código IBGE do ente ou identificador agregado histórico. |
| `esfera` | STRING | Esfera administrativa do ente. |
| `coeficiente` | STRING | Coeficiente oficial como texto bruto. |
| `vl_previsto_receita` | STRING | Valor previsto bruto como texto/normalizado. |
| `portaria` | STRING | Portaria FNDE identificada na origem. |
| `source_url` | STRING | URL do PDF oficial de origem. |
| `pdf_hash` | STRING | Hash do PDF processado. |
| `dt_ingestao_lake` | STRING | Timestamp UTC da ingestão no lake. |

## raw · fnde_salario_educacao_previsto_2018

File `raw__fnde_salario_educacao_previsto_2018.parquet` · 5,595 rows · 11 columns

Salário-Educação (FNDE) — previsto/estimativa por ente federado, camada raw anual. 1 linha por ano x ente federado na publicação oficial do FNDE. Ano específico: 2018.

| Column | Type | Description |
|---|---|---|
| `ano` | STRING | Ano de exercício do previsto (raw). |
| `uf` | STRING | Sigla da UF do ente. |
| `ente_federado` | STRING | Nome do ente federado. |
| `cod_ibge` | STRING | Código IBGE do ente ou identificador agregado histórico. |
| `esfera` | STRING | Esfera administrativa do ente. |
| `coeficiente` | STRING | Coeficiente oficial como texto bruto. |
| `vl_previsto_receita` | STRING | Valor previsto bruto como texto/normalizado. |
| `portaria` | STRING | Portaria FNDE identificada na origem. |
| `source_url` | STRING | URL do PDF oficial de origem. |
| `pdf_hash` | STRING | Hash do PDF processado. |
| `dt_ingestao_lake` | STRING | Timestamp UTC da ingestão no lake. |

## raw · fnde_salario_educacao_previsto_2019

File `raw__fnde_salario_educacao_previsto_2019.parquet` · 5,595 rows · 11 columns

Salário-Educação (FNDE) — previsto/estimativa por ente federado, camada raw anual. 1 linha por ano x ente federado na publicação oficial do FNDE. Ano específico: 2019.

| Column | Type | Description |
|---|---|---|
| `ano` | STRING | Ano de exercício do previsto (raw). |
| `uf` | STRING | Sigla da UF do ente. |
| `ente_federado` | STRING | Nome do ente federado. |
| `cod_ibge` | STRING | Código IBGE do ente ou identificador agregado histórico. |
| `esfera` | STRING | Esfera administrativa do ente. |
| `coeficiente` | STRING | Coeficiente oficial como texto bruto. |
| `vl_previsto_receita` | STRING | Valor previsto bruto como texto/normalizado. |
| `portaria` | STRING | Portaria FNDE identificada na origem. |
| `source_url` | STRING | URL do PDF oficial de origem. |
| `pdf_hash` | STRING | Hash do PDF processado. |
| `dt_ingestao_lake` | STRING | Timestamp UTC da ingestão no lake. |

## raw · fnde_salario_educacao_previsto_2020

File `raw__fnde_salario_educacao_previsto_2020.parquet` · 5,595 rows · 11 columns

Salário-Educação (FNDE) — previsto/estimativa por ente federado, camada raw anual. 1 linha por ano x ente federado na publicação oficial do FNDE. Ano específico: 2020.

| Column | Type | Description |
|---|---|---|
| `ano` | STRING | Ano de exercício do previsto (raw). |
| `uf` | STRING | Sigla da UF do ente. |
| `ente_federado` | STRING | Nome do ente federado. |
| `cod_ibge` | STRING | Código IBGE do ente ou identificador agregado histórico. |
| `esfera` | STRING | Esfera administrativa do ente. |
| `coeficiente` | STRING | Coeficiente oficial como texto bruto. |
| `vl_previsto_receita` | STRING | Valor previsto bruto como texto/normalizado. |
| `portaria` | STRING | Portaria FNDE identificada na origem. |
| `source_url` | STRING | URL do PDF oficial de origem. |
| `pdf_hash` | STRING | Hash do PDF processado. |
| `dt_ingestao_lake` | STRING | Timestamp UTC da ingestão no lake. |

## raw · fnde_salario_educacao_previsto_2021

File `raw__fnde_salario_educacao_previsto_2021.parquet` · 5,595 rows · 11 columns

Salário-Educação (FNDE) — previsto/estimativa por ente federado, camada raw anual. 1 linha por ano x ente federado na publicação oficial do FNDE. Ano específico: 2021.

| Column | Type | Description |
|---|---|---|
| `ano` | STRING | Ano de exercício do previsto (raw). |
| `uf` | STRING | Sigla da UF do ente. |
| `ente_federado` | STRING | Nome do ente federado. |
| `cod_ibge` | STRING | Código IBGE do ente ou identificador agregado histórico. |
| `esfera` | STRING | Esfera administrativa do ente. |
| `coeficiente` | STRING | Coeficiente oficial como texto bruto. |
| `vl_previsto_receita` | STRING | Valor previsto bruto como texto/normalizado. |
| `portaria` | STRING | Portaria FNDE identificada na origem. |
| `source_url` | STRING | URL do PDF oficial de origem. |
| `pdf_hash` | STRING | Hash do PDF processado. |
| `dt_ingestao_lake` | STRING | Timestamp UTC da ingestão no lake. |

## raw · fnde_salario_educacao_previsto_2022

File `raw__fnde_salario_educacao_previsto_2022.parquet` · 5,595 rows · 11 columns

Salário-Educação (FNDE) — previsto/estimativa por ente federado, camada raw anual. 1 linha por ano x ente federado na publicação oficial do FNDE. Ano específico: 2022.

| Column | Type | Description |
|---|---|---|
| `ano` | STRING | Ano de exercício do previsto (raw). |
| `uf` | STRING | Sigla da UF do ente. |
| `ente_federado` | STRING | Nome do ente federado. |
| `cod_ibge` | STRING | Código IBGE do ente ou identificador agregado histórico. |
| `esfera` | STRING | Esfera administrativa do ente. |
| `coeficiente` | STRING | Coeficiente oficial como texto bruto. |
| `vl_previsto_receita` | STRING | Valor previsto bruto como texto/normalizado. |
| `portaria` | STRING | Portaria FNDE identificada na origem. |
| `source_url` | STRING | URL do PDF oficial de origem. |
| `pdf_hash` | STRING | Hash do PDF processado. |
| `dt_ingestao_lake` | STRING | Timestamp UTC da ingestão no lake. |

## raw · fnde_salario_educacao_previsto_2023

File `raw__fnde_salario_educacao_previsto_2023.parquet` · 5,595 rows · 11 columns

Salário-Educação (FNDE) — previsto/estimativa por ente federado, camada raw anual. 1 linha por ano x ente federado na publicação oficial do FNDE. Ano específico: 2023.

| Column | Type | Description |
|---|---|---|
| `ano` | STRING | Ano de exercício do previsto (raw). |
| `uf` | STRING | Sigla da UF do ente. |
| `ente_federado` | STRING | Nome do ente federado. |
| `cod_ibge` | STRING | Código IBGE do ente ou identificador agregado histórico. |
| `esfera` | STRING | Esfera administrativa do ente. |
| `coeficiente` | STRING | Coeficiente oficial como texto bruto. |
| `vl_previsto_receita` | STRING | Valor previsto bruto como texto/normalizado. |
| `portaria` | STRING | Portaria FNDE identificada na origem. |
| `source_url` | STRING | URL do PDF oficial de origem. |
| `pdf_hash` | STRING | Hash do PDF processado. |
| `dt_ingestao_lake` | STRING | Timestamp UTC da ingestão no lake. |

## raw · fnde_salario_educacao_previsto_2024

File `raw__fnde_salario_educacao_previsto_2024.parquet` · 5,595 rows · 11 columns

Salário-Educação (FNDE) — previsto/estimativa por ente federado, camada raw anual. 1 linha por ano x ente federado na publicação oficial do FNDE. Ano específico: 2024.

| Column | Type | Description |
|---|---|---|
| `ano` | STRING | Ano de exercício do previsto (raw). |
| `uf` | STRING | Sigla da UF do ente. |
| `ente_federado` | STRING | Nome do ente federado. |
| `cod_ibge` | STRING | Código IBGE do ente ou identificador agregado histórico. |
| `esfera` | STRING | Esfera administrativa do ente. |
| `coeficiente` | STRING | Coeficiente oficial como texto bruto. |
| `vl_previsto_receita` | STRING | Valor previsto bruto como texto/normalizado. |
| `portaria` | STRING | Portaria FNDE identificada na origem. |
| `source_url` | STRING | URL do PDF oficial de origem. |
| `pdf_hash` | STRING | Hash do PDF processado. |
| `dt_ingestao_lake` | STRING | Timestamp UTC da ingestão no lake. |

## raw · fnde_salario_educacao_previsto_2025

File `raw__fnde_salario_educacao_previsto_2025.parquet` · 5,595 rows · 11 columns

Salário-Educação (FNDE) — previsto/estimativa por ente federado, camada raw anual. 1 linha por ano x ente federado na publicação oficial do FNDE. Ano específico: 2025.

| Column | Type | Description |
|---|---|---|
| `ano` | STRING | Ano de exercício do previsto (raw). |
| `uf` | STRING | Sigla da UF do ente. |
| `ente_federado` | STRING | Nome do ente federado. |
| `cod_ibge` | STRING | Código IBGE do ente ou identificador agregado histórico. |
| `esfera` | STRING | Esfera administrativa do ente. |
| `coeficiente` | STRING | Coeficiente oficial como texto bruto. |
| `vl_previsto_receita` | STRING | Valor previsto bruto como texto/normalizado. |
| `portaria` | STRING | Portaria FNDE identificada na origem. |
| `source_url` | STRING | URL do PDF oficial de origem. |
| `pdf_hash` | STRING | Hash do PDF processado. |
| `dt_ingestao_lake` | STRING | Timestamp UTC da ingestão no lake. |

## raw · fnde_salario_educacao_previsto_2026

File `raw__fnde_salario_educacao_previsto_2026.parquet` · 5,596 rows · 11 columns

Salário-Educação (FNDE) — estimativa anual das quotas por ente federado, exercício 2026, camada RAW (tudo STRING). 1 linha por ente. A fonte é anual: o FNDE não publica abertura mensal da estimativa.

| Column | Type | Description |
|---|---|---|
| `ano` | STRING | Ano de exercício da estimativa. |
| `uf` | STRING | Sigla da UF do ente. |
| `ente_federado` | STRING | Nome do ente: município ou GOVERNO ESTADUAL. |
| `cod_ibge` | STRING | Código IBGE do município (7 dígitos) ou UF_<sigla> na quota estadual. |
| `esfera` | STRING | 'municipal' ou 'estadual'. |
| `coeficiente` | STRING | Coeficiente de distribuição do ente. |
| `vl_previsto_receita` | STRING | Estimativa de receita do ente no exercício (R$). |
| `portaria` | STRING | Portaria FNDE que publicou a estimativa. |
| `source_url` | STRING | URL do PDF oficial de origem. |
| `pdf_hash` | STRING | Hash do PDF ingerido. |
| `dt_ingestao_lake` | STRING | Timestamp UTC da ingestão. |

## raw · fnde_salario_educacao_realizado_2000

File `raw__fnde_salario_educacao_realizado_2000.parquet` · 24 rows · 21 columns

Salário-Educação (FNDE) — distribuído/realizado por ente federado, camada raw anual. 1 linha por ano x ente federado na publicação oficial do FNDE, com colunas mensais preservadas. Ano específico: 2000.

| Column | Type | Description |
|---|---|---|
| `ano` | STRING | Ano de referência do distribuído (raw). |
| `uf` | STRING | Sigla da UF do ente. |
| `ente_federado` | STRING | Nome do ente federado. |
| `cod_ibge` | STRING | Código IBGE do ente ou identificador agregado histórico. |
| `esfera` | STRING | Esfera administrativa do ente. |
| `competencias_com_valor` | STRING | Quantidade de competências com valor informado. |
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

## raw · fnde_salario_educacao_realizado_2001

File `raw__fnde_salario_educacao_realizado_2001.parquet` · 23 rows · 21 columns

Salário-Educação (FNDE) — distribuído/realizado por ente federado, camada raw anual. 1 linha por ano x ente federado na publicação oficial do FNDE, com colunas mensais preservadas. Ano específico: 2001.

| Column | Type | Description |
|---|---|---|
| `ano` | STRING | Ano de referência do distribuído (raw). |
| `uf` | STRING | Sigla da UF do ente. |
| `ente_federado` | STRING | Nome do ente federado. |
| `cod_ibge` | STRING | Código IBGE do ente ou identificador agregado histórico. |
| `esfera` | STRING | Esfera administrativa do ente. |
| `competencias_com_valor` | STRING | Quantidade de competências com valor informado. |
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

## raw · fnde_salario_educacao_realizado_2002

File `raw__fnde_salario_educacao_realizado_2002.parquet` · 24 rows · 21 columns

Salário-Educação (FNDE) — distribuído/realizado por ente federado, camada raw anual. 1 linha por ano x ente federado na publicação oficial do FNDE, com colunas mensais preservadas. Ano específico: 2002.

| Column | Type | Description |
|---|---|---|
| `ano` | STRING | Ano de referência do distribuído (raw). |
| `uf` | STRING | Sigla da UF do ente. |
| `ente_federado` | STRING | Nome do ente federado. |
| `cod_ibge` | STRING | Código IBGE do ente ou identificador agregado histórico. |
| `esfera` | STRING | Esfera administrativa do ente. |
| `competencias_com_valor` | STRING | Quantidade de competências com valor informado. |
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

## raw · fnde_salario_educacao_realizado_2003

File `raw__fnde_salario_educacao_realizado_2003.parquet` · 24 rows · 21 columns

Salário-Educação (FNDE) — distribuído/realizado por ente federado, camada raw anual. 1 linha por ano x ente federado na publicação oficial do FNDE, com colunas mensais preservadas. Ano específico: 2003.

| Column | Type | Description |
|---|---|---|
| `ano` | STRING | Ano de referência do distribuído (raw). |
| `uf` | STRING | Sigla da UF do ente. |
| `ente_federado` | STRING | Nome do ente federado. |
| `cod_ibge` | STRING | Código IBGE do ente ou identificador agregado histórico. |
| `esfera` | STRING | Esfera administrativa do ente. |
| `competencias_com_valor` | STRING | Quantidade de competências com valor informado. |
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

## raw · fnde_salario_educacao_realizado_2004

File `raw__fnde_salario_educacao_realizado_2004.parquet` · 54 rows · 21 columns

Salário-Educação (FNDE) — distribuído/realizado por ente federado, camada raw anual. 1 linha por ano x ente federado na publicação oficial do FNDE, com colunas mensais preservadas. Ano específico: 2004.

| Column | Type | Description |
|---|---|---|
| `ano` | STRING | Ano de referência do distribuído (raw). |
| `uf` | STRING | Sigla da UF do ente. |
| `ente_federado` | STRING | Nome do ente federado. |
| `cod_ibge` | STRING | Código IBGE do ente ou identificador agregado histórico. |
| `esfera` | STRING | Esfera administrativa do ente. |
| `competencias_com_valor` | STRING | Quantidade de competências com valor informado. |
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

## raw · fnde_salario_educacao_realizado_2005

File `raw__fnde_salario_educacao_realizado_2005.parquet` · 54 rows · 21 columns

Salário-Educação (FNDE) — distribuído/realizado por ente federado, camada raw anual. 1 linha por ano x ente federado na publicação oficial do FNDE, com colunas mensais preservadas. Ano específico: 2005.

| Column | Type | Description |
|---|---|---|
| `ano` | STRING | Ano de referência do distribuído (raw). |
| `uf` | STRING | Sigla da UF do ente. |
| `ente_federado` | STRING | Nome do ente federado. |
| `cod_ibge` | STRING | Código IBGE do ente ou identificador agregado histórico. |
| `esfera` | STRING | Esfera administrativa do ente. |
| `competencias_com_valor` | STRING | Quantidade de competências com valor informado. |
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

## raw · fnde_salario_educacao_realizado_2006

File `raw__fnde_salario_educacao_realizado_2006.parquet` · 54 rows · 21 columns

Salário-Educação (FNDE) — distribuído/realizado por ente federado, camada raw anual. 1 linha por ano x ente federado na publicação oficial do FNDE, com colunas mensais preservadas. Ano específico: 2006.

| Column | Type | Description |
|---|---|---|
| `ano` | STRING | Ano de referência do distribuído (raw). |
| `uf` | STRING | Sigla da UF do ente. |
| `ente_federado` | STRING | Nome do ente federado. |
| `cod_ibge` | STRING | Código IBGE do ente ou identificador agregado histórico. |
| `esfera` | STRING | Esfera administrativa do ente. |
| `competencias_com_valor` | STRING | Quantidade de competências com valor informado. |
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

## raw · fnde_salario_educacao_realizado_2007

File `raw__fnde_salario_educacao_realizado_2007.parquet` · 54 rows · 21 columns

Salário-Educação (FNDE) — distribuído/realizado por ente federado, camada raw anual. 1 linha por ano x ente federado na publicação oficial do FNDE, com colunas mensais preservadas. Ano específico: 2007.

| Column | Type | Description |
|---|---|---|
| `ano` | STRING | Ano de referência do distribuído (raw). |
| `uf` | STRING | Sigla da UF do ente. |
| `ente_federado` | STRING | Nome do ente federado. |
| `cod_ibge` | STRING | Código IBGE do ente ou identificador agregado histórico. |
| `esfera` | STRING | Esfera administrativa do ente. |
| `competencias_com_valor` | STRING | Quantidade de competências com valor informado. |
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

## raw · fnde_salario_educacao_realizado_2008

File `raw__fnde_salario_educacao_realizado_2008.parquet` · 54 rows · 21 columns

Salário-Educação (FNDE) — distribuído/realizado por ente federado, camada raw anual. 1 linha por ano x ente federado na publicação oficial do FNDE, com colunas mensais preservadas. Ano específico: 2008.

| Column | Type | Description |
|---|---|---|
| `ano` | STRING | Ano de referência do distribuído (raw). |
| `uf` | STRING | Sigla da UF do ente. |
| `ente_federado` | STRING | Nome do ente federado. |
| `cod_ibge` | STRING | Código IBGE do ente ou identificador agregado histórico. |
| `esfera` | STRING | Esfera administrativa do ente. |
| `competencias_com_valor` | STRING | Quantidade de competências com valor informado. |
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

## raw · fnde_salario_educacao_realizado_2009

File `raw__fnde_salario_educacao_realizado_2009.parquet` · 52 rows · 21 columns

Salário-Educação (FNDE) — distribuição mensal por ente federado, exercício 2009, camada RAW (tudo STRING). Layout antigo: o documento não abre por município, traz a quota ESTADUAL e o agregado da rede MUNICIPAL de cada UF. 1 linha por (UF, esfera) com as 12 competências e o total.

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

## raw · fnde_salario_educacao_realizado_2010

File `raw__fnde_salario_educacao_realizado_2010.parquet` · 54 rows · 21 columns

Salário-Educação (FNDE) — distribuído/realizado por ente federado, camada raw anual. 1 linha por ano x ente federado na publicação oficial do FNDE, com colunas mensais preservadas. Ano específico: 2010.

| Column | Type | Description |
|---|---|---|
| `ano` | STRING | Ano de referência do distribuído (raw). |
| `uf` | STRING | Sigla da UF do ente. |
| `ente_federado` | STRING | Nome do ente federado. |
| `cod_ibge` | STRING | Código IBGE do ente ou identificador agregado histórico. |
| `esfera` | STRING | Esfera administrativa do ente. |
| `competencias_com_valor` | STRING | Quantidade de competências com valor informado. |
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

## raw · fnde_salario_educacao_realizado_2011

File `raw__fnde_salario_educacao_realizado_2011.parquet` · 54 rows · 21 columns

Salário-Educação (FNDE) — distribuição mensal por ente federado, exercício 2011, camada RAW (tudo STRING). Layout antigo: o documento não abre por município, traz a quota ESTADUAL e o agregado da rede MUNICIPAL de cada UF. 1 linha por (UF, esfera) com as 12 competências e o total.

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

## raw · fnde_salario_educacao_realizado_2012

File `raw__fnde_salario_educacao_realizado_2012.parquet` · 54 rows · 21 columns

Salário-Educação (FNDE) — distribuição mensal por ente federado, exercício 2012, camada RAW (tudo STRING). Layout antigo: o documento não abre por município, traz a quota ESTADUAL e o agregado da rede MUNICIPAL de cada UF. 1 linha por (UF, esfera) com as 12 competências e o total.

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

## raw · fnde_salario_educacao_realizado_2013

File `raw__fnde_salario_educacao_realizado_2013.parquet` · 54 rows · 21 columns

Salário-Educação (FNDE) — distribuição mensal por ente federado, exercício 2013, camada RAW (tudo STRING). Layout antigo: o documento não abre por município, traz a quota ESTADUAL e o agregado da rede MUNICIPAL de cada UF. 1 linha por (UF, esfera) com as 12 competências e o total.

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

## raw · fnde_salario_educacao_realizado_2014

File `raw__fnde_salario_educacao_realizado_2014.parquet` · 54 rows · 21 columns

Salário-Educação (FNDE) — distribuição mensal por ente federado, exercício 2014, camada RAW (tudo STRING). Layout antigo: o documento não abre por município, traz a quota ESTADUAL e o agregado da rede MUNICIPAL de cada UF. 1 linha por (UF, esfera) com as 12 competências e o total.

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

## raw · fnde_salario_educacao_realizado_2015

File `raw__fnde_salario_educacao_realizado_2015.parquet` · 54 rows · 21 columns

Salário-Educação (FNDE) — distribuição mensal por ente federado, exercício 2015, camada RAW (tudo STRING). Layout antigo: o documento não abre por município, traz a quota ESTADUAL e o agregado da rede MUNICIPAL de cada UF. 1 linha por (UF, esfera) com as 12 competências e o total.

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

## raw · fnde_salario_educacao_realizado_2016

File `raw__fnde_salario_educacao_realizado_2016.parquet` · 54 rows · 21 columns

Salário-Educação (FNDE) — distribuição mensal por ente federado, exercício 2016, camada RAW (tudo STRING). Layout antigo: o documento não abre por município, traz a quota ESTADUAL e o agregado da rede MUNICIPAL de cada UF. 1 linha por (UF, esfera) com as 12 competências e o total.

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

## raw · fnde_salario_educacao_realizado_2017

File `raw__fnde_salario_educacao_realizado_2017.parquet` · 54 rows · 21 columns

Salário-Educação (FNDE) — distribuição mensal por ente federado, exercício 2017, camada RAW (tudo STRING). Layout antigo: o documento não abre por município, traz a quota ESTADUAL e o agregado da rede MUNICIPAL de cada UF. 1 linha por (UF, esfera) com as 12 competências e o total.

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

## raw · fnde_salario_educacao_realizado_2018

File `raw__fnde_salario_educacao_realizado_2018.parquet` · 54 rows · 21 columns

Salário-Educação (FNDE) — distribuição mensal por ente federado, exercício 2018, camada RAW (tudo STRING). Layout antigo: o documento não abre por município, traz a quota ESTADUAL e o agregado da rede MUNICIPAL de cada UF. 1 linha por (UF, esfera) com as 12 competências e o total.

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

## raw · fnde_salario_educacao_realizado_2019

File `raw__fnde_salario_educacao_realizado_2019.parquet` · 54 rows · 21 columns

Salário-Educação (FNDE) — distribuição mensal por ente federado, exercício 2019, camada RAW (tudo STRING). Layout antigo: o documento não abre por município, traz a quota ESTADUAL e o agregado da rede MUNICIPAL de cada UF. 1 linha por (UF, esfera) com as 12 competências e o total.

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

## raw · fnde_salario_educacao_realizado_2020

File `raw__fnde_salario_educacao_realizado_2020.parquet` · 5,594 rows · 21 columns

Salário-Educação (FNDE) — distribuído/realizado por ente federado, camada raw anual. 1 linha por ano x ente federado na publicação oficial do FNDE, com colunas mensais preservadas. Ano específico: 2020.

| Column | Type | Description |
|---|---|---|
| `ano` | STRING | Ano de referência do distribuído (raw). |
| `uf` | STRING | Sigla da UF do ente. |
| `ente_federado` | STRING | Nome do ente federado. |
| `cod_ibge` | STRING | Código IBGE do ente ou identificador agregado histórico. |
| `esfera` | STRING | Esfera administrativa do ente. |
| `competencias_com_valor` | STRING | Quantidade de meses no ano com repasse de recursos registrado. — descrição gerada por IA. |
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

## raw · fnde_salario_educacao_realizado_2021

File `raw__fnde_salario_educacao_realizado_2021.parquet` · 5,596 rows · 21 columns

Salário-Educação (FNDE) — distribuído/realizado por ente federado, camada raw anual. 1 linha por ano x ente federado na publicação oficial do FNDE, com colunas mensais preservadas. Ano específico: 2021.

| Column | Type | Description |
|---|---|---|
| `ano` | STRING | Ano de referência do distribuído (raw). |
| `uf` | STRING | Sigla da UF do ente. |
| `ente_federado` | STRING | Nome do ente federado. |
| `cod_ibge` | STRING | Código IBGE do ente ou identificador agregado histórico. |
| `esfera` | STRING | Esfera administrativa do ente. |
| `competencias_com_valor` | STRING | Quantidade de meses do ano em que houve repasse efetivo registrado. — descrição gerada por IA. |
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

## raw · fnde_salario_educacao_realizado_2022

File `raw__fnde_salario_educacao_realizado_2022.parquet` · 5,595 rows · 21 columns

Salário-Educação (FNDE) — distribuído/realizado por ente federado, camada raw anual. 1 linha por ano x ente federado na publicação oficial do FNDE, com colunas mensais preservadas. Ano específico: 2022.

| Column | Type | Description |
|---|---|---|
| `ano` | STRING | Ano de referência do distribuído (raw). |
| `uf` | STRING | Sigla da UF do ente. |
| `ente_federado` | STRING | Nome do ente federado. |
| `cod_ibge` | STRING | Código IBGE do ente ou identificador agregado histórico. |
| `esfera` | STRING | Esfera administrativa do ente. |
| `competencias_com_valor` | STRING | Quantidade de meses do ano em que houve registro de repasse financeiro. — descrição gerada por IA. |
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
