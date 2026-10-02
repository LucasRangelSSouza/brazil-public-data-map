# FUNDEB: Raw and Trusted

Dataset: [lucasrangelss/fundeb-raw-trusted](https://www.kaggle.com/datasets/lucasrangelss/fundeb-raw-trusted) · snapshot 2026-09-30 · 14 tables · 10,107,275 rows

**Source:** Fundo Nacional de Desenvolvimento da Educação (FNDE), [https://www.fnde.gov.br/](https://www.fnde.gov.br/)

The FUNDEB panel: complementation by VAAF, VAAT and VAAR, distribution, qualification and indicators per entity and year.

**Grain and keys:** One row per federal entity (state or municipality) and year for the panel tables.

**Layers.** `raw` is the source snapshot as delivered. `trusted` is typed, deduplicated and named consistently. `semantic` joins and reshapes trusted tables for analysis. Every table is a Parquet file named `<layer>__<table>.parquet` at the root of the dataset.

The full interactive map (lineage, joins, search) is at [https://rangeltech.net/datamap/](https://rangeltech.net/datamap/). Column descriptions come from the source lake's catalogue and are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns | Described | Upstream |
|---|---|---:|---:|---:|---|
| raw | [`fnde_fundeb_painel_complementacao`](#raw-fnde-fundeb-painel-complementacao) | 106,300 | 25 | 25 | source |
| raw | [`fnde_fundeb_painel_cronograma_vaat`](#raw-fnde-fundeb-painel-cronograma-vaat) | 23,246 | 23 | 23 | source |
| raw | [`fnde_fundeb_painel_dim_entes`](#raw-fnde-fundeb-painel-dim-entes) | 27,980 | 14 | 14 | source |
| raw | [`fnde_fundeb_painel_distribuicao`](#raw-fnde-fundeb-painel-distribuicao) | 4,362,779 | 12 | 12 | source |
| raw | [`fnde_fundeb_painel_hab_vaar`](#raw-fnde-fundeb-painel-hab-vaar) | 268,712 | 10 | 10 | source |
| raw | [`fnde_fundeb_painel_hab_vaat`](#raw-fnde-fundeb-painel-hab-vaat) | 55,955 | 9 | 9 | source |
| raw | [`fnde_fundeb_painel_indicadores`](#raw-fnde-fundeb-painel-indicadores) | 983,302 | 10 | 10 | source |
| trusted | [`fundeb_painel_complementacao`](#trusted-fundeb-painel-complementacao) | 83,916 | 25 | 25 | `fnde_fundeb_painel_complementacao` |
| trusted | [`fundeb_painel_cronograma_vaat`](#trusted-fundeb-painel-cronograma-vaat) | 13,030 | 23 | 23 | `fnde_fundeb_painel_cronograma_vaat` |
| trusted | [`fundeb_painel_dim_entes`](#trusted-fundeb-painel-dim-entes) | 5,570 | 14 | 14 | `fnde_fundeb_painel_dim_entes` |
| trusted | [`fundeb_painel_distribuicao`](#trusted-fundeb-painel-distribuicao) | 3,382,306 | 15 | 15 | `fnde_fundeb_painel_distribuicao` |
| trusted | [`fundeb_painel_habilitacao_vaar`](#trusted-fundeb-painel-habilitacao-vaar) | 134,352 | 11 | 11 | `fnde_fundeb_painel_hab_vaar` |
| trusted | [`fundeb_painel_habilitacao_vaat`](#trusted-fundeb-painel-habilitacao-vaat) | 33,571 | 10 | 10 | `fnde_fundeb_painel_hab_vaat` |
| trusted | [`fundeb_painel_indicadores_siope`](#trusted-fundeb-painel-indicadores-siope) | 626,256 | 10 | 10 | `fnde_fundeb_painel_indicadores` |

## raw · fnde_fundeb_painel_complementacao

File `raw__fnde_fundeb_painel_complementacao.parquet` · 106,300 rows · 25 columns

Tabela com dados de distribuição de recursos do FUNDEB (VAAF, VAAT e VAAR) por ente federado (municípios e estados) e ano vigente, incluindo matrículas ponderadas e valores de complementação da União.

**Feeds:** `trusted/fundeb_painel_complementacao`

| Column | Type | Description |
|---|---|---|
| `co_ibge` | STRING | Código IBGE de identificação do município ou estado (ente federado). |
| `no_ente_federado` | STRING | Nome do ente federado (município ou governo estadual). |
| `sg_uf` | STRING | Sigla da Unidade da Federação (Estado). |
| `ano_vigente` | STRING | Ano de referência dos dados financeiros e de matrículas (formato YYYY). |
| `qt_matriculas` | FLOAT | Quantidade total bruta de matrículas da educação básica consideradas no ente. — descrição gerada por IA. |
| `qt_matriculas_pond_vaaf` | FLOAT | Quantidade de matrículas ponderadas calculadas para a redistribuição do VAAF. — descrição gerada por IA. |
| `qt_matriculas_pond_vaaf_fundo` | FLOAT | Quantidade total de matrículas ponderadas consolidadas no fundo estadual do VAAF. — descrição gerada por IA. |
| `qt_matriculas_pond_vaat` | FLOAT | Quantidade de matrículas ponderadas calculadas para a complementação do VAAT. — descrição gerada por IA. |
| `vl_receita_fundo_vaaf` | FLOAT | Valor total da receita do fundo para o cálculo do VAAF (em Reais). |
| `vl_complementacao_vaaf_uf` | FLOAT | Valor da complementação do VAAF realizada pelo estado (em Reais). |
| `vl_receita_vaat` | FLOAT | Valor da receita estimada para o cálculo do VAAT (em Reais). |
| `vl_total_vaat` | FLOAT | Valor total de recursos do VAAT destinados ao ente federado (em Reais). |
| `vl_coeficiente_vaaf` | FLOAT | Coeficiente de distribuição do VAAF do ente federado no fundo estadual. |
| `vl_coeficiente_vaar` | FLOAT | Coeficiente de distribuição do VAAR (Valor Aluno Ano Resultado) do ente federado. |
| `vl_contribuicao_estados` | FLOAT | Valor da contribuição financeira do estado para o fundo (em Reais). |
| `vl_complementacao_vaaf` | FLOAT | Valor da complementação da União ao VAAF para o ente federado (em Reais). |
| `vl_complementacao_vaat` | FLOAT | Valor da complementação da União ao VAAT para o ente federado (em Reais). |
| `vl_distribuicao_vaar` | FLOAT | Valor distribuído ao ente federado referente ao VAAR (em Reais). |
| `vl_complementacao_total` | FLOAT | Valor total da complementação da União (VAAF + VAAT + VAAR) recebida (em Reais). |
| `vl_total_receitas` | FLOAT | Valor total das receitas do FUNDEB distribuídas ao ente federado (em Reais). |
| `vl_vaat_min` | FLOAT | Valor mínimo definido por aluno/ano para o VAAT no ano vigente (em Reais). |
| `vl_vaaf_min` | FLOAT | Valor mínimo definido por aluno/ano para o VAAF no ano vigente (em Reais). |
| `ctrl_fonte_url` | STRING | URL da fonte original dos dados (painéis do PowerBI ou portais governamentais). |
| `ctrl_tabela_bi` | STRING | Identificador ou sigla da tabela de origem no Business Intelligence (BI). |
| `dt_extracao_lake` | TIMESTAMP | Data e hora do processamento e inclusão do registro no Data Lake (AAAA-MM-DD HH:MM:SS). — descrição gerada por IA. |

## raw · fnde_fundeb_painel_cronograma_vaat

File `raw__fnde_fundeb_painel_cronograma_vaat.parquet` · 23,246 rows · 23 columns

Cronograma de repasses e distribuição mensal de recursos do VAAT (Valor Aluno Ano Total) do FUNDEB para estados e municípios.

**Feeds:** `trusted/fundeb_painel_cronograma_vaat`

| Column | Type | Description |
|---|---|---|
| `co_ibge` | STRING | Código identificador de 7 dígitos do IBGE para o município ou estado. |
| `no_ente_federado` | STRING | Nome do município ou estado beneficiário dos recursos. |
| `sg_uf` | STRING | Sigla da Unidade da Federação (estado). |
| `ano_vigente` | STRING | Ano de referência dos repasses financeiros (formato YYYY). |
| `vl_mes_1` | FLOAT | Valor financeiro repassado no mês de Janeiro, em Reais (R$). |
| `vl_mes_2` | FLOAT | Valor financeiro repassado no mês de Fevereiro, em Reais (R$). |
| `vl_mes_3` | FLOAT | Valor financeiro repassado no mês de Março, em Reais (R$). |
| `vl_mes_4` | FLOAT | Valor financeiro repassado no mês de Abril, em Reais (R$). |
| `vl_mes_5` | FLOAT | Valor financeiro repassado no mês de Maio, em Reais (R$). |
| `vl_mes_6` | FLOAT | Valor financeiro repassado no mês de Junho, em Reais (R$). |
| `vl_mes_7` | FLOAT | Valor financeiro repassado no mês de Julho, em Reais (R$). |
| `vl_mes_8` | FLOAT | Valor financeiro repassado no mês de Agosto, em Reais (R$). |
| `vl_mes_9` | FLOAT | Valor financeiro repassado no mês de Setembro, em Reais (R$). |
| `vl_mes_10` | FLOAT | Valor financeiro repassado no mês de Outubro, em Reais (R$). |
| `vl_mes_11` | FLOAT | Valor financeiro repassado no mês de Novembro, em Reais (R$). |
| `vl_mes_12` | FLOAT | Valor financeiro repassado no mês de Dezembro, em Reais (R$). |
| `vl_mes_1_seg` | FLOAT | Valor da segunda parcela ou repasse complementar referente ao mês de Janeiro, em Reais (R$). |
| `vl_ajuste` | FLOAT | Valor de ajuste financeiro anual aplicado ao ente federado, em Reais (R$). |
| `vl_acerto` | FLOAT | Valor de acerto ou correção de repasses de exercícios anteriores, em Reais (R$). |
| `vl_distribuicao_ente` | FLOAT | Valor total anual distribuído ao ente federado, em Reais (R$). |
| `ctrl_fonte_url` | STRING | URL da fonte original dos dados (painel do Power BI de origem). |
| `ctrl_tabela_bi` | STRING | Nome da tabela de controle correspondente na origem do BI. |
| `dt_extracao_lake` | TIMESTAMP | Data e hora de extração do dado para o Data Lake (formato YYYY-MM-DD HH:MM:SS). — descrição gerada por IA. |

## raw · fnde_fundeb_painel_dim_entes

File `raw__fnde_fundeb_painel_dim_entes.parquet` · 27,980 rows · 14 columns

corp_entes_uf_municipios

**Feeds:** `trusted/fundeb_painel_dim_entes`

| Column | Type | Description |
|---|---|---|
| `co_municipio_ibge` | STRING | Código identificador do município com 7 dígitos, padronizado pelo IBGE. |
| `co_municipio_ibge_completo` | STRING | Código estendido de identificação do município baseado na divisão territorial do IBGE. |
| `co_municipio_fnde` | STRING | Código identificador do município utilizado pelo Fundo Nacional de Desenvolvimento da Educação (FNDE). |
| `nome_ente` | STRING | Nome oficial do ente federativo (município ou estado). |
| `sg_uf` | STRING | Sigla da Unidade Federativa com duas letras (ex: RO, AC). |
| `no_uf` | STRING | Nome completo da Unidade Federativa (ex: Rondônia, Acre). |
| `co_uf_ibge` | STRING | Código numérico de dois dígitos que identifica a Unidade Federativa no IBGE. |
| `sg_regiao` | STRING | Sigla da região geográfica brasileira (ex: N, NE, CO, SE, S). |
| `no_regiao` | STRING | Nome completo da região geográfica brasileira (ex: NORTE, NORDESTE). |
| `tipo_governo` | STRING | Esfera administrativa do governo (ex: Governo Estadual, Governo Municipal). |
| `st_capital_estado` | STRING | Indicador se o ente federativo é a capital do estado (S para Sim, N para Não). |
| `ctrl_fonte_url` | STRING | URL de origem do relatório ou painel de BI de onde os dados foram extraídos. |
| `ctrl_tabela_bi` | STRING | Nome da tabela de origem no sistema de Business Intelligence (BI). |
| `dt_extracao_lake` | TIMESTAMP | Data e hora do carregamento do registro no Data Lake (YYYY-MM-DD HH:MM:SS). — descrição gerada por IA. |

## raw · fnde_fundeb_painel_distribuicao

File `raw__fnde_fundeb_painel_distribuicao.parquet` · 4,362,779 rows · 12 columns

Tabela com dados de repasses e contribuições financeiras do FUNDEB (Fundo de Manutenção e Desenvolvimento da Educação Básica) para estados e municípios brasileiros, detalhados por ano, mês e categoria.

**Feeds:** `trusted/fundeb_painel_distribuicao`

| Column | Type | Description |
|---|---|---|
| `codigo_ibge` | STRING | Código identificador do IBGE para o estado ou município (formato numérico em string). |
| `ente_federado` | STRING | Tipo de ente federativo beneficiado ou responsável (ex: Governo de Estado, Município). |
| `uf` | STRING | Sigla da unidade da federação onde se encontra o estabelecimento. |
| `regiao` | STRING | Região geográfica do Brasil onde se localiza o ente federativo. |
| `ano` | STRING | Ano de referência do repasse financeiro (formato YYYY). |
| `mes` | STRING | Mês de referência do repasse financeiro por extenso. |
| `transferencia` | STRING | Sigla ou código identificador do tipo de transferência ou origem do recurso (ex: FUNDEB/FPE, FUNDEB/ICMS). |
| `categoria_de_repasse` | STRING | Classificação da categoria do repasse (ex: Complementação da União, Contribuição de Estados). |
| `total` | FLOAT | Valor monetário total repassado ou contribuído em Reais (formato decimal). |
| `ctrl_fonte_url` | STRING | URL de controle que aponta para a origem dos dados no relatório do PowerBI. |
| `ctrl_tabela_bi` | STRING | Nome da tabela ou planilha de origem no sistema de Business Intelligence de origem. |
| `dt_extracao_lake` | TIMESTAMP | Data e hora do processamento e carga do registro no Data Lake (AAAA-MM-DD HH:MM:SS). — descrição gerada por IA. |

## raw · fnde_fundeb_painel_hab_vaar

File `raw__fnde_fundeb_painel_hab_vaar.parquet` · 268,712 rows · 10 columns

Tabela que armazena o histórico de habilitação e inabilitação dos entes federativos (municípios e estados) para o recebimento do VAAR (Valor Aluno Ano Resultado) do FUNDEB, detalhando o cumprimento de condicionalidades e critérios específicos.

**Feeds:** `trusted/fundeb_painel_habilitacao_vaar`

| Column | Type | Description |
|---|---|---|
| `ano_vigente` | STRING | Ano de referência e vigência da avaliação do VAAR (formato YYYY). |
| `sg_uf` | STRING | Sigla da Unidade Federativa do ente avaliado. |
| `nome_ente` | STRING | Nome do município ou estado avaliado. |
| `co_ibge` | STRING | Código de 7 dígitos do IBGE que identifica univocamente o município. |
| `situacao_vaar` | STRING | Situação de habilitação do ente para o recebimento do VAAR (ex: Habilitado, Inabilitado). |
| `atributo` | STRING | Condicionalidade ou critério específico do VAAR em avaliação (ex: ICMS educacional, eleição de diretores). |
| `motivo` | STRING | Descrição do motivo ou justificativa para o resultado da avaliação do atributo. |
| `ctrl_fonte_url` | STRING | URL do painel ou relatório de origem (Power BI) utilizado para auditoria e controle. |
| `ctrl_tabela_bi` | STRING | Nome da tabela de origem no ambiente de Business Intelligence (BI). |
| `dt_extracao_lake` | TIMESTAMP | Data e hora de extração e carga do registro no Data Lake (formato 'AAAA-MM-DD HH:MM:SS'). — descrição gerada por IA. |

## raw · fnde_fundeb_painel_hab_vaat

File `raw__fnde_fundeb_painel_hab_vaat.parquet` · 55,955 rows · 9 columns

Histórico de habilitação e inabilitação dos entes federados (estados e municípios) para o recebimento de recursos do VAAT (Valor Aluno Ano Total), detalhando conformidades legais e pendências financeiras.

**Feeds:** `trusted/fundeb_painel_habilitacao_vaat`

| Column | Type | Description |
|---|---|---|
| `uf` | STRING | Sigla da unidade da federação onde se encontra o estabelecimento. |
| `ente_federado` | STRING | Nome do município ou estado analisado. |
| `codigo_ibge` | STRING | Código identificador do IBGE para o estado (2 dígitos) ou município (7 dígitos). |
| `ano` | STRING | Ano de referência da análise de habilitação (formato YYYY). |
| `situacao` | STRING | Status de habilitação do ente federado ('Habilitado' ou 'Inabilitado') perante os critérios do VAAT/FNDE. — descrição gerada por IA. |
| `motivos` | STRING | Descrição do motivo ou base legal que determinou a situação de habilitação ou inabilitação. |
| `ctrl_fonte_url` | STRING | URL de controle que aponta para o relatório ou painel de origem no Power BI. |
| `ctrl_tabela_bi` | STRING | Nome da tabela ou arquivo de origem no ambiente de BI/SharePoint. |
| `dt_extracao_lake` | TIMESTAMP | Data e hora do registro da extração do dado para o Data Lake no formato 'AAAA-MM-DD HH:MM:SS'. — descrição gerada por IA. |

## raw · fnde_fundeb_painel_indicadores

File `raw__fnde_fundeb_painel_indicadores.parquet` · 983,302 rows · 10 columns

Tabela contendo os indicadores legais do SIOPE e FUNDEB por ente federativo, detalhando o cumprimento de limites constitucionais e legais de investimento em educação (como aplicação em MDE e valorização do magistério).

**Feeds:** `trusted/fundeb_painel_indicadores_siope`

| Column | Type | Description |
|---|---|---|
| `num_ano` | STRING | Ano de referência dos dados financeiros e educacionais (formato YYYY). |
| `num_peri` | STRING | Período de referência do relatório dentro do ano (ex: bimestre ou semestre). |
| `sig_uf` | STRING | Sigla da Unidade da Federação (estado) do ente federativo. |
| `co_ibge_completo_agrupado` | STRING | Código IBGE do estado ou município utilizado para georreferenciamento e cruzamento de dados. |
| `nome_ente` | STRING | Nome do ente federativo (município ou estado) responsável pela aplicação dos recursos. |
| `nom_indi` | STRING | Nome do indicador legal avaliado (ex: percentual mínimo aplicado em educação infantil ou magistério). |
| `val_indi` | FLOAT | Valor numérico do indicador, geralmente expresso em formato percentual ou decimal. |
| `ctrl_fonte_url` | STRING | URL da fonte original dos dados (painel do PowerBI do SIOPE/FNDE) para fins de auditoria. |
| `ctrl_tabela_bi` | STRING | Nome da tabela de origem no sistema de Business Intelligence (BI) de onde os dados foram extraídos. |
| `dt_extracao_lake` | TIMESTAMP | Data e horário da carga/extração dos dados para o data lake (formato YYYY-MM-DD HH:MM:SS). — descrição gerada por IA. |

## trusted · fundeb_painel_complementacao

File `trusted__fundeb_painel_complementacao.parquet` · 83,916 rows · 25 columns

FUNDEB Painel FNDE — complementacao/coeficientes/matriculas por ente x ano (tabela stl). Grao: co_ibge x ano_vigente.

**Built from:** `raw/fnde_fundeb_painel_complementacao`

**Feeds:** `semantic/obt_fnde_fundeb_municipio_ano`

| Column | Type | Description |
|---|---|---|
| `ano` | INTEGER | Ano de referencia do FUNDEB. |
| `codigo_municipio` | STRING | Codigo IBGE do municipio, 7 digitos. FK -> semantic/obt_ibge_municipio.codigo_municipio. |
| `ente_federado` | STRING | Nome do ente federado (municipio ou governo estadual). |
| `sigla_uf` | STRING | Sigla da UF (ex.: SP, MG). |
| `qt_matriculas` | INTEGER | Quantidade total de matrículas presenciais na rede pública consideradas pelo FUNDEB. — descrição gerada por IA. |
| `qt_matriculas_pond_vaaf` | NUMERIC | Matriculas ponderadas para calculo do VAAF. |
| `qt_matriculas_pond_vaaf_fundo` | NUMERIC | Matriculas ponderadas VAAF no ambito do fundo estadual. |
| `qt_matriculas_pond_vaat` | NUMERIC | Matriculas ponderadas para calculo do VAAT. |
| `vl_receita_fundo_vaaf` | NUMERIC | Receita do fundo considerada no VAAF, em R$. |
| `vl_complementacao_vaaf_uf` | NUMERIC | Complementacao VAAF no ambito da UF, em R$. |
| `vl_receita_vaat` | NUMERIC | Receita considerada no calculo do VAAT, em R$. |
| `vl_total_vaat` | NUMERIC | Valor total do VAAT, em R$. |
| `vl_coeficiente_vaaf` | NUMERIC | Coeficiente de distribuicao do VAAF. |
| `vl_coeficiente_vaar` | NUMERIC | Coeficiente de distribuicao do VAAR. |
| `vl_contribuicao_estados` | NUMERIC | Contribuicao de estados/DF/municipios ao fundo, em R$. |
| `vl_complementacao_vaaf` | NUMERIC | Complementacao da Uniao via VAAF, em R$. |
| `vl_complementacao_vaat` | NUMERIC | Complementacao da Uniao via VAAT, em R$. |
| `vl_distribuicao_vaar` | NUMERIC | Distribuicao da Uniao via VAAR (resultados), em R$. |
| `vl_complementacao_total` | NUMERIC | Complementacao total da Uniao (VAAF+VAAT+VAAR), em R$. |
| `vl_total_receitas` | NUMERIC | Total de receitas do fundo para o ente, em R$. |
| `vl_vaat_min` | NUMERIC | VAAT minimo por aluno definido nacionalmente, em R$. |
| `vl_vaaf_min` | NUMERIC | VAAF minimo por aluno definido nacionalmente, em R$. |
| `ctrl_fonte_url` | STRING | URL do Painel FUNDEB (Power BI) de origem. |
| `ctrl_tabela_bi` | STRING | Tabela do modelo Power BI de origem. |
| `dt_extracao_lake` | TIMESTAMP | Timestamp UTC da extracao do painel. |

## trusted · fundeb_painel_cronograma_vaat

File `trusted__fundeb_painel_cronograma_vaat.parquet` · 13,030 rows · 23 columns

FUNDEB Painel FNDE — cronograma mensal da complementacao VAAT por ente x ano. Grao: co_ibge x ano_vigente.

**Built from:** `raw/fnde_fundeb_painel_cronograma_vaat`

**Feeds:** `semantic/obt_fnde_fundeb_cronograma_vaat_municipio_ano`, `semantic/obt_fnde_fundeb_municipio_ano`

| Column | Type | Description |
|---|---|---|
| `ano` | INTEGER | Ano de referencia do FUNDEB. |
| `codigo_municipio` | STRING | Codigo IBGE do municipio, 7 digitos. FK -> semantic/obt_ibge_municipio.codigo_municipio. |
| `ente_federado` | STRING | Nome do ente federado (municipio ou governo estadual). |
| `sigla_uf` | STRING | Sigla da UF (ex.: SP, MG). |
| `vl_mes_1` | NUMERIC | Parcela do mes 1 da complementacao VAAT distribuida ao ente, em R$. |
| `vl_mes_2` | NUMERIC | Parcela do mes 2 da complementacao VAAT distribuida ao ente, em R$. |
| `vl_mes_3` | NUMERIC | Parcela do mes 3 da complementacao VAAT distribuida ao ente, em R$. |
| `vl_mes_4` | NUMERIC | Parcela do mes 4 da complementacao VAAT distribuida ao ente, em R$. |
| `vl_mes_5` | NUMERIC | Parcela do mes 5 da complementacao VAAT distribuida ao ente, em R$. |
| `vl_mes_6` | NUMERIC | Parcela do mes 6 da complementacao VAAT distribuida ao ente, em R$. |
| `vl_mes_7` | NUMERIC | Parcela do mes 7 da complementacao VAAT distribuida ao ente, em R$. |
| `vl_mes_8` | NUMERIC | Parcela do mes 8 da complementacao VAAT distribuida ao ente, em R$. |
| `vl_mes_9` | NUMERIC | Parcela do mes 9 da complementacao VAAT distribuida ao ente, em R$. |
| `vl_mes_10` | NUMERIC | Parcela do mes 10 da complementacao VAAT distribuida ao ente, em R$. |
| `vl_mes_11` | NUMERIC | Parcela do mes 11 da complementacao VAAT distribuida ao ente, em R$. |
| `vl_mes_12` | NUMERIC | Parcela do mes 12 da complementacao VAAT distribuida ao ente, em R$. |
| `vl_mes_1_seg` | NUMERIC | Parcela complementar (2a) referente ao mes 1 do cronograma VAAT, em R$. |
| `vl_ajuste` | NUMERIC | Ajuste aplicado ao cronograma VAAT, em R$. |
| `vl_acerto` | NUMERIC | Acerto de contas do cronograma VAAT, em R$. |
| `vl_distribuicao_ente` | NUMERIC | Total do VAAT distribuido ao ente no ano (soma do cronograma), em R$. |
| `ctrl_fonte_url` | STRING | URL do Painel FUNDEB (Power BI) de origem. |
| `ctrl_tabela_bi` | STRING | Tabela do modelo Power BI de origem. |
| `dt_extracao_lake` | TIMESTAMP | Timestamp UTC da extracao do painel. |

## trusted · fundeb_painel_dim_entes

File `trusted__fundeb_painel_dim_entes.parquet` · 5,570 rows · 14 columns

FUNDEB Painel FNDE — dimensao de entes (geografia): municipio/estado, UF, regiao, tipo de governo.

**Built from:** `raw/fnde_fundeb_painel_dim_entes`

**Feeds:** `semantic/obt_fnde_fundeb_municipio_ano`

| Column | Type | Description |
|---|---|---|
| `codigo_municipio` | STRING | Codigo IBGE do municipio, 7 digitos. FK -> semantic/obt_ibge_municipio.codigo_municipio. |
| `codigo_ibge_completo` | STRING | Codigo IBGE completo agrupado do ente (identificador do painel). |
| `codigo_municipio_fnde` | STRING | Codigo do municipio no padrao FNDE. |
| `ente_federado` | STRING | Nome do ente federado (municipio ou governo estadual). |
| `sigla_uf` | STRING | Sigla da UF (ex.: SP, MG). |
| `nome_uf` | STRING | Nome da UF. |
| `codigo_uf` | STRING | Codigo IBGE da UF (2 digitos). |
| `sigla_regiao` | STRING | Sigla da regiao geografica. |
| `nome_regiao` | STRING | Nome da regiao geografica. |
| `tipo_governo` | STRING | Tipo de governo: Municipal ou Estadual. |
| `is_capital` | BOOLEAN | TRUE se o municipio e capital de estado. |
| `ctrl_fonte_url` | STRING | URL do Painel FUNDEB (Power BI) de origem. |
| `ctrl_tabela_bi` | STRING | Tabela do modelo Power BI de origem. |
| `dt_extracao_lake` | TIMESTAMP | Timestamp UTC da extracao do painel. |

## trusted · fundeb_painel_distribuicao

File `trusted__fundeb_painel_distribuicao.parquet` · 3,382,306 rows · 15 columns

FUNDEB Painel FNDE — valores efetivamente distribuidos (pagos) por ente/ano/mes/fonte. Grao: codigo_ibge x ano x mes x transferencia x categoria. Dedup pela extracao mais recente.

**Built from:** `raw/fnde_fundeb_painel_distribuicao`

**Feeds:** `semantic/obt_api_olinda_siope_indicadores_uf_ano`, `semantic/obt_fnde_fundeb_distribuicao_municipio_mes`, `semantic/obt_fnde_fundeb_municipio_ano`

| Column | Type | Description |
|---|---|---|
| `ano` | INTEGER | Ano de referencia do FUNDEB. |
| `mes_num` | INTEGER | Mes numerico (1-12). |
| `mes_nome` | STRING | Mes por extenso. |
| `codigo_ibge` | STRING | Codigo IBGE bruto (municipio 7 digitos; governo estadual 2 digitos = UF). |
| `codigo_municipio` | STRING | Codigo IBGE do municipio, 7 digitos. FK -> semantic/obt_ibge_municipio.codigo_municipio. |
| `esfera` | STRING | Esfera do ente: Estadual ou Municipal. |
| `ente_federado` | STRING | Nome do ente federado (municipio ou governo estadual). |
| `sigla_uf` | STRING | Sigla da UF (ex.: SP, MG). |
| `regiao` | STRING | Regiao geografica do ente. |
| `transferencia` | STRING | Fonte do repasse ao FUNDEB: FUNDEB/FPE, /FPM, /ICMS, /IPVA, /ITCMD, /ITR, /IPI-EXP, /COUN VAAF, /COUN VAAT, /COUN VAAR, AJUSTE FUNDEB etc. |
| `categoria_de_repasse` | STRING | Categoria do repasse: Contribuicao de Estados/DF/Municipios ou Complementacao da Uniao. |
| `vl_distribuido` | NUMERIC | Valor efetivamente distribuido (pago) ao ente no mes, em R$. |
| `ctrl_fonte_url` | STRING | URL do Painel FUNDEB (Power BI) de origem. |
| `ctrl_tabela_bi` | STRING | Tabela do modelo Power BI de origem. |
| `dt_extracao_lake` | TIMESTAMP | Timestamp UTC da extracao do painel. |

## trusted · fundeb_painel_habilitacao_vaar

File `trusted__fundeb_painel_habilitacao_vaar.parquet` · 134,352 rows · 11 columns

FUNDEB Painel FNDE — habilitacao VAAR (situacao + motivo/atributo de inabilitacao) por ente x ano. Grao: co_ibge x ano x situacao x atributo x motivo.

**Built from:** `raw/fnde_fundeb_painel_hab_vaar`

**Feeds:** `semantic/obt_fnde_fundeb_municipio_ano`

| Column | Type | Description |
|---|---|---|
| `ano` | INTEGER | Ano de referencia do FUNDEB. |
| `codigo_municipio` | STRING | Codigo IBGE do municipio, 7 digitos. FK -> semantic/obt_ibge_municipio.codigo_municipio. |
| `ente_federado` | STRING | Nome do ente federado (municipio ou governo estadual). |
| `sigla_uf` | STRING | Sigla da UF (ex.: SP, MG). |
| `situacao_vaar` | STRING | Situacao de habilitacao ao VAAR (Habilitado/Inabilitado). |
| `habilitado_vaar` | BOOLEAN | TRUE se o ente esta habilitado a receber VAAR. |
| `atributo` | STRING | Atributo/dimensao da condicao de habilitacao VAAR. |
| `motivo` | STRING | Motivo da (in)habilitacao ao VAAR. |
| `ctrl_fonte_url` | STRING | URL do Painel FUNDEB (Power BI) de origem. |
| `ctrl_tabela_bi` | STRING | Tabela do modelo Power BI de origem. |
| `dt_extracao_lake` | TIMESTAMP | Timestamp UTC da extracao do painel. |

## trusted · fundeb_painel_habilitacao_vaat

File `trusted__fundeb_painel_habilitacao_vaat.parquet` · 33,571 rows · 10 columns

FUNDEB Painel FNDE — habilitacao VAAT (serie historica: situacao + motivo) por ente x ano. Grao: codigo_ibge x ano x motivos.

**Built from:** `raw/fnde_fundeb_painel_hab_vaat`

**Feeds:** `semantic/obt_fnde_fundeb_municipio_ano`

| Column | Type | Description |
|---|---|---|
| `ano` | INTEGER | Ano de referencia do FUNDEB. |
| `codigo_municipio` | STRING | Codigo IBGE do municipio, 7 digitos. FK -> semantic/obt_ibge_municipio.codigo_municipio. |
| `ente_federado` | STRING | Nome do ente federado (municipio ou governo estadual). |
| `sigla_uf` | STRING | Sigla da UF (ex.: SP, MG). |
| `situacao` | STRING | Situacao de habilitacao ao VAAT (Habilitado/Inabilitado). |
| `habilitado_vaat` | BOOLEAN | TRUE se o ente esta habilitado a receber VAAT. |
| `motivos` | STRING | Motivo da (in)habilitacao ao VAAT. |
| `ctrl_fonte_url` | STRING | URL do Painel FUNDEB (Power BI) de origem. |
| `ctrl_tabela_bi` | STRING | Tabela do modelo Power BI de origem. |
| `dt_extracao_lake` | TIMESTAMP | Timestamp UTC da extracao do painel. |

## trusted · fundeb_painel_indicadores_siope

File `trusted__fundeb_painel_indicadores_siope.parquet` · 626,256 rows · 10 columns

FUNDEB Painel FNDE — indicadores legais SIOPE (MDE, remuneracao, IEI, aplicacao VAAT etc.) por ente x ano x periodo x indicador.

**Built from:** `raw/fnde_fundeb_painel_indicadores`

**Feeds:** `semantic/obt_fnde_fundeb_indicadores_siope_municipio_ano`

| Column | Type | Description |
|---|---|---|
| `ano` | INTEGER | Ano de referencia do FUNDEB. |
| `periodo` | INTEGER | Periodo/bimestre do indicador. |
| `codigo_municipio` | STRING | Codigo IBGE do municipio, 7 digitos. FK -> semantic/obt_ibge_municipio.codigo_municipio. |
| `ente_federado` | STRING | Nome do ente federado (municipio ou governo estadual). |
| `sigla_uf` | STRING | Sigla da UF (ex.: SP, MG). |
| `nome_indicador` | STRING | Indicador legal SIOPE (MDE 25%, remuneracao 70%, MDE 40%, IEI, aplicacao VAAT em educacao infantil/capital, % destinacao ao Fundeb etc.). |
| `valor_indicador` | NUMERIC | Valor apurado do indicador. |
| `ctrl_fonte_url` | STRING | URL do Painel FUNDEB (Power BI) de origem. |
| `ctrl_tabela_bi` | STRING | Tabela do modelo Power BI de origem. |
| `dt_extracao_lake` | TIMESTAMP | Timestamp UTC da extracao do painel. |
