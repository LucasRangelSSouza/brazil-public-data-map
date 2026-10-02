# SIOPE education finance: Analytics

Dataset: [lucasrangelss/siope-analytics](https://www.kaggle.com/datasets/lucasrangelss/siope-analytics) · snapshot 2026-10-01 · 16 tables · 365,591,796 rows

**Source:** Fundo Nacional de Desenvolvimento da Educação (FNDE), [https://www.fnde.gov.br/siope/](https://www.fnde.gov.br/siope/)

Education revenue, expenditure and indicators reported by municipalities and states, from the SIOPE open-data API (Olinda), the FNDE SIOPE exports, and the budget execution report (RREO) PDFs parsed into tables.

**Grain and keys:** Municipality (or state) by year and reporting period. Indicator rows repeat by `num_periodo`, so analyses keep the latest period per municipality and year. Municipality joins to IBGE through `codigo_municipio`.

**Layers.** `raw` is the source snapshot as delivered. `trusted` is typed, deduplicated and named consistently. `semantic` joins and reshapes trusted tables for analysis. Every table is a Parquet file named `<layer>__<table>.parquet` at the root of the dataset.

The full interactive map (lineage, joins, search) is at [https://rangeltech.net/datamap/](https://rangeltech.net/datamap/). Column descriptions come from the source lake's catalogue and are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns | Described | Upstream |
|---|---|---:|---:|---:|---|
| semantic | [`obt_api_olinda_siope_comparativo_municipio_par_anos`](#semantic-obt-api-olinda-siope-comparativo-municipio-par-anos) | 1,984,229 | 159 | 159 | `obt_api_olinda_siope_indicadores_municipio_ano` |
| semantic | [`obt_api_olinda_siope_comparativo_uf_par_anos`](#semantic-obt-api-olinda-siope-comparativo-uf-par-anos) | 9,073 | 158 | 158 | `obt_api_olinda_siope_indicadores_uf_ano` |
| semantic | [`obt_api_olinda_siope_indicadores_municipio_ano`](#semantic-obt-api-olinda-siope-indicadores-municipio-ano) | 105,073 | 51 | 51 | `obt_fnde_fundeb_municipio_ano`, `obt_fnde_salario_educacao_distribuido_municipio_mes`, `obt_fnde_salario_educacao_previsto_municipio_ano`, `obt_ibge_municipio` … |
| semantic | [`obt_api_olinda_siope_indicadores_municipio_bimestre`](#semantic-obt-api-olinda-siope-indicadores-municipio-bimestre) | 316,538 | 25 | 25 | `obt_api_olinda_siope_indicadores_municipio_ano`, `obt_rreo_siope_municipio_bimestre`, `api_olinda_siope_indicadores`, `api_olinda_siope_receita` |
| semantic | [`obt_api_olinda_siope_indicadores_uf_ano`](#semantic-obt-api-olinda-siope-indicadores-uf-ano) | 491 | 50 | 50 | `obt_fnde_fundeb_municipio_ano`, `obt_fnde_salario_educacao_distribuido_municipio_mes`, `obt_fnde_salario_educacao_previsto_municipio_ano`, `obt_ibge_uf` … |
| semantic | [`obt_api_olinda_siope_indicadores_uf_bimestre`](#semantic-obt-api-olinda-siope-indicadores-uf-bimestre) | 1,433 | 21 | 21 | `obt_ibge_uf`, `api_olinda_siope_indicadores`, `api_olinda_siope_receita` |
| semantic | [`obt_fnde_siope_dados_gerais_municipio_ano`](#semantic-obt-fnde-siope-dados-gerais-municipio-ano) | 166,293 | 29 | 29 | `obt_ibge_municipio`, `fnde_siope_dados_gerais` |
| semantic | [`obt_fnde_siope_despesa_educacao_municipio_ano`](#semantic-obt-fnde-siope-despesa-educacao-municipio-ano) | 135,140,891 | 18 | 18 | `obt_ibge_municipio`, `fnde_siope_despesa_total_educacao` |
| semantic | [`obt_fnde_siope_despesa_funcao_municipio_ano`](#semantic-obt-fnde-siope-despesa-funcao-municipio-ano) | 1,191,974 | 13 | 13 | `obt_ibge_municipio`, `fnde_siope_despesas_funcao_educacao` |
| semantic | [`obt_fnde_siope_indicador_municipio_ano`](#semantic-obt-fnde-siope-indicador-municipio-ano) | 6,411,059 | 12 | 12 | `obt_ibge_municipio`, `fnde_siope_indicadores` |
| semantic | [`obt_fnde_siope_info_complementar_municipio_ano`](#semantic-obt-fnde-siope-info-complementar-municipio-ano) | 8,322,693 | 11 | 11 | `obt_ibge_municipio`, `fnde_siope_informacoes_complementares` |
| semantic | [`obt_fnde_siope_receita_municipio_ano`](#semantic-obt-fnde-siope-receita-municipio-ano) | 14,236,762 | 14 | 14 | `obt_ibge_municipio`, `fnde_siope_receita_total` |
| semantic | [`obt_rreo_siope_municipio_ano`](#semantic-obt-rreo-siope-municipio-ano) | 42,649,158 | 16 | 16 | `obt_ibge_municipio`, `rreo_siope_municipio` |
| semantic | [`obt_rreo_siope_municipio_bimestre`](#semantic-obt-rreo-siope-municipio-bimestre) | 154,132,717 | 17 | 17 | `obt_ibge_municipio`, `rreo_siope_municipio` |
| semantic | [`obt_rreo_siope_uf_ano`](#semantic-obt-rreo-siope-uf-ano) | 197,542 | 16 | 16 | `obt_ibge_uf`, `rreo_siope_uf` |
| semantic | [`obt_rreo_siope_uf_bimestre`](#semantic-obt-rreo-siope-uf-bimestre) | 725,870 | 17 | 17 | `obt_ibge_uf`, `rreo_siope_uf` |

## semantic · obt_api_olinda_siope_comparativo_municipio_par_anos

File `semantic__obt_api_olinda_siope_comparativo_municipio_par_anos.parquet` · 1,984,229 rows · 159 columns

SIOPE - comparativo de indicadores financeiros da educacao por MUNICIPIO x PAR DE ANOS. Grao: 1 linha por municipio x ano_vigente x ano_base, com cada indicador em duas versoes (_vigente e _base) e as variacoes derivadas. Existe para comparar dois anos quaisquer no dashboard e no GUI do Metabase sem escrever SQL. ATENCAO AO GRAO: agregar sem filtrar ano_vigente E ano_base soma o mesmo municipio uma vez por par de anos; para qualquer leitura por ano use a serie obt_api_olinda_siope_indicadores_municipio_ano. Variacoes em R$ sao NOMINAIS (nao deflacionadas) e a serie tem quebras de regra em 2021 (FUNDEB, EC 108/2020) e 2024 (criterio de rateio do Salario-Educacao). O RREO nao publica variacao entre anos: a conferencia documental e por lado, cada ano contra o seu proprio RREO.

**Built from:** `semantic/obt_api_olinda_siope_indicadores_municipio_ano`

| Column | Type | Description |
|---|---|---|
| `cod_ibge` | STRING | Codigo IBGE do municipio (7 digitos). |
| `cod_ibge_int` | INTEGER | Codigo IBGE (7 digitos) como inteiro — chave de join. |
| `cod_muni_siope` | INTEGER | Codigo do municipio no SIOPE/Olinda (6 digitos). |
| `nome_municipio` | STRING | Nome do municipio. |
| `sigla_uf` | STRING | Sigla da UF. |
| `ano_vigente` | INTEGER | Ano selecionado como principal na analise. |
| `ano_base` | INTEGER | Ano selecionado como referencia de comparacao. |
| `num_periodo_referencia_vigente` | INTEGER | [ano vigente] Bimestre de referencia da linha: ultimo bimestre em que o municipio declarou os indicadores de MDE (6 = fechamento anual; menor se o municipio nao fechou o ano). TODOS os valores e o link do PDF sao deste mesmo bimestre. |
| `num_periodo_referencia_base` | INTEGER | [ano base] Bimestre de referencia da linha: ultimo bimestre em que o municipio declarou os indicadores de MDE (6 = fechamento anual; menor se o municipio nao fechou o ano). TODOS os valores e o link do PDF sao deste mesmo bimestre. |
| `num_periodo_referencia_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `num_periodo_referencia_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao, entao pares de anos distantes embutem IPCA. NULA quando os dois anos sao o mesmo. |
| `ind1_fundeb_recebido_vigente` | NUMERIC | [ano vigente] FUNDEB recebido no ano conforme declaracao do proprio municipio no SIOPE, reconciliado com o RREO/PDF: ate 2020 usa o layout historico do codigo 11; de 2021 em diante usa o codigo 6 somando principal, rendimento de aplicacao e ressarcimento quando os componentes fecham com a linha oficial. Para anos sem RREO parseado, preserva a cobertura da Olinda. Leia junto das flags de defasagem/incompletude. |
| `ind1_fundeb_recebido_base` | NUMERIC | [ano base] FUNDEB recebido no ano conforme declaracao do proprio municipio no SIOPE, reconciliado com o RREO/PDF: ate 2020 usa o layout historico do codigo 11; de 2021 em diante usa o codigo 6 somando principal, rendimento de aplicacao e ressarcimento quando os componentes fecham com a linha oficial. Para anos sem RREO parseado, preserva a cobertura da Olinda. Leia junto das flags de defasagem/incompletude. |
| `ind1_fundeb_recebido_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind1_fundeb_recebido_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao, entao pares de anos distantes embutem IPCA. NULA quando os dois anos sao o mesmo. |
| `ind1_fundeb_previsao_atualizada_vigente` | NUMERIC | [ano vigente] Previsao atualizada do FUNDEB do municipio, preferindo o valor publicado no RREO/PDF no mesmo periodo de referencia e mantendo a Olinda como cobertura quando nao houver RREO parseado. |
| `ind1_fundeb_previsao_atualizada_base` | NUMERIC | [ano base] Previsao atualizada do FUNDEB do municipio, preferindo o valor publicado no RREO/PDF no mesmo periodo de referencia e mantendo a Olinda como cobertura quando nao houver RREO parseado. |
| `ind1_fundeb_previsao_atualizada_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind1_fundeb_previsao_atualizada_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao, entao pares de anos distantes embutem IPCA. NULA quando os dois anos sao o mesmo. |
| `ind1_fundeb_previsao_federal_vigente` | NUMERIC | [ano vigente] Previsao federal anual do FUNDEB para o ente, publicada pelo FNDE como Total das receitas previstas no arquivo Receita total do Fundeb por ente federado. Grao anual; nao deve ser repartida por bimestre. |
| `ind1_fundeb_previsao_federal_base` | NUMERIC | [ano base] Previsao federal anual do FUNDEB para o ente, publicada pelo FNDE como Total das receitas previstas no arquivo Receita total do Fundeb por ente federado. Grao anual; nao deve ser repartida por bimestre. |
| `ind1_fundeb_previsao_federal_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind1_fundeb_previsao_federal_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao, entao pares de anos distantes embutem IPCA. NULA quando os dois anos sao o mesmo. |
| `num_periodo_receita_vigente` | INTEGER | [ano vigente] Bimestre de onde vieram ind1_fundeb_recebido e ind1_fundeb_previsao_atualizada. IDEALMENTE igual a num_periodo_referencia. Quando e MENOR, o valor do FUNDEB e o acumulado ate um bimestre anterior e SUBESTIMA o ano — leia junto com flag_ind1_receita_defasada. |
| `num_periodo_receita_base` | INTEGER | [ano base] Bimestre de onde vieram ind1_fundeb_recebido e ind1_fundeb_previsao_atualizada. IDEALMENTE igual a num_periodo_referencia. Quando e MENOR, o valor do FUNDEB e o acumulado ate um bimestre anterior e SUBESTIMA o ano — leia junto com flag_ind1_receita_defasada. |
| `num_periodo_receita_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `num_periodo_receita_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao, entao pares de anos distantes embutem IPCA. NULA quando os dois anos sao o mesmo. |
| `ind1_ressarcimento_fundeb_rreo_vigente` | NUMERIC | [ano vigente] Ressarcimento de recursos do FUNDEB quando publicado no RREO/PDF do mesmo bimestre de referencia; fica NULL/0 quando nao houver valor publicado. |
| `ind1_ressarcimento_fundeb_rreo_base` | NUMERIC | [ano base] Ressarcimento de recursos do FUNDEB quando publicado no RREO/PDF do mesmo bimestre de referencia; fica NULL/0 quando nao houver valor publicado. |
| `ind1_ressarcimento_fundeb_rreo_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind1_ressarcimento_fundeb_rreo_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao, entao pares de anos distantes embutem IPCA. NULA quando os dois anos sao o mesmo. |
| `flag_ind1_tem_ressarcimento_vigente` | BOOLEAN | [ano vigente] TRUE quando o RREO/PDF do bimestre de referencia traz ressarcimento de recursos do FUNDEB maior que zero. |
| `flag_ind1_tem_ressarcimento_base` | BOOLEAN | [ano base] TRUE quando o RREO/PDF do bimestre de referencia traz ressarcimento de recursos do FUNDEB maior que zero. |
| `flag_ind1_receita_defasada_vigente` | BOOLEAN | [ano vigente] TRUE quando num_periodo_receita < num_periodo_referencia, ou seja o IND1 esta acumulado ate um bimestre ANTERIOR ao dos demais indicadores da linha. Nesse caso o FUNDEB recebido/previsto subestima o exercicio e NAO deve ser comparado com o total de outro ano. Caso real: Campinas 2024 tem receita ate o 5o bimestre e referencia no 6o, e o recebido fica 18% abaixo do RREO. A causa e cobertura da fonte/backfill, nao calculo; conforme os bimestres faltantes entram, a flag se apaga sozinha. Em 2017+ isso atinge ~38% dos pares municipio x ano. |
| `flag_ind1_receita_defasada_base` | BOOLEAN | [ano base] TRUE quando num_periodo_receita < num_periodo_referencia, ou seja o IND1 esta acumulado ate um bimestre ANTERIOR ao dos demais indicadores da linha. Nesse caso o FUNDEB recebido/previsto subestima o exercicio e NAO deve ser comparado com o total de outro ano. Caso real: Campinas 2024 tem receita ate o 5o bimestre e referencia no 6o, e o recebido fica 18% abaixo do RREO. A causa e cobertura da fonte/backfill, nao calculo; conforme os bimestres faltantes entram, a flag se apaga sozinha. Em 2017+ isso atinge ~38% dos pares municipio x ano. |
| `flag_ind1_receita_incompleta_vigente` | BOOLEAN | [ano vigente] TRUE quando o bimestre usado para a receita EXISTE mas veio sem a conta principal do FUNDEB (transferencia do fundo), tendo apenas a complementacao da Uniao. TAMBEM e TRUE quando o bimestre usado tem MENOS contas distintas de FUNDEB do que outro bimestre do mesmo exercicio — o acumulado do RREO nunca perde componente, entao isso denuncia ingestao parcial. Os dois padroes existem: Curitiba 2025 veio SO com a complementacao (R$ 2,09 mi contra R$ 1,03 bi no RREO) e Teresina/PI 2023 veio so com a principal, perdendo a complementacao que o 2o bimestre tinha (R$ 428,9 mi contra R$ 570,4 mi). Diferente de flag_ind1_receita_defasada, que e o bimestre inteiro faltando; esta aqui e mais perigosa porque o bimestre parece correto. Ambas somem sozinhas conforme o backfill da receita fecha. |
| `flag_ind1_receita_incompleta_base` | BOOLEAN | [ano base] TRUE quando o bimestre usado para a receita EXISTE mas veio sem a conta principal do FUNDEB (transferencia do fundo), tendo apenas a complementacao da Uniao. TAMBEM e TRUE quando o bimestre usado tem MENOS contas distintas de FUNDEB do que outro bimestre do mesmo exercicio — o acumulado do RREO nunca perde componente, entao isso denuncia ingestao parcial. Os dois padroes existem: Curitiba 2025 veio SO com a complementacao (R$ 2,09 mi contra R$ 1,03 bi no RREO) e Teresina/PI 2023 veio so com a principal, perdendo a complementacao que o 2o bimestre tinha (R$ 428,9 mi contra R$ 570,4 mi). Diferente de flag_ind1_receita_defasada, que e o bimestre inteiro faltando; esta aqui e mais perigosa porque o bimestre parece correto. Ambas somem sozinhas conforme o backfill da receita fecha. |
| `ind1_fundeb_recebido_rotulo_vigente` | STRING | [ano vigente] ind1_fundeb_recebido formatado em R$ pt-BR, com asterisco no fim quando flag_ind1_receita_defasada e TRUE (valor acumulado ate um bimestre anterior ao de referencia, portanto subestimado). Existe para os cartoes de numero do dashboard, que nao conseguem marcar a condicao de outro jeito. |
| `ind1_fundeb_recebido_rotulo_base` | STRING | [ano base] ind1_fundeb_recebido formatado em R$ pt-BR, com asterisco no fim quando flag_ind1_receita_defasada e TRUE (valor acumulado ate um bimestre anterior ao de referencia, portanto subestimado). Existe para os cartoes de numero do dashboard, que nao conseguem marcar a condicao de outro jeito. |
| `ind1_fundeb_previsao_atualizada_rotulo_vigente` | STRING | [ano vigente] Mesmo tratamento do ind1_fundeb_recebido_rotulo, para a previsao orcamentaria atualizada. |
| `ind1_fundeb_previsao_atualizada_rotulo_base` | STRING | [ano base] Mesmo tratamento do ind1_fundeb_recebido_rotulo, para a previsao orcamentaria atualizada. |
| `ind1_fundeb_previsao_federal_rotulo_vigente` | STRING | [ano vigente] ind1_fundeb_previsao_federal formatado em R$ pt-BR para os cartoes do dashboard. |
| `ind1_fundeb_previsao_federal_rotulo_base` | STRING | [ano base] ind1_fundeb_previsao_federal formatado em R$ pt-BR para os cartoes do dashboard. |
| `ind1_pct_aumento_fundeb_municipio_vigente` | FLOAT | [ano vigente] IND1 visao MUNICIPIO: (previsao atualizada do ano - FUNDEB recebido no ano anterior) / recebido anterior x 100. |
| `ind1_pct_aumento_fundeb_municipio_base` | FLOAT | [ano base] IND1 visao MUNICIPIO: (previsao atualizada do ano - FUNDEB recebido no ano anterior) / recebido anterior x 100. |
| `ind1_pct_aumento_fundeb_municipio_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em pontos percentuais). NULA quando os dois anos sao o mesmo. |
| `ind1_pct_variacao_recebido_vs_previsao_federal_vigente` | FLOAT | [ano vigente] Percentual de variacao do FUNDEB recebido/distribuido em relacao a previsao federal do FNDE no mesmo ano: (recebido - previsao federal) / previsao federal x 100. |
| `ind1_pct_variacao_recebido_vs_previsao_federal_base` | FLOAT | [ano base] Percentual de variacao do FUNDEB recebido/distribuido em relacao a previsao federal do FNDE no mesmo ano: (recebido - previsao federal) / previsao federal x 100. |
| `ind1_pct_variacao_recebido_vs_previsao_federal_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em pontos percentuais). NULA quando os dois anos sao o mesmo. |
| `ind1_valor_variacao_recebido_vs_previsao_federal_vigente` | NUMERIC | [ano vigente] Diferenca nominal em R$ entre FUNDEB recebido/distribuido e previsao federal do FNDE no mesmo ano: recebido - previsao federal. |
| `ind1_valor_variacao_recebido_vs_previsao_federal_base` | NUMERIC | [ano base] Diferenca nominal em R$ entre FUNDEB recebido/distribuido e previsao federal do FNDE no mesmo ano: recebido - previsao federal. |
| `ind1_valor_variacao_recebido_vs_previsao_federal_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind1_valor_variacao_recebido_vs_previsao_federal_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao, entao pares de anos distantes embutem IPCA. NULA quando os dois anos sao o mesmo. |
| `ind1_pct_variacao_recebido_vs_previsao_municipal_vigente` | FLOAT | [ano vigente] Percentual de variacao do FUNDEB recebido/distribuido em relacao a previsao municipal atualizada no mesmo ano: (recebido - previsao municipal) / previsao municipal x 100. |
| `ind1_pct_variacao_recebido_vs_previsao_municipal_base` | FLOAT | [ano base] Percentual de variacao do FUNDEB recebido/distribuido em relacao a previsao municipal atualizada no mesmo ano: (recebido - previsao municipal) / previsao municipal x 100. |
| `ind1_pct_variacao_recebido_vs_previsao_municipal_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em pontos percentuais). NULA quando os dois anos sao o mesmo. |
| `ind1_valor_variacao_recebido_vs_previsao_municipal_vigente` | NUMERIC | [ano vigente] Diferenca nominal em R$ entre FUNDEB recebido/distribuido e previsao municipal atualizada no mesmo ano: recebido - previsao municipal. |
| `ind1_valor_variacao_recebido_vs_previsao_municipal_base` | NUMERIC | [ano base] Diferenca nominal em R$ entre FUNDEB recebido/distribuido e previsao municipal atualizada no mesmo ano: recebido - previsao municipal. |
| `ind1_valor_variacao_recebido_vs_previsao_municipal_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind1_valor_variacao_recebido_vs_previsao_municipal_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao, entao pares de anos distantes embutem IPCA. NULA quando os dois anos sao o mesmo. |
| `ind2_pct_fundeb_nao_aplicado_vigente` | FLOAT | [ano vigente] % das receitas do FUNDEB nao aplicadas no exercicio (max 10%). Indicador nativo Olinda COD_INDI 27 = linha 18 col (r) do RREO. |
| `ind2_pct_fundeb_nao_aplicado_base` | FLOAT | [ano base] % das receitas do FUNDEB nao aplicadas no exercicio (max 10%). Indicador nativo Olinda COD_INDI 27 = linha 18 col (r) do RREO. |
| `ind2_pct_fundeb_nao_aplicado_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em pontos percentuais). NULA quando os dois anos sao o mesmo. |
| `ind2_valor_fundeb_nao_aplicado_vigente` | NUMERIC | [ano vigente] Valor R$ dos recursos do FUNDEB nao utilizados no exercicio. Indicador nativo Olinda COD_INDI 91 = linha 18 col (o) do RREO. SO EXISTE DE 2021 EM DIANTE (e parcial em 2021, ~1/3 dos municipios): ate 2020 a Olinda publica apenas o percentual. Para os anos sem esse dado use ind2_valor_fundeb_nao_aplicado_estimado_piso, que e ESTIMATIVA, nao medicao. |
| `ind2_valor_fundeb_nao_aplicado_base` | NUMERIC | [ano base] Valor R$ dos recursos do FUNDEB nao utilizados no exercicio. Indicador nativo Olinda COD_INDI 91 = linha 18 col (o) do RREO. SO EXISTE DE 2021 EM DIANTE (e parcial em 2021, ~1/3 dos municipios): ate 2020 a Olinda publica apenas o percentual. Para os anos sem esse dado use ind2_valor_fundeb_nao_aplicado_estimado_piso, que e ESTIMATIVA, nao medicao. |
| `ind2_valor_fundeb_nao_aplicado_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind2_valor_fundeb_nao_aplicado_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao, entao pares de anos distantes embutem IPCA. NULA quando os dois anos sao o mesmo. |
| `ind2_valor_fundeb_nao_aplicado_estimado_piso_vigente` | NUMERIC | [ano vigente] ESTIMATIVA (nao e dado oficial): ind2_pct_fundeb_nao_aplicado x ind1_fundeb_recebido. Serve para dar ordem de grandeza aos anos anteriores a 2021, em que a Olinda nao publica o valor. E um PISO, nao o valor: conferida contra o COD_INDI 91 nos exercicios fechados de 2021-2025 (11.574 casos), bate dentro de +-2% em ~40% dos municipios, SUBESTIMA ~59% (mediana da razao oficial/estimado sobe de 1,04 em 2022 para 1,24 em 2025, p90 chega a 5,3) e superestima apenas 0,5%. A causa: o denominador do percentual nao e a receita FUNDEB do ano — inclui recurso de exercicios anteriores ainda parado. Somar o saldo do ano anterior piora (acerto cai de 40% para 12%), entao nao ha formula que reconstrua o valor. NUNCA use como se fosse o valor declarado. |
| `ind2_valor_fundeb_nao_aplicado_estimado_piso_base` | NUMERIC | [ano base] ESTIMATIVA (nao e dado oficial): ind2_pct_fundeb_nao_aplicado x ind1_fundeb_recebido. Serve para dar ordem de grandeza aos anos anteriores a 2021, em que a Olinda nao publica o valor. E um PISO, nao o valor: conferida contra o COD_INDI 91 nos exercicios fechados de 2021-2025 (11.574 casos), bate dentro de +-2% em ~40% dos municipios, SUBESTIMA ~59% (mediana da razao oficial/estimado sobe de 1,04 em 2022 para 1,24 em 2025, p90 chega a 5,3) e superestima apenas 0,5%. A causa: o denominador do percentual nao e a receita FUNDEB do ano — inclui recurso de exercicios anteriores ainda parado. Somar o saldo do ano anterior piora (acerto cai de 40% para 12%), entao nao ha formula que reconstrua o valor. NUNCA use como se fosse o valor declarado. |
| `ind2_valor_fundeb_nao_aplicado_estimado_piso_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind2_valor_fundeb_nao_aplicado_estimado_piso_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao, entao pares de anos distantes embutem IPCA. NULA quando os dois anos sao o mesmo. |
| `ind2_valor_fundeb_nao_aplicado_exibicao_vigente` | NUMERIC | [ano vigente] Valor do FUNDEB nao aplicado para EXIBICAO: o oficial (COD_INDI 91) quando existe, senao a estimativa de piso. Use junto com ind2_valor_fundeb_nao_aplicado_e_estimado para saber qual dos dois esta na linha. |
| `ind2_valor_fundeb_nao_aplicado_exibicao_base` | NUMERIC | [ano base] Valor do FUNDEB nao aplicado para EXIBICAO: o oficial (COD_INDI 91) quando existe, senao a estimativa de piso. Use junto com ind2_valor_fundeb_nao_aplicado_e_estimado para saber qual dos dois esta na linha. |
| `ind2_valor_fundeb_nao_aplicado_exibicao_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind2_valor_fundeb_nao_aplicado_exibicao_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao, entao pares de anos distantes embutem IPCA. NULA quando os dois anos sao o mesmo. |
| `ind2_valor_fundeb_nao_aplicado_e_estimado_vigente` | BOOLEAN | [ano vigente] TRUE quando ind2_valor_fundeb_nao_aplicado_exibicao veio da estimativa de piso (ano sem dado oficial), FALSE quando veio do valor declarado no SIOPE. |
| `ind2_valor_fundeb_nao_aplicado_e_estimado_base` | BOOLEAN | [ano base] TRUE quando ind2_valor_fundeb_nao_aplicado_exibicao veio da estimativa de piso (ano sem dado oficial), FALSE quando veio do valor declarado no SIOPE. |
| `ind2_valor_fundeb_nao_aplicado_rotulo_vigente` | STRING | [ano vigente] ind2_valor_fundeb_nao_aplicado_exibicao ja formatado em R$ pt-BR, com asterisco no fim quando e estimativa. Existe para os cartoes de numero do dashboard, que nao conseguem marcar a estimativa de outro jeito. |
| `ind2_valor_fundeb_nao_aplicado_rotulo_base` | STRING | [ano base] ind2_valor_fundeb_nao_aplicado_exibicao ja formatado em R$ pt-BR, com asterisco no fim quando e estimativa. Existe para os cartoes de numero do dashboard, que nao conseguem marcar a estimativa de outro jeito. |
| `ind3_salario_educacao_vigente` | NUMERIC | [ano vigente] Valor de Salario-Educacao do municipio no ano. Usa o distribuido quando o exercicio esta fechado; enquanto o ano corre, usa o previsto, porque o documento do ano corrente e publicado parcial. Fontes: obt_fnde_salario_educacao_previsto_municipio_ano e obt_fnde_salario_educacao_distribuido_municipio_mes. |
| `ind3_salario_educacao_base` | NUMERIC | [ano base] Valor de Salario-Educacao do municipio no ano. Usa o distribuido quando o exercicio esta fechado; enquanto o ano corre, usa o previsto, porque o documento do ano corrente e publicado parcial. Fontes: obt_fnde_salario_educacao_previsto_municipio_ano e obt_fnde_salario_educacao_distribuido_municipio_mes. |
| `ind3_salario_educacao_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind3_salario_educacao_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao, entao pares de anos distantes embutem IPCA. NULA quando os dois anos sao o mesmo. |
| `ind3_pct_aumento_salario_educacao_vigente` | FLOAT | [ano vigente] Variacao % do valor analitico de Salario-Educacao vs ano anterior (mesmo municipio) x 100. |
| `ind3_pct_aumento_salario_educacao_base` | FLOAT | [ano base] Variacao % do valor analitico de Salario-Educacao vs ano anterior (mesmo municipio) x 100. |
| `ind3_pct_aumento_salario_educacao_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em pontos percentuais). NULA quando os dois anos sao o mesmo. |
| `ind3_fonte_valor_analitico_vigente` | STRING | [ano vigente] Fonte usada no IND3 do ano: DISTRIBUIDO (exercicio fechado), PREVISTO (exercicio em curso) ou DISTRIBUIDO_PARCIAL (em curso e sem previsto publicado). |
| `ind3_fonte_valor_analitico_base` | STRING | [ano base] Fonte usada no IND3 do ano: DISTRIBUIDO (exercicio fechado), PREVISTO (exercicio em curso) ou DISTRIBUIDO_PARCIAL (em curso e sem previsto publicado). |
| `ind3_salario_educacao_previsto_vigente` | NUMERIC | [ano vigente] Valor previsto oficial de Salario-Educacao no municipio/ano, mantido para auditoria. |
| `ind3_salario_educacao_previsto_base` | NUMERIC | [ano base] Valor previsto oficial de Salario-Educacao no municipio/ano, mantido para auditoria. |
| `ind3_salario_educacao_previsto_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind3_salario_educacao_previsto_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao, entao pares de anos distantes embutem IPCA. NULA quando os dois anos sao o mesmo. |
| `ind3_salario_educacao_distribuido_vigente` | NUMERIC | [ano vigente] Valor efetivamente distribuido de Salario-Educacao no municipio/ano (consolidado do exercicio ate a ultima publicacao), mantido para auditoria. |
| `ind3_salario_educacao_distribuido_base` | NUMERIC | [ano base] Valor efetivamente distribuido de Salario-Educacao no municipio/ano (consolidado do exercicio ate a ultima publicacao), mantido para auditoria. |
| `ind3_salario_educacao_distribuido_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind3_salario_educacao_distribuido_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao, entao pares de anos distantes embutem IPCA. NULA quando os dois anos sao o mesmo. |
| `ind3_exercicio_fechado_vigente` | BOOLEAN | [ano vigente] TRUE quando o distribuido do ano cobre o exercicio inteiro. FALSE no ano corrente, cujo documento e publicado parcial — nesse caso o IND3 usa o previsto. |
| `ind3_exercicio_fechado_base` | BOOLEAN | [ano base] TRUE quando o distribuido do ano cobre o exercicio inteiro. FALSE no ano corrente, cujo documento e publicado parcial — nesse caso o IND3 usa o previsto. |
| `ind4_pct_aplicado_mde_fechado_vigente` | FLOAT | [ano vigente] % aplicado em MDE sobre a receita de impostos no FECHAMENTO do exercicio. Preenchido quando num_periodo_referencia = 6 OU quando o ano e <= 2016 — ate 2016 o SIOPE publicava uma unica declaracao por exercicio (NUM_PERI = 1), que era o fechamento da epoca e nao uma declaracao abandonada no 1o bimestre. |
| `ind4_pct_aplicado_mde_fechado_base` | FLOAT | [ano base] % aplicado em MDE sobre a receita de impostos no FECHAMENTO do exercicio. Preenchido quando num_periodo_referencia = 6 OU quando o ano e <= 2016 — ate 2016 o SIOPE publicava uma unica declaracao por exercicio (NUM_PERI = 1), que era o fechamento da epoca e nao uma declaracao abandonada no 1o bimestre. |
| `ind4_pct_aplicado_mde_fechado_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em pontos percentuais). NULA quando os dois anos sao o mesmo. |
| `ind5_pct_aplicado_mde_parcial_vigente` | FLOAT | [ano vigente] % aplicado em MDE sobre a receita de impostos em declaracao PARCIAL: o municipio parou de declarar antes do 6o bimestre. Preenchido quando num_periodo_referencia < 6 E o ano e >= 2017 — antes de 2017 nao existe declaracao parcial na fonte, so a declaracao anual unica, que vai para o IND4. |
| `ind5_pct_aplicado_mde_parcial_base` | FLOAT | [ano base] % aplicado em MDE sobre a receita de impostos em declaracao PARCIAL: o municipio parou de declarar antes do 6o bimestre. Preenchido quando num_periodo_referencia < 6 E o ano e >= 2017 — antes de 2017 nao existe declaracao parcial na fonte, so a declaracao anual unica, que vai para o IND4. |
| `ind5_pct_aplicado_mde_parcial_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em pontos percentuais). NULA quando os dois anos sao o mesmo. |
| `ind4_valor_exigido_mde_fechado_vigente` | NUMERIC | [ano vigente] Valor exigido de aplicacao em MDE no fechamento do exercicio (mesma regra de num_periodo_referencia do ind4_pct_aplicado_mde_fechado). So existe de 2020 em diante: antes disso a Olinda publica apenas o percentual. |
| `ind4_valor_exigido_mde_fechado_base` | NUMERIC | [ano base] Valor exigido de aplicacao em MDE no fechamento do exercicio (mesma regra de num_periodo_referencia do ind4_pct_aplicado_mde_fechado). So existe de 2020 em diante: antes disso a Olinda publica apenas o percentual. |
| `ind4_valor_exigido_mde_fechado_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind4_valor_exigido_mde_fechado_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao, entao pares de anos distantes embutem IPCA. NULA quando os dois anos sao o mesmo. |
| `ind5_valor_exigido_mde_parcial_vigente` | NUMERIC | [ano vigente] Valor exigido de aplicacao em MDE em declaracao parcial (mesma regra do ind5_pct_aplicado_mde_parcial). ACUMULADO ate o bimestre declarado, nao o exigido do ano inteiro. |
| `ind5_valor_exigido_mde_parcial_base` | NUMERIC | [ano base] Valor exigido de aplicacao em MDE em declaracao parcial (mesma regra do ind5_pct_aplicado_mde_parcial). ACUMULADO ate o bimestre declarado, nao o exigido do ano inteiro. |
| `ind5_valor_exigido_mde_parcial_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind5_valor_exigido_mde_parcial_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao, entao pares de anos distantes embutem IPCA. NULA quando os dois anos sao o mesmo. |
| `ind4_valor_aplicado_mde_fechado_vigente` | NUMERIC | [ano vigente] Valor aplicado em MDE no fechamento do exercicio (mesma regra de num_periodo_referencia do ind4_pct_aplicado_mde_fechado). So existe de 2020 em diante. |
| `ind4_valor_aplicado_mde_fechado_base` | NUMERIC | [ano base] Valor aplicado em MDE no fechamento do exercicio (mesma regra de num_periodo_referencia do ind4_pct_aplicado_mde_fechado). So existe de 2020 em diante. |
| `ind4_valor_aplicado_mde_fechado_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind4_valor_aplicado_mde_fechado_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao, entao pares de anos distantes embutem IPCA. NULA quando os dois anos sao o mesmo. |
| `ind5_valor_aplicado_mde_parcial_vigente` | NUMERIC | [ano vigente] Valor aplicado em MDE em declaracao parcial (mesma regra do ind5_pct_aplicado_mde_parcial). ACUMULADO ate o bimestre declarado. |
| `ind5_valor_aplicado_mde_parcial_base` | NUMERIC | [ano base] Valor aplicado em MDE em declaracao parcial (mesma regra do ind5_pct_aplicado_mde_parcial). ACUMULADO ate o bimestre declarado. |
| `ind5_valor_aplicado_mde_parcial_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind5_valor_aplicado_mde_parcial_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao, entao pares de anos distantes embutem IPCA. NULA quando os dois anos sao o mesmo. |
| `ind4_falta_para_valor_exigido_vigente` | NUMERIC | [ano vigente] Quanto ainda FALTA aplicar em R$ para alcancar o minimo constitucional de MDE no fechamento anual: GREATEST(0, exigido - aplicado). ZERO quando o municipio ja atingiu ou passou o minimo — nao fica negativo, porque excedente nao e divida. NULO quando a Olinda nao publica os valores em R$ (ate 2019): nulo significa NAO SEI, e e diferente de zero, que significa NAO FALTA NADA. |
| `ind4_falta_para_valor_exigido_base` | NUMERIC | [ano base] Quanto ainda FALTA aplicar em R$ para alcancar o minimo constitucional de MDE no fechamento anual: GREATEST(0, exigido - aplicado). ZERO quando o municipio ja atingiu ou passou o minimo — nao fica negativo, porque excedente nao e divida. NULO quando a Olinda nao publica os valores em R$ (ate 2019): nulo significa NAO SEI, e e diferente de zero, que significa NAO FALTA NADA. |
| `ind4_falta_para_valor_exigido_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind4_falta_para_valor_exigido_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao, entao pares de anos distantes embutem IPCA. NULA quando os dois anos sao o mesmo. |
| `ind5_falta_para_valor_exigido_vigente` | NUMERIC | [ano vigente] Mesmo calculo do ind4_falta_para_valor_exigido, para os anos de declaracao parcial. ATENCAO: em ano parcial o exigido tambem e parcial (acumulado ate o bimestre declarado), entao a falta e a do periodo declarado, nao a do ano inteiro. |
| `ind5_falta_para_valor_exigido_base` | NUMERIC | [ano base] Mesmo calculo do ind4_falta_para_valor_exigido, para os anos de declaracao parcial. ATENCAO: em ano parcial o exigido tambem e parcial (acumulado ate o bimestre declarado), entao a falta e a do periodo declarado, nao a do ano inteiro. |
| `ind5_falta_para_valor_exigido_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind5_falta_para_valor_exigido_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao, entao pares de anos distantes embutem IPCA. NULA quando os dois anos sao o mesmo. |
| `ind4_diferenca_aplicado_vs_exigido_vigente` | NUMERIC | [ano vigente] Diferenca em R$ entre o aplicado em MDE e o minimo constitucional exigido no fechamento anual: aplicado - exigido. NEGATIVO quando o municipio ficou abaixo do minimo (o modulo e quanto falta) e POSITIVO quando passou (quanto ultrapassou). Diferente de ind4_falta_para_valor_exigido, que trava em zero e so enxerga a falta: aqui o excedente aparece. NULO nas mesmas condicoes: sem valores em R$ na fonte (ate 2019) ou exigido <= 0, que e declaracao vazia. |
| `ind4_diferenca_aplicado_vs_exigido_base` | NUMERIC | [ano base] Diferenca em R$ entre o aplicado em MDE e o minimo constitucional exigido no fechamento anual: aplicado - exigido. NEGATIVO quando o municipio ficou abaixo do minimo (o modulo e quanto falta) e POSITIVO quando passou (quanto ultrapassou). Diferente de ind4_falta_para_valor_exigido, que trava em zero e so enxerga a falta: aqui o excedente aparece. NULO nas mesmas condicoes: sem valores em R$ na fonte (ate 2019) ou exigido <= 0, que e declaracao vazia. |
| `ind4_diferenca_aplicado_vs_exigido_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind4_diferenca_aplicado_vs_exigido_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao, entao pares de anos distantes embutem IPCA. NULA quando os dois anos sao o mesmo. |
| `ind5_diferenca_aplicado_vs_exigido_vigente` | NUMERIC | [ano vigente] Mesmo calculo do ind4_diferenca_aplicado_vs_exigido, para os anos de declaracao parcial. ATENCAO: em ano parcial o exigido tambem e parcial (acumulado ate o bimestre declarado), entao a diferenca e a do periodo declarado, nao a do ano inteiro. |
| `ind5_diferenca_aplicado_vs_exigido_base` | NUMERIC | [ano base] Mesmo calculo do ind4_diferenca_aplicado_vs_exigido, para os anos de declaracao parcial. ATENCAO: em ano parcial o exigido tambem e parcial (acumulado ate o bimestre declarado), entao a diferenca e a do periodo declarado, nao a do ano inteiro. |
| `ind5_diferenca_aplicado_vs_exigido_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind5_diferenca_aplicado_vs_exigido_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao, entao pares de anos distantes embutem IPCA. NULA quando os dois anos sao o mesmo. |
| `pct_uso_folha_fundeb_vigente` | FLOAT | [ano vigente] % de aplicacao do FUNDEF/FUNDEB na remuneracao dos profissionais da educacao (Olinda COD_INDI 67), serie continua desde 2008. A definicao legal muda em 2021 (magisterio/60% -> profissionais da educacao/70%), por isso a meta do ano vem em meta_pct_uso_folha_fundeb. |
| `pct_uso_folha_fundeb_base` | FLOAT | [ano base] % de aplicacao do FUNDEF/FUNDEB na remuneracao dos profissionais da educacao (Olinda COD_INDI 67), serie continua desde 2008. A definicao legal muda em 2021 (magisterio/60% -> profissionais da educacao/70%), por isso a meta do ano vem em meta_pct_uso_folha_fundeb. |
| `pct_uso_folha_fundeb_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em pontos percentuais). NULA quando os dois anos sao o mesmo. |
| `meta_pct_uso_folha_fundeb_vigente` | FLOAT | [ano vigente] Meta percentual aplicavel ao indicador de uso de folha no ano: 60 (2008-2020) ou 70 (2021+). |
| `meta_pct_uso_folha_fundeb_base` | FLOAT | [ano base] Meta percentual aplicavel ao indicador de uso de folha no ano: 60 (2008-2020) ou 70 (2021+). |
| `meta_pct_uso_folha_fundeb_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em pontos percentuais). NULA quando os dois anos sao o mesmo. |
| `regra_pct_uso_folha_fundeb_vigente` | STRING | [ano vigente] Rotulo da regra historica do indicador de uso de folha no ano: MAGISTERIO_60 (2008-2020) ou EDUCACAO_70 (2021+). |
| `regra_pct_uso_folha_fundeb_base` | STRING | [ano base] Rotulo da regra historica do indicador de uso de folha no ano: MAGISTERIO_60 (2008-2020) ou EDUCACAO_70 (2021+). |
| `superavit_deficit_exercicio_vigente` | NUMERIC | [ano vigente] Superavit(+)/Deficit(-) do ente no exercicio (R$). Olinda COD_INDI 69. |
| `superavit_deficit_exercicio_base` | NUMERIC | [ano base] Superavit(+)/Deficit(-) do ente no exercicio (R$). Olinda COD_INDI 69. |
| `superavit_deficit_exercicio_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `superavit_deficit_exercicio_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao, entao pares de anos distantes embutem IPCA. NULA quando os dois anos sao o mesmo. |
| `saldo_financeiro_fundeb_vigente` | NUMERIC | [ano vigente] Disponibilidade financeira de FUNDEB ate o bimestre de referencia (R$). Olinda COD_INDI 70. E ESTOQUE, nao fluxo acumulado: sobe e desce ao longo do ano conforme entra repasse e sai pagamento. Conferido no PDF do RREO: corresponde a linha '(=) DISPONIBILIDADE FINANCEIRA ATE O BIMESTRE', NAO a linha seguinte '(=) SALDO FINANCEIRO CONCILIADO (Saldo Bancario)'. As duas coincidem quando o ente nao lanca ajustes de conciliacao — foi o caso em 7 de 10 conferencias — mas divergem quando ha ajuste: Acrelandia 2021 tem 1.876.610,68 de disponibilidade contra 2.070.420,70 de conciliado, e esta coluna traz o primeiro. Campinas 2021: 43.056.036,73 contra 36.657.924,15. |
| `saldo_financeiro_fundeb_base` | NUMERIC | [ano base] Disponibilidade financeira de FUNDEB ate o bimestre de referencia (R$). Olinda COD_INDI 70. E ESTOQUE, nao fluxo acumulado: sobe e desce ao longo do ano conforme entra repasse e sai pagamento. Conferido no PDF do RREO: corresponde a linha '(=) DISPONIBILIDADE FINANCEIRA ATE O BIMESTRE', NAO a linha seguinte '(=) SALDO FINANCEIRO CONCILIADO (Saldo Bancario)'. As duas coincidem quando o ente nao lanca ajustes de conciliacao — foi o caso em 7 de 10 conferencias — mas divergem quando ha ajuste: Acrelandia 2021 tem 1.876.610,68 de disponibilidade contra 2.070.420,70 de conciliado, e esta coluna traz o primeiro. Campinas 2021: 43.056.036,73 contra 36.657.924,15. |
| `saldo_financeiro_fundeb_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `saldo_financeiro_fundeb_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao, entao pares de anos distantes embutem IPCA. NULA quando os dois anos sao o mesmo. |
| `ind1_variacao_recebido_rotulo` | STRING | Variacao percentual do FUNDEB recebido entre os dois anos, formatada, com ASTERISCO quando qualquer um dos lados tem flag_ind1_receita_defasada. Nesse caso os dois anos estao truncados em bimestres diferentes e a variacao NAO representa crescimento real: Campinas 2025 x 2024 mostra -17,15% enquanto o RREO registra crescimento de 509,6 mi para 529,4 mi. NULA quando os anos sao iguais ou falta um lado. |
| `ind1_diferenca_recebido_base_vs_previsao_federal` | NUMERIC | Diferenca em R$ entre o FUNDEB recebido no ano BASE e a previsao federal do FNDE para o ano VIGENTE: recebido(base) - previsao federal(vigente). Cruza os dois anos de proposito, para medir o que ja entrou contra o que se espera. NEGATIVA quando a previsao do ano vigente supera o recebido do ano base. NOMINAL: nao desconta inflacao. |
| `ind1_diferenca_recebido_base_vs_previsao_municipal` | NUMERIC | Diferenca em R$ entre o FUNDEB recebido no ano BASE e a previsao orcamentaria atualizada do MUNICIPIO para o ano VIGENTE: recebido(base) - previsao municipal(vigente). Cruza os dois anos de proposito. NEGATIVA quando a previsao do ano vigente supera o recebido do ano base. NOMINAL: nao desconta inflacao. |
| `ind1_pct_diferenca_recebido_base_vs_previsao_federal` | FLOAT | Mesma comparacao de ind1_diferenca_recebido_base_vs_previsao_federal, em percentual sobre a previsao federal do ano VIGENTE: (recebido do ano base - previsao federal do ano vigente) / previsao federal do ano vigente x 100. NEGATIVA quando a previsao deste ano supera o que entrou no ano base. |
| `ind1_pct_diferenca_recebido_base_vs_previsao_municipal` | FLOAT | Mesma comparacao de ind1_diferenca_recebido_base_vs_previsao_municipal, em percentual sobre a previsao municipal do ano VIGENTE: (recebido do ano base - previsao municipal do ano vigente) / previsao municipal do ano vigente x 100. NEGATIVA quando a previsao deste ano supera o que entrou no ano base. |
| `flag_mesmo_ano` | BOOLEAN | TRUE quando ano_vigente e ano_base sao o mesmo ano; nesse caso todas as variacoes ficam nulas. |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC da construcao da tabela. |

## semantic · obt_api_olinda_siope_comparativo_uf_par_anos

File `semantic__obt_api_olinda_siope_comparativo_uf_par_anos.parquet` · 9,073 rows · 158 columns

SIOPE - comparativo de indicadores financeiros da educacao por UNIDADE FEDERATIVA x PAR DE ANOS. Grao: 1 linha por UF x ano_vigente x ano_base, com cada indicador em duas versoes (_vigente e _base) e as variacoes derivadas. Alimenta os cartoes de numero da aba de UF do dashboard 113. ATENCAO AO GRAO: agregar sem filtrar ano_vigente E ano_base soma a mesma UF uma vez por par de anos; para leitura por ano use obt_api_olinda_siope_indicadores_uf_ano. Variacoes em R$ sao NOMINAIS.

**Built from:** `semantic/obt_api_olinda_siope_indicadores_uf_ano`

| Column | Type | Description |
|---|---|---|
| `codigo_uf` | INTEGER | Codigo IBGE da UF (2 digitos) — chave de join e do RREO estadual. |
| `sigla_uf` | STRING | Sigla da UF. |
| `nome_uf` | STRING | Nome da UF segundo o IBGE. |
| `nome_regiao` | STRING | Nome da regiao segundo o IBGE. |
| `ano_vigente` | INTEGER | Ano selecionado como principal na analise. |
| `ano_base` | INTEGER | Ano selecionado como referencia de comparacao. |
| `num_periodo_referencia_vigente` | INTEGER | [ano vigente] Ultimo bimestre em que o governo estadual declarou os indicadores de MDE (COD_INDI 40/96/97). TODOS os valores da linha saem deste mesmo bimestre, para o snapshot ser consistente. 6 = exercicio fechado; menor = o estado nao fechou as contas. Ate 2016 o SIOPE publica uma declaracao anual unica marcada como bimestre 1, que E o fechamento daquela era. |
| `num_periodo_referencia_base` | INTEGER | [ano base] Ultimo bimestre em que o governo estadual declarou os indicadores de MDE (COD_INDI 40/96/97). TODOS os valores da linha saem deste mesmo bimestre, para o snapshot ser consistente. 6 = exercicio fechado; menor = o estado nao fechou as contas. Ate 2016 o SIOPE publica uma declaracao anual unica marcada como bimestre 1, que E o fechamento daquela era. |
| `num_periodo_referencia_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `num_periodo_referencia_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao. |
| `ind1_fundeb_recebido_vigente` | NUMERIC | [ano vigente] FUNDEB efetivamente recebido pelo governo estadual, acumulado ate o bimestre de referencia. RECONCILIADO com o RREO: o valor e a LINHA CHEIA do relatorio (Receitas Recebidas do FUNDEB), que e exatamente o que esta no PDF publicado pelo estado. A Olinda entra como fallback quando o RREO daquele bimestre nao existe. A linha cheia inclui o rendimento de aplicacao financeira e o ressarcimento, que a Olinda NAO publica como FUNDEB — por isso a Olinda pura fica ~0,5% abaixo do PDF. Conferido ao centavo em Pernambuco 2024, 6o bimestre: total 4.014.584.777,28 = Olinda 3.980.435.276,46 + rendimento 34.059.369,66 + ressarcimento 90.131,16. |
| `ind1_fundeb_recebido_base` | NUMERIC | [ano base] FUNDEB efetivamente recebido pelo governo estadual, acumulado ate o bimestre de referencia. RECONCILIADO com o RREO: o valor e a LINHA CHEIA do relatorio (Receitas Recebidas do FUNDEB), que e exatamente o que esta no PDF publicado pelo estado. A Olinda entra como fallback quando o RREO daquele bimestre nao existe. A linha cheia inclui o rendimento de aplicacao financeira e o ressarcimento, que a Olinda NAO publica como FUNDEB — por isso a Olinda pura fica ~0,5% abaixo do PDF. Conferido ao centavo em Pernambuco 2024, 6o bimestre: total 4.014.584.777,28 = Olinda 3.980.435.276,46 + rendimento 34.059.369,66 + ressarcimento 90.131,16. |
| `ind1_fundeb_recebido_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind1_fundeb_recebido_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao. |
| `ind1_fundeb_recebido_fonte_vigente` | STRING | [ano vigente] De onde saiu ind1_fundeb_recebido: RREO quando veio da linha cheia do relatorio (bate 100% com o PDF) ou OLINDA quando o RREO daquele bimestre nao existe e o valor caiu no somatorio da receita declarada, que fica ligeiramente abaixo. |
| `ind1_fundeb_recebido_fonte_base` | STRING | [ano base] De onde saiu ind1_fundeb_recebido: RREO quando veio da linha cheia do relatorio (bate 100% com o PDF) ou OLINDA quando o RREO daquele bimestre nao existe e o valor caiu no somatorio da receita declarada, que fica ligeiramente abaixo. |
| `ind1_rendimento_aplicacao_rreo_vigente` | NUMERIC | [ano vigente] Rendimento de aplicacao financeira dos recursos do FUNDEB, lido do RREO. Ja esta DENTRO de ind1_fundeb_recebido, porque a linha cheia do relatorio o soma. Existe em coluna propria porque a Olinda classifica esse valor como receita patrimonial e nao como FUNDEB: e a maior parte da diferenca entre as duas fontes. |
| `ind1_rendimento_aplicacao_rreo_base` | NUMERIC | [ano base] Rendimento de aplicacao financeira dos recursos do FUNDEB, lido do RREO. Ja esta DENTRO de ind1_fundeb_recebido, porque a linha cheia do relatorio o soma. Existe em coluna propria porque a Olinda classifica esse valor como receita patrimonial e nao como FUNDEB: e a maior parte da diferenca entre as duas fontes. |
| `ind1_rendimento_aplicacao_rreo_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind1_rendimento_aplicacao_rreo_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao. |
| `ind1_ressarcimento_fundeb_rreo_vigente` | NUMERIC | [ano vigente] Ressarcimento de recursos do FUNDEB (devolucao do ente ao fundo), lido do RREO. Tambem ja esta dentro de ind1_fundeb_recebido. A Olinda nao expoe essa parcela. |
| `ind1_ressarcimento_fundeb_rreo_base` | NUMERIC | [ano base] Ressarcimento de recursos do FUNDEB (devolucao do ente ao fundo), lido do RREO. Tambem ja esta dentro de ind1_fundeb_recebido. A Olinda nao expoe essa parcela. |
| `ind1_ressarcimento_fundeb_rreo_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind1_ressarcimento_fundeb_rreo_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao. |
| `flag_ind1_tem_ressarcimento_vigente` | BOOLEAN | [ano vigente] TRUE quando o RREO do bimestre de referencia traz ressarcimento de recursos do FUNDEB maior que zero. |
| `flag_ind1_tem_ressarcimento_base` | BOOLEAN | [ano base] TRUE quando o RREO do bimestre de referencia traz ressarcimento de recursos do FUNDEB maior que zero. |
| `ind1_fundeb_previsao_atualizada_vigente` | NUMERIC | [ano vigente] Previsao orcamentaria ATUALIZADA do FUNDEB declarada pelo proprio governo estadual, no mesmo bimestre de referencia. E a expectativa do ente, nao a do FNDE. |
| `ind1_fundeb_previsao_atualizada_base` | NUMERIC | [ano base] Previsao orcamentaria ATUALIZADA do FUNDEB declarada pelo proprio governo estadual, no mesmo bimestre de referencia. E a expectativa do ente, nao a do FNDE. |
| `ind1_fundeb_previsao_atualizada_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind1_fundeb_previsao_atualizada_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao. |
| `ind1_fundeb_previsao_federal_vigente` | NUMERIC | [ano vigente] Previsao oficial do FNDE de repasse de FUNDEB ao governo estadual no ano (painel do FUNDEB, esfera Estadual). So existe de 2021 em diante. Diferente da previsao do ente: esta e a estimativa de quem paga. |
| `ind1_fundeb_previsao_federal_base` | NUMERIC | [ano base] Previsao oficial do FNDE de repasse de FUNDEB ao governo estadual no ano (painel do FUNDEB, esfera Estadual). So existe de 2021 em diante. Diferente da previsao do ente: esta e a estimativa de quem paga. |
| `ind1_fundeb_previsao_federal_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind1_fundeb_previsao_federal_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao. |
| `num_periodo_receita_vigente` | INTEGER | [ano vigente] De qual bimestre veio a receita usada no IND1. Quando menor que num_periodo_referencia, o FUNDEB esta acumulado ate um bimestre ANTERIOR ao dos demais indicadores da linha e subestima o exercicio — e o que flag_ind1_receita_defasada marca. |
| `num_periodo_receita_base` | INTEGER | [ano base] De qual bimestre veio a receita usada no IND1. Quando menor que num_periodo_referencia, o FUNDEB esta acumulado ate um bimestre ANTERIOR ao dos demais indicadores da linha e subestima o exercicio — e o que flag_ind1_receita_defasada marca. |
| `num_periodo_receita_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `num_periodo_receita_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao. |
| `flag_ind1_receita_defasada_vigente` | BOOLEAN | [ano vigente] TRUE quando num_periodo_receita < num_periodo_referencia. Nesse caso o FUNDEB recebido/previsto NAO deve ser comparado com o total de outro ano. Causa e cobertura da fonte, nao calculo. |
| `flag_ind1_receita_defasada_base` | BOOLEAN | [ano base] TRUE quando num_periodo_receita < num_periodo_referencia. Nesse caso o FUNDEB recebido/previsto NAO deve ser comparado com o total de outro ano. Causa e cobertura da fonte, nao calculo. |
| `flag_ind1_receita_incompleta_vigente` | BOOLEAN | [ano vigente] TRUE quando o bimestre usado para a receita existe mas veio sem a conta PRINCIPAL do FUNDEB (so a complementacao da Uniao), OU com MENOS contas distintas que outro bimestre do mesmo exercicio. O acumulado do RREO nunca perde componente, entao isso denuncia ingestao parcial. |
| `flag_ind1_receita_incompleta_base` | BOOLEAN | [ano base] TRUE quando o bimestre usado para a receita existe mas veio sem a conta PRINCIPAL do FUNDEB (so a complementacao da Uniao), OU com MENOS contas distintas que outro bimestre do mesmo exercicio. O acumulado do RREO nunca perde componente, entao isso denuncia ingestao parcial. |
| `ind1_fundeb_recebido_rotulo_vigente` | STRING | [ano vigente] ind1_fundeb_recebido formatado em R$ pt-BR, com asterisco quando ha flag de qualidade. Existe para os cartoes de numero do dashboard, que nao conseguem marcar a condicao de outro jeito. |
| `ind1_fundeb_recebido_rotulo_base` | STRING | [ano base] ind1_fundeb_recebido formatado em R$ pt-BR, com asterisco quando ha flag de qualidade. Existe para os cartoes de numero do dashboard, que nao conseguem marcar a condicao de outro jeito. |
| `ind1_fundeb_previsao_atualizada_rotulo_vigente` | STRING | [ano vigente] Mesmo tratamento do rotulo do recebido, para a previsao do proprio estado. |
| `ind1_fundeb_previsao_atualizada_rotulo_base` | STRING | [ano base] Mesmo tratamento do rotulo do recebido, para a previsao do proprio estado. |
| `ind1_fundeb_previsao_federal_rotulo_vigente` | STRING | [ano vigente] ind1_fundeb_previsao_federal formatado em R$ pt-BR para os cartoes do dashboard. |
| `ind1_fundeb_previsao_federal_rotulo_base` | STRING | [ano base] ind1_fundeb_previsao_federal formatado em R$ pt-BR para os cartoes do dashboard. |
| `ind1_pct_variacao_recebido_vs_previsao_federal_vigente` | FLOAT | [ano vigente] (recebido - previsao federal) / previsao federal x 100, no mesmo ano. |
| `ind1_pct_variacao_recebido_vs_previsao_federal_base` | FLOAT | [ano base] (recebido - previsao federal) / previsao federal x 100, no mesmo ano. |
| `ind1_pct_variacao_recebido_vs_previsao_federal_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em pontos percentuais). NULA quando os dois anos sao o mesmo. |
| `ind1_valor_variacao_recebido_vs_previsao_federal_vigente` | NUMERIC | [ano vigente] recebido - previsao federal, no mesmo ano, em R$ nominais. |
| `ind1_valor_variacao_recebido_vs_previsao_federal_base` | NUMERIC | [ano base] recebido - previsao federal, no mesmo ano, em R$ nominais. |
| `ind1_valor_variacao_recebido_vs_previsao_federal_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind1_valor_variacao_recebido_vs_previsao_federal_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao. |
| `ind1_pct_variacao_recebido_vs_previsao_estadual_vigente` | FLOAT | [ano vigente] (recebido - previsao do proprio estado) / previsao estadual x 100, no mesmo ano. Equivale ao ..._vs_previsao_municipal do grao municipal. |
| `ind1_pct_variacao_recebido_vs_previsao_estadual_base` | FLOAT | [ano base] (recebido - previsao do proprio estado) / previsao estadual x 100, no mesmo ano. Equivale ao ..._vs_previsao_municipal do grao municipal. |
| `ind1_pct_variacao_recebido_vs_previsao_estadual_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em pontos percentuais). NULA quando os dois anos sao o mesmo. |
| `ind1_valor_variacao_recebido_vs_previsao_estadual_vigente` | NUMERIC | [ano vigente] recebido - previsao do proprio estado, no mesmo ano, em R$ nominais. |
| `ind1_valor_variacao_recebido_vs_previsao_estadual_base` | NUMERIC | [ano base] recebido - previsao do proprio estado, no mesmo ano, em R$ nominais. |
| `ind1_valor_variacao_recebido_vs_previsao_estadual_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind1_valor_variacao_recebido_vs_previsao_estadual_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao. |
| `ind2_pct_fundeb_nao_aplicado_vigente` | FLOAT | [ano vigente] % das receitas do FUNDEB nao aplicadas no exercicio (max 10%). Olinda estadual COD_INDI 44. O limite so vincula no 6o bimestre. |
| `ind2_pct_fundeb_nao_aplicado_base` | FLOAT | [ano base] % das receitas do FUNDEB nao aplicadas no exercicio (max 10%). Olinda estadual COD_INDI 44. O limite so vincula no 6o bimestre. |
| `ind2_pct_fundeb_nao_aplicado_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em pontos percentuais). NULA quando os dois anos sao o mesmo. |
| `ind2_valor_fundeb_nao_aplicado_vigente` | NUMERIC | [ano vigente] Valor R$ dos recursos do FUNDEB nao utilizados. Olinda estadual COD_INDI 94. So existe de 2021 em diante. |
| `ind2_valor_fundeb_nao_aplicado_base` | NUMERIC | [ano base] Valor R$ dos recursos do FUNDEB nao utilizados. Olinda estadual COD_INDI 94. So existe de 2021 em diante. |
| `ind2_valor_fundeb_nao_aplicado_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind2_valor_fundeb_nao_aplicado_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao. |
| `ind2_valor_fundeb_nao_aplicado_estimado_piso_vigente` | NUMERIC | [ano vigente] ESTIMATIVA de piso (nao e dado oficial): ind2_pct x ind1_fundeb_recebido. Existe para os anos em que a fonte publica so o percentual. |
| `ind2_valor_fundeb_nao_aplicado_estimado_piso_base` | NUMERIC | [ano base] ESTIMATIVA de piso (nao e dado oficial): ind2_pct x ind1_fundeb_recebido. Existe para os anos em que a fonte publica so o percentual. |
| `ind2_valor_fundeb_nao_aplicado_estimado_piso_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind2_valor_fundeb_nao_aplicado_estimado_piso_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao. |
| `ind2_valor_fundeb_nao_aplicado_exibicao_vigente` | NUMERIC | [ano vigente] Valor do FUNDEB nao aplicado para EXIBICAO: o oficial quando existe, senao a estimativa de piso. |
| `ind2_valor_fundeb_nao_aplicado_exibicao_base` | NUMERIC | [ano base] Valor do FUNDEB nao aplicado para EXIBICAO: o oficial quando existe, senao a estimativa de piso. |
| `ind2_valor_fundeb_nao_aplicado_exibicao_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind2_valor_fundeb_nao_aplicado_exibicao_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao. |
| `ind2_valor_fundeb_nao_aplicado_e_estimado_vigente` | BOOLEAN | [ano vigente] TRUE quando ind2_valor_fundeb_nao_aplicado_exibicao veio da estimativa, nao do valor oficial. |
| `ind2_valor_fundeb_nao_aplicado_e_estimado_base` | BOOLEAN | [ano base] TRUE quando ind2_valor_fundeb_nao_aplicado_exibicao veio da estimativa, nao do valor oficial. |
| `ind2_valor_fundeb_nao_aplicado_rotulo_vigente` | STRING | [ano vigente] Valor de exibicao formatado em R$ pt-BR, com asterisco quando e estimativa. |
| `ind2_valor_fundeb_nao_aplicado_rotulo_base` | STRING | [ano base] Valor de exibicao formatado em R$ pt-BR, com asterisco quando e estimativa. |
| `ind3_salario_educacao_vigente` | NUMERIC | [ano vigente] Salario-Educacao do governo estadual no ano: distribuido quando o exercicio fechou, previsto enquanto o ano corre. A serie do distribuido e CONTINUA desde 2007: ate 2019 ela sai do documento de cota estadual/municipal, que traz uma linha por UF e esfera, e de 2020 em diante do documento por ente federado. |
| `ind3_salario_educacao_base` | NUMERIC | [ano base] Salario-Educacao do governo estadual no ano: distribuido quando o exercicio fechou, previsto enquanto o ano corre. A serie do distribuido e CONTINUA desde 2007: ate 2019 ela sai do documento de cota estadual/municipal, que traz uma linha por UF e esfera, e de 2020 em diante do documento por ente federado. |
| `ind3_salario_educacao_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind3_salario_educacao_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao. |
| `ind3_salario_educacao_previsto_vigente` | NUMERIC | [ano vigente] Estimativa das quotas de Salario-Educacao publicada pelo FNDE no comeco do ano. Serie por UF desde 2010. |
| `ind3_salario_educacao_previsto_base` | NUMERIC | [ano base] Estimativa das quotas de Salario-Educacao publicada pelo FNDE no comeco do ano. Serie por UF desde 2010. |
| `ind3_salario_educacao_previsto_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind3_salario_educacao_previsto_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao. |
| `ind3_salario_educacao_distribuido_vigente` | NUMERIC | [ano vigente] Salario-Educacao efetivamente repassado ao governo estadual no ano, somando as 12 competencias. Diferente do grao municipal, que so tem distribuido de 2020 em diante: no estadual a serie e continua, porque ate 2019 o FNDE publicava justamente a abertura por UF e esfera. |
| `ind3_salario_educacao_distribuido_base` | NUMERIC | [ano base] Salario-Educacao efetivamente repassado ao governo estadual no ano, somando as 12 competencias. Diferente do grao municipal, que so tem distribuido de 2020 em diante: no estadual a serie e continua, porque ate 2019 o FNDE publicava justamente a abertura por UF e esfera. |
| `ind3_salario_educacao_distribuido_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind3_salario_educacao_distribuido_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao. |
| `ind3_fonte_valor_analitico_vigente` | STRING | [ano vigente] De onde saiu ind3_salario_educacao: DISTRIBUIDO, PREVISTO ou DISTRIBUIDO_PARCIAL. |
| `ind3_fonte_valor_analitico_base` | STRING | [ano base] De onde saiu ind3_salario_educacao: DISTRIBUIDO, PREVISTO ou DISTRIBUIDO_PARCIAL. |
| `ind3_exercicio_fechado_vigente` | BOOLEAN | [ano vigente] TRUE quando o distribuido do ano cobre o exercicio inteiro. |
| `ind3_exercicio_fechado_base` | BOOLEAN | [ano base] TRUE quando o distribuido do ano cobre o exercicio inteiro. |
| `ind4_pct_aplicado_mde_fechado_vigente` | FLOAT | [ano vigente] % aplicado em MDE no FECHAMENTO do exercicio (num_periodo_referencia = 6, ou ano <= 2016). Minimo constitucional de 25%. Olinda estadual COD_INDI 40. |
| `ind4_pct_aplicado_mde_fechado_base` | FLOAT | [ano base] % aplicado em MDE no FECHAMENTO do exercicio (num_periodo_referencia = 6, ou ano <= 2016). Minimo constitucional de 25%. Olinda estadual COD_INDI 40. |
| `ind4_pct_aplicado_mde_fechado_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em pontos percentuais). NULA quando os dois anos sao o mesmo. |
| `ind5_pct_aplicado_mde_parcial_vigente` | FLOAT | [ano vigente] % aplicado em MDE em declaracao PARCIAL: o estado parou de declarar antes do 6o bimestre (e o ano e >= 2017). Acumulado ate o bimestre declarado, entao um valor abaixo de 25% aqui significa ano incompleto, nao descumprimento. |
| `ind5_pct_aplicado_mde_parcial_base` | FLOAT | [ano base] % aplicado em MDE em declaracao PARCIAL: o estado parou de declarar antes do 6o bimestre (e o ano e >= 2017). Acumulado ate o bimestre declarado, entao um valor abaixo de 25% aqui significa ano incompleto, nao descumprimento. |
| `ind5_pct_aplicado_mde_parcial_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em pontos percentuais). NULA quando os dois anos sao o mesmo. |
| `ind4_valor_exigido_mde_fechado_vigente` | NUMERIC | [ano vigente] Valor exigido de aplicacao em MDE no fechamento. Olinda estadual COD_INDI 96. So existe de 2020 em diante. |
| `ind4_valor_exigido_mde_fechado_base` | NUMERIC | [ano base] Valor exigido de aplicacao em MDE no fechamento. Olinda estadual COD_INDI 96. So existe de 2020 em diante. |
| `ind4_valor_exigido_mde_fechado_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind4_valor_exigido_mde_fechado_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao. |
| `ind5_valor_exigido_mde_parcial_vigente` | NUMERIC | [ano vigente] Valor exigido de aplicacao em MDE em declaracao parcial, ACUMULADO ate o bimestre declarado. |
| `ind5_valor_exigido_mde_parcial_base` | NUMERIC | [ano base] Valor exigido de aplicacao em MDE em declaracao parcial, ACUMULADO ate o bimestre declarado. |
| `ind5_valor_exigido_mde_parcial_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind5_valor_exigido_mde_parcial_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao. |
| `ind4_valor_aplicado_mde_fechado_vigente` | NUMERIC | [ano vigente] Valor aplicado em MDE no fechamento. Olinda estadual COD_INDI 97. So existe de 2020 em diante. |
| `ind4_valor_aplicado_mde_fechado_base` | NUMERIC | [ano base] Valor aplicado em MDE no fechamento. Olinda estadual COD_INDI 97. So existe de 2020 em diante. |
| `ind4_valor_aplicado_mde_fechado_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind4_valor_aplicado_mde_fechado_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao. |
| `ind5_valor_aplicado_mde_parcial_vigente` | NUMERIC | [ano vigente] Valor aplicado em MDE em declaracao parcial, ACUMULADO ate o bimestre declarado. |
| `ind5_valor_aplicado_mde_parcial_base` | NUMERIC | [ano base] Valor aplicado em MDE em declaracao parcial, ACUMULADO ate o bimestre declarado. |
| `ind5_valor_aplicado_mde_parcial_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind5_valor_aplicado_mde_parcial_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao. |
| `ind4_falta_para_valor_exigido_vigente` | NUMERIC | [ano vigente] Quanto FALTA aplicar em R$ para alcancar o minimo no fechamento: GREATEST(0, exigido - aplicado). Trava em zero: excedente nao e divida. NULO quando a fonte nao publica os valores em R$. |
| `ind4_falta_para_valor_exigido_base` | NUMERIC | [ano base] Quanto FALTA aplicar em R$ para alcancar o minimo no fechamento: GREATEST(0, exigido - aplicado). Trava em zero: excedente nao e divida. NULO quando a fonte nao publica os valores em R$. |
| `ind4_falta_para_valor_exigido_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind4_falta_para_valor_exigido_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao. |
| `ind5_falta_para_valor_exigido_vigente` | NUMERIC | [ano vigente] Mesmo calculo, para os anos de declaracao parcial. O exigido tambem e parcial. |
| `ind5_falta_para_valor_exigido_base` | NUMERIC | [ano base] Mesmo calculo, para os anos de declaracao parcial. O exigido tambem e parcial. |
| `ind5_falta_para_valor_exigido_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind5_falta_para_valor_exigido_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao. |
| `ind4_diferenca_aplicado_vs_exigido_vigente` | NUMERIC | [ano vigente] Diferenca em R$ entre o aplicado e o exigido no fechamento: aplicado - exigido. NEGATIVA quando ficou abaixo do minimo (o modulo e quanto falta) e POSITIVA quando passou. Diferente da falta, que trava em zero. |
| `ind4_diferenca_aplicado_vs_exigido_base` | NUMERIC | [ano base] Diferenca em R$ entre o aplicado e o exigido no fechamento: aplicado - exigido. NEGATIVA quando ficou abaixo do minimo (o modulo e quanto falta) e POSITIVA quando passou. Diferente da falta, que trava em zero. |
| `ind4_diferenca_aplicado_vs_exigido_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind4_diferenca_aplicado_vs_exigido_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao. |
| `ind5_diferenca_aplicado_vs_exigido_vigente` | NUMERIC | [ano vigente] Mesmo calculo, para os anos de declaracao parcial. |
| `ind5_diferenca_aplicado_vs_exigido_base` | NUMERIC | [ano base] Mesmo calculo, para os anos de declaracao parcial. |
| `ind5_diferenca_aplicado_vs_exigido_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `ind5_diferenca_aplicado_vs_exigido_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao. |
| `pct_uso_folha_fundeb_vigente` | FLOAT | [ano vigente] % de aplicacao do FUNDEF/FUNDEB na remuneracao dos profissionais da educacao. Olinda estadual COD_INDI 42, serie continua desde 2008. |
| `pct_uso_folha_fundeb_base` | FLOAT | [ano base] % de aplicacao do FUNDEF/FUNDEB na remuneracao dos profissionais da educacao. Olinda estadual COD_INDI 42, serie continua desde 2008. |
| `pct_uso_folha_fundeb_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em pontos percentuais). NULA quando os dois anos sao o mesmo. |
| `meta_pct_uso_folha_fundeb_vigente` | FLOAT | [ano vigente] Meta percentual aplicavel no ano: 60 (2008-2020, magisterio) ou 70 (2021+, todos os profissionais da educacao, Lei 14.113/2020). |
| `meta_pct_uso_folha_fundeb_base` | FLOAT | [ano base] Meta percentual aplicavel no ano: 60 (2008-2020, magisterio) ou 70 (2021+, todos os profissionais da educacao, Lei 14.113/2020). |
| `meta_pct_uso_folha_fundeb_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em pontos percentuais). NULA quando os dois anos sao o mesmo. |
| `regra_pct_uso_folha_fundeb_vigente` | STRING | [ano vigente] Qual regra vale no ano: MAGISTERIO_60 ou EDUCACAO_70. |
| `regra_pct_uso_folha_fundeb_base` | STRING | [ano base] Qual regra vale no ano: MAGISTERIO_60 ou EDUCACAO_70. |
| `superavit_deficit_exercicio_vigente` | NUMERIC | [ano vigente] Superavit(+)/Deficit(-) do ente no exercicio (R$). Olinda estadual COD_INDI 83. E o resultado do ente inteiro, nao so da educacao. |
| `superavit_deficit_exercicio_base` | NUMERIC | [ano base] Superavit(+)/Deficit(-) do ente no exercicio (R$). Olinda estadual COD_INDI 83. E o resultado do ente inteiro, nao so da educacao. |
| `superavit_deficit_exercicio_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `superavit_deficit_exercicio_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao. |
| `saldo_financeiro_fundeb_vigente` | NUMERIC | [ano vigente] Disponibilidade financeira de FUNDEB ate o bimestre de referencia (R$). Olinda estadual COD_INDI 84. E ESTOQUE (o que esta em caixa), nao fluxo acumulado. |
| `saldo_financeiro_fundeb_base` | NUMERIC | [ano base] Disponibilidade financeira de FUNDEB ate o bimestre de referencia (R$). Olinda estadual COD_INDI 84. E ESTOQUE (o que esta em caixa), nao fluxo acumulado. |
| `saldo_financeiro_fundeb_variacao_abs` | FLOAT | Diferenca entre o ano vigente e o ano base (em R$ nominais, sem deflacionar). NULA quando os dois anos sao o mesmo. |
| `saldo_financeiro_fundeb_variacao_pct` | FLOAT | Variacao percentual do ano vigente sobre o ano base. NOMINAL: nao desconta inflacao. |
| `ind1_variacao_recebido_rotulo` | STRING | Variacao percentual do FUNDEB recebido entre os dois anos, formatada, com ASTERISCO quando qualquer um dos lados tem flag de qualidade na receita. NULA quando os anos sao iguais ou falta um lado. |
| `ind1_diferenca_recebido_base_vs_previsao_federal` | NUMERIC | Diferenca em R$ entre o FUNDEB recebido no ano BASE e a previsao federal para o ano VIGENTE. Cruza os dois anos de proposito, para medir o que ja entrou contra o que se espera. NEGATIVA quando a previsao do ano vigente supera o recebido do ano base. NOMINAL. |
| `ind1_pct_diferenca_recebido_base_vs_previsao_federal` | FLOAT | Mesma comparacao em percentual sobre a previsao federal do ano VIGENTE. |
| `ind1_diferenca_recebido_base_vs_previsao_estadual` | NUMERIC | Diferenca em R$ entre o FUNDEB recebido no ano BASE e a previsao estadual para o ano VIGENTE. Cruza os dois anos de proposito, para medir o que ja entrou contra o que se espera. NEGATIVA quando a previsao do ano vigente supera o recebido do ano base. NOMINAL. |
| `ind1_pct_diferenca_recebido_base_vs_previsao_estadual` | FLOAT | Mesma comparacao em percentual sobre a previsao estadual do ano VIGENTE. |
| `flag_mesmo_ano` | BOOLEAN | TRUE quando ano_vigente e ano_base sao o mesmo ano; nesse caso todas as variacoes ficam nulas. |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC da construcao da tabela. |

## semantic · obt_api_olinda_siope_indicadores_municipio_ano

File `semantic__obt_api_olinda_siope_indicadores_municipio_ano.parquet` · 105,073 rows · 51 columns

SIOPE — indicadores financeiros da educacao por MUNICIPIO x ANO (WIDE). Valores calculados no modelo SIOPE do dashboard, usando Olinda como base e complemento do RREO/PDF oficial para cobrir lacunas publicadas, sem expor coluna de origem. Salario-Educacao vem do FNDE, escolhendo distribuido em exercicio fechado e previsto no ano corrente. A serie de folha respeita a regra historica do ano e MDE e exposto separando fechamento anual (IND4) de declaracao parcial (IND5).

**Built from:** `semantic/obt_fnde_fundeb_municipio_ano`, `semantic/obt_fnde_salario_educacao_distribuido_municipio_mes`, `semantic/obt_fnde_salario_educacao_previsto_municipio_ano`, `semantic/obt_ibge_municipio`, `semantic/obt_rreo_siope_municipio_bimestre`, `trusted/api_olinda_siope_indicadores`, `trusted/api_olinda_siope_receita`

**Feeds:** `semantic/obt_api_olinda_siope_comparativo_municipio_par_anos`, `semantic/obt_api_olinda_siope_indicadores_municipio_bimestre`

| Column | Type | Description |
|---|---|---|
| `cod_ibge` | STRING | Codigo IBGE do municipio (7 digitos). |
| `cod_ibge_int` | INTEGER | Codigo IBGE (7 digitos) como inteiro — chave de join. |
| `cod_muni_siope` | INTEGER | Codigo do municipio no SIOPE/Olinda (6 digitos). |
| `nome_municipio` | STRING | Nome do municipio. |
| `sigla_uf` | STRING | Sigla da UF. |
| `ano` | INTEGER | Ano de exercicio. |
| `num_periodo_referencia` | INTEGER | Bimestre de referencia da linha: ultimo bimestre em que o municipio declarou os indicadores de MDE (6 = fechamento anual; menor se o municipio nao fechou o ano). TODOS os valores e o link do PDF sao deste mesmo bimestre. |
| `ind1_fundeb_recebido` | NUMERIC | FUNDEB recebido no ano conforme declaracao do proprio municipio no SIOPE, reconciliado com o RREO/PDF: ate 2020 usa o layout historico do codigo 11; de 2021 em diante usa o codigo 6 somando principal, rendimento de aplicacao e ressarcimento quando os componentes fecham com a linha oficial. Para anos sem RREO parseado, preserva a cobertura da Olinda. Leia junto das flags de defasagem/incompletude. |
| `ind1_fundeb_previsao_atualizada` | NUMERIC | Previsao atualizada do FUNDEB do municipio, preferindo o valor publicado no RREO/PDF no mesmo periodo de referencia e mantendo a Olinda como cobertura quando nao houver RREO parseado. |
| `ind1_fundeb_previsao_federal` | NUMERIC | Previsao federal anual do FUNDEB para o ente, publicada pelo FNDE como Total das receitas previstas no arquivo Receita total do Fundeb por ente federado. Grao anual; nao deve ser repartida por bimestre. |
| `num_periodo_receita` | INTEGER | Bimestre de onde vieram ind1_fundeb_recebido e ind1_fundeb_previsao_atualizada. IDEALMENTE igual a num_periodo_referencia. Quando e MENOR, o valor do FUNDEB e o acumulado ate um bimestre anterior e SUBESTIMA o ano — leia junto com flag_ind1_receita_defasada. |
| `ind1_ressarcimento_fundeb_rreo` | NUMERIC | Ressarcimento de recursos do FUNDEB quando publicado no RREO/PDF do mesmo bimestre de referencia; fica NULL/0 quando nao houver valor publicado. |
| `flag_ind1_tem_ressarcimento` | BOOLEAN | TRUE quando o RREO/PDF do bimestre de referencia traz ressarcimento de recursos do FUNDEB maior que zero. |
| `flag_ind1_receita_defasada` | BOOLEAN | TRUE quando num_periodo_receita < num_periodo_referencia, ou seja o IND1 esta acumulado ate um bimestre ANTERIOR ao dos demais indicadores da linha. Nesse caso o FUNDEB recebido/previsto subestima o exercicio e NAO deve ser comparado com o total de outro ano. Caso real: Campinas 2024 tem receita ate o 5o bimestre e referencia no 6o, e o recebido fica 18% abaixo do RREO. A causa e cobertura da fonte/backfill, nao calculo; conforme os bimestres faltantes entram, a flag se apaga sozinha. Em 2017+ isso atinge ~38% dos pares municipio x ano. |
| `flag_ind1_receita_incompleta` | BOOLEAN | TRUE quando o bimestre usado para a receita EXISTE mas veio sem a conta principal do FUNDEB (transferencia do fundo), tendo apenas a complementacao da Uniao. TAMBEM e TRUE quando o bimestre usado tem MENOS contas distintas de FUNDEB do que outro bimestre do mesmo exercicio — o acumulado do RREO nunca perde componente, entao isso denuncia ingestao parcial. Os dois padroes existem: Curitiba 2025 veio SO com a complementacao (R$ 2,09 mi contra R$ 1,03 bi no RREO) e Teresina/PI 2023 veio so com a principal, perdendo a complementacao que o 2o bimestre tinha (R$ 428,9 mi contra R$ 570,4 mi). Diferente de flag_ind1_receita_defasada, que e o bimestre inteiro faltando; esta aqui e mais perigosa porque o bimestre parece correto. Ambas somem sozinhas conforme o backfill da receita fecha. |
| `ind1_fundeb_recebido_rotulo` | STRING | ind1_fundeb_recebido formatado em R$ pt-BR, com asterisco no fim quando flag_ind1_receita_defasada e TRUE (valor acumulado ate um bimestre anterior ao de referencia, portanto subestimado). Existe para os cartoes de numero do dashboard, que nao conseguem marcar a condicao de outro jeito. |
| `ind1_fundeb_previsao_atualizada_rotulo` | STRING | Mesmo tratamento do ind1_fundeb_recebido_rotulo, para a previsao orcamentaria atualizada. |
| `ind1_fundeb_previsao_federal_rotulo` | STRING | ind1_fundeb_previsao_federal formatado em R$ pt-BR para os cartoes do dashboard. |
| `ind1_pct_aumento_fundeb_municipio` | FLOAT | IND1 visao MUNICIPIO: (previsao atualizada do ano - FUNDEB recebido no ano anterior) / recebido anterior x 100. |
| `ind1_pct_variacao_recebido_vs_previsao_federal` | FLOAT | Percentual de variacao do FUNDEB recebido/distribuido em relacao a previsao federal do FNDE no mesmo ano: (recebido - previsao federal) / previsao federal x 100. |
| `ind1_valor_variacao_recebido_vs_previsao_federal` | NUMERIC | Diferenca nominal em R$ entre FUNDEB recebido/distribuido e previsao federal do FNDE no mesmo ano: recebido - previsao federal. |
| `ind1_pct_variacao_recebido_vs_previsao_municipal` | FLOAT | Percentual de variacao do FUNDEB recebido/distribuido em relacao a previsao municipal atualizada no mesmo ano: (recebido - previsao municipal) / previsao municipal x 100. |
| `ind1_valor_variacao_recebido_vs_previsao_municipal` | NUMERIC | Diferenca nominal em R$ entre FUNDEB recebido/distribuido e previsao municipal atualizada no mesmo ano: recebido - previsao municipal. |
| `ind2_pct_fundeb_nao_aplicado` | FLOAT | % das receitas do FUNDEB nao aplicadas no exercicio (max 10%). Indicador nativo Olinda COD_INDI 27 = linha 18 col (r) do RREO. |
| `ind2_valor_fundeb_nao_aplicado` | NUMERIC | Valor R$ dos recursos do FUNDEB nao utilizados no exercicio. Indicador nativo Olinda COD_INDI 91 = linha 18 col (o) do RREO. SO EXISTE DE 2021 EM DIANTE (e parcial em 2021, ~1/3 dos municipios): ate 2020 a Olinda publica apenas o percentual. Para os anos sem esse dado use ind2_valor_fundeb_nao_aplicado_estimado_piso, que e ESTIMATIVA, nao medicao. |
| `ind2_valor_fundeb_nao_aplicado_estimado_piso` | NUMERIC | ESTIMATIVA (nao e dado oficial): ind2_pct_fundeb_nao_aplicado x ind1_fundeb_recebido. Serve para dar ordem de grandeza aos anos anteriores a 2021, em que a Olinda nao publica o valor. E um PISO, nao o valor: conferida contra o COD_INDI 91 nos exercicios fechados de 2021-2025 (11.574 casos), bate dentro de +-2% em ~40% dos municipios, SUBESTIMA ~59% (mediana da razao oficial/estimado sobe de 1,04 em 2022 para 1,24 em 2025, p90 chega a 5,3) e superestima apenas 0,5%. A causa: o denominador do percentual nao e a receita FUNDEB do ano — inclui recurso de exercicios anteriores ainda parado. Somar o saldo do ano anterior piora (acerto cai de 40% para 12%), entao nao ha formula que reconstrua o valor. NUNCA use como se fosse o valor declarado. |
| `ind2_valor_fundeb_nao_aplicado_exibicao` | NUMERIC | Valor do FUNDEB nao aplicado para EXIBICAO: o oficial (COD_INDI 91) quando existe, senao a estimativa de piso. Use junto com ind2_valor_fundeb_nao_aplicado_e_estimado para saber qual dos dois esta na linha. |
| `ind2_valor_fundeb_nao_aplicado_e_estimado` | BOOLEAN | TRUE quando ind2_valor_fundeb_nao_aplicado_exibicao veio da estimativa de piso (ano sem dado oficial), FALSE quando veio do valor declarado no SIOPE. |
| `ind2_valor_fundeb_nao_aplicado_rotulo` | STRING | ind2_valor_fundeb_nao_aplicado_exibicao ja formatado em R$ pt-BR, com asterisco no fim quando e estimativa. Existe para os cartoes de numero do dashboard, que nao conseguem marcar a estimativa de outro jeito. |
| `ind3_salario_educacao` | NUMERIC | Valor de Salario-Educacao do municipio no ano. Usa o distribuido quando o exercicio esta fechado; enquanto o ano corre, usa o previsto, porque o documento do ano corrente e publicado parcial. Fontes: obt_fnde_salario_educacao_previsto_municipio_ano e obt_fnde_salario_educacao_distribuido_municipio_mes. |
| `ind3_pct_aumento_salario_educacao` | FLOAT | Variacao % do valor analitico de Salario-Educacao vs ano anterior (mesmo municipio) x 100. |
| `ind3_fonte_valor_analitico` | STRING | Fonte usada no IND3 do ano: DISTRIBUIDO (exercicio fechado), PREVISTO (exercicio em curso) ou DISTRIBUIDO_PARCIAL (em curso e sem previsto publicado). |
| `ind3_salario_educacao_previsto` | NUMERIC | Valor previsto oficial de Salario-Educacao no municipio/ano, mantido para auditoria. |
| `ind3_salario_educacao_distribuido` | NUMERIC | Valor efetivamente distribuido de Salario-Educacao no municipio/ano (consolidado do exercicio ate a ultima publicacao), mantido para auditoria. |
| `ind3_exercicio_fechado` | BOOLEAN | TRUE quando o distribuido do ano cobre o exercicio inteiro. FALSE no ano corrente, cujo documento e publicado parcial — nesse caso o IND3 usa o previsto. |
| `ind4_pct_aplicado_mde_fechado` | FLOAT | % aplicado em MDE sobre a receita de impostos no FECHAMENTO do exercicio. Preenchido quando num_periodo_referencia = 6 OU quando o ano e <= 2016 — ate 2016 o SIOPE publicava uma unica declaracao por exercicio (NUM_PERI = 1), que era o fechamento da epoca e nao uma declaracao abandonada no 1o bimestre. |
| `ind5_pct_aplicado_mde_parcial` | FLOAT | % aplicado em MDE sobre a receita de impostos em declaracao PARCIAL: o municipio parou de declarar antes do 6o bimestre. Preenchido quando num_periodo_referencia < 6 E o ano e >= 2017 — antes de 2017 nao existe declaracao parcial na fonte, so a declaracao anual unica, que vai para o IND4. |
| `ind4_valor_exigido_mde_fechado` | NUMERIC | Valor exigido de aplicacao em MDE no fechamento do exercicio (mesma regra de num_periodo_referencia do ind4_pct_aplicado_mde_fechado). So existe de 2020 em diante: antes disso a Olinda publica apenas o percentual. |
| `ind5_valor_exigido_mde_parcial` | NUMERIC | Valor exigido de aplicacao em MDE em declaracao parcial (mesma regra do ind5_pct_aplicado_mde_parcial). ACUMULADO ate o bimestre declarado, nao o exigido do ano inteiro. |
| `ind4_valor_aplicado_mde_fechado` | NUMERIC | Valor aplicado em MDE no fechamento do exercicio (mesma regra de num_periodo_referencia do ind4_pct_aplicado_mde_fechado). So existe de 2020 em diante. |
| `ind5_valor_aplicado_mde_parcial` | NUMERIC | Valor aplicado em MDE em declaracao parcial (mesma regra do ind5_pct_aplicado_mde_parcial). ACUMULADO ate o bimestre declarado. |
| `ind4_falta_para_valor_exigido` | NUMERIC | Quanto ainda FALTA aplicar em R$ para alcancar o minimo constitucional de MDE no fechamento anual: GREATEST(0, exigido - aplicado). ZERO quando o municipio ja atingiu ou passou o minimo — nao fica negativo, porque excedente nao e divida. NULO quando a Olinda nao publica os valores em R$ (ate 2019): nulo significa NAO SEI, e e diferente de zero, que significa NAO FALTA NADA. |
| `ind5_falta_para_valor_exigido` | NUMERIC | Mesmo calculo do ind4_falta_para_valor_exigido, para os anos de declaracao parcial. ATENCAO: em ano parcial o exigido tambem e parcial (acumulado ate o bimestre declarado), entao a falta e a do periodo declarado, nao a do ano inteiro. |
| `ind4_diferenca_aplicado_vs_exigido` | NUMERIC | Diferenca em R$ entre o aplicado em MDE e o minimo constitucional exigido no fechamento anual: aplicado - exigido. NEGATIVO quando o municipio ficou abaixo do minimo (o modulo e quanto falta) e POSITIVO quando passou (quanto ultrapassou). Diferente de ind4_falta_para_valor_exigido, que trava em zero e so enxerga a falta: aqui o excedente aparece. NULO nas mesmas condicoes: sem valores em R$ na fonte (ate 2019) ou exigido <= 0, que e declaracao vazia. |
| `ind5_diferenca_aplicado_vs_exigido` | NUMERIC | Mesmo calculo do ind4_diferenca_aplicado_vs_exigido, para os anos de declaracao parcial. ATENCAO: em ano parcial o exigido tambem e parcial (acumulado ate o bimestre declarado), entao a diferenca e a do periodo declarado, nao a do ano inteiro. |
| `pct_uso_folha_fundeb` | FLOAT | % de aplicacao do FUNDEF/FUNDEB na remuneracao dos profissionais da educacao (Olinda COD_INDI 67), serie continua desde 2008. A definicao legal muda em 2021 (magisterio/60% -> profissionais da educacao/70%), por isso a meta do ano vem em meta_pct_uso_folha_fundeb. |
| `meta_pct_uso_folha_fundeb` | FLOAT | Meta percentual aplicavel ao indicador de uso de folha no ano: 60 (2008-2020) ou 70 (2021+). |
| `regra_pct_uso_folha_fundeb` | STRING | Rotulo da regra historica do indicador de uso de folha no ano: MAGISTERIO_60 (2008-2020) ou EDUCACAO_70 (2021+). |
| `superavit_deficit_exercicio` | NUMERIC | Superavit(+)/Deficit(-) do ente no exercicio (R$). Olinda COD_INDI 69. |
| `saldo_financeiro_fundeb` | NUMERIC | Disponibilidade financeira de FUNDEB ate o bimestre de referencia (R$). Olinda COD_INDI 70. E ESTOQUE, nao fluxo acumulado: sobe e desce ao longo do ano conforme entra repasse e sai pagamento. Conferido no PDF do RREO: corresponde a linha '(=) DISPONIBILIDADE FINANCEIRA ATE O BIMESTRE', NAO a linha seguinte '(=) SALDO FINANCEIRO CONCILIADO (Saldo Bancario)'. As duas coincidem quando o ente nao lanca ajustes de conciliacao — foi o caso em 7 de 10 conferencias — mas divergem quando ha ajuste: Acrelandia 2021 tem 1.876.610,68 de disponibilidade contra 2.070.420,70 de conciliado, e esta coluna traz o primeiro. Campinas 2021: 43.056.036,73 contra 36.657.924,15. |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC da construcao da tabela. |

## semantic · obt_api_olinda_siope_indicadores_municipio_bimestre

File `semantic__obt_api_olinda_siope_indicadores_municipio_bimestre.parquet` · 316,538 rows · 25 columns

SIOPE - IND1, IND2, MDE (indicadores 4 e 5) e IND6 no grao MUNICIPIO x ANO x BIMESTRE, para as visoes bimestrais do dashboard. SO 2017+: ate 2016 o Olinda publica um unico registro por ano (NUM_PERI=1), nao seis. OS VALORES SAO ACUMULADOS NO ANO, como o RREO publica: IND1 vem tambem desacumulado (_no_bimestre) e IND2 so acumulado, porque percentual nao se desacumula. O limite legal de 10% do IND2 so vincula no 6o bimestre. O grao canonico dos indicadores continua sendo obt_api_olinda_siope_indicadores_municipio_ano; esta tabela e recorte de leitura e NAO alimenta os cartoes de numero.

**Built from:** `semantic/obt_api_olinda_siope_indicadores_municipio_ano`, `semantic/obt_rreo_siope_municipio_bimestre`, `trusted/api_olinda_siope_indicadores`, `trusted/api_olinda_siope_receita`

| Column | Type | Description |
|---|---|---|
| `cod_ibge` | STRING | Codigo IBGE de 7 digitos do municipio. |
| `cod_ibge_int` | INTEGER | Codigo IBGE de 7 digitos como inteiro (chave de join). |
| `cod_muni_siope` | INTEGER | Codigo do municipio no SIOPE (COD_MUNI da Olinda). INT64 para casar com o tipo da tabela anual. |
| `nome_municipio` | STRING | Nome do municipio. |
| `sigla_uf` | STRING | UF. |
| `ano` | INTEGER | Exercicio. |
| `bimestre` | INTEGER | Bimestre do RREO (1 a 6). O 6o e o fechamento do exercicio. |
| `ind1_fundeb_recebido_acumulado` | NUMERIC | FUNDEB recebido ACUMULADO do inicio do ano ate este bimestre conforme declaracao do proprio municipio no SIOPE, reconciliado com o RREO/PDF: ate 2020 usa o layout historico do codigo 11; de 2021 em diante usa o codigo 6 somando principal, rendimento de aplicacao e ressarcimento quando os componentes fecham com a linha oficial. Cada bimestre repete o exercicio acumulado ate ali. |
| `ind1_fundeb_recebido_no_bimestre` | NUMERIC | FUNDEB recebido DENTRO deste bimestre, desacumulado por diferenca contra o bimestre anterior do mesmo ano (no 1o bimestre e igual ao acumulado). E a leitura comparavel entre bimestres; o acumulado sempre cresce dentro do ano e cairia de degrau na virada. |
| `ind1_fundeb_previsao_atualizada` | NUMERIC | Previsao orcamentaria atualizada do FUNDEB vigente neste bimestre, preferindo o RREO/PDF e mantendo a Olinda como cobertura quando nao houver RREO parseado. E previsao do ANO, nao do bimestre: nao acumula e costuma mudar pouco ao longo do exercicio. |
| `ind2_pct_fundeb_nao_aplicado` | FLOAT | % das receitas do FUNDEB nao aplicadas, ACUMULADO ate este bimestre (Olinda COD_INDI 27). CAI ao longo do ano por construcao: o denominador acumula receita e a sobra se dilui (exemplo real, Acrelandia 2024: 38,83% no 1o bimestre -> 2,90% no 6o). O limite legal de 10% SO VINCULA NO 6o BIMESTRE; nos bimestres 1 a 5 um valor acima de 10% e o normal, nao descumprimento. Nao existe versao 'do bimestre': percentual nao se desacumula. |
| `ind2_valor_fundeb_nao_aplicado` | NUMERIC | Valor R$ do FUNDEB nao utilizado, ACUMULADO ate este bimestre (Olinda COD_INDI 91). So existe de 2021 em diante. |
| `ind2_valor_fundeb_nao_aplicado_estimado_piso` | NUMERIC | ESTIMATIVA de piso do valor nao aplicado: ind2_pct x ind1_fundeb_recebido_acumulado. Mesma ressalva da tabela anual — subestima na maioria dos municipios porque a base do percentual inclui recurso de exercicios anteriores. Use como piso, nunca como valor declarado. |
| `mde_pct` | FLOAT | % da receita de impostos aplicado em MDE, ACUMULADO ate este bimestre (Olinda COD_INDI 24 no fechamento ou 40 na parcial). Minimo constitucional: 25%. Serve aos indicadores 4 e 5 — a diferenca entre eles e do grao ANUAL (fechou o 6o bimestre ou parou antes); bimestre a bimestre existe um unico valor, e mde_origem diz de qual familia veio. |
| `mde_valor_exigido` | NUMERIC | Valor exigido de aplicacao em MDE acumulado ate este bimestre (Olinda COD_INDI 93 no fechamento ou 96 na parcial). So existe de 2020 em diante: antes disso a Olinda publica apenas o percentual. |
| `mde_valor_aplicado` | NUMERIC | Valor aplicado em MDE acumulado ate este bimestre (Olinda COD_INDI 94 no fechamento ou 97 na parcial). So existe de 2020 em diante. |
| `mde_falta_para_valor_exigido` | NUMERIC | Quanto ainda FALTA aplicar em R$ para alcancar o exigido ate este bimestre: GREATEST(0, exigido - aplicado). ZERO quando ja atingiu — nao fica negativo. NULO quando a fonte nao publica os valores em R$ (bimestres de 2017 a 2019): nulo e NAO SEI, zero e NAO FALTA NADA. Tambem e nulo quando o exigido vem zerado (declaracao vazia). ATENCAO: ~16 registros de 2023 (bimestres 1 e 2) trazem percentual e valores INCONSISTENTES na propria fonte — o aplicado supera o exigido enquanto o COD_INDI 24 marca 7%; nesses casos a falta zero contradiz o percentual, e a divergencia e da declaracao, nao do calculo. Cair a zero ao longo do ano e o comportamento esperado: mostra em QUE BIMESTRE o municipio fecha a conta do minimo. |
| `mde_diferenca_aplicado_vs_exigido` | NUMERIC | Diferenca em R$ entre o aplicado e o exigido em MDE, acumulada ate este bimestre: aplicado - exigido. NEGATIVA enquanto o municipio esta abaixo do exigido do periodo (o modulo e quanto falta) e POSITIVA quando ja passou (quanto ultrapassou). Diferente de mde_falta_para_valor_exigido, que trava em zero e so enxerga a falta. Mesmas guardas de nulo: sem os valores em R$ (bimestres de 2017 a 2019) ou exigido <= 0, que e declaracao vazia. |
| `mde_origem` | STRING | De qual familia de indicadores da Olinda o MDE deste bimestre veio: FECHAMENTO (COD_INDI 24/93/94) ou PARCIAL (40/96/97). Alimenta a separacao entre IND4 e IND5. |
| `ind1_ressarcimento_fundeb_rreo` | NUMERIC | Ressarcimento de recursos do FUNDEB quando publicado no RREO/PDF do mesmo bimestre de referencia; fica NULL/0 quando nao houver valor publicado. |
| `flag_ind1_tem_ressarcimento` | BOOLEAN | TRUE quando o RREO/PDF do bimestre de referencia traz ressarcimento de recursos do FUNDEB maior que zero. |
| `pct_uso_folha_fundeb` | FLOAT | IND6: % de aplicacao do FUNDEB na remuneracao dos profissionais da educacao, ACUMULADO ate este bimestre (Olinda COD_INDI 67). |
| `meta_pct_uso_folha_fundeb` | FLOAT | Meta percentual do IND6 no ano: 60 (2008-2020, magisterio) ou 70 (2021+, profissionais da educacao, Lei 14.113/2020). |
| `regra_pct_uso_folha_fundeb` | STRING | Rotulo da regra historica do IND6 no ano: MAGISTERIO_60 ou EDUCACAO_70. |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC da construcao da tabela. |

## semantic · obt_api_olinda_siope_indicadores_uf_ano

File `semantic__obt_api_olinda_siope_indicadores_uf_ano.parquet` · 491 rows · 50 columns

SIOPE - indicadores financeiros da educacao por UNIDADE FEDERATIVA x ANO (27 governos estaduais, 26 estados + DF). Espelha obt_api_olinda_siope_indicadores_municipio_ano no grao estadual. ATENCAO: o SIOPE usa um codebook de COD_INDI DIFERENTE para estado e municipio - o mesmo codigo significa outra coisa em cada esfera, e o mapa aqui foi validado contra o RREO da propria UF. O IND1 e Olinda pura (o municipal e reconciliado com o RREO), com residuo medido na casa de 0,5%. Minas Gerais praticamente nao declara ao SIOPE e aparece vazio em quase tudo.

**Built from:** `semantic/obt_fnde_fundeb_municipio_ano`, `semantic/obt_fnde_salario_educacao_distribuido_municipio_mes`, `semantic/obt_fnde_salario_educacao_previsto_municipio_ano`, `semantic/obt_ibge_uf`, `semantic/obt_rreo_siope_uf_bimestre`, `trusted/api_olinda_siope_indicadores`, `trusted/api_olinda_siope_receita`, `trusted/fundeb_painel_distribuicao`

**Feeds:** `semantic/obt_api_olinda_siope_comparativo_uf_par_anos`

| Column | Type | Description |
|---|---|---|
| `codigo_uf` | INTEGER | Codigo IBGE da UF (2 digitos) — chave de join e do RREO estadual. |
| `sigla_uf` | STRING | Sigla da UF. |
| `nome_uf` | STRING | Nome da UF segundo o IBGE. |
| `nome_regiao` | STRING | Nome da regiao segundo o IBGE. |
| `ano` | INTEGER | Ano de exercicio. |
| `num_periodo_referencia` | INTEGER | Ultimo bimestre em que o governo estadual declarou os indicadores de MDE (COD_INDI 40/96/97). TODOS os valores da linha saem deste mesmo bimestre, para o snapshot ser consistente. 6 = exercicio fechado; menor = o estado nao fechou as contas. Ate 2016 o SIOPE publica uma declaracao anual unica marcada como bimestre 1, que E o fechamento daquela era. |
| `ind1_fundeb_recebido` | NUMERIC | FUNDEB efetivamente recebido pelo governo estadual, acumulado ate o bimestre de referencia. RECONCILIADO com o RREO: o valor e a LINHA CHEIA do relatorio (Receitas Recebidas do FUNDEB), que e exatamente o que esta no PDF publicado pelo estado. A Olinda entra como fallback quando o RREO daquele bimestre nao existe. A linha cheia inclui o rendimento de aplicacao financeira e o ressarcimento, que a Olinda NAO publica como FUNDEB — por isso a Olinda pura fica ~0,5% abaixo do PDF. Conferido ao centavo em Pernambuco 2024, 6o bimestre: total 4.014.584.777,28 = Olinda 3.980.435.276,46 + rendimento 34.059.369,66 + ressarcimento 90.131,16. |
| `ind1_fundeb_recebido_fonte` | STRING | De onde saiu ind1_fundeb_recebido: RREO quando veio da linha cheia do relatorio (bate 100% com o PDF) ou OLINDA quando o RREO daquele bimestre nao existe e o valor caiu no somatorio da receita declarada, que fica ligeiramente abaixo. |
| `ind1_rendimento_aplicacao_rreo` | NUMERIC | Rendimento de aplicacao financeira dos recursos do FUNDEB, lido do RREO. Ja esta DENTRO de ind1_fundeb_recebido, porque a linha cheia do relatorio o soma. Existe em coluna propria porque a Olinda classifica esse valor como receita patrimonial e nao como FUNDEB: e a maior parte da diferenca entre as duas fontes. |
| `ind1_ressarcimento_fundeb_rreo` | NUMERIC | Ressarcimento de recursos do FUNDEB (devolucao do ente ao fundo), lido do RREO. Tambem ja esta dentro de ind1_fundeb_recebido. A Olinda nao expoe essa parcela. |
| `flag_ind1_tem_ressarcimento` | BOOLEAN | TRUE quando o RREO do bimestre de referencia traz ressarcimento de recursos do FUNDEB maior que zero. |
| `ind1_fundeb_previsao_atualizada` | NUMERIC | Previsao orcamentaria ATUALIZADA do FUNDEB declarada pelo proprio governo estadual, no mesmo bimestre de referencia. E a expectativa do ente, nao a do FNDE. |
| `ind1_fundeb_previsao_federal` | NUMERIC | Previsao oficial do FNDE de repasse de FUNDEB ao governo estadual no ano (painel do FUNDEB, esfera Estadual). So existe de 2021 em diante. Diferente da previsao do ente: esta e a estimativa de quem paga. |
| `num_periodo_receita` | INTEGER | De qual bimestre veio a receita usada no IND1. Quando menor que num_periodo_referencia, o FUNDEB esta acumulado ate um bimestre ANTERIOR ao dos demais indicadores da linha e subestima o exercicio — e o que flag_ind1_receita_defasada marca. |
| `flag_ind1_receita_defasada` | BOOLEAN | TRUE quando num_periodo_receita < num_periodo_referencia. Nesse caso o FUNDEB recebido/previsto NAO deve ser comparado com o total de outro ano. Causa e cobertura da fonte, nao calculo. |
| `flag_ind1_receita_incompleta` | BOOLEAN | TRUE quando o bimestre usado para a receita existe mas veio sem a conta PRINCIPAL do FUNDEB (so a complementacao da Uniao), OU com MENOS contas distintas que outro bimestre do mesmo exercicio. O acumulado do RREO nunca perde componente, entao isso denuncia ingestao parcial. |
| `ind1_fundeb_recebido_rotulo` | STRING | ind1_fundeb_recebido formatado em R$ pt-BR, com asterisco quando ha flag de qualidade. Existe para os cartoes de numero do dashboard, que nao conseguem marcar a condicao de outro jeito. |
| `ind1_fundeb_previsao_atualizada_rotulo` | STRING | Mesmo tratamento do rotulo do recebido, para a previsao do proprio estado. |
| `ind1_fundeb_previsao_federal_rotulo` | STRING | ind1_fundeb_previsao_federal formatado em R$ pt-BR para os cartoes do dashboard. |
| `ind1_pct_variacao_recebido_vs_previsao_federal` | FLOAT | (recebido - previsao federal) / previsao federal x 100, no mesmo ano. |
| `ind1_valor_variacao_recebido_vs_previsao_federal` | NUMERIC | recebido - previsao federal, no mesmo ano, em R$ nominais. |
| `ind1_pct_variacao_recebido_vs_previsao_estadual` | FLOAT | (recebido - previsao do proprio estado) / previsao estadual x 100, no mesmo ano. Equivale ao ..._vs_previsao_municipal do grao municipal. |
| `ind1_valor_variacao_recebido_vs_previsao_estadual` | NUMERIC | recebido - previsao do proprio estado, no mesmo ano, em R$ nominais. |
| `ind2_pct_fundeb_nao_aplicado` | FLOAT | % das receitas do FUNDEB nao aplicadas no exercicio (max 10%). Olinda estadual COD_INDI 44. O limite so vincula no 6o bimestre. |
| `ind2_valor_fundeb_nao_aplicado` | NUMERIC | Valor R$ dos recursos do FUNDEB nao utilizados. Olinda estadual COD_INDI 94. So existe de 2021 em diante. |
| `ind2_valor_fundeb_nao_aplicado_estimado_piso` | NUMERIC | ESTIMATIVA de piso (nao e dado oficial): ind2_pct x ind1_fundeb_recebido. Existe para os anos em que a fonte publica so o percentual. |
| `ind2_valor_fundeb_nao_aplicado_exibicao` | NUMERIC | Valor do FUNDEB nao aplicado para EXIBICAO: o oficial quando existe, senao a estimativa de piso. |
| `ind2_valor_fundeb_nao_aplicado_e_estimado` | BOOLEAN | TRUE quando ind2_valor_fundeb_nao_aplicado_exibicao veio da estimativa, nao do valor oficial. |
| `ind2_valor_fundeb_nao_aplicado_rotulo` | STRING | Valor de exibicao formatado em R$ pt-BR, com asterisco quando e estimativa. |
| `ind3_salario_educacao` | NUMERIC | Salario-Educacao do governo estadual no ano: distribuido quando o exercicio fechou, previsto enquanto o ano corre. A serie do distribuido e CONTINUA desde 2007: ate 2019 ela sai do documento de cota estadual/municipal, que traz uma linha por UF e esfera, e de 2020 em diante do documento por ente federado. |
| `ind3_salario_educacao_previsto` | NUMERIC | Estimativa das quotas de Salario-Educacao publicada pelo FNDE no comeco do ano. Serie por UF desde 2010. |
| `ind3_salario_educacao_distribuido` | NUMERIC | Salario-Educacao efetivamente repassado ao governo estadual no ano, somando as 12 competencias. Diferente do grao municipal, que so tem distribuido de 2020 em diante: no estadual a serie e continua, porque ate 2019 o FNDE publicava justamente a abertura por UF e esfera. |
| `ind3_fonte_valor_analitico` | STRING | De onde saiu ind3_salario_educacao: DISTRIBUIDO, PREVISTO ou DISTRIBUIDO_PARCIAL. |
| `ind3_exercicio_fechado` | BOOLEAN | TRUE quando o distribuido do ano cobre o exercicio inteiro. |
| `ind4_pct_aplicado_mde_fechado` | FLOAT | % aplicado em MDE no FECHAMENTO do exercicio (num_periodo_referencia = 6, ou ano <= 2016). Minimo constitucional de 25%. Olinda estadual COD_INDI 40. |
| `ind5_pct_aplicado_mde_parcial` | FLOAT | % aplicado em MDE em declaracao PARCIAL: o estado parou de declarar antes do 6o bimestre (e o ano e >= 2017). Acumulado ate o bimestre declarado, entao um valor abaixo de 25% aqui significa ano incompleto, nao descumprimento. |
| `ind4_valor_exigido_mde_fechado` | NUMERIC | Valor exigido de aplicacao em MDE no fechamento. Olinda estadual COD_INDI 96. So existe de 2020 em diante. |
| `ind5_valor_exigido_mde_parcial` | NUMERIC | Valor exigido de aplicacao em MDE em declaracao parcial, ACUMULADO ate o bimestre declarado. |
| `ind4_valor_aplicado_mde_fechado` | NUMERIC | Valor aplicado em MDE no fechamento. Olinda estadual COD_INDI 97. So existe de 2020 em diante. |
| `ind5_valor_aplicado_mde_parcial` | NUMERIC | Valor aplicado em MDE em declaracao parcial, ACUMULADO ate o bimestre declarado. |
| `ind4_falta_para_valor_exigido` | NUMERIC | Quanto FALTA aplicar em R$ para alcancar o minimo no fechamento: GREATEST(0, exigido - aplicado). Trava em zero: excedente nao e divida. NULO quando a fonte nao publica os valores em R$. |
| `ind5_falta_para_valor_exigido` | NUMERIC | Mesmo calculo, para os anos de declaracao parcial. O exigido tambem e parcial. |
| `ind4_diferenca_aplicado_vs_exigido` | NUMERIC | Diferenca em R$ entre o aplicado e o exigido no fechamento: aplicado - exigido. NEGATIVA quando ficou abaixo do minimo (o modulo e quanto falta) e POSITIVA quando passou. Diferente da falta, que trava em zero. |
| `ind5_diferenca_aplicado_vs_exigido` | NUMERIC | Mesmo calculo, para os anos de declaracao parcial. |
| `pct_uso_folha_fundeb` | FLOAT | % de aplicacao do FUNDEF/FUNDEB na remuneracao dos profissionais da educacao. Olinda estadual COD_INDI 42, serie continua desde 2008. |
| `meta_pct_uso_folha_fundeb` | FLOAT | Meta percentual aplicavel no ano: 60 (2008-2020, magisterio) ou 70 (2021+, todos os profissionais da educacao, Lei 14.113/2020). |
| `regra_pct_uso_folha_fundeb` | STRING | Qual regra vale no ano: MAGISTERIO_60 ou EDUCACAO_70. |
| `superavit_deficit_exercicio` | NUMERIC | Superavit(+)/Deficit(-) do ente no exercicio (R$). Olinda estadual COD_INDI 83. E o resultado do ente inteiro, nao so da educacao. |
| `saldo_financeiro_fundeb` | NUMERIC | Disponibilidade financeira de FUNDEB ate o bimestre de referencia (R$). Olinda estadual COD_INDI 84. E ESTOQUE (o que esta em caixa), nao fluxo acumulado. |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC da construcao da tabela. |

## semantic · obt_api_olinda_siope_indicadores_uf_bimestre

File `semantic__obt_api_olinda_siope_indicadores_uf_bimestre.parquet` · 1,433 rows · 21 columns

SIOPE - indicadores financeiros da educacao por UNIDADE FEDERATIVA x ANO x BIMESTRE (2017+). Espelha obt_api_olinda_siope_indicadores_municipio_bimestre no grao estadual, com o codebook de COD_INDI ESTADUAL (40/42/44/94/96/97), que e diferente do municipal. ATENCAO: os valores sao ACUMULADOS no ano, como o RREO publica - somar os 6 bimestres multiplica o exercicio. Para valor do periodo existe ind1_fundeb_recebido_no_bimestre, ja desacumulado; percentual nao se desacumula.

**Built from:** `semantic/obt_ibge_uf`, `trusted/api_olinda_siope_indicadores`, `trusted/api_olinda_siope_receita`

| Column | Type | Description |
|---|---|---|
| `codigo_uf` | INTEGER | Codigo IBGE da UF (2 digitos). |
| `sigla_uf` | STRING | Sigla da UF. |
| `nome_uf` | STRING | Nome da UF segundo o IBGE. |
| `ano` | INTEGER | Ano de exercicio. |
| `bimestre` | INTEGER | Bimestre do RREO (1 a 6). |
| `ind1_fundeb_recebido_acumulado` | NUMERIC | FUNDEB recebido ACUMULADO no ano ate este bimestre, como o RREO publica. NAO e o valor do bimestre: cada bimestre repete o exercicio inteiro ate ali. Para o valor do periodo use ind1_fundeb_recebido_no_bimestre. |
| `ind1_fundeb_recebido_no_bimestre` | NUMERIC | FUNDEB que entrou NESTE bimestre: o acumulado menos o do bimestre anterior do mesmo ano. E o que faz sentido somar. Percentual NAO se desacumula. |
| `ind1_fundeb_previsao_atualizada` | NUMERIC | Previsao orcamentaria atualizada do FUNDEB vigente neste bimestre, declarada pelo proprio estado. |
| `ind2_pct_fundeb_nao_aplicado` | FLOAT | % das receitas do FUNDEB nao aplicadas, ACUMULADO ate este bimestre (Olinda estadual COD_INDI 44). CAI ao longo do ano por construcao, e o limite de 10% so vincula no 6o bimestre. |
| `ind2_valor_fundeb_nao_aplicado` | NUMERIC | Valor R$ do FUNDEB nao utilizado, ACUMULADO ate este bimestre (Olinda estadual COD_INDI 94). So existe de 2021 em diante. |
| `ind2_valor_fundeb_nao_aplicado_estimado_piso` | NUMERIC | ESTIMATIVA de piso: ind2_pct x recebido acumulado. Para os bimestres em que a fonte publica so o percentual. |
| `mde_pct` | FLOAT | % da receita de impostos aplicado em MDE, ACUMULADO ate este bimestre (Olinda estadual COD_INDI 40). Minimo constitucional de 25%, que so vincula no 6o bimestre. |
| `mde_valor_exigido` | NUMERIC | Valor exigido de aplicacao em MDE acumulado ate este bimestre (Olinda estadual COD_INDI 96). So existe de 2020 em diante. |
| `mde_valor_aplicado` | NUMERIC | Valor aplicado em MDE acumulado ate este bimestre (Olinda estadual COD_INDI 97). So existe de 2020 em diante. |
| `mde_falta_para_valor_exigido` | NUMERIC | Quanto ainda FALTA aplicar em R$ para alcancar o exigido ate este bimestre: GREATEST(0, exigido - aplicado). Trava em zero. NULO quando a fonte nao publica os valores em R$ ou o exigido vem zerado. |
| `mde_diferenca_aplicado_vs_exigido` | NUMERIC | Diferenca em R$ entre o aplicado e o exigido, acumulada ate este bimestre: aplicado - exigido. NEGATIVA enquanto esta abaixo do exigido do periodo, POSITIVA quando ja passou. Diferente da falta, que trava em zero. |
| `mde_origem` | STRING | De qual situacao de prestacao de contas o MDE deste bimestre veio: FECHAMENTO quando o bimestre e o 6o, PARCIAL nos demais. Alimenta a separacao entre IND4 e IND5 na visao bimestral. |
| `pct_uso_folha_fundeb` | FLOAT | % de aplicacao do FUNDEB na remuneracao dos profissionais da educacao, ACUMULADO ate este bimestre (Olinda estadual COD_INDI 42). |
| `meta_pct_uso_folha_fundeb` | FLOAT | Meta percentual do ano: 60 ate 2020, 70 de 2021 em diante. |
| `regra_pct_uso_folha_fundeb` | STRING | MAGISTERIO_60 ou EDUCACAO_70. |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC da construcao da tabela. |

## semantic · obt_fnde_siope_dados_gerais_municipio_ano

File `semantic__obt_fnde_siope_dados_gerais_municipio_ano.parquet` · 166,293 rows · 29 columns

SIOPE FNDE Dados Gerais (resumo) por municipio x ano x bimestre. WIDE: conjunto fixo de metricas (receita/despesa totais, despesa com educacao, PIB, populacao, FPM/ICMS/FUNDEB). Dedup pela declaracao mais recente. FK codigo_municipio -> obt_ibge_municipio. Origem: trusted_zone.fnde_siope_dados_gerais.

**Built from:** `semantic/obt_ibge_municipio`, `trusted/fnde_siope_dados_gerais`

| Column | Type | Description |
|---|---|---|
| `codigo_municipio` | INTEGER | Codigo IBGE 7 digitos (FK obt_ibge_municipio); resolvido do codigo FNDE 6 dig. |
| `nome_municipio` | STRING | Nome do municipio (IBGE). |
| `sigla_uf` | STRING | Sigla UF (IBGE). |
| `nome_regiao` | STRING | Regiao (IBGE). |
| `esfera` | STRING | Esfera administrativa: Municipal ou Estadual (coluna 'tipo' da origem). |
| `ano` | INTEGER | Ano de referencia (num_ano). |
| `num_periodo` | INTEGER | Bimestre de referencia (num_peri). |
| `populacao` | INTEGER | Populacao do municipio (num_popu). |
| `pib` | FLOAT | PIB do municipio (val_pib). |
| `pib_per_capita` | FLOAT | PIB per capita (val_pib_percapto). |
| `receita_prevista_atualizada` | FLOAT | Receita prevista atualizada (val_rece_prev_atua). |
| `receita_realizada` | FLOAT | Receita realizada (val_rece_real). |
| `receita_orcada` | FLOAT | Receita orcada (val_rece_orca). |
| `despesa_dotacao_atualizada` | FLOAT | Despesa - dotacao atualizada (val_desp_dota_atua). |
| `despesa_empenhada` | FLOAT | Despesa empenhada (val_desp_empe). |
| `despesa_liquidada` | FLOAT | Despesa liquidada (val_desp_liqu). |
| `despesa_paga` | FLOAT | Despesa paga (val_desp_paga). |
| `despesa_orcada` | FLOAT | Despesa orcada (val_desp_orca). |
| `despesa_edu_dotacao_atualizada` | FLOAT | Despesa com educacao - dotacao (vl_desp_dota_atua_edu). |
| `despesa_edu_empenhada` | FLOAT | Despesa educacao empenhada (vl_desp_empe_edu). |
| `despesa_edu_liquidada` | FLOAT | Despesa educacao liquidada (vl_desp_liqu_edu). |
| `despesa_edu_paga` | FLOAT | Despesa educacao paga (vl_desp_paga_edu). |
| `despesa_edu_orcada` | FLOAT | Despesa educacao orcada (vl_desp_orca_edu). |
| `fpm` | FLOAT | Fundo de Participacao dos Municipios (num_fpm). |
| `icms` | FLOAT | Cota ICMS (num_icms). |
| `fundef_fundeb` | FLOAT | FUNDEF/FUNDEB (num_fundef). |
| `data_declaracao` | TIMESTAMP | Data da declaracao (dat_decl). |
| `responsavel_metodo_apuracao` | STRING | Indicador do metodo de apuracao (idn_assu_resp_mtdo_apur). |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC de geracao na semantica. |

## semantic · obt_fnde_siope_despesa_educacao_municipio_ano

File `semantic__obt_fnde_siope_despesa_educacao_municipio_ano.parquet` · 135,140,891 rows · 18 columns

FNDE SIOPE Despesa com Educacao detalhada — LONG hierarquico (pasta/subfuncao/item/fonte x fase). Grao inclui coluna_valor (Dotacao/Empenhada/Liquidada/Paga). 2021-2025. Ruido de coluna numerica filtrado. Origem: trusted_zone.fnde_siope_despesa_total_educacao + IBGE.

**Built from:** `semantic/obt_ibge_municipio`, `trusted/fnde_siope_despesa_total_educacao`

| Column | Type | Description |
|---|---|---|
| `codigo_municipio` | INTEGER | Codigo IBGE 7 digitos do municipio (FK obt_ibge_municipio); resolvido do codigo FNDE de 6 digitos. |
| `nome_municipio` | STRING | Nome do municipio (obt_ibge_municipio). |
| `sigla_uf` | STRING | Sigla da UF (obt_ibge_municipio). |
| `nome_regiao` | STRING | Regiao geografica (obt_ibge_municipio). |
| `esfera` | STRING | Esfera: Municipal ou Estadual. |
| `ano` | INTEGER | Ano. |
| `num_periodo` | INTEGER | Numero do periodo (bimestre 1-6; anual). |
| `codigo_pasta` | STRING | Codigo da pasta/grupo de despesa. |
| `nome_pasta` | STRING | Nome da pasta/grupo. |
| `codigo_subfuncao` | STRING | Codigo da subfuncao. |
| `codigo_exibicao` | STRING | Codigo de exibicao do item na arvore. |
| `codigo_fonte` | STRING | Codigo da fonte de recurso. |
| `nome_item` | STRING | Nome do item/rubrica de despesa. |
| `nivel` | INTEGER | Nivel hierarquico do item. |
| `ordem` | INTEGER | Ordem de exibicao. |
| `coluna_valor` | STRING | Fase da despesa: Dotacao Atualizada, Desp. Empenhadas, Desp. Liquidadas, Desp. Pagas. |
| `valor` | FLOAT | Valor declarado (R$). |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC de geracao desta tabela semantica. |

## semantic · obt_fnde_siope_despesa_funcao_municipio_ano

File `semantic__obt_fnde_siope_despesa_funcao_municipio_ano.parquet` · 1,191,974 rows · 13 columns

FNDE SIOPE Despesa por Subfuncao da Educacao — LONG. Grao: (codigo_municipio, ano, num_periodo, esfera, subfuncao). empenhada/liquidada/paga. 2021-2025. Origem: trusted_zone.fnde_siope_despesas_funcao_educacao + IBGE.

**Built from:** `semantic/obt_ibge_municipio`, `trusted/fnde_siope_despesas_funcao_educacao`

| Column | Type | Description |
|---|---|---|
| `codigo_municipio` | INTEGER | Codigo IBGE 7 digitos do municipio (FK obt_ibge_municipio); resolvido do codigo FNDE de 6 digitos. |
| `nome_municipio` | STRING | Nome do municipio (obt_ibge_municipio). |
| `sigla_uf` | STRING | Sigla da UF (obt_ibge_municipio). |
| `nome_regiao` | STRING | Regiao geografica (obt_ibge_municipio). |
| `esfera` | STRING | Esfera: Municipal ou Estadual. |
| `ano` | INTEGER | Ano. |
| `num_periodo` | INTEGER | Numero do periodo. |
| `ordem` | INTEGER | Ordem de exibicao. |
| `subfuncao` | STRING | Subfuncao da despesa (ex: Ensino Fundamental, Educacao Infantil). |
| `valor_empenhada` | FLOAT | Despesa empenhada (R$). |
| `valor_liquidada` | FLOAT | Despesa liquidada (R$). |
| `valor_paga` | FLOAT | Despesa paga (R$). |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC de geracao desta tabela semantica. |

## semantic · obt_fnde_siope_indicador_municipio_ano

File `semantic__obt_fnde_siope_indicador_municipio_ano.parquet` · 6,411,059 rows · 12 columns

FNDE SIOPE Indicadores — LONG. Grao: (codigo_municipio, ano, num_periodo, esfera, indicador). Colunas de grupo descartadas (corrompidas no raw). 2021-2025. Origem: trusted_zone.fnde_siope_indicadores + IBGE.

**Built from:** `semantic/obt_ibge_municipio`, `trusted/fnde_siope_indicadores`

| Column | Type | Description |
|---|---|---|
| `codigo_municipio` | INTEGER | Codigo IBGE 7 digitos do municipio (FK obt_ibge_municipio); resolvido do codigo FNDE de 6 digitos. |
| `nome_municipio` | STRING | Nome do municipio (obt_ibge_municipio). |
| `sigla_uf` | STRING | Sigla da UF (obt_ibge_municipio). |
| `nome_regiao` | STRING | Regiao geografica (obt_ibge_municipio). |
| `esfera` | STRING | Esfera: Municipal ou Estadual. |
| `ano` | INTEGER | Ano. |
| `num_periodo` | INTEGER | Numero do periodo. |
| `codigo_indicador` | STRING | Codigo do indicador SIOPE. |
| `codigo_exibicao` | STRING | Codigo de exibicao. |
| `nome_indicador` | STRING | Nome do indicador. |
| `valor` | FLOAT | Valor do indicador (numero ou %). |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC de geracao desta tabela semantica. |

## semantic · obt_fnde_siope_info_complementar_municipio_ano

File `semantic__obt_fnde_siope_info_complementar_municipio_ano.parquet` · 8,322,693 rows · 11 columns

FNDE SIOPE Informacoes Complementares — LONG. Grao: (codigo_municipio, ano, num_periodo, item). item -> valor_texto/valor_numerico. 2007-2025. Origem: trusted_zone.fnde_siope_informacoes_complementares + IBGE.

**Built from:** `semantic/obt_ibge_municipio`, `trusted/fnde_siope_informacoes_complementares`

| Column | Type | Description |
|---|---|---|
| `codigo_municipio` | INTEGER | Codigo IBGE 7 digitos do municipio (FK obt_ibge_municipio); resolvido do codigo FNDE de 6 digitos. |
| `nome_municipio` | STRING | Nome do municipio (obt_ibge_municipio). |
| `sigla_uf` | STRING | Sigla da UF (obt_ibge_municipio). |
| `nome_regiao` | STRING | Regiao geografica (obt_ibge_municipio). |
| `ano` | INTEGER | Ano. |
| `num_periodo` | INTEGER | Numero do periodo. |
| `codigo_exibicao` | STRING | Codigo de exibicao do item. |
| `nome_item` | STRING | Nome do item/informacao complementar. |
| `valor_texto` | STRING | Valor declarado como texto (quando aplicavel). |
| `valor_numerico` | FLOAT | Valor declarado numerico (quando aplicavel). |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC de geracao desta tabela semantica. |

## semantic · obt_fnde_siope_receita_municipio_ano

File `semantic__obt_fnde_siope_receita_municipio_ano.parquet` · 14,236,762 rows · 14 columns

FNDE SIOPE Receita por conta contabil — LONG. Grao: (codigo_municipio, ano, tipo_periodo, num_periodo, esfera, conta_contabil). 2005-2019. Origem: trusted_zone.fnde_siope_receita_total + IBGE.

**Built from:** `semantic/obt_ibge_municipio`, `trusted/fnde_siope_receita_total`

| Column | Type | Description |
|---|---|---|
| `codigo_municipio` | INTEGER | Codigo IBGE 7 digitos do municipio (FK obt_ibge_municipio); resolvido do codigo FNDE de 6 digitos. |
| `nome_municipio` | STRING | Nome do municipio (obt_ibge_municipio). |
| `sigla_uf` | STRING | Sigla da UF (obt_ibge_municipio). |
| `nome_regiao` | STRING | Regiao geografica (obt_ibge_municipio). |
| `esfera` | STRING | Esfera administrativa: MUNICIPAL ou ESTADUAL. |
| `ano` | INTEGER | Ano do exercicio. |
| `tipo_periodo` | STRING | Tipo de periodo: ANUAL ou BIMESTRAL. |
| `num_periodo` | INTEGER | Numero do periodo (bimestre 1-6; anual=1). |
| `codigo_conta_contabil` | STRING | Codigo da conta contabil da receita. |
| `nome_conta_contabil` | STRING | Nome da conta contabil. |
| `valor_previsao_atualizada` | FLOAT | Valor previsto atualizado (R$). |
| `valor_realizadas` | FLOAT | Valor realizado (R$). |
| `valor_orcada` | FLOAT | Valor orcado (R$). |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC de geracao desta tabela semantica. |

## semantic · obt_rreo_siope_municipio_ano

File `semantic__obt_rreo_siope_municipio_ano.parquet` · 42,649,158 rows · 16 columns

RREO SIOPE Municipio — formato LONG/tidy, snapshot ANUAL (ultimo bimestre disponivel de cada ano, que e acumulado ate o bimestre). Grao: 1 linha por (codigo_municipio, ano, codigo, posicao). Cada linha e um par (rubrica x metrica) da arvore do RREO. FORMATO LONG porque o RREO e uma arvore hierarquica viva: os codigos (1, 1.1, 1.1.1 ... ate ~52) entram e saem entre anos (ex: VAAT/VAAR so apos a nova lei do FUNDEB 2021), entao uma tabela WIDE quebraria a cada mudanca de layout. LONG absorve: nova rubrica = nova linha, sem mudar schema. Use nome_metrica para a metrica e descricao/codigo para a rubrica. Enriquecido com geografia IBGE. url_download_pdf aponta para o PDF-fonte no GCS. Origem: trusted_zone.rreo_siope_municipio.

**Built from:** `semantic/obt_ibge_municipio`, `trusted/rreo_siope_municipio`

| Column | Type | Description |
|---|---|---|
| `codigo_municipio` | INTEGER | Codigo IBGE 7 digitos do municipio. FK para obt_ibge_municipio. (resolvido do codigo FNDE de 6 digitos). |
| `nome_municipio` | STRING | Nome do municipio (de obt_ibge_municipio). |
| `sigla_uf` | STRING | Sigla da UF do municipio (de obt_ibge_municipio). |
| `nome_regiao` | STRING | Regiao geografica do municipio (de obt_ibge_municipio). |
| `ano` | INTEGER | Ano de referencia do RREO. |
| `bimestre` | INTEGER | Bimestre de referencia do snapshot anual (o ultimo disponivel do ano; valores sao acumulados ate o bimestre). |
| `secao` | INTEGER | Codigo raiz (INT64, 1..52) — agrupa o assunto: receitas, deducoes, FUNDEB, despesas MDE, restos a pagar, disponibilidade financeira. |
| `codigo` | STRING | Codigo hierarquico completo da rubrica no RREO (ex '6.3.1'). STRING. |
| `nivel` | INTEGER | Profundidade do codigo: 0=secao raiz, 1=X.Y, 2=X.Y.Z. |
| `descricao` | STRING | Rotulo textual da rubrica conforme o PDF do RREO. |
| `coluna` | STRING | Header cru da coluna de valor extraido do PDF (pode ter ruido de parse); NULL quando so posicional. Use nome_metrica. |
| `posicao` | INTEGER | Ordinal da coluna de valor dentro da rubrica (1..N). Sempre presente. |
| `nome_metrica` | STRING | Nome canonico da metrica: header observado quando capturado, senao default pelo perfil de colunas da secao (receita: Previsao/Realizada; despesa: Dotacao/Empenhada/Liquidada/Paga/RP; indicador: Exigido/Aplicado/%). |
| `valor` | FLOAT | Valor numerico (FLOAT64) da rubrica x metrica, em R$ (ou % para indicadores). |
| `arquivo` | STRING | Nome do PDF-fonte no FTP do FNDE. |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC de geracao desta tabela semantica. |

## semantic · obt_rreo_siope_municipio_bimestre

File `semantic__obt_rreo_siope_municipio_bimestre.parquet` · 154,132,717 rows · 17 columns

RREO SIOPE Municipio BIMESTRAL (LONG) — 1 linha por (codigo_municipio, ano, bimestre, codigo, posicao). TODOS os bimestres (2017-2025 completos; 2010-2016 so 1/ano na origem FNDE). Valores acumulados ate o bimestre (permite a curva de execucao intra-ano). is_fechamento=TRUE marca o ultimo bimestre do ano (= snapshot da obt_..._ano). Origem: trusted_zone.rreo_siope_municipio. Complementa obt_rreo_siope_municipio_ano (anual). Base p/ previsao (Produto 2).

**Built from:** `semantic/obt_ibge_municipio`, `trusted/rreo_siope_municipio`

**Feeds:** `semantic/obt_api_olinda_siope_indicadores_municipio_ano`, `semantic/obt_api_olinda_siope_indicadores_municipio_bimestre`

| Column | Type | Description |
|---|---|---|
| `codigo_municipio` | INTEGER | Código IBGE de 7 dígitos que identifica univocamente o município. |
| `nome_municipio` | STRING | Nome do município brasileiro correspondente. |
| `sigla_uf` | STRING | Sigla da Unidade Federativa (estado) do município. |
| `nome_regiao` | STRING | Nome da região geográfica brasileira onde o município está localizado. |
| `ano` | INTEGER | Ano de referência do relatório orçamentário (formato YYYY). |
| `bimestre` | INTEGER | Bimestre de referência do relatório (valores de 1 a 6). |
| `is_fechamento` | BOOLEAN | Indica se os dados correspondem à versão final/fechamento do relatório (true/false). |
| `secao` | INTEGER | Identificador da seção ou quadro específico dentro do relatório RREO. |
| `codigo` | STRING | Código numérico identificador da linha ou item de despesa/receita no relatório. |
| `nivel` | INTEGER | Nível hierárquico da conta ou item na estrutura do relatório (ex: 0 para nível principal). |
| `descricao` | STRING | Descrição textual da conta, receita ou despesa orçamentária declarada. |
| `coluna` | STRING | Nome da coluna original do relatório RREO de onde o valor foi extraído. |
| `posicao` | INTEGER | Posição de ordenação ou índice do item no documento original. |
| `nome_metrica` | STRING | Nome da métrica financeira ou indicador orçamentário associado (ex: DOTAÇÃO ATUALIZADA). |
| `valor` | FLOAT | Valor numérico associado à métrica (geralmente em formato decimal/monetário ou percentual). |
| `arquivo` | STRING | Nome do arquivo PDF original do RREO do qual os dados foram extraídos. |
| `dt_ingestao_lake` | TIMESTAMP | Data e hora do processamento e gravação do registro no Data Lake (AAAA-MM-DD HH:MM:SS). — descrição gerada por IA. |

## semantic · obt_rreo_siope_uf_ano

File `semantic__obt_rreo_siope_uf_ano.parquet` · 197,542 rows · 16 columns

RREO SIOPE UF/Estado — formato LONG/tidy, snapshot ANUAL (ultimo bimestre disponivel de cada ano, que e acumulado ate o bimestre). Grao: 1 linha por (codigo_uf, ano, codigo, posicao). Cada linha e um par (rubrica x metrica) da arvore do RREO. FORMATO LONG porque o RREO e uma arvore hierarquica viva: os codigos (1, 1.1, 1.1.1 ... ate ~52) entram e saem entre anos (ex: VAAT/VAAR so apos a nova lei do FUNDEB 2021), entao uma tabela WIDE quebraria a cada mudanca de layout. LONG absorve: nova rubrica = nova linha, sem mudar schema. Use nome_metrica para a metrica e descricao/codigo para a rubrica. Enriquecido com geografia IBGE. url_download_pdf aponta para o PDF-fonte no GCS. Origem: trusted_zone.rreo_siope_uf.

**Built from:** `semantic/obt_ibge_uf`, `trusted/rreo_siope_uf`

| Column | Type | Description |
|---|---|---|
| `codigo_uf` | INTEGER | Codigo IBGE 2 digitos da UF. FK para obt_ibge_uf. |
| `sigla_uf` | STRING | Sigla da UF (de obt_ibge_uf; fallback sg_uf da trusted). |
| `nome_uf` | STRING | Nome da UF (de obt_ibge_uf). |
| `nome_regiao` | STRING | Regiao geografica da UF (de obt_ibge_uf). |
| `ano` | INTEGER | Ano de referencia do RREO. |
| `bimestre` | INTEGER | Bimestre de referencia do snapshot anual (o ultimo disponivel do ano; valores sao acumulados ate o bimestre). |
| `secao` | INTEGER | Codigo raiz (INT64, 1..52) — agrupa o assunto: receitas, deducoes, FUNDEB, despesas MDE, restos a pagar, disponibilidade financeira. |
| `codigo` | STRING | Codigo hierarquico completo da rubrica no RREO (ex '6.3.1'). STRING. |
| `nivel` | INTEGER | Profundidade do codigo: 0=secao raiz, 1=X.Y, 2=X.Y.Z. |
| `descricao` | STRING | Rotulo textual da rubrica conforme o PDF do RREO. |
| `coluna` | STRING | Header cru da coluna de valor extraido do PDF (pode ter ruido de parse); NULL quando so posicional. Use nome_metrica. |
| `posicao` | INTEGER | Ordinal da coluna de valor dentro da rubrica (1..N). Sempre presente. |
| `nome_metrica` | STRING | Nome canonico da metrica: header observado quando capturado, senao default pelo perfil de colunas da secao (receita: Previsao/Realizada; despesa: Dotacao/Empenhada/Liquidada/Paga/RP; indicador: Exigido/Aplicado/%). |
| `valor` | FLOAT | Valor numerico (FLOAT64) da rubrica x metrica, em R$ (ou % para indicadores). |
| `arquivo` | STRING | Nome do PDF-fonte no FTP do FNDE. |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC de geracao desta tabela semantica. |

## semantic · obt_rreo_siope_uf_bimestre

File `semantic__obt_rreo_siope_uf_bimestre.parquet` · 725,870 rows · 17 columns

RREO SIOPE UF/Estado BIMESTRAL (LONG) - 1 linha por (codigo_uf, ano, bimestre, codigo, posicao). TODOS os bimestres, 27 UFs, 2010 em diante. Valores ACUMULADOS ate o bimestre, como o relatorio publica: permite a curva de execucao intra-ano e NAO deve ser somado entre bimestres. is_fechamento=TRUE marca o ultimo bimestre do ano (= snapshot da obt_rreo_siope_uf_ano). Origem: trusted_zone.rreo_siope_uf, com join por co_uf - a coluna sg_uf da trusted e nula em ~98% das linhas. Alimenta a tabela de entrega do RREO na aba de UF do dashboard 113 e a conferencia documental dos indicadores estaduais. ATENCAO: o RREO renumera secoes e desloca colunas entre exercicios, entao qualquer leitura de linha especifica deve ancorar pelo TEXTO da descricao, nunca pelo numero da secao ou pela letra da coluna.

**Built from:** `semantic/obt_ibge_uf`, `trusted/rreo_siope_uf`

**Feeds:** `semantic/obt_api_olinda_siope_indicadores_uf_ano`

| Column | Type | Description |
|---|---|---|
| `codigo_uf` | INTEGER | Código IBGE de dois dígitos correspondente à Unidade Federativa. — descrição gerada por IA. |
| `sigla_uf` | STRING | Sigla de duas letras do estado (ex: RO, SP). — descrição gerada por IA. |
| `nome_uf` | STRING | Nome completo da Unidade Federativa. — descrição gerada por IA. |
| `nome_regiao` | STRING | Nome da região geográfica do estado (ex: Norte, Sudeste). — descrição gerada por IA. |
| `ano` | INTEGER | Ano de exercício financeiro do relatório (formato AAAA). — descrição gerada por IA. |
| `bimestre` | INTEGER | Número do bimestre de referência das informações (1 a 6). — descrição gerada por IA. |
| `is_fechamento` | BOOLEAN | Indica se o registro se refere ao relatório final/fechamento do exercício (true/false). — descrição gerada por IA. |
| `secao` | INTEGER | Número ou identificador da seção do relatório RREO. — descrição gerada por IA. |
| `codigo` | STRING | Código da rubrica ou indicador orçamentário conforme o padrão SIOPE. — descrição gerada por IA. |
| `nivel` | INTEGER | Nível hierárquico da linha na estrutura do relatório (ex: 0 para consolidado, 1 para detalhamento). — descrição gerada por IA. |
| `descricao` | STRING | Descrição textual do indicador, despesa ou receita educacional. — descrição gerada por IA. |
| `coluna` | STRING | Nome do cabeçalho da coluna extraída do relatório original. — descrição gerada por IA. |
| `posicao` | INTEGER | Posição relativa do item na tabela original do documento. — descrição gerada por IA. |
| `nome_metrica` | STRING | Nome simplificado da métrica ou tipo de avaliação orçamentária. — descrição gerada por IA. |
| `valor` | FLOAT | Valor numérico (em reais ou percentual) apurado para a métrica e rubrica. — descrição gerada por IA. |
| `arquivo` | STRING | Nome do arquivo PDF original extraído do SIOPE. — descrição gerada por IA. |
| `dt_ingestao_lake` | TIMESTAMP | Data e hora do processamento e inclusão dos dados no Data Lake (AAAA-MM-DD HH:MM:SS). — descrição gerada por IA. |
