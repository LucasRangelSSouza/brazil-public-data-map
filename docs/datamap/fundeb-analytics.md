# FUNDEB: Analytics

Dataset: [lucasrangelss/fundeb-analytics](https://www.kaggle.com/datasets/lucasrangelss/fundeb-analytics) · snapshot 2026-09-30 · 4 tables · 4,105,508 rows

**Source:** Fundo Nacional de Desenvolvimento da Educação (FNDE), [https://www.fnde.gov.br/](https://www.fnde.gov.br/)

The FUNDEB panel: complementation by VAAF, VAAT and VAAR, distribution, qualification and indicators per entity and year.

**Grain and keys:** One row per federal entity (state or municipality) and year for the panel tables.

**Layers.** `raw` is the source snapshot as delivered. `trusted` is typed, deduplicated and named consistently. `semantic` joins and reshapes trusted tables for analysis. Every table is a Parquet file named `<layer>__<table>.parquet` at the root of the dataset.

The full interactive map (lineage, joins, search) is at [https://rangeltech.net/datamap/](https://rangeltech.net/datamap/). Column descriptions come from the source lake's catalogue and are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns | Described | Upstream |
|---|---|---:|---:|---:|---|
| semantic | [`obt_fnde_fundeb_cronograma_vaat_municipio_ano`](#semantic-obt-fnde-fundeb-cronograma-vaat-municipio-ano) | 13,030 | 24 | 24 | `obt_ibge_municipio`, `fundeb_painel_cronograma_vaat` |
| semantic | [`obt_fnde_fundeb_distribuicao_municipio_mes`](#semantic-obt-fnde-fundeb-distribuicao-municipio-mes) | 3,382,306 | 16 | 16 | `obt_ibge_municipio`, `fundeb_painel_distribuicao` |
| semantic | [`obt_fnde_fundeb_indicadores_siope_municipio_ano`](#semantic-obt-fnde-fundeb-indicadores-siope-municipio-ano) | 626,256 | 12 | 12 | `obt_ibge_municipio`, `fundeb_painel_indicadores_siope` |
| semantic | [`obt_fnde_fundeb_municipio_ano`](#semantic-obt-fnde-fundeb-municipio-ano) | 83,916 | 34 | 34 | `obt_ibge_municipio`, `fundeb_painel_complementacao`, `fundeb_painel_cronograma_vaat`, `fundeb_painel_dim_entes` … |

## semantic · obt_fnde_fundeb_cronograma_vaat_municipio_ano

File `semantic__obt_fnde_fundeb_cronograma_vaat_municipio_ano.parquet` · 13,030 rows · 24 columns

FUNDEB — cronograma mensal da complementacao VAAT por municipio x ano (parcelas mes a mes, ajuste, acerto e total distribuido). Fonte: Painel FUNDEB (FNDE).

**Built from:** `semantic/obt_ibge_municipio`, `trusted/fundeb_painel_cronograma_vaat`

| Column | Type | Description |
|---|---|---|
| `ano` | INTEGER | Ano de referencia. |
| `codigo_municipio` | INTEGER | Codigo IBGE do municipio (INT64). FK -> obt_ibge_municipio. |
| `ente_federado` | STRING | Nome do ente federado (municipio ou governo estadual). |
| `sigla_uf` | STRING | Sigla da UF. |
| `nome_municipio` | STRING | Nome do municipio (IBGE). |
| `nome_uf` | STRING | Nome da UF (IBGE). |
| `nome_regiao` | STRING | Nome da regiao (IBGE). |
| `vl_mes_1` | NUMERIC | Parcela do mes 1 da complementacao VAAT distribuida ao ente (R$). |
| `vl_mes_2` | NUMERIC | Parcela do mes 2 da complementacao VAAT distribuida ao ente (R$). |
| `vl_mes_3` | NUMERIC | Parcela do mes 3 da complementacao VAAT distribuida ao ente (R$). |
| `vl_mes_4` | NUMERIC | Parcela do mes 4 da complementacao VAAT distribuida ao ente (R$). |
| `vl_mes_5` | NUMERIC | Parcela do mes 5 da complementacao VAAT distribuida ao ente (R$). |
| `vl_mes_6` | NUMERIC | Parcela do mes 6 da complementacao VAAT distribuida ao ente (R$). |
| `vl_mes_7` | NUMERIC | Parcela do mes 7 da complementacao VAAT distribuida ao ente (R$). |
| `vl_mes_8` | NUMERIC | Parcela do mes 8 da complementacao VAAT distribuida ao ente (R$). |
| `vl_mes_9` | NUMERIC | Parcela do mes 9 da complementacao VAAT distribuida ao ente (R$). |
| `vl_mes_10` | NUMERIC | Parcela do mes 10 da complementacao VAAT distribuida ao ente (R$). |
| `vl_mes_11` | NUMERIC | Parcela do mes 11 da complementacao VAAT distribuida ao ente (R$). |
| `vl_mes_12` | NUMERIC | Parcela do mes 12 da complementacao VAAT distribuida ao ente (R$). |
| `vl_mes_1_seg` | NUMERIC | Parcela complementar (2a) referente ao mes 1 do cronograma VAAT (R$). |
| `vl_ajuste` | NUMERIC | Ajuste aplicado ao cronograma VAAT (R$). |
| `vl_acerto` | NUMERIC | Acerto de contas do cronograma VAAT (R$). |
| `vl_distribuicao_ente` | NUMERIC | Total do VAAT distribuido ao ente no ano (soma do cronograma) (R$). |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC de geracao na camada semantica. |

## semantic · obt_fnde_fundeb_distribuicao_municipio_mes

File `semantic__obt_fnde_fundeb_distribuicao_municipio_mes.parquet` · 3,382,306 rows · 16 columns

FUNDEB — valores efetivamente distribuidos (pagos) por municipio/estado x ano x mes x fonte de repasse. Fonte: Painel FUNDEB (FNDE, Power BI). Grao: ente x ano x mes x transferencia x categoria.

**Built from:** `semantic/obt_ibge_municipio`, `trusted/fundeb_painel_distribuicao`

| Column | Type | Description |
|---|---|---|
| `ano` | INTEGER | Ano de referencia. |
| `mes_num` | INTEGER | Mes numerico (1-12). |
| `mes_nome` | STRING | Mes por extenso. |
| `codigo_ibge` | STRING | Codigo IBGE bruto (municipio 7 digitos; governo estadual 2 digitos = UF). |
| `codigo_municipio` | INTEGER | Codigo IBGE do municipio (INT64). FK -> obt_ibge_municipio. |
| `esfera` | STRING | Esfera do ente: Estadual ou Municipal. |
| `ente_federado` | STRING | Nome do ente federado (municipio ou governo estadual). |
| `sigla_uf` | STRING | Sigla da UF. |
| `regiao` | STRING | Regiao geografica (bruto do painel). |
| `transferencia` | STRING | Fonte do repasse: FUNDEB/FPE, /FPM, /ICMS, /IPVA, /ITCMD, /ITR, /IPI-EXP, /COUN VAAF, /COUN VAAT, /COUN VAAR, AJUSTE FUNDEB. |
| `categoria_de_repasse` | STRING | Categoria: Contribuicao de Estados/DF/Municipios ou Complementacao da Uniao. |
| `vl_distribuido` | NUMERIC | Valor efetivamente distribuido (pago) ao ente no mes/fonte (R$). |
| `nome_municipio` | STRING | Nome do municipio (IBGE). |
| `nome_uf` | STRING | Nome da UF (IBGE). |
| `nome_regiao` | STRING | Nome da regiao (IBGE). |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC de geracao na camada semantica. |

## semantic · obt_fnde_fundeb_indicadores_siope_municipio_ano

File `semantic__obt_fnde_fundeb_indicadores_siope_municipio_ano.parquet` · 626,256 rows · 12 columns

FUNDEB indicadores legais SIOPE por municipio x ano x periodo. Fonte: Painel FUNDEB (FNDE, Power BI). LONG. codigo_municipio=IBGE 7dig derivado do codigo-ente 12dig (UF+sufixo); codigo_ente_original preserva o original.

**Built from:** `semantic/obt_ibge_municipio`, `trusted/fundeb_painel_indicadores_siope`

| Column | Type | Description |
|---|---|---|
| `ano` | INTEGER | Ano de referencia. |
| `periodo` | INTEGER | Periodo/bimestre do indicador. |
| `codigo_ente_original` | STRING | Código identificador original do ente federativo no sistema de origem. |
| `codigo_municipio` | INTEGER | Codigo IBGE do municipio (INT64). FK -> obt_ibge_municipio. |
| `ente_federado` | STRING | Nome do ente federado (municipio ou governo estadual). |
| `sigla_uf` | STRING | Sigla da UF. |
| `nome_municipio` | STRING | Nome do municipio (IBGE). |
| `nome_uf` | STRING | Nome da UF (IBGE). |
| `nome_regiao` | STRING | Nome da regiao (IBGE). |
| `nome_indicador` | STRING | Indicador legal SIOPE (MDE 25%, remuneracao 70%, MDE 40%, IEI, aplicacao VAAT em educacao infantil/capital, % destinacao ao Fundeb etc.). |
| `valor_indicador` | NUMERIC | Valor apurado do indicador. |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC de geracao na camada semantica. |

## semantic · obt_fnde_fundeb_municipio_ano

File `semantic__obt_fnde_fundeb_municipio_ano.parquet` · 83,916 rows · 34 columns

FUNDEB — visao consolidada por municipio/estado x ano: matriculas ponderadas, coeficientes, complementacao VAAF/VAAT, distribuicao VAAR, receita total, total efetivamente distribuido no ano, e situacao de habilitacao VAAT/VAAR. Fonte: Painel FUNDEB (FNDE). Uma linha por ente x ano.

**Built from:** `semantic/obt_ibge_municipio`, `trusted/fundeb_painel_complementacao`, `trusted/fundeb_painel_cronograma_vaat`, `trusted/fundeb_painel_dim_entes`, `trusted/fundeb_painel_distribuicao`, `trusted/fundeb_painel_habilitacao_vaar`, `trusted/fundeb_painel_habilitacao_vaat`

**Feeds:** `semantic/obt_api_olinda_siope_indicadores_municipio_ano`, `semantic/obt_api_olinda_siope_indicadores_uf_ano`

| Column | Type | Description |
|---|---|---|
| `ano` | INTEGER | Ano de referencia. |
| `codigo_municipio` | INTEGER | Codigo IBGE do municipio (INT64). FK -> obt_ibge_municipio. |
| `ente_federado` | STRING | Nome do ente federado (municipio ou governo estadual). |
| `sigla_uf` | STRING | Sigla da UF. |
| `nome_municipio` | STRING | Nome do municipio (IBGE). |
| `nome_uf` | STRING | Nome da UF (IBGE). |
| `nome_regiao` | STRING | Nome da regiao (IBGE). |
| `tipo_governo` | STRING | Tipo de governo: Municipal ou Estadual. |
| `is_capital` | BOOLEAN | TRUE se o municipio e capital de estado. |
| `qt_matriculas` | INTEGER | Quantidade total de matrículas na educação básica pública consideradas na contagem. — descrição gerada por IA. |
| `qt_matriculas_pond_vaaf` | NUMERIC | Matriculas ponderadas para o VAAF. |
| `qt_matriculas_pond_vaaf_fundo` | NUMERIC | Matriculas ponderadas VAAF no ambito do fundo estadual. |
| `qt_matriculas_pond_vaat` | NUMERIC | Matriculas ponderadas para o VAAT. |
| `vl_coeficiente_vaaf` | NUMERIC | Coeficiente de distribuicao do VAAF (nao e R$). |
| `vl_coeficiente_vaar` | NUMERIC | Coeficiente de distribuicao do VAAR (nao e R$). |
| `vl_receita_fundo_vaaf` | NUMERIC | Receita do fundo considerada no VAAF (R$). |
| `vl_receita_vaat` | NUMERIC | Receita considerada no calculo do VAAT (R$). |
| `vl_total_vaat` | NUMERIC | Valor total do VAAT (R$). |
| `vl_complementacao_vaaf` | NUMERIC | Complementacao da Uniao via VAAF (R$). |
| `vl_complementacao_vaaf_uf` | NUMERIC | Complementacao VAAF no ambito da UF (R$). |
| `vl_complementacao_vaat` | NUMERIC | Complementacao da Uniao via VAAT (R$). |
| `vl_distribuicao_vaar` | NUMERIC | Distribuicao da Uniao via VAAR - resultados (R$). |
| `vl_complementacao_total` | NUMERIC | Complementacao total da Uniao (VAAF+VAAT+VAAR) (R$). |
| `vl_contribuicao_estados` | NUMERIC | Contribuicao de estados/DF/municipios ao fundo (R$). |
| `vl_total_receitas` | NUMERIC | Total de receitas do fundo para o ente (R$). |
| `vl_vaaf_min` | NUMERIC | VAAF minimo por aluno definido nacionalmente (R$). |
| `vl_vaat_min` | NUMERIC | VAAT minimo definido nacionalmente (R$). |
| `vl_total_distribuido_ano` | NUMERIC | Total efetivamente pago ao ente no ano (soma de todas as fontes/meses) (R$). |
| `vl_vaat_distribuido_ano` | NUMERIC | Total do VAAT distribuido ao ente no ano (do cronograma) (R$). |
| `habilitado_vaat` | BOOLEAN | TRUE se o ente esta habilitado a receber VAAT. |
| `motivos_vaat` | STRING | Motivos de (in)habilitacao ao VAAT (concatenado). |
| `habilitado_vaar` | BOOLEAN | TRUE se o ente esta habilitado a receber VAAR. |
| `motivos_vaar` | STRING | Motivos de (in)habilitacao ao VAAR (concatenado). |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC de geracao na camada semantica. |
