# IDEB (INEP): Raw and Trusted

Dataset: [lucasrangelss/ideb-raw-trusted](https://www.kaggle.com/datasets/lucasrangelss/ideb-raw-trusted) · snapshot 2026-09-30 · 16 tables · 1,925,765 rows

**Source:** Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP), [https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/ideb](https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/ideb)

Observed IDEB against targets by school, municipality, state, region and Brazil, every two years. IDEB is the SAEB proficiency score times the flow indicator.

**Grain and keys:** School, municipality, state, region or Brazil by edition.

**Layers.** `raw` is the source snapshot as delivered. `trusted` is typed, deduplicated and named consistently. `semantic` joins and reshapes trusted tables for analysis. Every table is a Parquet file named `<layer>__<table>.parquet` at the root of the dataset.

The full interactive map (lineage, joins, search) is at [https://rangeltech.net/datamap/](https://rangeltech.net/datamap/). Column descriptions come from the source lake's catalogue and are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns | Described | Upstream |
|---|---|---:|---:|---:|---|
| raw | [`inep_ideb_brasil_anos_finais`](#raw-inep-ideb-brasil-anos-finais) | 15 | 122 | 122 | source |
| raw | [`inep_ideb_brasil_anos_iniciais`](#raw-inep-ideb-brasil-anos-iniciais) | 16 | 133 | 133 | source |
| raw | [`inep_ideb_brasil_ensino_medio`](#raw-inep-ideb-brasil-ensino-medio) | 14 | 122 | 122 | source |
| raw | [`inep_ideb_escola_anos_finais`](#raw-inep-ideb-escola-anos-finais) | 48,020 | 126 | 126 | source |
| raw | [`inep_ideb_escola_anos_iniciais`](#raw-inep-ideb-escola-anos-iniciais) | 66,153 | 137 | 137 | source |
| raw | [`inep_ideb_escola_ensino_medio`](#raw-inep-ideb-escola-ensino-medio) | 22,184 | 60 | 60 | source |
| raw | [`inep_ideb_municipio_anos_finais`](#raw-inep-ideb-municipio-anos-finais) | 14,428 | 124 | 124 | source |
| raw | [`inep_ideb_municipio_anos_iniciais`](#raw-inep-ideb-municipio-anos-iniciais) | 14,533 | 135 | 135 | source |
| raw | [`inep_ideb_municipio_ensino_medio`](#raw-inep-ideb-municipio-ensino-medio) | 11,765 | 58 | 58 | source |
| raw | [`inep_ideb_regioes_ufs_anos_finais`](#raw-inep-ideb-regioes-ufs-anos-finais) | 141 | 122 | 122 | source |
| raw | [`inep_ideb_regioes_ufs_anos_iniciais`](#raw-inep-ideb-regioes-ufs-anos-iniciais) | 142 | 133 | 133 | source |
| raw | [`inep_ideb_regioes_ufs_ensino_medio`](#raw-inep-ideb-regioes-ufs-ensino-medio) | 109 | 122 | 122 | source |
| trusted | [`inep_ideb_brasil`](#trusted-inep-ideb-brasil) | 154 | 13 | 13 | `inep_ideb_brasil_anos_finais`, `inep_ideb_brasil_anos_iniciais`, `inep_ideb_brasil_ensino_medio` |
| trusted | [`inep_ideb_escola`](#trusted-inep-ideb-escola) | 1,366,823 | 21 | 21 | `inep_ideb_escola_anos_finais`, `inep_ideb_escola_anos_iniciais`, `inep_ideb_escola_ensino_medio` |
| trusted | [`inep_ideb_municipio`](#trusted-inep-ideb-municipio) | 377,396 | 19 | 19 | `inep_ideb_municipio_anos_finais`, `inep_ideb_municipio_anos_iniciais`, `inep_ideb_municipio_ensino_medio` |
| trusted | [`inep_ideb_regioes_ufs`](#trusted-inep-ideb-regioes-ufs) | 3,872 | 15 | 15 | `inep_ideb_regioes_ufs_anos_finais`, `inep_ideb_regioes_ufs_anos_iniciais`, `inep_ideb_regioes_ufs_ensino_medio` |

## raw · inep_ideb_brasil_anos_finais

File `raw__inep_ideb_brasil_anos_finais.parquet` · 15 rows · 122 columns

Tabela histórica com indicadores do IDEB (Índice de Desenvolvimento da Educação Básica) agregados por nível de ensino e rede escolar, contendo taxas de aprovação, notas do SAEB (Matemática e Português), indicador de rendimento, valores observados e metas projetadas de 2005 a 2023.

**Feeds:** `trusted/inep_ideb_brasil`

| Column | Type | Description |
|---|---|---|
| `BRASIL` | STRING | Nome da região geográfica ou país de referência (ex: 'Brasil'). |
| `rede` | STRING | Tipo de rede de ensino analisada (ex: 'Total', 'Estadual', 'Municipal', 'Privada'). |
| `VL_APROVACAO_2005_SI_4` | STRING | Taxa de aprovação média do segmento de ensino no ano de 2005 (em %). |
| `VL_APROVACAO_2005_1` | STRING | Taxa de aprovação escolar no 1º ano do segmento no ano de 2005 (em %). |
| `VL_APROVACAO_2005_2` | STRING | Taxa de aprovação escolar no 2º ano do segmento no ano de 2005 (em %). |
| `VL_APROVACAO_2005_3` | STRING | Taxa de aprovação escolar no 3º ano do segmento no ano de 2005 (em %). |
| `VL_APROVACAO_2005_4` | STRING | Taxa de aprovação escolar no 4º ano do segmento no ano de 2005 (em %). |
| `VL_INDICADOR_REND_2005` | STRING | Indicador de rendimento escolar (taxa média de aprovação) para o cálculo do IDEB no ano de 2005. |
| `VL_APROVACAO_2007_SI_4` | STRING | Taxa de aprovação média do segmento de ensino no ano de 2007 (em %). |
| `VL_APROVACAO_2007_1` | STRING | Taxa de aprovação escolar no 1º ano do segmento no ano de 2007 (em %). |
| `VL_APROVACAO_2007_2` | STRING | Taxa de aprovação escolar no 2º ano do segmento no ano de 2007 (em %). |
| `VL_APROVACAO_2007_3` | STRING | Taxa de aprovação escolar no 3º ano do segmento no ano de 2007 (em %). |
| `VL_APROVACAO_2007_4` | STRING | Taxa de aprovação escolar no 4º ano do segmento no ano de 2007 (em %). |
| `VL_INDICADOR_REND_2007` | STRING | Indicador de rendimento escolar (taxa média de aprovação) para o cálculo do IDEB no ano de 2007. |
| `VL_APROVACAO_2009_SI_4` | STRING | Taxa de aprovação média do segmento de ensino no ano de 2009 (em %). |
| `VL_APROVACAO_2009_1` | STRING | Taxa de aprovação escolar no 1º ano do segmento no ano de 2009 (em %). |
| `VL_APROVACAO_2009_2` | STRING | Taxa de aprovação escolar no 2º ano do segmento no ano de 2009 (em %). |
| `VL_APROVACAO_2009_3` | STRING | Taxa de aprovação escolar no 3º ano do segmento no ano de 2009 (em %). |
| `VL_APROVACAO_2009_4` | STRING | Taxa de aprovação escolar no 4º ano do segmento no ano de 2009 (em %). |
| `VL_INDICADOR_REND_2009` | STRING | Indicador de rendimento escolar (taxa média de aprovação) para o cálculo do IDEB no ano de 2009. |
| `VL_APROVACAO_2011_SI_4` | STRING | Taxa de aprovação média do segmento de ensino no ano de 2011 (em %). |
| `VL_APROVACAO_2011_1` | STRING | Taxa de aprovação escolar no 1º ano do segmento no ano de 2011 (em %). |
| `VL_APROVACAO_2011_2` | STRING | Taxa de aprovação escolar no 2º ano do segmento no ano de 2011 (em %). |
| `VL_APROVACAO_2011_3` | STRING | Taxa de aprovação escolar no 3º ano do segmento no ano de 2011 (em %). |
| `VL_APROVACAO_2011_4` | STRING | Taxa de aprovação escolar no 4º ano do segmento no ano de 2011 (em %). |
| `VL_INDICADOR_REND_2011` | STRING | Indicador de rendimento escolar (taxa média de aprovação) para o cálculo do IDEB no ano de 2011. |
| `VL_APROVACAO_2013_SI_4` | STRING | Taxa de aprovação média do segmento de ensino no ano de 2013 (em %). |
| `VL_APROVACAO_2013_1` | STRING | Taxa de aprovação escolar no 1º ano do segmento no ano de 2013 (em %). |
| `VL_APROVACAO_2013_2` | STRING | Taxa de aprovação escolar no 2º ano do segmento no ano de 2013 (em %). |
| `VL_APROVACAO_2013_3` | STRING | Taxa de aprovação escolar no 3º ano do segmento no ano de 2013 (em %). |
| `VL_APROVACAO_2013_4` | STRING | Taxa de aprovação escolar no 4º ano do segmento no ano de 2013 (em %). |
| `VL_INDICADOR_REND_2013` | STRING | Indicador de rendimento escolar (taxa média de aprovação) para o cálculo do IDEB no ano de 2013. |
| `VL_APROVACAO_2015_SI_4` | STRING | Taxa de aprovação média do segmento de ensino no ano de 2015 (em %). |
| `VL_APROVACAO_2015_1` | STRING | Taxa de aprovação escolar no 1º ano do segmento no ano de 2015 (em %). |
| `VL_APROVACAO_2015_2` | STRING | Taxa de aprovação escolar no 2º ano do segmento no ano de 2015 (em %). |
| `VL_APROVACAO_2015_3` | STRING | Taxa de aprovação escolar no 3º ano do segmento no ano de 2015 (em %). |
| `VL_APROVACAO_2015_4` | STRING | Taxa de aprovação escolar no 4º ano do segmento no ano de 2015 (em %). |
| `VL_INDICADOR_REND_2015` | STRING | Indicador de rendimento escolar (taxa média de aprovação) para o cálculo do IDEB no ano de 2015. |
| `VL_APROVACAO_2017_SI_4` | STRING | Taxa de aprovação média do segmento de ensino no ano de 2017 (em %). |
| `VL_APROVACAO_2017_1` | STRING | Taxa de aprovação escolar no 1º ano do segmento no ano de 2017 (em %). |
| `VL_APROVACAO_2017_2` | STRING | Taxa de aprovação escolar no 2º ano do segmento no ano de 2017 (em %). |
| `VL_APROVACAO_2017_3` | STRING | Taxa de aprovação escolar no 3º ano do segmento no ano de 2017 (em %). |
| `VL_APROVACAO_2017_4` | STRING | Taxa de aprovação escolar no 4º ano do segmento no ano de 2017 (em %). |
| `VL_INDICADOR_REND_2017` | STRING | Indicador de rendimento escolar (taxa média de aprovação) para o cálculo do IDEB no ano de 2017. |
| `VL_APROVACAO_2019_SI_4` | STRING | Taxa de aprovação média do segmento de ensino no ano de 2019 (em %). |
| `VL_APROVACAO_2019_1` | STRING | Taxa de aprovação escolar no 1º ano do segmento no ano de 2019 (em %). |
| `VL_APROVACAO_2019_2` | STRING | Taxa de aprovação escolar no 2º ano do segmento no ano de 2019 (em %). |
| `VL_APROVACAO_2019_3` | STRING | Taxa de aprovação escolar no 3º ano do segmento no ano de 2019 (em %). |
| `VL_APROVACAO_2019_4` | STRING | Taxa de aprovação escolar no 4º ano do segmento no ano de 2019 (em %). |
| `VL_INDICADOR_REND_2019` | STRING | Indicador de rendimento escolar (taxa média de aprovação) para o cálculo do IDEB no ano de 2019. |
| `VL_APROVACAO_2021_SI_4` | STRING | Taxa de aprovação média do segmento de ensino no ano de 2021 (em %). |
| `VL_APROVACAO_2021_1` | STRING | Taxa de aprovação escolar no 1º ano do segmento no ano de 2021 (em %). |
| `VL_APROVACAO_2021_2` | STRING | Taxa de aprovação escolar no 2º ano do segmento no ano de 2021 (em %). |
| `VL_APROVACAO_2021_3` | STRING | Taxa de aprovação escolar no 3º ano do segmento no ano de 2021 (em %). |
| `VL_APROVACAO_2021_4` | STRING | Taxa de aprovação escolar no 4º ano do segmento no ano de 2021 (em %). |
| `VL_INDICADOR_REND_2021` | STRING | Indicador de rendimento escolar (taxa média de aprovação) para o cálculo do IDEB no ano de 2021. |
| `VL_APROVACAO_2023_SI_4` | STRING | Taxa de aprovação média do segmento de ensino no ano de 2023 (em %). |
| `VL_APROVACAO_2023_1` | STRING | Taxa de aprovação escolar no 1º ano do segmento no ano de 2023 (em %). |
| `VL_APROVACAO_2023_2` | STRING | Taxa de aprovação escolar no 2º ano do segmento no ano de 2023 (em %). |
| `VL_APROVACAO_2023_3` | STRING | Taxa de aprovação escolar no 3º ano do segmento no ano de 2023 (em %). |
| `VL_APROVACAO_2023_4` | STRING | Taxa de aprovação escolar no 4º ano do segmento no ano de 2023 (em %). |
| `VL_INDICADOR_REND_2023` | STRING | Indicador de rendimento escolar (taxa média de aprovação) para o cálculo do IDEB no ano de 2023. |
| `VL_APROVACAO_2025_SI_4` | STRING | Taxa média de aprovação do bloco de anos escolares em 2025 (%). — descrição gerada por IA. |
| `VL_APROVACAO_2025_1` | STRING | Taxa de aprovação na 1ª série/ano da etapa escolar em 2025 (%). — descrição gerada por IA. |
| `VL_APROVACAO_2025_2` | STRING | Taxa de aprovação na 2ª série/ano da etapa escolar em 2025 (%). — descrição gerada por IA. |
| `VL_APROVACAO_2025_3` | STRING | Taxa de aprovação na 3ª série/ano da etapa escolar em 2025 (%). — descrição gerada por IA. |
| `VL_APROVACAO_2025_4` | STRING | Taxa de aprovação na 4ª série/ano da etapa escolar em 2025 (%). — descrição gerada por IA. |
| `VL_INDICADOR_REND_2025` | STRING | Indicador de rendimento escolar (P) do IDEB em 2025 (variação de 0 a 1). — descrição gerada por IA. |
| `VL_NOTA_MATEMATICA_2005` | STRING | Nota média de proficiência em Matemática obtida no SAEB no ano de 2005. |
| `VL_NOTA_PORTUGUES_2005` | STRING | Nota média de proficiência em Língua Portuguesa obtida no SAEB no ano de 2005. |
| `VL_NOTA_MEDIA_2005` | STRING | Nota média padronizada (indicador de aprendizado) para o cálculo do IDEB no ano de 2005. |
| `VL_NOTA_MATEMATICA_2007` | STRING | Nota média de proficiência em Matemática obtida no SAEB no ano de 2007. |
| `VL_NOTA_PORTUGUES_2007` | STRING | Nota média de proficiência em Língua Portuguesa obtida no SAEB no ano de 2007. |
| `VL_NOTA_MEDIA_2007` | STRING | Nota média padronizada (indicador de aprendizado) para o cálculo do IDEB no ano de 2007. |
| `VL_NOTA_MATEMATICA_2009` | STRING | Nota média de proficiência em Matemática obtida no SAEB no ano de 2009. |
| `VL_NOTA_PORTUGUES_2009` | STRING | Nota média de proficiência em Língua Portuguesa obtida no SAEB no ano de 2009. |
| `VL_NOTA_MEDIA_2009` | STRING | Nota média padronizada (indicador de aprendizado) para o cálculo do IDEB no ano de 2009. |
| `VL_NOTA_MATEMATICA_2011` | STRING | Nota média de proficiência em Matemática obtida no SAEB no ano de 2011. |
| `VL_NOTA_PORTUGUES_2011` | STRING | Nota média de proficiência em Língua Portuguesa obtida no SAEB no ano de 2011. |
| `VL_NOTA_MEDIA_2011` | STRING | Nota média padronizada (indicador de aprendizado) para o cálculo do IDEB no ano de 2011. |
| `VL_NOTA_MATEMATICA_2013` | STRING | Nota média de proficiência em Matemática obtida no SAEB no ano de 2013. |
| `VL_NOTA_PORTUGUES_2013` | STRING | Nota média de proficiência em Língua Portuguesa obtida no SAEB no ano de 2013. |
| `VL_NOTA_MEDIA_2013` | STRING | Nota média padronizada (indicador de aprendizado) para o cálculo do IDEB no ano de 2013. |
| `VL_NOTA_MATEMATICA_2015` | STRING | Nota média de proficiência em Matemática obtida no SAEB no ano de 2015. |
| `VL_NOTA_PORTUGUES_2015` | STRING | Nota média de proficiência em Língua Portuguesa obtida no SAEB no ano de 2015. |
| `VL_NOTA_MEDIA_2015` | STRING | Nota média padronizada (indicador de aprendizado) para o cálculo do IDEB no ano de 2015. |
| `VL_NOTA_MATEMATICA_2017` | STRING | Nota média de proficiência em Matemática obtida no SAEB no ano de 2017. |
| `VL_NOTA_PORTUGUES_2017` | STRING | Nota média de proficiência em Língua Portuguesa obtida no SAEB no ano de 2017. |
| `VL_NOTA_MEDIA_2017` | STRING | Nota média padronizada (indicador de aprendizado) para o cálculo do IDEB no ano de 2017. |
| `VL_NOTA_MATEMATICA_2019` | STRING | Nota média de proficiência em Matemática obtida no SAEB no ano de 2019. |
| `VL_NOTA_PORTUGUES_2019` | STRING | Nota média de proficiência em Língua Portuguesa obtida no SAEB no ano de 2019. |
| `VL_NOTA_MEDIA_2019` | STRING | Nota média padronizada (indicador de aprendizado) para o cálculo do IDEB no ano de 2019. |
| `VL_NOTA_MATEMATICA_2021` | STRING | Nota média de proficiência em Matemática obtida no SAEB no ano de 2021. |
| `VL_NOTA_PORTUGUES_2021` | STRING | Nota média de proficiência em Língua Portuguesa obtida no SAEB no ano de 2021. |
| `VL_NOTA_MEDIA_2021` | STRING | Nota média padronizada (indicador de aprendizado) para o cálculo do IDEB no ano de 2021. |
| `VL_NOTA_MATEMATICA_2023` | STRING | Nota média de proficiência em Matemática obtida no SAEB no ano de 2023. |
| `VL_NOTA_PORTUGUES_2023` | STRING | Nota média de proficiência em Língua Portuguesa obtida no SAEB no ano de 2023. |
| `VL_NOTA_MEDIA_2023` | STRING | Nota média padronizada (indicador de aprendizado) para o cálculo do IDEB no ano de 2023. |
| `VL_NOTA_MATEMATICA_2025` | STRING | Nota média em Matemática na avaliação do SAEB no ano de 2025. — descrição gerada por IA. |
| `VL_NOTA_PORTUGUES_2025` | STRING | Nota média em Língua Portuguesa na avaliação do SAEB no ano de 2025. — descrição gerada por IA. |
| `VL_NOTA_MEDIA_2025` | STRING | Nota média padronizada do SAEB (N) em 2025 (escala de 0 a 10). — descrição gerada por IA. |
| `VL_OBSERVADO_2005` | STRING | Valor observado do IDEB no ano de 2005. |
| `VL_OBSERVADO_2007` | STRING | Valor observado do IDEB no ano de 2007. |
| `VL_OBSERVADO_2009` | STRING | Valor observado do IDEB no ano de 2009. |
| `VL_OBSERVADO_2011` | STRING | Valor observado do IDEB no ano de 2011. |
| `VL_OBSERVADO_2013` | STRING | Valor observado do IDEB no ano de 2013. |
| `VL_OBSERVADO_2015` | STRING | Valor observado do IDEB no ano de 2015. |
| `VL_OBSERVADO_2017` | STRING | Valor observado do IDEB no ano de 2017. |
| `VL_OBSERVADO_2019` | STRING | Valor observado do IDEB no ano de 2019. |
| `VL_OBSERVADO_2021` | STRING | Valor observado do IDEB no ano de 2021. |
| `VL_OBSERVADO_2023` | STRING | Valor observado do IDEB no ano de 2023. |
| `VL_OBSERVADO_2025` | STRING | Índice IDEB observado e calculado para o ano de 2025. — descrição gerada por IA. |
| `VL_PROJECAO_2007` | STRING | Meta projetada do IDEB para o ano de 2007. |
| `VL_PROJECAO_2009` | STRING | Meta projetada do IDEB para o ano de 2009. |
| `VL_PROJECAO_2011` | STRING | Meta projetada do IDEB para o ano de 2011. |
| `VL_PROJECAO_2013` | STRING | Meta projetada do IDEB para o ano de 2013. |
| `VL_PROJECAO_2015` | STRING | Meta projetada do IDEB para o ano de 2015. |
| `VL_PROJECAO_2017` | STRING | Meta projetada do IDEB para o ano de 2017. |
| `VL_PROJECAO_2019` | STRING | Meta projetada do IDEB para o ano de 2019. |
| `VL_PROJECAO_2021` | STRING | Meta projetada do IDEB para o ano de 2021. |
| `nivel` | STRING | Nível ou segmento da educação básica analisado (ex: 'anos_finais', 'anos_iniciais'). |
| `dt_ingestao_lake` | STRING | Data e hora do processamento/ingestão do registro no Data Lake (formato ISO 8601). — descrição gerada por IA. |

## raw · inep_ideb_brasil_anos_iniciais

File `raw__inep_ideb_brasil_anos_iniciais.parquet` · 16 rows · 133 columns

Tabela histórica consolidada do IDEB (Índice de Desenvolvimento da Educação Básica) e SAEB, contendo taxas de aprovação escolar, notas padronizadas de proficiência (Matemática e Português), indicadores de rendimento, valores observados e metas projetadas de 2005 a 2023.

**Feeds:** `trusted/inep_ideb_brasil`

| Column | Type | Description |
|---|---|---|
| `BRASIL` | STRING | Indica a abrangência geográfica nacional do registro (ex: 'Brasil'). |
| `rede` | STRING | Rede de ensino avaliada (ex: estadual, municipal, privada, pública). |
| `VL_APROVACAO_2005_SI_4` | STRING | Taxa de aprovação média das séries iniciais (1º ao 4º ano) em 2005 (%). |
| `VL_APROVACAO_2005_SI` | STRING | Taxa de aprovação para turmas sem informação de série em 2005 (%). |
| `VL_APROVACAO_2005_1` | STRING | Taxa de aprovação no 1º ano do Ensino Fundamental em 2005 (%). |
| `VL_APROVACAO_2005_2` | STRING | Taxa de aprovação no 2º ano do Ensino Fundamental em 2005 (%). |
| `VL_APROVACAO_2005_3` | STRING | Taxa de aprovação no 3º ano do Ensino Fundamental em 2005 (%). |
| `VL_APROVACAO_2005_4` | STRING | Taxa de aprovação no 4º ano do Ensino Fundamental em 2005 (%). |
| `VL_INDICADOR_REND_2005` | STRING | Indicador de rendimento escolar (fluxo) para o cálculo do IDEB em 2005. |
| `VL_APROVACAO_2007_SI_4` | STRING | Taxa de aprovação média das séries iniciais (1º ao 4º ano) em 2007 (%). |
| `VL_APROVACAO_2007_SI` | STRING | Taxa de aprovação para turmas sem informação de série em 2007 (%). |
| `VL_APROVACAO_2007_1` | STRING | Taxa de aprovação no 1º ano do Ensino Fundamental em 2007 (%). |
| `VL_APROVACAO_2007_2` | STRING | Taxa de aprovação no 2º ano do Ensino Fundamental em 2007 (%). |
| `VL_APROVACAO_2007_3` | STRING | Taxa de aprovação no 3º ano do Ensino Fundamental em 2007 (%). |
| `VL_APROVACAO_2007_4` | STRING | Taxa de aprovação no 4º ano do Ensino Fundamental em 2007 (%). |
| `VL_INDICADOR_REND_2007` | STRING | Indicador de rendimento escolar (fluxo) para o cálculo do IDEB em 2007. |
| `VL_APROVACAO_2009_SI_4` | STRING | Taxa de aprovação média das séries iniciais (1º ao 4º ano) em 2009 (%). |
| `VL_APROVACAO_2009_SI` | STRING | Taxa de aprovação para turmas sem informação de série em 2009 (%). |
| `VL_APROVACAO_2009_1` | STRING | Taxa de aprovação no 1º ano do Ensino Fundamental em 2009 (%). |
| `VL_APROVACAO_2009_2` | STRING | Taxa de aprovação no 2º ano do Ensino Fundamental em 2009 (%). |
| `VL_APROVACAO_2009_3` | STRING | Taxa de aprovação no 3º ano do Ensino Fundamental em 2009 (%). |
| `VL_APROVACAO_2009_4` | STRING | Taxa de aprovação no 4º ano do Ensino Fundamental em 2009 (%). |
| `VL_INDICADOR_REND_2009` | STRING | Indicador de rendimento escolar (fluxo) para o cálculo do IDEB em 2009. |
| `VL_APROVACAO_2011_SI_4` | STRING | Taxa de aprovação média das séries iniciais (1º ao 4º ano) em 2011 (%). |
| `VL_APROVACAO_2011_SI` | STRING | Taxa de aprovação para turmas sem informação de série em 2011 (%). |
| `VL_APROVACAO_2011_1` | STRING | Taxa de aprovação no 1º ano do Ensino Fundamental em 2011 (%). |
| `VL_APROVACAO_2011_2` | STRING | Taxa de aprovação no 2º ano do Ensino Fundamental em 2011 (%). |
| `VL_APROVACAO_2011_3` | STRING | Taxa de aprovação no 3º ano do Ensino Fundamental em 2011 (%). |
| `VL_APROVACAO_2011_4` | STRING | Taxa de aprovação no 4º ano do Ensino Fundamental em 2011 (%). |
| `VL_INDICADOR_REND_2011` | STRING | Indicador de rendimento escolar (fluxo) para o cálculo do IDEB em 2011. |
| `VL_APROVACAO_2013_SI_4` | STRING | Taxa de aprovação média das séries iniciais (1º ao 4º ano) em 2013 (%). |
| `VL_APROVACAO_2013_SI` | STRING | Taxa de aprovação para turmas sem informação de série em 2013 (%). |
| `VL_APROVACAO_2013_1` | STRING | Taxa de aprovação no 1º ano do Ensino Fundamental em 2013 (%). |
| `VL_APROVACAO_2013_2` | STRING | Taxa de aprovação no 2º ano do Ensino Fundamental em 2013 (%). |
| `VL_APROVACAO_2013_3` | STRING | Taxa de aprovação no 3º ano do Ensino Fundamental em 2013 (%). |
| `VL_APROVACAO_2013_4` | STRING | Taxa de aprovação no 4º ano do Ensino Fundamental em 2013 (%). |
| `VL_INDICADOR_REND_2013` | STRING | Indicador de rendimento escolar (fluxo) para o cálculo do IDEB em 2013. |
| `VL_APROVACAO_2015_SI_4` | STRING | Taxa de aprovação média das séries iniciais (1º ao 4º ano) em 2015 (%). |
| `VL_APROVACAO_2015_SI` | STRING | Taxa de aprovação para turmas sem informação de série em 2015 (%). |
| `VL_APROVACAO_2015_1` | STRING | Taxa de aprovação no 1º ano do Ensino Fundamental em 2015 (%). |
| `VL_APROVACAO_2015_2` | STRING | Taxa de aprovação no 2º ano do Ensino Fundamental em 2015 (%). |
| `VL_APROVACAO_2015_3` | STRING | Taxa de aprovação no 3º ano do Ensino Fundamental em 2015 (%). |
| `VL_APROVACAO_2015_4` | STRING | Taxa de aprovação no 4º ano do Ensino Fundamental em 2015 (%). |
| `VL_INDICADOR_REND_2015` | STRING | Indicador de rendimento escolar (fluxo) para o cálculo do IDEB em 2015. |
| `VL_APROVACAO_2017_SI_4` | STRING | Taxa de aprovação média das séries iniciais (1º ao 4º ano) em 2017 (%). |
| `VL_APROVACAO_2017_SI` | STRING | Taxa de aprovação para turmas sem informação de série em 2017 (%). |
| `VL_APROVACAO_2017_1` | STRING | Taxa de aprovação no 1º ano do Ensino Fundamental em 2017 (%). |
| `VL_APROVACAO_2017_2` | STRING | Taxa de aprovação no 2º ano do Ensino Fundamental em 2017 (%). |
| `VL_APROVACAO_2017_3` | STRING | Taxa de aprovação no 3º ano do Ensino Fundamental em 2017 (%). |
| `VL_APROVACAO_2017_4` | STRING | Taxa de aprovação no 4º ano do Ensino Fundamental em 2017 (%). |
| `VL_INDICADOR_REND_2017` | STRING | Indicador de rendimento escolar (fluxo) para o cálculo do IDEB em 2017. |
| `VL_APROVACAO_2019_SI_4` | STRING | Taxa de aprovação média das séries iniciais (1º ao 4º ano) em 2019 (%). |
| `VL_APROVACAO_2019_SI` | STRING | Taxa de aprovação para turmas sem informação de série em 2019 (%). |
| `VL_APROVACAO_2019_1` | STRING | Taxa de aprovação no 1º ano do Ensino Fundamental em 2019 (%). |
| `VL_APROVACAO_2019_2` | STRING | Taxa de aprovação no 2º ano do Ensino Fundamental em 2019 (%). |
| `VL_APROVACAO_2019_3` | STRING | Taxa de aprovação no 3º ano do Ensino Fundamental em 2019 (%). |
| `VL_APROVACAO_2019_4` | STRING | Taxa de aprovação no 4º ano do Ensino Fundamental em 2019 (%). |
| `VL_INDICADOR_REND_2019` | STRING | Indicador de rendimento escolar (fluxo) para o cálculo do IDEB em 2019. |
| `VL_APROVACAO_2021_SI_4` | STRING | Taxa de aprovação média das séries iniciais (1º ao 4º ano) em 2021 (%). |
| `VL_APROVACAO_2021_SI` | STRING | Taxa de aprovação para turmas sem informação de série em 2021 (%). |
| `VL_APROVACAO_2021_1` | STRING | Taxa de aprovação no 1º ano do Ensino Fundamental em 2021 (%). |
| `VL_APROVACAO_2021_2` | STRING | Taxa de aprovação no 2º ano do Ensino Fundamental em 2021 (%). |
| `VL_APROVACAO_2021_3` | STRING | Taxa de aprovação no 3º ano do Ensino Fundamental em 2021 (%). |
| `VL_APROVACAO_2021_4` | STRING | Taxa de aprovação no 4º ano do Ensino Fundamental em 2021 (%). |
| `VL_INDICADOR_REND_2021` | STRING | Indicador de rendimento escolar (fluxo) para o cálculo do IDEB em 2021. |
| `VL_APROVACAO_2023_SI_4` | STRING | Taxa de aprovação média das séries iniciais (1º ao 4º ano) em 2023 (%). |
| `VL_APROVACAO_2023_SI` | STRING | Taxa de aprovação para turmas sem informação de série em 2023 (%). |
| `VL_APROVACAO_2023_1` | STRING | Taxa de aprovação no 1º ano do Ensino Fundamental em 2023 (%). |
| `VL_APROVACAO_2023_2` | STRING | Taxa de aprovação no 2º ano do Ensino Fundamental em 2023 (%). |
| `VL_APROVACAO_2023_3` | STRING | Taxa de aprovação no 3º ano do Ensino Fundamental em 2023 (%). |
| `VL_APROVACAO_2023_4` | STRING | Taxa de aprovação no 4º ano do Ensino Fundamental em 2023 (%). |
| `VL_INDICADOR_REND_2023` | STRING | Indicador de rendimento escolar (fluxo) para o cálculo do IDEB em 2023. |
| `VL_APROVACAO_2025_SI_4` | STRING | Taxa de aprovação (%) agregada até o 4º ano em 2025. — descrição gerada por IA. |
| `VL_APROVACAO_2025_SI` | STRING | Taxa de aprovação (%) média agregada das séries do segmento em 2025. — descrição gerada por IA. |
| `VL_APROVACAO_2025_1` | STRING | Taxa de aprovação (%) no 1º ano/série no ano de 2025. — descrição gerada por IA. |
| `VL_APROVACAO_2025_2` | STRING | Taxa de aprovação (%) no 2º ano/série no ano de 2025. — descrição gerada por IA. |
| `VL_APROVACAO_2025_3` | STRING | Taxa de aprovação (%) no 3º ano/série no ano de 2025. — descrição gerada por IA. |
| `VL_APROVACAO_2025_4` | STRING | Taxa de aprovação (%) no 4º ano/série no ano de 2025. — descrição gerada por IA. |
| `VL_INDICADOR_REND_2025` | STRING | Indicador de rendimento escolar (fluxo) calculado pelo INEP para 2025 (0 a 1). — descrição gerada por IA. |
| `VL_NOTA_MATEMATICA_2005` | STRING | Nota média padronizada em Matemática no SAEB em 2005. |
| `VL_NOTA_PORTUGUES_2005` | STRING | Nota média padronizada em Língua Portuguesa no SAEB em 2005. |
| `VL_NOTA_MEDIA_2005` | STRING | Nota média padronizada geral (Matemática e Português) no SAEB em 2005. |
| `VL_NOTA_MATEMATICA_2007` | STRING | Nota média padronizada em Matemática no SAEB em 2007. |
| `VL_NOTA_PORTUGUES_2007` | STRING | Nota média padronizada em Língua Portuguesa no SAEB em 2007. |
| `VL_NOTA_MEDIA_2007` | STRING | Nota média padronizada geral (Matemática e Português) no SAEB em 2007. |
| `VL_NOTA_MATEMATICA_2009` | STRING | Nota média padronizada em Matemática no SAEB em 2009. |
| `VL_NOTA_PORTUGUES_2009` | STRING | Nota média padronizada em Língua Portuguesa no SAEB em 2009. |
| `VL_NOTA_MEDIA_2009` | STRING | Nota média padronizada geral (Matemática e Português) no SAEB em 2009. |
| `VL_NOTA_MATEMATICA_2011` | STRING | Nota média padronizada em Matemática no SAEB em 2011. |
| `VL_NOTA_PORTUGUES_2011` | STRING | Nota média padronizada em Língua Portuguesa no SAEB em 2011. |
| `VL_NOTA_MEDIA_2011` | STRING | Nota média padronizada geral (Matemática e Português) no SAEB em 2011. |
| `VL_NOTA_MATEMATICA_2013` | STRING | Nota média padronizada em Matemática no SAEB em 2013. |
| `VL_NOTA_PORTUGUES_2013` | STRING | Nota média padronizada em Língua Portuguesa no SAEB em 2013. |
| `VL_NOTA_MEDIA_2013` | STRING | Nota média padronizada geral (Matemática e Português) no SAEB em 2013. |
| `VL_NOTA_MATEMATICA_2015` | STRING | Nota média padronizada em Matemática no SAEB em 2015. |
| `VL_NOTA_PORTUGUES_2015` | STRING | Nota média padronizada em Língua Portuguesa no SAEB em 2015. |
| `VL_NOTA_MEDIA_2015` | STRING | Nota média padronizada geral (Matemática e Português) no SAEB em 2015. |
| `VL_NOTA_MATEMATICA_2017` | STRING | Nota média padronizada em Matemática no SAEB em 2017. |
| `VL_NOTA_PORTUGUES_2017` | STRING | Nota média padronizada em Língua Portuguesa no SAEB em 2017. |
| `VL_NOTA_MEDIA_2017` | STRING | Nota média padronizada geral (Matemática e Português) no SAEB em 2017. |
| `VL_NOTA_MATEMATICA_2019` | STRING | Nota média padronizada em Matemática no SAEB em 2019. |
| `VL_NOTA_PORTUGUES_2019` | STRING | Nota média padronizada em Língua Portuguesa no SAEB em 2019. |
| `VL_NOTA_MEDIA_2019` | STRING | Nota média padronizada geral (Matemática e Português) no SAEB em 2019. |
| `VL_NOTA_MATEMATICA_2021` | STRING | Nota média padronizada em Matemática no SAEB em 2021. |
| `VL_NOTA_PORTUGUES_2021` | STRING | Nota média padronizada em Língua Portuguesa no SAEB em 2021. |
| `VL_NOTA_MEDIA_2021` | STRING | Nota média padronizada geral (Matemática e Português) no SAEB em 2021. |
| `VL_NOTA_MATEMATICA_2023` | STRING | Nota média padronizada em Matemática no SAEB em 2023. |
| `VL_NOTA_PORTUGUES_2023` | STRING | Nota média padronizada em Língua Portuguesa no SAEB em 2023. |
| `VL_NOTA_MEDIA_2023` | STRING | Nota média padronizada geral (Matemática e Português) no SAEB em 2023. |
| `VL_NOTA_MATEMATICA_2025` | STRING | Nota média padronizada em Matemática estimada/calculada para 2025. — descrição gerada por IA. |
| `VL_NOTA_PORTUGUES_2025` | STRING | Nota média padronizada em Língua Portuguesa estimada/calculada para 2025. — descrição gerada por IA. |
| `VL_NOTA_MEDIA_2025` | STRING | Nota média padronizada agregada estimada/calculada para 2025. — descrição gerada por IA. |
| `VL_OBSERVADO_2005` | STRING | Valor observado do IDEB em 2005. |
| `VL_OBSERVADO_2007` | STRING | Valor observado do IDEB em 2007. |
| `VL_OBSERVADO_2009` | STRING | Valor observado do IDEB em 2009. |
| `VL_OBSERVADO_2011` | STRING | Valor observado do IDEB em 2011. |
| `VL_OBSERVADO_2013` | STRING | Valor observado do IDEB em 2013. |
| `VL_OBSERVADO_2015` | STRING | Valor observado do IDEB em 2015. |
| `VL_OBSERVADO_2017` | STRING | Valor observado do IDEB em 2017. |
| `VL_OBSERVADO_2019` | STRING | Valor observado do IDEB em 2019. |
| `VL_OBSERVADO_2021` | STRING | Valor observado do IDEB em 2021. |
| `VL_OBSERVADO_2023` | STRING | Valor observado do IDEB em 2023. |
| `VL_OBSERVADO_2025` | STRING | Índice do IDEB observado ou projetado para o ano de 2025 (escala de 0 a 10). — descrição gerada por IA. |
| `VL_PROJECAO_2007` | STRING | Meta projetada do IDEB para o ano de 2007. |
| `VL_PROJECAO_2009` | STRING | Meta projetada do IDEB para o ano de 2009. |
| `VL_PROJECAO_2011` | STRING | Meta projetada do IDEB para o ano de 2011. |
| `VL_PROJECAO_2013` | STRING | Meta projetada do IDEB para o ano de 2013. |
| `VL_PROJECAO_2015` | STRING | Meta projetada do IDEB para o ano de 2015. |
| `VL_PROJECAO_2017` | STRING | Meta projetada do IDEB para o ano de 2017. |
| `VL_PROJECAO_2019` | STRING | Meta projetada do IDEB para o ano de 2019. |
| `VL_PROJECAO_2021` | STRING | Meta projetada do IDEB para o ano de 2021. |
| `nivel` | STRING | Etapa ou nível de ensino avaliado (ex: 'anos_iniciais', 'anos_finais'). |
| `dt_ingestao_lake` | STRING | Data e hora de ingestão do registro no Data Lake (YYYY-MM-DD). — descrição gerada por IA. |

## raw · inep_ideb_brasil_ensino_medio

File `raw__inep_ideb_brasil_ensino_medio.parquet` · 14 rows · 122 columns

Tabela histórica contendo indicadores do IDEB (fluxo escolar, notas do SAEB, IDEB observado e metas projetadas) agregados em nível nacional por rede de ensino e nível de escolaridade.

**Feeds:** `trusted/inep_ideb_brasil`

| Column | Type | Description |
|---|---|---|
| `BRASIL` | STRING | Nome da abrangência geográfica (Brasil). |
| `rede` | STRING | Rede de ensino analisada (ex: Estadual, Privada, Pública, Total). |
| `VL_APROVACAO_2005_SI_4` | STRING | Taxa de aprovação (%) média/consolidada das séries do nível de ensino em 2005. |
| `VL_APROVACAO_2005_1` | STRING | Taxa de aprovação (%) no 1º ano/série do nível de ensino em 2005. |
| `VL_APROVACAO_2005_2` | STRING | Taxa de aprovação (%) no 2º ano/série do nível de ensino em 2005. |
| `VL_APROVACAO_2005_3` | STRING | Taxa de aprovação (%) no 3º ano/série do nível de ensino em 2005. |
| `VL_APROVACAO_2005_4` | STRING | Taxa de aprovação (%) no 4º ano/série do nível de ensino em 2005. |
| `VL_INDICADOR_REND_2005` | STRING | Indicador de rendimento escolar (fluxo) para o cálculo do IDEB em 2005. |
| `VL_APROVACAO_2007_SI_4` | STRING | Taxa de aprovação (%) média/consolidada das séries do nível de ensino em 2007. |
| `VL_APROVACAO_2007_1` | STRING | Taxa de aprovação (%) no 1º ano/série do nível de ensino em 2007. |
| `VL_APROVACAO_2007_2` | STRING | Taxa de aprovação (%) no 2º ano/série do nível de ensino em 2007. |
| `VL_APROVACAO_2007_3` | STRING | Taxa de aprovação (%) no 3º ano/série do nível de ensino em 2007. |
| `VL_APROVACAO_2007_4` | STRING | Taxa de aprovação (%) no 4º ano/série do nível de ensino em 2007. |
| `VL_INDICADOR_REND_2007` | STRING | Indicador de rendimento escolar (fluxo) para o cálculo do IDEB em 2007. |
| `VL_APROVACAO_2009_SI_4` | STRING | Taxa de aprovação (%) média/consolidada das séries do nível de ensino em 2009. |
| `VL_APROVACAO_2009_1` | STRING | Taxa de aprovação (%) no 1º ano/série do nível de ensino em 2009. |
| `VL_APROVACAO_2009_2` | STRING | Taxa de aprovação (%) no 2º ano/série do nível de ensino em 2009. |
| `VL_APROVACAO_2009_3` | STRING | Taxa de aprovação (%) no 3º ano/série do nível de ensino em 2009. |
| `VL_APROVACAO_2009_4` | STRING | Taxa de aprovação (%) no 4º ano/série do nível de ensino em 2009. |
| `VL_INDICADOR_REND_2009` | STRING | Indicador de rendimento escolar (fluxo) para o cálculo do IDEB em 2009. |
| `VL_APROVACAO_2011_SI_4` | STRING | Taxa de aprovação (%) média/consolidada das séries do nível de ensino em 2011. |
| `VL_APROVACAO_2011_1` | STRING | Taxa de aprovação (%) no 1º ano/série do nível de ensino em 2011. |
| `VL_APROVACAO_2011_2` | STRING | Taxa de aprovação (%) no 2º ano/série do nível de ensino em 2011. |
| `VL_APROVACAO_2011_3` | STRING | Taxa de aprovação (%) no 3º ano/série do nível de ensino em 2011. |
| `VL_APROVACAO_2011_4` | STRING | Taxa de aprovação (%) no 4º ano/série do nível de ensino em 2011. |
| `VL_INDICADOR_REND_2011` | STRING | Indicador de rendimento escolar (fluxo) para o cálculo do IDEB em 2011. |
| `VL_APROVACAO_2013_SI_4` | STRING | Taxa de aprovação (%) média/consolidada das séries do nível de ensino em 2013. |
| `VL_APROVACAO_2013_1` | STRING | Taxa de aprovação (%) no 1º ano/série do nível de ensino em 2013. |
| `VL_APROVACAO_2013_2` | STRING | Taxa de aprovação (%) no 2º ano/série do nível de ensino em 2013. |
| `VL_APROVACAO_2013_3` | STRING | Taxa de aprovação (%) no 3º ano/série do nível de ensino em 2013. |
| `VL_APROVACAO_2013_4` | STRING | Taxa de aprovação (%) no 4º ano/série do nível de ensino em 2013. |
| `VL_INDICADOR_REND_2013` | STRING | Indicador de rendimento escolar (fluxo) para o cálculo do IDEB em 2013. |
| `VL_APROVACAO_2015_SI_4` | STRING | Taxa de aprovação (%) média/consolidada das séries do nível de ensino em 2015. |
| `VL_APROVACAO_2015_1` | STRING | Taxa de aprovação (%) no 1º ano/série do nível de ensino em 2015. |
| `VL_APROVACAO_2015_2` | STRING | Taxa de aprovação (%) no 2º ano/série do nível de ensino em 2015. |
| `VL_APROVACAO_2015_3` | STRING | Taxa de aprovação (%) no 3º ano/série do nível de ensino em 2015. |
| `VL_APROVACAO_2015_4` | STRING | Taxa de aprovação (%) no 4º ano/série do nível de ensino em 2015. |
| `VL_INDICADOR_REND_2015` | STRING | Indicador de rendimento escolar (fluxo) para o cálculo do IDEB em 2015. |
| `VL_APROVACAO_2017_SI_4` | STRING | Taxa de aprovação (%) média/consolidada das séries do nível de ensino em 2017. |
| `VL_APROVACAO_2017_1` | STRING | Taxa de aprovação (%) no 1º ano/série do nível de ensino em 2017. |
| `VL_APROVACAO_2017_2` | STRING | Taxa de aprovação (%) no 2º ano/série do nível de ensino em 2017. |
| `VL_APROVACAO_2017_3` | STRING | Taxa de aprovação (%) no 3º ano/série do nível de ensino em 2017. |
| `VL_APROVACAO_2017_4` | STRING | Taxa de aprovação (%) no 4º ano/série do nível de ensino em 2017. |
| `VL_INDICADOR_REND_2017` | STRING | Indicador de rendimento escolar (fluxo) para o cálculo do IDEB em 2017. |
| `VL_APROVACAO_2019_SI_4` | STRING | Taxa de aprovação (%) média/consolidada das séries do nível de ensino em 2019. |
| `VL_APROVACAO_2019_1` | STRING | Taxa de aprovação (%) no 1º ano/série do nível de ensino em 2019. |
| `VL_APROVACAO_2019_2` | STRING | Taxa de aprovação (%) no 2º ano/série do nível de ensino em 2019. |
| `VL_APROVACAO_2019_3` | STRING | Taxa de aprovação (%) no 3º ano/série do nível de ensino em 2019. |
| `VL_APROVACAO_2019_4` | STRING | Taxa de aprovação (%) no 4º ano/série do nível de ensino em 2019. |
| `VL_INDICADOR_REND_2019` | STRING | Indicador de rendimento escolar (fluxo) para o cálculo do IDEB em 2019. |
| `VL_APROVACAO_2021_SI_4` | STRING | Taxa de aprovação (%) média/consolidada das séries do nível de ensino em 2021. |
| `VL_APROVACAO_2021_1` | STRING | Taxa de aprovação (%) no 1º ano/série do nível de ensino em 2021. |
| `VL_APROVACAO_2021_2` | STRING | Taxa de aprovação (%) no 2º ano/série do nível de ensino em 2021. |
| `VL_APROVACAO_2021_3` | STRING | Taxa de aprovação (%) no 3º ano/série do nível de ensino em 2021. |
| `VL_APROVACAO_2021_4` | STRING | Taxa de aprovação (%) no 4º ano/série do nível de ensino em 2021. |
| `VL_INDICADOR_REND_2021` | STRING | Indicador de rendimento escolar (fluxo) para o cálculo do IDEB em 2021. |
| `VL_APROVACAO_2023_SI_4` | STRING | Taxa de aprovação (%) média/consolidada das séries do nível de ensino em 2023. |
| `VL_APROVACAO_2023_1` | STRING | Taxa de aprovação (%) no 1º ano/série do nível de ensino em 2023. |
| `VL_APROVACAO_2023_2` | STRING | Taxa de aprovação (%) no 2º ano/série do nível de ensino em 2023. |
| `VL_APROVACAO_2023_3` | STRING | Taxa de aprovação (%) no 3º ano/série do nível de ensino em 2023. |
| `VL_APROVACAO_2023_4` | STRING | Taxa de aprovação (%) no 4º ano/série do nível de ensino em 2023. |
| `VL_INDICADOR_REND_2023` | STRING | Indicador de rendimento escolar (fluxo) para o cálculo do IDEB em 2023. |
| `VL_APROVACAO_2025_SI_4` | STRING | Taxa media projetada/estimada de aprovacao escolar do 1o ao 4o ano do Ensino Medio em 2025 (%). — descrição gerada por IA. |
| `VL_APROVACAO_2025_1` | STRING | Taxa de aprovacao escolar projetada/estimada na 1a serie do Ensino Medio em 2025 (%). — descrição gerada por IA. |
| `VL_APROVACAO_2025_2` | STRING | Taxa de aprovacao escolar projetada/estimada na 2a serie do Ensino Medio em 2025 (%). — descrição gerada por IA. |
| `VL_APROVACAO_2025_3` | STRING | Taxa de aprovacao escolar projetada/estimada na 3a serie do Ensino Medio em 2025 (%). — descrição gerada por IA. |
| `VL_APROVACAO_2025_4` | STRING | Taxa de aprovacao escolar projetada/estimada na 4a serie do Ensino Medio em 2025 (%). — descrição gerada por IA. |
| `VL_INDICADOR_REND_2025` | STRING | Indicador de rendimento escolar (P) projetado/estimado para o IDEB 2025 (escala de 0 a 1). — descrição gerada por IA. |
| `VL_NOTA_MATEMATICA_2005` | STRING | Nota média padronizada em Matemática obtida no SAEB em 2005. |
| `VL_NOTA_PORTUGUES_2005` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB em 2005. |
| `VL_NOTA_MEDIA_2005` | STRING | Nota média padronizada total (proficiência) para o cálculo do IDEB em 2005. |
| `VL_NOTA_MATEMATICA_2007` | STRING | Nota média padronizada em Matemática obtida no SAEB em 2007. |
| `VL_NOTA_PORTUGUES_2007` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB em 2007. |
| `VL_NOTA_MEDIA_2007` | STRING | Nota média padronizada total (proficiência) para o cálculo do IDEB em 2007. |
| `VL_NOTA_MATEMATICA_2009` | STRING | Nota média padronizada em Matemática obtida no SAEB em 2009. |
| `VL_NOTA_PORTUGUES_2009` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB em 2009. |
| `VL_NOTA_MEDIA_2009` | STRING | Nota média padronizada total (proficiência) para o cálculo do IDEB em 2009. |
| `VL_NOTA_MATEMATICA_2011` | STRING | Nota média padronizada em Matemática obtida no SAEB em 2011. |
| `VL_NOTA_PORTUGUES_2011` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB em 2011. |
| `VL_NOTA_MEDIA_2011` | STRING | Nota média padronizada total (proficiência) para o cálculo do IDEB em 2011. |
| `VL_NOTA_MATEMATICA_2013` | STRING | Nota média padronizada em Matemática obtida no SAEB em 2013. |
| `VL_NOTA_PORTUGUES_2013` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB em 2013. |
| `VL_NOTA_MEDIA_2013` | STRING | Nota média padronizada total (proficiência) para o cálculo do IDEB em 2013. |
| `VL_NOTA_MATEMATICA_2015` | STRING | Nota média padronizada em Matemática obtida no SAEB em 2015. |
| `VL_NOTA_PORTUGUES_2015` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB em 2015. |
| `VL_NOTA_MEDIA_2015` | STRING | Nota média padronizada total (proficiência) para o cálculo do IDEB em 2015. |
| `VL_NOTA_MATEMATICA_2017` | STRING | Nota média padronizada em Matemática obtida no SAEB em 2017. |
| `VL_NOTA_PORTUGUES_2017` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB em 2017. |
| `VL_NOTA_MEDIA_2017` | STRING | Nota média padronizada total (proficiência) para o cálculo do IDEB em 2017. |
| `VL_NOTA_MATEMATICA_2019` | STRING | Nota média padronizada em Matemática obtida no SAEB em 2019. |
| `VL_NOTA_PORTUGUES_2019` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB em 2019. |
| `VL_NOTA_MEDIA_2019` | STRING | Nota média padronizada total (proficiência) para o cálculo do IDEB em 2019. |
| `VL_NOTA_MATEMATICA_2021` | STRING | Nota média padronizada em Matemática obtida no SAEB em 2021. |
| `VL_NOTA_PORTUGUES_2021` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB em 2021. |
| `VL_NOTA_MEDIA_2021` | STRING | Nota média padronizada total (proficiência) para o cálculo do IDEB em 2021. |
| `VL_NOTA_MATEMATICA_2023` | STRING | Nota média padronizada em Matemática obtida no SAEB em 2023. |
| `VL_NOTA_PORTUGUES_2023` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB em 2023. |
| `VL_NOTA_MEDIA_2023` | STRING | Nota média padronizada total (proficiência) para o cálculo do IDEB em 2023. |
| `VL_NOTA_MATEMATICA_2025` | STRING | Nota media padronizada projetada/estimada na avaliacao de Matematica para 2025. — descrição gerada por IA. |
| `VL_NOTA_PORTUGUES_2025` | STRING | Nota media padronizada projetada/estimada na avaliacao de Lingua Portuguesa para 2025. — descrição gerada por IA. |
| `VL_NOTA_MEDIA_2025` | STRING | Nota media de aprendizado (N) projetada/estimada para o IDEB 2025 (escala de 0 a 10). — descrição gerada por IA. |
| `VL_OBSERVADO_2005` | STRING | Valor observado do IDEB obtido no ano de 2005. |
| `VL_OBSERVADO_2007` | STRING | Valor observado do IDEB obtido no ano de 2007. |
| `VL_OBSERVADO_2009` | STRING | Valor observado do IDEB obtido no ano de 2009. |
| `VL_OBSERVADO_2011` | STRING | Valor observado do IDEB obtido no ano de 2011. |
| `VL_OBSERVADO_2013` | STRING | Valor observado do IDEB obtido no ano de 2013. |
| `VL_OBSERVADO_2015` | STRING | Valor observado do IDEB obtido no ano de 2015. |
| `VL_OBSERVADO_2017` | STRING | Valor observado do IDEB obtido no ano de 2017. |
| `VL_OBSERVADO_2019` | STRING | Valor observado do IDEB obtido no ano de 2019. |
| `VL_OBSERVADO_2021` | STRING | Valor observado do IDEB obtido no ano de 2021. |
| `VL_OBSERVADO_2023` | STRING | Valor observado do IDEB obtido no ano de 2023. |
| `VL_OBSERVADO_2025` | STRING | Indice do IDEB observado ou estimado para o ano de 2025 (escala de 0 a 10). — descrição gerada por IA. |
| `VL_PROJECAO_2007` | STRING | Meta projetada do IDEB para o ano de 2007. |
| `VL_PROJECAO_2009` | STRING | Meta projetada do IDEB para o ano de 2009. |
| `VL_PROJECAO_2011` | STRING | Meta projetada do IDEB para o ano de 2011. |
| `VL_PROJECAO_2013` | STRING | Meta projetada do IDEB para o ano de 2013. |
| `VL_PROJECAO_2015` | STRING | Meta projetada do IDEB para o ano de 2015. |
| `VL_PROJECAO_2017` | STRING | Meta projetada do IDEB para o ano de 2017. |
| `VL_PROJECAO_2019` | STRING | Meta projetada do IDEB para o ano de 2019. |
| `VL_PROJECAO_2021` | STRING | Meta projetada do IDEB para o ano de 2021. |
| `nivel` | STRING | Nível de ensino correspondente aos dados (ex: ensino_medio). |
| `dt_ingestao_lake` | STRING | Data e hora do carregamento do registro no Data Lake (formato ISO 8601). — descrição gerada por IA. |

## raw · inep_ideb_escola_anos_finais

File `raw__inep_ideb_escola_anos_finais.parquet` · 48,020 rows · 126 columns

Tabela histórica de indicadores educacionais do IDEB (Índice de Desenvolvimento da Educação Básica) por escola, contendo taxas de aprovação, notas do SAEB (Matemática e Português), indicador de rendimento, valores observados e projeções de metas de 2005 a 2023.

**Feeds:** `trusted/inep_ideb_escola`

| Column | Type | Description |
|---|---|---|
| `SG_UF` | STRING | Sigla do estado (UF) onde a escola ou município está localizado |
| `CO_MUNICIPIO` | STRING | Código IBGE do município (7 dígitos) |
| `NO_MUNICIPIO` | STRING | Nome do município conforme IBGE |
| `ID_ESCOLA` | STRING | Código INEP da escola (8 dígitos) — identificador único nacional da escola |
| `NO_ESCOLA` | STRING | Nome da escola conforme cadastro do Censo Escolar |
| `REDE` | STRING | Dependência administrativa: Municipal, Estadual, Federal ou Privada |
| `VL_APROVACAO_2005_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2005 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2005_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2005 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2005_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2005 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2005_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2005 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2005_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2005 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2005` | STRING | Indicador de Rendimento (P) em 2005 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2007_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2007 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2007_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2007 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2007_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2007 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2007_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2007 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2007_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2007 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2007` | STRING | Indicador de Rendimento (P) em 2007 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2009_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2009 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2009_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2009 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2009_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2009 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2009_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2009 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2009_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2009 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2009` | STRING | Indicador de Rendimento (P) em 2009 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2011_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2011 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2011_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2011 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2011_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2011 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2011_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2011 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2011_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2011 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2011` | STRING | Indicador de Rendimento (P) em 2011 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2013_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2013 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2013_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2013 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2013_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2013 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2013_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2013 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2013_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2013 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2013` | STRING | Indicador de Rendimento (P) em 2013 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2015_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2015 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2015_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2015 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2015_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2015 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2015_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2015 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2015_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2015 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2015` | STRING | Indicador de Rendimento (P) em 2015 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2017_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2017 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2017_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2017 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2017_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2017 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2017_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2017 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2017_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2017 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2017` | STRING | Indicador de Rendimento (P) em 2017 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2019_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2019 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2019_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2019 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2019_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2019 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2019_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2019 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2019_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2019 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2019` | STRING | Indicador de Rendimento (P) em 2019 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2021_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2021 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2021_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2021 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2021_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2021 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2021_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2021 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2021_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2021 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2021` | STRING | Indicador de Rendimento (P) em 2021 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2023_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2023 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2023_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2023 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2023_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2023 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2023_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2023 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2023_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2023 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2023` | STRING | Indicador de Rendimento (P) em 2023 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2025_SI_4` | STRING | Taxa media de aprovacao (%) projetada/esperada dos anos/series em 2025. — descrição gerada por IA. |
| `VL_APROVACAO_2025_1` | STRING | Taxa de aprovacao (%) no 1o ano/serie do ciclo em 2025. — descrição gerada por IA. |
| `VL_APROVACAO_2025_2` | STRING | Taxa de aprovacao (%) no 2o ano/serie do ciclo em 2025. — descrição gerada por IA. |
| `VL_APROVACAO_2025_3` | STRING | Taxa de aprovacao (%) no 3o ano/serie do ciclo em 2025. — descrição gerada por IA. |
| `VL_APROVACAO_2025_4` | STRING | Taxa de aprovacao (%) no 4o ano/serie do ciclo em 2025. — descrição gerada por IA. |
| `VL_INDICADOR_REND_2025` | STRING | Indicador de rendimento escolar (P) em 2025. — descrição gerada por IA. |
| `VL_NOTA_MATEMATICA_2005` | STRING | Nota padronizada de Matemática no SAEB 2005. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2005` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2005. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2005` | STRING | Nota média padronizada (N) em 2005 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2007` | STRING | Nota padronizada de Matemática no SAEB 2007. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2007` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2007. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2007` | STRING | Nota média padronizada (N) em 2007 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2009` | STRING | Nota padronizada de Matemática no SAEB 2009. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2009` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2009. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2009` | STRING | Nota média padronizada (N) em 2009 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2011` | STRING | Nota padronizada de Matemática no SAEB 2011. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2011` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2011. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2011` | STRING | Nota média padronizada (N) em 2011 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2013` | STRING | Nota padronizada de Matemática no SAEB 2013. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2013` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2013. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2013` | STRING | Nota média padronizada (N) em 2013 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2015` | STRING | Nota padronizada de Matemática no SAEB 2015. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2015` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2015. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2015` | STRING | Nota média padronizada (N) em 2015 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2017` | STRING | Nota padronizada de Matemática no SAEB 2017. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2017` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2017. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2017` | STRING | Nota média padronizada (N) em 2017 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2019` | STRING | Nota padronizada de Matemática no SAEB 2019. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2019` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2019. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2019` | STRING | Nota média padronizada (N) em 2019 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2021` | STRING | Nota padronizada de Matemática no SAEB 2021. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2021` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2021. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2021` | STRING | Nota média padronizada (N) em 2021 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2023` | STRING | Nota padronizada de Matemática no SAEB 2023. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2023` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2023. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2023` | STRING | Nota média padronizada (N) em 2023 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2025` | STRING | Nota media padronizada em Matematica no Saeb 2025. — descrição gerada por IA. |
| `VL_NOTA_PORTUGUES_2025` | STRING | Nota media padronizada em Lingua Portuguesa no Saeb 2025. — descrição gerada por IA. |
| `VL_NOTA_MEDIA_2025` | STRING | Nota media padronizada total (N) no Saeb 2025. — descrição gerada por IA. |
| `VL_OBSERVADO_2005` | STRING | IDEB observado em 2005 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2007` | STRING | IDEB observado em 2007 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2009` | STRING | IDEB observado em 2009 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2011` | STRING | IDEB observado em 2011 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2013` | STRING | IDEB observado em 2013 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2015` | STRING | IDEB observado em 2015 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2017` | STRING | IDEB observado em 2017 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2019` | STRING | IDEB observado em 2019 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2021` | STRING | IDEB observado em 2021 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2023` | STRING | IDEB observado em 2023 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2025` | STRING | Indice IDEB observado ou projetado para o ano de 2025. — descrição gerada por IA. |
| `VL_PROJECAO_2007` | STRING | Meta projetada pelo MEC para o IDEB em 2007. Trajetória definida no âmbito do Compromisso Todos pela Educação para que o Brasil atinja o nível dos países da OCDE até 2022. Ausente para 2005 (ano base) e 2023 (meta não publicada). |
| `VL_PROJECAO_2009` | STRING | Meta projetada pelo MEC para o IDEB em 2009. Trajetória definida no âmbito do Compromisso Todos pela Educação para que o Brasil atinja o nível dos países da OCDE até 2022. Ausente para 2005 (ano base) e 2023 (meta não publicada). |
| `VL_PROJECAO_2011` | STRING | Meta projetada pelo MEC para o IDEB em 2011. Trajetória definida no âmbito do Compromisso Todos pela Educação para que o Brasil atinja o nível dos países da OCDE até 2022. Ausente para 2005 (ano base) e 2023 (meta não publicada). |
| `VL_PROJECAO_2013` | STRING | Meta projetada pelo MEC para o IDEB em 2013. Trajetória definida no âmbito do Compromisso Todos pela Educação para que o Brasil atinja o nível dos países da OCDE até 2022. Ausente para 2005 (ano base) e 2023 (meta não publicada). |
| `VL_PROJECAO_2015` | STRING | Meta projetada pelo MEC para o IDEB em 2015. Trajetória definida no âmbito do Compromisso Todos pela Educação para que o Brasil atinja o nível dos países da OCDE até 2022. Ausente para 2005 (ano base) e 2023 (meta não publicada). |
| `VL_PROJECAO_2017` | STRING | Meta projetada pelo MEC para o IDEB em 2017. Trajetória definida no âmbito do Compromisso Todos pela Educação para que o Brasil atinja o nível dos países da OCDE até 2022. Ausente para 2005 (ano base) e 2023 (meta não publicada). |
| `VL_PROJECAO_2019` | STRING | Meta projetada pelo MEC para o IDEB em 2019. Trajetória definida no âmbito do Compromisso Todos pela Educação para que o Brasil atinja o nível dos países da OCDE até 2022. Ausente para 2005 (ano base) e 2023 (meta não publicada). |
| `VL_PROJECAO_2021` | STRING | Meta projetada pelo MEC para o IDEB em 2021. Trajetória definida no âmbito do Compromisso Todos pela Educação para que o Brasil atinja o nível dos países da OCDE até 2022. Ausente para 2005 (ano base) e 2023 (meta não publicada). |
| `nivel` | STRING | Segmento avaliado: anos_iniciais, anos_finais ou ensino_medio (adicionado na ingestão) |
| `dt_ingestao_lake` | STRING | Timestamp UTC de quando o arquivo foi carregado no data lake |

## raw · inep_ideb_escola_anos_iniciais

File `raw__inep_ideb_escola_anos_iniciais.parquet` · 66,153 rows · 137 columns

Tabela histórica com indicadores do IDEB (Índice de Desenvolvimento da Educação Básica) e do SAEB por escola, contendo taxas de aprovação, notas de proficiência em matemática e português, médias, valores observados e metas projetadas de 2005 a 2023.

**Feeds:** `trusted/inep_ideb_escola`

| Column | Type | Description |
|---|---|---|
| `SG_UF` | STRING | Sigla do estado (UF) onde a escola ou município está localizado |
| `CO_MUNICIPIO` | STRING | Código IBGE do município (7 dígitos) |
| `NO_MUNICIPIO` | STRING | Nome do município conforme IBGE |
| `ID_ESCOLA` | STRING | Código INEP da escola (8 dígitos) — identificador único nacional da escola |
| `NO_ESCOLA` | STRING | Nome da escola conforme cadastro do Censo Escolar |
| `REDE` | STRING | Dependência administrativa: Municipal, Estadual, Federal ou Privada |
| `VL_APROVACAO_2005_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2005 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2005_SI` | STRING | Taxa de aprovação da 1ª série dos Anos Iniciais em 2005 (%). Coluna exclusiva do segmento anos_iniciais — ausente em anos_finais e ensino_medio. |
| `VL_APROVACAO_2005_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2005 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2005_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2005 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2005_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2005 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2005_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2005 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2005` | STRING | Indicador de Rendimento (P) em 2005 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2007_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2007 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2007_SI` | STRING | Taxa de aprovação da 1ª série dos Anos Iniciais em 2007 (%). Coluna exclusiva do segmento anos_iniciais — ausente em anos_finais e ensino_medio. |
| `VL_APROVACAO_2007_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2007 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2007_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2007 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2007_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2007 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2007_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2007 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2007` | STRING | Indicador de Rendimento (P) em 2007 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2009_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2009 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2009_SI` | STRING | Taxa de aprovação da 1ª série dos Anos Iniciais em 2009 (%). Coluna exclusiva do segmento anos_iniciais — ausente em anos_finais e ensino_medio. |
| `VL_APROVACAO_2009_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2009 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2009_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2009 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2009_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2009 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2009_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2009 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2009` | STRING | Indicador de Rendimento (P) em 2009 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2011_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2011 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2011_SI` | STRING | Taxa de aprovação da 1ª série dos Anos Iniciais em 2011 (%). Coluna exclusiva do segmento anos_iniciais — ausente em anos_finais e ensino_medio. |
| `VL_APROVACAO_2011_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2011 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2011_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2011 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2011_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2011 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2011_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2011 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2011` | STRING | Indicador de Rendimento (P) em 2011 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2013_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2013 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2013_SI` | STRING | Taxa de aprovação da 1ª série dos Anos Iniciais em 2013 (%). Coluna exclusiva do segmento anos_iniciais — ausente em anos_finais e ensino_medio. |
| `VL_APROVACAO_2013_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2013 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2013_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2013 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2013_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2013 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2013_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2013 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2013` | STRING | Indicador de Rendimento (P) em 2013 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2015_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2015 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2015_SI` | STRING | Taxa de aprovação da 1ª série dos Anos Iniciais em 2015 (%). Coluna exclusiva do segmento anos_iniciais — ausente em anos_finais e ensino_medio. |
| `VL_APROVACAO_2015_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2015 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2015_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2015 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2015_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2015 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2015_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2015 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2015` | STRING | Indicador de Rendimento (P) em 2015 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2017_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2017 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2017_SI` | STRING | Taxa de aprovação da 1ª série dos Anos Iniciais em 2017 (%). Coluna exclusiva do segmento anos_iniciais — ausente em anos_finais e ensino_medio. |
| `VL_APROVACAO_2017_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2017 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2017_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2017 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2017_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2017 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2017_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2017 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2017` | STRING | Indicador de Rendimento (P) em 2017 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2019_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2019 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2019_SI` | STRING | Taxa de aprovação da 1ª série dos Anos Iniciais em 2019 (%). Coluna exclusiva do segmento anos_iniciais — ausente em anos_finais e ensino_medio. |
| `VL_APROVACAO_2019_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2019 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2019_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2019 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2019_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2019 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2019_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2019 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2019` | STRING | Indicador de Rendimento (P) em 2019 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2021_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2021 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2021_SI` | STRING | Taxa de aprovação da 1ª série dos Anos Iniciais em 2021 (%). Coluna exclusiva do segmento anos_iniciais — ausente em anos_finais e ensino_medio. |
| `VL_APROVACAO_2021_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2021 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2021_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2021 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2021_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2021 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2021_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2021 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2021` | STRING | Indicador de Rendimento (P) em 2021 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2023_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2023 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2023_SI` | STRING | Taxa de aprovação da 1ª série dos Anos Iniciais em 2023 (%). Coluna exclusiva do segmento anos_iniciais — ausente em anos_finais e ensino_medio. |
| `VL_APROVACAO_2023_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2023 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2023_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2023 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2023_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2023 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2023_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2023 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2023` | STRING | Indicador de Rendimento (P) em 2023 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2025_SI_4` | STRING | Taxa média de aprovação (%) do 1º ao 4º ano das séries iniciais em 2025. — descrição gerada por IA. |
| `VL_APROVACAO_2025_SI` | STRING | Taxa média de aprovação (%) das séries iniciais em 2025. — descrição gerada por IA. |
| `VL_APROVACAO_2025_1` | STRING | Taxa de aprovação (%) no 1º ano em 2025. — descrição gerada por IA. |
| `VL_APROVACAO_2025_2` | STRING | Taxa de aprovação (%) no 2º ano em 2025. — descrição gerada por IA. |
| `VL_APROVACAO_2025_3` | STRING | Taxa de aprovação (%) no 3º ano em 2025. — descrição gerada por IA. |
| `VL_APROVACAO_2025_4` | STRING | Taxa de aprovação (%) no 4º ano em 2025. — descrição gerada por IA. |
| `VL_INDICADOR_REND_2025` | STRING | Indicador de rendimento escolar (P) em 2025. — descrição gerada por IA. |
| `VL_NOTA_MATEMATICA_2005` | STRING | Nota padronizada de Matemática no SAEB 2005. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2005` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2005. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2005` | STRING | Nota média padronizada (N) em 2005 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2007` | STRING | Nota padronizada de Matemática no SAEB 2007. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2007` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2007. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2007` | STRING | Nota média padronizada (N) em 2007 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2009` | STRING | Nota padronizada de Matemática no SAEB 2009. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2009` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2009. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2009` | STRING | Nota média padronizada (N) em 2009 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2011` | STRING | Nota padronizada de Matemática no SAEB 2011. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2011` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2011. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2011` | STRING | Nota média padronizada (N) em 2011 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2013` | STRING | Nota padronizada de Matemática no SAEB 2013. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2013` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2013. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2013` | STRING | Nota média padronizada (N) em 2013 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2015` | STRING | Nota padronizada de Matemática no SAEB 2015. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2015` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2015. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2015` | STRING | Nota média padronizada (N) em 2015 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2017` | STRING | Nota padronizada de Matemática no SAEB 2017. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2017` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2017. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2017` | STRING | Nota média padronizada (N) em 2017 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2019` | STRING | Nota padronizada de Matemática no SAEB 2019. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2019` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2019. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2019` | STRING | Nota média padronizada (N) em 2019 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2021` | STRING | Nota padronizada de Matemática no SAEB 2021. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2021` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2021. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2021` | STRING | Nota média padronizada (N) em 2021 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2023` | STRING | Nota padronizada de Matemática no SAEB 2023. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2023` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2023. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2023` | STRING | Nota média padronizada (N) em 2023 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2025` | STRING | Nota média de Matemática no SAEB em 2025. — descrição gerada por IA. |
| `VL_NOTA_PORTUGUES_2025` | STRING | Nota média de Língua Portuguesa no SAEB em 2025. — descrição gerada por IA. |
| `VL_NOTA_MEDIA_2025` | STRING | Nota média padronizada (N) do SAEB em 2025. — descrição gerada por IA. |
| `VL_OBSERVADO_2005` | STRING | IDEB observado em 2005 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2007` | STRING | IDEB observado em 2007 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2009` | STRING | IDEB observado em 2009 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2011` | STRING | IDEB observado em 2011 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2013` | STRING | IDEB observado em 2013 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2015` | STRING | IDEB observado em 2015 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2017` | STRING | IDEB observado em 2017 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2019` | STRING | IDEB observado em 2019 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2021` | STRING | IDEB observado em 2021 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2023` | STRING | IDEB observado em 2023 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2025` | STRING | Valor observado do IDEB alcançado pela escola em 2025. — descrição gerada por IA. |
| `VL_PROJECAO_2007` | STRING | Meta projetada pelo MEC para o IDEB em 2007. Trajetória definida no âmbito do Compromisso Todos pela Educação para que o Brasil atinja o nível dos países da OCDE até 2022. Ausente para 2005 (ano base) e 2023 (meta não publicada). |
| `VL_PROJECAO_2009` | STRING | Meta projetada pelo MEC para o IDEB em 2009. Trajetória definida no âmbito do Compromisso Todos pela Educação para que o Brasil atinja o nível dos países da OCDE até 2022. Ausente para 2005 (ano base) e 2023 (meta não publicada). |
| `VL_PROJECAO_2011` | STRING | Meta projetada pelo MEC para o IDEB em 2011. Trajetória definida no âmbito do Compromisso Todos pela Educação para que o Brasil atinja o nível dos países da OCDE até 2022. Ausente para 2005 (ano base) e 2023 (meta não publicada). |
| `VL_PROJECAO_2013` | STRING | Meta projetada pelo MEC para o IDEB em 2013. Trajetória definida no âmbito do Compromisso Todos pela Educação para que o Brasil atinja o nível dos países da OCDE até 2022. Ausente para 2005 (ano base) e 2023 (meta não publicada). |
| `VL_PROJECAO_2015` | STRING | Meta projetada pelo MEC para o IDEB em 2015. Trajetória definida no âmbito do Compromisso Todos pela Educação para que o Brasil atinja o nível dos países da OCDE até 2022. Ausente para 2005 (ano base) e 2023 (meta não publicada). |
| `VL_PROJECAO_2017` | STRING | Meta projetada pelo MEC para o IDEB em 2017. Trajetória definida no âmbito do Compromisso Todos pela Educação para que o Brasil atinja o nível dos países da OCDE até 2022. Ausente para 2005 (ano base) e 2023 (meta não publicada). |
| `VL_PROJECAO_2019` | STRING | Meta projetada pelo MEC para o IDEB em 2019. Trajetória definida no âmbito do Compromisso Todos pela Educação para que o Brasil atinja o nível dos países da OCDE até 2022. Ausente para 2005 (ano base) e 2023 (meta não publicada). |
| `VL_PROJECAO_2021` | STRING | Meta projetada pelo MEC para o IDEB em 2021. Trajetória definida no âmbito do Compromisso Todos pela Educação para que o Brasil atinja o nível dos países da OCDE até 2022. Ausente para 2005 (ano base) e 2023 (meta não publicada). |
| `nivel` | STRING | Segmento avaliado: anos_iniciais, anos_finais ou ensino_medio (adicionado na ingestão) |
| `dt_ingestao_lake` | STRING | Timestamp UTC de quando o arquivo foi carregado no data lake |

## raw · inep_ideb_escola_ensino_medio

File `raw__inep_ideb_escola_ensino_medio.parquet` · 22,184 rows · 60 columns

Tabela histórica de indicadores educacionais por escola, contendo taxas de aprovação detalhadas por série, proficiência no SAEB (Matemática e Português) e notas do IDEB (observadas e projetadas) para os anos de 2017, 2019, 2021 e 2023.

**Feeds:** `trusted/inep_ideb_escola`

| Column | Type | Description |
|---|---|---|
| `SG_UF` | STRING | Sigla do estado (UF) onde a escola ou município está localizado |
| `CO_MUNICIPIO` | STRING | Código IBGE do município (7 dígitos) |
| `NO_MUNICIPIO` | STRING | Nome do município conforme IBGE |
| `ID_ESCOLA` | STRING | Código INEP da escola (8 dígitos) — identificador único nacional da escola |
| `NO_ESCOLA` | STRING | Nome da escola conforme cadastro do Censo Escolar |
| `REDE` | STRING | Dependência administrativa: Municipal, Estadual, Federal ou Privada |
| `VL_APROVACAO_2017_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2017 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2017_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2017 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2017_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2017 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2017_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2017 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2017_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2017 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2017` | STRING | Indicador de Rendimento (P) em 2017 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2019_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2019 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2019_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2019 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2019_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2019 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2019_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2019 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2019_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2019 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2019` | STRING | Indicador de Rendimento (P) em 2019 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2021_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2021 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2021_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2021 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2021_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2021 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2021_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2021 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2021_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2021 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2021` | STRING | Indicador de Rendimento (P) em 2021 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2023_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2023 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2023_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2023 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2023_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2023 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2023_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2023 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2023_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2023 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2023` | STRING | Indicador de Rendimento (P) em 2023 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2025_SI_4` | STRING | Taxa média de aprovação do ciclo em 2025 (%). — descrição gerada por IA. |
| `VL_APROVACAO_2025_1` | STRING | Taxa de aprovação na 1ª série/ano em 2025 (%). — descrição gerada por IA. |
| `VL_APROVACAO_2025_2` | STRING | Taxa de aprovação na 2ª série/ano em 2025 (%). — descrição gerada por IA. |
| `VL_APROVACAO_2025_3` | STRING | Taxa de aprovação na 3ª série/ano em 2025 (%). — descrição gerada por IA. |
| `VL_APROVACAO_2025_4` | STRING | Taxa de aprovação na 4ª série/ano em 2025 (%). — descrição gerada por IA. |
| `VL_INDICADOR_REND_2025` | STRING | Indicador de rendimento escolar (fator P) em 2025 (0 a 1). — descrição gerada por IA. |
| `VL_NOTA_MATEMATICA_2017` | STRING | Nota padronizada de Matemática no SAEB 2017. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2017` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2017. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2017` | STRING | Nota média padronizada (N) em 2017 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2019` | STRING | Nota padronizada de Matemática no SAEB 2019. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2019` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2019. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2019` | STRING | Nota média padronizada (N) em 2019 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2021` | STRING | Nota padronizada de Matemática no SAEB 2021. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2021` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2021. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2021` | STRING | Nota média padronizada (N) em 2021 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2023` | STRING | Nota padronizada de Matemática no SAEB 2023. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2023` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2023. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2023` | STRING | Nota média padronizada (N) em 2023 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2025` | STRING | Nota média padronizada em Matemática no SAEB 2025. — descrição gerada por IA. |
| `VL_NOTA_PORTUGUES_2025` | STRING | Nota média padronizada em Língua Portuguesa no SAEB 2025. — descrição gerada por IA. |
| `VL_NOTA_MEDIA_2025` | STRING | Nota média padronizada do SAEB em 2025. — descrição gerada por IA. |
| `VL_OBSERVADO_2017` | STRING | IDEB observado em 2017 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2019` | STRING | IDEB observado em 2019 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2021` | STRING | IDEB observado em 2021 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2023` | STRING | IDEB observado em 2023 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2025` | STRING | Nota do IDEB observada ou estimada para a escola em 2025. — descrição gerada por IA. |
| `VL_PROJECAO_2019` | STRING | Meta projetada pelo MEC para o IDEB em 2019. Trajetória definida no âmbito do Compromisso Todos pela Educação para que o Brasil atinja o nível dos países da OCDE até 2022. Ausente para 2005 (ano base) e 2023 (meta não publicada). |
| `VL_PROJECAO_2021` | STRING | Meta projetada pelo MEC para o IDEB em 2021. Trajetória definida no âmbito do Compromisso Todos pela Educação para que o Brasil atinja o nível dos países da OCDE até 2022. Ausente para 2005 (ano base) e 2023 (meta não publicada). |
| `nivel` | STRING | Segmento avaliado: anos_iniciais, anos_finais ou ensino_medio (adicionado na ingestão) |
| `dt_ingestao_lake` | STRING | Timestamp UTC de quando o arquivo foi carregado no data lake |

## raw · inep_ideb_municipio_anos_finais

File `raw__inep_ideb_municipio_anos_finais.parquet` · 14,428 rows · 124 columns

Tabela histórica contendo indicadores do IDEB (Índice de Desenvolvimento da Educação Básica) agregados por município, rede de ensino e nível de escolaridade, incluindo taxas de aprovação por série, notas do SAEB (Matemática e Português), indicador de rendimento, notas observadas do IDEB e metas projetadas de 2005 a 2023.

**Feeds:** `trusted/inep_ideb_municipio`

| Column | Type | Description |
|---|---|---|
| `SG_UF` | STRING | Sigla do estado (UF) onde a escola ou município está localizado |
| `CO_MUNICIPIO` | STRING | Código IBGE do município (7 dígitos) |
| `NO_MUNICIPIO` | STRING | Nome do município conforme IBGE |
| `REDE` | STRING | Dependência administrativa: Municipal, Estadual, Federal ou Privada |
| `VL_APROVACAO_2005_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2005 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2005_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2005 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2005_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2005 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2005_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2005 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2005_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2005 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2005` | STRING | Indicador de Rendimento (P) em 2005 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2007_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2007 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2007_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2007 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2007_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2007 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2007_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2007 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2007_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2007 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2007` | STRING | Indicador de Rendimento (P) em 2007 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2009_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2009 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2009_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2009 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2009_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2009 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2009_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2009 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2009_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2009 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2009` | STRING | Indicador de Rendimento (P) em 2009 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2011_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2011 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2011_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2011 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2011_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2011 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2011_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2011 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2011_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2011 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2011` | STRING | Indicador de Rendimento (P) em 2011 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2013_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2013 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2013_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2013 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2013_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2013 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2013_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2013 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2013_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2013 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2013` | STRING | Indicador de Rendimento (P) em 2013 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2015_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2015 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2015_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2015 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2015_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2015 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2015_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2015 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2015_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2015 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2015` | STRING | Indicador de Rendimento (P) em 2015 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2017_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2017 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2017_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2017 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2017_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2017 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2017_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2017 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2017_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2017 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2017` | STRING | Indicador de Rendimento (P) em 2017 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2019_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2019 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2019_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2019 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2019_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2019 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2019_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2019 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2019_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2019 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2019` | STRING | Indicador de Rendimento (P) em 2019 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2021_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2021 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2021_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2021 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2021_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2021 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2021_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2021 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2021_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2021 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2021` | STRING | Indicador de Rendimento (P) em 2021 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2023_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2023 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2023_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2023 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2023_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2023 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2023_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2023 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2023_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2023 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2023` | STRING | Indicador de Rendimento (P) em 2023 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2025_SI_4` | STRING | Taxa de aprovação (%) das séries iniciais até a 4ª série/ano no IDEB 2025. — descrição gerada por IA. |
| `VL_APROVACAO_2025_1` | STRING | Taxa de aprovação (%) no 1º ano/série no IDEB 2025. — descrição gerada por IA. |
| `VL_APROVACAO_2025_2` | STRING | Taxa de aprovação (%) no 2º ano/série no IDEB 2025. — descrição gerada por IA. |
| `VL_APROVACAO_2025_3` | STRING | Taxa de aprovação (%) no 3º ano/série no IDEB 2025. — descrição gerada por IA. |
| `VL_APROVACAO_2025_4` | STRING | Taxa de aprovação (%) no 4º ano/série no IDEB 2025. — descrição gerada por IA. |
| `VL_INDICADOR_REND_2025` | STRING | Indicador de rendimento escolar (P) no IDEB 2025 (0 a 1). — descrição gerada por IA. |
| `VL_NOTA_MATEMATICA_2005` | STRING | Nota padronizada de Matemática no SAEB 2005. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2005` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2005. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2005` | STRING | Nota média padronizada (N) em 2005 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2007` | STRING | Nota padronizada de Matemática no SAEB 2007. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2007` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2007. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2007` | STRING | Nota média padronizada (N) em 2007 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2009` | STRING | Nota padronizada de Matemática no SAEB 2009. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2009` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2009. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2009` | STRING | Nota média padronizada (N) em 2009 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2011` | STRING | Nota padronizada de Matemática no SAEB 2011. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2011` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2011. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2011` | STRING | Nota média padronizada (N) em 2011 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2013` | STRING | Nota padronizada de Matemática no SAEB 2013. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2013` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2013. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2013` | STRING | Nota média padronizada (N) em 2013 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2015` | STRING | Nota padronizada de Matemática no SAEB 2015. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2015` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2015. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2015` | STRING | Nota média padronizada (N) em 2015 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2017` | STRING | Nota padronizada de Matemática no SAEB 2017. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2017` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2017. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2017` | STRING | Nota média padronizada (N) em 2017 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2019` | STRING | Nota padronizada de Matemática no SAEB 2019. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2019` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2019. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2019` | STRING | Nota média padronizada (N) em 2019 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2021` | STRING | Nota padronizada de Matemática no SAEB 2021. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2021` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2021. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2021` | STRING | Nota média padronizada (N) em 2021 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2023` | STRING | Nota padronizada de Matemática no SAEB 2023. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2023` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2023. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2023` | STRING | Nota média padronizada (N) em 2023 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2025` | STRING | Nota média de Matemática no SAEB 2025. — descrição gerada por IA. |
| `VL_NOTA_PORTUGUES_2025` | STRING | Nota média de Língua Portuguesa no SAEB 2025. — descrição gerada por IA. |
| `VL_NOTA_MEDIA_2025` | STRING | Nota média padronizada do desempenho no SAEB 2025. — descrição gerada por IA. |
| `VL_OBSERVADO_2005` | STRING | IDEB observado em 2005 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2007` | STRING | IDEB observado em 2007 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2009` | STRING | IDEB observado em 2009 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2011` | STRING | IDEB observado em 2011 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2013` | STRING | IDEB observado em 2013 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2015` | STRING | IDEB observado em 2015 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2017` | STRING | IDEB observado em 2017 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2019` | STRING | IDEB observado em 2019 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2021` | STRING | IDEB observado em 2021 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2023` | STRING | IDEB observado em 2023 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2025` | STRING | Índice IDEB observado no ano de 2025. — descrição gerada por IA. |
| `VL_PROJECAO_2007` | STRING | Meta projetada pelo MEC para o IDEB em 2007. Trajetória definida no âmbito do Compromisso Todos pela Educação para que o Brasil atinja o nível dos países da OCDE até 2022. Ausente para 2005 (ano base) e 2023 (meta não publicada). |
| `VL_PROJECAO_2009` | STRING | Meta projetada pelo MEC para o IDEB em 2009. Trajetória definida no âmbito do Compromisso Todos pela Educação para que o Brasil atinja o nível dos países da OCDE até 2022. Ausente para 2005 (ano base) e 2023 (meta não publicada). |
| `VL_PROJECAO_2011` | STRING | Meta projetada pelo MEC para o IDEB em 2011. Trajetória definida no âmbito do Compromisso Todos pela Educação para que o Brasil atinja o nível dos países da OCDE até 2022. Ausente para 2005 (ano base) e 2023 (meta não publicada). |
| `VL_PROJECAO_2013` | STRING | Meta projetada pelo MEC para o IDEB em 2013. Trajetória definida no âmbito do Compromisso Todos pela Educação para que o Brasil atinja o nível dos países da OCDE até 2022. Ausente para 2005 (ano base) e 2023 (meta não publicada). |
| `VL_PROJECAO_2015` | STRING | Meta projetada pelo MEC para o IDEB em 2015. Trajetória definida no âmbito do Compromisso Todos pela Educação para que o Brasil atinja o nível dos países da OCDE até 2022. Ausente para 2005 (ano base) e 2023 (meta não publicada). |
| `VL_PROJECAO_2017` | STRING | Meta projetada pelo MEC para o IDEB em 2017. Trajetória definida no âmbito do Compromisso Todos pela Educação para que o Brasil atinja o nível dos países da OCDE até 2022. Ausente para 2005 (ano base) e 2023 (meta não publicada). |
| `VL_PROJECAO_2019` | STRING | Meta projetada pelo MEC para o IDEB em 2019. Trajetória definida no âmbito do Compromisso Todos pela Educação para que o Brasil atinja o nível dos países da OCDE até 2022. Ausente para 2005 (ano base) e 2023 (meta não publicada). |
| `VL_PROJECAO_2021` | STRING | Meta projetada pelo MEC para o IDEB em 2021. Trajetória definida no âmbito do Compromisso Todos pela Educação para que o Brasil atinja o nível dos países da OCDE até 2022. Ausente para 2005 (ano base) e 2023 (meta não publicada). |
| `nivel` | STRING | Segmento avaliado: anos_iniciais, anos_finais ou ensino_medio (adicionado na ingestão) |
| `dt_ingestao_lake` | STRING | Timestamp UTC de quando o arquivo foi carregado no data lake |

## raw · inep_ideb_municipio_anos_iniciais

File `raw__inep_ideb_municipio_anos_iniciais.parquet` · 14,533 rows · 135 columns

Tabela histórica contendo indicadores do IDEB (fluxo escolar, proficiência em Língua Portuguesa e Matemática, metas e notas observadas) agregados por município, rede de ensino e nível de ensino, cobrindo as edições bienais de 2005 a 2023.

**Feeds:** `trusted/inep_ideb_municipio`

| Column | Type | Description |
|---|---|---|
| `SG_UF` | STRING | Sigla do estado (UF) onde a escola ou município está localizado |
| `CO_MUNICIPIO` | STRING | Código IBGE do município (7 dígitos) |
| `NO_MUNICIPIO` | STRING | Nome do município conforme IBGE |
| `REDE` | STRING | Dependência administrativa: Municipal, Estadual, Federal ou Privada |
| `VL_APROVACAO_2005_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2005 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2005_SI` | STRING | Taxa de aprovação da 1ª série dos Anos Iniciais em 2005 (%). Coluna exclusiva do segmento anos_iniciais — ausente em anos_finais e ensino_medio. |
| `VL_APROVACAO_2005_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2005 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2005_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2005 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2005_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2005 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2005_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2005 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2005` | STRING | Indicador de Rendimento (P) em 2005 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2007_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2007 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2007_SI` | STRING | Taxa de aprovação da 1ª série dos Anos Iniciais em 2007 (%). Coluna exclusiva do segmento anos_iniciais — ausente em anos_finais e ensino_medio. |
| `VL_APROVACAO_2007_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2007 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2007_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2007 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2007_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2007 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2007_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2007 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2007` | STRING | Indicador de Rendimento (P) em 2007 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2009_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2009 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2009_SI` | STRING | Taxa de aprovação da 1ª série dos Anos Iniciais em 2009 (%). Coluna exclusiva do segmento anos_iniciais — ausente em anos_finais e ensino_medio. |
| `VL_APROVACAO_2009_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2009 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2009_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2009 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2009_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2009 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2009_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2009 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2009` | STRING | Indicador de Rendimento (P) em 2009 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2011_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2011 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2011_SI` | STRING | Taxa de aprovação da 1ª série dos Anos Iniciais em 2011 (%). Coluna exclusiva do segmento anos_iniciais — ausente em anos_finais e ensino_medio. |
| `VL_APROVACAO_2011_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2011 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2011_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2011 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2011_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2011 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2011_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2011 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2011` | STRING | Indicador de Rendimento (P) em 2011 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2013_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2013 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2013_SI` | STRING | Taxa de aprovação da 1ª série dos Anos Iniciais em 2013 (%). Coluna exclusiva do segmento anos_iniciais — ausente em anos_finais e ensino_medio. |
| `VL_APROVACAO_2013_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2013 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2013_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2013 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2013_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2013 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2013_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2013 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2013` | STRING | Indicador de Rendimento (P) em 2013 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2015_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2015 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2015_SI` | STRING | Taxa de aprovação da 1ª série dos Anos Iniciais em 2015 (%). Coluna exclusiva do segmento anos_iniciais — ausente em anos_finais e ensino_medio. |
| `VL_APROVACAO_2015_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2015 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2015_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2015 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2015_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2015 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2015_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2015 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2015` | STRING | Indicador de Rendimento (P) em 2015 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2017_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2017 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2017_SI` | STRING | Taxa de aprovação da 1ª série dos Anos Iniciais em 2017 (%). Coluna exclusiva do segmento anos_iniciais — ausente em anos_finais e ensino_medio. |
| `VL_APROVACAO_2017_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2017 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2017_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2017 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2017_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2017 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2017_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2017 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2017` | STRING | Indicador de Rendimento (P) em 2017 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2019_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2019 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2019_SI` | STRING | Taxa de aprovação da 1ª série dos Anos Iniciais em 2019 (%). Coluna exclusiva do segmento anos_iniciais — ausente em anos_finais e ensino_medio. |
| `VL_APROVACAO_2019_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2019 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2019_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2019 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2019_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2019 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2019_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2019 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2019` | STRING | Indicador de Rendimento (P) em 2019 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2021_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2021 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2021_SI` | STRING | Taxa de aprovação da 1ª série dos Anos Iniciais em 2021 (%). Coluna exclusiva do segmento anos_iniciais — ausente em anos_finais e ensino_medio. |
| `VL_APROVACAO_2021_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2021 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2021_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2021 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2021_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2021 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2021_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2021 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2021` | STRING | Indicador de Rendimento (P) em 2021 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2023_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2023 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2023_SI` | STRING | Taxa de aprovação da 1ª série dos Anos Iniciais em 2023 (%). Coluna exclusiva do segmento anos_iniciais — ausente em anos_finais e ensino_medio. |
| `VL_APROVACAO_2023_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2023 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2023_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2023 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2023_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2023 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2023_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2023 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2023` | STRING | Indicador de Rendimento (P) em 2023 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2025_SI_4` | STRING | Taxa de aprovação das séries iniciais (1º ao 4º ano) projetada ou registrada para 2025 (em %). — descrição gerada por IA. |
| `VL_APROVACAO_2025_SI` | STRING | Taxa de aprovação geral das séries iniciais projetada ou registrada para 2025 (em %). — descrição gerada por IA. |
| `VL_APROVACAO_2025_1` | STRING | Taxa de aprovação do 1º ano em 2025 (em %). — descrição gerada por IA. |
| `VL_APROVACAO_2025_2` | STRING | Taxa de aprovação do 2º ano em 2025 (em %). — descrição gerada por IA. |
| `VL_APROVACAO_2025_3` | STRING | Taxa de aprovação do 3º ano em 2025 (em %). — descrição gerada por IA. |
| `VL_APROVACAO_2025_4` | STRING | Taxa de aprovação do 4º ano em 2025 (em %). — descrição gerada por IA. |
| `VL_INDICADOR_REND_2025` | STRING | Indicador de rendimento escolar (fluxo) do IDEB em 2025 (0 a 1). — descrição gerada por IA. |
| `VL_NOTA_MATEMATICA_2005` | STRING | Nota padronizada de Matemática no SAEB 2005. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2005` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2005. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2005` | STRING | Nota média padronizada (N) em 2005 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2007` | STRING | Nota padronizada de Matemática no SAEB 2007. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2007` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2007. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2007` | STRING | Nota média padronizada (N) em 2007 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2009` | STRING | Nota padronizada de Matemática no SAEB 2009. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2009` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2009. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2009` | STRING | Nota média padronizada (N) em 2009 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2011` | STRING | Nota padronizada de Matemática no SAEB 2011. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2011` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2011. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2011` | STRING | Nota média padronizada (N) em 2011 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2013` | STRING | Nota padronizada de Matemática no SAEB 2013. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2013` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2013. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2013` | STRING | Nota média padronizada (N) em 2013 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2015` | STRING | Nota padronizada de Matemática no SAEB 2015. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2015` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2015. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2015` | STRING | Nota média padronizada (N) em 2015 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2017` | STRING | Nota padronizada de Matemática no SAEB 2017. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2017` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2017. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2017` | STRING | Nota média padronizada (N) em 2017 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2019` | STRING | Nota padronizada de Matemática no SAEB 2019. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2019` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2019. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2019` | STRING | Nota média padronizada (N) em 2019 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2021` | STRING | Nota padronizada de Matemática no SAEB 2021. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2021` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2021. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2021` | STRING | Nota média padronizada (N) em 2021 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2023` | STRING | Nota padronizada de Matemática no SAEB 2023. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2023` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2023. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2023` | STRING | Nota média padronizada (N) em 2023 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2025` | STRING | Nota média em Matemática no SAEB em 2025. — descrição gerada por IA. |
| `VL_NOTA_PORTUGUES_2025` | STRING | Nota média em Língua Portuguesa no SAEB em 2025. — descrição gerada por IA. |
| `VL_NOTA_MEDIA_2025` | STRING | Nota média padronizada de aprendizado do IDEB em 2025. — descrição gerada por IA. |
| `VL_OBSERVADO_2005` | STRING | IDEB observado em 2005 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2007` | STRING | IDEB observado em 2007 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2009` | STRING | IDEB observado em 2009 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2011` | STRING | IDEB observado em 2011 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2013` | STRING | IDEB observado em 2013 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2015` | STRING | IDEB observado em 2015 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2017` | STRING | IDEB observado em 2017 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2019` | STRING | IDEB observado em 2019 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2021` | STRING | IDEB observado em 2021 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2023` | STRING | IDEB observado em 2023 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2025` | STRING | Nota final observada do IDEB no ano de 2025. — descrição gerada por IA. |
| `VL_PROJECAO_2007` | STRING | Meta projetada pelo MEC para o IDEB em 2007. Trajetória definida no âmbito do Compromisso Todos pela Educação para que o Brasil atinja o nível dos países da OCDE até 2022. Ausente para 2005 (ano base) e 2023 (meta não publicada). |
| `VL_PROJECAO_2009` | STRING | Meta projetada pelo MEC para o IDEB em 2009. Trajetória definida no âmbito do Compromisso Todos pela Educação para que o Brasil atinja o nível dos países da OCDE até 2022. Ausente para 2005 (ano base) e 2023 (meta não publicada). |
| `VL_PROJECAO_2011` | STRING | Meta projetada pelo MEC para o IDEB em 2011. Trajetória definida no âmbito do Compromisso Todos pela Educação para que o Brasil atinja o nível dos países da OCDE até 2022. Ausente para 2005 (ano base) e 2023 (meta não publicada). |
| `VL_PROJECAO_2013` | STRING | Meta projetada pelo MEC para o IDEB em 2013. Trajetória definida no âmbito do Compromisso Todos pela Educação para que o Brasil atinja o nível dos países da OCDE até 2022. Ausente para 2005 (ano base) e 2023 (meta não publicada). |
| `VL_PROJECAO_2015` | STRING | Meta projetada pelo MEC para o IDEB em 2015. Trajetória definida no âmbito do Compromisso Todos pela Educação para que o Brasil atinja o nível dos países da OCDE até 2022. Ausente para 2005 (ano base) e 2023 (meta não publicada). |
| `VL_PROJECAO_2017` | STRING | Meta projetada pelo MEC para o IDEB em 2017. Trajetória definida no âmbito do Compromisso Todos pela Educação para que o Brasil atinja o nível dos países da OCDE até 2022. Ausente para 2005 (ano base) e 2023 (meta não publicada). |
| `VL_PROJECAO_2019` | STRING | Meta projetada pelo MEC para o IDEB em 2019. Trajetória definida no âmbito do Compromisso Todos pela Educação para que o Brasil atinja o nível dos países da OCDE até 2022. Ausente para 2005 (ano base) e 2023 (meta não publicada). |
| `VL_PROJECAO_2021` | STRING | Meta projetada pelo MEC para o IDEB em 2021. Trajetória definida no âmbito do Compromisso Todos pela Educação para que o Brasil atinja o nível dos países da OCDE até 2022. Ausente para 2005 (ano base) e 2023 (meta não publicada). |
| `nivel` | STRING | Segmento avaliado: anos_iniciais, anos_finais ou ensino_medio (adicionado na ingestão) |
| `dt_ingestao_lake` | STRING | Timestamp UTC de quando o arquivo foi carregado no data lake |

## raw · inep_ideb_municipio_ensino_medio

File `raw__inep_ideb_municipio_ensino_medio.parquet` · 11,765 rows · 58 columns

Tabela consolidada com indicadores históricos do IDEB e SAEB por município, rede de ensino e nível de escolaridade, abrangendo taxas de aprovação, proficiências em matemática e português, notas médias, metas e resultados observados de 2017 a 2023.

**Feeds:** `trusted/inep_ideb_municipio`

| Column | Type | Description |
|---|---|---|
| `SG_UF` | STRING | Sigla do estado (UF) onde a escola ou município está localizado |
| `CO_MUNICIPIO` | STRING | Código IBGE do município (7 dígitos) |
| `NO_MUNICIPIO` | STRING | Nome do município conforme IBGE |
| `REDE` | STRING | Dependência administrativa: Municipal, Estadual, Federal ou Privada |
| `VL_APROVACAO_2017_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2017 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2017_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2017 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2017_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2017 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2017_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2017 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2017_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2017 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2017` | STRING | Indicador de Rendimento (P) em 2017 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2019_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2019 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2019_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2019 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2019_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2019 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2019_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2019 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2019_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2019 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2019` | STRING | Indicador de Rendimento (P) em 2019 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2021_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2021 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2021_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2021 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2021_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2021 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2021_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2021 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2021_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2021 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2021` | STRING | Indicador de Rendimento (P) em 2021 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2023_SI_4` | STRING | Taxa de aprovação média de todas as séries do segmento em 2023 (%). '-' indica que a escola/município não participou do IDEB nessa edição. |
| `VL_APROVACAO_2023_1` | STRING | Taxa de aprovação na 1ª série medida do segmento em 2023 (%). Para AI: 2° ano; para AF: 6° ano; para EM: 1° ano do EM. |
| `VL_APROVACAO_2023_2` | STRING | Taxa de aprovação na 2ª série medida do segmento em 2023 (%). Para AI: 3° ano EF; para AF: 7° ano; para EM: 2° ano do EM. |
| `VL_APROVACAO_2023_3` | STRING | Taxa de aprovação na 3ª série medida do segmento em 2023 (%). Para AI: 4° ano EF; para AF: 8° ano; para EM: 3° ano do EM. |
| `VL_APROVACAO_2023_4` | STRING | Taxa de aprovação na 4ª série medida do segmento em 2023 (%). Para AI: 5° ano EF; para AF: 9° ano. |
| `VL_INDICADOR_REND_2023` | STRING | Indicador de Rendimento (P) em 2023 — média ponderada das taxas de aprovação de todas as séries. Quanto mais próximo de 1, melhor o fluxo escolar. Componente P da fórmula: IDEB = N × P. |
| `VL_APROVACAO_2025_SI_4` | STRING | Taxa média de aprovação total para o ciclo de séries em 2025 (%). — descrição gerada por IA. |
| `VL_APROVACAO_2025_1` | STRING | Taxa de aprovação dos alunos na 1ª série/ano em 2025 (%). — descrição gerada por IA. |
| `VL_APROVACAO_2025_2` | STRING | Taxa de aprovação dos alunos na 2ª série/ano em 2025 (%). — descrição gerada por IA. |
| `VL_APROVACAO_2025_3` | STRING | Taxa de aprovação dos alunos na 3ª série/ano em 2025 (%). — descrição gerada por IA. |
| `VL_APROVACAO_2025_4` | STRING | Taxa de aprovação dos alunos na 4ª série/ano em 2025 (%). — descrição gerada por IA. |
| `VL_INDICADOR_REND_2025` | STRING | Indicador de rendimento escolar (fluxo) calculado para o IDEB 2025. — descrição gerada por IA. |
| `VL_NOTA_MATEMATICA_2017` | STRING | Nota padronizada de Matemática no SAEB 2017. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2017` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2017. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2017` | STRING | Nota média padronizada (N) em 2017 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2019` | STRING | Nota padronizada de Matemática no SAEB 2019. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2019` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2019. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2019` | STRING | Nota média padronizada (N) em 2019 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2021` | STRING | Nota padronizada de Matemática no SAEB 2021. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2021` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2021. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2021` | STRING | Nota média padronizada (N) em 2021 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2023` | STRING | Nota padronizada de Matemática no SAEB 2023. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica que a escola não aplicou o SAEB. |
| `VL_NOTA_PORTUGUES_2023` | STRING | Nota padronizada de Língua Portuguesa no SAEB 2023. Escala normalizada para alimentar o cálculo do IDEB. 'ND' indica ausência de aplicação. |
| `VL_NOTA_MEDIA_2023` | STRING | Nota média padronizada (N) em 2023 — média geométrica entre nota de Matemática e de Língua Portuguesa no SAEB. Componente N da fórmula: IDEB = N × P. |
| `VL_NOTA_MATEMATICA_2025` | STRING | Nota média obtida em Matemática no SAEB 2025. — descrição gerada por IA. |
| `VL_NOTA_PORTUGUES_2025` | STRING | Nota média obtida em Língua Portuguesa no SAEB 2025. — descrição gerada por IA. |
| `VL_NOTA_MEDIA_2025` | STRING | Nota média padronizada do SAEB utilizada no cálculo do IDEB 2025. — descrição gerada por IA. |
| `VL_OBSERVADO_2017` | STRING | IDEB observado em 2017 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2019` | STRING | IDEB observado em 2019 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2021` | STRING | IDEB observado em 2021 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2023` | STRING | IDEB observado em 2023 — resultado final calculado como N × P. Varia de 0 a 10. '-' indica que escola/município não compõe o IDEB nessa edição. |
| `VL_OBSERVADO_2025` | STRING | Valor observado ou projetado da nota do IDEB no ano de 2025. — descrição gerada por IA. |
| `VL_PROJECAO_2019` | STRING | Meta projetada pelo MEC para o IDEB em 2019. Trajetória definida no âmbito do Compromisso Todos pela Educação para que o Brasil atinja o nível dos países da OCDE até 2022. Ausente para 2005 (ano base) e 2023 (meta não publicada). |
| `VL_PROJECAO_2021` | STRING | Meta projetada pelo MEC para o IDEB em 2021. Trajetória definida no âmbito do Compromisso Todos pela Educação para que o Brasil atinja o nível dos países da OCDE até 2022. Ausente para 2005 (ano base) e 2023 (meta não publicada). |
| `nivel` | STRING | Segmento avaliado: anos_iniciais, anos_finais ou ensino_medio (adicionado na ingestão) |
| `dt_ingestao_lake` | STRING | Timestamp UTC de quando o arquivo foi carregado no data lake |

## raw · inep_ideb_regioes_ufs_anos_finais

File `raw__inep_ideb_regioes_ufs_anos_finais.parquet` · 141 rows · 122 columns

Tabela histórica com indicadores do IDEB (2005-2023), contendo taxas de aprovação escolar por série, notas médias do SAEB (Matemática e Português), indicador de rendimento, além dos valores observados e projetados do IDEB, segmentados por unidade geográfica, rede de ensino e nível.

**Feeds:** `trusted/inep_ideb_regioes_ufs`

| Column | Type | Description |
|---|---|---|
| `unidade_geografica` | STRING | Nome ou sigla da unidade geográfica analisada (ex: Estado, Município ou Brasil). |
| `rede` | STRING | Rede de ensino avaliada (ex: Estadual, Municipal, Federal, Privada ou Pública). |
| `VL_APROVACAO_2005_SI_4` | STRING | Taxa de aprovação escolar para séries iniciais/finais sem informação específica de série no ano de 2005 (de 0 a 100). |
| `VL_APROVACAO_2005_1` | STRING | Taxa de aprovação escolar no 1º ano/série do segmento no ano de 2005 (de 0 a 100). |
| `VL_APROVACAO_2005_2` | STRING | Taxa de aprovação escolar no 2º ano/série do segmento no ano de 2005 (de 0 a 100). |
| `VL_APROVACAO_2005_3` | STRING | Taxa de aprovação escolar no 3º ano/série do segmento no ano de 2005 (de 0 a 100). |
| `VL_APROVACAO_2005_4` | STRING | Taxa de aprovação escolar no 4º ano/série do segmento no ano de 2005 (de 0 a 100). |
| `VL_INDICADOR_REND_2005` | STRING | Indicador de rendimento médio (fluxo escolar) calculado para o IDEB no ano de 2005. |
| `VL_APROVACAO_2007_SI_4` | STRING | Taxa de aprovação escolar para séries iniciais/finais sem informação específica de série no ano de 2007 (de 0 a 100). |
| `VL_APROVACAO_2007_1` | STRING | Taxa de aprovação escolar no 1º ano/série do segmento no ano de 2007 (de 0 a 100). |
| `VL_APROVACAO_2007_2` | STRING | Taxa de aprovação escolar no 2º ano/série do segmento no ano de 2007 (de 0 a 100). |
| `VL_APROVACAO_2007_3` | STRING | Taxa de aprovação escolar no 3º ano/série do segmento no ano de 2007 (de 0 a 100). |
| `VL_APROVACAO_2007_4` | STRING | Taxa de aprovação escolar no 4º ano/série do segmento no ano de 2007 (de 0 a 100). |
| `VL_INDICADOR_REND_2007` | STRING | Indicador de rendimento médio (fluxo escolar) calculado para o IDEB no ano de 2007. |
| `VL_APROVACAO_2009_SI_4` | STRING | Taxa de aprovação escolar para séries iniciais/finais sem informação específica de série no ano de 2009 (de 0 a 100). |
| `VL_APROVACAO_2009_1` | STRING | Taxa de aprovação escolar no 1º ano/série do segmento no ano de 2009 (de 0 a 100). |
| `VL_APROVACAO_2009_2` | STRING | Taxa de aprovação escolar no 2º ano/série do segmento no ano de 2009 (de 0 a 100). |
| `VL_APROVACAO_2009_3` | STRING | Taxa de aprovação escolar no 3º ano/série do segmento no ano de 2009 (de 0 a 100). |
| `VL_APROVACAO_2009_4` | STRING | Taxa de aprovação escolar no 4º ano/série do segmento no ano de 2009 (de 0 a 100). |
| `VL_INDICADOR_REND_2009` | STRING | Indicador de rendimento médio (fluxo escolar) calculado para o IDEB no ano de 2009. |
| `VL_APROVACAO_2011_SI_4` | STRING | Taxa de aprovação escolar para séries iniciais/finais sem informação específica de série no ano de 2011 (de 0 a 100). |
| `VL_APROVACAO_2011_1` | STRING | Taxa de aprovação escolar no 1º ano/série do segmento no ano de 2011 (de 0 a 100). |
| `VL_APROVACAO_2011_2` | STRING | Taxa de aprovação escolar no 2º ano/série do segmento no ano de 2011 (de 0 a 100). |
| `VL_APROVACAO_2011_3` | STRING | Taxa de aprovação escolar no 3º ano/série do segmento no ano de 2011 (de 0 a 100). |
| `VL_APROVACAO_2011_4` | STRING | Taxa de aprovação escolar no 4º ano/série do segmento no ano de 2011 (de 0 a 100). |
| `VL_INDICADOR_REND_2011` | STRING | Indicador de rendimento médio (fluxo escolar) calculado para o IDEB no ano de 2011. |
| `VL_APROVACAO_2013_SI_4` | STRING | Taxa de aprovação escolar para séries iniciais/finais sem informação específica de série no ano de 2013 (de 0 a 100). |
| `VL_APROVACAO_2013_1` | STRING | Taxa de aprovação escolar no 1º ano/série do segmento no ano de 2013 (de 0 a 100). |
| `VL_APROVACAO_2013_2` | STRING | Taxa de aprovação escolar no 2º ano/série do segmento no ano de 2013 (de 0 a 100). |
| `VL_APROVACAO_2013_3` | STRING | Taxa de aprovação escolar no 3º ano/série do segmento no ano de 2013 (de 0 a 100). |
| `VL_APROVACAO_2013_4` | STRING | Taxa de aprovação escolar no 4º ano/série do segmento no ano de 2013 (de 0 a 100). |
| `VL_INDICADOR_REND_2013` | STRING | Indicador de rendimento médio (fluxo escolar) calculado para o IDEB no ano de 2013. |
| `VL_APROVACAO_2015_SI_4` | STRING | Taxa de aprovação escolar para séries iniciais/finais sem informação específica de série no ano de 2015 (de 0 a 100). |
| `VL_APROVACAO_2015_1` | STRING | Taxa de aprovação escolar no 1º ano/série do segmento no ano de 2015 (de 0 a 100). |
| `VL_APROVACAO_2015_2` | STRING | Taxa de aprovação escolar no 2º ano/série do segmento no ano de 2015 (de 0 a 100). |
| `VL_APROVACAO_2015_3` | STRING | Taxa de aprovação escolar no 3º ano/série do segmento no ano de 2015 (de 0 a 100). |
| `VL_APROVACAO_2015_4` | STRING | Taxa de aprovação escolar no 4º ano/série do segmento no ano de 2015 (de 0 a 100). |
| `VL_INDICADOR_REND_2015` | STRING | Indicador de rendimento médio (fluxo escolar) calculado para o IDEB no ano de 2015. |
| `VL_APROVACAO_2017_SI_4` | STRING | Taxa de aprovação escolar para séries iniciais/finais sem informação específica de série no ano de 2017 (de 0 a 100). |
| `VL_APROVACAO_2017_1` | STRING | Taxa de aprovação escolar no 1º ano/série do segmento no ano de 2017 (de 0 a 100). |
| `VL_APROVACAO_2017_2` | STRING | Taxa de aprovação escolar no 2º ano/série do segmento no ano de 2017 (de 0 a 100). |
| `VL_APROVACAO_2017_3` | STRING | Taxa de aprovação escolar no 3º ano/série do segmento no ano de 2017 (de 0 a 100). |
| `VL_APROVACAO_2017_4` | STRING | Taxa de aprovação escolar no 4º ano/série do segmento no ano de 2017 (de 0 a 100). |
| `VL_INDICADOR_REND_2017` | STRING | Indicador de rendimento médio (fluxo escolar) calculado para o IDEB no ano de 2017. |
| `VL_APROVACAO_2019_SI_4` | STRING | Taxa de aprovação escolar para séries iniciais/finais sem informação específica de série no ano de 2019 (de 0 a 100). |
| `VL_APROVACAO_2019_1` | STRING | Taxa de aprovação escolar no 1º ano/série do segmento no ano de 2019 (de 0 a 100). |
| `VL_APROVACAO_2019_2` | STRING | Taxa de aprovação escolar no 2º ano/série do segmento no ano de 2019 (de 0 a 100). |
| `VL_APROVACAO_2019_3` | STRING | Taxa de aprovação escolar no 3º ano/série do segmento no ano de 2019 (de 0 a 100). |
| `VL_APROVACAO_2019_4` | STRING | Taxa de aprovação escolar no 4º ano/série do segmento no ano de 2019 (de 0 a 100). |
| `VL_INDICADOR_REND_2019` | STRING | Indicador de rendimento médio (fluxo escolar) calculado para o IDEB no ano de 2019. |
| `VL_APROVACAO_2021_SI_4` | STRING | Taxa de aprovação escolar para séries iniciais/finais sem informação específica de série no ano de 2021 (de 0 a 100). |
| `VL_APROVACAO_2021_1` | STRING | Taxa de aprovação escolar no 1º ano/série do segmento no ano de 2021 (de 0 a 100). |
| `VL_APROVACAO_2021_2` | STRING | Taxa de aprovação escolar no 2º ano/série do segmento no ano de 2021 (de 0 a 100). |
| `VL_APROVACAO_2021_3` | STRING | Taxa de aprovação escolar no 3º ano/série do segmento no ano de 2021 (de 0 a 100). |
| `VL_APROVACAO_2021_4` | STRING | Taxa de aprovação escolar no 4º ano/série do segmento no ano de 2021 (de 0 a 100). |
| `VL_INDICADOR_REND_2021` | STRING | Indicador de rendimento médio (fluxo escolar) calculado para o IDEB no ano de 2021. |
| `VL_APROVACAO_2023_SI_4` | STRING | Taxa de aprovação escolar para séries iniciais/finais sem informação específica de série no ano de 2023 (de 0 a 100). |
| `VL_APROVACAO_2023_1` | STRING | Taxa de aprovação escolar no 1º ano/série do segmento no ano de 2023 (de 0 a 100). |
| `VL_APROVACAO_2023_2` | STRING | Taxa de aprovação escolar no 2º ano/série do segmento no ano de 2023 (de 0 a 100). |
| `VL_APROVACAO_2023_3` | STRING | Taxa de aprovação escolar no 3º ano/série do segmento no ano de 2023 (de 0 a 100). |
| `VL_APROVACAO_2023_4` | STRING | Taxa de aprovação escolar no 4º ano/série do segmento no ano de 2023 (de 0 a 100). |
| `VL_INDICADOR_REND_2023` | STRING | Indicador de rendimento médio (fluxo escolar) calculado para o IDEB no ano de 2023. |
| `VL_APROVACAO_2025_SI_4` | STRING | Taxa média de aprovação (%) no 1º ao 4º ano/série da etapa em 2025. — descrição gerada por IA. |
| `VL_APROVACAO_2025_1` | STRING | Taxa de aprovação (%) no 1º ano/série da etapa em 2025. — descrição gerada por IA. |
| `VL_APROVACAO_2025_2` | STRING | Taxa de aprovação (%) no 2º ano/série da etapa em 2025. — descrição gerada por IA. |
| `VL_APROVACAO_2025_3` | STRING | Taxa de aprovação (%) no 3º ano/série da etapa em 2025. — descrição gerada por IA. |
| `VL_APROVACAO_2025_4` | STRING | Taxa de aprovação (%) no 4º ano/série da etapa em 2025. — descrição gerada por IA. |
| `VL_INDICADOR_REND_2025` | STRING | Indicador de rendimento escolar médio (P) em 2025. — descrição gerada por IA. |
| `VL_NOTA_MATEMATICA_2005` | STRING | Nota média padronizada em Matemática obtida no SAEB no ano de 2005. |
| `VL_NOTA_PORTUGUES_2005` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB no ano de 2005. |
| `VL_NOTA_MEDIA_2005` | STRING | Nota média padronizada total (proficiência) obtida no SAEB no ano de 2005. |
| `VL_NOTA_MATEMATICA_2007` | STRING | Nota média padronizada em Matemática obtida no SAEB no ano de 2007. |
| `VL_NOTA_PORTUGUES_2007` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB no ano de 2007. |
| `VL_NOTA_MEDIA_2007` | STRING | Nota média padronizada total (proficiência) obtida no SAEB no ano de 2007. |
| `VL_NOTA_MATEMATICA_2009` | STRING | Nota média padronizada em Matemática obtida no SAEB no ano de 2009. |
| `VL_NOTA_PORTUGUES_2009` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB no ano de 2009. |
| `VL_NOTA_MEDIA_2009` | STRING | Nota média padronizada total (proficiência) obtida no SAEB no ano de 2009. |
| `VL_NOTA_MATEMATICA_2011` | STRING | Nota média padronizada em Matemática obtida no SAEB no ano de 2011. |
| `VL_NOTA_PORTUGUES_2011` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB no ano de 2011. |
| `VL_NOTA_MEDIA_2011` | STRING | Nota média padronizada total (proficiência) obtida no SAEB no ano de 2011. |
| `VL_NOTA_MATEMATICA_2013` | STRING | Nota média padronizada em Matemática obtida no SAEB no ano de 2013. |
| `VL_NOTA_PORTUGUES_2013` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB no ano de 2013. |
| `VL_NOTA_MEDIA_2013` | STRING | Nota média padronizada total (proficiência) obtida no SAEB no ano de 2013. |
| `VL_NOTA_MATEMATICA_2015` | STRING | Nota média padronizada em Matemática obtida no SAEB no ano de 2015. |
| `VL_NOTA_PORTUGUES_2015` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB no ano de 2015. |
| `VL_NOTA_MEDIA_2015` | STRING | Nota média padronizada total (proficiência) obtida no SAEB no ano de 2015. |
| `VL_NOTA_MATEMATICA_2017` | STRING | Nota média padronizada em Matemática obtida no SAEB no ano de 2017. |
| `VL_NOTA_PORTUGUES_2017` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB no ano de 2017. |
| `VL_NOTA_MEDIA_2017` | STRING | Nota média padronizada total (proficiência) obtida no SAEB no ano de 2017. |
| `VL_NOTA_MATEMATICA_2019` | STRING | Nota média padronizada em Matemática obtida no SAEB no ano de 2019. |
| `VL_NOTA_PORTUGUES_2019` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB no ano de 2019. |
| `VL_NOTA_MEDIA_2019` | STRING | Nota média padronizada total (proficiência) obtida no SAEB no ano de 2019. |
| `VL_NOTA_MATEMATICA_2021` | STRING | Nota média padronizada em Matemática obtida no SAEB no ano de 2021. |
| `VL_NOTA_PORTUGUES_2021` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB no ano de 2021. |
| `VL_NOTA_MEDIA_2021` | STRING | Nota média padronizada total (proficiência) obtida no SAEB no ano de 2021. |
| `VL_NOTA_MATEMATICA_2023` | STRING | Nota média padronizada em Matemática obtida no SAEB no ano de 2023. |
| `VL_NOTA_PORTUGUES_2023` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB no ano de 2023. |
| `VL_NOTA_MEDIA_2023` | STRING | Nota média padronizada total (proficiência) obtida no SAEB no ano de 2023. |
| `VL_NOTA_MATEMATICA_2025` | STRING | Nota média de proficiência em Matemática no SAEB/Prova Brasil estimada ou obtida em 2025. — descrição gerada por IA. |
| `VL_NOTA_PORTUGUES_2025` | STRING | Nota média de proficiência em Língua Portuguesa no SAEB/Prova Brasil estimada ou obtida em 2025. — descrição gerada por IA. |
| `VL_NOTA_MEDIA_2025` | STRING | Nota média de desempenho padronizada (N) no SAEB em 2025. — descrição gerada por IA. |
| `VL_OBSERVADO_2005` | STRING | Valor observado do IDEB no ano de 2005. |
| `VL_OBSERVADO_2007` | STRING | Valor observado do IDEB no ano de 2007. |
| `VL_OBSERVADO_2009` | STRING | Valor observado do IDEB no ano de 2009. |
| `VL_OBSERVADO_2011` | STRING | Valor observado do IDEB no ano de 2011. |
| `VL_OBSERVADO_2013` | STRING | Valor observado do IDEB no ano de 2013. |
| `VL_OBSERVADO_2015` | STRING | Valor observado do IDEB no ano de 2015. |
| `VL_OBSERVADO_2017` | STRING | Valor observado do IDEB no ano de 2017. |
| `VL_OBSERVADO_2019` | STRING | Valor observado do IDEB no ano de 2019. |
| `VL_OBSERVADO_2021` | STRING | Valor observado do IDEB no ano de 2021. |
| `VL_OBSERVADO_2023` | STRING | Valor observado do IDEB no ano de 2023. |
| `VL_OBSERVADO_2025` | STRING | Valor observado do IDEB no ano de 2025. — descrição gerada por IA. |
| `VL_PROJECAO_2007` | STRING | Meta projetada do IDEB para o ano de 2007. |
| `VL_PROJECAO_2009` | STRING | Meta projetada do IDEB para o ano de 2009. |
| `VL_PROJECAO_2011` | STRING | Meta projetada do IDEB para o ano de 2011. |
| `VL_PROJECAO_2013` | STRING | Meta projetada do IDEB para o ano de 2013. |
| `VL_PROJECAO_2015` | STRING | Meta projetada do IDEB para o ano de 2015. |
| `VL_PROJECAO_2017` | STRING | Meta projetada do IDEB para o ano de 2017. |
| `VL_PROJECAO_2019` | STRING | Meta projetada do IDEB para o ano de 2019. |
| `VL_PROJECAO_2021` | STRING | Meta projetada do IDEB para o ano de 2021. |
| `nivel` | STRING | Etapa de ensino avaliada (ex: anos_iniciais, anos_finais, ensino_medio). |
| `dt_ingestao_lake` | STRING | Data e hora do registro da carga dos dados no Data Lake (timestamp ISO-8601). — descrição gerada por IA. |

## raw · inep_ideb_regioes_ufs_anos_iniciais

File `raw__inep_ideb_regioes_ufs_anos_iniciais.parquet` · 142 rows · 133 columns

Tabela histórica consolidada com indicadores do IDEB (Índice de Desenvolvimento da Educação Básica), incluindo taxas de aprovação por série, notas médias do SAEB (Matemática e Língua Portuguesa), indicador de rendimento e metas projetadas, segmentados por unidade geográfica, rede de ensino e nível escolar.

**Feeds:** `trusted/inep_ideb_regioes_ufs`

| Column | Type | Description |
|---|---|---|
| `unidade_geografica` | STRING | Nome ou código identificador da unidade geográfica analisada (ex: escola, município ou estado). |
| `rede` | STRING | Rede de ensino à qual a escola ou região pertence (ex: municipal, estadual, federal, privada ou pública). |
| `VL_APROVACAO_2005_SI_4` | STRING | Taxa de aprovação para turmas sem informação de série (4ª série/5º ano) no ano de 2005. |
| `VL_APROVACAO_2005_SI` | STRING | Taxa de aprovação para turmas sem informação de série no ano de 2005. |
| `VL_APROVACAO_2005_1` | STRING | Taxa de aprovação no 1º ano/série do ensino fundamental no ano de 2005. |
| `VL_APROVACAO_2005_2` | STRING | Taxa de aprovação no 2º ano/série do ensino fundamental no ano de 2005. |
| `VL_APROVACAO_2005_3` | STRING | Taxa de aprovação no 3º ano/série do ensino fundamental no ano de 2005. |
| `VL_APROVACAO_2005_4` | STRING | Taxa de aprovação no 4º ano/série do ensino fundamental no ano de 2005. |
| `VL_INDICADOR_REND_2005` | STRING | Indicador de rendimento escolar (fluxo) calculado para o IDEB no ano de 2005. |
| `VL_APROVACAO_2007_SI_4` | STRING | Taxa de aprovação para turmas sem informação de série (4ª série/5º ano) no ano de 2007. |
| `VL_APROVACAO_2007_SI` | STRING | Taxa de aprovação para turmas sem informação de série no ano de 2007. |
| `VL_APROVACAO_2007_1` | STRING | Taxa de aprovação no 1º ano/série do ensino fundamental no ano de 2007. |
| `VL_APROVACAO_2007_2` | STRING | Taxa de aprovação no 2º ano/série do ensino fundamental no ano de 2007. |
| `VL_APROVACAO_2007_3` | STRING | Taxa de aprovação no 3º ano/série do ensino fundamental no ano de 2007. |
| `VL_APROVACAO_2007_4` | STRING | Taxa de aprovação no 4º ano/série do ensino fundamental no ano de 2007. |
| `VL_INDICADOR_REND_2007` | STRING | Indicador de rendimento escolar (fluxo) calculado para o IDEB no ano de 2007. |
| `VL_APROVACAO_2009_SI_4` | STRING | Taxa de aprovação para turmas sem informação de série (4ª série/5º ano) no ano de 2009. |
| `VL_APROVACAO_2009_SI` | STRING | Taxa de aprovação para turmas sem informação de série no ano de 2009. |
| `VL_APROVACAO_2009_1` | STRING | Taxa de aprovação no 1º ano/série do ensino fundamental no ano de 2009. |
| `VL_APROVACAO_2009_2` | STRING | Taxa de aprovação no 2º ano/série do ensino fundamental no ano de 2009. |
| `VL_APROVACAO_2009_3` | STRING | Taxa de aprovação no 3º ano/série do ensino fundamental no ano de 2009. |
| `VL_APROVACAO_2009_4` | STRING | Taxa de aprovação no 4º ano/série do ensino fundamental no ano de 2009. |
| `VL_INDICADOR_REND_2009` | STRING | Indicador de rendimento escolar (fluxo) calculado para o IDEB no ano de 2009. |
| `VL_APROVACAO_2011_SI_4` | STRING | Taxa de aprovação para turmas sem informação de série (4ª série/5º ano) no ano de 2011. |
| `VL_APROVACAO_2011_SI` | STRING | Taxa de aprovação para turmas sem informação de série no ano de 2011. |
| `VL_APROVACAO_2011_1` | STRING | Taxa de aprovação no 1º ano/série do ensino fundamental no ano de 2011. |
| `VL_APROVACAO_2011_2` | STRING | Taxa de aprovação no 2º ano/série do ensino fundamental no ano de 2011. |
| `VL_APROVACAO_2011_3` | STRING | Taxa de aprovação no 3º ano/série do ensino fundamental no ano de 2011. |
| `VL_APROVACAO_2011_4` | STRING | Taxa de aprovação no 4º ano/série do ensino fundamental no ano de 2011. |
| `VL_INDICADOR_REND_2011` | STRING | Indicador de rendimento escolar (fluxo) calculado para o IDEB no ano de 2011. |
| `VL_APROVACAO_2013_SI_4` | STRING | Taxa de aprovação para turmas sem informação de série (4ª série/5º ano) no ano de 2013. |
| `VL_APROVACAO_2013_SI` | STRING | Taxa de aprovação para turmas sem informação de série no ano de 2013. |
| `VL_APROVACAO_2013_1` | STRING | Taxa de aprovação no 1º ano/série do ensino fundamental no ano de 2013. |
| `VL_APROVACAO_2013_2` | STRING | Taxa de aprovação no 2º ano/série do ensino fundamental no ano de 2013. |
| `VL_APROVACAO_2013_3` | STRING | Taxa de aprovação no 3º ano/série do ensino fundamental no ano de 2013. |
| `VL_APROVACAO_2013_4` | STRING | Taxa de aprovação no 4º ano/série do ensino fundamental no ano de 2013. |
| `VL_INDICADOR_REND_2013` | STRING | Indicador de rendimento escolar (fluxo) calculado para o IDEB no ano de 2013. |
| `VL_APROVACAO_2015_SI_4` | STRING | Taxa de aprovação para turmas sem informação de série (4ª série/5º ano) no ano de 2015. |
| `VL_APROVACAO_2015_SI` | STRING | Taxa de aprovação para turmas sem informação de série no ano de 2015. |
| `VL_APROVACAO_2015_1` | STRING | Taxa de aprovação no 1º ano/série do ensino fundamental no ano de 2015. |
| `VL_APROVACAO_2015_2` | STRING | Taxa de aprovação no 2º ano/série do ensino fundamental no ano de 2015. |
| `VL_APROVACAO_2015_3` | STRING | Taxa de aprovação no 3º ano/série do ensino fundamental no ano de 2015. |
| `VL_APROVACAO_2015_4` | STRING | Taxa de aprovação no 4º ano/série do ensino fundamental no ano de 2015. |
| `VL_INDICADOR_REND_2015` | STRING | Indicador de rendimento escolar (fluxo) calculado para o IDEB no ano de 2015. |
| `VL_APROVACAO_2017_SI_4` | STRING | Taxa de aprovação para turmas sem informação de série (4ª série/5º ano) no ano de 2017. |
| `VL_APROVACAO_2017_SI` | STRING | Taxa de aprovação para turmas sem informação de série no ano de 2017. |
| `VL_APROVACAO_2017_1` | STRING | Taxa de aprovação no 1º ano/série do ensino fundamental no ano de 2017. |
| `VL_APROVACAO_2017_2` | STRING | Taxa de aprovação no 2º ano/série do ensino fundamental no ano de 2017. |
| `VL_APROVACAO_2017_3` | STRING | Taxa de aprovação no 3º ano/série do ensino fundamental no ano de 2017. |
| `VL_APROVACAO_2017_4` | STRING | Taxa de aprovação no 4º ano/série do ensino fundamental no ano de 2017. |
| `VL_INDICADOR_REND_2017` | STRING | Indicador de rendimento escolar (fluxo) calculado para o IDEB no ano de 2017. |
| `VL_APROVACAO_2019_SI_4` | STRING | Taxa de aprovação para turmas sem informação de série (4ª série/5º ano) no ano de 2019. |
| `VL_APROVACAO_2019_SI` | STRING | Taxa de aprovação para turmas sem informação de série no ano de 2019. |
| `VL_APROVACAO_2019_1` | STRING | Taxa de aprovação no 1º ano/série do ensino fundamental no ano de 2019. |
| `VL_APROVACAO_2019_2` | STRING | Taxa de aprovação no 2º ano/série do ensino fundamental no ano de 2019. |
| `VL_APROVACAO_2019_3` | STRING | Taxa de aprovação no 3º ano/série do ensino fundamental no ano de 2019. |
| `VL_APROVACAO_2019_4` | STRING | Taxa de aprovação no 4º ano/série do ensino fundamental no ano de 2019. |
| `VL_INDICADOR_REND_2019` | STRING | Indicador de rendimento escolar (fluxo) calculado para o IDEB no ano de 2019. |
| `VL_APROVACAO_2021_SI_4` | STRING | Taxa de aprovação para turmas sem informação de série (4ª série/5º ano) no ano de 2021. |
| `VL_APROVACAO_2021_SI` | STRING | Taxa de aprovação para turmas sem informação de série no ano de 2021. |
| `VL_APROVACAO_2021_1` | STRING | Taxa de aprovação no 1º ano/série do ensino fundamental no ano de 2021. |
| `VL_APROVACAO_2021_2` | STRING | Taxa de aprovação no 2º ano/série do ensino fundamental no ano de 2021. |
| `VL_APROVACAO_2021_3` | STRING | Taxa de aprovação no 3º ano/série do ensino fundamental no ano de 2021. |
| `VL_APROVACAO_2021_4` | STRING | Taxa de aprovação no 4º ano/série do ensino fundamental no ano de 2021. |
| `VL_INDICADOR_REND_2021` | STRING | Indicador de rendimento escolar (fluxo) calculado para o IDEB no ano de 2021. |
| `VL_APROVACAO_2023_SI_4` | STRING | Taxa de aprovação para turmas sem informação de série (4ª série/5º ano) no ano de 2023. |
| `VL_APROVACAO_2023_SI` | STRING | Taxa de aprovação para turmas sem informação de série no ano de 2023. |
| `VL_APROVACAO_2023_1` | STRING | Taxa de aprovação no 1º ano/série do ensino fundamental no ano de 2023. |
| `VL_APROVACAO_2023_2` | STRING | Taxa de aprovação no 2º ano/série do ensino fundamental no ano de 2023. |
| `VL_APROVACAO_2023_3` | STRING | Taxa de aprovação no 3º ano/série do ensino fundamental no ano de 2023. |
| `VL_APROVACAO_2023_4` | STRING | Taxa de aprovação no 4º ano/série do ensino fundamental no ano de 2023. |
| `VL_INDICADOR_REND_2023` | STRING | Indicador de rendimento escolar (fluxo) calculado para o IDEB no ano de 2023. |
| `VL_APROVACAO_2025_SI_4` | STRING | Taxa média de aprovação (%) das Séries Iniciais (1º ao 4º/5º ano) em 2025. — descrição gerada por IA. |
| `VL_APROVACAO_2025_SI` | STRING | Taxa média geral de aprovação (%) das Séries Iniciais em 2025. — descrição gerada por IA. |
| `VL_APROVACAO_2025_1` | STRING | Taxa de aprovação (%) no 1º ano em 2025. — descrição gerada por IA. |
| `VL_APROVACAO_2025_2` | STRING | Taxa de aprovação (%) no 2º ano em 2025. — descrição gerada por IA. |
| `VL_APROVACAO_2025_3` | STRING | Taxa de aprovação (%) no 3º ano em 2025. — descrição gerada por IA. |
| `VL_APROVACAO_2025_4` | STRING | Taxa de aprovação (%) no 4º ano em 2025. — descrição gerada por IA. |
| `VL_INDICADOR_REND_2025` | STRING | Indicador de rendimento escolar (P-bar, de 0 a 1) do INEP projetado/calculado para 2025. — descrição gerada por IA. |
| `VL_NOTA_MATEMATICA_2005` | STRING | Nota média padronizada em Matemática obtida no SAEB no ano de 2005. |
| `VL_NOTA_PORTUGUES_2005` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB no ano de 2005. |
| `VL_NOTA_MEDIA_2005` | STRING | Nota média padronizada geral (proficiência) obtida no SAEB no ano de 2005. |
| `VL_NOTA_MATEMATICA_2007` | STRING | Nota média padronizada em Matemática obtida no SAEB no ano de 2007. |
| `VL_NOTA_PORTUGUES_2007` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB no ano de 2007. |
| `VL_NOTA_MEDIA_2007` | STRING | Nota média padronizada geral (proficiência) obtida no SAEB no ano de 2007. |
| `VL_NOTA_MATEMATICA_2009` | STRING | Nota média padronizada em Matemática obtida no SAEB no ano de 2009. |
| `VL_NOTA_PORTUGUES_2009` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB no ano de 2009. |
| `VL_NOTA_MEDIA_2009` | STRING | Nota média padronizada geral (proficiência) obtida no SAEB no ano de 2009. |
| `VL_NOTA_MATEMATICA_2011` | STRING | Nota média padronizada em Matemática obtida no SAEB no ano de 2011. |
| `VL_NOTA_PORTUGUES_2011` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB no ano de 2011. |
| `VL_NOTA_MEDIA_2011` | STRING | Nota média padronizada geral (proficiência) obtida no SAEB no ano de 2011. |
| `VL_NOTA_MATEMATICA_2013` | STRING | Nota média padronizada em Matemática obtida no SAEB no ano de 2013. |
| `VL_NOTA_PORTUGUES_2013` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB no ano de 2013. |
| `VL_NOTA_MEDIA_2013` | STRING | Nota média padronizada geral (proficiência) obtida no SAEB no ano de 2013. |
| `VL_NOTA_MATEMATICA_2015` | STRING | Nota média padronizada em Matemática obtida no SAEB no ano de 2015. |
| `VL_NOTA_PORTUGUES_2015` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB no ano de 2015. |
| `VL_NOTA_MEDIA_2015` | STRING | Nota média padronizada geral (proficiência) obtida no SAEB no ano de 2015. |
| `VL_NOTA_MATEMATICA_2017` | STRING | Nota média padronizada em Matemática obtida no SAEB no ano de 2017. |
| `VL_NOTA_PORTUGUES_2017` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB no ano de 2017. |
| `VL_NOTA_MEDIA_2017` | STRING | Nota média padronizada geral (proficiência) obtida no SAEB no ano de 2017. |
| `VL_NOTA_MATEMATICA_2019` | STRING | Nota média padronizada em Matemática obtida no SAEB no ano de 2019. |
| `VL_NOTA_PORTUGUES_2019` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB no ano de 2019. |
| `VL_NOTA_MEDIA_2019` | STRING | Nota média padronizada geral (proficiência) obtida no SAEB no ano de 2019. |
| `VL_NOTA_MATEMATICA_2021` | STRING | Nota média padronizada em Matemática obtida no SAEB no ano de 2021. |
| `VL_NOTA_PORTUGUES_2021` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB no ano de 2021. |
| `VL_NOTA_MEDIA_2021` | STRING | Nota média padronizada geral (proficiência) obtida no SAEB no ano de 2021. |
| `VL_NOTA_MATEMATICA_2023` | STRING | Nota média padronizada em Matemática obtida no SAEB no ano de 2023. |
| `VL_NOTA_PORTUGUES_2023` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB no ano de 2023. |
| `VL_NOTA_MEDIA_2023` | STRING | Nota média padronizada geral (proficiência) obtida no SAEB no ano de 2023. |
| `VL_NOTA_MATEMATICA_2025` | STRING | Nota média padronizada em Matemática no SAEB em 2025. — descrição gerada por IA. |
| `VL_NOTA_PORTUGUES_2025` | STRING | Nota média padronizada em Língua Portuguesa no SAEB em 2025. — descrição gerada por IA. |
| `VL_NOTA_MEDIA_2025` | STRING | Nota média padronizada padronizada total (N) no SAEB em 2025. — descrição gerada por IA. |
| `VL_OBSERVADO_2005` | STRING | Valor observado do índice do IDEB obtido no ano de 2005. |
| `VL_OBSERVADO_2007` | STRING | Valor observado do índice do IDEB obtido no ano de 2007. |
| `VL_OBSERVADO_2009` | STRING | Valor observado do índice do IDEB obtido no ano de 2009. |
| `VL_OBSERVADO_2011` | STRING | Valor observado do índice do IDEB obtido no ano de 2011. |
| `VL_OBSERVADO_2013` | STRING | Valor observado do índice do IDEB obtido no ano de 2013. |
| `VL_OBSERVADO_2015` | STRING | Valor observado do índice do IDEB obtido no ano de 2015. |
| `VL_OBSERVADO_2017` | STRING | Valor observado do índice do IDEB obtido no ano de 2017. |
| `VL_OBSERVADO_2019` | STRING | Valor observado do índice do IDEB obtido no ano de 2019. |
| `VL_OBSERVADO_2021` | STRING | Valor observado do índice do IDEB obtido no ano de 2021. |
| `VL_OBSERVADO_2023` | STRING | Valor observado do índice do IDEB obtido no ano de 2023. |
| `VL_OBSERVADO_2025` | STRING | Valor do índice IDEB observado em 2025 (escala de 0 a 10). — descrição gerada por IA. |
| `VL_PROJECAO_2007` | STRING | Meta projetada do IDEB para o ano de 2007. |
| `VL_PROJECAO_2009` | STRING | Meta projetada do IDEB para o ano de 2009. |
| `VL_PROJECAO_2011` | STRING | Meta projetada do IDEB para o ano de 2011. |
| `VL_PROJECAO_2013` | STRING | Meta projetada do IDEB para o ano de 2013. |
| `VL_PROJECAO_2015` | STRING | Meta projetada do IDEB para o ano de 2015. |
| `VL_PROJECAO_2017` | STRING | Meta projetada do IDEB para o ano de 2017. |
| `VL_PROJECAO_2019` | STRING | Meta projetada do IDEB para o ano de 2019. |
| `VL_PROJECAO_2021` | STRING | Meta projetada do IDEB para o ano de 2021. |
| `nivel` | STRING | Etapa ou nível de ensino avaliado (ex: anos_iniciais, anos_finais). |
| `dt_ingestao_lake` | STRING | Data e hora de ingestão do registro no Data Lake (formato ISO 8601). — descrição gerada por IA. |

## raw · inep_ideb_regioes_ufs_ensino_medio

File `raw__inep_ideb_regioes_ufs_ensino_medio.parquet` · 109 rows · 122 columns

Tabela histórica consolidada do IDEB (Índice de Desenvolvimento da Educação Básica) que reúne taxas de aprovação escolar, proficiências do SAEB (Matemática e Português), indicadores de rendimento, notas observadas e metas projetadas de 2005 a 2023, segmentadas por unidade geográfica, rede de ensino e nível escolar.

**Feeds:** `trusted/inep_ideb_regioes_ufs`

| Column | Type | Description |
|---|---|---|
| `unidade_geografica` | STRING | Nome ou identificação da unidade geográfica analisada (ex: estado, município ou escola). |
| `rede` | STRING | Rede de ensino associada (ex: Estadual, Municipal, Federal, Privada, Pública). |
| `VL_APROVACAO_2005_SI_4` | STRING | Taxa de aprovação da série inicial ao 4º ano/série em 2005 (em porcentagem). |
| `VL_APROVACAO_2005_1` | STRING | Taxa de aprovação do 1º ano/série em 2005 (em porcentagem). |
| `VL_APROVACAO_2005_2` | STRING | Taxa de aprovação do 2º ano/série em 2005 (em porcentagem). |
| `VL_APROVACAO_2005_3` | STRING | Taxa de aprovação do 3º ano/série em 2005 (em porcentagem). |
| `VL_APROVACAO_2005_4` | STRING | Taxa de aprovação do 4º ano/série em 2005 (em porcentagem). |
| `VL_INDICADOR_REND_2005` | STRING | Indicador de rendimento escolar (taxa média de aprovação) para o IDEB de 2005. |
| `VL_APROVACAO_2007_SI_4` | STRING | Taxa de aprovação da série inicial ao 4º ano/série em 2007 (em porcentagem). |
| `VL_APROVACAO_2007_1` | STRING | Taxa de aprovação do 1º ano/série em 2007 (em porcentagem). |
| `VL_APROVACAO_2007_2` | STRING | Taxa de aprovação do 2º ano/série em 2007 (em porcentagem). |
| `VL_APROVACAO_2007_3` | STRING | Taxa de aprovação do 3º ano/série em 2007 (em porcentagem). |
| `VL_APROVACAO_2007_4` | STRING | Taxa de aprovação do 4º ano/série em 2007 (em porcentagem). |
| `VL_INDICADOR_REND_2007` | STRING | Indicador de rendimento escolar (taxa média de aprovação) para o IDEB de 2007. |
| `VL_APROVACAO_2009_SI_4` | STRING | Taxa de aprovação da série inicial ao 4º ano/série em 2009 (em porcentagem). |
| `VL_APROVACAO_2009_1` | STRING | Taxa de aprovação do 1º ano/série em 2009 (em porcentagem). |
| `VL_APROVACAO_2009_2` | STRING | Taxa de aprovação do 2º ano/série em 2009 (em porcentagem). |
| `VL_APROVACAO_2009_3` | STRING | Taxa de aprovação do 3º ano/série em 2009 (em porcentagem). |
| `VL_APROVACAO_2009_4` | STRING | Taxa de aprovação do 4º ano/série em 2009 (em porcentagem). |
| `VL_INDICADOR_REND_2009` | STRING | Indicador de rendimento escolar (taxa média de aprovação) para o IDEB de 2009. |
| `VL_APROVACAO_2011_SI_4` | STRING | Taxa de aprovação da série inicial ao 4º ano/série em 2011 (em porcentagem). |
| `VL_APROVACAO_2011_1` | STRING | Taxa de aprovação do 1º ano/série em 2011 (em porcentagem). |
| `VL_APROVACAO_2011_2` | STRING | Taxa de aprovação do 2º ano/série em 2011 (em porcentagem). |
| `VL_APROVACAO_2011_3` | STRING | Taxa de aprovação do 3º ano/série em 2011 (em porcentagem). |
| `VL_APROVACAO_2011_4` | STRING | Taxa de aprovação do 4º ano/série em 2011 (em porcentagem). |
| `VL_INDICADOR_REND_2011` | STRING | Indicador de rendimento escolar (taxa média de aprovação) para o IDEB de 2011. |
| `VL_APROVACAO_2013_SI_4` | STRING | Taxa de aprovação da série inicial ao 4º ano/série em 2013 (em porcentagem). |
| `VL_APROVACAO_2013_1` | STRING | Taxa de aprovação do 1º ano/série em 2013 (em porcentagem). |
| `VL_APROVACAO_2013_2` | STRING | Taxa de aprovação do 2º ano/série em 2013 (em porcentagem). |
| `VL_APROVACAO_2013_3` | STRING | Taxa de aprovação do 3º ano/série em 2013 (em porcentagem). |
| `VL_APROVACAO_2013_4` | STRING | Taxa de aprovação do 4º ano/série em 2013 (em porcentagem). |
| `VL_INDICADOR_REND_2013` | STRING | Indicador de rendimento escolar (taxa média de aprovação) para o IDEB de 2013. |
| `VL_APROVACAO_2015_SI_4` | STRING | Taxa de aprovação da série inicial ao 4º ano/série em 2015 (em porcentagem). |
| `VL_APROVACAO_2015_1` | STRING | Taxa de aprovação do 1º ano/série em 2015 (em porcentagem). |
| `VL_APROVACAO_2015_2` | STRING | Taxa de aprovação do 2º ano/série em 2015 (em porcentagem). |
| `VL_APROVACAO_2015_3` | STRING | Taxa de aprovação do 3º ano/série em 2015 (em porcentagem). |
| `VL_APROVACAO_2015_4` | STRING | Taxa de aprovação do 4º ano/série em 2015 (em porcentagem). |
| `VL_INDICADOR_REND_2015` | STRING | Indicador de rendimento escolar (taxa média de aprovação) para o IDEB de 2015. |
| `VL_APROVACAO_2017_SI_4` | STRING | Taxa de aprovação da série inicial ao 4º ano/série em 2017 (em porcentagem). |
| `VL_APROVACAO_2017_1` | STRING | Taxa de aprovação do 1º ano/série em 2017 (em porcentagem). |
| `VL_APROVACAO_2017_2` | STRING | Taxa de aprovação do 2º ano/série em 2017 (em porcentagem). |
| `VL_APROVACAO_2017_3` | STRING | Taxa de aprovação do 3º ano/série em 2017 (em porcentagem). |
| `VL_APROVACAO_2017_4` | STRING | Taxa de aprovação do 4º ano/série em 2017 (em porcentagem). |
| `VL_INDICADOR_REND_2017` | STRING | Indicador de rendimento escolar (taxa média de aprovação) para o IDEB de 2017. |
| `VL_APROVACAO_2019_SI_4` | STRING | Taxa de aprovação da série inicial ao 4º ano/série em 2019 (em porcentagem). |
| `VL_APROVACAO_2019_1` | STRING | Taxa de aprovação do 1º ano/série em 2019 (em porcentagem). |
| `VL_APROVACAO_2019_2` | STRING | Taxa de aprovação do 2º ano/série em 2019 (em porcentagem). |
| `VL_APROVACAO_2019_3` | STRING | Taxa de aprovação do 3º ano/série em 2019 (em porcentagem). |
| `VL_APROVACAO_2019_4` | STRING | Taxa de aprovação do 4º ano/série em 2019 (em porcentagem). |
| `VL_INDICADOR_REND_2019` | STRING | Indicador de rendimento escolar (taxa média de aprovação) para o IDEB de 2019. |
| `VL_APROVACAO_2021_SI_4` | STRING | Taxa de aprovação da série inicial ao 4º ano/série em 2021 (em porcentagem). |
| `VL_APROVACAO_2021_1` | STRING | Taxa de aprovação do 1º ano/série em 2021 (em porcentagem). |
| `VL_APROVACAO_2021_2` | STRING | Taxa de aprovação do 2º ano/série em 2021 (em porcentagem). |
| `VL_APROVACAO_2021_3` | STRING | Taxa de aprovação do 3º ano/série em 2021 (em porcentagem). |
| `VL_APROVACAO_2021_4` | STRING | Taxa de aprovação do 4º ano/série em 2021 (em porcentagem). |
| `VL_INDICADOR_REND_2021` | STRING | Indicador de rendimento escolar (taxa média de aprovação) para o IDEB de 2021. |
| `VL_APROVACAO_2023_SI_4` | STRING | Taxa de aprovação da série inicial ao 4º ano/série em 2023 (em porcentagem). |
| `VL_APROVACAO_2023_1` | STRING | Taxa de aprovação do 1º ano/série em 2023 (em porcentagem). |
| `VL_APROVACAO_2023_2` | STRING | Taxa de aprovação do 2º ano/série em 2023 (em porcentagem). |
| `VL_APROVACAO_2023_3` | STRING | Taxa de aprovação do 3º ano/série em 2023 (em porcentagem). |
| `VL_APROVACAO_2023_4` | STRING | Taxa de aprovação do 4º ano/série em 2023 (em porcentagem). |
| `VL_INDICADOR_REND_2023` | STRING | Indicador de rendimento escolar (taxa média de aprovação) para o IDEB de 2023. |
| `VL_APROVACAO_2025_SI_4` | STRING | Taxa de aprovação média do indicador do ano 2025 (0 a 100%). — descrição gerada por IA. |
| `VL_APROVACAO_2025_1` | STRING | Taxa de aprovação na 1ª série/ano do nível de ensino no ano de 2025 (0 a 100%). — descrição gerada por IA. |
| `VL_APROVACAO_2025_2` | STRING | Taxa de aprovação na 2ª série/ano do nível de ensino no ano de 2025 (0 a 100%). — descrição gerada por IA. |
| `VL_APROVACAO_2025_3` | STRING | Taxa de aprovação na 3ª série/ano do nível de ensino no ano de 2025 (0 a 100%). — descrição gerada por IA. |
| `VL_APROVACAO_2025_4` | STRING | Taxa de aprovação na 4ª série/ano do nível de ensino no ano de 2025 (0 a 100%). — descrição gerada por IA. |
| `VL_INDICADOR_REND_2025` | STRING | Indicador de rendimento escolar do IDEB (fluxo escolar) para o ano de 2025 (valor de 0 a 1). — descrição gerada por IA. |
| `VL_NOTA_MATEMATICA_2005` | STRING | Nota média padronizada em Matemática obtida no SAEB em 2005. |
| `VL_NOTA_PORTUGUES_2005` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB em 2005. |
| `VL_NOTA_MEDIA_2005` | STRING | Nota média padronizada total (proficiência) obtida no SAEB em 2005. |
| `VL_NOTA_MATEMATICA_2007` | STRING | Nota média padronizada em Matemática obtida no SAEB em 2007. |
| `VL_NOTA_PORTUGUES_2007` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB em 2007. |
| `VL_NOTA_MEDIA_2007` | STRING | Nota média padronizada total (proficiência) obtida no SAEB em 2007. |
| `VL_NOTA_MATEMATICA_2009` | STRING | Nota média padronizada em Matemática obtida no SAEB em 2009. |
| `VL_NOTA_PORTUGUES_2009` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB em 2009. |
| `VL_NOTA_MEDIA_2009` | STRING | Nota média padronizada total (proficiência) obtida no SAEB em 2009. |
| `VL_NOTA_MATEMATICA_2011` | STRING | Nota média padronizada em Matemática obtida no SAEB em 2011. |
| `VL_NOTA_PORTUGUES_2011` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB em 2011. |
| `VL_NOTA_MEDIA_2011` | STRING | Nota média padronizada total (proficiência) obtida no SAEB em 2011. |
| `VL_NOTA_MATEMATICA_2013` | STRING | Nota média padronizada em Matemática obtida no SAEB em 2013. |
| `VL_NOTA_PORTUGUES_2013` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB em 2013. |
| `VL_NOTA_MEDIA_2013` | STRING | Nota média padronizada total (proficiência) obtida no SAEB em 2013. |
| `VL_NOTA_MATEMATICA_2015` | STRING | Nota média padronizada em Matemática obtida no SAEB em 2015. |
| `VL_NOTA_PORTUGUES_2015` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB em 2015. |
| `VL_NOTA_MEDIA_2015` | STRING | Nota média padronizada total (proficiência) obtida no SAEB em 2015. |
| `VL_NOTA_MATEMATICA_2017` | STRING | Nota média padronizada em Matemática obtida no SAEB em 2017. |
| `VL_NOTA_PORTUGUES_2017` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB em 2017. |
| `VL_NOTA_MEDIA_2017` | STRING | Nota média padronizada total (proficiência) obtida no SAEB em 2017. |
| `VL_NOTA_MATEMATICA_2019` | STRING | Nota média padronizada em Matemática obtida no SAEB em 2019. |
| `VL_NOTA_PORTUGUES_2019` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB em 2019. |
| `VL_NOTA_MEDIA_2019` | STRING | Nota média padronizada total (proficiência) obtida no SAEB em 2019. |
| `VL_NOTA_MATEMATICA_2021` | STRING | Nota média padronizada em Matemática obtida no SAEB em 2021. |
| `VL_NOTA_PORTUGUES_2021` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB em 2021. |
| `VL_NOTA_MEDIA_2021` | STRING | Nota média padronizada total (proficiência) obtida no SAEB em 2021. |
| `VL_NOTA_MATEMATICA_2023` | STRING | Nota média padronizada em Matemática obtida no SAEB em 2023. |
| `VL_NOTA_PORTUGUES_2023` | STRING | Nota média padronizada em Língua Portuguesa obtida no SAEB em 2023. |
| `VL_NOTA_MEDIA_2023` | STRING | Nota média padronizada total (proficiência) obtida no SAEB em 2023. |
| `VL_NOTA_MATEMATICA_2025` | STRING | Nota média padronizada projetada/estimada no exame do SAEB em Matemática no ano de 2025. — descrição gerada por IA. |
| `VL_NOTA_PORTUGUES_2025` | STRING | Nota média padronizada projetada/estimada no exame do SAEB em Língua Portuguesa no ano de 2025. — descrição gerada por IA. |
| `VL_NOTA_MEDIA_2025` | STRING | Nota média padronizada projetada/estimada entre Português e Matemática no ano de 2025. — descrição gerada por IA. |
| `VL_OBSERVADO_2005` | STRING | Valor observado do IDEB no ano de 2005. |
| `VL_OBSERVADO_2007` | STRING | Valor observado do IDEB no ano de 2007. |
| `VL_OBSERVADO_2009` | STRING | Valor observado do IDEB no ano de 2009. |
| `VL_OBSERVADO_2011` | STRING | Valor observado do IDEB no ano de 2011. |
| `VL_OBSERVADO_2013` | STRING | Valor observado do IDEB no ano de 2013. |
| `VL_OBSERVADO_2015` | STRING | Valor observado do IDEB no ano de 2015. |
| `VL_OBSERVADO_2017` | STRING | Valor observado do IDEB no ano de 2017. |
| `VL_OBSERVADO_2019` | STRING | Valor observado do IDEB no ano de 2019. |
| `VL_OBSERVADO_2021` | STRING | Valor observado do IDEB no ano de 2021. |
| `VL_OBSERVADO_2023` | STRING | Valor observado do IDEB no ano de 2023. |
| `VL_OBSERVADO_2025` | STRING | Valor do IDEB observado ou estimativa final acumulada para o ano de 2025 (escala de 0 a 10). — descrição gerada por IA. |
| `VL_PROJECAO_2007` | STRING | Meta projetada do IDEB para o ano de 2007. |
| `VL_PROJECAO_2009` | STRING | Meta projetada do IDEB para o ano de 2009. |
| `VL_PROJECAO_2011` | STRING | Meta projetada do IDEB para o ano de 2011. |
| `VL_PROJECAO_2013` | STRING | Meta projetada do IDEB para o ano de 2013. |
| `VL_PROJECAO_2015` | STRING | Meta projetada do IDEB para o ano de 2015. |
| `VL_PROJECAO_2017` | STRING | Meta projetada do IDEB para o ano de 2017. |
| `VL_PROJECAO_2019` | STRING | Meta projetada do IDEB para o ano de 2019. |
| `VL_PROJECAO_2021` | STRING | Meta projetada do IDEB para o ano de 2021. |
| `nivel` | STRING | Nível de ensino avaliado (ex: anos_iniciais, anos_finais, ensino_medio). |
| `dt_ingestao_lake` | STRING | Data e hora em que o registro foi ingerido na camada do Data Lake (formato ISO timestamp). — descrição gerada por IA. |

## trusted · inep_ideb_brasil

File `trusted__inep_ideb_brasil.parquet` · 154 rows · 13 columns

IDEB nivel Brasil — uma linha por (nivel, ano, rede). EF Anos Iniciais e Anos Finais: 2005-2023 (bienal). Ensino Medio: 2005-2023. Inclui nota SAEB (matematica, portugues, media), IDEB observado e meta projetada. Fonte: raw_zone.inep_ideb_brasil_anos_iniciais, _anos_finais, _ensino_medio.

**Built from:** `raw/inep_ideb_brasil_anos_finais`, `raw/inep_ideb_brasil_anos_iniciais`, `raw/inep_ideb_brasil_ensino_medio`

**Feeds:** `semantic/obt_inep_ideb_brasil_ano`

| Column | Type | Description |
|---|---|---|
| `nivel` | STRING | Nivel educacional: anos_iniciais (1-5 EF), anos_finais (6-9 EF), ensino_medio. |
| `ano` | INTEGER | Ano de referencia do IDEB (bienal: 2005, 2007, ..., 2023). |
| `abrangencia` | STRING | Sempre 'Brasil' — identificador geografico do arquivo INEP. |
| `rede` | STRING | Dependencia administrativa: Total, Publica, Federal, Estadual, Municipal, Privada. |
| `taxa_aprovacao_total` | FLOAT | Taxa de aprovacao media do fluxo escolar (%). Componente P do IDEB. |
| `taxa_aprovacao_serie1` | FLOAT | Taxa de aprovacao na 1 serie do nivel (%). Disponivel apenas para anos_iniciais. |
| `indicador_rendimento` | FLOAT | Indicador de rendimento P (0 a 1): media harmonica das taxas de aprovacao por serie. |
| `nota_matematica` | FLOAT | Nota SAEB media em Matematica (escala SAEB). Componente N do IDEB. |
| `nota_portugues` | FLOAT | Nota SAEB media em Lingua Portuguesa (escala SAEB). Componente N do IDEB. |
| `nota_media` | FLOAT | Nota SAEB media padronizada combinada LP e Mat. Componente N do IDEB. |
| `ideb_observado` | FLOAT | IDEB observado = N x P (escala 0-10). NULL se dado insuficiente. |
| `meta_projecao` | FLOAT | Meta IDEB projetada pelo MEC para este ano e nivel. NULL em 2005 e 2023. |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC de geracao deste registro na camada trusted. |

## trusted · inep_ideb_escola

File `trusted__inep_ideb_escola.parquet` · 1,366,823 rows · 21 columns

IDEB por escola. EF: 2005-2025. EM: 2017-2025.

**Built from:** `raw/inep_ideb_escola_anos_finais`, `raw/inep_ideb_escola_anos_iniciais`, `raw/inep_ideb_escola_ensino_medio`

**Feeds:** `semantic/obt_inep_ideb_escola_ano`

| Column | Type | Description |
|---|---|---|
| `nivel` | STRING | Nivel. |
| `ano` | INTEGER | Ano de referencia. |
| `sg_uf` | STRING | Sigla da UF. |
| `co_municipio` | STRING | Codigo IBGE do municipio. |
| `no_municipio` | STRING | Nome do municipio. |
| `id_escola` | STRING | Codigo INEP da escola (8 digitos). |
| `no_escola` | STRING | Nome da escola. |
| `rede` | STRING | Rede de ensino. |
| `taxa_aprovacao_total` | FLOAT | Taxa / percentual (%). |
| `taxa_aprovacao_serie1_ai` | FLOAT | Taxa / percentual (%). |
| `taxa_aprovacao_serie2` | FLOAT | Taxa / percentual (%). |
| `taxa_aprovacao_serie3` | FLOAT | Taxa / percentual (%). |
| `taxa_aprovacao_serie4` | FLOAT | Taxa / percentual (%). |
| `taxa_aprovacao_serie5` | FLOAT | Taxa / percentual (%). |
| `indicador_rendimento` | FLOAT | Indicador rendimento. |
| `nota_matematica` | FLOAT | Nota matematica. |
| `nota_portugues` | FLOAT | Nota portugues. |
| `nota_media` | FLOAT | Nota media. |
| `ideb_observado` | FLOAT | Ideb observado. |
| `meta_projecao` | FLOAT | Meta projecao. |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC da carga no lake. |

## trusted · inep_ideb_municipio

File `trusted__inep_ideb_municipio.parquet` · 377,396 rows · 19 columns

IDEB por municipio. EF: 2005-2025. EM: 2017-2025.

**Built from:** `raw/inep_ideb_municipio_anos_finais`, `raw/inep_ideb_municipio_anos_iniciais`, `raw/inep_ideb_municipio_ensino_medio`

**Feeds:** `semantic/obt_inep_ideb_municipio_ano`

| Column | Type | Description |
|---|---|---|
| `nivel` | STRING | Nivel. |
| `ano` | INTEGER | Ano de referencia. |
| `sg_uf` | STRING | Sigla da UF. |
| `co_municipio` | STRING | Codigo IBGE do municipio. |
| `no_municipio` | STRING | Nome do municipio. |
| `rede` | STRING | Rede de ensino. |
| `taxa_aprovacao_total` | FLOAT | Taxa / percentual (%). |
| `taxa_aprovacao_serie1_ai` | FLOAT | Taxa / percentual (%). |
| `taxa_aprovacao_serie2` | FLOAT | Taxa / percentual (%). |
| `taxa_aprovacao_serie3` | FLOAT | Taxa / percentual (%). |
| `taxa_aprovacao_serie4` | FLOAT | Taxa / percentual (%). |
| `taxa_aprovacao_serie5` | FLOAT | Taxa / percentual (%). |
| `indicador_rendimento` | FLOAT | Indicador rendimento. |
| `nota_matematica` | FLOAT | Nota matematica. |
| `nota_portugues` | FLOAT | Nota portugues. |
| `nota_media` | FLOAT | Nota media. |
| `ideb_observado` | FLOAT | Ideb observado. |
| `meta_projecao` | FLOAT | Meta projecao. |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC da carga no lake. |

## trusted · inep_ideb_regioes_ufs

File `trusted__inep_ideb_regioes_ufs.parquet` · 3,872 rows · 15 columns

IDEB por regiao geografica e Unidade da Federacao — uma linha por (unidade_geografica, nivel, ano, rede). Inclui 5 regioes (Norte, Nordeste, Sudeste, Sul, Centro-Oeste) e 27 UFs. EF Anos Iniciais, Anos Finais e Ensino Medio: 2005-2023 bienal. Fonte: raw_zone.inep_ideb_regioes_ufs_anos_iniciais, _anos_finais, _ensino_medio.

**Built from:** `raw/inep_ideb_regioes_ufs_anos_finais`, `raw/inep_ideb_regioes_ufs_anos_iniciais`, `raw/inep_ideb_regioes_ufs_ensino_medio`

**Feeds:** `semantic/obt_inep_ideb_regiao_ano`

| Column | Type | Description |
|---|---|---|
| `nivel` | STRING | Nivel educacional: anos_iniciais (1-5 EF), anos_finais (6-9 EF), ensino_medio. |
| `ano` | INTEGER | Ano de referencia do IDEB (bienal: 2005, 2007, ..., 2023). |
| `unidade_geografica` | STRING | Nome da regiao (Norte, Nordeste...) ou nome completo da UF (Sao Paulo, Minas Gerais...). |
| `rede` | STRING | Dependencia administrativa: Total, Publica, Federal, Estadual, Municipal, Privada. |
| `tipo_unidade` | STRING | Tipo da unidade geografica: 'regiao' (5 regioes) ou 'uf' (27 UFs). |
| `sg_uf` | STRING | Sigla da UF (2 letras). NULL para linhas de regioes geograficas. |
| `taxa_aprovacao_total` | FLOAT | Taxa de aprovacao media do fluxo escolar (%). Componente P do IDEB. |
| `taxa_aprovacao_serie1` | FLOAT | Taxa de aprovacao na 1 serie do nivel (%). Disponivel apenas para anos_iniciais. |
| `indicador_rendimento` | FLOAT | Indicador de rendimento P (0 a 1): media harmonica das taxas de aprovacao por serie. |
| `nota_matematica` | FLOAT | Nota SAEB media em Matematica (escala SAEB). Componente N do IDEB. |
| `nota_portugues` | FLOAT | Nota SAEB media em Lingua Portuguesa (escala SAEB). Componente N do IDEB. |
| `nota_media` | FLOAT | Nota SAEB media padronizada combinada LP e Mat. Componente N do IDEB. |
| `ideb_observado` | FLOAT | IDEB observado = N x P (escala 0-10). NULL se dado insuficiente. |
| `meta_projecao` | FLOAT | Meta IDEB projetada pelo MEC para este ano e nivel. NULL em 2005 e 2023. |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC de geracao deste registro na camada trusted. |
