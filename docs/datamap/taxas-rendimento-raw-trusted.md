# School flow and distortion rates (INEP): Raw and Trusted

Dataset: [lucasrangelss/taxas-rendimento-raw-trusted](https://www.kaggle.com/datasets/lucasrangelss/taxas-rendimento-raw-trusted) · snapshot 2026-10-01 · 11 tables · 218,331,656 rows

**Source:** Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP), [https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais)

Approval, failure and dropout rates and the age-grade distortion rate by school, municipality, state, region and Brazil, per year.

**Grain and keys:** School, municipality, state, region or Brazil by year.

**Layers.** `raw` is the source snapshot as delivered. `trusted` is typed, deduplicated and named consistently. `semantic` joins and reshapes trusted tables for analysis. Every table is a Parquet file named `<layer>__<table>.parquet` at the root of the dataset.

The full interactive map (lineage, joins, search) is at [https://rangeltech.net/datamap/](https://rangeltech.net/datamap/). Column descriptions come from the source lake's catalogue and are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns | Described | Upstream |
|---|---|---:|---:|---:|---|
| raw | [`inep_taxa_distorcao_brasil_regioes_ufs`](#raw-inep-taxa-distorcao-brasil-regioes-ufs) | 7,404 | 43 | 43 | source |
| raw | [`inep_taxa_distorcao_escolas`](#raw-inep-taxa-distorcao-escolas) | 2,148,217 | 48 | 48 | source |
| raw | [`inep_taxa_distorcao_municipios`](#raw-inep-taxa-distorcao-municipios) | 982,518 | 45 | 45 | source |
| raw | [`inep_taxas_rendimento_escolar`](#raw-inep-taxas-rendimento-escolar) | 3,974,168 | 71 | 71 | source |
| raw | [`inep_taxas_rendimento_escolar_arquivos`](#raw-inep-taxas-rendimento-escolar-arquivos) | 54 | 11 | 11 | source |
| trusted | [`inep_taxa_distorcao_brasil_regioes_ufs`](#trusted-inep-taxa-distorcao-brasil-regioes-ufs) | 7,356 | 24 | 24 | `inep_taxa_distorcao_brasil_regioes_ufs` |
| trusted | [`inep_taxa_distorcao_escolas`](#trusted-inep-taxa-distorcao-escolas) | 2,148,183 | 27 | 27 | `inep_taxa_distorcao_escolas` |
| trusted | [`inep_taxa_distorcao_municipios`](#trusted-inep-taxa-distorcao-municipios) | 982,486 | 25 | 25 | `inep_taxa_distorcao_municipios` |
| trusted | [`inep_taxas_rendimento_escolar`](#trusted-inep-taxas-rendimento-escolar) | 3,974,168 | 71 | 71 | `inep_taxas_rendimento_escolar` |
| trusted | [`inep_taxas_rendimento_escolar_long`](#trusted-inep-taxas-rendimento-escolar-long) | 204,107,094 | 25 | 25 | `inep_taxas_rendimento_escolar` |
| trusted | [`inep_taxas_rendimento_escolar_qualidade`](#trusted-inep-taxas-rendimento-escolar-qualidade) | 8 | 28 | 28 | `inep_taxas_rendimento_escolar_long` |

## raw · inep_taxa_distorcao_brasil_regioes_ufs

File `raw__inep_taxa_distorcao_brasil_regioes_ufs.parquet` · 7,404 rows · 43 columns

Tabela de indicadores educacionais do INEP contendo a Taxa de Distorção Idade-Série (TDI) e o Indicador de Adequação da Formação Docente (Categoria 0) para os ensinos Fundamental e Médio, segmentados por região, dependência administrativa e localização.

**Feeds:** `trusted/inep_taxa_distorcao_brasil_regioes_ufs`

| Column | Type | Description |
|---|---|---|
| `NU_ANO_CENSO` | STRING | Ano de referência do Censo Escolar ou identificação da fonte dos dados. |
| `NO_REGIAO` | STRING | Nome da região geográfica brasileira. |
| `TIPOLOCA` | STRING | Tipo de localização da escola (Urbana ou Rural). |
| `DEPENDAD` | STRING | Dependência administrativa da escola (Federal, Estadual, Municipal ou Privada). |
| `TDI_FUN` | STRING | Taxa de distorção idade-série total no Ensino Fundamental (%). |
| `TDI_F14` | STRING | Taxa de distorção idade-série do 1º ao 4º ano do Ensino Fundamental (%). |
| `TDI_F58` | STRING | Taxa de distorção idade-série do 5º ao 8º ano do Ensino Fundamental (%). |
| `TDI_F00` | STRING | Taxa de distorção idade-série na etapa inicial/pré-escola do Ensino Fundamental (%). |
| `TDI_F01` | STRING | Taxa de distorção idade-série no 1º ano do Ensino Fundamental (%). |
| `TDI_F02` | STRING | Taxa de distorção idade-série no 2º ano do Ensino Fundamental (%). |
| `TDI_F03` | STRING | Taxa de distorção idade-série no 3º ano do Ensino Fundamental (%). |
| `TDI_F04` | STRING | Taxa de distorção idade-série no 4º ano do Ensino Fundamental (%). |
| `TDI_F05` | STRING | Taxa de distorção idade-série no 5º ano do Ensino Fundamental (%). |
| `TDI_F06` | STRING | Taxa de distorção idade-série no 6º ano do Ensino Fundamental (%). |
| `TDI_F07` | STRING | Taxa de distorção idade-série no 7º ano do Ensino Fundamental (%). |
| `TDI_F08` | STRING | Taxa de distorção idade-série no 8º ano do Ensino Fundamental (%). |
| `TDI_MED` | STRING | Taxa de distorção idade-série total no Ensino Médio (%). |
| `TDI_M01` | STRING | Taxa de distorção idade-série no 1º ano do Ensino Médio (%). |
| `TDI_M02` | STRING | Taxa de distorção idade-série no 2º ano do Ensino Médio (%). |
| `TDI_M03` | STRING | Taxa de distorção idade-série no 3º ano do Ensino Médio (%). |
| `TDI_M04` | STRING | Taxa de distorção idade-série no 4º ano do Ensino Médio/Ensino Técnico integrado (%). |
| `dt_ingestao_lake` | STRING | Data e hora do carregamento do registro no Data Lake (formato ISO 8601). — descrição gerada por IA. |
| `NO_CODIGO` | STRING | Código identificador da unidade geográfica ou administrativa. |
| `UNIDGEO` | STRING | Nome da unidade geográfica de análise (ex: Brasil, Unidade da Federação). |
| `NO_CATEGORIA` | STRING | Categoria de localização ou agrupamento dos dados (ex: Urbana, Rural, Total). |
| `NO_DEPENDENCIA` | STRING | Nome por extenso da dependência administrativa (ex: Federal, Estadual, Municipal). |
| `FUN_01_CAT_0` | STRING | Percentual de docentes do 1º ano do Ensino Fundamental classificados na Categoria 0 de adequação da formação (%). |
| `FUN_02_CAT_0` | STRING | Percentual de docentes do 2º ano do Ensino Fundamental classificados na Categoria 0 de adequação da formação (%). |
| `FUN_03_CAT_0` | STRING | Percentual de docentes do 3º ano do Ensino Fundamental classificados na Categoria 0 de adequação da formação (%). |
| `FUN_04_CAT_0` | STRING | Percentual de docentes do 4º ano do Ensino Fundamental classificados na Categoria 0 de adequação da formação (%). |
| `FUN_05_CAT_0` | STRING | Percentual de docentes do 5º ano do Ensino Fundamental classificados na Categoria 0 de adequação da formação (%). |
| `FUN_06_CAT_0` | STRING | Percentual de docentes do 6º ano do Ensino Fundamental classificados na Categoria 0 de adequação da formação (%). |
| `FUN_07_CAT_0` | STRING | Percentual de docentes do 7º ano do Ensino Fundamental classificados na Categoria 0 de adequação da formação (%). |
| `FUN_08_CAT_0` | STRING | Percentual de docentes do 8º ano do Ensino Fundamental classificados na Categoria 0 de adequação da formação (%). |
| `FUN_09_CAT_0` | STRING | Percentual de docentes do 9º ano do Ensino Fundamental classificados na Categoria 0 de adequação da formação (%). |
| `FUN_AI_CAT_0` | STRING | Percentual de docentes dos Anos Iniciais do Ensino Fundamental na Categoria 0 de adequação da formação (%). |
| `FUN_AF_CAT_0` | STRING | Percentual de docentes dos Anos Finais do Ensino Fundamental na Categoria 0 de adequação da formação (%). |
| `FUN_CAT_0` | STRING | Percentual total de docentes do Ensino Fundamental classificados na Categoria 0 de adequação da formação (%). |
| `MED_01_CAT_0` | STRING | Percentual de docentes do 1º ano do Ensino Médio classificados na Categoria 0 de adequação da formação (%). |
| `MED_02_CAT_0` | STRING | Percentual de docentes do 2º ano do Ensino Médio classificados na Categoria 0 de adequação da formação (%). |
| `MED_03_CAT_0` | STRING | Percentual de docentes do 3º ano do Ensino Médio classificados na Categoria 0 de adequação da formação (%). |
| `MED_04_CAT_0` | STRING | Percentual de docentes do 4º ano do Ensino Médio classificados na Categoria 0 de adequação da formação (%). |
| `MED_CAT_0` | STRING | Percentual total de docentes do Ensino Médio classificados na Categoria 0 de adequação da formação (%). |

## raw · inep_taxa_distorcao_escolas

File `raw__inep_taxa_distorcao_escolas.parquet` · 2,148,217 rows · 48 columns

Tabela de indicadores de Taxa de Distorção Idade-Série (TDI) do Ensino Fundamental e Médio, baseada em dados do INEP/Censo Escolar, mapeando escolas, municípios e dependências administrativas.

**Feeds:** `trusted/inep_taxa_distorcao_escolas`

| Column | Type | Description |
|---|---|---|
| `NU_ANO_CENSO` | STRING | Ano de referência do Censo Escolar ou notas de rodapé da base original (Texto). |
| `NO_REGIAO` | STRING | Nome da região geográfica onde a escola está localizada. |
| `CO_UF` | STRING | Código numérico do estado (IBGE). |
| `SG_UF` | STRING | Sigla do estado (Unidade Federativa). |
| `CO_MUNICIPIO` | STRING | Código numérico do município (IBGE). |
| `NO_MUNICIPIO` | STRING | Nome do município. |
| `CO_ENTIDADE` | STRING | Código único de identificação da escola (INEP). |
| `NO_ENTIDADE` | STRING | Nome oficial da escola. |
| `TIPOLOCA` | STRING | Tipo de localização da escola (ex: Urbana ou Rural). |
| `DEPENDAD` | STRING | Código ou sigla da dependência administrativa da escola. |
| `TDI_FUN` | STRING | Taxa de distorção idade-série total do Ensino Fundamental (%). |
| `TDI_F14` | STRING | Taxa de distorção idade-série dos anos iniciais do Ensino Fundamental (%). |
| `TDI_F58` | STRING | Taxa de distorção idade-série dos anos finais do Ensino Fundamental (%). |
| `TDI_F00` | STRING | Taxa de distorção idade-série do Ensino Fundamental de 9 anos (%). |
| `TDI_F01` | STRING | Taxa de distorção idade-série do 1º ano do Ensino Fundamental (%). |
| `TDI_F02` | STRING | Taxa de distorção idade-série do 2º ano do Ensino Fundamental (%). |
| `TDI_F03` | STRING | Taxa de distorção idade-série do 3º ano do Ensino Fundamental (%). |
| `TDI_F04` | STRING | Taxa de distorção idade-série do 4º ano do Ensino Fundamental (%). |
| `TDI_F05` | STRING | Taxa de distorção idade-série do 5º ano do Ensino Fundamental (%). |
| `TDI_F06` | STRING | Taxa de distorção idade-série do 6º ano do Ensino Fundamental (%). |
| `TDI_F07` | STRING | Taxa de distorção idade-série do 7º ano do Ensino Fundamental (%). |
| `TDI_F08` | STRING | Taxa de distorção idade-série do 8º ano do Ensino Fundamental (%). |
| `TDI_MED` | STRING | Taxa de distorção idade-série total do Ensino Médio (%). |
| `TDI_M01` | STRING | Taxa de distorção idade-série do 1º ano do Ensino Médio (%). |
| `TDI_M02` | STRING | Taxa de distorção idade-série do 2º ano do Ensino Médio (%). |
| `TDI_M03` | STRING | Taxa de distorção idade-série do 3º ano do Ensino Médio (%). |
| `TDI_M04` | STRING | Taxa de distorção idade-série do 4º ano do Ensino Médio (%). |
| `dt_ingestao_lake` | STRING | Data e hora de ingestão do registro no Data Lake (timestamp ISO 8601). — descrição gerada por IA. |
| `Ano` | STRING | Ano civil de referência do dado (Numérico). |
| `NO_CATEGORIA` | STRING | Nome da categoria administrativa ou de análise da escola. |
| `NO_DEPENDENCIA` | STRING | Nome descritivo da dependência administrativa (ex: Estadual, Municipal). |
| `FUN_CAT_0` | STRING | Rótulo descritivo geral do Ensino Fundamental. |
| `FUN_AI_CAT_0` | STRING | Rótulo descritivo para os Anos Iniciais do Ensino Fundamental. |
| `FUN_AF_CAT_0` | STRING | Rótulo descritivo para os Anos Finais do Ensino Fundamental. |
| `FUN_01_CAT_0` | STRING | Rótulo descritivo para o 1º ano do Ensino Fundamental. |
| `FUN_02_CAT_0` | STRING | Rótulo descritivo para o 2º ano do Ensino Fundamental. |
| `FUN_03_CAT_0` | STRING | Rótulo descritivo para o 3º ano do Ensino Fundamental. |
| `FUN_04_CAT_0` | STRING | Rótulo descritivo para o 4º ano do Ensino Fundamental. |
| `FUN_05_CAT_0` | STRING | Rótulo descritivo para o 5º ano do Ensino Fundamental. |
| `FUN_06_CAT_0` | STRING | Rótulo descritivo para o 6º ano do Ensino Fundamental. |
| `FUN_07_CAT_0` | STRING | Rótulo descritivo para o 7º ano do Ensino Fundamental. |
| `FUN_08_CAT_0` | STRING | Rótulo descritivo para o 8º ano do Ensino Fundamental. |
| `FUN_09_CAT_0` | STRING | Rótulo descritivo para o 9º ano do Ensino Fundamental. |
| `MED_CAT_0` | STRING | Rótulo descritivo geral do Ensino Médio. |
| `MED_01_CAT_0` | STRING | Rótulo descritivo para o 1º ano do Ensino Médio. |
| `MED_02_CAT_0` | STRING | Rótulo descritivo para o 2º ano do Ensino Médio. |
| `MED_03_CAT_0` | STRING | Rótulo descritivo para o 3º ano do Ensino Médio. |
| `MED_04_CAT_0` | STRING | Rótulo descritivo para o 4º ano do Ensino Médio. |

## raw · inep_taxa_distorcao_municipios

File `raw__inep_taxa_distorcao_municipios.parquet` · 982,518 rows · 45 columns

Tabela de indicadores educacionais do INEP (Censo Escolar), contendo taxas de distorção idade-série (TDI) e indicadores de adequação da formação docente (Categoria 0) para o Ensino Fundamental e Médio, segmentados por região, município, localização e dependência administrativa.

**Feeds:** `trusted/inep_taxa_distorcao_municipios`

| Column | Type | Description |
|---|---|---|
| `NU_ANO_CENSO` | STRING | Ano de referência do Censo Escolar ou texto de metadado/nota de rodapé da fonte original. |
| `NO_REGIAO` | STRING | Nome da região geográfica do município. |
| `CO_UF` | STRING | Código numérico identificador da Unidade da Federação (IBGE). |
| `SG_UF` | STRING | Sigla da Unidade da Federação. |
| `CO_MUNICIPIO` | STRING | Nome do município (nota: campo invertido com NO_MUNICIPIO na carga de origem). |
| `NO_MUNICIPIO` | STRING | Código IBGE identificador do município (nota: campo invertido com CO_MUNICIPIO na carga de origem). |
| `TIPOLOCA` | STRING | Tipo de localização da escola (Urbana ou Rural). |
| `DEPENDAD` | STRING | Dependência administrativa da escola (Federal, Estadual, Municipal ou Privada). |
| `TDI_FUN` | STRING | Taxa de distorção idade-série total no Ensino Fundamental (%). |
| `TDI_F14` | STRING | Taxa de distorção idade-série nos anos iniciais (1ª a 4ª série / 1º ao 5º ano) do Ensino Fundamental (%). |
| `TDI_F58` | STRING | Taxa de distorção idade-série nos anos finais (5ª a 8ª série / 6º ao 9º ano) do Ensino Fundamental (%). |
| `TDI_F00` | STRING | Taxa de distorção idade-série na classe de alfabetização ou ano inicial não especificado (%). |
| `TDI_F01` | STRING | Taxa de distorção idade-série no 1º ano do Ensino Fundamental (%). |
| `TDI_F02` | STRING | Taxa de distorção idade-série no 2º ano do Ensino Fundamental (%). |
| `TDI_F03` | STRING | Taxa de distorção idade-série no 3º ano do Ensino Fundamental (%). |
| `TDI_F04` | STRING | Taxa de distorção idade-série no 4º ano do Ensino Fundamental (%). |
| `TDI_F05` | STRING | Taxa de distorção idade-série no 5º ano do Ensino Fundamental (%). |
| `TDI_F06` | STRING | Taxa de distorção idade-série no 6º ano do Ensino Fundamental (%). |
| `TDI_F07` | STRING | Taxa de distorção idade-série no 7º ano do Ensino Fundamental (%). |
| `TDI_F08` | STRING | Taxa de distorção idade-série no 8º ano do Ensino Fundamental (%). |
| `TDI_MED` | STRING | Taxa de distorção idade-série total no Ensino Médio (%). |
| `TDI_M01` | STRING | Taxa de distorção idade-série no 1º ano do Ensino Médio (%). |
| `TDI_M02` | STRING | Taxa de distorção idade-série no 2º ano do Ensino Médio (%). |
| `TDI_M03` | STRING | Taxa de distorção idade-série no 3º ano do Ensino Médio (%). |
| `TDI_M04` | STRING | Taxa de distorção idade-série no 4º ano (Ensino Médio Integrado/Profissionalizante) (%). |
| `dt_ingestao_lake` | STRING | Data e hora de ingestão do registro no Data Lake (formato ISO 8601). — descrição gerada por IA. |
| `NO_CATEGORIA` | STRING | Categoria de localização ou agrupamento para análise (ex: Urbana, Rural, Total). |
| `NO_DEPENDENCIA` | STRING | Nome por extenso da dependência administrativa da escola (Estadual, Municipal, Federal, Particular). |
| `FUN_01_CAT_0` | STRING | Percentual de docentes/turmas na Categoria 0 (sem formação adequada) no 1º ano do Ensino Fundamental. |
| `FUN_02_CAT_0` | STRING | Percentual de docentes/turmas na Categoria 0 (sem formação adequada) no 2º ano do Ensino Fundamental. |
| `FUN_03_CAT_0` | STRING | Percentual de docentes/turmas na Categoria 0 (sem formação adequada) no 3º ano do Ensino Fundamental. |
| `FUN_04_CAT_0` | STRING | Percentual de docentes/turmas na Categoria 0 (sem formação adequada) no 4º ano do Ensino Fundamental. |
| `FUN_05_CAT_0` | STRING | Percentual de docentes/turmas na Categoria 0 (sem formação adequada) no 5º ano do Ensino Fundamental. |
| `FUN_06_CAT_0` | STRING | Percentual de docentes/turmas na Categoria 0 (sem formação adequada) no 6º ano do Ensino Fundamental. |
| `FUN_07_CAT_0` | STRING | Percentual de docentes/turmas na Categoria 0 (sem formação adequada) no 7º ano do Ensino Fundamental. |
| `FUN_08_CAT_0` | STRING | Percentual de docentes/turmas na Categoria 0 (sem formação adequada) no 8º ano do Ensino Fundamental. |
| `FUN_09_CAT_0` | STRING | Percentual de docentes/turmas na Categoria 0 (sem formação adequada) no 9º ano do Ensino Fundamental. |
| `FUN_AI_CAT_0` | STRING | Percentual de docentes/turmas na Categoria 0 (sem formação adequada) nos Anos Iniciais do Ensino Fundamental. |
| `FUN_AF_CAT_0` | STRING | Percentual de docentes/turmas na Categoria 0 (sem formação adequada) nos Anos Finais do Ensino Fundamental. |
| `FUN_CAT_0` | STRING | Percentual total de docentes/turmas na Categoria 0 (sem formação adequada) no Ensino Fundamental. |
| `MED_01_CAT_0` | STRING | Percentual de docentes/turmas na Categoria 0 (sem formação adequada) no 1º ano do Ensino Médio. |
| `MED_02_CAT_0` | STRING | Percentual de docentes/turmas na Categoria 0 (sem formação adequada) no 2º ano do Ensino Médio. |
| `MED_03_CAT_0` | STRING | Percentual de docentes/turmas na Categoria 0 (sem formação adequada) no 3º ano do Ensino Médio. |
| `MED_04_CAT_0` | STRING | Percentual de docentes/turmas na Categoria 0 (sem formação adequada) no 4º ano do Ensino Médio. |
| `MED_CAT_0` | STRING | Percentual total de docentes/turmas na Categoria 0 (sem formação adequada) no Ensino Médio. |

## raw · inep_taxas_rendimento_escolar

File `raw__inep_taxas_rendimento_escolar.parquet` · 3,974,168 rows · 71 columns

Dados brutos estruturados das Taxas de Rendimento Escolar do INEP, preservando valores textuais dos arquivos oficiais.

**Feeds:** `trusted/inep_taxas_rendimento_escolar`

| Column | Type | Description |
|---|---|---|
| `ano_censo` | STRING | Ano de referência do Censo Escolar no arquivo de origem. |
| `nivel_agregacao` | STRING | Nível do arquivo de origem: brasil_regioes_ufs, municipios ou escolas. |
| `unidade_geografica` | STRING | Unidade geográfica agregada, quando aplicável a Brasil, regiões e UFs. |
| `regiao` | STRING | Nome da região geográfica brasileira. |
| `sg_uf` | STRING | Sigla da unidade da Federação. |
| `co_municipio` | STRING | Código IBGE do município conforme arquivo de origem. |
| `no_municipio` | STRING | Nome do município conforme arquivo de origem. |
| `co_entidade` | STRING | Código INEP da escola, quando o nível é escolas. |
| `no_entidade` | STRING | Nome da escola, quando o nível é escolas. |
| `localizacao` | STRING | Categoria de localização: Total, Urbana ou Rural. |
| `dependencia_administrativa` | STRING | Dependência administrativa/rede conforme arquivo de origem. |
| `tx_aprovacao_ef_total` | STRING | Taxa de Aprovação (%) - Ensino Fundamental de 8 e 9 anos, Total. Codigo INEP original: 1_CAT_FUN. Valor bruto textual. |
| `tx_aprovacao_ef_anos_iniciais` | STRING | Taxa de Aprovação (%) - Ensino Fundamental de 8 e 9 anos, Anos Iniciais. Codigo INEP original: 1_CAT_FUN_AI. Valor bruto textual. |
| `tx_aprovacao_ef_anos_finais` | STRING | Taxa de Aprovação (%) - Ensino Fundamental de 8 e 9 anos, Anos Finais. Codigo INEP original: 1_CAT_FUN_AF. Valor bruto textual. |
| `tx_aprovacao_ef_01` | STRING | Taxa de Aprovação (%) - Ensino Fundamental de 8 e 9 anos, 1º Ano. Codigo INEP original: 1_CAT_FUN_01. Valor bruto textual. |
| `tx_aprovacao_ef_02` | STRING | Taxa de Aprovação (%) - Ensino Fundamental de 8 e 9 anos, 2º Ano. Codigo INEP original: 1_CAT_FUN_02. Valor bruto textual. |
| `tx_aprovacao_ef_03` | STRING | Taxa de Aprovação (%) - Ensino Fundamental de 8 e 9 anos, 3º Ano. Codigo INEP original: 1_CAT_FUN_03. Valor bruto textual. |
| `tx_aprovacao_ef_04` | STRING | Taxa de Aprovação (%) - Ensino Fundamental de 8 e 9 anos, 4º Ano. Codigo INEP original: 1_CAT_FUN_04. Valor bruto textual. |
| `tx_aprovacao_ef_05` | STRING | Taxa de Aprovação (%) - Ensino Fundamental de 8 e 9 anos, 5º Ano. Codigo INEP original: 1_CAT_FUN_05. Valor bruto textual. |
| `tx_aprovacao_ef_06` | STRING | Taxa de Aprovação (%) - Ensino Fundamental de 8 e 9 anos, 6º Ano. Codigo INEP original: 1_CAT_FUN_06. Valor bruto textual. |
| `tx_aprovacao_ef_07` | STRING | Taxa de Aprovação (%) - Ensino Fundamental de 8 e 9 anos, 7º Ano. Codigo INEP original: 1_CAT_FUN_07. Valor bruto textual. |
| `tx_aprovacao_ef_08` | STRING | Taxa de Aprovação (%) - Ensino Fundamental de 8 e 9 anos, 8º Ano. Codigo INEP original: 1_CAT_FUN_08. Valor bruto textual. |
| `tx_aprovacao_ef_09` | STRING | Taxa de Aprovação (%) - Ensino Fundamental de 8 e 9 anos, 9º Ano. Codigo INEP original: 1_CAT_FUN_09. Valor bruto textual. |
| `tx_aprovacao_em_total` | STRING | Taxa de Aprovação (%) - Ensino Médio, Total. Codigo INEP original: 1_CAT_MED. Valor bruto textual. |
| `tx_aprovacao_em_01` | STRING | Taxa de Aprovação (%) - Ensino Médio, 1ª série. Codigo INEP original: 1_CAT_MED_01. Valor bruto textual. |
| `tx_aprovacao_em_02` | STRING | Taxa de Aprovação (%) - Ensino Médio, 2ª série. Codigo INEP original: 1_CAT_MED_02. Valor bruto textual. |
| `tx_aprovacao_em_03` | STRING | Taxa de Aprovação (%) - Ensino Médio, 3ª série. Codigo INEP original: 1_CAT_MED_03. Valor bruto textual. |
| `tx_aprovacao_em_04` | STRING | Taxa de Aprovação (%) - Ensino Médio, 4ª série. Codigo INEP original: 1_CAT_MED_04. Valor bruto textual. |
| `tx_aprovacao_em_nao_seriado` | STRING | Taxa de Aprovação (%) - Ensino Médio, Não-Seriado. Codigo INEP original: 1_CAT_MED_NS. Valor bruto textual. |
| `tx_reprovacao_ef_total` | STRING | Taxa de Reprovação (%) - Ensino Fundamental de 8 e 9 anos, Total. Codigo INEP original: 2_CAT_FUN. Valor bruto textual. |
| `tx_reprovacao_ef_anos_iniciais` | STRING | Taxa de Reprovação (%) - Ensino Fundamental de 8 e 9 anos, Anos Iniciais. Codigo INEP original: 2_CAT_FUN_AI. Valor bruto textual. |
| `tx_reprovacao_ef_anos_finais` | STRING | Taxa de Reprovação (%) - Ensino Fundamental de 8 e 9 anos, Anos Finais. Codigo INEP original: 2_CAT_FUN_AF. Valor bruto textual. |
| `tx_reprovacao_ef_01` | STRING | Taxa de Reprovação (%) - Ensino Fundamental de 8 e 9 anos, 1º Ano. Codigo INEP original: 2_CAT_FUN_01. Valor bruto textual. |
| `tx_reprovacao_ef_02` | STRING | Taxa de Reprovação (%) - Ensino Fundamental de 8 e 9 anos, 2º Ano. Codigo INEP original: 2_CAT_FUN_02. Valor bruto textual. |
| `tx_reprovacao_ef_03` | STRING | Taxa de Reprovação (%) - Ensino Fundamental de 8 e 9 anos, 3º Ano. Codigo INEP original: 2_CAT_FUN_03. Valor bruto textual. |
| `tx_reprovacao_ef_04` | STRING | Taxa de Reprovação (%) - Ensino Fundamental de 8 e 9 anos, 4º Ano. Codigo INEP original: 2_CAT_FUN_04. Valor bruto textual. |
| `tx_reprovacao_ef_05` | STRING | Taxa de Reprovação (%) - Ensino Fundamental de 8 e 9 anos, 5º Ano. Codigo INEP original: 2_CAT_FUN_05. Valor bruto textual. |
| `tx_reprovacao_ef_06` | STRING | Taxa de Reprovação (%) - Ensino Fundamental de 8 e 9 anos, 6º Ano. Codigo INEP original: 2_CAT_FUN_06. Valor bruto textual. |
| `tx_reprovacao_ef_07` | STRING | Taxa de Reprovação (%) - Ensino Fundamental de 8 e 9 anos, 7º Ano. Codigo INEP original: 2_CAT_FUN_07. Valor bruto textual. |
| `tx_reprovacao_ef_08` | STRING | Taxa de Reprovação (%) - Ensino Fundamental de 8 e 9 anos, 8º Ano. Codigo INEP original: 2_CAT_FUN_08. Valor bruto textual. |
| `tx_reprovacao_ef_09` | STRING | Taxa de Reprovação (%) - Ensino Fundamental de 8 e 9 anos, 9º Ano. Codigo INEP original: 2_CAT_FUN_09. Valor bruto textual. |
| `tx_reprovacao_em_total` | STRING | Taxa de Reprovação (%) - Ensino Médio, Total. Codigo INEP original: 2_CAT_MED. Valor bruto textual. |
| `tx_reprovacao_em_01` | STRING | Taxa de Reprovação (%) - Ensino Médio, 1ª série. Codigo INEP original: 2_CAT_MED_01. Valor bruto textual. |
| `tx_reprovacao_em_02` | STRING | Taxa de Reprovação (%) - Ensino Médio, 2ª série. Codigo INEP original: 2_CAT_MED_02. Valor bruto textual. |
| `tx_reprovacao_em_03` | STRING | Taxa de Reprovação (%) - Ensino Médio, 3ª série. Codigo INEP original: 2_CAT_MED_03. Valor bruto textual. |
| `tx_reprovacao_em_04` | STRING | Taxa de Reprovação (%) - Ensino Médio, 4ª série. Codigo INEP original: 2_CAT_MED_04. Valor bruto textual. |
| `tx_reprovacao_em_nao_seriado` | STRING | Taxa de Reprovação (%) - Ensino Médio, Não-Seriado. Codigo INEP original: 2_CAT_MED_NS. Valor bruto textual. |
| `tx_abandono_ef_total` | STRING | Taxa de Abandono (%) - Ensino Fundamental de 8 e 9 anos, Total. Codigo INEP original: 3_CAT_FUN. Valor bruto textual. |
| `tx_abandono_ef_anos_iniciais` | STRING | Taxa de Abandono (%) - Ensino Fundamental de 8 e 9 anos, Anos Iniciais. Codigo INEP original: 3_CAT_FUN_AI. Valor bruto textual. |
| `tx_abandono_ef_anos_finais` | STRING | Taxa de Abandono (%) - Ensino Fundamental de 8 e 9 anos, Anos Finais. Codigo INEP original: 3_CAT_FUN_AF. Valor bruto textual. |
| `tx_abandono_ef_01` | STRING | Taxa de Abandono (%) - Ensino Fundamental de 8 e 9 anos, 1º Ano. Codigo INEP original: 3_CAT_FUN_01. Valor bruto textual. |
| `tx_abandono_ef_02` | STRING | Taxa de Abandono (%) - Ensino Fundamental de 8 e 9 anos, 2º Ano. Codigo INEP original: 3_CAT_FUN_02. Valor bruto textual. |
| `tx_abandono_ef_03` | STRING | Taxa de Abandono (%) - Ensino Fundamental de 8 e 9 anos, 3º Ano. Codigo INEP original: 3_CAT_FUN_03. Valor bruto textual. |
| `tx_abandono_ef_04` | STRING | Taxa de Abandono (%) - Ensino Fundamental de 8 e 9 anos, 4º Ano. Codigo INEP original: 3_CAT_FUN_04. Valor bruto textual. |
| `tx_abandono_ef_05` | STRING | Taxa de Abandono (%) - Ensino Fundamental de 8 e 9 anos, 5º Ano. Codigo INEP original: 3_CAT_FUN_05. Valor bruto textual. |
| `tx_abandono_ef_06` | STRING | Taxa de Abandono (%) - Ensino Fundamental de 8 e 9 anos, 6º Ano. Codigo INEP original: 3_CAT_FUN_06. Valor bruto textual. |
| `tx_abandono_ef_07` | STRING | Taxa de Abandono (%) - Ensino Fundamental de 8 e 9 anos, 7º Ano. Codigo INEP original: 3_CAT_FUN_07. Valor bruto textual. |
| `tx_abandono_ef_08` | STRING | Taxa de Abandono (%) - Ensino Fundamental de 8 e 9 anos, 8º Ano. Codigo INEP original: 3_CAT_FUN_08. Valor bruto textual. |
| `tx_abandono_ef_09` | STRING | Taxa de Abandono (%) - Ensino Fundamental de 8 e 9 anos, 9º Ano. Codigo INEP original: 3_CAT_FUN_09. Valor bruto textual. |
| `tx_abandono_em_total` | STRING | Taxa de Abandono (%) - Ensino Médio, Total. Codigo INEP original: 3_CAT_MED. Valor bruto textual. |
| `tx_abandono_em_01` | STRING | Taxa de Abandono (%) - Ensino Médio, 1ª série. Codigo INEP original: 3_CAT_MED_01. Valor bruto textual. |
| `tx_abandono_em_02` | STRING | Taxa de Abandono (%) - Ensino Médio, 2ª série. Codigo INEP original: 3_CAT_MED_02. Valor bruto textual. |
| `tx_abandono_em_03` | STRING | Taxa de Abandono (%) - Ensino Médio, 3ª série. Codigo INEP original: 3_CAT_MED_03. Valor bruto textual. |
| `tx_abandono_em_04` | STRING | Taxa de Abandono (%) - Ensino Médio, 4ª série. Codigo INEP original: 3_CAT_MED_04. Valor bruto textual. |
| `tx_abandono_em_nao_seriado` | STRING | Taxa de Abandono (%) - Ensino Médio, Não-Seriado. Codigo INEP original: 3_CAT_MED_NS. Valor bruto textual. |
| `fonte_pagina_url` | STRING | URL da página oficial do INEP de onde o link foi coletado. |
| `fonte_download_url` | STRING | URL oficial do arquivo ZIP baixado. |
| `fonte_arquivo_zip` | STRING | Nome do ZIP oficial baixado. |
| `fonte_arquivo_planilha` | STRING | Nome da planilha lida dentro do ZIP. |
| `fonte_aba` | STRING | Nome da aba da planilha de origem. |
| `dt_ingestao_lake` | TIMESTAMP | Data/hora de ingestão no data lake. |

## raw · inep_taxas_rendimento_escolar_arquivos

File `raw__inep_taxas_rendimento_escolar_arquivos.parquet` · 54 rows · 11 columns

Catálogo dos arquivos oficiais de Taxas de Rendimento Escolar baixados do INEP.

| Column | Type | Description |
|---|---|---|
| `ano` | INTEGER | Ano de referência do arquivo. |
| `nivel_agregacao` | STRING | Nível do arquivo: brasil_regioes_ufs, municipios ou escolas. |
| `rotulo_origem` | STRING | Rótulo do link na página oficial do INEP. |
| `pagina_url` | STRING | URL da página oficial do INEP. |
| `download_url` | STRING | URL oficial do ZIP. |
| `arquivo_zip` | STRING | Nome do arquivo ZIP. |
| `tamanho_bytes` | INTEGER | Tamanho do ZIP baixado em bytes. |
| `sha256` | STRING | Hash SHA-256 calculado após download. |
| `dt_descoberta_utc` | STRING | Timestamp UTC de descoberta do link. |
| `dt_download_utc` | STRING | Timestamp UTC do download. |
| `dt_ingestao_lake` | TIMESTAMP | Data/hora de ingestão no data lake. |

## trusted · inep_taxa_distorcao_brasil_regioes_ufs

File `trusted__inep_taxa_distorcao_brasil_regioes_ufs.parquet` · 7,356 rows · 24 columns

Taxa de Distorcao Idade-Serie (TDI) nacional, regioes e UFs. INEP 2006-2025. tipo_unidade: brasil | regiao | uf. Grain: (unidade_geografica, ano, no_categoria, no_dependencia). Para 2015-2018 o arquivo fonte do INEP usa nomes de coluna legados (TIPOLOCA/DEPENDAD/TDI_*, NO_CODIGO ou NO_REGIAO para a unidade geografica) em vez do schema 2016+; esta query usa COALESCE para unificar ambas as variantes. Para 2006-2009 o arquivo fonte nao publica nivel Brasil/UF separado: NO_CATEGORIA guarda a sigla da UF em vez de Total/Urbana/Rural; estas linhas sao reclassificadas como tipo_unidade='uf'. Brasil/UF genuinamente nao publicados pelo INEP para 2006-2010 (so nivel regiao disponivel nesses anos).

**Built from:** `raw/inep_taxa_distorcao_brasil_regioes_ufs`

**Feeds:** `semantic/obt_inep_taxa_distorcao_brasil_ano`, `semantic/obt_inep_taxa_distorcao_regiao_ano`, `semantic/obt_inep_taxa_distorcao_uf_ano`

| Column | Type | Description |
|---|---|---|
| `ano` | INTEGER | Ano de referencia. |
| `unidade_geografica` | STRING | Unidade geografica. |
| `tipo_unidade` | STRING | Tipo. |
| `sg_uf` | STRING | Sigla da UF. |
| `no_categoria` | STRING | Nome. |
| `no_dependencia` | STRING | Nome. |
| `taxa_distorcao_ef_total` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_ef_ai` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_ef_af` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_ef_1ano` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_ef_2ano` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_ef_3ano` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_ef_4ano` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_ef_5ano` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_ef_6ano` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_ef_7ano` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_ef_8ano` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_ef_9ano` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_em_total` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_em_1serie` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_em_2serie` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_em_3serie` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_em_4serie` | FLOAT | Taxa / percentual (%). |
| `dt_ingestao_lake` | STRING | Timestamp UTC da carga no lake. |

## trusted · inep_taxa_distorcao_escolas

File `trusted__inep_taxa_distorcao_escolas.parquet` · 2,148,183 rows · 27 columns

Taxa de Distorcao Idade-Serie (TDI) por escola. INEP 2006-2025. Grain: (co_entidade, ano, no_categoria, no_dependencia). no_categoria: Total/Urbana/Rural. no_dependencia: Total/Federal/Estadual/Municipal/Privada. Para 2015-2018 o arquivo fonte do INEP usa nomes de coluna legados (TIPOLOCA/DEPENDAD/TDI_*) em vez do schema 2016+; esta query usa COALESCE para unificar ambas as variantes. Para 2013-2014 o ano vem da coluna legada 'Ano' em vez de NU_ANO_CENSO. Para 2007 e 2009 as colunas CO_ENTIDADE/NO_ENTIDADE vem trocadas na fonte; deteccao via SAFE_CAST corrige.

**Built from:** `raw/inep_taxa_distorcao_escolas`

**Feeds:** `semantic/obt_inep_taxa_distorcao_escola_ano`

| Column | Type | Description |
|---|---|---|
| `ano` | INTEGER | Ano de referencia. |
| `no_regiao` | STRING | Nome da regiao geografica. |
| `sg_uf` | STRING | Sigla da UF. |
| `co_municipio` | INTEGER | Codigo IBGE do municipio. |
| `no_municipio` | STRING | Nome do municipio. |
| `co_entidade` | INTEGER | Codigo INEP da escola/entidade. |
| `no_entidade` | STRING | Nome da escola/entidade. |
| `no_categoria` | STRING | Nome. |
| `no_dependencia` | STRING | Nome. |
| `taxa_distorcao_ef_total` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_ef_ai` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_ef_af` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_ef_1ano` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_ef_2ano` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_ef_3ano` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_ef_4ano` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_ef_5ano` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_ef_6ano` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_ef_7ano` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_ef_8ano` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_ef_9ano` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_em_total` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_em_1serie` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_em_2serie` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_em_3serie` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_em_4serie` | FLOAT | Taxa / percentual (%). |
| `dt_ingestao_lake` | STRING | Timestamp UTC da carga no lake. |

## trusted · inep_taxa_distorcao_municipios

File `trusted__inep_taxa_distorcao_municipios.parquet` · 982,486 rows · 25 columns

Taxa de Distorcao Idade-Serie (TDI) por municipio. INEP 2006-2025. Grain: (co_municipio, ano, no_categoria, no_dependencia). ~5600 municipios x 20 anos x ~10 linhas cada. Para 2015-2018 o arquivo fonte do INEP usa nomes de coluna legados (TIPOLOCA/DEPENDAD/TDI_*) em vez do schema 2016+; esta query usa COALESCE para unificar ambas as variantes.

**Built from:** `raw/inep_taxa_distorcao_municipios`

**Feeds:** `semantic/obt_inep_taxa_distorcao_municipio_ano`

| Column | Type | Description |
|---|---|---|
| `ano` | INTEGER | Ano de referencia. |
| `no_regiao` | STRING | Nome da regiao geografica. |
| `sg_uf` | STRING | Sigla da UF. |
| `co_municipio` | INTEGER | Codigo IBGE do municipio. |
| `no_municipio` | STRING | Nome do municipio. |
| `no_categoria` | STRING | Nome. |
| `no_dependencia` | STRING | Nome. |
| `taxa_distorcao_ef_total` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_ef_ai` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_ef_af` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_ef_1ano` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_ef_2ano` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_ef_3ano` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_ef_4ano` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_ef_5ano` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_ef_6ano` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_ef_7ano` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_ef_8ano` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_ef_9ano` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_em_total` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_em_1serie` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_em_2serie` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_em_3serie` | FLOAT | Taxa / percentual (%). |
| `taxa_distorcao_em_4serie` | FLOAT | Taxa / percentual (%). |
| `dt_ingestao_lake` | STRING | Timestamp UTC da carga no lake. |

## trusted · inep_taxas_rendimento_escolar

File `trusted__inep_taxas_rendimento_escolar.parquet` · 3,974,168 rows · 71 columns

Taxa de Rendimento Escolar INEP -- aprovacao, reprovacao e abandono por escola, etapa e serie. Anual. Fonte: INEP indicadores educacionais.

**Built from:** `raw/inep_taxas_rendimento_escolar`

**Feeds:** `semantic/obt_inep_taxa_rendimento_brasil_ano`, `semantic/obt_inep_taxa_rendimento_escola_ano`, `semantic/obt_inep_taxa_rendimento_municipio_ano`, `semantic/obt_inep_taxa_rendimento_regiao_ano`, `semantic/obt_inep_taxa_rendimento_uf_ano`, `trusted/inep_taxas_rendimento_escolar_long`

| Column | Type | Description |
|---|---|---|
| `ano_censo` | INTEGER | Ano do Censo Escolar. |
| `nivel_agregacao` | STRING | Nivel agregacao. |
| `unidade_geografica` | STRING | Unidade geografica. |
| `regiao` | STRING | Regiao geografica. |
| `sg_uf` | STRING | Sigla da UF. |
| `co_municipio` | INTEGER | Codigo IBGE do municipio. |
| `no_municipio` | STRING | Nome do municipio. |
| `co_entidade` | INTEGER | Codigo INEP da escola/entidade. |
| `no_entidade` | STRING | Nome da escola/entidade. |
| `localizacao` | STRING | Localizacao (Urbana/Rural). |
| `dependencia_administrativa` | STRING | Dependencia administrativa (Federal, Estadual, Municipal, Privada). |
| `fonte_pagina_url` | STRING | Fonte pagina url. |
| `fonte_download_url` | STRING | Fonte download url. |
| `fonte_arquivo_zip` | STRING | Fonte arquivo zip. |
| `fonte_arquivo_planilha` | STRING | Fonte arquivo planilha. |
| `fonte_aba` | STRING | Fonte aba. |
| `tx_aprovacao_ef_total` | FLOAT | Taxa / percentual (%). |
| `tx_aprovacao_ef_anos_iniciais` | FLOAT | Taxa / percentual (%). |
| `tx_aprovacao_ef_anos_finais` | FLOAT | Taxa / percentual (%). |
| `tx_aprovacao_ef_01` | FLOAT | Taxa / percentual (%). |
| `tx_aprovacao_ef_02` | FLOAT | Taxa / percentual (%). |
| `tx_aprovacao_ef_03` | FLOAT | Taxa / percentual (%). |
| `tx_aprovacao_ef_04` | FLOAT | Taxa / percentual (%). |
| `tx_aprovacao_ef_05` | FLOAT | Taxa / percentual (%). |
| `tx_aprovacao_ef_06` | FLOAT | Taxa / percentual (%). |
| `tx_aprovacao_ef_07` | FLOAT | Taxa / percentual (%). |
| `tx_aprovacao_ef_08` | FLOAT | Taxa / percentual (%). |
| `tx_aprovacao_ef_09` | FLOAT | Taxa / percentual (%). |
| `tx_aprovacao_em_total` | FLOAT | Taxa / percentual (%). |
| `tx_aprovacao_em_01` | FLOAT | Taxa / percentual (%). |
| `tx_aprovacao_em_02` | FLOAT | Taxa / percentual (%). |
| `tx_aprovacao_em_03` | FLOAT | Taxa / percentual (%). |
| `tx_aprovacao_em_04` | FLOAT | Taxa / percentual (%). |
| `tx_aprovacao_em_nao_seriado` | FLOAT | Taxa / percentual (%). |
| `tx_reprovacao_ef_total` | FLOAT | Taxa / percentual (%). |
| `tx_reprovacao_ef_anos_iniciais` | FLOAT | Taxa / percentual (%). |
| `tx_reprovacao_ef_anos_finais` | FLOAT | Taxa / percentual (%). |
| `tx_reprovacao_ef_01` | FLOAT | Taxa / percentual (%). |
| `tx_reprovacao_ef_02` | FLOAT | Taxa / percentual (%). |
| `tx_reprovacao_ef_03` | FLOAT | Taxa / percentual (%). |
| `tx_reprovacao_ef_04` | FLOAT | Taxa / percentual (%). |
| `tx_reprovacao_ef_05` | FLOAT | Taxa / percentual (%). |
| `tx_reprovacao_ef_06` | FLOAT | Taxa / percentual (%). |
| `tx_reprovacao_ef_07` | FLOAT | Taxa / percentual (%). |
| `tx_reprovacao_ef_08` | FLOAT | Taxa / percentual (%). |
| `tx_reprovacao_ef_09` | FLOAT | Taxa / percentual (%). |
| `tx_reprovacao_em_total` | FLOAT | Taxa / percentual (%). |
| `tx_reprovacao_em_01` | FLOAT | Taxa / percentual (%). |
| `tx_reprovacao_em_02` | FLOAT | Taxa / percentual (%). |
| `tx_reprovacao_em_03` | FLOAT | Taxa / percentual (%). |
| `tx_reprovacao_em_04` | FLOAT | Taxa / percentual (%). |
| `tx_reprovacao_em_nao_seriado` | FLOAT | Taxa / percentual (%). |
| `tx_abandono_ef_total` | FLOAT | Taxa / percentual (%). |
| `tx_abandono_ef_anos_iniciais` | FLOAT | Taxa / percentual (%). |
| `tx_abandono_ef_anos_finais` | FLOAT | Taxa / percentual (%). |
| `tx_abandono_ef_01` | FLOAT | Taxa / percentual (%). |
| `tx_abandono_ef_02` | FLOAT | Taxa / percentual (%). |
| `tx_abandono_ef_03` | FLOAT | Taxa / percentual (%). |
| `tx_abandono_ef_04` | FLOAT | Taxa / percentual (%). |
| `tx_abandono_ef_05` | FLOAT | Taxa / percentual (%). |
| `tx_abandono_ef_06` | FLOAT | Taxa / percentual (%). |
| `tx_abandono_ef_07` | FLOAT | Taxa / percentual (%). |
| `tx_abandono_ef_08` | FLOAT | Taxa / percentual (%). |
| `tx_abandono_ef_09` | FLOAT | Taxa / percentual (%). |
| `tx_abandono_em_total` | FLOAT | Taxa / percentual (%). |
| `tx_abandono_em_01` | FLOAT | Taxa / percentual (%). |
| `tx_abandono_em_02` | FLOAT | Taxa / percentual (%). |
| `tx_abandono_em_03` | FLOAT | Taxa / percentual (%). |
| `tx_abandono_em_04` | FLOAT | Taxa / percentual (%). |
| `tx_abandono_em_nao_seriado` | FLOAT | Taxa / percentual (%). |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC da carga no lake. |

## trusted · inep_taxas_rendimento_escolar_long

File `trusted__inep_taxas_rendimento_escolar_long.parquet` · 204,107,094 rows · 25 columns

Tabela trusted long das Taxas de Rendimento Escolar do INEP, uma linha por taxa/etapa/série.

**Built from:** `trusted/inep_taxas_rendimento_escolar`

**Feeds:** `trusted/inep_taxas_rendimento_escolar_qualidade`

| Column | Type | Description |
|---|---|---|
| `ano_censo` | INTEGER | Ano de referência do Censo Escolar. |
| `nivel_agregacao` | STRING | Nível de agregação: brasil_regioes_ufs, municipios ou escolas. |
| `unidade_geografica` | STRING | Unidade geográfica agregada, quando aplicável. |
| `regiao` | STRING | Nome da região geográfica brasileira. |
| `sg_uf` | STRING | Sigla da unidade da Federação. |
| `co_municipio` | INTEGER | Código IBGE do município. |
| `no_municipio` | STRING | Nome do município. |
| `co_entidade` | INTEGER | Código INEP da escola. |
| `no_entidade` | STRING | Nome da escola. |
| `localizacao` | STRING | Categoria de localização: Total, Urbana ou Rural. |
| `tp_localizacao` | INTEGER | Código derivado da localização: 0=Total, 1=Urbana, 2=Rural. |
| `dependencia_administrativa` | STRING | Dependência administrativa/rede. |
| `tp_dependencia` | INTEGER | Código derivado da dependência administrativa/rede. |
| `taxa_tipo` | STRING | Tipo da taxa: aprovacao, reprovacao ou abandono. |
| `taxa_tipo_nome` | STRING | Nome do tipo da taxa. |
| `etapa_ensino` | STRING | Etapa de ensino normalizada: ensino_fundamental ou ensino_medio. |
| `etapa_ensino_nome` | STRING | Nome da etapa de ensino. |
| `serie_ano` | STRING | Série/ano/agrupamento normalizado. |
| `serie_ano_nome` | STRING | Nome da série/ano/agrupamento. |
| `codigo_variavel_original` | STRING | Código original da variável nos arquivos modernos do INEP. |
| `valor_taxa` | FLOAT | Valor percentual da taxa de rendimento escolar. |
| `fonte_arquivo_zip` | STRING | Nome do ZIP oficial baixado. |
| `fonte_arquivo_planilha` | STRING | Nome da planilha lida dentro do ZIP. |
| `fonte_aba` | STRING | Nome da aba da planilha de origem. |
| `dt_ingestao_lake` | TIMESTAMP | Data/hora de ingestão no data lake. |

## trusted · inep_taxas_rendimento_escolar_qualidade

File `trusted__inep_taxas_rendimento_escolar_qualidade.parquet` · 8 rows · 28 columns

Tabela trusted de anomalias de qualidade encontradas nas Taxas de Rendimento Escolar do INEP.

**Built from:** `trusted/inep_taxas_rendimento_escolar_long`

| Column | Type | Description |
|---|---|---|
| `tipo_anomalia` | STRING | Codigo da regra de qualidade violada. |
| `descricao_anomalia` | STRING | Descricao curta da anomalia identificada. |
| `ano_censo` | INTEGER | Ano de referência do Censo Escolar. |
| `nivel_agregacao` | STRING | Nível de agregação: brasil_regioes_ufs, municipios ou escolas. |
| `unidade_geografica` | STRING | Unidade geográfica agregada, quando aplicável. |
| `regiao` | STRING | Nome da região geográfica brasileira. |
| `sg_uf` | STRING | Sigla da unidade da Federação. |
| `co_municipio` | INTEGER | Código IBGE do município. |
| `no_municipio` | STRING | Nome do município. |
| `co_entidade` | INTEGER | Código INEP da escola. |
| `no_entidade` | STRING | Nome da escola. |
| `localizacao` | STRING | Categoria de localização: Total, Urbana ou Rural. |
| `tp_localizacao` | INTEGER | Código derivado da localização: 0=Total, 1=Urbana, 2=Rural. |
| `dependencia_administrativa` | STRING | Dependência administrativa/rede. |
| `tp_dependencia` | INTEGER | Código derivado da dependência administrativa/rede. |
| `taxa_tipo` | STRING | Tipo da taxa: aprovacao, reprovacao ou abandono. |
| `taxa_tipo_nome` | STRING | Nome do tipo da taxa. |
| `etapa_ensino` | STRING | Etapa de ensino normalizada: ensino_fundamental ou ensino_medio. |
| `etapa_ensino_nome` | STRING | Nome da etapa de ensino. |
| `serie_ano` | STRING | Série/ano/agrupamento normalizado. |
| `serie_ano_nome` | STRING | Nome da série/ano/agrupamento. |
| `codigo_variavel_original` | STRING | Código original da variável nos arquivos modernos do INEP. |
| `valor_taxa` | FLOAT | Valor percentual da taxa de rendimento escolar. |
| `fonte_arquivo_zip` | STRING | Nome do ZIP oficial baixado. |
| `fonte_arquivo_planilha` | STRING | Nome da planilha lida dentro do ZIP. |
| `fonte_aba` | STRING | Nome da aba da planilha de origem. |
| `dt_ingestao_lake` | TIMESTAMP | Data/hora de ingestão no data lake. |
| `dt_validacao_lake` | TIMESTAMP | Data/hora em que a regra de qualidade foi avaliada. |
