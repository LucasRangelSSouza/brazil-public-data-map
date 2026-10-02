# SAEB assessment (INEP): Raw and Trusted

Dataset: [lucasrangelss/saeb-raw-trusted-part-4](https://www.kaggle.com/datasets/lucasrangelss/saeb-raw-trusted-part-4) · snapshot 2026-10-01 · 38 tables · 5,526,123 rows

**Source:** Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP), [https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/saeb](https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/saeb)

SAEB results: aggregated proficiency indicators, the school report-card API (boletim) for 2011 onward, and the assessment microdata tables released without student-level records.

**Grain and keys:** Indicators: school, municipality, state or Brazil by edition. Boletim: school by edition. The publication format changes between editions, so each edition is validated against the live source.

**Layers.** `raw` is the source snapshot as delivered. `trusted` is typed, deduplicated and named consistently. `semantic` joins and reshapes trusted tables for analysis. Every table is a Parquet file named `<layer>__<table>.parquet` at the root of the dataset.

The full interactive map (lineage, joins, search) is at [https://rangeltech.net/datamap/](https://rangeltech.net/datamap/). Column descriptions come from the source lake's catalogue and are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns | Described | Upstream |
|---|---|---:|---:|---:|---|
| raw | [`inep_saeb_microdados_txt_2003_escola_03_txt`](#raw-inep-saeb-microdados-txt-2003-escola-03-txt) | 6,637 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_2003_mascara_txt`](#raw-inep-saeb-microdados-txt-2003-mascara-txt) | 356,880 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_2003_matematica_03ano_txt`](#raw-inep-saeb-microdados-txt-2003-matematica-03ano-txt) | 26,187 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_2003_matematica_04serie_txt`](#raw-inep-saeb-microdados-txt-2003-matematica-04serie-txt) | 46,131 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_2003_matematica_08serie_txt`](#raw-inep-saeb-microdados-txt-2003-matematica-08serie-txt) | 36,908 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_2003_portugues_03ano_txt`](#raw-inep-saeb-microdados-txt-2003-portugues-03ano-txt) | 26,219 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_2003_portugues_04serie_txt`](#raw-inep-saeb-microdados-txt-2003-portugues-04serie-txt) | 46,067 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_2003_portugues_08serie_txt`](#raw-inep-saeb-microdados-txt-2003-portugues-08serie-txt) | 37,009 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_2003_turma_03_txt`](#raw-inep-saeb-microdados-txt-2003-turma-03-txt) | 8,957 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_2005_diretor_05_txt`](#raw-inep-saeb-microdados-txt-2005-diretor-05-txt) | 4,851 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_2005_docente_05_txt`](#raw-inep-saeb-microdados-txt-2005-docente-05-txt) | 16,014 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_2005_escola_05_txt`](#raw-inep-saeb-microdados-txt-2005-escola-05-txt) | 4,851 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_2005_matematica_03ano_txt`](#raw-inep-saeb-microdados-txt-2005-matematica-03ano-txt) | 22,255 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_2005_matematica_04serie_txt`](#raw-inep-saeb-microdados-txt-2005-matematica-04serie-txt) | 41,783 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_2005_matematica_08serie_txt`](#raw-inep-saeb-microdados-txt-2005-matematica-08serie-txt) | 33,189 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_2005_portugues_03ano_txt`](#raw-inep-saeb-microdados-txt-2005-portugues-03ano-txt) | 22,285 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_2005_portugues_04serie_txt`](#raw-inep-saeb-microdados-txt-2005-portugues-04serie-txt) | 42,146 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_2005_portugues_08serie_txt`](#raw-inep-saeb-microdados-txt-2005-portugues-08serie-txt) | 33,164 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_2005_turma_05_txt`](#raw-inep-saeb-microdados-txt-2005-turma-05-txt) | 8,007 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_tabelas`](#raw-inep-saeb-microdados-txt-tabelas) | 68 | 13 | 13 | source |
| raw | [`inep_saeb_resultados_planilhas_linhas`](#raw-inep-saeb-resultados-planilhas-linhas) | 1,045,960 | 8 | 8 | source |
| raw | [`saeb_indicadores_brasil`](#raw-saeb-indicadores-brasil) | 453 | 178 | 178 | source |
| raw | [`saeb_indicadores_estados`](#raw-saeb-indicadores-estados) | 9,917 | 179 | 179 | source |
| raw | [`saeb_indicadores_historico_brasil`](#raw-saeb-indicadores-historico-brasil) | 24 | 84 | 84 | source |
| raw | [`saeb_indicadores_historico_estados`](#raw-saeb-indicadores-historico-estados) | 714 | 84 | 84 | source |
| raw | [`saeb_indicadores_municipios`](#raw-saeb-indicadores-municipios) | 540,927 | 115 | 115 | source |
| trusted | [`api_saeb_boletim_desempenho`](#trusted-api-saeb-boletim-desempenho) | 1,206,898 | 34 | 34 | `api_saeb_boletim_raw` |
| trusted | [`api_saeb_boletim_escola_edicao`](#trusted-api-saeb-boletim-escola-edicao) | 464,749 | 20 | 20 | `api_saeb_boletim_raw` |
| trusted | [`inep_saeb_escola`](#trusted-inep-saeb-escola) | 402,323 | 20 | 20 | `inep_saeb_microdados_csv_2013_ts_escola`, `inep_saeb_microdados_csv_2015_ts_escola`, `inep_saeb_microdados_csv_2017_ts_escola`, `inep_saeb_microdados_csv_2019_ts_escola` … |
| trusted | [`inep_saeb_indicadores_brasil`](#trusted-inep-saeb-indicadores-brasil) | 453 | 178 | 178 | `saeb_indicadores_brasil` |
| trusted | [`inep_saeb_indicadores_erros_amostrais`](#trusted-inep-saeb-indicadores-erros-amostrais) | 429 | 11 | 11 | source |
| trusted | [`inep_saeb_indicadores_estados`](#trusted-inep-saeb-indicadores-estados) | 9,917 | 179 | 179 | `saeb_indicadores_estados` |
| trusted | [`inep_saeb_indicadores_historico_brasil`](#trusted-inep-saeb-indicadores-historico-brasil) | 24 | 85 | 85 | `saeb_indicadores_historico_brasil` |
| trusted | [`inep_saeb_indicadores_historico_estados`](#trusted-inep-saeb-indicadores-historico-estados) | 714 | 85 | 85 | `saeb_indicadores_historico_estados` |
| trusted | [`inep_saeb_indicadores_municipios`](#trusted-inep-saeb-indicadores-municipios) | 540,927 | 115 | 115 | `saeb_indicadores_municipios` |
| trusted | [`inep_saeb_microdados_escola`](#trusted-inep-saeb-microdados-escola) | 461,283 | 28 | 28 | `inep_saeb_microdados_csv_2011_ts_quest_escola`, `inep_saeb_microdados_csv_2013_ts_escola`, `inep_saeb_microdados_csv_2015_ts_escola`, `inep_saeb_microdados_csv_2017_ts_escola` … |
| trusted | [`inep_saeb_microdados_item`](#trusted-inep-saeb-microdados-item) | 4,255 | 29 | 29 | `inep_saeb_microdados_csv_2011_ts_item`, `inep_saeb_microdados_csv_2013_ts_item`, `inep_saeb_microdados_csv_2015_ts_item`, `inep_saeb_microdados_csv_2019_ts_item` … |
| trusted | [`inep_saeb_secretario`](#trusted-inep-saeb-secretario) | 16,548 | 6 | 6 | `inep_saeb_microdados_csv_2019_ts_secretario_municipal`, `inep_saeb_microdados_csv_2021_ts_secretario_municipal`, `inep_saeb_microdados_csv_2023_ts_secretario_municipal` |

## raw · inep_saeb_microdados_txt_2003_escola_03_txt

File `raw__inep_saeb_microdados_txt_2003_escola_03_txt.parquet` · 6,637 rows · 1 columns

Raw de linhas TXT do microdado historico ESCOLA_03.TXT do Saeb 2003.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_2003_mascara_txt

File `raw__inep_saeb_microdados_txt_2003_mascara_txt.parquet` · 356,880 rows · 1 columns

Raw de linhas TXT do microdado historico MASCARA.TXT do Saeb 2003.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_2003_matematica_03ano_txt

File `raw__inep_saeb_microdados_txt_2003_matematica_03ano_txt.parquet` · 26,187 rows · 1 columns

Raw de linhas TXT do microdado historico MATEMATICA_03ANO.TXT do Saeb 2003.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_2003_matematica_04serie_txt

File `raw__inep_saeb_microdados_txt_2003_matematica_04serie_txt.parquet` · 46,131 rows · 1 columns

Raw de linhas TXT do microdado historico MATEMATICA_04SERIE.TXT do Saeb 2003.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_2003_matematica_08serie_txt

File `raw__inep_saeb_microdados_txt_2003_matematica_08serie_txt.parquet` · 36,908 rows · 1 columns

Raw de linhas TXT do microdado historico MATEMATICA_08SERIE.TXT do Saeb 2003.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_2003_portugues_03ano_txt

File `raw__inep_saeb_microdados_txt_2003_portugues_03ano_txt.parquet` · 26,219 rows · 1 columns

Raw de linhas TXT do microdado historico PORTUGUES_03ANO.TXT do Saeb 2003.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_2003_portugues_04serie_txt

File `raw__inep_saeb_microdados_txt_2003_portugues_04serie_txt.parquet` · 46,067 rows · 1 columns

Raw de linhas TXT do microdado historico PORTUGUES_04SERIE.TXT do Saeb 2003.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_2003_portugues_08serie_txt

File `raw__inep_saeb_microdados_txt_2003_portugues_08serie_txt.parquet` · 37,009 rows · 1 columns

Raw de linhas TXT do microdado historico PORTUGUES_08SERIE.TXT do Saeb 2003.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_2003_turma_03_txt

File `raw__inep_saeb_microdados_txt_2003_turma_03_txt.parquet` · 8,957 rows · 1 columns

Raw de linhas TXT do microdado historico TURMA_03.TXT do Saeb 2003.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_2005_diretor_05_txt

File `raw__inep_saeb_microdados_txt_2005_diretor_05_txt.parquet` · 4,851 rows · 1 columns

Raw de linhas TXT do microdado historico DIRETOR_05.TXT do Saeb 2005.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_2005_docente_05_txt

File `raw__inep_saeb_microdados_txt_2005_docente_05_txt.parquet` · 16,014 rows · 1 columns

Raw de linhas TXT do microdado historico DOCENTE_05.TXT do Saeb 2005.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_2005_escola_05_txt

File `raw__inep_saeb_microdados_txt_2005_escola_05_txt.parquet` · 4,851 rows · 1 columns

Raw de linhas TXT do microdado historico ESCOLA_05.TXT do Saeb 2005.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_2005_matematica_03ano_txt

File `raw__inep_saeb_microdados_txt_2005_matematica_03ano_txt.parquet` · 22,255 rows · 1 columns

Raw de linhas TXT do microdado historico MATEMATICA_03ANO.TXT do Saeb 2005.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_2005_matematica_04serie_txt

File `raw__inep_saeb_microdados_txt_2005_matematica_04serie_txt.parquet` · 41,783 rows · 1 columns

Raw de linhas TXT do microdado historico MATEMATICA_04SERIE.TXT do Saeb 2005.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_2005_matematica_08serie_txt

File `raw__inep_saeb_microdados_txt_2005_matematica_08serie_txt.parquet` · 33,189 rows · 1 columns

Raw de linhas TXT do microdado historico MATEMATICA_08SERIE.TXT do Saeb 2005.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_2005_portugues_03ano_txt

File `raw__inep_saeb_microdados_txt_2005_portugues_03ano_txt.parquet` · 22,285 rows · 1 columns

Raw de linhas TXT do microdado historico PORTUGUES_03ANO.TXT do Saeb 2005.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_2005_portugues_04serie_txt

File `raw__inep_saeb_microdados_txt_2005_portugues_04serie_txt.parquet` · 42,146 rows · 1 columns

Raw de linhas TXT do microdado historico PORTUGUES_04SERIE.TXT do Saeb 2005.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_2005_portugues_08serie_txt

File `raw__inep_saeb_microdados_txt_2005_portugues_08serie_txt.parquet` · 33,164 rows · 1 columns

Raw de linhas TXT do microdado historico PORTUGUES_08SERIE.TXT do Saeb 2005.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_2005_turma_05_txt

File `raw__inep_saeb_microdados_txt_2005_turma_05_txt.parquet` · 8,007 rows · 1 columns

Raw de linhas TXT do microdado historico TURMA_05.TXT do Saeb 2005.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_tabelas

File `raw__inep_saeb_microdados_txt_tabelas.parquet` · 68 rows · 13 columns

Catalogo das tabelas raw criadas a partir dos TXTs historicos de microdados do Saeb.

| Column | Type | Description |
|---|---|---|
| `ano` | INTEGER | Ano da edicao do Saeb. |
| `arquivo_zip` | STRING | Arquivo oficial ZIP de origem. |
| `nome_conteudo` | STRING | Nome do TXT de dados. |
| `membro_zip` | STRING | Caminho do TXT dentro do ZIP ou ZIP aninhado. |
| `familia` | STRING | Familia inferida do microdado. |
| `serie_arquivo` | STRING | Serie/etapa inferida pelo nome do arquivo. |
| `disciplina_arquivo` | STRING | Disciplina inferida pelo nome do arquivo. |
| `layout_sas` | STRING | Script SAS associado usado para localizar campos comuns, quando encontrado. |
| `posicoes_json` | STRING | Mapa JSON de posicoes comuns extraidas do layout SAS. |
| `qtd_linhas` | INTEGER | Quantidade total de registros contidos no arquivo e ingeridos na raw zone. — descrição gerada por IA. |
| `status_carga` | STRING | Estado do processamento da carga da tabela (ex: 'loaded', 'error'). — descrição gerada por IA. |
| `erro_carga` | STRING | Mensagem de erro de carga, quando houver. |
| `dt_ingestao_lake` | TIMESTAMP | Data/hora da carga no BigQuery. |

## raw · inep_saeb_resultados_planilhas_linhas

File `raw__inep_saeb_resultados_planilhas_linhas.parquet` · 1,045,960 rows · 8 columns

Raw das linhas das planilhas oficiais agregadas de resultados do Saeb, preservadas como JSON.

| Column | Type | Description |
|---|---|---|
| `ano` | INTEGER | Ano da edicao do Saeb associada ao arquivo oficial. |
| `arquivo` | STRING | Nome oficial do arquivo baixado. |
| `arquivo_local` | STRING | Nome local usado para evitar colisoes. |
| `nome_conteudo` | STRING | Nome do arquivo de planilha lido. |
| `aba` | STRING | Nome da aba da planilha. |
| `linha_planilha` | INTEGER | Numero sequencial da linha lida na aba, iniciando em 1 apos o cabecalho interpretado. |
| `dados_json` | STRING | Linha da planilha serializada em JSON, preservando colunas originais. |
| `dt_ingestao_lake` | TIMESTAMP | Data/hora da carga no BigQuery. |

## raw · saeb_indicadores_brasil

File `raw__saeb_indicadores_brasil.parquet` · 453 rows · 178 columns

SAEB Planilha de Resultados — nível nacional. Fonte: INEP.

**Feeds:** `trusted/inep_saeb_indicadores_brasil`

| Column | Type | Description |
|---|---|---|
| `ANO_SAEB` | STRING | Ano de realização da edição do SAEB (formato YYYY). |
| `ID` | STRING | Identificador único do usuário no sistema. |
| `DEPENDENCIA_ADM` | STRING | Dependência administrativa das escolas avaliadas (ex: Federal, Estadual, Municipal, Privada ou Total). |
| `LOCALIZACAO` | STRING | Localização geográfica das escolas (Urbana, Rural ou Total). |
| `CAPITAL` | STRING | Indicador de abrangência territorial em relação a capitais (Capital, Interior ou Total). |
| `TX_ALFABETIZADO` | STRING | Taxa de alfabetização calculada para o grupo avaliado (percentual). |
| `MEDIA_2_LP` | STRING | Nota média em Língua Portuguesa dos alunos do 2º ano do Ensino Fundamental. |
| `MEDIA_2_MT` | STRING | Nota média em Matemática dos alunos do 2º ano do Ensino Fundamental. |
| `PC_ALFABETIZADO` | STRING | Percentual de alunos considerados alfabetizados na avaliação. |
| `MEDIA_5_LP` | STRING | Nota média em Língua Portuguesa dos alunos do 5º ano do Ensino Fundamental. |
| `MEDIA_5_MT` | STRING | Nota média em Matemática dos alunos do 5º ano do Ensino Fundamental. |
| `MEDIA_5_CH` | STRING | Nota média em Ciências Humanas dos alunos do 5º ano do Ensino Fundamental. |
| `MEDIA_5_CN` | STRING | Nota média em Ciências da Natureza dos alunos do 5º ano do Ensino Fundamental. |
| `MEDIA_9_LP` | STRING | Nota média em Língua Portuguesa dos alunos do 9º ano do Ensino Fundamental. |
| `MEDIA_9_MT` | STRING | Nota média em Matemática dos alunos do 9º ano do Ensino Fundamental. |
| `MEDIA_9_CH` | STRING | Nota média em Ciências Humanas dos alunos do 9º ano do Ensino Fundamental. |
| `MEDIA_9_CN` | STRING | Nota média em Ciências da Natureza dos alunos do 9º ano do Ensino Fundamental. |
| `MEDIA_12_LP` | STRING | Nota média em Língua Portuguesa dos alunos da 3ª série do Ensino Médio (antigo 12º ano). |
| `MEDIA_12_MT` | STRING | Nota média em Matemática dos alunos da 3ª série do Ensino Médio (antigo 12º ano). |
| `MEDIA_13_LP` | STRING | Nota média em Língua Portuguesa dos alunos da 4ª série do Ensino Médio Integrado (antigo 13º ano). |
| `MEDIA_13_MT` | STRING | Nota média em Matemática dos alunos da 4ª série do Ensino Médio Integrado (antigo 13º ano). |
| `MEDIA_14_LP` | STRING | Nota média em Língua Portuguesa dos alunos do 14º ano/série (quando aplicável em programas específicos). |
| `MEDIA_14_MT` | STRING | Nota média em Matemática dos alunos do 14º ano/série (quando aplicável em programas específicos). |
| `nivel_0_LP2` | STRING | Percentual de alunos do 2º ano do EF no nível 0 de proficiência em Língua Portuguesa. |
| `nivel_1_LP2` | STRING | Percentual de alunos do 2º ano do EF no nível 1 de proficiência em Língua Portuguesa. |
| `nivel_2_LP2` | STRING | Percentual de alunos do 2º ano do EF no nível 2 de proficiência em Língua Portuguesa. |
| `nivel_3_LP2` | STRING | Percentual de alunos do 2º ano do EF no nível 3 de proficiência em Língua Portuguesa. |
| `nivel_4_LP2` | STRING | Percentual de alunos do 2º ano do EF no nível 4 de proficiência em Língua Portuguesa. |
| `nivel_5_LP2` | STRING | Percentual de alunos do 2º ano do EF no nível 5 de proficiência em Língua Portuguesa. |
| `nivel_6_LP2` | STRING | Percentual de alunos do 2º ano do EF no nível 6 de proficiência em Língua Portuguesa. |
| `nivel_7_LP2` | STRING | Percentual de alunos do 2º ano do EF no nível 7 de proficiência em Língua Portuguesa. |
| `nivel_8_LP2` | STRING | Percentual de alunos do 2º ano do EF no nível 8 de proficiência em Língua Portuguesa. |
| `nivel_0_MT2` | STRING | Percentual de alunos do 2º ano do EF no nível 0 de proficiência em Matemática. |
| `nivel_1_MT2` | STRING | Percentual de alunos do 2º ano do EF no nível 1 de proficiência em Matemática. |
| `nivel_2_MT2` | STRING | Percentual de alunos do 2º ano do EF no nível 2 de proficiência em Matemática. |
| `nivel_3_MT2` | STRING | Percentual de alunos do 2º ano do EF no nível 3 de proficiência em Matemática. |
| `nivel_4_MT2` | STRING | Percentual de alunos do 2º ano do EF no nível 4 de proficiência em Matemática. |
| `nivel_5_MT2` | STRING | Percentual de alunos do 2º ano do EF no nível 5 de proficiência em Matemática. |
| `nivel_6_MT2` | STRING | Percentual de alunos do 2º ano do EF no nível 6 de proficiência em Matemática. |
| `nivel_7_MT2` | STRING | Percentual de alunos do 2º ano do EF no nível 7 de proficiência em Matemática. |
| `nivel_8_MT2` | STRING | Percentual de alunos do 2º ano do EF no nível 8 de proficiência em Matemática. |
| `nivel_0_LP5` | STRING | Percentual de alunos do 5º ano do EF no nível 0 de proficiência em Língua Portuguesa. |
| `nivel_1_LP5` | STRING | Percentual de alunos do 5º ano do EF no nível 1 de proficiência em Língua Portuguesa. |
| `nivel_2_LP5` | STRING | Percentual de alunos do 5º ano do EF no nível 2 de proficiência em Língua Portuguesa. |
| `nivel_3_LP5` | STRING | Percentual de alunos do 5º ano do EF no nível 3 de proficiência em Língua Portuguesa. |
| `nivel_4_LP5` | STRING | Percentual de alunos do 5º ano do EF no nível 4 de proficiência em Língua Portuguesa. |
| `nivel_5_LP5` | STRING | Percentual de alunos do 5º ano do EF no nível 5 de proficiência em Língua Portuguesa. |
| `nivel_6_LP5` | STRING | Percentual de alunos do 5º ano do EF no nível 6 de proficiência em Língua Portuguesa. |
| `nivel_7_LP5` | STRING | Percentual de alunos do 5º ano do EF no nível 7 de proficiência em Língua Portuguesa. |
| `nivel_8_LP5` | STRING | Percentual de alunos do 5º ano do EF no nível 8 de proficiência em Língua Portuguesa. |
| `nivel_9_LP5` | STRING | Percentual de alunos do 5º ano do EF no nível 9 de proficiência em Língua Portuguesa. |
| `nivel_0_MT5` | STRING | Percentual de alunos do 5º ano do EF no nível 0 de proficiência em Matemática. |
| `nivel_1_MT5` | STRING | Percentual de alunos do 5º ano do EF no nível 1 de proficiência em Matemática. |
| `nivel_2_MT5` | STRING | Percentual de alunos do 5º ano do EF no nível 2 de proficiência em Matemática. |
| `nivel_3_MT5` | STRING | Percentual de alunos do 5º ano do EF no nível 3 de proficiência em Matemática. |
| `nivel_4_MT5` | STRING | Percentual de alunos do 5º ano do EF no nível 4 de proficiência em Matemática. |
| `nivel_5_MT5` | STRING | Percentual de alunos do 5º ano do EF no nível 5 de proficiência em Matemática. |
| `nivel_6_MT5` | STRING | Percentual de alunos do 5º ano do EF no nível 6 de proficiência em Matemática. |
| `nivel_7_MT5` | STRING | Percentual de alunos do 5º ano do EF no nível 7 de proficiência em Matemática. |
| `nivel_8_MT5` | STRING | Percentual de alunos do 5º ano do EF no nível 8 de proficiência em Matemática. |
| `nivel_9_MT5` | STRING | Percentual de alunos do 5º ano do EF no nível 9 de proficiência em Matemática. |
| `nivel_10_MT5` | STRING | Percentual de alunos do 5º ano do EF no nível 10 de proficiência em Matemática. |
| `nivel_0_CH5` | STRING | Percentual de alunos do 5º ano do EF no nível 0 de proficiência em Ciências Humanas. |
| `nivel_1_CH5` | STRING | Percentual de alunos do 5º ano do EF no nível 1 de proficiência em Ciências Humanas. |
| `nivel_2_CH5` | STRING | Percentual de alunos do 5º ano do EF no nível 2 de proficiência em Ciências Humanas. |
| `nivel_3_CH5` | STRING | Percentual de alunos do 5º ano do EF no nível 3 de proficiência em Ciências Humanas. |
| `nivel_4_CH5` | STRING | Percentual de alunos do 5º ano do EF no nível 4 de proficiência em Ciências Humanas. |
| `nivel_5_CH5` | STRING | Percentual de alunos do 5º ano do EF no nível 5 de proficiência em Ciências Humanas. |
| `nivel_6_CH5` | STRING | Percentual de alunos do 5º ano do EF no nível 6 de proficiência em Ciências Humanas. |
| `nivel_7_CH5` | STRING | Percentual de alunos do 5º ano do EF no nível 7 de proficiência em Ciências Humanas. |
| `nivel_0_CN5` | STRING | Percentual de alunos do 5º ano do EF no nível 0 de proficiência em Ciências da Natureza. |
| `nivel_1_CN5` | STRING | Percentual de alunos do 5º ano do EF no nível 1 de proficiência em Ciências da Natureza. |
| `nivel_2_CN5` | STRING | Percentual de alunos do 5º ano do EF no nível 2 de proficiência em Ciências da Natureza. |
| `nivel_3_CN5` | STRING | Percentual de alunos do 5º ano do EF no nível 3 de proficiência em Ciências da Natureza. |
| `nivel_4_CN5` | STRING | Percentual de alunos do 5º ano do EF no nível 4 de proficiência em Ciências da Natureza. |
| `nivel_5_CN5` | STRING | Percentual de alunos do 5º ano do EF no nível 5 de proficiência em Ciências da Natureza. |
| `nivel_6_CN5` | STRING | Percentual de alunos do 5º ano do EF no nível 6 de proficiência em Ciências da Natureza. |
| `nivel_7_CN5` | STRING | Percentual de alunos do 5º ano do EF no nível 7 de proficiência em Ciências da Natureza. |
| `nivel_8_CN5` | STRING | Percentual de alunos do 5º ano do EF no nível 8 de proficiência em Ciências da Natureza. |
| `nivel_0_LP9` | STRING | Percentual de alunos do 9º ano do EF no nível 0 de proficiência em Língua Portuguesa. |
| `nivel_1_LP9` | STRING | Percentual de alunos do 9º ano do EF no nível 1 de proficiência em Língua Portuguesa. |
| `nivel_2_LP9` | STRING | Percentual de alunos do 9º ano do EF no nível 2 de proficiência em Língua Portuguesa. |
| `nivel_3_LP9` | STRING | Percentual de alunos do 9º ano do EF no nível 3 de proficiência em Língua Portuguesa. |
| `nivel_4_LP9` | STRING | Percentual de alunos do 9º ano do EF no nível 4 de proficiência em Língua Portuguesa. |
| `nivel_5_LP9` | STRING | Percentual de alunos do 9º ano do EF no nível 5 de proficiência em Língua Portuguesa. |
| `nivel_6_LP9` | STRING | Percentual de alunos do 9º ano do EF no nível 6 de proficiência em Língua Portuguesa. |
| `nivel_7_LP9` | STRING | Percentual de alunos do 9º ano do EF no nível 7 de proficiência em Língua Portuguesa. |
| `nivel_8_LP9` | STRING | Percentual de alunos do 9º ano do EF no nível 8 de proficiência em Língua Portuguesa. |
| `nivel_0_MT9` | STRING | Percentual de alunos do 9º ano do EF no nível 0 de proficiência em Matemática. |
| `nivel_1_MT9` | STRING | Percentual de alunos do 9º ano do EF no nível 1 de proficiência em Matemática. |
| `nivel_2_MT9` | STRING | Percentual de alunos do 9º ano do EF no nível 2 de proficiência em Matemática. |
| `nivel_3_MT9` | STRING | Percentual de alunos do 9º ano do EF no nível 3 de proficiência em Matemática. |
| `nivel_4_MT9` | STRING | Percentual de alunos do 9º ano do EF no nível 4 de proficiência em Matemática. |
| `nivel_5_MT9` | STRING | Percentual de alunos do 9º ano do EF no nível 5 de proficiência em Matemática. |
| `nivel_6_MT9` | STRING | Percentual de alunos do 9º ano do EF no nível 6 de proficiência em Matemática. |
| `nivel_7_MT9` | STRING | Percentual de alunos do 9º ano do EF no nível 7 de proficiência em Matemática. |
| `nivel_8_MT9` | STRING | Percentual de alunos do 9º ano do EF no nível 8 de proficiência em Matemática. |
| `nivel_9_MT9` | STRING | Percentual de alunos do 9º ano do EF no nível 9 de proficiência em Matemática. |
| `nivel_0_CH9` | STRING | Percentual de alunos do 9º ano do EF no nível 0 de proficiência em Ciências Humanas. |
| `nivel_1_CH9` | STRING | Percentual de alunos do 9º ano do EF no nível 1 de proficiência em Ciências Humanas. |
| `nivel_2_CH9` | STRING | Percentual de alunos do 9º ano do EF no nível 2 de proficiência em Ciências Humanas. |
| `nivel_3_CH9` | STRING | Percentual de alunos do 9º ano do EF no nível 3 de proficiência em Ciências Humanas. |
| `nivel_4_CH9` | STRING | Percentual de alunos do 9º ano do EF no nível 4 de proficiência em Ciências Humanas. |
| `nivel_5_CH9` | STRING | Percentual de alunos do 9º ano do EF no nível 5 de proficiência em Ciências Humanas. |
| `nivel_6_CH9` | STRING | Percentual de alunos do 9º ano do EF no nível 6 de proficiência em Ciências Humanas. |
| `nivel_7_CH9` | STRING | Percentual de alunos do 9º ano do EF no nível 7 de proficiência em Ciências Humanas. |
| `nivel_8_CH9` | STRING | Percentual de alunos do 9º ano do EF no nível 8 de proficiência em Ciências Humanas. |
| `nivel_9_CH9` | STRING | Percentual de alunos do 9º ano do EF no nível 9 de proficiência em Ciências Humanas. |
| `nivel_0_CN9` | STRING | Percentual de alunos do 9º ano do EF no nível 0 de proficiência em Ciências da Natureza. |
| `nivel_1_CN9` | STRING | Percentual de alunos do 9º ano do EF no nível 1 de proficiência em Ciências da Natureza. |
| `nivel_2_CN9` | STRING | Percentual de alunos do 9º ano do EF no nível 2 de proficiência em Ciências da Natureza. |
| `nivel_3_CN9` | STRING | Percentual de alunos do 9º ano do EF no nível 3 de proficiência em Ciências da Natureza. |
| `nivel_4_CN9` | STRING | Percentual de alunos do 9º ano do EF no nível 4 de proficiência em Ciências da Natureza. |
| `nivel_5_CN9` | STRING | Percentual de alunos do 9º ano do EF no nível 5 de proficiência em Ciências da Natureza. |
| `nivel_6_CN9` | STRING | Percentual de alunos do 9º ano do EF no nível 6 de proficiência em Ciências da Natureza. |
| `nivel_7_CN9` | STRING | Percentual de alunos do 9º ano do EF no nível 7 de proficiência em Ciências da Natureza. |
| `nivel_8_CN9` | STRING | Percentual de alunos do 9º ano do EF no nível 8 de proficiência em Ciências da Natureza. |
| `nivel_0_LP12` | STRING | Percentual de alunos da 3ª série do EM no nível 0 de proficiência em Língua Portuguesa. |
| `nivel_1_LP12` | STRING | Percentual de alunos da 3ª série do EM no nível 1 de proficiência em Língua Portuguesa. |
| `nivel_2_LP12` | STRING | Percentual de alunos da 3ª série do EM no nível 2 de proficiência em Língua Portuguesa. |
| `nivel_3_LP12` | STRING | Percentual de alunos da 3ª série do EM no nível 3 de proficiência em Língua Portuguesa. |
| `nivel_4_LP12` | STRING | Percentual de alunos da 3ª série do EM no nível 4 de proficiência em Língua Portuguesa. |
| `nivel_5_LP12` | STRING | Percentual de alunos da 3ª série do EM no nível 5 de proficiência em Língua Portuguesa. |
| `nivel_6_LP12` | STRING | Percentual de alunos da 3ª série do EM no nível 6 de proficiência em Língua Portuguesa. |
| `nivel_7_LP12` | STRING | Percentual de alunos da 3ª série do EM no nível 7 de proficiência em Língua Portuguesa. |
| `nivel_8_LP12` | STRING | Percentual de alunos da 3ª série do EM no nível 8 de proficiência em Língua Portuguesa. |
| `nivel_0_MT12` | STRING | Percentual de alunos da 3ª série do EM no nível 0 de proficiência em Matemática. |
| `nivel_1_MT12` | STRING | Percentual de alunos da 3ª série do EM no nível 1 de proficiência em Matemática. |
| `nivel_2_MT12` | STRING | Percentual de alunos da 3ª série do EM no nível 2 de proficiência em Matemática. |
| `nivel_3_MT12` | STRING | Percentual de alunos da 3ª série do EM no nível 3 de proficiência em Matemática. |
| `nivel_4_MT12` | STRING | Percentual de alunos da 3ª série do EM no nível 4 de proficiência em Matemática. |
| `nivel_5_MT12` | STRING | Percentual de alunos da 3ª série do EM no nível 5 de proficiência em Matemática. |
| `nivel_6_MT12` | STRING | Percentual de alunos da 3ª série do EM no nível 6 de proficiência em Matemática. |
| `nivel_7_MT12` | STRING | Percentual de alunos da 3ª série do EM no nível 7 de proficiência em Matemática. |
| `nivel_8_MT12` | STRING | Percentual de alunos da 3ª série do EM no nível 8 de proficiência em Matemática. |
| `nivel_9_MT12` | STRING | Percentual de alunos da 3ª série do EM no nível 9 de proficiência em Matemática. |
| `nivel_10_MT12` | STRING | Percentual de alunos da 3ª série do EM no nível 10 de proficiência em Matemática. |
| `nivel_0_LP13` | STRING | Percentual de alunos da 4ª série do EM no nível 0 de proficiência em Língua Portuguesa. |
| `nivel_1_LP13` | STRING | Percentual de alunos da 4ª série do EM no nível 1 de proficiência em Língua Portuguesa. |
| `nivel_2_LP13` | STRING | Percentual de alunos da 4ª série do EM no nível 2 de proficiência em Língua Portuguesa. |
| `nivel_3_LP13` | STRING | Percentual de alunos da 4ª série do EM no nível 3 de proficiência em Língua Portuguesa. |
| `nivel_4_LP13` | STRING | Percentual de alunos da 4ª série do EM no nível 4 de proficiência em Língua Portuguesa. |
| `nivel_5_LP13` | STRING | Percentual de alunos da 4ª série do EM no nível 5 de proficiência em Língua Portuguesa. |
| `nivel_6_LP13` | STRING | Percentual de alunos da 4ª série do EM no nível 6 de proficiência em Língua Portuguesa. |
| `nivel_7_LP13` | STRING | Percentual de alunos da 4ª série do EM no nível 7 de proficiência em Língua Portuguesa. |
| `nivel_8_LP13` | STRING | Percentual de alunos da 4ª série do EM no nível 8 de proficiência em Língua Portuguesa. |
| `nivel_0_MT13` | STRING | Percentual de alunos da 4ª série do EM no nível 0 de proficiência em Matemática. |
| `nivel_1_MT13` | STRING | Percentual de alunos da 4ª série do EM no nível 1 de proficiência em Matemática. |
| `nivel_2_MT13` | STRING | Percentual de alunos da 4ª série do EM no nível 2 de proficiência em Matemática. |
| `nivel_3_MT13` | STRING | Percentual de alunos da 4ª série do EM no nível 3 de proficiência em Matemática. |
| `nivel_4_MT13` | STRING | Percentual de alunos da 4ª série do EM no nível 4 de proficiência em Matemática. |
| `nivel_5_MT13` | STRING | Percentual de alunos da 4ª série do EM no nível 5 de proficiência em Matemática. |
| `nivel_6_MT13` | STRING | Percentual de alunos da 4ª série do EM no nível 6 de proficiência em Matemática. |
| `nivel_7_MT13` | STRING | Percentual de alunos da 4ª série do EM no nível 7 de proficiência em Matemática. |
| `nivel_8_MT13` | STRING | Percentual de alunos da 4ª série do EM no nível 8 de proficiência em Matemática. |
| `nivel_9_MT13` | STRING | Percentual de alunos da 4ª série do EM no nível 9 de proficiência em Matemática. |
| `nivel_10_MT13` | STRING | Percentual de alunos da 4ª série do EM no nível 10 de proficiência em Matemática. |
| `nivel_0_LP14` | STRING | Percentual de alunos do 14º ano/série no nível 0 de proficiência em Língua Portuguesa. |
| `nivel_1_LP14` | STRING | Percentual de alunos do 14º ano/série no nível 1 de proficiência em Língua Portuguesa. |
| `nivel_2_LP14` | STRING | Percentual de alunos do 14º ano/série no nível 2 de proficiência em Língua Portuguesa. |
| `nivel_3_LP14` | STRING | Percentual de alunos do 14º ano/série no nível 3 de proficiência em Língua Portuguesa. |
| `nivel_4_LP14` | STRING | Percentual de alunos do 14º ano/série no nível 4 de proficiência em Língua Portuguesa. |
| `nivel_5_LP14` | STRING | Percentual de alunos do 14º ano/série no nível 5 de proficiência em Língua Portuguesa. |
| `nivel_6_LP14` | STRING | Percentual de alunos do 14º ano/série no nível 6 de proficiência em Língua Portuguesa. |
| `nivel_7_LP14` | STRING | Percentual de alunos do 14º ano/série no nível 7 de proficiência em Língua Portuguesa. |
| `nivel_8_LP14` | STRING | Percentual de alunos do 14º ano/série no nível 8 de proficiência em Língua Portuguesa. |
| `nivel_0_MT14` | STRING | Percentual de alunos do 14º ano/série no nível 0 de proficiência em Matemática. |
| `nivel_1_MT14` | STRING | Percentual de alunos do 14º ano/série no nível 1 de proficiência em Matemática. |
| `nivel_2_MT14` | STRING | Percentual de alunos do 14º ano/série no nível 2 de proficiência em Matemática. |
| `nivel_3_MT14` | STRING | Percentual de alunos do 14º ano/série no nível 3 de proficiência em Matemática. |
| `nivel_4_MT14` | STRING | Percentual de alunos do 14º ano/série no nível 4 de proficiência em Matemática. |
| `nivel_5_MT14` | STRING | Percentual de alunos do 14º ano/série no nível 5 de proficiência em Matemática. |
| `nivel_6_MT14` | STRING | Percentual de alunos do 14º ano/série no nível 6 de proficiência em Matemática. |
| `nivel_7_MT14` | STRING | Percentual de alunos do 14º ano/série no nível 7 de proficiência em Matemática. |
| `nivel_8_MT14` | STRING | Percentual de alunos do 14º ano/série no nível 8 de proficiência em Matemática. |
| `nivel_9_MT14` | STRING | Percentual de alunos do 14º ano/série no nível 9 de proficiência em Matemática. |
| `nivel_10_MT14` | STRING | Percentual de alunos do 14º ano/série no nível 10 de proficiência em Matemática. |
| `dt_ingestao_lake` | TIMESTAMP | Data e hora do carregamento ou atualização do registro na camada do Data Lake. Formato: Timestamp. — descrição gerada por IA. |

## raw · saeb_indicadores_estados

File `raw__saeb_indicadores_estados.parquet` · 9,917 rows · 179 columns

SAEB Planilha de Resultados — nível estadual (UF). Fonte: INEP.

**Feeds:** `trusted/inep_saeb_indicadores_estados`

| Column | Type | Description |
|---|---|---|
| `ANO_SAEB` | STRING | Ano de realização da edição do exame SAEB. |
| `CO_UF` | STRING | Código numérico do IBGE correspondente à Unidade da Federação. |
| `NO_UF` | STRING | Nome da Unidade da Federação. |
| `DEPENDENCIA_ADM` | STRING | Dependência administrativa das escolas avaliadas (ex: Federal, Estadual, Municipal, Privada ou Total). |
| `LOCALIZACAO` | STRING | Localização geográfica das escolas (Urbana, Rural ou Total). |
| `CAPITAL` | STRING | Indicador se os dados são restritos à capital do estado (Sim/Não/Nulo). |
| `TX_ALFABETIZADO` | STRING | Taxa de alfabetização dos alunos avaliados (percentual). |
| `MEDIA_2_LP` | STRING | Média de proficiência em Língua Portuguesa dos alunos do 2º ano do Ensino Fundamental. |
| `MEDIA_2_MT` | STRING | Média de proficiência em Matemática dos alunos do 2º ano do Ensino Fundamental. |
| `PC_ALFABETIZADO` | STRING | Percentual de alunos classificados como alfabetizados. |
| `MEDIA_5_LP` | STRING | Média de proficiência em Língua Portuguesa dos alunos do 5º ano do Ensino Fundamental. |
| `MEDIA_5_MT` | STRING | Média de proficiência em Matemática dos alunos do 5º ano do Ensino Fundamental. |
| `MEDIA_5_CH` | STRING | Média de proficiência em Ciências Humanas dos alunos do 5º ano do Ensino Fundamental. |
| `MEDIA_5_CN` | STRING | Média de proficiência em Ciências da Natureza dos alunos do 5º ano do Ensino Fundamental. |
| `MEDIA_9_LP` | STRING | Média de proficiência em Língua Portuguesa dos alunos do 9º ano do Ensino Fundamental. |
| `MEDIA_9_MT` | STRING | Média de proficiência em Matemática dos alunos do 9º ano do Ensino Fundamental. |
| `MEDIA_9_CH` | STRING | Média de proficiência em Ciências Humanas dos alunos do 9º ano do Ensino Fundamental. |
| `MEDIA_9_CN` | STRING | Média de proficiência em Ciências da Natureza dos alunos do 9º ano do Ensino Fundamental. |
| `MEDIA_12_LP` | STRING | Média de proficiência em Língua Portuguesa dos alunos do 3º ano do Ensino Médio (Série 12). |
| `MEDIA_12_MT` | STRING | Média de proficiência em Matemática dos alunos do 3º ano do Ensino Médio (Série 12). |
| `MEDIA_13_LP` | STRING | Média de proficiência em Língua Portuguesa dos alunos do 4º ano do Ensino Médio/Técnico (Série 13). |
| `MEDIA_13_MT` | STRING | Média de proficiência em Matemática dos alunos do 4º ano do Ensino Médio/Técnico (Série 13). |
| `MEDIA_14_LP` | STRING | Média de proficiência em Língua Portuguesa dos alunos da Série 14. |
| `MEDIA_14_MT` | STRING | Média de proficiência em Matemática dos alunos da Série 14. |
| `nivel_0_LP2` | STRING | Percentual de alunos do 2º ano do Ensino Fundamental no nível 0 de proficiência em Língua Portuguesa. |
| `nivel_1_LP2` | STRING | Percentual de alunos do 2º ano do Ensino Fundamental no nível 1 de proficiência em Língua Portuguesa. |
| `nivel_2_LP2` | STRING | Percentual de alunos do 2º ano do Ensino Fundamental no nível 2 de proficiência em Língua Portuguesa. |
| `nivel_3_LP2` | STRING | Percentual de alunos do 2º ano do Ensino Fundamental no nível 3 de proficiência em Língua Portuguesa. |
| `nivel_4_LP2` | STRING | Percentual de alunos do 2º ano do Ensino Fundamental no nível 4 de proficiência em Língua Portuguesa. |
| `nivel_5_LP2` | STRING | Percentual de alunos do 2º ano do Ensino Fundamental no nível 5 de proficiência em Língua Portuguesa. |
| `nivel_6_LP2` | STRING | Percentual de alunos do 2º ano do Ensino Fundamental no nível 6 de proficiência em Língua Portuguesa. |
| `nivel_7_LP2` | STRING | Percentual de alunos do 2º ano do Ensino Fundamental no nível 7 de proficiência em Língua Portuguesa. |
| `nivel_8_LP2` | STRING | Percentual de alunos do 2º ano do Ensino Fundamental no nível 8 de proficiência em Língua Portuguesa. |
| `nivel_0_MT2` | STRING | Percentual de alunos do 2º ano do Ensino Fundamental no nível 0 de proficiência em Matemática. |
| `nivel_1_MT2` | STRING | Percentual de alunos do 2º ano do Ensino Fundamental no nível 1 de proficiência em Matemática. |
| `nivel_2_MT2` | STRING | Percentual de alunos do 2º ano do Ensino Fundamental no nível 2 de proficiência em Matemática. |
| `nivel_3_MT2` | STRING | Percentual de alunos do 2º ano do Ensino Fundamental no nível 3 de proficiência em Matemática. |
| `nivel_4_MT2` | STRING | Percentual de alunos do 2º ano do Ensino Fundamental no nível 4 de proficiência em Matemática. |
| `nivel_5_MT2` | STRING | Percentual de alunos do 2º ano do Ensino Fundamental no nível 5 de proficiência em Matemática. |
| `nivel_6_MT2` | STRING | Percentual de alunos do 2º ano do Ensino Fundamental no nível 6 de proficiência em Matemática. |
| `nivel_7_MT2` | STRING | Percentual de alunos do 2º ano do Ensino Fundamental no nível 7 de proficiência em Matemática. |
| `nivel_8_MT2` | STRING | Percentual de alunos do 2º ano do Ensino Fundamental no nível 8 de proficiência em Matemática. |
| `nivel_0_LP5` | STRING | Percentual de alunos do 5º ano do Ensino Fundamental no nível 0 de proficiência em Língua Portuguesa. |
| `nivel_1_LP5` | STRING | Percentual de alunos do 5º ano do Ensino Fundamental no nível 1 de proficiência em Língua Portuguesa. |
| `nivel_2_LP5` | STRING | Percentual de alunos do 5º ano do Ensino Fundamental no nível 2 de proficiência em Língua Portuguesa. |
| `nivel_3_LP5` | STRING | Percentual de alunos do 5º ano do Ensino Fundamental no nível 3 de proficiência em Língua Portuguesa. |
| `nivel_4_LP5` | STRING | Percentual de alunos do 5º ano do Ensino Fundamental no nível 4 de proficiência em Língua Portuguesa. |
| `nivel_5_LP5` | STRING | Percentual de alunos do 5º ano do Ensino Fundamental no nível 5 de proficiência em Língua Portuguesa. |
| `nivel_6_LP5` | STRING | Percentual de alunos do 5º ano do Ensino Fundamental no nível 6 de proficiência em Língua Portuguesa. |
| `nivel_7_LP5` | STRING | Percentual de alunos do 5º ano do Ensino Fundamental no nível 7 de proficiência em Língua Portuguesa. |
| `nivel_8_LP5` | STRING | Percentual de alunos do 5º ano do Ensino Fundamental no nível 8 de proficiência em Língua Portuguesa. |
| `nivel_9_LP5` | STRING | Percentual de alunos do 5º ano do Ensino Fundamental no nível 9 de proficiência em Língua Portuguesa. |
| `nivel_0_MT5` | STRING | Percentual de alunos do 5º ano do Ensino Fundamental no nível 0 de proficiência em Matemática. |
| `nivel_1_MT5` | STRING | Percentual de alunos do 5º ano do Ensino Fundamental no nível 1 de proficiência em Matemática. |
| `nivel_2_MT5` | STRING | Percentual de alunos do 5º ano do Ensino Fundamental no nível 2 de proficiência em Matemática. |
| `nivel_3_MT5` | STRING | Percentual de alunos do 5º ano do Ensino Fundamental no nível 3 de proficiência em Matemática. |
| `nivel_4_MT5` | STRING | Percentual de alunos do 5º ano do Ensino Fundamental no nível 4 de proficiência em Matemática. |
| `nivel_5_MT5` | STRING | Percentual de alunos do 5º ano do Ensino Fundamental no nível 5 de proficiência em Matemática. |
| `nivel_6_MT5` | STRING | Percentual de alunos do 5º ano do Ensino Fundamental no nível 6 de proficiência em Matemática. |
| `nivel_7_MT5` | STRING | Percentual de alunos do 5º ano do Ensino Fundamental no nível 7 de proficiência em Matemática. |
| `nivel_8_MT5` | STRING | Percentual de alunos do 5º ano do Ensino Fundamental no nível 8 de proficiência em Matemática. |
| `nivel_9_MT5` | STRING | Percentual de alunos do 5º ano do Ensino Fundamental no nível 9 de proficiência em Matemática. |
| `nivel_10_MT5` | STRING | Percentual de alunos do 5º ano do Ensino Fundamental no nível 10 de proficiência em Matemática. |
| `nivel_0_CH5` | STRING | Percentual de alunos do 5º ano do Ensino Fundamental no nível 0 de proficiência em Ciências Humanas. |
| `nivel_1_CH5` | STRING | Percentual de alunos do 5º ano do Ensino Fundamental no nível 1 de proficiência em Ciências Humanas. |
| `nivel_2_CH5` | STRING | Percentual de alunos do 5º ano do Ensino Fundamental no nível 2 de proficiência em Ciências Humanas. |
| `nivel_3_CH5` | STRING | Percentual de alunos do 5º ano do Ensino Fundamental no nível 3 de proficiência em Ciências Humanas. |
| `nivel_4_CH5` | STRING | Percentual de alunos do 5º ano do Ensino Fundamental no nível 4 de proficiência em Ciências Humanas. |
| `nivel_5_CH5` | STRING | Percentual de alunos do 5º ano do Ensino Fundamental no nível 5 de proficiência em Ciências Humanas. |
| `nivel_6_CH5` | STRING | Percentual de alunos do 5º ano do Ensino Fundamental no nível 6 de proficiência em Ciências Humanas. |
| `nivel_7_CH5` | STRING | Percentual de alunos do 5º ano do Ensino Fundamental no nível 7 de proficiência em Ciências Humanas. |
| `nivel_0_CN5` | STRING | Percentual de alunos do 5º ano do Ensino Fundamental no nível 0 de proficiência em Ciências da Natureza. |
| `nivel_1_CN5` | STRING | Percentual de alunos do 5º ano do Ensino Fundamental no nível 1 de proficiência em Ciências da Natureza. |
| `nivel_2_CN5` | STRING | Percentual de alunos do 5º ano do Ensino Fundamental no nível 2 de proficiência em Ciências da Natureza. |
| `nivel_3_CN5` | STRING | Percentual de alunos do 5º ano do Ensino Fundamental no nível 3 de proficiência em Ciências da Natureza. |
| `nivel_4_CN5` | STRING | Percentual de alunos do 5º ano do Ensino Fundamental no nível 4 de proficiência em Ciências da Natureza. |
| `nivel_5_CN5` | STRING | Percentual de alunos do 5º ano do Ensino Fundamental no nível 5 de proficiência em Ciências da Natureza. |
| `nivel_6_CN5` | STRING | Percentual de alunos do 5º ano do Ensino Fundamental no nível 6 de proficiência em Ciências da Natureza. |
| `nivel_7_CN5` | STRING | Percentual de alunos do 5º ano do Ensino Fundamental no nível 7 de proficiência em Ciências da Natureza. |
| `nivel_8_CN5` | STRING | Percentual de alunos do 5º ano do Ensino Fundamental no nível 8 de proficiência em Ciências da Natureza. |
| `nivel_0_LP9` | STRING | Percentual de alunos do 9º ano do Ensino Fundamental no nível 0 de proficiência em Língua Portuguesa. |
| `nivel_1_LP9` | STRING | Percentual de alunos do 9º ano do Ensino Fundamental no nível 1 de proficiência em Língua Portuguesa. |
| `nivel_2_LP9` | STRING | Percentual de alunos do 9º ano do Ensino Fundamental no nível 2 de proficiência em Língua Portuguesa. |
| `nivel_3_LP9` | STRING | Percentual de alunos do 9º ano do Ensino Fundamental no nível 3 de proficiência em Língua Portuguesa. |
| `nivel_4_LP9` | STRING | Percentual de alunos do 9º ano do Ensino Fundamental no nível 4 de proficiência em Língua Portuguesa. |
| `nivel_5_LP9` | STRING | Percentual de alunos do 9º ano do Ensino Fundamental no nível 5 de proficiência em Língua Portuguesa. |
| `nivel_6_LP9` | STRING | Percentual de alunos do 9º ano do Ensino Fundamental no nível 6 de proficiência em Língua Portuguesa. |
| `nivel_7_LP9` | STRING | Percentual de alunos do 9º ano do Ensino Fundamental no nível 7 de proficiência em Língua Portuguesa. |
| `nivel_8_LP9` | STRING | Percentual de alunos do 9º ano do Ensino Fundamental no nível 8 de proficiência em Língua Portuguesa. |
| `nivel_0_MT9` | STRING | Percentual de alunos do 9º ano do Ensino Fundamental no nível 0 de proficiência em Matemática. |
| `nivel_1_MT9` | STRING | Percentual de alunos do 9º ano do Ensino Fundamental no nível 1 de proficiência em Matemática. |
| `nivel_2_MT9` | STRING | Percentual de alunos do 9º ano do Ensino Fundamental no nível 2 de proficiência em Matemática. |
| `nivel_3_MT9` | STRING | Percentual de alunos do 9º ano do Ensino Fundamental no nível 3 de proficiência em Matemática. |
| `nivel_4_MT9` | STRING | Percentual de alunos do 9º ano do Ensino Fundamental no nível 4 de proficiência em Matemática. |
| `nivel_5_MT9` | STRING | Percentual de alunos do 9º ano do Ensino Fundamental no nível 5 de proficiência em Matemática. |
| `nivel_6_MT9` | STRING | Percentual de alunos do 9º ano do Ensino Fundamental no nível 6 de proficiência em Matemática. |
| `nivel_7_MT9` | STRING | Percentual de alunos do 9º ano do Ensino Fundamental no nível 7 de proficiência em Matemática. |
| `nivel_8_MT9` | STRING | Percentual de alunos do 9º ano do Ensino Fundamental no nível 8 de proficiência em Matemática. |
| `nivel_9_MT9` | STRING | Percentual de alunos do 9º ano do Ensino Fundamental no nível 9 de proficiência em Matemática. |
| `nivel_0_CH9` | STRING | Percentual de alunos do 9º ano do Ensino Fundamental no nível 0 de proficiência em Ciências Humanas. |
| `nivel_1_CH9` | STRING | Percentual de alunos do 9º ano do Ensino Fundamental no nível 1 de proficiência em Ciências Humanas. |
| `nivel_2_CH9` | STRING | Percentual de alunos do 9º ano do Ensino Fundamental no nível 2 de proficiência em Ciências Humanas. |
| `nivel_3_CH9` | STRING | Percentual de alunos do 9º ano do Ensino Fundamental no nível 3 de proficiência em Ciências Humanas. |
| `nivel_4_CH9` | STRING | Percentual de alunos do 9º ano do Ensino Fundamental no nível 4 de proficiência em Ciências Humanas. |
| `nivel_5_CH9` | STRING | Percentual de alunos do 9º ano do Ensino Fundamental no nível 5 de proficiência em Ciências Humanas. |
| `nivel_6_CH9` | STRING | Percentual de alunos do 9º ano do Ensino Fundamental no nível 6 de proficiência em Ciências Humanas. |
| `nivel_7_CH9` | STRING | Percentual de alunos do 9º ano do Ensino Fundamental no nível 7 de proficiência em Ciências Humanas. |
| `nivel_8_CH9` | STRING | Percentual de alunos do 9º ano do Ensino Fundamental no nível 8 de proficiência em Ciências Humanas. |
| `nivel_9_CH9` | STRING | Percentual de alunos do 9º ano do Ensino Fundamental no nível 9 de proficiência em Ciências Humanas. |
| `nivel_0_CN9` | STRING | Percentual de alunos do 9º ano do Ensino Fundamental no nível 0 de proficiência em Ciências da Natureza. |
| `nivel_1_CN9` | STRING | Percentual de alunos do 9º ano do Ensino Fundamental no nível 1 de proficiência em Ciências da Natureza. |
| `nivel_2_CN9` | STRING | Percentual de alunos do 9º ano do Ensino Fundamental no nível 2 de proficiência em Ciências da Natureza. |
| `nivel_3_CN9` | STRING | Percentual de alunos do 9º ano do Ensino Fundamental no nível 3 de proficiência em Ciências da Natureza. |
| `nivel_4_CN9` | STRING | Percentual de alunos do 9º ano do Ensino Fundamental no nível 4 de proficiência em Ciências da Natureza. |
| `nivel_5_CN9` | STRING | Percentual de alunos do 9º ano do Ensino Fundamental no nível 5 de proficiência em Ciências da Natureza. |
| `nivel_6_CN9` | STRING | Percentual de alunos do 9º ano do Ensino Fundamental no nível 6 de proficiência em Ciências da Natureza. |
| `nivel_7_CN9` | STRING | Percentual de alunos do 9º ano do Ensino Fundamental no nível 7 de proficiência em Ciências da Natureza. |
| `nivel_8_CN9` | STRING | Percentual de alunos do 9º ano do Ensino Fundamental no nível 8 de proficiência em Ciências da Natureza. |
| `nivel_0_LP12` | STRING | Percentual de alunos do 3º ano do Ensino Médio no nível 0 de proficiência em Língua Portuguesa. |
| `nivel_1_LP12` | STRING | Percentual de alunos do 3º ano do Ensino Médio no nível 1 de proficiência em Língua Portuguesa. |
| `nivel_2_LP12` | STRING | Percentual de alunos do 3º ano do Ensino Médio no nível 2 de proficiência em Língua Portuguesa. |
| `nivel_3_LP12` | STRING | Percentual de alunos do 3º ano do Ensino Médio no nível 3 de proficiência em Língua Portuguesa. |
| `nivel_4_LP12` | STRING | Percentual de alunos do 3º ano do Ensino Médio no nível 4 de proficiência em Língua Portuguesa. |
| `nivel_5_LP12` | STRING | Percentual de alunos do 3º ano do Ensino Médio no nível 5 de proficiência em Língua Portuguesa. |
| `nivel_6_LP12` | STRING | Percentual de alunos do 3º ano do Ensino Médio no nível 6 de proficiência em Língua Portuguesa. |
| `nivel_7_LP12` | STRING | Percentual de alunos do 3º ano do Ensino Médio no nível 7 de proficiência em Língua Portuguesa. |
| `nivel_8_LP12` | STRING | Percentual de alunos do 3º ano do Ensino Médio no nível 8 de proficiência em Língua Portuguesa. |
| `nivel_0_MT12` | STRING | Percentual de alunos do 3º ano do Ensino Médio no nível 0 de proficiência em Matemática. |
| `nivel_1_MT12` | STRING | Percentual de alunos do 3º ano do Ensino Médio no nível 1 de proficiência em Matemática. |
| `nivel_2_MT12` | STRING | Percentual de alunos do 3º ano do Ensino Médio no nível 2 de proficiência em Matemática. |
| `nivel_3_MT12` | STRING | Percentual de alunos do 3º ano do Ensino Médio no nível 3 de proficiência em Matemática. |
| `nivel_4_MT12` | STRING | Percentual de alunos do 3º ano do Ensino Médio no nível 4 de proficiência em Matemática. |
| `nivel_5_MT12` | STRING | Percentual de alunos do 3º ano do Ensino Médio no nível 5 de proficiência em Matemática. |
| `nivel_6_MT12` | STRING | Percentual de alunos do 3º ano do Ensino Médio no nível 6 de proficiência em Matemática. |
| `nivel_7_MT12` | STRING | Percentual de alunos do 3º ano do Ensino Médio no nível 7 de proficiência em Matemática. |
| `nivel_8_MT12` | STRING | Percentual de alunos do 3º ano do Ensino Médio no nível 8 de proficiência em Matemática. |
| `nivel_9_MT12` | STRING | Percentual de alunos do 3º ano do Ensino Médio no nível 9 de proficiência em Matemática. |
| `nivel_10_MT12` | STRING | Percentual de alunos do 3º ano do Ensino Médio no nível 10 de proficiência em Matemática. |
| `nivel_0_LP13` | STRING | Percentual de alunos do 4º ano do Ensino Médio/Técnico no nível 0 de proficiência em Língua Portuguesa. |
| `nivel_1_LP13` | STRING | Percentual de alunos do 4º ano do Ensino Médio/Técnico no nível 1 de proficiência em Língua Portuguesa. |
| `nivel_2_LP13` | STRING | Percentual de alunos do 4º ano do Ensino Médio/Técnico no nível 2 de proficiência em Língua Portuguesa. |
| `nivel_3_LP13` | STRING | Percentual de alunos do 4º ano do Ensino Médio/Técnico no nível 3 de proficiência em Língua Portuguesa. |
| `nivel_4_LP13` | STRING | Percentual de alunos do 4º ano do Ensino Médio/Técnico no nível 4 de proficiência em Língua Portuguesa. |
| `nivel_5_LP13` | STRING | Percentual de alunos do 4º ano do Ensino Médio/Técnico no nível 5 de proficiência em Língua Portuguesa. |
| `nivel_6_LP13` | STRING | Percentual de alunos do 4º ano do Ensino Médio/Técnico no nível 6 de proficiência em Língua Portuguesa. |
| `nivel_7_LP13` | STRING | Percentual de alunos do 4º ano do Ensino Médio/Técnico no nível 7 de proficiência em Língua Portuguesa. |
| `nivel_8_LP13` | STRING | Percentual de alunos do 4º ano do Ensino Médio/Técnico no nível 8 de proficiência em Língua Portuguesa. |
| `nivel_0_MT13` | STRING | Percentual de alunos do 4º ano do Ensino Médio/Técnico no nível 0 de proficiência em Matemática. |
| `nivel_1_MT13` | STRING | Percentual de alunos do 4º ano do Ensino Médio/Técnico no nível 1 de proficiência em Matemática. |
| `nivel_2_MT13` | STRING | Percentual de alunos do 4º ano do Ensino Médio/Técnico no nível 2 de proficiência em Matemática. |
| `nivel_3_MT13` | STRING | Percentual de alunos do 4º ano do Ensino Médio/Técnico no nível 3 de proficiência em Matemática. |
| `nivel_4_MT13` | STRING | Percentual de alunos do 4º ano do Ensino Médio/Técnico no nível 4 de proficiência em Matemática. |
| `nivel_5_MT13` | STRING | Percentual de alunos do 4º ano do Ensino Médio/Técnico no nível 5 de proficiência em Matemática. |
| `nivel_6_MT13` | STRING | Percentual de alunos do 4º ano do Ensino Médio/Técnico no nível 6 de proficiência em Matemática. |
| `nivel_7_MT13` | STRING | Percentual de alunos do 4º ano do Ensino Médio/Técnico no nível 7 de proficiência em Matemática. |
| `nivel_8_MT13` | STRING | Percentual de alunos do 4º ano do Ensino Médio/Técnico no nível 8 de proficiência em Matemática. |
| `nivel_9_MT13` | STRING | Percentual de alunos do 4º ano do Ensino Médio/Técnico no nível 9 de proficiência em Matemática. |
| `nivel_10_MT13` | STRING | Percentual de alunos do 4º ano do Ensino Médio/Técnico no nível 10 de proficiência em Matemática. |
| `nivel_0_LP14` | STRING | Percentual de alunos da Série 14 no nível 0 de proficiência em Língua Portuguesa. |
| `nivel_1_LP14` | STRING | Percentual de alunos da Série 14 no nível 1 de proficiência em Língua Portuguesa. |
| `nivel_2_LP14` | STRING | Percentual de alunos da Série 14 no nível 2 de proficiência em Língua Portuguesa. |
| `nivel_3_LP14` | STRING | Percentual de alunos da Série 14 no nível 3 de proficiência em Língua Portuguesa. |
| `nivel_4_LP14` | STRING | Percentual de alunos da Série 14 no nível 4 de proficiência em Língua Portuguesa. |
| `nivel_5_LP14` | STRING | Percentual de alunos da Série 14 no nível 5 de proficiência em Língua Portuguesa. |
| `nivel_6_LP14` | STRING | Percentual de alunos da Série 14 no nível 6 de proficiência em Língua Portuguesa. |
| `nivel_7_LP14` | STRING | Percentual de alunos da Série 14 no nível 7 de proficiência em Língua Portuguesa. |
| `nivel_8_LP14` | STRING | Percentual de alunos da Série 14 no nível 8 de proficiência em Língua Portuguesa. |
| `nivel_0_MT14` | STRING | Percentual de alunos da Série 14 no nível 0 de proficiência em Matemática. |
| `nivel_1_MT14` | STRING | Percentual de alunos da Série 14 no nível 1 de proficiência em Matemática. |
| `nivel_2_MT14` | STRING | Percentual de alunos da Série 14 no nível 2 de proficiência em Matemática. |
| `nivel_3_MT14` | STRING | Percentual de alunos da Série 14 no nível 3 de proficiência em Matemática. |
| `nivel_4_MT14` | STRING | Percentual de alunos da Série 14 no nível 4 de proficiência em Matemática. |
| `nivel_5_MT14` | STRING | Percentual de alunos da Série 14 no nível 5 de proficiência em Matemática. |
| `nivel_6_MT14` | STRING | Percentual de alunos da Série 14 no nível 6 de proficiência em Matemática. |
| `nivel_7_MT14` | STRING | Percentual de alunos da Série 14 no nível 7 de proficiência em Matemática. |
| `nivel_8_MT14` | STRING | Percentual de alunos da Série 14 no nível 8 de proficiência em Matemática. |
| `nivel_9_MT14` | STRING | Percentual de alunos da Série 14 no nível 9 de proficiência em Matemática. |
| `nivel_10_MT14` | STRING | Percentual de alunos da Série 14 no nível 10 de proficiência em Matemática. |
| `dt_ingestao_lake` | TIMESTAMP | Data e hora em que os dados foram carregados no Data Lake. — descrição gerada por IA. |

## raw · saeb_indicadores_historico_brasil

File `raw__saeb_indicadores_historico_brasil.parquet` · 24 rows · 84 columns

Tabela com a distribuição percentual de alunos por níveis de proficiência em Língua Portuguesa (LP) e Matemática (MT) nas avaliações do SAEB, segmentada por ano, UF, dependência administrativa e série (5º ano, 9º ano e Ensino Médio/12º ano).

**Feeds:** `trusted/inep_saeb_indicadores_historico_brasil`

| Column | Type | Description |
|---|---|---|
| `ANO_SAEB` | STRING | Ano de realização da edição do SAEB (formato YYYY). |
| `GRUPO` | STRING | Grupo de agregação geográfica dos dados (ex: 'BR' para Brasil). |
| `DEPENDENCIA_ADM` | STRING | Dependência administrativa das escolas avaliadas (Estadual, Municipal, Federal, Privada ou Total). |
| `CO_UF` | INTEGER | Código numérico do IBGE correspondente à Unidade da Federação. |
| `NO_UF` | STRING | Nome da Unidade da Federação (UF) ou 'Brasil' para dados nacionais. |
| `tipo` | STRING | Tipo de agregação territorial do registro (ex: 'BR', 'UF'). |
| `nivel_0_MT5` | STRING | Proporção de alunos do 5º ano EF no nível 0 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_1_MT5` | STRING | Proporção de alunos do 5º ano EF no nível 1 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_2_MT5` | STRING | Proporção de alunos do 5º ano EF no nível 2 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_3_MT5` | STRING | Proporção de alunos do 5º ano EF no nível 3 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_4_MT5` | STRING | Proporção de alunos do 5º ano EF no nível 4 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_5_MT5` | STRING | Proporção de alunos do 5º ano EF no nível 5 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_6_MT5` | STRING | Proporção de alunos do 5º ano EF no nível 6 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_7_MT5` | STRING | Proporção de alunos do 5º ano EF no nível 7 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_8_MT5` | STRING | Proporção de alunos do 5º ano EF no nível 8 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_9_MT5` | STRING | Proporção de alunos do 5º ano EF no nível 9 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_10_MT5` | STRING | Proporção de alunos do 5º ano EF no nível 10 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_11_MT5` | STRING | Proporção de alunos do 5º ano EF no nível 11 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_12_MT5` | INTEGER | Proporção de alunos do 5º ano EF no nível 12 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_13_MT5` | INTEGER | Proporção de alunos do 5º ano EF no nível 13 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_0_MT9` | STRING | Proporção de alunos do 9º ano EF no nível 0 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_1_MT9` | STRING | Proporção de alunos do 9º ano EF no nível 1 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_2_MT9` | STRING | Proporção de alunos do 9º ano EF no nível 2 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_3_MT9` | STRING | Proporção de alunos do 9º ano EF no nível 3 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_4_MT9` | STRING | Proporção de alunos do 9º ano EF no nível 4 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_5_MT9` | STRING | Proporção de alunos do 9º ano EF no nível 5 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_6_MT9` | STRING | Proporção de alunos do 9º ano EF no nível 6 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_7_MT9` | STRING | Proporção de alunos do 9º ano EF no nível 7 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_8_MT9` | STRING | Proporção de alunos do 9º ano EF no nível 8 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_9_MT9` | STRING | Proporção de alunos do 9º ano EF no nível 9 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_10_MT9` | STRING | Proporção de alunos do 9º ano EF no nível 10 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_11_MT9` | STRING | Proporção de alunos do 9º ano EF no nível 11 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_12_MT9` | STRING | Proporção de alunos do 9º ano EF no nível 12 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_13_MT9` | STRING | Proporção de alunos do 9º ano EF no nível 13 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_0_MT12` | INTEGER | Proporção de alunos do 3º ano EM (12º ano) no nível 0 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_1_MT12` | STRING | Proporção de alunos do 3º ano EM (12º ano) no nível 1 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_2_MT12` | STRING | Proporção de alunos do 3º ano EM (12º ano) no nível 2 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_3_MT12` | STRING | Proporção de alunos do 3º ano EM (12º ano) no nível 3 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_4_MT12` | STRING | Proporção de alunos do 3º ano EM (12º ano) no nível 4 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_5_MT12` | STRING | Proporção de alunos do 3º ano EM (12º ano) no nível 5 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_6_MT12` | STRING | Proporção de alunos do 3º ano EM (12º ano) no nível 6 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_7_MT12` | STRING | Proporção de alunos do 3º ano EM (12º ano) no nível 7 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_8_MT12` | STRING | Proporção de alunos do 3º ano EM (12º ano) no nível 8 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_9_MT12` | STRING | Proporção de alunos do 3º ano EM (12º ano) no nível 9 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_10_MT12` | STRING | Proporção de alunos do 3º ano EM (12º ano) no nível 10 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_11_MT12` | STRING | Proporção de alunos do 3º ano EM (12º ano) no nível 11 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_12_MT12` | STRING | Proporção de alunos do 3º ano EM (12º ano) no nível 12 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_13_MT12` | STRING | Proporção de alunos do 3º ano EM (12º ano) no nível 13 de proficiência em Matemática (decimal de 0 a 1). |
| `nivel_0_LP5` | STRING | Proporção de alunos do 5º ano EF no nível 0 de proficiência em Língua Portuguesa (decimal de 0 a 1). |
| `nivel_1_LP5` | STRING | Proporção de alunos do 5º ano EF no nível 1 de proficiência em Língua Portuguesa (decimal de 0 a 1). |
| `nivel_2_LP5` | STRING | Proporção de alunos do 5º ano EF no nível 2 de proficiência em Língua Portuguesa (decimal de 0 a 1). |
| `nivel_3_LP5` | STRING | Proporção de alunos do 5º ano EF no nível 3 de proficiência em Língua Portuguesa (decimal de 0 a 1). |
| `nivel_4_LP5` | STRING | Proporção de alunos do 5º ano EF no nível 4 de proficiência em Língua Portuguesa (decimal de 0 a 1). |
| `nivel_5_LP5` | STRING | Proporção de alunos do 5º ano EF no nível 5 de proficiência em Língua Portuguesa (decimal de 0 a 1). |
| `nivel_6_LP5` | STRING | Proporção de alunos do 5º ano EF no nível 6 de proficiência em Língua Portuguesa (decimal de 0 a 1). |
| `nivel_7_LP5` | STRING | Proporção de alunos do 5º ano EF no nível 7 de proficiência em Língua Portuguesa (decimal de 0 a 1). |
| `nivel_8_LP5` | STRING | Proporção de alunos do 5º ano EF no nível 8 de proficiência em Língua Portuguesa (decimal de 0 a 1). |
| `nivel_9_LP5` | STRING | Proporção de alunos do 5º ano EF no nível 9 de proficiência em Língua Portuguesa (decimal de 0 a 1). |
| `nivel_10_LP5` | STRING | Proporção de alunos do 5º ano EF no nível 10 de proficiência em Língua Portuguesa (decimal de 0 a 1). |
| `nivel_11_LP5` | INTEGER | Proporção de alunos do 5º ano EF no nível 11 de proficiência em Língua Portuguesa (decimal de 0 a 1). |
| `nivel_0_LP9` | STRING | Proporção de alunos do 9º ano EF no nível 0 de proficiência em Língua Portuguesa (decimal de 0 a 1). |
| `nivel_1_LP9` | STRING | Proporção de alunos do 9º ano EF no nível 1 de proficiência em Língua Portuguesa (decimal de 0 a 1). |
| `nivel_2_LP9` | STRING | Proporção de alunos do 9º ano EF no nível 2 de proficiência em Língua Portuguesa (decimal de 0 a 1). |
| `nivel_3_LP9` | STRING | Proporção de alunos do 9º ano EF no nível 3 de proficiência em Língua Portuguesa (decimal de 0 a 1). |
| `nivel_4_LP9` | STRING | Proporção de alunos do 9º ano EF no nível 4 de proficiência em Língua Portuguesa (decimal de 0 a 1). |
| `nivel_5_LP9` | STRING | Proporção de alunos do 9º ano EF no nível 5 de proficiência em Língua Portuguesa (decimal de 0 a 1). |
| `nivel_6_LP9` | STRING | Proporção de alunos do 9º ano EF no nível 6 de proficiência em Língua Portuguesa (decimal de 0 a 1). |
| `nivel_7_LP9` | STRING | Proporção de alunos do 9º ano EF no nível 7 de proficiência em Língua Portuguesa (decimal de 0 a 1). |
| `nivel_8_LP9` | STRING | Proporção de alunos do 9º ano EF no nível 8 de proficiência em Língua Portuguesa (decimal de 0 a 1). |
| `nivel_9_LP9` | STRING | Proporção de alunos do 9º ano EF no nível 9 de proficiência em Língua Portuguesa (decimal de 0 a 1). |
| `nivel_10_LP9` | STRING | Proporção de alunos do 9º ano EF no nível 10 de proficiência em Língua Portuguesa (decimal de 0 a 1). |
| `nivel_11_LP9` | STRING | Proporção de alunos do 9º ano EF no nível 11 de proficiência em Língua Portuguesa (decimal de 0 a 1). |
| `nivel_0_LP12` | STRING | Proporção de alunos do 3º ano EM (12º ano) no nível 0 de proficiência em Língua Portuguesa (decimal de 0 a 1). |
| `nivel_1_LP12` | STRING | Proporção de alunos do 3º ano EM (12º ano) no nível 1 de proficiência em Língua Portuguesa (decimal de 0 a 1). |
| `nivel_2_LP12` | STRING | Proporção de alunos do 3º ano EM (12º ano) no nível 2 de proficiência em Língua Portuguesa (decimal de 0 a 1). |
| `nivel_3_LP12` | STRING | Proporção de alunos do 3º ano EM (12º ano) no nível 3 de proficiência em Língua Portuguesa (decimal de 0 a 1). |
| `nivel_4_LP12` | STRING | Proporção de alunos do 3º ano EM (12º ano) no nível 4 de proficiência em Língua Portuguesa (decimal de 0 a 1). |
| `nivel_5_LP12` | STRING | Proporção de alunos do 3º ano EM (12º ano) no nível 5 de proficiência em Língua Portuguesa (decimal de 0 a 1). |
| `nivel_6_LP12` | STRING | Proporção de alunos do 3º ano EM (12º ano) no nível 6 de proficiência em Língua Portuguesa (decimal de 0 a 1). |
| `nivel_7_LP12` | STRING | Proporção de alunos do 3º ano EM (12º ano) no nível 7 de proficiência em Língua Portuguesa (decimal de 0 a 1). |
| `nivel_8_LP12` | STRING | Proporção de alunos do 3º ano EM (12º ano) no nível 8 de proficiência em Língua Portuguesa (decimal de 0 a 1). |
| `nivel_9_LP12` | STRING | Proporção de alunos do 3º ano EM (12º ano) no nível 9 de proficiência em Língua Portuguesa (decimal de 0 a 1). |
| `nivel_10_LP12` | STRING | Proporção de alunos do 3º ano EM (12º ano) no nível 10 de proficiência em Língua Portuguesa (decimal de 0 a 1). |
| `nivel_11_LP12` | STRING | Proporção de alunos do 3º ano EM (12º ano) no nível 11 de proficiência em Língua Portuguesa (decimal de 0 a 1). |

## raw · saeb_indicadores_historico_estados

File `raw__saeb_indicadores_historico_estados.parquet` · 714 rows · 84 columns

Distribuição histórica da proporção de alunos por níveis de proficiência em Matemática (MT) e Língua Portuguesa (LP) no SAEB, segmentada por ano, UF e dependência administrativa.

**Feeds:** `trusted/inep_saeb_indicadores_historico_estados`

| Column | Type | Description |
|---|---|---|
| `ANO_SAEB` | STRING | Ano de realização da edição do SAEB (formato YYYY). |
| `GRUPO` | STRING | Sigla da Unidade Federativa (UF) correspondente aos dados. |
| `DEPENDENCIA_ADM` | STRING | Dependência administrativa das escolas avaliadas (ex: Federal, Estadual, Municipal, Particular ou Total). |
| `CO_UF` | STRING | Código de identificação da Unidade Federativa segundo o IBGE. |
| `NO_UF` | STRING | Nome por extenso da Unidade Federativa. |
| `tipo` | STRING | Nível de agregação geográfica dos dados (ex: 'UF'). |
| `nivel_0_MT5` | STRING | Proporção de alunos do 5º ano do Ensino Fundamental no nível 0 de proficiência em Matemática. |
| `nivel_1_MT5` | STRING | Proporção de alunos do 5º ano do Ensino Fundamental no nível 1 de proficiência em Matemática. |
| `nivel_2_MT5` | STRING | Proporção de alunos do 5º ano do Ensino Fundamental no nível 2 de proficiência em Matemática. |
| `nivel_3_MT5` | STRING | Proporção de alunos do 5º ano do Ensino Fundamental no nível 3 de proficiência em Matemática. |
| `nivel_4_MT5` | STRING | Proporção de alunos do 5º ano do Ensino Fundamental no nível 4 de proficiência em Matemática. |
| `nivel_5_MT5` | STRING | Proporção de alunos do 5º ano do Ensino Fundamental no nível 5 de proficiência em Matemática. |
| `nivel_6_MT5` | STRING | Proporção de alunos do 5º ano do Ensino Fundamental no nível 6 de proficiência em Matemática. |
| `nivel_7_MT5` | STRING | Proporção de alunos do 5º ano do Ensino Fundamental no nível 7 de proficiência em Matemática. |
| `nivel_8_MT5` | STRING | Proporção de alunos do 5º ano do Ensino Fundamental no nível 8 de proficiência em Matemática. |
| `nivel_9_MT5` | STRING | Proporção de alunos do 5º ano do Ensino Fundamental no nível 9 de proficiência em Matemática. |
| `nivel_10_MT5` | STRING | Proporção de alunos do 5º ano do Ensino Fundamental no nível 10 de proficiência em Matemática. |
| `nivel_11_MT5` | STRING | Proporção de alunos do 5º ano do Ensino Fundamental no nível 11 de proficiência em Matemática. |
| `nivel_12_MT5` | INTEGER | Proporção de alunos do 5º ano do Ensino Fundamental no nível 12 de proficiência em Matemática. |
| `nivel_13_MT5` | INTEGER | Proporção de alunos do 5º ano do Ensino Fundamental no nível 13 de proficiência em Matemática. |
| `nivel_0_MT9` | STRING | Proporção de alunos do 9º ano do Ensino Fundamental no nível 0 de proficiência em Matemática. |
| `nivel_1_MT9` | STRING | Proporção de alunos do 9º ano do Ensino Fundamental no nível 1 de proficiência em Matemática. |
| `nivel_2_MT9` | STRING | Proporção de alunos do 9º ano do Ensino Fundamental no nível 2 de proficiência em Matemática. |
| `nivel_3_MT9` | STRING | Proporção de alunos do 9º ano do Ensino Fundamental no nível 3 de proficiência em Matemática. |
| `nivel_4_MT9` | STRING | Proporção de alunos do 9º ano do Ensino Fundamental no nível 4 de proficiência em Matemática. |
| `nivel_5_MT9` | STRING | Proporção de alunos do 9º ano do Ensino Fundamental no nível 5 de proficiência em Matemática. |
| `nivel_6_MT9` | STRING | Proporção de alunos do 9º ano do Ensino Fundamental no nível 6 de proficiência em Matemática. |
| `nivel_7_MT9` | STRING | Proporção de alunos do 9º ano do Ensino Fundamental no nível 7 de proficiência em Matemática. |
| `nivel_8_MT9` | STRING | Proporção de alunos do 9º ano do Ensino Fundamental no nível 8 de proficiência em Matemática. |
| `nivel_9_MT9` | STRING | Proporção de alunos do 9º ano do Ensino Fundamental no nível 9 de proficiência em Matemática. |
| `nivel_10_MT9` | STRING | Proporção de alunos do 9º ano do Ensino Fundamental no nível 10 de proficiência em Matemática. |
| `nivel_11_MT9` | STRING | Proporção de alunos do 9º ano do Ensino Fundamental no nível 11 de proficiência em Matemática. |
| `nivel_12_MT9` | STRING | Proporção de alunos do 9º ano do Ensino Fundamental no nível 12 de proficiência em Matemática. |
| `nivel_13_MT9` | STRING | Proporção de alunos do 9º ano do Ensino Fundamental no nível 13 de proficiência em Matemática. |
| `nivel_0_MT12` | INTEGER | Proporção de alunos da 3ª série do Ensino Médio (12º ano) no nível 0 de proficiência em Matemática. |
| `nivel_1_MT12` | STRING | Proporção de alunos da 3ª série do Ensino Médio (12º ano) no nível 1 de proficiência em Matemática. |
| `nivel_2_MT12` | STRING | Proporção de alunos da 3ª série do Ensino Médio (12º ano) no nível 2 de proficiência em Matemática. |
| `nivel_3_MT12` | STRING | Proporção de alunos da 3ª série do Ensino Médio (12º ano) no nível 3 de proficiência em Matemática. |
| `nivel_4_MT12` | STRING | Proporção de alunos da 3ª série do Ensino Médio (12º ano) no nível 4 de proficiência em Matemática. |
| `nivel_5_MT12` | STRING | Proporção de alunos da 3ª série do Ensino Médio (12º ano) no nível 5 de proficiência em Matemática. |
| `nivel_6_MT12` | STRING | Proporção de alunos da 3ª série do Ensino Médio (12º ano) no nível 6 de proficiência em Matemática. |
| `nivel_7_MT12` | STRING | Proporção de alunos da 3ª série do Ensino Médio (12º ano) no nível 7 de proficiência em Matemática. |
| `nivel_8_MT12` | STRING | Proporção de alunos da 3ª série do Ensino Médio (12º ano) no nível 8 de proficiência em Matemática. |
| `nivel_9_MT12` | STRING | Proporção de alunos da 3ª série do Ensino Médio (12º ano) no nível 9 de proficiência em Matemática. |
| `nivel_10_MT12` | STRING | Proporção de alunos da 3ª série do Ensino Médio (12º ano) no nível 10 de proficiência em Matemática. |
| `nivel_11_MT12` | STRING | Proporção de alunos da 3ª série do Ensino Médio (12º ano) no nível 11 de proficiência em Matemática. |
| `nivel_12_MT12` | STRING | Proporção de alunos da 3ª série do Ensino Médio (12º ano) no nível 12 de proficiência em Matemática. |
| `nivel_13_MT12` | STRING | Proporção de alunos da 3ª série do Ensino Médio (12º ano) no nível 13 de proficiência em Matemática. |
| `nivel_0_LP5` | STRING | Proporção de alunos do 5º ano do Ensino Fundamental no nível 0 de proficiência em Língua Portuguesa. |
| `nivel_1_LP5` | STRING | Proporção de alunos do 5º ano do Ensino Fundamental no nível 1 de proficiência em Língua Portuguesa. |
| `nivel_2_LP5` | STRING | Proporção de alunos do 5º ano do Ensino Fundamental no nível 2 de proficiência em Língua Portuguesa. |
| `nivel_3_LP5` | STRING | Proporção de alunos do 5º ano do Ensino Fundamental no nível 3 de proficiência em Língua Portuguesa. |
| `nivel_4_LP5` | STRING | Proporção de alunos do 5º ano do Ensino Fundamental no nível 4 de proficiência em Língua Portuguesa. |
| `nivel_5_LP5` | STRING | Proporção de alunos do 5º ano do Ensino Fundamental no nível 5 de proficiência em Língua Portuguesa. |
| `nivel_6_LP5` | STRING | Proporção de alunos do 5º ano do Ensino Fundamental no nível 6 de proficiência em Língua Portuguesa. |
| `nivel_7_LP5` | STRING | Proporção de alunos do 5º ano do Ensino Fundamental no nível 7 de proficiência em Língua Portuguesa. |
| `nivel_8_LP5` | STRING | Proporção de alunos do 5º ano do Ensino Fundamental no nível 8 de proficiência em Língua Portuguesa. |
| `nivel_9_LP5` | STRING | Proporção de alunos do 5º ano do Ensino Fundamental no nível 9 de proficiência em Língua Portuguesa. |
| `nivel_10_LP5` | STRING | Proporção de alunos do 5º ano do Ensino Fundamental no nível 10 de proficiência em Língua Portuguesa. |
| `nivel_11_LP5` | INTEGER | Proporção de alunos do 5º ano do Ensino Fundamental no nível 11 de proficiência em Língua Portuguesa. |
| `nivel_0_LP9` | STRING | Proporção de alunos do 9º ano do Ensino Fundamental no nível 0 de proficiência em Língua Portuguesa. |
| `nivel_1_LP9` | STRING | Proporção de alunos do 9º ano do Ensino Fundamental no nível 1 de proficiência em Língua Portuguesa. |
| `nivel_2_LP9` | STRING | Proporção de alunos do 9º ano do Ensino Fundamental no nível 2 de proficiência em Língua Portuguesa. |
| `nivel_3_LP9` | STRING | Proporção de alunos do 9º ano do Ensino Fundamental no nível 3 de proficiência em Língua Portuguesa. |
| `nivel_4_LP9` | STRING | Proporção de alunos do 9º ano do Ensino Fundamental no nível 4 de proficiência em Língua Portuguesa. |
| `nivel_5_LP9` | STRING | Proporção de alunos do 9º ano do Ensino Fundamental no nível 5 de proficiência em Língua Portuguesa. |
| `nivel_6_LP9` | STRING | Proporção de alunos do 9º ano do Ensino Fundamental no nível 6 de proficiência em Língua Portuguesa. |
| `nivel_7_LP9` | STRING | Proporção de alunos do 9º ano do Ensino Fundamental no nível 7 de proficiência em Língua Portuguesa. |
| `nivel_8_LP9` | STRING | Proporção de alunos do 9º ano do Ensino Fundamental no nível 8 de proficiência em Língua Portuguesa. |
| `nivel_9_LP9` | STRING | Proporção de alunos do 9º ano do Ensino Fundamental no nível 9 de proficiência em Língua Portuguesa. |
| `nivel_10_LP9` | STRING | Proporção de alunos do 9º ano do Ensino Fundamental no nível 10 de proficiência em Língua Portuguesa. |
| `nivel_11_LP9` | STRING | Proporção de alunos do 9º ano do Ensino Fundamental no nível 11 de proficiência em Língua Portuguesa. |
| `nivel_0_LP12` | STRING | Proporção de alunos da 3ª série do Ensino Médio (12º ano) no nível 0 de proficiência em Língua Portuguesa. |
| `nivel_1_LP12` | STRING | Proporção de alunos da 3ª série do Ensino Médio (12º ano) no nível 1 de proficiência em Língua Portuguesa. |
| `nivel_2_LP12` | STRING | Proporção de alunos da 3ª série do Ensino Médio (12º ano) no nível 2 de proficiência em Língua Portuguesa. |
| `nivel_3_LP12` | STRING | Proporção de alunos da 3ª série do Ensino Médio (12º ano) no nível 3 de proficiência em Língua Portuguesa. |
| `nivel_4_LP12` | STRING | Proporção de alunos da 3ª série do Ensino Médio (12º ano) no nível 4 de proficiência em Língua Portuguesa. |
| `nivel_5_LP12` | STRING | Proporção de alunos da 3ª série do Ensino Médio (12º ano) no nível 5 de proficiência em Língua Portuguesa. |
| `nivel_6_LP12` | STRING | Proporção de alunos da 3ª série do Ensino Médio (12º ano) no nível 6 de proficiência em Língua Portuguesa. |
| `nivel_7_LP12` | STRING | Proporção de alunos da 3ª série do Ensino Médio (12º ano) no nível 7 de proficiência em Língua Portuguesa. |
| `nivel_8_LP12` | STRING | Proporção de alunos da 3ª série do Ensino Médio (12º ano) no nível 8 de proficiência em Língua Portuguesa. |
| `nivel_9_LP12` | STRING | Proporção de alunos da 3ª série do Ensino Médio (12º ano) no nível 9 de proficiência em Língua Portuguesa. |
| `nivel_10_LP12` | STRING | Proporção de alunos da 3ª série do Ensino Médio (12º ano) no nível 10 de proficiência em Língua Portuguesa. |
| `nivel_11_LP12` | STRING | Proporção de alunos da 3ª série do Ensino Médio (12º ano) no nível 11 de proficiência em Língua Portuguesa. |

## raw · saeb_indicadores_municipios

File `raw__saeb_indicadores_municipios.parquet` · 540,927 rows · 115 columns

SAEB Planilha de Resultados — nível municipal. Fonte: INEP.

**Feeds:** `trusted/inep_saeb_indicadores_municipios`

| Column | Type | Description |
|---|---|---|
| `ANO_SAEB` | STRING | Ano de referência da edição do SAEB. |
| `CO_UF` | STRING | Código IBGE da Unidade da Federação (Estado). |
| `NO_UF` | STRING | Nome da Unidade da Federação (Estado). |
| `CO_MUNICIPIO` | STRING | Código IBGE do município. |
| `NO_MUNICIPIO` | STRING | Nome do município. |
| `DEPENDENCIA_ADM` | STRING | Dependência administrativa das escolas (ex: Estadual, Municipal, Federal, Privada). |
| `LOCALIZACAO` | STRING | Localização das escolas (Urbana ou Rural). |
| `CAPITAL` | STRING | Indicador se o município é capital do estado (1 para Sim, 0 ou nulo para Não). |
| `MEDIA_5_LP` | STRING | Média de proficiência em Língua Portuguesa dos alunos do 5º ano do Ensino Fundamental. |
| `MEDIA_5_MT` | STRING | Média de proficiência em Matemática dos alunos do 5º ano do Ensino Fundamental. |
| `MEDIA_9_LP` | STRING | Média de proficiência em Língua Portuguesa dos alunos do 9º ano do Ensino Fundamental. |
| `MEDIA_9_MT` | STRING | Média de proficiência em Matemática dos alunos do 9º ano do Ensino Fundamental. |
| `MEDIA_12_LP` | STRING | Média de proficiência em Língua Portuguesa dos alunos do 3º ano do Ensino Médio (Série 12). |
| `MEDIA_12_MT` | STRING | Média de proficiência em Matemática dos alunos do 3º ano do Ensino Médio (Série 12). |
| `nivel_0_LP5` | STRING | Percentual de alunos do 5º ano EF no nível 0 de proficiência em Língua Portuguesa. |
| `nivel_1_LP5` | STRING | Percentual de alunos do 5º ano EF no nível 1 de proficiência em Língua Portuguesa. |
| `nivel_2_LP5` | STRING | Percentual de alunos do 5º ano EF no nível 2 de proficiência em Língua Portuguesa. |
| `nivel_3_LP5` | STRING | Percentual de alunos do 5º ano EF no nível 3 de proficiência em Língua Portuguesa. |
| `nivel_4_LP5` | STRING | Percentual de alunos do 5º ano EF no nível 4 de proficiência em Língua Portuguesa. |
| `nivel_5_LP5` | STRING | Percentual de alunos do 5º ano EF no nível 5 de proficiência em Língua Portuguesa. |
| `nivel_6_LP5` | STRING | Percentual de alunos do 5º ano EF no nível 6 de proficiência em Língua Portuguesa. |
| `nivel_7_LP5` | STRING | Percentual de alunos do 5º ano EF no nível 7 de proficiência em Língua Portuguesa. |
| `nivel_8_LP5` | STRING | Percentual de alunos do 5º ano EF no nível 8 de proficiência em Língua Portuguesa. |
| `nivel_9_LP5` | STRING | Percentual de alunos do 5º ano EF no nível 9 de proficiência em Língua Portuguesa. |
| `nivel_0_MT5` | STRING | Percentual de alunos do 5º ano EF no nível 0 de proficiência em Matemática. |
| `nivel_1_MT5` | STRING | Percentual de alunos do 5º ano EF no nível 1 de proficiência em Matemática. |
| `nivel_2_MT5` | STRING | Percentual de alunos do 5º ano EF no nível 2 de proficiência em Matemática. |
| `nivel_3_MT5` | STRING | Percentual de alunos do 5º ano EF no nível 3 de proficiência em Matemática. |
| `nivel_4_MT5` | STRING | Percentual de alunos do 5º ano EF no nível 4 de proficiência em Matemática. |
| `nivel_5_MT5` | STRING | Percentual de alunos do 5º ano EF no nível 5 de proficiência em Matemática. |
| `nivel_6_MT5` | STRING | Percentual de alunos do 5º ano EF no nível 6 de proficiência em Matemática. |
| `nivel_7_MT5` | STRING | Percentual de alunos do 5º ano EF no nível 7 de proficiência em Matemática. |
| `nivel_8_MT5` | STRING | Percentual de alunos do 5º ano EF no nível 8 de proficiência em Matemática. |
| `nivel_9_MT5` | STRING | Percentual de alunos do 5º ano EF no nível 9 de proficiência em Matemática. |
| `nivel_10_MT5` | STRING | Percentual de alunos do 5º ano EF no nível 10 de proficiência em Matemática. |
| `nivel_0_LP9` | STRING | Percentual de alunos do 9º ano EF no nível 0 de proficiência em Língua Portuguesa. |
| `nivel_1_LP9` | STRING | Percentual de alunos do 9º ano EF no nível 1 de proficiência em Língua Portuguesa. |
| `nivel_2_LP9` | STRING | Percentual de alunos do 9º ano EF no nível 2 de proficiência em Língua Portuguesa. |
| `nivel_3_LP9` | STRING | Percentual de alunos do 9º ano EF no nível 3 de proficiência em Língua Portuguesa. |
| `nivel_4_LP9` | STRING | Percentual de alunos do 9º ano EF no nível 4 de proficiência em Língua Portuguesa. |
| `nivel_5_LP9` | STRING | Percentual de alunos do 9º ano EF no nível 5 de proficiência em Língua Portuguesa. |
| `nivel_6_LP9` | STRING | Percentual de alunos do 9º ano EF no nível 6 de proficiência em Língua Portuguesa. |
| `nivel_7_LP9` | STRING | Percentual de alunos do 9º ano EF no nível 7 de proficiência em Língua Portuguesa. |
| `nivel_8_LP9` | STRING | Percentual de alunos do 9º ano EF no nível 8 de proficiência em Língua Portuguesa. |
| `nivel_0_MT9` | STRING | Percentual de alunos do 9º ano EF no nível 0 de proficiência em Matemática. |
| `nivel_1_MT9` | STRING | Percentual de alunos do 9º ano EF no nível 1 de proficiência em Matemática. |
| `nivel_2_MT9` | STRING | Percentual de alunos do 9º ano EF no nível 2 de proficiência em Matemática. |
| `nivel_3_MT9` | STRING | Percentual de alunos do 9º ano EF no nível 3 de proficiência em Matemática. |
| `nivel_4_MT9` | STRING | Percentual de alunos do 9º ano EF no nível 4 de proficiência em Matemática. |
| `nivel_5_MT9` | STRING | Percentual de alunos do 9º ano EF no nível 5 de proficiência em Matemática. |
| `nivel_6_MT9` | STRING | Percentual de alunos do 9º ano EF no nível 6 de proficiência em Matemática. |
| `nivel_7_MT9` | STRING | Percentual de alunos do 9º ano EF no nível 7 de proficiência em Matemática. |
| `nivel_8_MT9` | STRING | Percentual de alunos do 9º ano EF no nível 8 de proficiência em Matemática. |
| `nivel_9_MT9` | STRING | Percentual de alunos do 9º ano EF no nível 9 de proficiência em Matemática. |
| `nivel_0_LP12` | STRING | Percentual de alunos do 3º ano EM (Série 12) no nível 0 de proficiência em Língua Portuguesa. |
| `nivel_1_LP12` | STRING | Percentual de alunos do 3º ano EM (Série 12) no nível 1 de proficiência em Língua Portuguesa. |
| `nivel_2_LP12` | STRING | Percentual de alunos do 3º ano EM (Série 12) no nível 2 de proficiência em Língua Portuguesa. |
| `nivel_3_LP12` | STRING | Percentual de alunos do 3º ano EM (Série 12) no nível 3 de proficiência em Língua Portuguesa. |
| `nivel_4_LP12` | STRING | Percentual de alunos do 3º ano EM (Série 12) no nível 4 de proficiência em Língua Portuguesa. |
| `nivel_5_LP12` | STRING | Percentual de alunos do 3º ano EM (Série 12) no nível 5 de proficiência em Língua Portuguesa. |
| `nivel_6_LP12` | STRING | Percentual de alunos do 3º ano EM (Série 12) no nível 6 de proficiência em Língua Portuguesa. |
| `nivel_7_LP12` | STRING | Percentual de alunos do 3º ano EM (Série 12) no nível 7 de proficiência em Língua Portuguesa. |
| `nivel_8_LP12` | STRING | Percentual de alunos do 3º ano EM (Série 12) no nível 8 de proficiência em Língua Portuguesa. |
| `nivel_0_MT12` | STRING | Percentual de alunos do 3º ano EM (Série 12) no nível 0 de proficiência em Matemática. |
| `nivel_1_MT12` | STRING | Percentual de alunos do 3º ano EM (Série 12) no nível 1 de proficiência em Matemática. |
| `nivel_2_MT12` | STRING | Percentual de alunos do 3º ano EM (Série 12) no nível 2 de proficiência em Matemática. |
| `nivel_3_MT12` | STRING | Percentual de alunos do 3º ano EM (Série 12) no nível 3 de proficiência em Matemática. |
| `nivel_4_MT12` | STRING | Percentual de alunos do 3º ano EM (Série 12) no nível 4 de proficiência em Matemática. |
| `nivel_5_MT12` | STRING | Percentual de alunos do 3º ano EM (Série 12) no nível 5 de proficiência em Matemática. |
| `nivel_6_MT12` | STRING | Percentual de alunos do 3º ano EM (Série 12) no nível 6 de proficiência em Matemática. |
| `nivel_7_MT12` | STRING | Percentual de alunos do 3º ano EM (Série 12) no nível 7 de proficiência em Matemática. |
| `nivel_8_MT12` | STRING | Percentual de alunos do 3º ano EM (Série 12) no nível 8 de proficiência em Matemática. |
| `nivel_9_MT12` | STRING | Percentual de alunos do 3º ano EM (Série 12) no nível 9 de proficiência em Matemática. |
| `nivel_10_MT12` | STRING | Percentual de alunos do 3º ano EM (Série 12) no nível 10 de proficiência em Matemática. |
| `nivel_0_LP13` | STRING | Percentual de alunos da Série 13 (Ensino Médio) no nível 0 de proficiência em Língua Portuguesa. |
| `nivel_1_LP13` | STRING | Percentual de alunos da Série 13 (Ensino Médio) no nível 1 de proficiência em Língua Portuguesa. |
| `nivel_2_LP13` | STRING | Percentual de alunos da Série 13 (Ensino Médio) no nível 2 de proficiência em Língua Portuguesa. |
| `nivel_3_LP13` | STRING | Percentual de alunos da Série 13 (Ensino Médio) no nível 3 de proficiência em Língua Portuguesa. |
| `nivel_4_LP13` | STRING | Percentual de alunos da Série 13 (Ensino Médio) no nível 4 de proficiência em Língua Portuguesa. |
| `nivel_5_LP13` | STRING | Percentual de alunos da Série 13 (Ensino Médio) no nível 5 de proficiência em Língua Portuguesa. |
| `nivel_6_LP13` | STRING | Percentual de alunos da Série 13 (Ensino Médio) no nível 6 de proficiência em Língua Portuguesa. |
| `nivel_7_LP13` | STRING | Percentual de alunos da Série 13 (Ensino Médio) no nível 7 de proficiência em Língua Portuguesa. |
| `nivel_8_LP13` | STRING | Percentual de alunos da Série 13 (Ensino Médio) no nível 8 de proficiência em Língua Portuguesa. |
| `nivel_0_MT13` | STRING | Percentual de alunos da Série 13 (Ensino Médio) no nível 0 de proficiência em Matemática. |
| `nivel_1_MT13` | STRING | Percentual de alunos da Série 13 (Ensino Médio) no nível 1 de proficiência em Matemática. |
| `nivel_2_MT13` | STRING | Percentual de alunos da Série 13 (Ensino Médio) no nível 2 de proficiência em Matemática. |
| `nivel_3_MT13` | STRING | Percentual de alunos da Série 13 (Ensino Médio) no nível 3 de proficiência em Matemática. |
| `nivel_4_MT13` | STRING | Percentual de alunos da Série 13 (Ensino Médio) no nível 4 de proficiência em Matemática. |
| `nivel_5_MT13` | STRING | Percentual de alunos da Série 13 (Ensino Médio) no nível 5 de proficiência em Matemática. |
| `nivel_6_MT13` | STRING | Percentual de alunos da Série 13 (Ensino Médio) no nível 6 de proficiência em Matemática. |
| `nivel_7_MT13` | STRING | Percentual de alunos da Série 13 (Ensino Médio) no nível 7 de proficiência em Matemática. |
| `nivel_8_MT13` | STRING | Percentual de alunos da Série 13 (Ensino Médio) no nível 8 de proficiência em Matemática. |
| `nivel_9_MT13` | STRING | Percentual de alunos da Série 13 (Ensino Médio) no nível 9 de proficiência em Matemática. |
| `nivel_10_MT13` | STRING | Percentual de alunos da Série 13 (Ensino Médio) no nível 10 de proficiência em Matemática. |
| `nivel_0_LP14` | STRING | Percentual de alunos da Série 14 (Ensino Médio) no nível 0 de proficiência em Língua Portuguesa. |
| `nivel_1_LP14` | STRING | Percentual de alunos da Série 14 (Ensino Médio) no nível 1 de proficiência em Língua Portuguesa. |
| `nivel_2_LP14` | STRING | Percentual de alunos da Série 14 (Ensino Médio) no nível 2 de proficiência em Língua Portuguesa. |
| `nivel_3_LP14` | STRING | Percentual de alunos da Série 14 (Ensino Médio) no nível 3 de proficiência em Língua Portuguesa. |
| `nivel_4_LP14` | STRING | Percentual de alunos da Série 14 (Ensino Médio) no nível 4 de proficiência em Língua Portuguesa. |
| `nivel_5_LP14` | STRING | Percentual de alunos da Série 14 (Ensino Médio) no nível 5 de proficiência em Língua Portuguesa. |
| `nivel_6_LP14` | STRING | Percentual de alunos da Série 14 (Ensino Médio) no nível 6 de proficiência em Língua Portuguesa. |
| `nivel_7_LP14` | STRING | Percentual de alunos da Série 14 (Ensino Médio) no nível 7 de proficiência em Língua Portuguesa. |
| `nivel_8_LP14` | STRING | Percentual de alunos da Série 14 (Ensino Médio) no nível 8 de proficiência em Língua Portuguesa. |
| `nivel_0_MT14` | STRING | Percentual de alunos da Série 14 (Ensino Médio) no nível 0 de proficiência em Matemática. |
| `nivel_1_MT14` | STRING | Percentual de alunos da Série 14 (Ensino Médio) no nível 1 de proficiência em Matemática. |
| `nivel_2_MT14` | STRING | Percentual de alunos da Série 14 (Ensino Médio) no nível 2 de proficiência em Matemática. |
| `nivel_3_MT14` | STRING | Percentual de alunos da Série 14 (Ensino Médio) no nível 3 de proficiência em Matemática. |
| `nivel_4_MT14` | STRING | Percentual de alunos da Série 14 (Ensino Médio) no nível 4 de proficiência em Matemática. |
| `nivel_5_MT14` | STRING | Percentual de alunos da Série 14 (Ensino Médio) no nível 5 de proficiência em Matemática. |
| `nivel_6_MT14` | STRING | Percentual de alunos da Série 14 (Ensino Médio) no nível 6 de proficiência em Matemática. |
| `nivel_7_MT14` | STRING | Percentual de alunos da Série 14 (Ensino Médio) no nível 7 de proficiência em Matemática. |
| `nivel_8_MT14` | STRING | Percentual de alunos da Série 14 (Ensino Médio) no nível 8 de proficiência em Matemática. |
| `nivel_9_MT14` | STRING | Percentual de alunos da Série 14 (Ensino Médio) no nível 9 de proficiência em Matemática. |
| `nivel_10_MT14` | STRING | Percentual de alunos da Série 14 (Ensino Médio) no nível 10 de proficiência em Matemática. |
| `dt_ingestao_lake` | TIMESTAMP | Data e hora em que os dados foram carregados na camada do Data Lake (AAAA-MM-DD HH:MM:SS). — descrição gerada por IA. |

## trusted · api_saeb_boletim_desempenho

File `trusted__api_saeb_boletim_desempenho.parquet` · 1,206,898 rows · 34 columns

Desempenho por escola/edicao/serie/disciplina no SAEB. Grao: 1 linha por (co_entidade, ano, id_serie, co_disciplina). Inclui proficiencias medias e distribuicao de alunos por nivel (0-10) para 5 benchmarks. Fonte: API saeb.inep.gov.br.

**Built from:** `raw/api_saeb_boletim_raw`

**Feeds:** `semantic/obt_api_saeb_boletim`

| Column | Type | Description |
|---|---|---|
| `co_entidade` | INTEGER | Codigo INEP da escola/entidade. |
| `ano` | INTEGER | Ano de referencia. |
| `co_disciplina` | INTEGER | Codigo da disciplina. |
| `no_disciplina` | STRING | Nome da disciplina (Lingua Portuguesa/Matematica). |
| `id_serie` | INTEGER | Codigo da serie/ano avaliado. |
| `ds_serie` | STRING | Descricao da serie/ano avaliado. |
| `profic_escola` | FLOAT | Proficiencia media no Saeb (escola). |
| `profic_similares` | FLOAT | Proficiencia media no Saeb (similares). |
| `profic_municipio` | FLOAT | Proficiencia media no Saeb (municipio). |
| `profic_estado` | FLOAT | Proficiencia media no Saeb (estado). |
| `profic_brasil` | FLOAT | Proficiencia media no Saeb (brasil). |
| `esc_nivel_0_pct` | FLOAT | Saeb: percentual de alunos no nivel 0 de proficiencia (da escola). |
| `esc_nivel_1_pct` | FLOAT | Saeb: percentual de alunos no nivel 1 de proficiencia (da escola). |
| `esc_nivel_2_pct` | FLOAT | Saeb: percentual de alunos no nivel 2 de proficiencia (da escola). |
| `esc_nivel_3_pct` | FLOAT | Saeb: percentual de alunos no nivel 3 de proficiencia (da escola). |
| `esc_nivel_4_pct` | FLOAT | Saeb: percentual de alunos no nivel 4 de proficiencia (da escola). |
| `esc_nivel_5_pct` | FLOAT | Saeb: percentual de alunos no nivel 5 de proficiencia (da escola). |
| `esc_nivel_6_pct` | FLOAT | Saeb: percentual de alunos no nivel 6 de proficiencia (da escola). |
| `esc_nivel_7_pct` | FLOAT | Saeb: percentual de alunos no nivel 7 de proficiencia (da escola). |
| `esc_nivel_8_pct` | FLOAT | Saeb: percentual de alunos no nivel 8 de proficiencia (da escola). |
| `esc_nivel_9_pct` | FLOAT | Saeb: percentual de alunos no nivel 9 de proficiencia (da escola). |
| `esc_nivel_10_pct` | FLOAT | Saeb: percentual de alunos no nivel 10 de proficiencia (da escola). |
| `sim_nivel_0_pct` | FLOAT | Saeb: percentual de alunos no nivel 0 de proficiencia (de escolas similares). |
| `sim_nivel_1_pct` | FLOAT | Saeb: percentual de alunos no nivel 1 de proficiencia (de escolas similares). |
| `sim_nivel_2_pct` | FLOAT | Saeb: percentual de alunos no nivel 2 de proficiencia (de escolas similares). |
| `sim_nivel_3_pct` | FLOAT | Saeb: percentual de alunos no nivel 3 de proficiencia (de escolas similares). |
| `sim_nivel_4_pct` | FLOAT | Saeb: percentual de alunos no nivel 4 de proficiencia (de escolas similares). |
| `sim_nivel_5_pct` | FLOAT | Saeb: percentual de alunos no nivel 5 de proficiencia (de escolas similares). |
| `sim_nivel_6_pct` | FLOAT | Saeb: percentual de alunos no nivel 6 de proficiencia (de escolas similares). |
| `sim_nivel_7_pct` | FLOAT | Saeb: percentual de alunos no nivel 7 de proficiencia (de escolas similares). |
| `sim_nivel_8_pct` | FLOAT | Saeb: percentual de alunos no nivel 8 de proficiencia (de escolas similares). |
| `sim_nivel_9_pct` | FLOAT | Saeb: percentual de alunos no nivel 9 de proficiencia (de escolas similares). |
| `sim_nivel_10_pct` | FLOAT | Saeb: percentual de alunos no nivel 10 de proficiencia (de escolas similares). |
| `dt_extracao` | STRING | Timestamp UTC da extracao da fonte. |

## trusted · api_saeb_boletim_escola_edicao

File `trusted__api_saeb_boletim_escola_edicao.parquet` · 464,749 rows · 20 columns

Metadados e indicadores de contexto de cada escola por edicao do SAEB. Grao: 1 linha por (co_entidade, ano). Inclui INSE, formacao docente e contagens de participacao por serie. Edicoes 2011-2015 tem metadados parciais. Fonte: API saeb.inep.gov.br.

**Built from:** `raw/api_saeb_boletim_raw`

**Feeds:** `semantic/obt_api_saeb_boletim`

| Column | Type | Description |
|---|---|---|
| `co_entidade` | INTEGER | Codigo INEP da escola/entidade. |
| `ano` | INTEGER | Ano de referencia. |
| `no_escola` | STRING | Nome da escola. |
| `sg_uf` | STRING | Sigla da UF. |
| `no_municipio` | STRING | Nome do municipio. |
| `ds_tipo_rede` | STRING | Descricao. |
| `no_inse` | STRING | Nome. |
| `perc_doc_sup_anos_iniciais` | FLOAT | Percentual de docentes com curso superior. |
| `perc_doc_sup_anos_finais` | FLOAT | Percentual de docentes com curso superior. |
| `perc_doc_sup_ensino_medio` | FLOAT | Percentual de docentes com curso superior. |
| `matriculados_5ef` | INTEGER | Total de alunos matriculados no 5º ano do Ensino Fundamental previstos para a avaliação. — descrição gerada por IA. |
| `presentes_5ef` | INTEGER | Quantidade de alunos do 5º ano do Ensino Fundamental efetivamente presentes no dia do exame. — descrição gerada por IA. |
| `tx_participacao_5ef` | FLOAT | Taxa de participacao dos alunos na avaliacao (%). |
| `matriculados_9ef` | INTEGER | Total de alunos matriculados no 9º ano do Ensino Fundamental previstos para a avaliação. — descrição gerada por IA. |
| `presentes_9ef` | INTEGER | Quantidade de alunos do 9º ano do Ensino Fundamental efetivamente presentes no dia do exame. — descrição gerada por IA. |
| `tx_participacao_9ef` | FLOAT | Taxa de participacao dos alunos na avaliacao (%). |
| `matriculados_3em` | INTEGER | Total de alunos matriculados no 3º ano do Ensino Médio previstos para a avaliação. — descrição gerada por IA. |
| `presentes_3em` | INTEGER | Quantidade de alunos do 3º ano do Ensino Médio efetivamente presentes no dia do exame. — descrição gerada por IA. |
| `tx_participacao_3em` | FLOAT | Taxa de participacao dos alunos na avaliacao (%). |
| `dt_extracao` | STRING | Timestamp UTC da extracao da fonte. |

## trusted · inep_saeb_escola

File `trusted__inep_saeb_escola.parquet` · 402,323 rows · 20 columns

SAEB microdados — escolas avaliadas, todos os anos.

**Built from:** `raw/inep_saeb_microdados_csv_2013_ts_escola`, `raw/inep_saeb_microdados_csv_2015_ts_escola`, `raw/inep_saeb_microdados_csv_2017_ts_escola`, `raw/inep_saeb_microdados_csv_2019_ts_escola`, `raw/inep_saeb_microdados_csv_2021_ts_escola`, `raw/inep_saeb_microdados_csv_2023_ts_escola`

**Feeds:** `semantic/obt_inep_saeb_micro_escola_ano`, `semantic/obt_inep_saeb_micro_municipio_ano`

| Column | Type | Description |
|---|---|---|
| `ano_saeb` | INTEGER | Ano da edicao do Saeb. |
| `id_saeb` | STRING | Id saeb. |
| `id_regiao` | INTEGER | Código identificador da região geográfica da escola. — descrição gerada por IA. |
| `id_uf` | INTEGER | Código IBGE do estado (UF) de localização da escola. — descrição gerada por IA. |
| `co_municipio` | INTEGER | Codigo IBGE do municipio. |
| `sg_uf` | STRING | Sigla da UF. |
| `no_municipio` | STRING | Nome do municipio. |
| `id_escola` | STRING | Codigo INEP da escola (8 digitos). |
| `no_escola` | STRING | Nome da escola. |
| `id_dependencia_adm` | INTEGER | Id dependencia adm. |
| `id_localizacao` | INTEGER | Id localizacao. |
| `nivel_socio_economico` | STRING | Nivel socio economico. |
| `media_5ef_lp` | FLOAT | Media 5ef lp. |
| `media_5ef_mt` | FLOAT | Media 5ef mt. |
| `media_9ef_lp` | FLOAT | Media 9ef lp. |
| `media_9ef_mt` | FLOAT | Media 9ef mt. |
| `media_3em_lp` | FLOAT | Media 3em lp. |
| `media_3em_mt` | FLOAT | Media 3em mt. |
| `dados_json` | STRING | Dados json. |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC da carga no lake. |

## trusted · inep_saeb_indicadores_brasil

File `trusted__inep_saeb_indicadores_brasil.parquet` · 453 rows · 178 columns

SAEB Planilha de Resultados — nível nacional. Fonte: INEP.

**Built from:** `raw/saeb_indicadores_brasil`

**Feeds:** `semantic/obt_inep_saeb_indicadores_brasil_ano`

| Column | Type | Description |
|---|---|---|
| `ano_saeb` | INTEGER | Ano de aplicação do Saeb |
| `id_agregacao` | STRING | Nível de agregação do resultado (Brasil, Pública, Federal, etc.) |
| `dependencia_adm` | STRING | Dependência administrativa (Pública, Federal, Estadual, Municipal, Privada) |
| `localizacao` | STRING | Localização (Urbana / Rural / Total) |
| `capital` | STRING | Capital ou Interior |
| `tx_alfabetizado` | STRING | TX_ALFABETIZADO |
| `media_2_lp` | FLOAT | Média em Língua Portuguesa 2º ano EF |
| `media_2_mt` | FLOAT | Média em Matemática 2º ano EF |
| `pc_alfabetizado` | FLOAT | Percentual de alunos alfabetizados (2º ano EF) |
| `media_5_lp` | FLOAT | Média em Língua Portuguesa 5º ano EF |
| `media_5_mt` | FLOAT | Média em Matemática 5º ano EF |
| `media_5_ch` | FLOAT | Média em Ciências Humanas 5º ano EF |
| `media_5_cn` | FLOAT | Média em Ciências da Natureza 5º ano EF |
| `media_9_lp` | FLOAT | Média em Língua Portuguesa 9º ano EF |
| `media_9_mt` | FLOAT | Média em Matemática 9º ano EF |
| `media_9_ch` | FLOAT | Média em Ciências Humanas 9º ano EF |
| `media_9_cn` | FLOAT | Média em Ciências da Natureza 9º ano EF |
| `media_12_lp` | FLOAT | Média em LP — EM tradicional |
| `media_12_mt` | FLOAT | Média em MT — EM tradicional |
| `media_13_lp` | FLOAT | Média em LP — EM integrado |
| `media_13_mt` | FLOAT | Média em MT — EM integrado |
| `media_14_lp` | FLOAT | Média em LP — EM (tradicional ou integrado) |
| `media_14_mt` | FLOAT | Média em MT — EM (tradicional ou integrado) |
| `nivel_0_lp2` | FLOAT | nivel_0_LP2 |
| `nivel_1_lp2` | FLOAT | nivel_1_LP2 |
| `nivel_2_lp2` | FLOAT | nivel_2_LP2 |
| `nivel_3_lp2` | FLOAT | nivel_3_LP2 |
| `nivel_4_lp2` | FLOAT | nivel_4_LP2 |
| `nivel_5_lp2` | FLOAT | nivel_5_LP2 |
| `nivel_6_lp2` | FLOAT | nivel_6_LP2 |
| `nivel_7_lp2` | FLOAT | nivel_7_LP2 |
| `nivel_8_lp2` | FLOAT | nivel_8_LP2 |
| `nivel_0_mt2` | FLOAT | nivel_0_MT2 |
| `nivel_1_mt2` | FLOAT | nivel_1_MT2 |
| `nivel_2_mt2` | FLOAT | nivel_2_MT2 |
| `nivel_3_mt2` | FLOAT | nivel_3_MT2 |
| `nivel_4_mt2` | FLOAT | nivel_4_MT2 |
| `nivel_5_mt2` | FLOAT | nivel_5_MT2 |
| `nivel_6_mt2` | FLOAT | nivel_6_MT2 |
| `nivel_7_mt2` | FLOAT | nivel_7_MT2 |
| `nivel_8_mt2` | FLOAT | nivel_8_MT2 |
| `nivel_0_lp5` | FLOAT | nivel_0_LP5 |
| `nivel_1_lp5` | FLOAT | nivel_1_LP5 |
| `nivel_2_lp5` | FLOAT | nivel_2_LP5 |
| `nivel_3_lp5` | FLOAT | nivel_3_LP5 |
| `nivel_4_lp5` | FLOAT | nivel_4_LP5 |
| `nivel_5_lp5` | FLOAT | nivel_5_LP5 |
| `nivel_6_lp5` | FLOAT | nivel_6_LP5 |
| `nivel_7_lp5` | FLOAT | nivel_7_LP5 |
| `nivel_8_lp5` | FLOAT | nivel_8_LP5 |
| `nivel_9_lp5` | FLOAT | nivel_9_LP5 |
| `nivel_0_mt5` | FLOAT | nivel_0_MT5 |
| `nivel_1_mt5` | FLOAT | nivel_1_MT5 |
| `nivel_2_mt5` | FLOAT | nivel_2_MT5 |
| `nivel_3_mt5` | FLOAT | nivel_3_MT5 |
| `nivel_4_mt5` | FLOAT | nivel_4_MT5 |
| `nivel_5_mt5` | FLOAT | nivel_5_MT5 |
| `nivel_6_mt5` | FLOAT | nivel_6_MT5 |
| `nivel_7_mt5` | FLOAT | nivel_7_MT5 |
| `nivel_8_mt5` | FLOAT | nivel_8_MT5 |
| `nivel_9_mt5` | FLOAT | nivel_9_MT5 |
| `nivel_10_mt5` | FLOAT | nivel_10_MT5 |
| `nivel_0_ch5` | FLOAT | nivel_0_CH5 |
| `nivel_1_ch5` | FLOAT | nivel_1_CH5 |
| `nivel_2_ch5` | FLOAT | nivel_2_CH5 |
| `nivel_3_ch5` | FLOAT | nivel_3_CH5 |
| `nivel_4_ch5` | FLOAT | nivel_4_CH5 |
| `nivel_5_ch5` | FLOAT | nivel_5_CH5 |
| `nivel_6_ch5` | FLOAT | nivel_6_CH5 |
| `nivel_7_ch5` | FLOAT | nivel_7_CH5 |
| `nivel_0_cn5` | FLOAT | nivel_0_CN5 |
| `nivel_1_cn5` | FLOAT | nivel_1_CN5 |
| `nivel_2_cn5` | FLOAT | nivel_2_CN5 |
| `nivel_3_cn5` | FLOAT | nivel_3_CN5 |
| `nivel_4_cn5` | FLOAT | nivel_4_CN5 |
| `nivel_5_cn5` | FLOAT | nivel_5_CN5 |
| `nivel_6_cn5` | FLOAT | nivel_6_CN5 |
| `nivel_7_cn5` | FLOAT | nivel_7_CN5 |
| `nivel_8_cn5` | FLOAT | nivel_8_CN5 |
| `nivel_0_lp9` | FLOAT | nivel_0_LP9 |
| `nivel_1_lp9` | FLOAT | nivel_1_LP9 |
| `nivel_2_lp9` | FLOAT | nivel_2_LP9 |
| `nivel_3_lp9` | FLOAT | nivel_3_LP9 |
| `nivel_4_lp9` | FLOAT | nivel_4_LP9 |
| `nivel_5_lp9` | FLOAT | nivel_5_LP9 |
| `nivel_6_lp9` | FLOAT | nivel_6_LP9 |
| `nivel_7_lp9` | FLOAT | nivel_7_LP9 |
| `nivel_8_lp9` | FLOAT | nivel_8_LP9 |
| `nivel_0_mt9` | FLOAT | nivel_0_MT9 |
| `nivel_1_mt9` | FLOAT | nivel_1_MT9 |
| `nivel_2_mt9` | FLOAT | nivel_2_MT9 |
| `nivel_3_mt9` | FLOAT | nivel_3_MT9 |
| `nivel_4_mt9` | FLOAT | nivel_4_MT9 |
| `nivel_5_mt9` | FLOAT | nivel_5_MT9 |
| `nivel_6_mt9` | FLOAT | nivel_6_MT9 |
| `nivel_7_mt9` | FLOAT | nivel_7_MT9 |
| `nivel_8_mt9` | FLOAT | nivel_8_MT9 |
| `nivel_9_mt9` | FLOAT | nivel_9_MT9 |
| `nivel_0_ch9` | FLOAT | nivel_0_CH9 |
| `nivel_1_ch9` | FLOAT | nivel_1_CH9 |
| `nivel_2_ch9` | FLOAT | nivel_2_CH9 |
| `nivel_3_ch9` | FLOAT | nivel_3_CH9 |
| `nivel_4_ch9` | FLOAT | nivel_4_CH9 |
| `nivel_5_ch9` | FLOAT | nivel_5_CH9 |
| `nivel_6_ch9` | FLOAT | nivel_6_CH9 |
| `nivel_7_ch9` | FLOAT | nivel_7_CH9 |
| `nivel_8_ch9` | FLOAT | nivel_8_CH9 |
| `nivel_9_ch9` | FLOAT | nivel_9_CH9 |
| `nivel_0_cn9` | FLOAT | nivel_0_CN9 |
| `nivel_1_cn9` | FLOAT | nivel_1_CN9 |
| `nivel_2_cn9` | FLOAT | nivel_2_CN9 |
| `nivel_3_cn9` | FLOAT | nivel_3_CN9 |
| `nivel_4_cn9` | FLOAT | nivel_4_CN9 |
| `nivel_5_cn9` | FLOAT | nivel_5_CN9 |
| `nivel_6_cn9` | FLOAT | nivel_6_CN9 |
| `nivel_7_cn9` | FLOAT | nivel_7_CN9 |
| `nivel_8_cn9` | FLOAT | nivel_8_CN9 |
| `nivel_0_lp12` | FLOAT | nivel_0_LP12 |
| `nivel_1_lp12` | FLOAT | nivel_1_LP12 |
| `nivel_2_lp12` | FLOAT | nivel_2_LP12 |
| `nivel_3_lp12` | FLOAT | nivel_3_LP12 |
| `nivel_4_lp12` | FLOAT | nivel_4_LP12 |
| `nivel_5_lp12` | FLOAT | nivel_5_LP12 |
| `nivel_6_lp12` | FLOAT | nivel_6_LP12 |
| `nivel_7_lp12` | FLOAT | nivel_7_LP12 |
| `nivel_8_lp12` | FLOAT | nivel_8_LP12 |
| `nivel_0_mt12` | FLOAT | nivel_0_MT12 |
| `nivel_1_mt12` | FLOAT | nivel_1_MT12 |
| `nivel_2_mt12` | FLOAT | nivel_2_MT12 |
| `nivel_3_mt12` | FLOAT | nivel_3_MT12 |
| `nivel_4_mt12` | FLOAT | nivel_4_MT12 |
| `nivel_5_mt12` | FLOAT | nivel_5_MT12 |
| `nivel_6_mt12` | FLOAT | nivel_6_MT12 |
| `nivel_7_mt12` | FLOAT | nivel_7_MT12 |
| `nivel_8_mt12` | FLOAT | nivel_8_MT12 |
| `nivel_9_mt12` | FLOAT | nivel_9_MT12 |
| `nivel_10_mt12` | FLOAT | nivel_10_MT12 |
| `nivel_0_lp13` | FLOAT | nivel_0_LP13 |
| `nivel_1_lp13` | FLOAT | nivel_1_LP13 |
| `nivel_2_lp13` | FLOAT | nivel_2_LP13 |
| `nivel_3_lp13` | FLOAT | nivel_3_LP13 |
| `nivel_4_lp13` | FLOAT | nivel_4_LP13 |
| `nivel_5_lp13` | FLOAT | nivel_5_LP13 |
| `nivel_6_lp13` | FLOAT | nivel_6_LP13 |
| `nivel_7_lp13` | FLOAT | nivel_7_LP13 |
| `nivel_8_lp13` | FLOAT | nivel_8_LP13 |
| `nivel_0_mt13` | FLOAT | nivel_0_MT13 |
| `nivel_1_mt13` | FLOAT | nivel_1_MT13 |
| `nivel_2_mt13` | FLOAT | nivel_2_MT13 |
| `nivel_3_mt13` | FLOAT | nivel_3_MT13 |
| `nivel_4_mt13` | FLOAT | nivel_4_MT13 |
| `nivel_5_mt13` | FLOAT | nivel_5_MT13 |
| `nivel_6_mt13` | FLOAT | nivel_6_MT13 |
| `nivel_7_mt13` | FLOAT | nivel_7_MT13 |
| `nivel_8_mt13` | FLOAT | nivel_8_MT13 |
| `nivel_9_mt13` | FLOAT | nivel_9_MT13 |
| `nivel_10_mt13` | FLOAT | nivel_10_MT13 |
| `nivel_0_lp14` | FLOAT | nivel_0_LP14 |
| `nivel_1_lp14` | FLOAT | nivel_1_LP14 |
| `nivel_2_lp14` | FLOAT | nivel_2_LP14 |
| `nivel_3_lp14` | FLOAT | nivel_3_LP14 |
| `nivel_4_lp14` | FLOAT | nivel_4_LP14 |
| `nivel_5_lp14` | FLOAT | nivel_5_LP14 |
| `nivel_6_lp14` | FLOAT | nivel_6_LP14 |
| `nivel_7_lp14` | FLOAT | nivel_7_LP14 |
| `nivel_8_lp14` | FLOAT | nivel_8_LP14 |
| `nivel_0_mt14` | FLOAT | nivel_0_MT14 |
| `nivel_1_mt14` | FLOAT | nivel_1_MT14 |
| `nivel_2_mt14` | FLOAT | nivel_2_MT14 |
| `nivel_3_mt14` | FLOAT | nivel_3_MT14 |
| `nivel_4_mt14` | FLOAT | nivel_4_MT14 |
| `nivel_5_mt14` | FLOAT | nivel_5_MT14 |
| `nivel_6_mt14` | FLOAT | nivel_6_MT14 |
| `nivel_7_mt14` | FLOAT | nivel_7_MT14 |
| `nivel_8_mt14` | FLOAT | nivel_8_MT14 |
| `nivel_9_mt14` | FLOAT | nivel_9_MT14 |
| `nivel_10_mt14` | FLOAT | nivel_10_MT14 |
| `dt_ingestao_lake` | TIMESTAMP | Data e hora do processamento/ingestão do registro no Data Lake (formato YYYY-MM-DD HH:MM:SS). — descrição gerada por IA. |

## trusted · inep_saeb_indicadores_erros_amostrais

File `trusted__inep_saeb_indicadores_erros_amostrais.parquet` · 429 rows · 11 columns

SAEB Planilha — erros amostrais e IC por série/disciplina. Fonte: INEP.

| Column | Type | Description |
|---|---|---|
| `ano_saeb` | INTEGER | Ano de aplicação do Saeb |
| `serie` | STRING | Série/ano de escolaridade avaliada (2EF, 5EF, 9EF, 12EM) |
| `disciplina` | STRING | Disciplina avaliada (LP, MT, CH, CN, Alfabetizacao) |
| `proficiencia` | STRING | Faixa ou nível de proficiência SAEB |
| `abrangencia` | STRING | Abrangência geográfica/administrativa |
| `media` | FLOAT | Média de proficiência para esta faixa e abrangência |
| `erro_amostral` | FLOAT | Erro amostral associado à média estimada |
| `ic_inferior` | FLOAT | Limite inferior do intervalo de confiança (95%) |
| `ic_superior` | FLOAT | Limite superior do intervalo de confiança (95%) |
| `erro_padrao` | FLOAT | Erro padrão da estimativa de proficiência |
| `dt_ingestao_lake` | TIMESTAMP | Data e hora do processamento e ingestão do registro no Data Lake (formato YYYY-MM-DD HH:MM:SS). — descrição gerada por IA. |

## trusted · inep_saeb_indicadores_estados

File `trusted__inep_saeb_indicadores_estados.parquet` · 9,917 rows · 179 columns

SAEB Planilha de Resultados — nível estadual (UF). Fonte: INEP.

**Built from:** `raw/saeb_indicadores_estados`

**Feeds:** `semantic/obt_inep_saeb_indicadores_estado_ano`

| Column | Type | Description |
|---|---|---|
| `ano_saeb` | INTEGER | Ano de aplicação do Saeb |
| `co_uf` | INTEGER | Código da Unidade da Federação (IBGE) |
| `no_uf` | STRING | Nome da Unidade da Federação |
| `dependencia_adm` | STRING | Dependência administrativa (Pública, Federal, Estadual, Municipal, Privada) |
| `localizacao` | STRING | Localização (Urbana / Rural / Total) |
| `capital` | STRING | Capital ou Interior |
| `tx_alfabetizado` | STRING | TX_ALFABETIZADO |
| `media_2_lp` | FLOAT | Média em Língua Portuguesa 2º ano EF |
| `media_2_mt` | FLOAT | Média em Matemática 2º ano EF |
| `pc_alfabetizado` | FLOAT | Percentual de alunos alfabetizados (2º ano EF) |
| `media_5_lp` | FLOAT | Média em Língua Portuguesa 5º ano EF |
| `media_5_mt` | FLOAT | Média em Matemática 5º ano EF |
| `media_5_ch` | FLOAT | Média em Ciências Humanas 5º ano EF |
| `media_5_cn` | FLOAT | Média em Ciências da Natureza 5º ano EF |
| `media_9_lp` | FLOAT | Média em Língua Portuguesa 9º ano EF |
| `media_9_mt` | FLOAT | Média em Matemática 9º ano EF |
| `media_9_ch` | FLOAT | Média em Ciências Humanas 9º ano EF |
| `media_9_cn` | FLOAT | Média em Ciências da Natureza 9º ano EF |
| `media_12_lp` | FLOAT | Média em LP — EM tradicional |
| `media_12_mt` | FLOAT | Média em MT — EM tradicional |
| `media_13_lp` | FLOAT | Média em LP — EM integrado |
| `media_13_mt` | FLOAT | Média em MT — EM integrado |
| `media_14_lp` | FLOAT | Média em LP — EM (tradicional ou integrado) |
| `media_14_mt` | FLOAT | Média em MT — EM (tradicional ou integrado) |
| `nivel_0_lp2` | FLOAT | nivel_0_LP2 |
| `nivel_1_lp2` | FLOAT | nivel_1_LP2 |
| `nivel_2_lp2` | FLOAT | nivel_2_LP2 |
| `nivel_3_lp2` | FLOAT | nivel_3_LP2 |
| `nivel_4_lp2` | FLOAT | nivel_4_LP2 |
| `nivel_5_lp2` | FLOAT | nivel_5_LP2 |
| `nivel_6_lp2` | FLOAT | nivel_6_LP2 |
| `nivel_7_lp2` | FLOAT | nivel_7_LP2 |
| `nivel_8_lp2` | FLOAT | nivel_8_LP2 |
| `nivel_0_mt2` | FLOAT | nivel_0_MT2 |
| `nivel_1_mt2` | FLOAT | nivel_1_MT2 |
| `nivel_2_mt2` | FLOAT | nivel_2_MT2 |
| `nivel_3_mt2` | FLOAT | nivel_3_MT2 |
| `nivel_4_mt2` | FLOAT | nivel_4_MT2 |
| `nivel_5_mt2` | FLOAT | nivel_5_MT2 |
| `nivel_6_mt2` | FLOAT | nivel_6_MT2 |
| `nivel_7_mt2` | FLOAT | nivel_7_MT2 |
| `nivel_8_mt2` | FLOAT | nivel_8_MT2 |
| `nivel_0_lp5` | FLOAT | nivel_0_LP5 |
| `nivel_1_lp5` | FLOAT | nivel_1_LP5 |
| `nivel_2_lp5` | FLOAT | nivel_2_LP5 |
| `nivel_3_lp5` | FLOAT | nivel_3_LP5 |
| `nivel_4_lp5` | FLOAT | nivel_4_LP5 |
| `nivel_5_lp5` | FLOAT | nivel_5_LP5 |
| `nivel_6_lp5` | FLOAT | nivel_6_LP5 |
| `nivel_7_lp5` | FLOAT | nivel_7_LP5 |
| `nivel_8_lp5` | FLOAT | nivel_8_LP5 |
| `nivel_9_lp5` | FLOAT | nivel_9_LP5 |
| `nivel_0_mt5` | FLOAT | nivel_0_MT5 |
| `nivel_1_mt5` | FLOAT | nivel_1_MT5 |
| `nivel_2_mt5` | FLOAT | nivel_2_MT5 |
| `nivel_3_mt5` | FLOAT | nivel_3_MT5 |
| `nivel_4_mt5` | FLOAT | nivel_4_MT5 |
| `nivel_5_mt5` | FLOAT | nivel_5_MT5 |
| `nivel_6_mt5` | FLOAT | nivel_6_MT5 |
| `nivel_7_mt5` | FLOAT | nivel_7_MT5 |
| `nivel_8_mt5` | FLOAT | nivel_8_MT5 |
| `nivel_9_mt5` | FLOAT | nivel_9_MT5 |
| `nivel_10_mt5` | FLOAT | nivel_10_MT5 |
| `nivel_0_ch5` | FLOAT | nivel_0_CH5 |
| `nivel_1_ch5` | FLOAT | nivel_1_CH5 |
| `nivel_2_ch5` | FLOAT | nivel_2_CH5 |
| `nivel_3_ch5` | FLOAT | nivel_3_CH5 |
| `nivel_4_ch5` | FLOAT | nivel_4_CH5 |
| `nivel_5_ch5` | FLOAT | nivel_5_CH5 |
| `nivel_6_ch5` | FLOAT | nivel_6_CH5 |
| `nivel_7_ch5` | FLOAT | nivel_7_CH5 |
| `nivel_0_cn5` | FLOAT | nivel_0_CN5 |
| `nivel_1_cn5` | FLOAT | nivel_1_CN5 |
| `nivel_2_cn5` | FLOAT | nivel_2_CN5 |
| `nivel_3_cn5` | FLOAT | nivel_3_CN5 |
| `nivel_4_cn5` | FLOAT | nivel_4_CN5 |
| `nivel_5_cn5` | FLOAT | nivel_5_CN5 |
| `nivel_6_cn5` | FLOAT | nivel_6_CN5 |
| `nivel_7_cn5` | FLOAT | nivel_7_CN5 |
| `nivel_8_cn5` | FLOAT | nivel_8_CN5 |
| `nivel_0_lp9` | FLOAT | nivel_0_LP9 |
| `nivel_1_lp9` | FLOAT | nivel_1_LP9 |
| `nivel_2_lp9` | FLOAT | nivel_2_LP9 |
| `nivel_3_lp9` | FLOAT | nivel_3_LP9 |
| `nivel_4_lp9` | FLOAT | nivel_4_LP9 |
| `nivel_5_lp9` | FLOAT | nivel_5_LP9 |
| `nivel_6_lp9` | FLOAT | nivel_6_LP9 |
| `nivel_7_lp9` | FLOAT | nivel_7_LP9 |
| `nivel_8_lp9` | FLOAT | nivel_8_LP9 |
| `nivel_0_mt9` | FLOAT | nivel_0_MT9 |
| `nivel_1_mt9` | FLOAT | nivel_1_MT9 |
| `nivel_2_mt9` | FLOAT | nivel_2_MT9 |
| `nivel_3_mt9` | FLOAT | nivel_3_MT9 |
| `nivel_4_mt9` | FLOAT | nivel_4_MT9 |
| `nivel_5_mt9` | FLOAT | nivel_5_MT9 |
| `nivel_6_mt9` | FLOAT | nivel_6_MT9 |
| `nivel_7_mt9` | FLOAT | nivel_7_MT9 |
| `nivel_8_mt9` | FLOAT | nivel_8_MT9 |
| `nivel_9_mt9` | FLOAT | nivel_9_MT9 |
| `nivel_0_ch9` | FLOAT | nivel_0_CH9 |
| `nivel_1_ch9` | FLOAT | nivel_1_CH9 |
| `nivel_2_ch9` | FLOAT | nivel_2_CH9 |
| `nivel_3_ch9` | FLOAT | nivel_3_CH9 |
| `nivel_4_ch9` | FLOAT | nivel_4_CH9 |
| `nivel_5_ch9` | FLOAT | nivel_5_CH9 |
| `nivel_6_ch9` | FLOAT | nivel_6_CH9 |
| `nivel_7_ch9` | FLOAT | nivel_7_CH9 |
| `nivel_8_ch9` | FLOAT | nivel_8_CH9 |
| `nivel_9_ch9` | FLOAT | nivel_9_CH9 |
| `nivel_0_cn9` | FLOAT | nivel_0_CN9 |
| `nivel_1_cn9` | FLOAT | nivel_1_CN9 |
| `nivel_2_cn9` | FLOAT | nivel_2_CN9 |
| `nivel_3_cn9` | FLOAT | nivel_3_CN9 |
| `nivel_4_cn9` | FLOAT | nivel_4_CN9 |
| `nivel_5_cn9` | FLOAT | nivel_5_CN9 |
| `nivel_6_cn9` | FLOAT | nivel_6_CN9 |
| `nivel_7_cn9` | FLOAT | nivel_7_CN9 |
| `nivel_8_cn9` | FLOAT | nivel_8_CN9 |
| `nivel_0_lp12` | FLOAT | nivel_0_LP12 |
| `nivel_1_lp12` | FLOAT | nivel_1_LP12 |
| `nivel_2_lp12` | FLOAT | nivel_2_LP12 |
| `nivel_3_lp12` | FLOAT | nivel_3_LP12 |
| `nivel_4_lp12` | FLOAT | nivel_4_LP12 |
| `nivel_5_lp12` | FLOAT | nivel_5_LP12 |
| `nivel_6_lp12` | FLOAT | nivel_6_LP12 |
| `nivel_7_lp12` | FLOAT | nivel_7_LP12 |
| `nivel_8_lp12` | FLOAT | nivel_8_LP12 |
| `nivel_0_mt12` | FLOAT | nivel_0_MT12 |
| `nivel_1_mt12` | FLOAT | nivel_1_MT12 |
| `nivel_2_mt12` | FLOAT | nivel_2_MT12 |
| `nivel_3_mt12` | FLOAT | nivel_3_MT12 |
| `nivel_4_mt12` | FLOAT | nivel_4_MT12 |
| `nivel_5_mt12` | FLOAT | nivel_5_MT12 |
| `nivel_6_mt12` | FLOAT | nivel_6_MT12 |
| `nivel_7_mt12` | FLOAT | nivel_7_MT12 |
| `nivel_8_mt12` | FLOAT | nivel_8_MT12 |
| `nivel_9_mt12` | FLOAT | nivel_9_MT12 |
| `nivel_10_mt12` | FLOAT | nivel_10_MT12 |
| `nivel_0_lp13` | FLOAT | nivel_0_LP13 |
| `nivel_1_lp13` | FLOAT | nivel_1_LP13 |
| `nivel_2_lp13` | FLOAT | nivel_2_LP13 |
| `nivel_3_lp13` | FLOAT | nivel_3_LP13 |
| `nivel_4_lp13` | FLOAT | nivel_4_LP13 |
| `nivel_5_lp13` | FLOAT | nivel_5_LP13 |
| `nivel_6_lp13` | FLOAT | nivel_6_LP13 |
| `nivel_7_lp13` | FLOAT | nivel_7_LP13 |
| `nivel_8_lp13` | FLOAT | nivel_8_LP13 |
| `nivel_0_mt13` | FLOAT | nivel_0_MT13 |
| `nivel_1_mt13` | FLOAT | nivel_1_MT13 |
| `nivel_2_mt13` | FLOAT | nivel_2_MT13 |
| `nivel_3_mt13` | FLOAT | nivel_3_MT13 |
| `nivel_4_mt13` | FLOAT | nivel_4_MT13 |
| `nivel_5_mt13` | FLOAT | nivel_5_MT13 |
| `nivel_6_mt13` | FLOAT | nivel_6_MT13 |
| `nivel_7_mt13` | FLOAT | nivel_7_MT13 |
| `nivel_8_mt13` | FLOAT | nivel_8_MT13 |
| `nivel_9_mt13` | FLOAT | nivel_9_MT13 |
| `nivel_10_mt13` | FLOAT | nivel_10_MT13 |
| `nivel_0_lp14` | FLOAT | nivel_0_LP14 |
| `nivel_1_lp14` | FLOAT | nivel_1_LP14 |
| `nivel_2_lp14` | FLOAT | nivel_2_LP14 |
| `nivel_3_lp14` | FLOAT | nivel_3_LP14 |
| `nivel_4_lp14` | FLOAT | nivel_4_LP14 |
| `nivel_5_lp14` | FLOAT | nivel_5_LP14 |
| `nivel_6_lp14` | FLOAT | nivel_6_LP14 |
| `nivel_7_lp14` | FLOAT | nivel_7_LP14 |
| `nivel_8_lp14` | FLOAT | nivel_8_LP14 |
| `nivel_0_mt14` | FLOAT | nivel_0_MT14 |
| `nivel_1_mt14` | FLOAT | nivel_1_MT14 |
| `nivel_2_mt14` | FLOAT | nivel_2_MT14 |
| `nivel_3_mt14` | FLOAT | nivel_3_MT14 |
| `nivel_4_mt14` | FLOAT | nivel_4_MT14 |
| `nivel_5_mt14` | FLOAT | nivel_5_MT14 |
| `nivel_6_mt14` | FLOAT | nivel_6_MT14 |
| `nivel_7_mt14` | FLOAT | nivel_7_MT14 |
| `nivel_8_mt14` | FLOAT | nivel_8_MT14 |
| `nivel_9_mt14` | FLOAT | nivel_9_MT14 |
| `nivel_10_mt14` | FLOAT | nivel_10_MT14 |
| `dt_ingestao_lake` | TIMESTAMP | Data e hora do processamento/carga do registro no Data Lake (YYYY-MM-DD HH:MM:SS). — descrição gerada por IA. |

## trusted · inep_saeb_indicadores_historico_brasil

File `trusted__inep_saeb_indicadores_historico_brasil.parquet` · 24 rows · 85 columns

SAEB Planilha de Resultados — nível nacional histórico 1995-2005. Até 14 níveis por série (0-13). Fonte: INEP.

**Built from:** `raw/saeb_indicadores_historico_brasil`

**Feeds:** `semantic/obt_inep_saeb_indicadores_historico_brasil_ano`

| Column | Type | Description |
|---|---|---|
| `ano_saeb` | INTEGER | Ano de aplicação do Saeb |
| `grupo` | STRING | GRUPO |
| `dependencia_adm` | STRING | Dependência administrativa (Pública, Federal, Estadual, Municipal, Privada) |
| `co_uf` | INTEGER | Código da Unidade da Federação (IBGE) |
| `no_uf` | STRING | Nome da Unidade da Federação |
| `tipo` | STRING | tipo |
| `nivel_0_mt5` | FLOAT | nivel_0_MT5 |
| `nivel_1_mt5` | FLOAT | nivel_1_MT5 |
| `nivel_2_mt5` | FLOAT | nivel_2_MT5 |
| `nivel_3_mt5` | FLOAT | nivel_3_MT5 |
| `nivel_4_mt5` | FLOAT | nivel_4_MT5 |
| `nivel_5_mt5` | FLOAT | nivel_5_MT5 |
| `nivel_6_mt5` | FLOAT | nivel_6_MT5 |
| `nivel_7_mt5` | FLOAT | nivel_7_MT5 |
| `nivel_8_mt5` | FLOAT | nivel_8_MT5 |
| `nivel_9_mt5` | FLOAT | nivel_9_MT5 |
| `nivel_10_mt5` | FLOAT | nivel_10_MT5 |
| `nivel_11_mt5` | FLOAT | nivel_11_MT5 |
| `nivel_12_mt5` | FLOAT | nivel_12_MT5 |
| `nivel_13_mt5` | FLOAT | nivel_13_MT5 |
| `nivel_0_mt9` | FLOAT | nivel_0_MT9 |
| `nivel_1_mt9` | FLOAT | nivel_1_MT9 |
| `nivel_2_mt9` | FLOAT | nivel_2_MT9 |
| `nivel_3_mt9` | FLOAT | nivel_3_MT9 |
| `nivel_4_mt9` | FLOAT | nivel_4_MT9 |
| `nivel_5_mt9` | FLOAT | nivel_5_MT9 |
| `nivel_6_mt9` | FLOAT | nivel_6_MT9 |
| `nivel_7_mt9` | FLOAT | nivel_7_MT9 |
| `nivel_8_mt9` | FLOAT | nivel_8_MT9 |
| `nivel_9_mt9` | FLOAT | nivel_9_MT9 |
| `nivel_10_mt9` | FLOAT | nivel_10_MT9 |
| `nivel_11_mt9` | FLOAT | nivel_11_MT9 |
| `nivel_12_mt9` | FLOAT | nivel_12_MT9 |
| `nivel_13_mt9` | FLOAT | nivel_13_MT9 |
| `nivel_0_mt12` | FLOAT | nivel_0_MT12 |
| `nivel_1_mt12` | FLOAT | nivel_1_MT12 |
| `nivel_2_mt12` | FLOAT | nivel_2_MT12 |
| `nivel_3_mt12` | FLOAT | nivel_3_MT12 |
| `nivel_4_mt12` | FLOAT | nivel_4_MT12 |
| `nivel_5_mt12` | FLOAT | nivel_5_MT12 |
| `nivel_6_mt12` | FLOAT | nivel_6_MT12 |
| `nivel_7_mt12` | FLOAT | nivel_7_MT12 |
| `nivel_8_mt12` | FLOAT | nivel_8_MT12 |
| `nivel_9_mt12` | FLOAT | nivel_9_MT12 |
| `nivel_10_mt12` | FLOAT | nivel_10_MT12 |
| `nivel_11_mt12` | FLOAT | nivel_11_MT12 |
| `nivel_12_mt12` | FLOAT | nivel_12_MT12 |
| `nivel_13_mt12` | FLOAT | nivel_13_MT12 |
| `nivel_0_lp5` | FLOAT | nivel_0_LP5 |
| `nivel_1_lp5` | FLOAT | nivel_1_LP5 |
| `nivel_2_lp5` | FLOAT | nivel_2_LP5 |
| `nivel_3_lp5` | FLOAT | nivel_3_LP5 |
| `nivel_4_lp5` | FLOAT | nivel_4_LP5 |
| `nivel_5_lp5` | FLOAT | nivel_5_LP5 |
| `nivel_6_lp5` | FLOAT | nivel_6_LP5 |
| `nivel_7_lp5` | FLOAT | nivel_7_LP5 |
| `nivel_8_lp5` | FLOAT | nivel_8_LP5 |
| `nivel_9_lp5` | FLOAT | nivel_9_LP5 |
| `nivel_10_lp5` | FLOAT | nivel_10_LP5 |
| `nivel_11_lp5` | FLOAT | nivel_11_LP5 |
| `nivel_0_lp9` | FLOAT | nivel_0_LP9 |
| `nivel_1_lp9` | FLOAT | nivel_1_LP9 |
| `nivel_2_lp9` | FLOAT | nivel_2_LP9 |
| `nivel_3_lp9` | FLOAT | nivel_3_LP9 |
| `nivel_4_lp9` | FLOAT | nivel_4_LP9 |
| `nivel_5_lp9` | FLOAT | nivel_5_LP9 |
| `nivel_6_lp9` | FLOAT | nivel_6_LP9 |
| `nivel_7_lp9` | FLOAT | nivel_7_LP9 |
| `nivel_8_lp9` | FLOAT | nivel_8_LP9 |
| `nivel_9_lp9` | FLOAT | nivel_9_LP9 |
| `nivel_10_lp9` | FLOAT | nivel_10_LP9 |
| `nivel_11_lp9` | FLOAT | nivel_11_LP9 |
| `nivel_0_lp12` | FLOAT | nivel_0_LP12 |
| `nivel_1_lp12` | FLOAT | nivel_1_LP12 |
| `nivel_2_lp12` | FLOAT | nivel_2_LP12 |
| `nivel_3_lp12` | FLOAT | nivel_3_LP12 |
| `nivel_4_lp12` | FLOAT | nivel_4_LP12 |
| `nivel_5_lp12` | FLOAT | nivel_5_LP12 |
| `nivel_6_lp12` | FLOAT | nivel_6_LP12 |
| `nivel_7_lp12` | FLOAT | nivel_7_LP12 |
| `nivel_8_lp12` | FLOAT | nivel_8_LP12 |
| `nivel_9_lp12` | FLOAT | nivel_9_LP12 |
| `nivel_10_lp12` | FLOAT | nivel_10_LP12 |
| `nivel_11_lp12` | FLOAT | nivel_11_LP12 |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC da carga no lake. |

## trusted · inep_saeb_indicadores_historico_estados

File `trusted__inep_saeb_indicadores_historico_estados.parquet` · 714 rows · 85 columns

SAEB Planilha de Resultados — nível estadual histórico 1995-2005. Até 14 níveis por série (0-13). Fonte: INEP.

**Built from:** `raw/saeb_indicadores_historico_estados`

**Feeds:** `semantic/obt_inep_saeb_indicadores_historico_estado_ano`

| Column | Type | Description |
|---|---|---|
| `ano_saeb` | INTEGER | Ano de aplicação do Saeb |
| `grupo` | STRING | GRUPO |
| `dependencia_adm` | STRING | Dependência administrativa (Pública, Federal, Estadual, Municipal, Privada) |
| `co_uf` | INTEGER | Código da Unidade da Federação (IBGE) |
| `no_uf` | STRING | Nome da Unidade da Federação |
| `tipo` | STRING | tipo |
| `nivel_0_mt5` | FLOAT | nivel_0_MT5 |
| `nivel_1_mt5` | FLOAT | nivel_1_MT5 |
| `nivel_2_mt5` | FLOAT | nivel_2_MT5 |
| `nivel_3_mt5` | FLOAT | nivel_3_MT5 |
| `nivel_4_mt5` | FLOAT | nivel_4_MT5 |
| `nivel_5_mt5` | FLOAT | nivel_5_MT5 |
| `nivel_6_mt5` | FLOAT | nivel_6_MT5 |
| `nivel_7_mt5` | FLOAT | nivel_7_MT5 |
| `nivel_8_mt5` | FLOAT | nivel_8_MT5 |
| `nivel_9_mt5` | FLOAT | nivel_9_MT5 |
| `nivel_10_mt5` | FLOAT | nivel_10_MT5 |
| `nivel_11_mt5` | FLOAT | nivel_11_MT5 |
| `nivel_12_mt5` | FLOAT | nivel_12_MT5 |
| `nivel_13_mt5` | FLOAT | nivel_13_MT5 |
| `nivel_0_mt9` | FLOAT | nivel_0_MT9 |
| `nivel_1_mt9` | FLOAT | nivel_1_MT9 |
| `nivel_2_mt9` | FLOAT | nivel_2_MT9 |
| `nivel_3_mt9` | FLOAT | nivel_3_MT9 |
| `nivel_4_mt9` | FLOAT | nivel_4_MT9 |
| `nivel_5_mt9` | FLOAT | nivel_5_MT9 |
| `nivel_6_mt9` | FLOAT | nivel_6_MT9 |
| `nivel_7_mt9` | FLOAT | nivel_7_MT9 |
| `nivel_8_mt9` | FLOAT | nivel_8_MT9 |
| `nivel_9_mt9` | FLOAT | nivel_9_MT9 |
| `nivel_10_mt9` | FLOAT | nivel_10_MT9 |
| `nivel_11_mt9` | FLOAT | nivel_11_MT9 |
| `nivel_12_mt9` | FLOAT | nivel_12_MT9 |
| `nivel_13_mt9` | FLOAT | nivel_13_MT9 |
| `nivel_0_mt12` | FLOAT | nivel_0_MT12 |
| `nivel_1_mt12` | FLOAT | nivel_1_MT12 |
| `nivel_2_mt12` | FLOAT | nivel_2_MT12 |
| `nivel_3_mt12` | FLOAT | nivel_3_MT12 |
| `nivel_4_mt12` | FLOAT | nivel_4_MT12 |
| `nivel_5_mt12` | FLOAT | nivel_5_MT12 |
| `nivel_6_mt12` | FLOAT | nivel_6_MT12 |
| `nivel_7_mt12` | FLOAT | nivel_7_MT12 |
| `nivel_8_mt12` | FLOAT | nivel_8_MT12 |
| `nivel_9_mt12` | FLOAT | nivel_9_MT12 |
| `nivel_10_mt12` | FLOAT | nivel_10_MT12 |
| `nivel_11_mt12` | FLOAT | nivel_11_MT12 |
| `nivel_12_mt12` | FLOAT | nivel_12_MT12 |
| `nivel_13_mt12` | FLOAT | nivel_13_MT12 |
| `nivel_0_lp5` | FLOAT | nivel_0_LP5 |
| `nivel_1_lp5` | FLOAT | nivel_1_LP5 |
| `nivel_2_lp5` | FLOAT | nivel_2_LP5 |
| `nivel_3_lp5` | FLOAT | nivel_3_LP5 |
| `nivel_4_lp5` | FLOAT | nivel_4_LP5 |
| `nivel_5_lp5` | FLOAT | nivel_5_LP5 |
| `nivel_6_lp5` | FLOAT | nivel_6_LP5 |
| `nivel_7_lp5` | FLOAT | nivel_7_LP5 |
| `nivel_8_lp5` | FLOAT | nivel_8_LP5 |
| `nivel_9_lp5` | FLOAT | nivel_9_LP5 |
| `nivel_10_lp5` | FLOAT | nivel_10_LP5 |
| `nivel_11_lp5` | FLOAT | nivel_11_LP5 |
| `nivel_0_lp9` | FLOAT | nivel_0_LP9 |
| `nivel_1_lp9` | FLOAT | nivel_1_LP9 |
| `nivel_2_lp9` | FLOAT | nivel_2_LP9 |
| `nivel_3_lp9` | FLOAT | nivel_3_LP9 |
| `nivel_4_lp9` | FLOAT | nivel_4_LP9 |
| `nivel_5_lp9` | FLOAT | nivel_5_LP9 |
| `nivel_6_lp9` | FLOAT | nivel_6_LP9 |
| `nivel_7_lp9` | FLOAT | nivel_7_LP9 |
| `nivel_8_lp9` | FLOAT | nivel_8_LP9 |
| `nivel_9_lp9` | FLOAT | nivel_9_LP9 |
| `nivel_10_lp9` | FLOAT | nivel_10_LP9 |
| `nivel_11_lp9` | FLOAT | nivel_11_LP9 |
| `nivel_0_lp12` | FLOAT | nivel_0_LP12 |
| `nivel_1_lp12` | FLOAT | nivel_1_LP12 |
| `nivel_2_lp12` | FLOAT | nivel_2_LP12 |
| `nivel_3_lp12` | FLOAT | nivel_3_LP12 |
| `nivel_4_lp12` | FLOAT | nivel_4_LP12 |
| `nivel_5_lp12` | FLOAT | nivel_5_LP12 |
| `nivel_6_lp12` | FLOAT | nivel_6_LP12 |
| `nivel_7_lp12` | FLOAT | nivel_7_LP12 |
| `nivel_8_lp12` | FLOAT | nivel_8_LP12 |
| `nivel_9_lp12` | FLOAT | nivel_9_LP12 |
| `nivel_10_lp12` | FLOAT | nivel_10_LP12 |
| `nivel_11_lp12` | FLOAT | nivel_11_LP12 |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC da carga no lake. |

## trusted · inep_saeb_indicadores_municipios

File `trusted__inep_saeb_indicadores_municipios.parquet` · 540,927 rows · 115 columns

SAEB Planilha de Resultados — nível municipal (~69k linhas/edição). Fonte: INEP.

**Built from:** `raw/saeb_indicadores_municipios`

**Feeds:** `semantic/obt_inep_saeb_indicadores_municipio_ano`

| Column | Type | Description |
|---|---|---|
| `ano_saeb` | INTEGER | Ano de aplicação do Saeb |
| `co_uf` | INTEGER | Código da Unidade da Federação (IBGE) |
| `no_uf` | STRING | Nome da Unidade da Federação |
| `co_municipio` | INTEGER | Código do Município (IBGE 7 dígitos) |
| `no_municipio` | STRING | Nome do Município |
| `dependencia_adm` | STRING | Dependência administrativa (Pública, Federal, Estadual, Municipal, Privada) |
| `localizacao` | STRING | Localização (Urbana / Rural / Total) |
| `capital` | STRING | Capital ou Interior |
| `media_5_lp` | FLOAT | Média em Língua Portuguesa 5º ano EF |
| `media_5_mt` | FLOAT | Média em Matemática 5º ano EF |
| `media_9_lp` | FLOAT | Média em Língua Portuguesa 9º ano EF |
| `media_9_mt` | FLOAT | Média em Matemática 9º ano EF |
| `media_12_lp` | FLOAT | Média em LP — EM tradicional |
| `media_12_mt` | FLOAT | Média em MT — EM tradicional |
| `nivel_0_lp5` | FLOAT | nivel_0_LP5 |
| `nivel_1_lp5` | FLOAT | nivel_1_LP5 |
| `nivel_2_lp5` | FLOAT | nivel_2_LP5 |
| `nivel_3_lp5` | FLOAT | nivel_3_LP5 |
| `nivel_4_lp5` | FLOAT | nivel_4_LP5 |
| `nivel_5_lp5` | FLOAT | nivel_5_LP5 |
| `nivel_6_lp5` | FLOAT | nivel_6_LP5 |
| `nivel_7_lp5` | FLOAT | nivel_7_LP5 |
| `nivel_8_lp5` | FLOAT | nivel_8_LP5 |
| `nivel_9_lp5` | FLOAT | nivel_9_LP5 |
| `nivel_0_mt5` | FLOAT | nivel_0_MT5 |
| `nivel_1_mt5` | FLOAT | nivel_1_MT5 |
| `nivel_2_mt5` | FLOAT | nivel_2_MT5 |
| `nivel_3_mt5` | FLOAT | nivel_3_MT5 |
| `nivel_4_mt5` | FLOAT | nivel_4_MT5 |
| `nivel_5_mt5` | FLOAT | nivel_5_MT5 |
| `nivel_6_mt5` | FLOAT | nivel_6_MT5 |
| `nivel_7_mt5` | FLOAT | nivel_7_MT5 |
| `nivel_8_mt5` | FLOAT | nivel_8_MT5 |
| `nivel_9_mt5` | FLOAT | nivel_9_MT5 |
| `nivel_10_mt5` | FLOAT | nivel_10_MT5 |
| `nivel_0_lp9` | FLOAT | nivel_0_LP9 |
| `nivel_1_lp9` | FLOAT | nivel_1_LP9 |
| `nivel_2_lp9` | FLOAT | nivel_2_LP9 |
| `nivel_3_lp9` | FLOAT | nivel_3_LP9 |
| `nivel_4_lp9` | FLOAT | nivel_4_LP9 |
| `nivel_5_lp9` | FLOAT | nivel_5_LP9 |
| `nivel_6_lp9` | FLOAT | nivel_6_LP9 |
| `nivel_7_lp9` | FLOAT | nivel_7_LP9 |
| `nivel_8_lp9` | FLOAT | nivel_8_LP9 |
| `nivel_0_mt9` | FLOAT | nivel_0_MT9 |
| `nivel_1_mt9` | FLOAT | nivel_1_MT9 |
| `nivel_2_mt9` | FLOAT | nivel_2_MT9 |
| `nivel_3_mt9` | FLOAT | nivel_3_MT9 |
| `nivel_4_mt9` | FLOAT | nivel_4_MT9 |
| `nivel_5_mt9` | FLOAT | nivel_5_MT9 |
| `nivel_6_mt9` | FLOAT | nivel_6_MT9 |
| `nivel_7_mt9` | FLOAT | nivel_7_MT9 |
| `nivel_8_mt9` | FLOAT | nivel_8_MT9 |
| `nivel_9_mt9` | FLOAT | nivel_9_MT9 |
| `nivel_0_lp12` | FLOAT | nivel_0_LP12 |
| `nivel_1_lp12` | FLOAT | nivel_1_LP12 |
| `nivel_2_lp12` | FLOAT | nivel_2_LP12 |
| `nivel_3_lp12` | FLOAT | nivel_3_LP12 |
| `nivel_4_lp12` | FLOAT | nivel_4_LP12 |
| `nivel_5_lp12` | FLOAT | nivel_5_LP12 |
| `nivel_6_lp12` | FLOAT | nivel_6_LP12 |
| `nivel_7_lp12` | FLOAT | nivel_7_LP12 |
| `nivel_8_lp12` | FLOAT | nivel_8_LP12 |
| `nivel_0_mt12` | FLOAT | nivel_0_MT12 |
| `nivel_1_mt12` | FLOAT | nivel_1_MT12 |
| `nivel_2_mt12` | FLOAT | nivel_2_MT12 |
| `nivel_3_mt12` | FLOAT | nivel_3_MT12 |
| `nivel_4_mt12` | FLOAT | nivel_4_MT12 |
| `nivel_5_mt12` | FLOAT | nivel_5_MT12 |
| `nivel_6_mt12` | FLOAT | nivel_6_MT12 |
| `nivel_7_mt12` | FLOAT | nivel_7_MT12 |
| `nivel_8_mt12` | FLOAT | nivel_8_MT12 |
| `nivel_9_mt12` | FLOAT | nivel_9_MT12 |
| `nivel_10_mt12` | FLOAT | nivel_10_MT12 |
| `nivel_0_lp13` | FLOAT | nivel_0_LP13 |
| `nivel_1_lp13` | FLOAT | nivel_1_LP13 |
| `nivel_2_lp13` | FLOAT | nivel_2_LP13 |
| `nivel_3_lp13` | FLOAT | nivel_3_LP13 |
| `nivel_4_lp13` | FLOAT | nivel_4_LP13 |
| `nivel_5_lp13` | FLOAT | nivel_5_LP13 |
| `nivel_6_lp13` | FLOAT | nivel_6_LP13 |
| `nivel_7_lp13` | FLOAT | nivel_7_LP13 |
| `nivel_8_lp13` | FLOAT | nivel_8_LP13 |
| `nivel_0_mt13` | FLOAT | nivel_0_MT13 |
| `nivel_1_mt13` | FLOAT | nivel_1_MT13 |
| `nivel_2_mt13` | FLOAT | nivel_2_MT13 |
| `nivel_3_mt13` | FLOAT | nivel_3_MT13 |
| `nivel_4_mt13` | FLOAT | nivel_4_MT13 |
| `nivel_5_mt13` | FLOAT | nivel_5_MT13 |
| `nivel_6_mt13` | FLOAT | nivel_6_MT13 |
| `nivel_7_mt13` | FLOAT | nivel_7_MT13 |
| `nivel_8_mt13` | FLOAT | nivel_8_MT13 |
| `nivel_9_mt13` | FLOAT | nivel_9_MT13 |
| `nivel_10_mt13` | FLOAT | nivel_10_MT13 |
| `nivel_0_lp14` | FLOAT | nivel_0_LP14 |
| `nivel_1_lp14` | FLOAT | nivel_1_LP14 |
| `nivel_2_lp14` | FLOAT | nivel_2_LP14 |
| `nivel_3_lp14` | FLOAT | nivel_3_LP14 |
| `nivel_4_lp14` | FLOAT | nivel_4_LP14 |
| `nivel_5_lp14` | FLOAT | nivel_5_LP14 |
| `nivel_6_lp14` | FLOAT | nivel_6_LP14 |
| `nivel_7_lp14` | FLOAT | nivel_7_LP14 |
| `nivel_8_lp14` | FLOAT | nivel_8_LP14 |
| `nivel_0_mt14` | FLOAT | nivel_0_MT14 |
| `nivel_1_mt14` | FLOAT | nivel_1_MT14 |
| `nivel_2_mt14` | FLOAT | nivel_2_MT14 |
| `nivel_3_mt14` | FLOAT | nivel_3_MT14 |
| `nivel_4_mt14` | FLOAT | nivel_4_MT14 |
| `nivel_5_mt14` | FLOAT | nivel_5_MT14 |
| `nivel_6_mt14` | FLOAT | nivel_6_MT14 |
| `nivel_7_mt14` | FLOAT | nivel_7_MT14 |
| `nivel_8_mt14` | FLOAT | nivel_8_MT14 |
| `nivel_9_mt14` | FLOAT | nivel_9_MT14 |
| `nivel_10_mt14` | FLOAT | nivel_10_MT14 |
| `dt_ingestao_lake` | TIMESTAMP | Data e hora de carga do registro no data lake (AAAA-MM-DD HH:MM:SS). — descrição gerada por IA. |

## trusted · inep_saeb_microdados_escola

File `trusted__inep_saeb_microdados_escola.parquet` · 461,283 rows · 28 columns

Microdados SAEB por escola — questionnaire + resultados agregados por escola. Anos 2011-2023. Fonte: INEP / microdados SAEB (ts_escola, ts_quest_escola). Respostas de questionário preservadas em dados_json.

**Built from:** `raw/inep_saeb_microdados_csv_2011_ts_quest_escola`, `raw/inep_saeb_microdados_csv_2013_ts_escola`, `raw/inep_saeb_microdados_csv_2015_ts_escola`, `raw/inep_saeb_microdados_csv_2017_ts_escola`, `raw/inep_saeb_microdados_csv_2019_ts_escola`, `raw/inep_saeb_microdados_csv_2021_ts_escola`, `raw/inep_saeb_microdados_csv_2023_ts_escola`

**Feeds:** `semantic/obt_inep_saeb_micro_escola_ano`, `semantic/obt_inep_saeb_micro_municipio_ano`

| Column | Type | Description |
|---|---|---|
| `ano` | INTEGER | Ano de referência da edição do SAEB em que os dados foram coletados. |
| `tabela_origem` | STRING | Nome da tabela raw de origem no BigQuery (raw_zone.inep_saeb_microdados_csv_*). |
| `id_saeb` | INTEGER | Código numérico da edição do SAEB. Identifica unicamente cada ciclo de avaliação. |
| `id_regiao` | STRING | Código da região geográfica brasileira: 1=Norte, 2=Nordeste, 3=Sudeste, 4=Sul, 5=Centro-Oeste. |
| `id_uf` | STRING | Código da Unidade Federativa (estado). Segue a codificação IBGE de 2 dígitos. |
| `id_municipio` | STRING | Código IBGE do município (7 dígitos). Identifica unicamente cada município brasileiro. |
| `id_area` | STRING | Código da área ou estrato amostral dentro do município, usado na amostragem probabilística do SAEB. |
| `id_escola` | STRING | Código INEP da escola (7 dígitos). Chave de ligação com tabelas do Censo Escolar e API SAEB. |
| `tp_dependencia_adm` | STRING | Tipo de dependência administrativa da escola: 1=Federal, 2=Estadual, 3=Municipal, 4=Privada. |
| `in_publica` | STRING | Indica se a escola é pública: 1=Sim, 0=Não (privada). |
| `tp_localizacao` | STRING | Código da localização: 1=Urbana, 2=Rural. |
| `tp_capital` | STRING | Indica se o município é capital de estado: 1=Sim (capital), 0=Não. |
| `nivel_socio_economico` | STRING | Nível Socioeconômico (NSE) da escola, calculado pelo INEP a partir do perfil socioeconômico médio dos alunos. Escala categórica (Grupo I a VIII). |
| `pc_formacao_docente_inicial` | FLOAT | Percentual de professores com formação superior adequada à disciplina que lecionam nos anos iniciais do EF (exige licenciatura na área ou pedagogia). |
| `pc_formacao_docente_final` | FLOAT | Percentual de professores com formação superior adequada nos anos finais do EF e Ensino Médio (exige licenciatura na área da disciplina). |
| `pc_formacao_docente_medio` | FLOAT | Percentual de professores com formação apenas em nível médio (magistério/normal), sem ensino superior. |
| `nu_matriculados_censo_5ef` | INTEGER | Total de alunos matriculados no 5º ano do Ensino Fundamental segundo o Censo Escolar, base para cálculo da taxa de participação. |
| `nu_presentes_5ef` | INTEGER | Total de alunos do 5º ano do EF que realizaram a prova SAEB na escola. |
| `taxa_participacao_5ef` | FLOAT | Taxa de participação na prova do 5º ano do EF: proporção entre presentes e matriculados (%). Escolas com menos de 10 alunos não recebem resultado. |
| `media_5ef_lp` | FLOAT | Média de proficiência em Língua Portuguesa dos alunos do 5º ano do EF da escola, na Escala SAEB. |
| `media_5ef_mt` | FLOAT | Média de proficiência em Matemática dos alunos do 5º ano do EF da escola, na Escala SAEB. |
| `nu_matriculados_censo_9ef` | INTEGER | Total de alunos matriculados no 9º ano do Ensino Fundamental segundo o Censo Escolar. |
| `nu_presentes_9ef` | INTEGER | Total de alunos do 9º ano do EF que realizaram a prova SAEB na escola. |
| `taxa_participacao_9ef` | FLOAT | Taxa de participação na prova do 9º ano do EF: proporção entre presentes e matriculados (%). |
| `media_9ef_lp` | FLOAT | Média de proficiência em Língua Portuguesa dos alunos do 9º ano do EF da escola, na Escala SAEB. |
| `media_9ef_mt` | FLOAT | Média de proficiência em Matemática dos alunos do 9º ano do EF da escola, na Escala SAEB. |
| `dados_json` | STRING | Respostas do questionário contextual SAEB preservadas em JSON. Cada chave é um código de questão (ex: TX_RESP_Q001, TX_Q003) e o valor é a alternativa marcada (A, B, C...). O significado de cada questão varia por edição — consulte o dicionário em trusted_zone.inep_saeb_resultados_planilhas_linhas para decodificar. |
| `dt_ingestao_lake` | TIMESTAMP | Data e hora de carregamento do registro no Data Lake (formato YYYY-MM-DD HH:MM:SS). — descrição gerada por IA. |

## trusted · inep_saeb_microdados_item

File `trusted__inep_saeb_microdados_item.parquet` · 4,255 rows · 29 columns

Catálogo de itens (questões) das provas SAEB por edição. Anos 2011-2023. Fonte: INEP / microdados SAEB (ts_item).

**Built from:** `raw/inep_saeb_microdados_csv_2011_ts_item`, `raw/inep_saeb_microdados_csv_2013_ts_item`, `raw/inep_saeb_microdados_csv_2015_ts_item`, `raw/inep_saeb_microdados_csv_2019_ts_item`, `raw/inep_saeb_microdados_csv_2021_ts_item`, `raw/inep_saeb_microdados_csv_2023_ts_item`

| Column | Type | Description |
|---|---|---|
| `ano` | INTEGER | Ano de referência da edição do SAEB em que os dados foram coletados. |
| `tabela_origem` | STRING | Nome da tabela raw de origem no BigQuery (raw_zone.inep_saeb_microdados_csv_*). |
| `a` | STRING | Parâmetro 'a' do modelo TRI: discriminação do item (capacidade de distinguir alunos proficientes dos não proficientes). Valores maiores = item mais discriminativo. |
| `b` | STRING | Parâmetro 'b' do modelo TRI: dificuldade do item (ponto da escala onde o aluno tem 50% de chance de acerto). Valores maiores = item mais difícil. |
| `b1` | STRING | Parâmetro de limiar 'b1' do Modelo de Resposta Graduada (item politômico): transição do nível 0 para o nível 1 de resposta. |
| `b2` | STRING | Parâmetro de limiar 'b2' do Modelo de Resposta Graduada: transição do nível 1 para o nível 2 de resposta. |
| `b3` | STRING | Parâmetro de limiar 'b3' do Modelo de Resposta Graduada: transição do nível 2 para o nível 3 de resposta (somente 2023+). |
| `bloco` | STRING | Código do bloco/caderno de prova em que o item foi aplicado. |
| `c` | STRING | Parâmetro 'c' do modelo TRI: pseudo-acaso/adivinhação (probabilidade de acerto ao acaso). Típico em múltipla escolha. |
| `disciplina` | STRING | Disciplina avaliada pelo item: LP=Língua Portuguesa, MT=Matemática (formato legado). |
| `gabarito` | STRING | Alternativa correta do item para questões de múltipla escolha (A, B, C, D, E). Vazio para itens abertos (formato legado). |
| `id_bloco` | STRING | Código do bloco/caderno de prova em que o item foi aplicado (formato legado 2011). |
| `id_descritor` | STRING | Código do descritor de habilidade avaliado pelo item (formato legado 2011). |
| `id_item` | STRING | Código único do item SAEB. Identifica a questão no banco de itens do INEP. |
| `id_posicao` | STRING | Posição do item dentro do bloco na prova (formato legado 2011). |
| `id_saeb` | STRING | Código numérico da edição do SAEB. Identifica unicamente cada ciclo de avaliação. |
| `id_serie` | STRING | Código da série/ano escolar avaliado: ex. 5=5ºano EF, 9=9ºano EF, 12=3ºano EM. |
| `id_serie_item` | STRING | Código da série para a qual o item foi desenvolvido (formato legado 2011). |
| `item_modelo` | STRING | Modelo de resposta do item no Modelo de Resposta Graduada (MRG) — indica se é dicotômico ou politômico (formato legado). |
| `nu_bloco` | STRING | Número do bloco de itens no caderno de prova (2023+). |
| `nu_descritor_habilidade` | STRING | Número do descritor de habilidade da Matriz de Referência SAEB avaliado pelo item (ex: D01, D15). |
| `nu_posicao` | STRING | Número da posição do item dentro do bloco (2023+). |
| `posicao` | STRING | Posição do item dentro do bloco na prova. |
| `tipo_item` | STRING | Tipo do item: 1=Múltipla escolha, 2=Item aberto/dissertativo (formato legado). |
| `tp_disciplina` | STRING | Disciplina avaliada pelo item: LP=Língua Portuguesa, MT=Matemática, CH=Ciências Humanas, CN=Ciências da Natureza. |
| `tp_item` | STRING | Tipo do item: 1=Múltipla escolha, 2=Item aberto/dissertativo. |
| `tp_item_modelo` | STRING | Modelo de resposta do item: D=Dicotômico (certo/errado), P=Politômico (resposta parcial). |
| `tx_gabarito` | STRING | Alternativa correta do item (A, B, C, D, E para múltipla escolha; código para item aberto/dissertativo). |
| `dt_ingestao_lake` | TIMESTAMP | Data e hora em que o registro foi inserido no Data Lake (formato YYYY-MM-DD HH:MM:SS). — descrição gerada por IA. |

## trusted · inep_saeb_secretario

File `trusted__inep_saeb_secretario.parquet` · 16,548 rows · 6 columns

SAEB microdados — secretario, todos os anos. Questionário em dados_json.

**Built from:** `raw/inep_saeb_microdados_csv_2019_ts_secretario_municipal`, `raw/inep_saeb_microdados_csv_2021_ts_secretario_municipal`, `raw/inep_saeb_microdados_csv_2023_ts_secretario_municipal`

| Column | Type | Description |
|---|---|---|
| `ano_saeb` | INTEGER | Ano da edicao do Saeb. |
| `id_escola` | STRING | Codigo INEP da escola (8 digitos). |
| `sg_uf` | STRING | Sigla da UF. |
| `id_municipio` | INTEGER | Id municipio. |
| `dados_json` | STRING | Dados json. |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC da carga no lake. |
