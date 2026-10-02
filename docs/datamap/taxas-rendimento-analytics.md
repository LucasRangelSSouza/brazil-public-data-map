# School flow and distortion rates (INEP): Analytics

Dataset: [lucasrangelss/taxas-rendimento-analytics](https://www.kaggle.com/datasets/lucasrangelss/taxas-rendimento-analytics) · snapshot 2026-10-01 · 10 tables · 5,003,248 rows

**Source:** Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP), [https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais)

Approval, failure and dropout rates and the age-grade distortion rate by school, municipality, state, region and Brazil, per year.

**Grain and keys:** School, municipality, state, region or Brazil by year.

**Layers.** `raw` is the source snapshot as delivered. `trusted` is typed, deduplicated and named consistently. `semantic` joins and reshapes trusted tables for analysis. Every table is a Parquet file named `<layer>__<table>.parquet` at the root of the dataset.

The full interactive map (lineage, joins, search) is at [https://rangeltech.net/datamap/](https://rangeltech.net/datamap/). Column descriptions come from the source lake's catalogue and are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns | Described | Upstream |
|---|---|---:|---:|---:|---|
| semantic | [`obt_inep_taxa_distorcao_brasil_ano`](#semantic-obt-inep-taxa-distorcao-brasil-ano) | 90 | 20 | 20 | `inep_taxa_distorcao_brasil_regioes_ufs` |
| semantic | [`obt_inep_taxa_distorcao_escola_ano`](#semantic-obt-inep-taxa-distorcao-escola-ano) | 2,148,183 | 31 | 31 | `inep_taxa_distorcao_escolas` |
| semantic | [`obt_inep_taxa_distorcao_municipio_ano`](#semantic-obt-inep-taxa-distorcao-municipio-ano) | 81,730 | 26 | 26 | `inep_taxa_distorcao_municipios` |
| semantic | [`obt_inep_taxa_distorcao_regiao_ano`](#semantic-obt-inep-taxa-distorcao-regiao-ano) | 300 | 22 | 22 | `inep_taxa_distorcao_brasil_regioes_ufs` |
| semantic | [`obt_inep_taxa_distorcao_uf_ano`](#semantic-obt-inep-taxa-distorcao-uf-ano) | 3,332 | 23 | 23 | `inep_taxa_distorcao_brasil_regioes_ufs` |
| semantic | [`obt_inep_taxa_rendimento_brasil_ano`](#semantic-obt-inep-taxa-rendimento-brasil-ano) | 342 | 16 | 16 | `inep_taxas_rendimento_escolar` |
| semantic | [`obt_inep_taxa_rendimento_escola_ano`](#semantic-obt-inep-taxa-rendimento-escola-ano) | 2,652,720 | 25 | 25 | `inep_taxas_rendimento_escolar` |
| semantic | [`obt_inep_taxa_rendimento_municipio_ano`](#semantic-obt-inep-taxa-rendimento-municipio-ano) | 105,799 | 21 | 21 | `inep_taxas_rendimento_escolar` |
| semantic | [`obt_inep_taxa_rendimento_regiao_ano`](#semantic-obt-inep-taxa-rendimento-regiao-ano) | 1,710 | 18 | 18 | `inep_taxas_rendimento_escolar` |
| semantic | [`obt_inep_taxa_rendimento_uf_ano`](#semantic-obt-inep-taxa-rendimento-uf-ano) | 9,042 | 19 | 19 | `inep_taxas_rendimento_escolar` |

## semantic · obt_inep_taxa_distorcao_brasil_ano

File `semantic__obt_inep_taxa_distorcao_brasil_ano.parquet` · 90 rows · 20 columns

Taxa de Distorcao Idade-Serie (TDI) nacional por ano e dependencia. Grao: (ano, rede). Filtro: tipo_unidade=brasil, no_categoria=Total. Origem: trusted/inep_taxa_distorcao_brasil_regioes_ufs. INEP 2006-2025.

**Built from:** `trusted/inep_taxa_distorcao_brasil_regioes_ufs`

| Column | Type | Description |
|---|---|---|
| `ano` | INTEGER | Ano do levantamento TDI (INEP). INT64. Coluna de particao. |
| `rede` | STRING | Dependencia administrativa (Total/Federal/Estadual/Municipal/Privada). |
| `taxa_distorcao_ef_total` | FLOAT | Taxa Distorcao Idade-Serie EF total (Anos Iniciais + Finais). Percentual. |
| `taxa_distorcao_ef_ai` | FLOAT | Taxa Distorcao Idade-Serie EF Anos Iniciais (1o ao 5o ano). Percentual. |
| `taxa_distorcao_ef_af` | FLOAT | Taxa Distorcao Idade-Serie EF Anos Finais (6o ao 9o ano). Percentual. |
| `taxa_distorcao_ef_1ano` | FLOAT | TDI EF 1o ano. Percentual. |
| `taxa_distorcao_ef_2ano` | FLOAT | TDI EF 2o ano. Percentual. |
| `taxa_distorcao_ef_3ano` | FLOAT | TDI EF 3o ano. Percentual. |
| `taxa_distorcao_ef_4ano` | FLOAT | TDI EF 4o ano. Percentual. |
| `taxa_distorcao_ef_5ano` | FLOAT | TDI EF 5o ano. Percentual. |
| `taxa_distorcao_ef_6ano` | FLOAT | TDI EF 6o ano. Percentual. |
| `taxa_distorcao_ef_7ano` | FLOAT | TDI EF 7o ano. Percentual. |
| `taxa_distorcao_ef_8ano` | FLOAT | TDI EF 8o ano. Percentual. |
| `taxa_distorcao_ef_9ano` | FLOAT | TDI EF 9o ano. Percentual. |
| `taxa_distorcao_em_total` | FLOAT | Taxa Distorcao Idade-Serie EM total. Percentual. |
| `taxa_distorcao_em_1serie` | FLOAT | TDI EM 1a serie. Percentual. |
| `taxa_distorcao_em_2serie` | FLOAT | TDI EM 2a serie. Percentual. |
| `taxa_distorcao_em_3serie` | FLOAT | TDI EM 3a serie. Percentual. |
| `taxa_distorcao_em_4serie` | FLOAT | TDI EM 4a serie (EM integrado/profissionalizante). Percentual. |
| `data_carga_semantica` | TIMESTAMP | Timestamp UTC de geracao da tabela na semantic/ |

## semantic · obt_inep_taxa_distorcao_escola_ano

File `semantic__obt_inep_taxa_distorcao_escola_ano.parquet` · 2,148,183 rows · 31 columns

Taxa de Distorcao Idade-Serie (TDI) por escola e ano. Grao: (codigo_escola, ano). 1 linha por escola/ano. Origem: trusted/inep_taxa_distorcao_escolas. INEP 2006-2025. FK: codigo_escola = obt_inep_censo_escola_ano.codigo_escola. FK: codigo_municipio -> obt_ibge_municipio.

**Built from:** `trusted/inep_taxa_distorcao_escolas`

| Column | Type | Description |
|---|---|---|
| `ano` | INTEGER | Ano do levantamento TDI (INEP). INT64. Coluna de particao. |
| `sg_uf` | STRING | Sigla 2 letras da UF da escola (SG_UF). |
| `sigla_uf` | STRING | Alias/redundância para a sigla da UF da escola. — descrição gerada por IA. |
| `regiao` | STRING | Nome da regiao geografica da escola. |
| `nome_regiao` | STRING | Alias/redundância para o nome da região geográfica. — descrição gerada por IA. |
| `codigo_municipio` | INTEGER | Codigo IBGE 7 digitos do municipio da escola. |
| `municipio` | STRING | Nome do municipio da escola. |
| `nome_municipio` | STRING | Alias/redundância para o nome do município da escola. — descrição gerada por IA. |
| `codigo_escola` | INTEGER | Codigo INEP da escola (co_entidade). INT64. PK composta com ano. |
| `escola` | STRING | Nome da escola (no_entidade). |
| `nome_escola` | STRING | Alias/redundância para o nome oficial da escola. — descrição gerada por IA. |
| `tdi_categoria` | STRING | Categoria da escola (ex: Escola de Ensino Basico, EE Especial). |
| `tdi_dependencia` | STRING | Dependencia administrativa (Federal/Estadual/Municipal/Privada). |
| `taxa_distorcao_ef_total` | FLOAT | Taxa Distorcao Idade-Serie EF total (Anos Iniciais + Finais). Percentual. |
| `taxa_distorcao_ef_ai` | FLOAT | Taxa Distorcao Idade-Serie EF Anos Iniciais (1o ao 5o ano). Percentual. |
| `taxa_distorcao_ef_af` | FLOAT | Taxa Distorcao Idade-Serie EF Anos Finais (6o ao 9o ano). Percentual. |
| `taxa_distorcao_ef_1ano` | FLOAT | TDI EF 1o ano. Percentual. |
| `taxa_distorcao_ef_2ano` | FLOAT | TDI EF 2o ano. Percentual. |
| `taxa_distorcao_ef_3ano` | FLOAT | TDI EF 3o ano. Percentual. |
| `taxa_distorcao_ef_4ano` | FLOAT | TDI EF 4o ano. Percentual. |
| `taxa_distorcao_ef_5ano` | FLOAT | TDI EF 5o ano. Percentual. |
| `taxa_distorcao_ef_6ano` | FLOAT | TDI EF 6o ano. Percentual. |
| `taxa_distorcao_ef_7ano` | FLOAT | TDI EF 7o ano. Percentual. |
| `taxa_distorcao_ef_8ano` | FLOAT | TDI EF 8o ano. Percentual. |
| `taxa_distorcao_ef_9ano` | FLOAT | TDI EF 9o ano. Percentual. |
| `taxa_distorcao_em_total` | FLOAT | Taxa Distorcao Idade-Serie EM total. Percentual. |
| `taxa_distorcao_em_1serie` | FLOAT | TDI EM 1a serie. Percentual. |
| `taxa_distorcao_em_2serie` | FLOAT | TDI EM 2a serie. Percentual. |
| `taxa_distorcao_em_3serie` | FLOAT | TDI EM 3a serie. Percentual. |
| `taxa_distorcao_em_4serie` | FLOAT | TDI EM 4a serie (EM integrado/profissionalizante). Percentual. |
| `data_carga_semantica` | TIMESTAMP | Timestamp UTC de geracao da tabela na semantic/ |

## semantic · obt_inep_taxa_distorcao_municipio_ano

File `semantic__obt_inep_taxa_distorcao_municipio_ano.parquet` · 81,730 rows · 26 columns

Taxa de Distorcao Idade-Serie (TDI) por municipio e ano. Grao: (codigo_municipio, ano). Filtro: Total/Total. Origem: trusted/inep_taxa_distorcao_municipios. INEP 2006-2025. FK: codigo_municipio -> obt_ibge_municipio.

**Built from:** `trusted/inep_taxa_distorcao_municipios`

| Column | Type | Description |
|---|---|---|
| `ano` | INTEGER | Ano do levantamento TDI (INEP). INT64. Coluna de particao. |
| `sg_uf` | STRING | Sigla 2 letras da UF do municipio. |
| `sigla_uf` | STRING | Sigla da Unidade Federativa (duplicação descritiva de sg_uf para facilitar consultas semânticas). — descrição gerada por IA. |
| `regiao` | STRING | Nome da regiao geografica. |
| `nome_regiao` | STRING | Nome da região do país (duplicação descritiva da coluna regiao). — descrição gerada por IA. |
| `codigo_municipio` | INTEGER | Codigo IBGE 7 digitos do municipio. INT64. PK composta com ano. |
| `municipio` | STRING | Nome do municipio. |
| `nome_municipio` | STRING | Nome oficial do município (duplicação descritiva da coluna municipio). — descrição gerada por IA. |
| `taxa_distorcao_ef_total` | FLOAT | Taxa Distorcao Idade-Serie EF total (Anos Iniciais + Finais). Percentual. |
| `taxa_distorcao_ef_ai` | FLOAT | Taxa Distorcao Idade-Serie EF Anos Iniciais (1o ao 5o ano). Percentual. |
| `taxa_distorcao_ef_af` | FLOAT | Taxa Distorcao Idade-Serie EF Anos Finais (6o ao 9o ano). Percentual. |
| `taxa_distorcao_ef_1ano` | FLOAT | TDI EF 1o ano. Percentual. |
| `taxa_distorcao_ef_2ano` | FLOAT | TDI EF 2o ano. Percentual. |
| `taxa_distorcao_ef_3ano` | FLOAT | TDI EF 3o ano. Percentual. |
| `taxa_distorcao_ef_4ano` | FLOAT | TDI EF 4o ano. Percentual. |
| `taxa_distorcao_ef_5ano` | FLOAT | TDI EF 5o ano. Percentual. |
| `taxa_distorcao_ef_6ano` | FLOAT | TDI EF 6o ano. Percentual. |
| `taxa_distorcao_ef_7ano` | FLOAT | TDI EF 7o ano. Percentual. |
| `taxa_distorcao_ef_8ano` | FLOAT | TDI EF 8o ano. Percentual. |
| `taxa_distorcao_ef_9ano` | FLOAT | TDI EF 9o ano. Percentual. |
| `taxa_distorcao_em_total` | FLOAT | Taxa Distorcao Idade-Serie EM total. Percentual. |
| `taxa_distorcao_em_1serie` | FLOAT | TDI EM 1a serie. Percentual. |
| `taxa_distorcao_em_2serie` | FLOAT | TDI EM 2a serie. Percentual. |
| `taxa_distorcao_em_3serie` | FLOAT | TDI EM 3a serie. Percentual. |
| `taxa_distorcao_em_4serie` | FLOAT | TDI EM 4a serie (EM integrado/profissionalizante). Percentual. |
| `data_carga_semantica` | TIMESTAMP | Timestamp UTC de geracao da tabela na semantic/ |

## semantic · obt_inep_taxa_distorcao_regiao_ano

File `semantic__obt_inep_taxa_distorcao_regiao_ano.parquet` · 300 rows · 22 columns

Taxa de Distorcao Idade-Serie (TDI) por regiao e ano. Grao: (regiao, ano, rede). Filtro: tipo_unidade=regiao, no_categoria=Total. Origem: trusted/inep_taxa_distorcao_brasil_regioes_ufs. INEP 2006-2025. Regioes: Norte / Nordeste / Sudeste / Sul / Centro-Oeste.

**Built from:** `trusted/inep_taxa_distorcao_brasil_regioes_ufs`

| Column | Type | Description |
|---|---|---|
| `ano` | INTEGER | Ano do levantamento TDI (INEP). INT64. Coluna de particao. |
| `regiao` | STRING | Nome da regiao geografica (Norte/Nordeste/Sudeste/Sul/Centro-Oeste). |
| `nome_regiao` | STRING | Nome por extenso da grande região do Brasil (ex: Centro-Oeste, Nordeste). — descrição gerada por IA. |
| `rede` | STRING | Dependencia administrativa (Total/Federal/Estadual/Municipal/Privada). |
| `taxa_distorcao_ef_total` | FLOAT | Taxa Distorcao Idade-Serie EF total (Anos Iniciais + Finais). Percentual. |
| `taxa_distorcao_ef_ai` | FLOAT | Taxa Distorcao Idade-Serie EF Anos Iniciais (1o ao 5o ano). Percentual. |
| `taxa_distorcao_ef_af` | FLOAT | Taxa Distorcao Idade-Serie EF Anos Finais (6o ao 9o ano). Percentual. |
| `taxa_distorcao_ef_1ano` | FLOAT | TDI EF 1o ano. Percentual. |
| `taxa_distorcao_ef_2ano` | FLOAT | TDI EF 2o ano. Percentual. |
| `taxa_distorcao_ef_3ano` | FLOAT | TDI EF 3o ano. Percentual. |
| `taxa_distorcao_ef_4ano` | FLOAT | TDI EF 4o ano. Percentual. |
| `taxa_distorcao_ef_5ano` | FLOAT | TDI EF 5o ano. Percentual. |
| `taxa_distorcao_ef_6ano` | FLOAT | TDI EF 6o ano. Percentual. |
| `taxa_distorcao_ef_7ano` | FLOAT | TDI EF 7o ano. Percentual. |
| `taxa_distorcao_ef_8ano` | FLOAT | TDI EF 8o ano. Percentual. |
| `taxa_distorcao_ef_9ano` | FLOAT | TDI EF 9o ano. Percentual. |
| `taxa_distorcao_em_total` | FLOAT | Taxa Distorcao Idade-Serie EM total. Percentual. |
| `taxa_distorcao_em_1serie` | FLOAT | TDI EM 1a serie. Percentual. |
| `taxa_distorcao_em_2serie` | FLOAT | TDI EM 2a serie. Percentual. |
| `taxa_distorcao_em_3serie` | FLOAT | TDI EM 3a serie. Percentual. |
| `taxa_distorcao_em_4serie` | FLOAT | TDI EM 4a serie (EM integrado/profissionalizante). Percentual. |
| `data_carga_semantica` | TIMESTAMP | Timestamp UTC de geracao da tabela na semantic/ |

## semantic · obt_inep_taxa_distorcao_uf_ano

File `semantic__obt_inep_taxa_distorcao_uf_ano.parquet` · 3,332 rows · 23 columns

Taxa de Distorcao Idade-Serie (TDI) por UF e ano. Grao: (sg_uf, ano, rede). Filtro: tipo_unidade=uf, no_categoria=Total. Origem: trusted/inep_taxa_distorcao_brasil_regioes_ufs. INEP 2006-2025.

**Built from:** `trusted/inep_taxa_distorcao_brasil_regioes_ufs`

| Column | Type | Description |
|---|---|---|
| `ano` | INTEGER | Ano do levantamento TDI (INEP). INT64. Coluna de particao. |
| `uf_nome_origem` | STRING | Nome da UF conforme arquivo fonte INEP (unidade_geografica). |
| `sg_uf` | STRING | Sigla 2 letras da UF (AC, AL, ... TO). Coluna de cluster. |
| `sigla_uf` | STRING | Sigla da Unidade da Federação relacionada à linha de dados (ex: 'AC'). — descrição gerada por IA. |
| `rede` | STRING | Dependencia administrativa (Total/Federal/Estadual/Municipal/Privada). |
| `taxa_distorcao_ef_total` | FLOAT | Taxa Distorcao Idade-Serie EF total (Anos Iniciais + Finais). Percentual. |
| `taxa_distorcao_ef_ai` | FLOAT | Taxa Distorcao Idade-Serie EF Anos Iniciais (1o ao 5o ano). Percentual. |
| `taxa_distorcao_ef_af` | FLOAT | Taxa Distorcao Idade-Serie EF Anos Finais (6o ao 9o ano). Percentual. |
| `taxa_distorcao_ef_1ano` | FLOAT | TDI EF 1o ano. Percentual. |
| `taxa_distorcao_ef_2ano` | FLOAT | TDI EF 2o ano. Percentual. |
| `taxa_distorcao_ef_3ano` | FLOAT | TDI EF 3o ano. Percentual. |
| `taxa_distorcao_ef_4ano` | FLOAT | TDI EF 4o ano. Percentual. |
| `taxa_distorcao_ef_5ano` | FLOAT | TDI EF 5o ano. Percentual. |
| `taxa_distorcao_ef_6ano` | FLOAT | TDI EF 6o ano. Percentual. |
| `taxa_distorcao_ef_7ano` | FLOAT | TDI EF 7o ano. Percentual. |
| `taxa_distorcao_ef_8ano` | FLOAT | TDI EF 8o ano. Percentual. |
| `taxa_distorcao_ef_9ano` | FLOAT | TDI EF 9o ano. Percentual. |
| `taxa_distorcao_em_total` | FLOAT | Taxa Distorcao Idade-Serie EM total. Percentual. |
| `taxa_distorcao_em_1serie` | FLOAT | TDI EM 1a serie. Percentual. |
| `taxa_distorcao_em_2serie` | FLOAT | TDI EM 2a serie. Percentual. |
| `taxa_distorcao_em_3serie` | FLOAT | TDI EM 3a serie. Percentual. |
| `taxa_distorcao_em_4serie` | FLOAT | TDI EM 4a serie (EM integrado/profissionalizante). Percentual. |
| `data_carga_semantica` | TIMESTAMP | Timestamp UTC de geracao da tabela na semantic/ |

## semantic · obt_inep_taxa_rendimento_brasil_ano

File `semantic__obt_inep_taxa_rendimento_brasil_ano.parquet` · 342 rows · 16 columns

Taxas de rendimento escolar no nivel Brasil. Grao: 1 linha por (ano, dependencia_administrativa, localizacao). Inclui todas as combinacoes de rede (Total, Federal, Estadual, Municipal, Privada, Publica) e localizacao (Total, Urbana, Rural). Cobre aprovacao, reprovacao e abandono para EF anos iniciais, EF anos finais, EF total e EM total. Serie historica 2007-2025. Origem: trusted/inep_taxas_rendimento_escolar nivel=brasil_regioes_ufs unidade=Brasil.

**Built from:** `trusted/inep_taxas_rendimento_escolar`

| Column | Type | Description |
|---|---|---|
| `ano` | INTEGER | Ano de referencia das taxas de rendimento (2007-2025). |
| `dependencia_administrativa` | STRING | Rede de ensino: Total, Federal, Estadual, Municipal, Privada, Publica. |
| `localizacao` | STRING | Localizacao das escolas: Total, Urbana, Rural. |
| `taxa_aprovacao_ef_anos_iniciais` | FLOAT | Taxa de aprovacao no EF anos iniciais (1 ao 5 ano) no Brasil, em %. |
| `taxa_reprovacao_ef_anos_iniciais` | FLOAT | Taxa de reprovacao no EF anos iniciais no Brasil, em %. |
| `taxa_abandono_ef_anos_iniciais` | FLOAT | Taxa de abandono no EF anos iniciais no Brasil, em %. |
| `taxa_aprovacao_ef_anos_finais` | FLOAT | Taxa de aprovacao no EF anos finais (6 ao 9 ano) no Brasil, em %. |
| `taxa_reprovacao_ef_anos_finais` | FLOAT | Taxa de reprovacao no EF anos finais no Brasil, em %. |
| `taxa_abandono_ef_anos_finais` | FLOAT | Taxa de abandono no EF anos finais no Brasil, em %. |
| `taxa_aprovacao_ef_total` | FLOAT | Taxa de aprovacao no EF total (AI + AF) no Brasil, em %. |
| `taxa_reprovacao_ef_total` | FLOAT | Taxa de reprovacao no EF total no Brasil, em %. |
| `taxa_abandono_ef_total` | FLOAT | Taxa de abandono no EF total no Brasil, em %. |
| `taxa_aprovacao_em_total` | FLOAT | Taxa de aprovacao no Ensino Medio no Brasil, em %. |
| `taxa_reprovacao_em_total` | FLOAT | Taxa de reprovacao no Ensino Medio no Brasil, em %. |
| `taxa_abandono_em_total` | FLOAT | Taxa de abandono no Ensino Medio no Brasil, em %. |
| `data_carga_semantica` | TIMESTAMP | Timestamp UTC de quando este registro foi gerado na camada semantica. |

## semantic · obt_inep_taxa_rendimento_escola_ano

File `semantic__obt_inep_taxa_rendimento_escola_ano.parquet` · 2,652,720 rows · 25 columns

Taxas de rendimento escolar (aprovacao, reprovacao e abandono) por escola e ano. Grao: 1 linha por (co_entidade, ano_censo). Publicadas pelo INEP anualmente. Cobertura: EF anos iniciais, EF anos finais, EF total, Ensino Medio. Apenas escolas com ao menos 1 taxa nao nula. FK: codigo_municipio para obt_ibge_municipio. Origem: trusted/inep_taxas_rendimento_escolar. INEP 2007-2024.

**Built from:** `trusted/inep_taxas_rendimento_escolar`

| Column | Type | Description |
|---|---|---|
| `codigo_escola` | INTEGER | Codigo INEP da escola (INT64). Chave primaria composta com ano_censo. |
| `nome_escola` | STRING | Nome oficial da escola. |
| `sg_uf` | STRING | Sigla da UF da escola. |
| `sigla_uf` | STRING | Sigla do estado da escola (redundante com sg_uf). — descrição gerada por IA. |
| `regiao` | STRING | Regiao geografica: Norte, Nordeste, Centro-Oeste, Sudeste, Sul. |
| `nome_regiao` | STRING | Nome por extenso da região geográfica da escola. — descrição gerada por IA. |
| `codigo_municipio` | INTEGER | Codigo IBGE do municipio (INT64). FK para obt_ibge_municipio. |
| `municipio` | STRING | Nome do municipio da escola. |
| `nome_municipio` | STRING | Nome oficial do município (redundante com municipio). — descrição gerada por IA. |
| `ano_censo` | INTEGER | Ano de referencia das taxas. Chave primaria composta com codigo_escola. |
| `dependencia_administrativa` | STRING | Dependencia: Federal, Estadual, Municipal, Privada. |
| `localizacao` | STRING | Localizacao: Urbana ou Rural. |
| `taxa_aprovacao_ef_anos_iniciais` | FLOAT | Taxa de aprovacao EF anos iniciais (%), NULL se escola nao oferta. |
| `taxa_aprovacao_ef_anos_finais` | FLOAT | Taxa de aprovacao EF anos finais (%), NULL se escola nao oferta. |
| `taxa_aprovacao_ef_total` | FLOAT | Taxa de aprovacao EF total (%). |
| `taxa_aprovacao_em_total` | FLOAT | Taxa de aprovacao Ensino Medio (%), NULL se escola nao oferta. |
| `taxa_reprovacao_ef_anos_iniciais` | FLOAT | Taxa de reprovacao EF anos iniciais (%). |
| `taxa_reprovacao_ef_anos_finais` | FLOAT | Taxa de reprovacao EF anos finais (%). |
| `taxa_reprovacao_ef_total` | FLOAT | Taxa de reprovacao EF total (%). |
| `taxa_reprovacao_em_total` | FLOAT | Taxa de reprovacao Ensino Medio (%). |
| `taxa_abandono_ef_anos_iniciais` | FLOAT | Taxa de abandono EF anos iniciais (%). |
| `taxa_abandono_ef_anos_finais` | FLOAT | Taxa de abandono EF anos finais (%). |
| `taxa_abandono_ef_total` | FLOAT | Taxa de abandono EF total (%). |
| `taxa_abandono_em_total` | FLOAT | Taxa de abandono Ensino Medio (%). |
| `data_carga_semantica` | TIMESTAMP | Timestamp UTC de geracao na camada semantica. |

## semantic · obt_inep_taxa_rendimento_municipio_ano

File `semantic__obt_inep_taxa_rendimento_municipio_ano.parquet` · 105,799 rows · 21 columns

Taxas de rendimento escolar por municipio e ano. Grao: 1 linha por (co_municipio, ano_censo). Agrega aprovacao, reprovacao e abandono por etapa (EF AI, EF AF, EF total, EM) para rede total. FK: codigo_municipio para obt_ibge_municipio. Origem: trusted/inep_taxas_rendimento_escolar. INEP 2007-2024.

**Built from:** `trusted/inep_taxas_rendimento_escolar`

| Column | Type | Description |
|---|---|---|
| `codigo_municipio` | INTEGER | Codigo IBGE do municipio (INT64). FK para obt_ibge_municipio. Chave primaria composta com ano_censo. |
| `municipio` | STRING | Nome do municipio. |
| `nome_municipio` | STRING | Nome completo do município. — descrição gerada por IA. |
| `sg_uf` | STRING | Sigla da UF. |
| `sigla_uf` | STRING | Sigla do estado/UF. — descrição gerada por IA. |
| `regiao` | STRING | Regiao geografica: Norte, Nordeste, Centro-Oeste, Sudeste, Sul. |
| `nome_regiao` | STRING | Nome da região do país. — descrição gerada por IA. |
| `ano_censo` | INTEGER | Ano de referencia. Chave primaria composta com codigo_municipio. |
| `taxa_aprovacao_ef_anos_iniciais` | FLOAT | Taxa media de aprovacao EF anos iniciais (%). |
| `taxa_aprovacao_ef_anos_finais` | FLOAT | Taxa media de aprovacao EF anos finais (%). |
| `taxa_aprovacao_ef_total` | FLOAT | Taxa media de aprovacao EF total (%). |
| `taxa_aprovacao_em_total` | FLOAT | Taxa media de aprovacao Ensino Medio (%). |
| `taxa_reprovacao_ef_anos_iniciais` | FLOAT | Taxa media de reprovacao EF anos iniciais (%). |
| `taxa_reprovacao_ef_anos_finais` | FLOAT | Taxa media de reprovacao EF anos finais (%). |
| `taxa_reprovacao_ef_total` | FLOAT | Taxa media de reprovacao EF total (%). |
| `taxa_reprovacao_em_total` | FLOAT | Taxa media de reprovacao Ensino Medio (%). |
| `taxa_abandono_ef_anos_iniciais` | FLOAT | Taxa media de abandono EF anos iniciais (%). |
| `taxa_abandono_ef_anos_finais` | FLOAT | Taxa media de abandono EF anos finais (%). |
| `taxa_abandono_ef_total` | FLOAT | Taxa media de abandono EF total (%). |
| `taxa_abandono_em_total` | FLOAT | Taxa media de abandono Ensino Medio (%). |
| `data_carga_semantica` | TIMESTAMP | Timestamp UTC de geracao na camada semantica. |

## semantic · obt_inep_taxa_rendimento_regiao_ano

File `semantic__obt_inep_taxa_rendimento_regiao_ano.parquet` · 1,710 rows · 18 columns

Taxas de rendimento escolar por regiao geografica e ano. Grao: 1 linha por (regiao, ano, dependencia_administrativa, localizacao). Regioes: Norte, Nordeste, Sudeste, Sul, Centro-Oeste. Inclui todas as combinacoes de rede (Total, Federal, Estadual, Municipal, Privada, Publica) e localizacao (Total, Urbana, Rural). Cobre aprovacao, reprovacao e abandono para EF anos iniciais, EF anos finais, EF total e EM total. Serie historica 2007-2025. Origem: trusted/inep_taxas_rendimento_escolar nivel=brasil_regioes_ufs.

**Built from:** `trusted/inep_taxas_rendimento_escolar`

| Column | Type | Description |
|---|---|---|
| `regiao` | STRING | Regiao geografica: Norte, Nordeste, Sudeste, Sul, Centro-Oeste. |
| `nome_regiao` | STRING | Nome por extenso da região geográfica do Brasil (ex: Centro-Oeste). — descrição gerada por IA. |
| `ano` | INTEGER | Ano de referencia das taxas de rendimento (2007-2025). |
| `dependencia_administrativa` | STRING | Rede de ensino: Total, Federal, Estadual, Municipal, Privada, Publica. |
| `localizacao` | STRING | Localizacao das escolas: Total, Urbana, Rural. |
| `taxa_aprovacao_ef_anos_iniciais` | FLOAT | Taxa de aprovacao no EF anos iniciais (1 ao 5 ano) na regiao, em %. |
| `taxa_reprovacao_ef_anos_iniciais` | FLOAT | Taxa de reprovacao no EF anos iniciais na regiao, em %. |
| `taxa_abandono_ef_anos_iniciais` | FLOAT | Taxa de abandono no EF anos iniciais na regiao, em %. |
| `taxa_aprovacao_ef_anos_finais` | FLOAT | Taxa de aprovacao no EF anos finais (6 ao 9 ano) na regiao, em %. |
| `taxa_reprovacao_ef_anos_finais` | FLOAT | Taxa de reprovacao no EF anos finais na regiao, em %. |
| `taxa_abandono_ef_anos_finais` | FLOAT | Taxa de abandono no EF anos finais na regiao, em %. |
| `taxa_aprovacao_ef_total` | FLOAT | Taxa de aprovacao no EF total (AI + AF) na regiao, em %. |
| `taxa_reprovacao_ef_total` | FLOAT | Taxa de reprovacao no EF total na regiao, em %. |
| `taxa_abandono_ef_total` | FLOAT | Taxa de abandono no EF total na regiao, em %. |
| `taxa_aprovacao_em_total` | FLOAT | Taxa de aprovacao no Ensino Medio na regiao, em %. |
| `taxa_reprovacao_em_total` | FLOAT | Taxa de reprovacao no Ensino Medio na regiao, em %. |
| `taxa_abandono_em_total` | FLOAT | Taxa de abandono no Ensino Medio na regiao, em %. |
| `data_carga_semantica` | TIMESTAMP | Timestamp UTC de quando este registro foi gerado na camada semantica. |

## semantic · obt_inep_taxa_rendimento_uf_ano

File `semantic__obt_inep_taxa_rendimento_uf_ano.parquet` · 9,042 rows · 19 columns

Taxas de rendimento escolar por UF e ano. Grao: 1 linha por (sg_uf, ano, dependencia_administrativa, localizacao). 27 UFs. Inclui todas as combinacoes de rede (Total, Federal, Estadual, Municipal, Privada, Publica) e localizacao (Total, Urbana, Rural). Cobre aprovacao, reprovacao e abandono para EF anos iniciais, EF anos finais, EF total e EM total. Serie historica completa 2007-2025. Origem: trusted/inep_taxas_rendimento_escolar nivel_agregacao=brasil_regioes_ufs.

**Built from:** `trusted/inep_taxas_rendimento_escolar`

| Column | Type | Description |
|---|---|---|
| `sg_uf` | STRING | Sigla da UF (2 letras), normalizada a partir de sigla ou nome completo conforme o ano de origem. |
| `sigla_uf` | STRING | Sigla de duas letras da Unidade Federativa (UF), utilizada para padronização de chaves. — descrição gerada por IA. |
| `uf_nome_origem` | STRING | Valor original de unidade_geografica na trusted (ja normalizado para sigla de 2 letras pela raw). |
| `ano` | INTEGER | Ano de referencia das taxas de rendimento. |
| `dependencia_administrativa` | STRING | Rede de ensino: Total, Federal, Estadual, Municipal, Privada, Publica. |
| `localizacao` | STRING | Localizacao das escolas: Total, Urbana, Rural. |
| `taxa_aprovacao_ef_anos_iniciais` | FLOAT | Taxa de aprovacao no EF anos iniciais (1 ao 5 ano) na UF, em %. |
| `taxa_reprovacao_ef_anos_iniciais` | FLOAT | Taxa de reprovacao no EF anos iniciais na UF, em %. |
| `taxa_abandono_ef_anos_iniciais` | FLOAT | Taxa de abandono no EF anos iniciais na UF, em %. |
| `taxa_aprovacao_ef_anos_finais` | FLOAT | Taxa de aprovacao no EF anos finais (6 ao 9 ano) na UF, em %. |
| `taxa_reprovacao_ef_anos_finais` | FLOAT | Taxa de reprovacao no EF anos finais na UF, em %. |
| `taxa_abandono_ef_anos_finais` | FLOAT | Taxa de abandono no EF anos finais na UF, em %. |
| `taxa_aprovacao_ef_total` | FLOAT | Taxa de aprovacao no EF total (AI + AF) na UF, em %. |
| `taxa_reprovacao_ef_total` | FLOAT | Taxa de reprovacao no EF total na UF, em %. |
| `taxa_abandono_ef_total` | FLOAT | Taxa de abandono no EF total na UF, em %. |
| `taxa_aprovacao_em_total` | FLOAT | Taxa de aprovacao no Ensino Medio na UF, em %. |
| `taxa_reprovacao_em_total` | FLOAT | Taxa de reprovacao no Ensino Medio na UF, em %. |
| `taxa_abandono_em_total` | FLOAT | Taxa de abandono no Ensino Medio na UF, em %. |
| `data_carga_semantica` | TIMESTAMP | Timestamp UTC de quando este registro foi gerado na camada semantica. |
