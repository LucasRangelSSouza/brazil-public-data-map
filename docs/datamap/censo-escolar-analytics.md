# School Census (INEP): Analytics

Dataset: [lucasrangelss/censo-escolar-analytics](https://www.kaggle.com/datasets/lucasrangelss/censo-escolar-analytics) · snapshot 2026-10-01 · 10 tables · 974,300,023 rows

**Source:** Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP), [https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar)

Yearly School Census microdata at school level: schools, classes, teachers, enrolments and infrastructure, with the historical series recovered from 1995. Student-level and teacher-level microdata are not released.

**Grain and keys:** School by year for the school tables; the semantic tables aggregate to school-year and municipality-year. The 2025 edition changed the enrolment file from student level to school-level aggregates.

**Layers.** `raw` is the source snapshot as delivered. `trusted` is typed, deduplicated and named consistently. `semantic` joins and reshapes trusted tables for analysis. Every table is a Parquet file named `<layer>__<table>.parquet` at the root of the dataset.

The full interactive map (lineage, joins, search) is at [https://rangeltech.net/datamap/](https://rangeltech.net/datamap/). Column descriptions come from the source lake's catalogue and are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns | Described | Upstream |
|---|---|---:|---:|---:|---|
| semantic | [`f_censo_escolar`](#semantic-f-censo-escolar) | 178,050 | 64 | 0 | `inep_censo_escolar_escolas`, `inep_censo_escolar_matriculas` |
| semantic | [`f_censo_escolar_municipio`](#semantic-f-censo-escolar-municipio) | 5,596 | 39 | 0 | `inep_censo_escolar_escolas`, `inep_censo_escolar_matriculas` |
| semantic | [`obt_inep_censo_docente_escola_ano`](#semantic-obt-inep-censo-docente-escola-ano) | 7,341,023 | 156 | 156 | `inep_censo_escolar_censoesc`, `obt_inep_censo_escola_ano`, `inep_censo_escolar_docentes` |
| semantic | [`obt_inep_censo_escola_ano`](#semantic-obt-inep-censo-escola-ano) | 7,376,443 | 85 | 85 | `obt_ibge_municipio`, `inep_censo_escolar_escolas`, `inep_censo_escolar_localizacao` |
| semantic | [`obt_inep_censo_infraestrutura_escola`](#semantic-obt-inep-censo-infraestrutura-escola) | 944,184,704 | 15 | 15 | `inep_censo_escolar_escolas`, `inep_censo_escolar_infraestrutura` |
| semantic | [`obt_inep_censo_matricula_escola_ano`](#semantic-obt-inep-censo-matricula-escola-ano) | 7,341,017 | 243 | 243 | `inep_censo_escolar_censoesc`, `obt_inep_censo_escola_ano`, `inep_censo_escolar_matriculas` |
| semantic | [`obt_inep_censo_municipio_ano`](#semantic-obt-inep-censo-municipio-ano) | 170,578 | 32 | 32 | `obt_inep_censo_docente_escola_ano`, `obt_inep_censo_escola_ano`, `obt_inep_censo_matricula_escola_ano`, `obt_inep_censo_turma_escola_ano` |
| semantic | [`obt_inep_censo_municipio_rede_ano`](#semantic-obt-inep-censo-municipio-rede-ano) | 352,866 | 30 | 30 | `obt_inep_censo_docente_escola_ano`, `obt_inep_censo_escola_ano`, `obt_inep_censo_matricula_escola_ano`, `obt_inep_censo_turma_escola_ano` |
| semantic | [`obt_inep_censo_perguntas`](#semantic-obt-inep-censo-perguntas) | 8,723 | 20 | 20 | `inep_censo_escolar_colunas_fonte`, `inep_censo_escolar_dicionario_campos` |
| semantic | [`obt_inep_censo_turma_escola_ano`](#semantic-obt-inep-censo-turma-escola-ano) | 7,341,023 | 190 | 190 | `inep_censo_escolar_censoesc`, `obt_inep_censo_escola_ano`, `inep_censo_escolar_turmas` |

## semantic · f_censo_escolar

File `semantic__f_censo_escolar.parquet` · 178,050 rows · 64 columns

**Built from:** `trusted/inep_censo_escolar_escolas`, `trusted/inep_censo_escolar_matriculas`

| Column | Type | Description |
|---|---|---|
| `CodEntidade` | INTEGER |  |
| `NomeEscola` | STRING |  |
| `CodMunicipio` | INTEGER |  |
| `NomeMunicipio` | STRING |  |
| `CodUF` | INTEGER |  |
| `SiglaUF` | STRING |  |
| `NomeUF` | STRING |  |
| `CodDependencia` | INTEGER |  |
| `Dependencia` | STRING |  |
| `Cliente` | STRING |  |
| `IndCreche` | INTEGER |  |
| `IndPre` | INTEGER |  |
| `IndFund` | INTEGER |  |
| `IndFundAI` | INTEGER |  |
| `IndFundAF` | INTEGER |  |
| `IndMed` | INTEGER |  |
| `IndProf` | INTEGER |  |
| `IndEJA` | INTEGER |  |
| `QtdMatCreche` | INTEGER |  |
| `QtdMatPre` | INTEGER |  |
| `QtdMatFund` | INTEGER |  |
| `QtdMatFundAI` | INTEGER |  |
| `QtdMatFundAF` | INTEGER |  |
| `QtdMatMed` | INTEGER |  |
| `QtdMatProf` | INTEGER |  |
| `QtdMatEJA` | INTEGER |  |
| `QtdMatTotal` | INTEGER |  |
| `KE_Creche` | INTEGER |  |
| `KE_PreTotal` | INTEGER |  |
| `KE_PreMenosEF` | INTEGER |  |
| `KE_PreMenosEFAI` | INTEGER |  |
| `KE_PreMenosEFAF` | INTEGER |  |
| `KE_Fund` | INTEGER |  |
| `KE_FundAI` | INTEGER |  |
| `KE_FundAF` | INTEGER |  |
| `KE_Med` | INTEGER |  |
| `KE_Prof_EJA` | INTEGER |  |
| `KE_Prof` | INTEGER |  |
| `KE_EJA` | INTEGER |  |
| `KE_Total` | INTEGER |  |
| `KA_Creche` | INTEGER |  |
| `KA_Pre` | INTEGER |  |
| `KA_FundAI` | INTEGER |  |
| `KA_FundAF` | INTEGER |  |
| `KA_Med` | INTEGER |  |
| `KA_Prof` | INTEGER |  |
| `KA_EJA` | INTEGER |  |
| `KA_Total` | INTEGER |  |
| `KP_Creche` | FLOAT |  |
| `KP_Pre` | FLOAT |  |
| `KP_FundAI` | FLOAT |  |
| `KP_FundAF` | FLOAT |  |
| `KP_Med` | FLOAT |  |
| `KP_Prof` | FLOAT |  |
| `KP_EJA` | FLOAT |  |
| `KP_Total` | FLOAT |  |
| `KA_KP_Creche` | FLOAT |  |
| `KA_KP_Pre` | FLOAT |  |
| `KA_KP_FundAI` | FLOAT |  |
| `KA_KP_FundAF` | FLOAT |  |
| `KA_KP_Med` | FLOAT |  |
| `KA_KP_Prof` | FLOAT |  |
| `KA_KP_EJA` | FLOAT |  |
| `KA_KP_Total` | FLOAT |  |

## semantic · f_censo_escolar_municipio

File `semantic__f_censo_escolar_municipio.parquet` · 5,596 rows · 39 columns

**Built from:** `trusted/inep_censo_escolar_escolas`, `trusted/inep_censo_escolar_matriculas`

| Column | Type | Description |
|---|---|---|
| `AnoCenso` | INTEGER |  |
| `Rede` | STRING |  |
| `Codigo` | INTEGER |  |
| `Cliente` | STRING |  |
| `CodUF` | INTEGER |  |
| `SiglaUF` | STRING |  |
| `NomeUF` | STRING |  |
| `CodMunicipio` | INTEGER |  |
| `NomeMunicipio` | STRING |  |
| `EscolasCreche` | INTEGER |  |
| `EscolasPre` | INTEGER |  |
| `EscolasFundAI` | INTEGER |  |
| `EscolasFundAF` | INTEGER |  |
| `EscolasMed` | INTEGER |  |
| `EscolasProf` | INTEGER |  |
| `EscolasEJA` | INTEGER |  |
| `EscolasTotal` | INTEGER |  |
| `QtdMatCreche` | INTEGER |  |
| `QtdMatPre` | INTEGER |  |
| `QtdMatFund` | INTEGER |  |
| `QtdMatFundAI` | INTEGER |  |
| `QtdMatFundAF` | INTEGER |  |
| `QtdMatMed` | INTEGER |  |
| `QtdMatProf` | INTEGER |  |
| `QtdMatEJA` | INTEGER |  |
| `QtdMatTotal` | INTEGER |  |
| `KE_Creche` | INTEGER |  |
| `KE_PreTotal` | INTEGER |  |
| `KE_PreMenosEF` | INTEGER |  |
| `KE_PreMenosEFAI` | INTEGER |  |
| `KE_PreMenosEFAF` | INTEGER |  |
| `KE_Fund` | INTEGER |  |
| `KE_FundAI` | INTEGER |  |
| `KE_FundAF` | INTEGER |  |
| `KE_Med` | INTEGER |  |
| `KE_Prof_EJA` | INTEGER |  |
| `KE_Prof` | INTEGER |  |
| `KE_EJA` | INTEGER |  |
| `KE_Total` | INTEGER |  |

## semantic · obt_inep_censo_docente_escola_ano

File `semantic__obt_inep_censo_docente_escola_ano.parquet` · 7,341,023 rows · 156 columns

Censo Escolar — contagens de docentes por escola e ano. Grao: 1 linha por (codigo_escola, ano). Colunas quantidade_doc_* (alias de QT_DOC_*). FK: codigo_escola = obt_inep_censo_escola_ano.codigo_escola. Para geografia JOIN com obt_inep_censo_escola_ano. INEP Censo Escolar dados.gov.br.

**Built from:** `raw/inep_censo_escolar_censoesc`, `semantic/obt_inep_censo_escola_ano`, `trusted/inep_censo_escolar_docentes`

**Feeds:** `semantic/obt_inep_censo_municipio_ano`, `semantic/obt_inep_censo_municipio_rede_ano`

| Column | Type | Description |
|---|---|---|
| `codigo_escola` | INTEGER | Código único INEP da escola (CO_ENTIDADE, 8 dígitos). PK composta com ano. |
| `ano` | INTEGER | Ano do Censo Escolar (NU_ANO_CENSO). INT64. PK composta com codigo_escola. |
| `quantidade_doc_bas` | INTEGER | Número de Docentes da Educação Básica |
| `quantidade_doc_inf` | INTEGER | Número de Docentes da Educação Infantil |
| `quantidade_doc_inf_cre` | INTEGER | Número de Docentes da Educação Infantil - Creche |
| `quantidade_doc_inf_pre` | INTEGER | Número de Docentes da Educação Infantil - Pré-Escola |
| `quantidade_doc_fund` | INTEGER | Número de Docentes do Ensino Fundamental |
| `quantidade_doc_fund_ai` | INTEGER | Número de Docentes do Ensino Fundamental - Anos Iniciais |
| `quantidade_doc_fund_af` | INTEGER | Número de Docentes do Ensino Fundamental - Anos Finais |
| `quantidade_doc_med` | INTEGER | Número de Docentes do Ensino Médio Regular |
| `quantidade_doc_prof` | INTEGER | Número de Docentes da Educação Profissional |
| `quantidade_doc_prof_tec` | INTEGER | Número de Docentes da Educação Profissional Técnica |
| `quantidade_doc_eja` | INTEGER | Número de Docentes da Educação de Jovens e Adultos (EJA) |
| `quantidade_doc_eja_fund` | INTEGER | Número de Docentes da Educação de Jovens e Adultos (EJA) - Ensino Fundamental |
| `quantidade_doc_eja_med` | INTEGER | Número de Docentes da Educação de Jovens e Adultos (EJA) - Ensino Médio |
| `quantidade_doc_esp` | INTEGER | Número de Docentes da Educação Especial |
| `quantidade_doc_esp_cc` | INTEGER | Número de Docentes da Educação Especial em Classes Comuns |
| `quantidade_doc_esp_ce` | INTEGER | Número de Docentes da Educação Especial em Classes Exclusivas |
| `quantidade_doc_fund_ai_1` | INTEGER | Número de Docentes do Ensino Fundamental - Anos Iniciais - 1º Ano |
| `quantidade_doc_fund_ai_2` | INTEGER | Número de Docentes do Ensino Fundamental - Anos Iniciais - 2º Ano |
| `quantidade_doc_fund_ai_3` | INTEGER | Número de Docentes do Ensino Fundamental - Anos Iniciais - 3º Ano |
| `quantidade_doc_fund_ai_4` | INTEGER | Número de Docentes do Ensino Fundamental - Anos Iniciais - 4º Ano |
| `quantidade_doc_fund_ai_5` | INTEGER | Número de Docentes do Ensino Fundamental - Anos Iniciais - 5º Ano |
| `quantidade_doc_fund_ai_multietapa` | INTEGER | Número de Docentes do Ensino Fundamental - Educação Infantil e Ensino Fundamental Multietapa |
| `quantidade_doc_fund_af_6` | INTEGER | Número de Docentes do Ensino Fundamental - Anos Finais - 6º Ano |
| `quantidade_doc_fund_af_7` | INTEGER | Número de Docentes do Ensino Fundamental - Anos Finais - 7º Ano |
| `quantidade_doc_fund_af_8` | INTEGER | Número de Docentes do Ensino Fundamental - Anos Finais - 8º Ano |
| `quantidade_doc_fund_af_9` | INTEGER | Número de Docentes do Ensino Fundamental - Anos Finais - 9º Ano |
| `quantidade_doc_fund_af_multi` | INTEGER | Número de Docentes do Ensino Fundamental - Multi |
| `quantidade_doc_fund_af_corrfluxo` | INTEGER | Número de Docentes do Ensino Fundamental - Correção de Fluxo |
| `quantidade_doc_med_prop` | INTEGER | Número de Docentes do Ensino Médio Regular - Propedêutico |
| `quantidade_doc_med_prop_1` | INTEGER | Número de Docentes do Ensino Médio Regular - Propedêutico - 1º ano/1ª Série |
| `quantidade_doc_med_prop_2` | INTEGER | Número de Docentes do Ensino Médio Regular - Propedêutico - 2º ano/2ª Série |
| `quantidade_doc_med_prop_3` | INTEGER | Número de Docentes do Ensino Médio Regular - Propedêutico - 3º ano/3ª Série |
| `quantidade_doc_med_prop_4` | INTEGER | Número de Docentes do Ensino Médio Regular - Propedêutico - 4º ano/4ª Série |
| `quantidade_doc_med_prop_ns` | INTEGER | Número de Docentes do Ensino Médio Regular - Propedêutico - Não Seriado |
| `quantidade_doc_med_iftp_ct` | INTEGER | Número de Docentes do Ensino Médio Regular - Ensino Médio Regular articulado ao Itinerário Formativo Técnico Profissional (IFTP) - Curso Técnico |
| `quantidade_doc_med_iftp_ct_1` | INTEGER | Número de Docentes do Ensino Médio Regular - Ensino Médio Regular articulado ao Itinerário Formativo Técnico Profissional (IFTP) - Curso Técnico - 1º ano/1ª Série |
| `quantidade_doc_med_iftp_ct_2` | INTEGER | Número de Docentes do Ensino Médio Regular - Ensino Médio Regular articulado ao Itinerário Formativo Técnico Profissional (IFTP) - Curso Técnico - 2º ano/2ª Série |
| `quantidade_doc_med_iftp_ct_3` | INTEGER | Número de Docentes do Ensino Médio Regular - Ensino Médio Regular articulado ao Itinerário Formativo Técnico Profissional (IFTP) - Curso Técnico - 3º ano/3ª Série |
| `quantidade_doc_med_iftp_ct_4` | INTEGER | Número de Docentes do Ensino Médio Regular - Ensino Médio Regular articulado ao Itinerário Formativo Técnico Profissional (IFTP) - Curso Técnico - 4º ano/4ª Série |
| `quantidade_doc_med_iftp_ct_ns` | INTEGER | Número de Docentes do Ensino Médio Regular - Ensino Médio Regular articulado ao Itinerário Formativo Técnico Profissional (IFTP) - Curso Técnico - Não Seriado |
| `quantidade_doc_med_iftp_qp` | INTEGER | Número de Docentes do Ensino Médio Regular - Ensino Médio Regular articulado ao Itinerário Formativo Técnico Profissional (IFTP) - Qualificação Profissional |
| `quantidade_doc_med_iftp_qp_1` | INTEGER | Número de Docentes do Ensino Médio Regular - Ensino Médio Regular articulado ao Itinerário Formativo Técnico Profissional (IFTP) - Qualificação Profissional - 1º ano/1ª Série |
| `quantidade_doc_med_iftp_qp_2` | INTEGER | Número de Docentes do Ensino Médio Regular - Ensino Médio Regular articulado ao Itinerário Formativo Técnico Profissional (IFTP) - Qualificação Profissional - 2º ano/2ª Série |
| `quantidade_doc_med_iftp_qp_3` | INTEGER | Número de Docentes do Ensino Médio Regular - Ensino Médio Regular articulado ao Itinerário Formativo Técnico Profissional (IFTP) - Qualificação Profissional - 3º ano/3ª Série |
| `quantidade_doc_med_iftp_qp_4` | INTEGER | Número de Docentes do Ensino Médio Regular - Ensino Médio Regular articulado ao Itinerário Formativo Técnico Profissional (IFTP) - Qualificação Profissional - 4º ano/4ª Série |
| `quantidade_doc_med_iftp_qp_ns` | INTEGER | Número de Docentes do Ensino Médio Regular - Ensino Médio Regular articulado ao Itinerário Formativo Técnico Profissional (IFTP) - Qualificação Profissional - Não Seriado |
| `quantidade_doc_med_nm` | INTEGER | Número de Docentes do Ensino Médio Regular - Modalidade Normal/Magistério |
| `quantidade_doc_med_nm_1` | INTEGER | Número de Docentes do Ensino Médio Regular - Modalidade Normal/Magistério - 1º ano/1ª Série |
| `quantidade_doc_med_nm_2` | INTEGER | Número de Docentes do Ensino Médio Regular - Modalidade Normal/Magistério - 2º ano/2ª Série |
| `quantidade_doc_med_nm_3` | INTEGER | Número de Docentes do Ensino Médio Regular - Modalidade Normal/Magistério - 3º ano/3ª Série |
| `quantidade_doc_med_nm_4` | INTEGER | Número de Docentes do Ensino Médio Regular - Modalidade Normal/Magistério - 4º ano/4ª Série |
| `quantidade_doc_prof_tec_conc` | INTEGER | Número de Docentes da Educação Profissional Técnica - Curso Técnico Concomitante |
| `quantidade_doc_prof_tec_subs` | INTEGER | Número de Docentes da Educação Profissional Técnica - Curso Técnico Subsequente |
| `quantidade_doc_prof_tec_misto` | INTEGER | Número de Docentes da Educação Profissional Técnica - Curso Técnico Misto (Concomitante e Subsequente) |
| `quantidade_doc_prof_tec_iftp_ct` | INTEGER | Número de Docentes da Educação Profissional Técnica - Itinerário Formativo Técnico Profissional (IFTP) Exclusivo - Curso Técnico (não articulado ao ensino médio regular) |
| `quantidade_doc_prof_nao_tec` | INTEGER | Número de Docentes da Educação Profissional Não-Técnica |
| `quantidade_doc_prof_iftp_qp` | INTEGER | Número de Docentes da Educação Profissional - Itinerário Formativo Técnico Profissional (IFTP) Exclusivo - Qualificação Profissional (não articulado ao ensino médio regular) |
| `quantidade_doc_prof_fic_conc` | INTEGER | Número de Docentes da Educação Profissional - Curso FIC Concomitante |
| `quantidade_doc_eja_fund_nprof` | INTEGER | Número de Docentes da Educação de Jovens e Adultos (EJA) - Ensino Fundamental - Sem componente profissionalizante |
| `quantidade_doc_eja_fund_ai` | INTEGER | Número de Docentes da Educação de Jovens e Adultos (EJA) - Ensino Fundamental - Anos Iniciais |
| `quantidade_doc_eja_fund_af` | INTEGER | Número de Docentes da Educação de Jovens e Adultos (EJA) - Ensino Fundamental - Anos Finais |
| `quantidade_doc_eja_fund_fic` | INTEGER | Número de Docentes da Educação de Jovens e Adultos (EJA) - Ensino Fundamental - Curso FIC Integrado na Modalidade EJA de Nível Fundamental |
| `quantidade_doc_eja_med_nprof` | INTEGER | Número de Docentes da Educação de Jovens e Adultos (EJA) - Ensino Médio - Sem componente profissionalizante |
| `quantidade_doc_eja_med_fic` | INTEGER | Número de Docentes da Educação de Jovens e Adultos (EJA) - Ensino Médio - Curso FIC Integrado na Modalidade EJA de Nível Médio |
| `quantidade_doc_eja_med_tec` | INTEGER | Número de Docentes da Educação de Jovens e Adultos (EJA) - Ensino Médio - Curso Técnico Integrado na Modalidade EJA de Nível Médio |
| `quantidade_doc_bas_fem` | INTEGER | Número de Docentes da Educação Básica - Feminino |
| `quantidade_doc_bas_masc` | INTEGER | Número de Docentes da Educação Básica - Masculino |
| `quantidade_doc_bas_nd` | INTEGER | Número de Docentes da Educação Básica - Cor/Raça Não Declarada |
| `quantidade_doc_bas_branca` | INTEGER | Número de Docentes da Educação Básica - Cor/Raça Branca |
| `quantidade_doc_bas_preta` | INTEGER | Número de Docentes da Educação Básica - Cor/Raça Preta |
| `quantidade_doc_bas_parda` | INTEGER | Número de Docentes da Educação Básica - Cor/Raça Parda |
| `quantidade_doc_bas_amarela` | INTEGER | Número de Docentes da Educação Básica - Cor/Raça Amarela |
| `quantidade_doc_bas_indigena` | INTEGER | Número de Docentes da Educação Básica - Cor/Raça Indígena |
| `quantidade_doc_bas_0_24` | INTEGER | Número de Docentes da Educação Básica - Até 24 anos de idade na data de referência do Censo Escolar (última quarta-feira do mês de maio de 2025) |
| `quantidade_doc_bas_25_29` | INTEGER | Número de Docentes da Educação Básica - Entre 25 e 29 anos de idade na data de referência do Censo Escolar (última quarta-feira do mês de maio de 2025) |
| `quantidade_doc_bas_30_39` | INTEGER | Número de Docentes da Educação Básica - Entre 30 e 39 anos de idade na data de referência do Censo Escolar (última quarta-feira do mês de maio de 2025) |
| `quantidade_doc_bas_40_49` | INTEGER | Número de Docentes da Educação Básica - Entre 40 e 49 anos de idade na data de referência do Censo Escolar (última quarta-feira do mês de maio de 2025) |
| `quantidade_doc_bas_50_54` | INTEGER | Número de Docentes da Educação Básica - Entre 50 e 54 anos de idade na data de referência do Censo Escolar (última quarta-feira do mês de maio de 2025) |
| `quantidade_doc_bas_55_59` | INTEGER | Número de Docentes da Educação Básica - Entre 55 e 59 anos de idade na data de referência do Censo Escolar (última quarta-feira do mês de maio de 2025) |
| `quantidade_doc_bas_60_mais` | INTEGER | Número de Docentes da Educação Básica - Com 60 ou mais anos de idade na data de referência do Censo Escolar (última quarta-feira do mês de maio de 2025) |
| `quantidade_doc_bas_pcd` | INTEGER | Número de Docentes da Educação Básica com alguma deficiência, transtorno do espectro autista (TEA) ou superdotação |
| `quantidade_doc_bas_zr_urb` | INTEGER | Número de Docentes da Educação Básica - Localização/Zona de residência do Docente - Urbana |
| `quantidade_doc_bas_zr_rur` | INTEGER | Número de Docentes da Educação Básica - Localização/Zona de residência do Docente - Rural |
| `quantidade_doc_bas_zr_na` | INTEGER | Número de Docentes da Educação Básica - Localização/Zona de residência do Docente - Não aplicável para Docentes residentes no exterior |
| `quantidade_doc_bas_esco_ef` | INTEGER | Número de Docentes da Educação Básica - Maior nível de Escolaridade concluída - Ensino Fundamental |
| `quantidade_doc_bas_esco_em` | INTEGER | Número de Docentes da Educação Básica - Maior nível de Escolaridade concluída - Ensino Médio |
| `quantidade_doc_bas_esco_sup_grad` | INTEGER | Número de Docentes da Educação Básica - Maior nível de Escolaridade concluída - Educação Superior (Graduação) |
| `quantidade_doc_bas_esco_sup_grad_licen` | INTEGER | Número de Docentes da Educação Básica - Número de Docentes da Educação Básica - Maior nível de Escolaridade concluída - Educação Superior Licenciatura |
| `quantidade_doc_bas_esco_sup_grad_slicen` | INTEGER | Número de Docentes da Educação Básica - Número de Docentes da Educação Básica - Maior nível de Escolaridade concluída - Educação Superior Sem Licenciatura |
| `quantidade_doc_bas_esco_sup_pos_espec` | INTEGER | Número de Docentes da Educação Básica - Pós-Graduação concluída - Especialização |
| `quantidade_doc_bas_esco_sup_pos_mestra` | INTEGER | Número de Docentes da Educação Básica - Pós-Graduação concluída - Mestrado |
| `quantidade_doc_bas_esco_sup_pos_douto` | INTEGER | Número de Docentes da Educação Básica - Pós-Graduação concluída - Doutorado |
| `quantidade_doc_bas_esco_sup_pos_nenhum` | INTEGER | Número de Docentes da Educação Básica - Pós-Graduação concluída - Não tem pós-graduação concluída |
| `quantidade_doc_bas_vinculo_concur` | INTEGER | Número de Docentes da Educação Básica - Situação Funcional/Regime de contratação/Tipo de Vínculo (Apenas para docente de escola pública) - Concursado/efetivo/estável |
| `quantidade_doc_bas_vinculo_contra` | INTEGER | Número de Docentes da Educação Básica - Situação Funcional/Regime de contratação/Tipo de Vínculo (Apenas para docente de escola pública) - Contrato temporário |
| `quantidade_doc_bas_vinculo_terceir` | INTEGER | Número de Docentes da Educação Básica - Situação Funcional/Regime de contratação/Tipo de Vínculo (Apenas para docente de escola pública) - Contrato terceirizado |
| `quantidade_doc_bas_vinculo_clt` | INTEGER | Número de Docentes da Educação Básica - Situação Funcional/Regime de contratação/Tipo de Vínculo (Apenas para docente de escola pública) - Contrato CLT |
| `quantidade_doc_bas_docente` | INTEGER | Número de Docentes da Educação Básica - Função que o Profissional Exerce em Sala de Aula - Docente |
| `quantidade_doc_bas_auxiliar` | INTEGER | Número de Docentes da Educação Básica - Função que o Profissional Exerce em Sala de Aula - Auxiliar/Assistente Educacional |
| `quantidade_doc_bas_profi_monitor` | INTEGER | Número de Docentes da Educação Básica - Função que o Profissional Exerce em Sala de Aula - Profissional/Monitor de atividade complementar |
| `quantidade_doc_bas_tradutor_libras` | INTEGER | Número de Docentes da Educação Básica - Função que o Profissional Exerce em Sala de Aula - Tradutor Intérprete de Libras |
| `quantidade_doc_bas_titular_ead` | INTEGER | Número de Docentes da Educação Básica - Função que o Profissional Exerce em Sala de Aula - Docente Titular - coordenador de tutoria (de módulo ou disciplina) - EAD |
| `quantidade_doc_bas_tutor_aux_ead` | INTEGER | Número de Docentes da Educação Básica - Função que o Profissional Exerce em Sala de Aula - Docente Tutor - Auxiliar (de módulo ou disciplina) - EAD |
| `quantidade_doc_bas_guia_interprete` | INTEGER | Número de Docentes da Educação Básica - Função que o Profissional Exerce em Sala de Aula - Guia intérprete |
| `quantidade_doc_bas_apoio_pcd` | INTEGER | Número de Docentes da Educação Básica - Função que o Profissional Exerce em Sala de Aula - Profissional de apoio escolar para alunos com deficiência (Lei 13.146/2015) |
| `quantidade_doc_bas_instrutor_ep` | INTEGER | Número de Docentes da Educação Básica - Função que o Profissional Exerce em Sala de Aula - Instrutor de educação profissional |
| `quantidade_doc_bas_espec_cre` | INTEGER | Número de Docentes da Educação Básica - Outros cursos - Formação Continuada com no mínimo 80 horas - Específico para creche (0 a 3 anos) |
| `quantidade_doc_bas_espec_pre_escola` | INTEGER | Número de Docentes da Educação Básica - Outros cursos - Formação Continuada com no mínimo 80 horas - Específico para pré-escola (4 e 5 anos) |
| `quantidade_doc_bas_espec_anos_iniciais` | INTEGER | Número de Docentes da Educação Básica - Outros cursos - Formação Continuada com no mínimo 80 horas - Específico para anos iniciais do ensino fundamental |
| `quantidade_doc_bas_espec_anos_finais` | INTEGER | Número de Docentes da Educação Básica - Outros cursos - Formação Continuada com no mínimo 80 horas - Específico para anos finais do ensino fundamental |
| `quantidade_doc_bas_espec_ens_medio` | INTEGER | Número de Docentes da Educação Básica - Outros cursos - Formação Continuada com no mínimo 80 horas - Específico para ensino médio |
| `quantidade_doc_bas_espec_eja` | INTEGER | Número de Docentes da Educação Básica - Outros cursos - Formação Continuada com no mínimo 80 horas - Específico para educação de jovens e adultos |
| `quantidade_doc_bas_espec_ed_especial` | INTEGER | Número de Docentes da Educação Básica - Outros cursos - Formação Continuada com no mínimo 80 horas - Específico para educação especial |
| `quantidade_doc_bas_espec_bil_surdos` | INTEGER | Número de Docentes da Educação Básica - Outros cursos - Formação Continuada com no mínimo 80 horas - Educação bilíngue de surdos |
| `quantidade_doc_bas_espec_ed_indigena` | INTEGER | Número de Docentes da Educação Básica - Outros cursos - Formação Continuada com no mínimo 80 horas - Específico para educação indígena |
| `quantidade_doc_bas_espec_campo` | INTEGER | Número de Docentes da Educação Básica - Outros cursos - Formação Continuada com no mínimo 80 horas - Educação do Campo |
| `quantidade_doc_bas_espec_ambiental` | INTEGER | Número de Docentes da Educação Básica - Outros cursos - Formação Continuada com no mínimo 80 horas - Educação Ambiental |
| `quantidade_doc_bas_espec_dir_humanos` | INTEGER | Número de Docentes da Educação Básica - Outros cursos - Formação Continuada com no mínimo 80 horas - Educação em direitos humanos |
| `quantidade_doc_bas_espec_div_sexual` | INTEGER | Número de Docentes da Educação Básica - Outros cursos - Formação Continuada com no mínimo 80 horas - Gênero e Diversidade Sexual |
| `quantidade_doc_bas_espec_dir_adolesc` | INTEGER | Número de Docentes da Educação Básica - Outros cursos - Formação Continuada com no mínimo 80 horas - Direitos de criança e adolescente |
| `quantidade_doc_bas_espec_afro` | INTEGER | Número de Docentes da Educação Básica - Outros cursos - Formação Continuada com no mínimo 80 horas - Educação para as relações étnico-raciais e história e cultura afro-brasileira e africana |
| `quantidade_doc_bas_espec_gestao` | INTEGER | Número de Docentes da Educação Básica - Outros cursos - Formação Continuada com no mínimo 80 horas - Gestão escolar |
| `quantidade_doc_bas_espec_educ_tic` | INTEGER | Número de Docentes da Educação Básica - Outros cursos - Formação Continuada com no mínimo 80 horas - Educação e Tecnologia de Informação e Comunicação (TIC) |
| `quantidade_doc_bas_espec_outros` | INTEGER | Número de Docentes da Educação Básica - Outros cursos - Formação Continuada com no mínimo 80 horas - Outros |
| `quantidade_doc_bas_espec_nenhum` | INTEGER | Número de Docentes da Educação Básica - Outros cursos - Formação Continuada com no mínimo 80 horas - Nenhum |
| `quantidade_doc_bas_disc_lingua_port` | INTEGER | Número de Docentes da Educação Básica - Disciplina que atua - Áreas do conhecimento/Componentes curriculares - Língua/ Literatura Portuguesa |
| `quantidade_doc_bas_disc_educ_fisica` | INTEGER | Número de Docentes da Educação Básica - Disciplina que atua - Áreas do conhecimento/Componentes curriculares - Educação Física |
| `quantidade_doc_bas_disc_artes` | INTEGER | Número de Docentes da Educação Básica - Disciplina que atua - Áreas do conhecimento/Componentes curriculares - Artes (Educação Artística, Teatro, Dança, Música, Artes Plásticas e outras) |
| `quantidade_doc_bas_disc_lingua_ing` | INTEGER | Número de Docentes da Educação Básica - Disciplina que atua - Áreas do conhecimento/Componentes curriculares - Língua/ Literatura estrangeira - Inglês |
| `quantidade_doc_bas_disc_lingua_espa` | INTEGER | Número de Docentes da Educação Básica - Disciplina que atua - Áreas do conhecimento/Componentes curriculares - Língua/ Literatura estrangeira - Espanhol |
| `quantidade_doc_bas_disc_lingua_franc` | INTEGER | Número de Docentes da Educação Básica - Disciplina que atua - Áreas do conhecimento/Componentes curriculares - Língua/ Literatura estrangeira - Francês |
| `quantidade_doc_bas_disc_lingua_outra` | INTEGER | Número de Docentes da Educação Básica - Disciplina que atua - Áreas do conhecimento/Componentes curriculares - Língua/ Literatura estrangeira - Outra |
| `quantidade_doc_bas_disc_libras` | INTEGER | Número de Docentes da Educação Básica - Disciplina que atua - Áreas do conhecimento/Componentes curriculares - Libras |
| `quantidade_doc_bas_disc_lingua_indig` | INTEGER | Número de Docentes da Educação Básica - Disciplina que atua - /Componentes curriculares - Língua Indígena |
| `quantidade_doc_bas_disc_port_seg_lingua` | INTEGER | Número de Docentes da Educação Básica - Disciplina que atua - /Componentes curriculares - Língua Portuguesa como segunda língua |
| `quantidade_doc_bas_disc_matematica` | INTEGER | Número de Docentes da Educação Básica - Disciplina que atua - /Componentes curriculares - Matemática |
| `quantidade_doc_bas_disc_ciencias` | INTEGER | Número de Docentes da Educação Básica - Disciplina que atua - /Componentes curriculares - Ciências |
| `quantidade_doc_bas_disc_fisica` | INTEGER | Número de Docentes da Educação Básica - Disciplina que atua - /Componentes curriculares - Física |
| `quantidade_doc_bas_disc_quimica` | INTEGER | Número de Docentes da Educação Básica - Disciplina que atua - /Componentes curriculares - Química |
| `quantidade_doc_bas_disc_biologia` | INTEGER | Número de Docentes da Educação Básica - Disciplina que atua - /Componentes curriculares - Biologia |
| `quantidade_doc_bas_disc_historia` | INTEGER | Número de Docentes da Educação Básica - Disciplina que atua - /Componentes curriculares - História |
| `quantidade_doc_bas_disc_geografia` | INTEGER | Número de Docentes da Educação Básica - Disciplina que atua - /Componentes curriculares - Geografia |
| `quantidade_doc_bas_disc_sociologia` | INTEGER | Número de Docentes da Educação Básica - Disciplina que atua - /Componentes curriculares - Sociologia |
| `quantidade_doc_bas_disc_filosofia` | INTEGER | Número de Docentes da Educação Básica - Disciplina que atua - /Componentes curriculares - Filosofia |
| `quantidade_doc_bas_disc_est_sociais` | INTEGER | Número de Docentes da Educação Básica - Disciplina que atua - /Componentes curriculares - Estudos Sociais |
| `quantidade_doc_bas_disc_est_sociais_soci` | INTEGER | Número de Docentes da Educação Básica - Disciplina que atua - /Componentes curriculares - Estudos Sociais ou Sociologia |
| `quantidade_doc_bas_disc_info_computacao` | INTEGER | Número de Docentes da Educação Básica - Disciplina que atua - /Componentes curriculares - Informática / Computação |
| `quantidade_doc_bas_disc_ensino_religioso` | INTEGER | Número de Docentes da Educação Básica - Disciplina que atua - /Componentes curriculares - Ensino Religioso |
| `quantidade_doc_bas_disc_profissiona` | INTEGER | Número de Docentes da Educação Básica - Disciplina que atua - /Componentes curriculares - Disciplinas dos cursos técnicos profissionais |
| `quantidade_doc_bas_disc_estagio_super` | INTEGER | Número de Docentes da Educação Básica - Disciplina que atua - /Componentes curriculares - Estágio curricular supervisionado |
| `quantidade_doc_bas_disc_pedagogicas` | INTEGER | Número de Docentes da Educação Básica - Disciplina que atua - /Componentes curriculares - Disciplinas pedagógicas |
| `quantidade_doc_bas_disc_projeto_de_vida` | INTEGER | Número de Docentes da Educação Básica - Disciplina que atua - /Componentes curriculares - Projeto de vida |
| `quantidade_doc_bas_disc_outras` | INTEGER | Número de Docentes da Educação Básica - Disciplina que atua - /Componentes curriculares - Outras disciplinas |
| `quantidade_doc_bas_libras` | INTEGER | Número de Docentes da Educação Básica - Classe bilíngue de surdos tendo a Libras (Língua Brasileira de Sinais) como língua de instrução, ensino, comunicação e interação e a língua portuguesa escrita c |

## semantic · obt_inep_censo_escola_ano

File `semantic__obt_inep_censo_escola_ano.parquet` · 7,376,443 rows · 85 columns

Censo Escolar — cadastro e classificacao de escolas por ano. Grao: 1 linha por (codigo_escola, ano). SEM colunas QT_* — matrículas em obt_inep_censo_matricula_escola_ano, docentes em obt_inep_censo_docente_escola_ano, turmas em obt_inep_censo_turma_escola_ano. Dedup por source_file DESC. FK: codigo_escola (= CO_ENTIDADE INEP), codigo_municipio → obt_ibge_municipio. Origem: trusted/inep_censo_escolar_escolas + inep_censo_escolar_localizacao. INEP Censo Escolar dados.gov.br.

**Built from:** `semantic/obt_ibge_municipio`, `trusted/inep_censo_escolar_escolas`, `trusted/inep_censo_escolar_localizacao`

**Feeds:** `semantic/obt_api_saeb_boletim`, `semantic/obt_inep_censo_docente_escola_ano`, `semantic/obt_inep_censo_matricula_escola_ano`, `semantic/obt_inep_censo_municipio_ano`, `semantic/obt_inep_censo_municipio_rede_ano`, `semantic/obt_inep_censo_turma_escola_ano`, `semantic/obt_inep_saeb_micro_escola_ano`, `semantic/obt_inep_saeb_micro_municipio_ano`

| Column | Type | Description |
|---|---|---|
| `codigo_escola` | INTEGER | Código único INEP da escola (CO_ENTIDADE, 8 dígitos). PK composta com ano. |
| `ano` | INTEGER | Ano do Censo Escolar (NU_ANO_CENSO). INT64. PK composta com codigo_escola. |
| `codigo_municipio` | INTEGER | Código IBGE 7 dígitos do município da escola (CO_MUNICIPIO). INT64. FK para obt_ibge_municipio. Para 1995-2006 (formato legado sem código IBGE), resolvido via join por (nome_municipio normalizado + sigla_uf) com obt_ibge_municipio — ~99,3% de cobertura; ~0,7% NULL são municípios renomeados desde então. |
| `nome_municipio` | STRING | Nome do município da escola (NO_MUNICIPIO). |
| `sigla_uf` | STRING | Sigla 2 letras da UF (SG_UF). Ex: SP, RJ, MG. |
| `codigo_uf` | INTEGER | Código IBGE 2 dígitos da UF (CO_UF). INT64. |
| `nome_uf` | STRING | Nome completo da UF (NO_UF). |
| `codigo_regiao` | INTEGER | Código IBGE 1 dígito da região (CO_REGIAO). INT64. |
| `nome_regiao` | STRING | Nome da região geográfica (NO_REGIAO). |
| `nome_escola` | STRING | Nome oficial da escola (NO_ENTIDADE). |
| `nome_mesorregiao` | STRING | Nome da Mesorregião |
| `codigo_mesorregiao` | INTEGER | Código da Mesorregião |
| `nome_microrregiao` | STRING | Nome da Microrregião |
| `codigo_microrregiao` | INTEGER | Código da Microrregião |
| `codigo_distrito` | INTEGER | Divisão Intramunicipal - Código do Distrito |
| `tipo_dependencia` | INTEGER | Dependência Administrativa |
| `tipo_categoria_escola_privada` | INTEGER | Categoria da escola privada |
| `tipo_localizacao` | INTEGER | Localização |
| `tipo_localizacao_diferenciada` | INTEGER | Localização diferenciada da escola |
| `descricao_endereco` | STRING | Endereço |
| `numero_endereco` | INTEGER | Número |
| `descricao_complemento` | STRING | Complemento |
| `nome_bairro` | STRING | Bairro |
| `codigo_cep` | INTEGER | CEP |
| `numero_ddd` | INTEGER | DDD |
| `numero_telefone` | INTEGER | Telefone |
| `tipo_situacao_funcionamento` | INTEGER | Situação de funcionamento |
| `codigo_orgao_regional` | INTEGER | Código do Órgão Regional de Ensino |
| `data_ano_letivo_inicio` | STRING | Início do ano letivo |
| `data_ano_letivo_termino` | STRING | Término (previsão) do ano letivo |
| `indicador_vinculo_secretaria_educacao` | INTEGER | Órgão ao qual a escola pública está vinculada - Secretaria de Educação/Ministério da Educação |
| `indicador_vinculo_seguranca_publica` | INTEGER | Órgão ao qual a escola pública está vinculada - Secretaria de Segurança Pública/Forças Armadas/Militar |
| `indicador_vinculo_secretaria_saude` | INTEGER | Órgão ao qual a escola pública está vinculada - Secretaria de Saúde/Ministério da Saúde |
| `indicador_vinculo_outro_orgao` | INTEGER | Órgão ao qual a escola pública está vinculada - Outro órgão da administração pública |
| `indicador_conveniada_pp` | INTEGER | Conveniada com o poder público |
| `tipo_convenio_poder_publico` | INTEGER | Dependência do convênio com o poder público |
| `indicador_mant_escola_privada_emp` | INTEGER | Mantenedora da escola privada - Empresa ou grupo empresarial do setor privado ou pessoa física |
| `indicador_mant_escola_privada_ong` | INTEGER | Mantenedora da escola privada - Organização Não Governamental (ONG) - internacional ou nacional |
| `indicador_mant_escola_privada_oscip` | INTEGER | Mantenedora da escola privada - Organização da Sociedade Civil de Interesse Público (Oscip) |
| `indicador_mant_escola_priv_ong_oscip` | INTEGER | Mantenedora da escola privada - Organização Não Governamental (ONG) - internacional ou nacional. Organização da Sociedade Civil de Interesse Público (Oscip) |
| `indicador_mant_escola_privada_sind` | INTEGER | Mantenedora da escola privada - Sindicatos de trabalhadores ou patronais, associações e cooperativas |
| `indicador_mant_escola_privada_sist_s` | INTEGER | Mantenedora da escola privada - Sistema S (Sesi, Senai, Sesc, outros) |
| `indicador_mant_escola_privada_s_fins` | INTEGER | Mantenedora da escola privada - Instituições sem fins lucrativos |
| `tipo_regulamentacao` | INTEGER | Regulamentação/Autorização no conselho ou órgão municipal, estadual ou federal de educação |
| `tipo_responsavel_regulamentacao` | INTEGER | Esfera administrativa do conselho ou órgão responsável pela Regulamentação/Autorização |
| `codigo_escola_sede_vinculada` | INTEGER | Código da escola sede |
| `codigo_ies_ofertante` | INTEGER | Código da IES vinculada à escola |
| `indicador_local_func_predio_escolar` | INTEGER | Local de funcionamento da escola - Prédio Escolar |
| `tipo_ocupacao_predio_escolar` | INTEGER | Forma de ocupação do Prédio escolar |
| `indicador_local_func_salas_empresa` | INTEGER | Local de funcionamento da escola - Salas de empresa |
| `indicador_local_func_socioeducativo` | INTEGER | Local de funcionamento da escola - Unidade de Atendimento socioeducativo |
| `indicador_local_func_unid_prisional` | INTEGER | Local de funcionamento da escola - Unidade Prisional |
| `indicador_local_func_prisional_socio` | INTEGER | Local de funcionamento da escola - Unidade Prisional ou Unidade de atendimento socioeducativo |
| `indicador_local_func_templo_igreja` | INTEGER | Local de funcionamento da escola - Templo/Igreja |
| `indicador_local_func_casa_professor` | INTEGER | Local de funcionamento da escola - Casa do professor |
| `indicador_local_func_galpao` | INTEGER | Local de funcionamento da escola - Galpão/Rancho/Paiol/Barracão |
| `tipo_ocupacao_galpao` | INTEGER | Forma de ocupação do Galpão/Rancho/Paiol/Barracão |
| `indicador_local_func_salas_outra_esc` | INTEGER | Local de funcionamento da escola - Salas em outra escola |
| `indicador_local_func_outros` | INTEGER | Local de funcionamento da escola - Outros |
| `tipo_rede_local` | INTEGER | Rede local de interligação de computadores |
| `tipo_indigena_lingua` | INTEGER | Escola Indígena - Língua em que o ensino é ministrado (apenas para escola indígena) |
| `codigo_lingua_indigena_1` | INTEGER | Escola Indígena - Língua em que o ensino é ministrado (apenas para escola indígena) - Língua Indígena - Código da língua Indígena 1 |
| `codigo_lingua_indigena_2` | INTEGER | Escola Indígena - Língua em que o ensino é ministrado (apenas para escola indígena) - Língua Indígena - Código da língua Indígena 2 |
| `codigo_lingua_indigena_3` | INTEGER | Escola Indígena - Língua em que o ensino é ministrado (apenas para escola indígena) - Língua Indígena - Código da língua Indígena 3 |
| `indicador_orgao_ass_pais` | INTEGER | Órgãos colegiados em funcionamento na escola - Associação de Pais |
| `indicador_orgao_ass_pais_mestres` | INTEGER | Órgãos colegiados em funcionamento na escola - Associação de Pais e Mestres |
| `indicador_orgao_conselho_escolar` | INTEGER | Órgãos colegiados em funcionamento na escola - Conselho Escolar |
| `indicador_orgao_gremio_estudantil` | INTEGER | Órgãos colegiados em funcionamento na escola - Grêmio Estudantil |
| `indicador_orgao_outros` | INTEGER | Órgãos colegiados em funcionamento na escola - Outros |
| `indicador_orgao_nenhum` | INTEGER | Órgãos colegiados em funcionamento na escola - Não há órgãos colegiados em funcionamento |
| `tipo_proposta_pedagogica` | INTEGER | O projeto político pedagógico ou a proposta pedagógica da escola (conforme art. 12 da LDB) foi atualizado nos últimos 12 meses até a data de referência |
| `tipo_aee` | INTEGER | Atendimento Educacional Especializado (AEE) |
| `tipo_atividade_complementar` | INTEGER | Atividade Complementar |
| `indicador_poder_publico_parceria` | INTEGER | Parceria ou convênio com o poder público (parceria ou convênio firmado entre a Administração Pública e instituições privadas ou instituições públicas de ensino, autarquias e fundações da administração |
| `tipo_poder_publico_parceria` | INTEGER | Poder público responsável pela parceria ou convênio entre a Administração Pública e outras instituições |
| `nome_regiao_geog_interm` | STRING | Nome da Região Geográfica Intermediária |
| `codigo_regiao_geog_interm` | INTEGER | Código da Região Geográfica Intermediária |
| `nome_regiao_geog_imed` | STRING | Nome da Região Geográfica Imediata |
| `codigo_regiao_geog_imed` | INTEGER | Código da Região Geográfica Imediata |
| `nome_distrito` | STRING | Divisão Intramunicipal - Nome do Distrito |
| `nome_regiao_administrativa` | STRING | Nome da Região Administrativa referente exclusivamente às regiões administrativas do Distrito Federal (DF) |
| `codigo_regiao_administrativa` | INTEGER | Código da Região Administrativa referente exclusivamente às regiões administrativas do Distrito Federal (DF) |
| `tipo_itinerario_formativo` | INTEGER | Itinerário formativo |
| `latitude` | STRING | Latitude em graus decimais. Fonte: inep_censo_escolar_localizacao. |
| `longitude` | STRING | Longitude em graus decimais. Fonte: inep_censo_escolar_localizacao. |

## semantic · obt_inep_censo_infraestrutura_escola

File `semantic__obt_inep_censo_infraestrutura_escola.parquet` · 944,184,704 rows · 15 columns

Infraestrutura escolar em formato longo (EAV): cada linha = 1 escola x 1 ano x 1 indicador. Particionada por ano, clusterizada por sigla_uf e campo_codigo. Origem: trusted/inep_censo_escolar_infraestrutura + inep_censo_escolar_escolas (geo). Chave logica: codigo_escola + ano + campo_codigo.

**Built from:** `trusted/inep_censo_escolar_escolas`, `trusted/inep_censo_escolar_infraestrutura`

| Column | Type | Description |
|---|---|---|
| `ano` | INTEGER | Ano do Censo Escolar. Coluna de partição. |
| `codigo_escola` | INTEGER | Código INEP da escola (CO_ENTIDADE). INT64. PK composta com ano+campo_codigo. |
| `codigo_municipio` | INTEGER | Código IBGE 7 dígitos do município (CO_MUNICIPIO). |
| `nome_municipio` | STRING | Nome do municipio. |
| `sigla_uf` | STRING | Sigla da UF (2 letras). Coluna de cluster. |
| `codigo_uf` | INTEGER | Codigo IBGE numerico da UF (2 digitos). |
| `nome_uf` | STRING | Nome da UF. |
| `codigo_regiao` | INTEGER | Codigo IBGE da regiao geografica. |
| `nome_regiao` | STRING | Nome da regiao geografica. |
| `dependencia_administrativa_codigo` | INTEGER | Código de dependência: 1=Federal, 2=Estadual, 3=Municipal, 4=Privada. |
| `dependencia_administrativa` | STRING | Texto de dependência. |
| `campo_codigo` | STRING | Nome do indicador IN_* (ex: IN_INTERNET, IN_LABORATORIO_INFORMATICA). PK composta. |
| `valor_booleano` | INTEGER | 1=Possui/Sim, 0=Não possui/Não, NULL=Campo não coletado este ano. |
| `arquivo_fonte_raw` | STRING | Arquivo CSV da raw_zone de origem do valor. |
| `data_carga_semantica` | TIMESTAMP | Timestamp UTC de geração da tabela. |

## semantic · obt_inep_censo_matricula_escola_ano

File `semantic__obt_inep_censo_matricula_escola_ano.parquet` · 7,341,017 rows · 243 columns

Censo Escolar — contagens de matrículas por escola e ano. Grao: 1 linha por (codigo_escola, ano). Colunas quantidade_mat_* (alias de QT_MAT_*). FK: codigo_escola = obt_inep_censo_escola_ano.codigo_escola. Para geografia JOIN com obt_inep_censo_escola_ano. INEP Censo Escolar dados.gov.br.

**Built from:** `raw/inep_censo_escolar_censoesc`, `semantic/obt_inep_censo_escola_ano`, `trusted/inep_censo_escolar_matriculas`

**Feeds:** `semantic/obt_inep_censo_municipio_ano`, `semantic/obt_inep_censo_municipio_rede_ano`

| Column | Type | Description |
|---|---|---|
| `codigo_escola` | INTEGER | Código único INEP da escola (CO_ENTIDADE, 8 dígitos). PK composta com ano. |
| `ano` | INTEGER | Ano do Censo Escolar (NU_ANO_CENSO). INT64. PK composta com codigo_escola. |
| `quantidade_mat_bas` | INTEGER | Número de Matrículas da Educação Básica |
| `quantidade_mat_inf` | INTEGER | Número de Matrículas da Educação Infantil |
| `quantidade_mat_inf_cre` | INTEGER | Número de Matrículas da Educação Infantil - Creche |
| `quantidade_mat_inf_pre` | INTEGER | Número de Matrículas da Educação Infantil - Pré-Escola |
| `quantidade_mat_fund` | INTEGER | Número de Matrículas do Ensino Fundamental |
| `quantidade_mat_fund_ai` | INTEGER | Número de Matrículas do Ensino Fundamental - Anos Iniciais |
| `quantidade_mat_fund_af` | INTEGER | Número de Matrículas do Ensino Fundamental - Anos Finais |
| `quantidade_mat_med` | INTEGER | Número de Matrículas do Ensino Médio Regular |
| `quantidade_mat_prof` | INTEGER | Número de Matrículas da Educação Profissional |
| `quantidade_mat_prof_tec` | INTEGER | Número de Matrículas da Educação Profissional Técnica |
| `quantidade_mat_eja` | INTEGER | Número de Matrículas da Educação de Jovens e Adultos (EJA) |
| `quantidade_mat_eja_fund` | INTEGER | Número de Matrículas da Educação de Jovens e Adultos (EJA) - Ensino Fundamental |
| `quantidade_mat_eja_med` | INTEGER | Número de Matrículas da Educação de Jovens e Adultos (EJA) - Ensino Médio |
| `quantidade_mat_esp` | INTEGER | Número de Matrículas da Educação Especial |
| `quantidade_mat_esp_cc` | INTEGER | Número de Matrículas da Educação Especial em Classes Comuns |
| `quantidade_mat_esp_ce` | INTEGER | Número de Matrículas da Educação Especial em Classes Exclusivas |
| `quantidade_mat_bas_fem` | INTEGER | Número de Matrículas da Educação Básica - Feminino |
| `quantidade_mat_bas_masc` | INTEGER | Número de Matrículas da Educação Básica - Masculino |
| `quantidade_mat_bas_nd` | INTEGER | Número de Matrículas da Educação Básica - Cor/Raça Não Declarada |
| `quantidade_mat_bas_branca` | INTEGER | Número de Matrículas da Educação Básica - Cor/Raça Branca |
| `quantidade_mat_bas_preta` | INTEGER | Número de Matrículas da Educação Básica - Cor/Raça Preta |
| `quantidade_mat_bas_parda` | INTEGER | Número de Matrículas da Educação Básica - Cor/Raça Parda |
| `quantidade_mat_bas_amarela` | INTEGER | Número de Matrículas da Educação Básica - Cor/Raça Amarela |
| `quantidade_mat_bas_indigena` | INTEGER | Número de Matrículas da Educação Básica - Cor/Raça Indígena |
| `quantidade_mat_bas_0_3` | INTEGER | Número de Matrículas da Educação Básica - Até 3 anos de idade na data de referência do Censo Escolar (última quarta-feira do mês de maio de 2025) |
| `quantidade_mat_bas_4_5` | INTEGER | Número de Matrículas da Educação Básica - Entre 4 e 5 anos de idade na data de referência do Censo Escolar (última quarta-feira do mês de maio de 2025) |
| `quantidade_mat_bas_6_10` | INTEGER | Número de Matrículas da Educação Básica - Entre 6 e 10 anos de idade na data de referência do Censo Escolar (última quarta-feira do mês de maio de 2025) |
| `quantidade_mat_bas_11_14` | INTEGER | Número de Matrículas da Educação Básica - Entre 11 e 14 anos de idade na data de referência do Censo Escolar (última quarta-feira do mês de maio de 2025) |
| `quantidade_mat_bas_15_17` | INTEGER | Número de Matrículas da Educação Básica - Entre 15 e 17 anos de idade na data de referência do Censo Escolar (última quarta-feira do mês de maio de 2025) |
| `quantidade_mat_bas_18_mais` | INTEGER | Número de Matrículas da Educação Básica - Com 18 ou mais anos de idade na data de referência do Censo Escolar (última quarta-feira do mês de maio de 2025) |
| `quantidade_mat_bas_d` | INTEGER | Número de Matrículas da Educação Básica - Turno Diurno |
| `quantidade_mat_bas_n` | INTEGER | Número de Matrículas da Educação Básica - Turno Noturno |
| `quantidade_mat_bas_ead` | INTEGER | Número de Matrículas da Educação Básica - Turno não aplicável para turmas semipresenciais ou de Educação a Distância (EAD) |
| `quantidade_mat_inf_int` | INTEGER | Número de Matrículas da Educação Infantil - Tempo Integral |
| `quantidade_mat_inf_cre_int` | INTEGER | Número de Matrículas da Educação Infantil - Creche - Tempo Integral |
| `quantidade_mat_inf_pre_int` | INTEGER | Número de Matrículas da Educação Infantil - Pré-Escola - Tempo Integral |
| `quantidade_mat_fund_int` | INTEGER | Número de Matrículas do Ensino Fundamental - Tempo Integral |
| `quantidade_mat_fund_ai_int` | INTEGER | Número de Matrículas do Ensino Fundamental - Anos Iniciais - Tempo Integral |
| `quantidade_mat_fund_af_int` | INTEGER | Número de Matrículas do Ensino Fundamental - Anos Finais - Tempo Integral |
| `quantidade_mat_med_int` | INTEGER | Número de Matrículas do Ensino Médio - Tempo Integral |
| `quantidade_mat_fund_ai_1` | INTEGER | Número de Matrículas do Ensino Fundamental - Anos Iniciais - 1º Ano |
| `quantidade_mat_fund_ai_2` | INTEGER | Número de Matrículas do Ensino Fundamental - Anos Iniciais - 2º Ano |
| `quantidade_mat_fund_ai_3` | INTEGER | Número de Matrículas do Ensino Fundamental - Anos Iniciais - 3º Ano |
| `quantidade_mat_fund_ai_4` | INTEGER | Número de Matrículas do Ensino Fundamental - Anos Iniciais - 4º Ano |
| `quantidade_mat_fund_ai_5` | INTEGER | Número de Matrículas do Ensino Fundamental - Anos Iniciais - 5º Ano |
| `quantidade_mat_fund_af_6` | INTEGER | Número de Matrículas do Ensino Fundamental - Anos Finais - 6º Ano |
| `quantidade_mat_fund_af_7` | INTEGER | Número de Matrículas do Ensino Fundamental - Anos Finais - 7º Ano |
| `quantidade_mat_fund_af_8` | INTEGER | Número de Matrículas do Ensino Fundamental - Anos Finais - 8º Ano |
| `quantidade_mat_fund_af_9` | INTEGER | Número de Matrículas do Ensino Fundamental - Anos Finais - 9º Ano |
| `quantidade_mat_med_prop` | INTEGER | Número de Matrículas do Ensino Médio Regular - Propedêutico |
| `quantidade_mat_med_prop_1` | INTEGER | Número de Matrículas do Ensino Médio Regular - Propedêutico - 1º ano/1ª Série |
| `quantidade_mat_med_prop_2` | INTEGER | Número de Matrículas do Ensino Médio Regular - Propedêutico - 2º ano/2ª Série |
| `quantidade_mat_med_prop_3` | INTEGER | Número de Matrículas do Ensino Médio Regular - Propedêutico - 3º ano/3ª Série |
| `quantidade_mat_med_prop_4` | INTEGER | Número de Matrículas do Ensino Médio Regular - Propedêutico - 4º ano/4ª Série |
| `quantidade_mat_med_prop_ns` | INTEGER | Número de Matrículas do Ensino Médio Regular - Propedêutico - Não Seriado |
| `quantidade_mat_med_ct` | INTEGER | Matrículas no Ensino Médio Curso Técnico Integrado. — descrição gerada por IA. |
| `quantidade_mat_med_ct_1` | INTEGER | Matrículas na 1ª série do Ensino Médio Técnico Integrado. — descrição gerada por IA. |
| `quantidade_mat_med_ct_2` | INTEGER | Matrículas na 2ª série do Ensino Médio Técnico Integrado. — descrição gerada por IA. |
| `quantidade_mat_med_ct_3` | INTEGER | Matrículas na 3ª série do Ensino Médio Técnico Integrado. — descrição gerada por IA. |
| `quantidade_mat_med_ct_4` | INTEGER | Matrículas na 4ª série do Ensino Médio Técnico Integrado. — descrição gerada por IA. |
| `quantidade_mat_med_ct_ns` | INTEGER | Matrículas no Ensino Médio Técnico Integrado não seriado. — descrição gerada por IA. |
| `quantidade_mat_med_nm` | INTEGER | Número de Matrículas do Ensino Médio Regular - Modalidade Normal/Magistério |
| `quantidade_mat_med_nm_1` | INTEGER | Número de Matrículas do Ensino Médio Regular - Modalidade Normal/Magistério - 1º ano/1ª Série |
| `quantidade_mat_med_nm_2` | INTEGER | Número de Matrículas do Ensino Médio Regular - Modalidade Normal/Magistério - 2º ano/2ª Série |
| `quantidade_mat_med_nm_3` | INTEGER | Número de Matrículas do Ensino Médio Regular - Modalidade Normal/Magistério - 3º ano/3ª Série |
| `quantidade_mat_med_nm_4` | INTEGER | Número de Matrículas do Ensino Médio Regular - Modalidade Normal/Magistério - 4º ano/4ª Série |
| `quantidade_mat_prof_tec_conc` | INTEGER | Número de Matrículas da Educação Profissional Técnica - Curso Técnico Concomitante |
| `quantidade_mat_prof_tec_subs` | INTEGER | Número de Matrículas da Educação Profissional Técnica - Curso Técnico Subsequente |
| `quantidade_mat_prof_fic_conc` | INTEGER | Número de Matrículas da Educação Profissional - Curso FIC Concomitante |
| `quantidade_mat_eja_fund_ai` | INTEGER | Número de Matrículas da Educação de Jovens e Adultos (EJA) - Ensino Fundamental - Anos Iniciais |
| `quantidade_mat_eja_fund_af` | INTEGER | Número de Matrículas da Educação de Jovens e Adultos (EJA) - Ensino Fundamental - Anos Finais |
| `quantidade_mat_eja_fund_fic` | INTEGER | Número de Matrículas da Educação de Jovens e Adultos (EJA) - Ensino Fundamental - Curso FIC Integrado na Modalidade EJA de Nível Fundamental |
| `quantidade_mat_eja_med_nprof` | INTEGER | Número de Matrículas da Educação de Jovens e Adultos (EJA) - Ensino Médio - Sem componente profissionalizante |
| `quantidade_mat_eja_med_fic` | INTEGER | Número de Matrículas da Educação de Jovens e Adultos (EJA) - Ensino Médio - Curso FIC Integrado na Modalidade EJA de Nível Médio |
| `quantidade_mat_eja_med_tec` | INTEGER | Número de Matrículas da Educação de Jovens e Adultos (EJA) - Ensino Médio - Curso Técnico Integrado na Modalidade EJA de Nível Médio |
| `quantidade_mat_zr_urb` | INTEGER | Número de Matrículas da Educação Básica - Localização/Zona de residência do Aluno - Urbana |
| `quantidade_mat_zr_rur` | INTEGER | Número de Matrículas da Educação Básica - Localização/Zona de residência do Aluno - Rural |
| `quantidade_mat_zr_na` | INTEGER | Número de Matrículas da Educação Básica - Localização/Zona de residência do Aluno - Não aplicável para alunos residentes no exterior |
| `quantidade_transp_publico` | INTEGER | Número de Matrículas da Educação Básica de alunos que utilizam transporte escolar público |
| `quantidade_transp_resp_est` | INTEGER | Número de Matrículas da Educação Básica segundo o poder público responsável pelo transporte escolar - Estadual |
| `quantidade_transp_resp_mun` | INTEGER | Número de Matrículas da Educação Básica segundo o poder público responsável pelo transporte escolar - Municipal |
| `quantidade_mat_med_iftp_ct` | INTEGER | Número de Matrículas do Ensino Médio Regular - Ensino Médio Regular articulado ao Itinerário Formativo Técnico Profissional (IFTP) - Curso Técnico |
| `quantidade_mat_med_iftp_ct_1` | INTEGER | Número de Matrículas do Ensino Médio Regular - Ensino Médio Regular articulado ao Itinerário Formativo Técnico Profissional (IFTP) - Curso Técnico - 1º ano/1ª Série |
| `quantidade_mat_med_iftp_ct_2` | INTEGER | Número de Matrículas do Ensino Médio Regular - Ensino Médio Regular articulado ao Itinerário Formativo Técnico Profissional (IFTP) - Curso Técnico - 2º ano/2ª Série |
| `quantidade_mat_med_iftp_ct_3` | INTEGER | Número de Matrículas do Ensino Médio Regular - Ensino Médio Regular articulado ao Itinerário Formativo Técnico Profissional (IFTP) - Curso Técnico - 3º ano/3ª Série |
| `quantidade_mat_med_iftp_ct_4` | INTEGER | Número de Matrículas do Ensino Médio Regular - Ensino Médio Regular articulado ao Itinerário Formativo Técnico Profissional (IFTP) - Curso Técnico - 4º ano/4ª Série |
| `quantidade_mat_med_iftp_ct_ns` | INTEGER | Número de Matrículas do Ensino Médio Regular - Ensino Médio Regular articulado ao Itinerário Formativo Técnico Profissional (IFTP) - Curso Técnico - Não Seriado |
| `quantidade_mat_med_iftp_qp` | INTEGER | Número de Matrículas do Ensino Médio Regular - Ensino Médio Regular articulado ao Itinerário Formativo Técnico Profissional (IFTP) - Qualificação Profissional |
| `quantidade_mat_med_iftp_qp_1` | INTEGER | Número de Matrículas do Ensino Médio Regular - Ensino Médio Regular articulado ao Itinerário Formativo Técnico Profissional (IFTP) - Qualificação Profissional - 1º ano/1ª Série |
| `quantidade_mat_med_iftp_qp_2` | INTEGER | Número de Matrículas do Ensino Médio Regular - Ensino Médio Regular articulado ao Itinerário Formativo Técnico Profissional (IFTP) - Qualificação Profissional - 2º ano/2ª Série |
| `quantidade_mat_med_iftp_qp_3` | INTEGER | Número de Matrículas do Ensino Médio Regular - Ensino Médio Regular articulado ao Itinerário Formativo Técnico Profissional (IFTP) - Qualificação Profissional - 3º ano/3ª Série |
| `quantidade_mat_med_iftp_qp_4` | INTEGER | Número de Matrículas do Ensino Médio Regular - Ensino Médio Regular articulado ao Itinerário Formativo Técnico Profissional (IFTP) - Qualificação Profissional - 4º ano/4ª Série |
| `quantidade_mat_med_iftp_qp_ns` | INTEGER | Número de Matrículas do Ensino Médio Regular - Ensino Médio Regular articulado ao Itinerário Formativo Técnico Profissional (IFTP) - Qualificação Profissional - Não Seriado |
| `quantidade_mat_med_ifa` | INTEGER | Número de Matrículas do Ensino Médio Regular - Itinerário formativo de aprofundamento (IFA). Percursos educacionais estruturados de livre escolha dos estudantes, que permite aos educandos o aprofundam |
| `quantidade_mat_med_ifa_ling` | INTEGER | Número de Matrículas do Ensino Médio Regular - Área do Itinerário formativo de aprofundamento (IFA) - Linguagens e suas tecnologias |
| `quantidade_mat_med_ifa_ling_mt` | INTEGER | Número de Matrículas do Ensino Médio Regular - Área do Itinerário formativo de aprofundamento (IFA) - Linguagens e suas tecnologias na mesma turma |
| `quantidade_mat_med_ifa_ling_otme` | INTEGER | Número de Matrículas do Ensino Médio Regular - Área do Itinerário formativo de aprofundamento (IFA) - Linguagens e suas tecnologias em outra turma da mesma escola |
| `quantidade_mat_med_ifa_ling_oe` | INTEGER | Número de Matrículas do Ensino Médio Regular - Área do Itinerário formativo de aprofundamento (IFA) - Linguagens e suas tecnologias em outra escola |
| `quantidade_mat_med_ifa_mate` | INTEGER | Número de Matrículas do Ensino Médio Regular - Área do Itinerário formativo de aprofundamento (IFA) - Matemática e suas tecnologias |
| `quantidade_mat_med_ifa_mate_mt` | INTEGER | Número de Matrículas do Ensino Médio Regular - Área do Itinerário formativo de aprofundamento (IFA) - Matemática e suas tecnologias na mesma turma |
| `quantidade_mat_med_ifa_mate_otme` | INTEGER | Número de Matrículas do Ensino Médio Regular - Área do Itinerário formativo de aprofundamento (IFA) - Matemática e suas tecnologias em outra turma da mesma escola |
| `quantidade_mat_med_ifa_mate_oe` | INTEGER | Número de Matrículas do Ensino Médio Regular - Área do Itinerário formativo de aprofundamento (IFA) - Matemática e suas tecnologias em outra escola |
| `quantidade_mat_med_ifa_cienc` | INTEGER | Número de Matrículas do Ensino Médio Regular - Área do Itinerário formativo de aprofundamento (IFA) - Ciências da natureza e suas tecnologias |
| `quantidade_mat_med_ifa_cienc_mt` | INTEGER | Número de Matrículas do Ensino Médio Regular - Área do Itinerário formativo de aprofundamento (IFA) - Ciências da natureza e suas tecnologias na mesma turma |
| `quantidade_mat_med_ifa_cienc_otme` | INTEGER | Número de Matrículas do Ensino Médio Regular - Área do Itinerário formativo de aprofundamento (IFA) - Ciências da natureza e suas tecnologias em outra turma da mesma escola |
| `quantidade_mat_med_ifa_cienc_oe` | INTEGER | Número de Matrículas do Ensino Médio Regular - Área do Itinerário formativo de aprofundamento (IFA) - Ciências da natureza e suas tecnologias em outra escola |
| `quantidade_mat_med_ifa_huma` | INTEGER | Número de Matrículas do Ensino Médio Regular - Área do Itinerário formativo de aprofundamento (IFA) - Ciências humanas e sociais aplicadas |
| `quantidade_mat_med_ifa_huma_mt` | INTEGER | Número de Matrículas do Ensino Médio Regular - Área do Itinerário formativo de aprofundamento (IFA) - Ciências humanas e sociais aplicadas na mesma turma |
| `quantidade_mat_med_ifa_huma_otme` | INTEGER | Número de Matrículas do Ensino Médio Regular - Área do Itinerário formativo de aprofundamento (IFA) - Ciências humanas e sociais aplicadas em outra turma da mesma escola |
| `quantidade_mat_med_ifa_huma_oe` | INTEGER | Número de Matrículas do Ensino Médio Regular - Área do Itinerário formativo de aprofundamento (IFA) - Ciências humanas e sociais aplicadas em outra escola |
| `quantidade_mat_med_arti_iftp_ct` | INTEGER | Número de Matrículas do Ensino Médio Regular (Propedêutico ou Normal/Magistério) articuladas ao Curso Técnico do Itinerário Formativo Técnico Profissional (IFTP) - Curso Técnico |
| `quantidade_mat_med_arti_iftp_ct_mt` | INTEGER | Número de Matrículas do Ensino Médio Regular (Propedêutico ou Normal/Magistério) articuladas ao Curso Técnico do Itinerário Formativo Técnico Profissional (IFTP) - Curso Técnico na mesma turma |
| `quantidade_mat_med_arti_iftp_ct_otme` | INTEGER | Número de Matrículas do Ensino Médio Regular (Propedêutico ou Normal/Magistério) articuladas ao Curso Técnico do Itinerário Formativo Técnico Profissional (IFTP) - Curso Técnico em outra turma da mesm |
| `quantidade_mat_med_arti_iftp_ct_oe` | INTEGER | Número de Matrículas do Ensino Médio Regular (Propedêutico ou Normal/Magistério) articuladas ao Curso Técnico do Itinerário Formativo Técnico Profissional (IFTP) - Curso Técnico em outra escola |
| `quantidade_mat_med_arti_iftp_qp` | INTEGER | Número de Matrículas do Ensino Médio Regular (Propedêutico ou Normal/Magistério) articuladas ao Curso Técnico do Itinerário Formativo Técnico Profissional (IFTP) - Qualificação Profissional |
| `quantidade_mat_med_arti_iftp_qp_mt` | INTEGER | Número de Matrículas do Ensino Médio Regular (Propedêutico ou Normal/Magistério) articuladas ao Curso Técnico do Itinerário Formativo Técnico Profissional (IFTP) - Qualificação Profissional na mesma t |
| `quantidade_mat_med_arti_iftp_qp_otme` | INTEGER | Número de Matrículas do Ensino Médio Regular (Propedêutico ou Normal/Magistério) articuladas ao Curso Técnico do Itinerário Formativo Técnico Profissional (IFTP) - Qualificação Profissional em outra t |
| `quantidade_mat_med_arti_iftp_qp_oe` | INTEGER | Número de Matrículas do Ensino Médio Regular (Propedêutico ou Normal/Magistério) articuladas ao Curso Técnico do Itinerário Formativo Técnico Profissional (IFTP) - Qualificação Profissional em outra e |
| `quantidade_mat_prof_tec_iftp_ct` | INTEGER | Número de Matrículas da Educação Profissional Técnica - Itinerário Formativo Técnico Profissional (IFTP) Exclusivo - Curso Técnico (não articulado ao ensino médio regular) |
| `quantidade_mat_prof_nao_tec` | INTEGER | Número de Matrículas da Educação Profissional Não-Técnica |
| `quantidade_mat_prof_iftp_qp` | INTEGER | Número de Matrículas da Educação Profissional - Itinerário Formativo Técnico Profissional (IFTP) Exclusivo - Qualificação Profissional (não articulado ao ensino médio regular) |
| `quantidade_mat_eja_fund_nprof` | INTEGER | Número de Matrículas da Educação de Jovens e Adultos (EJA) - Ensino Fundamental - Sem componente profissionalizante |
| `quantidade_mat_esp_inf` | INTEGER | Número de Matrículas da Educação Especial - Educação Infantil |
| `quantidade_mat_esp_inf_cre` | INTEGER | Número de Matrículas da Educação Especial - Educação Infantil - Creche |
| `quantidade_mat_esp_inf_pre` | INTEGER | Número de Matrículas da Educação Especial - Educação Infantil - Pré-Escola |
| `quantidade_mat_esp_fund` | INTEGER | Número de Matrículas da Educação Especial - Ensino Fundamental |
| `quantidade_mat_esp_fund_ai` | INTEGER | Número de Matrículas da Educação Especial - Ensino Fundamental - Anos Iniciais |
| `quantidade_mat_esp_fund_af` | INTEGER | Número de Matrículas da Educação Especial - Ensino Fundamental - Anos Finais |
| `quantidade_mat_esp_med` | INTEGER | Número de Matrículas da Educação Especial - Ensino Médio |
| `quantidade_mat_esp_prof` | INTEGER | Número de Matrículas da Educação Especial - Educação Profissional |
| `quantidade_mat_esp_prof_tec` | INTEGER | Número de Matrículas da Educação Especial - Educação Profissional Técnica |
| `quantidade_mat_esp_eja` | INTEGER | Número de Matrículas da Educação Especial - Educação de Jovens e Adultos (EJA) |
| `quantidade_mat_esp_eja_fund` | INTEGER | Número de Matrículas da Educação Especial - Educação de Jovens e Adultos (EJA) - Ensino Fundamental |
| `quantidade_mat_esp_eja_med` | INTEGER | Número de Matrículas da Educação Especial - Educação de Jovens e Adultos (EJA) - Ensino Médio |
| `quantidade_mat_esp_cc_inf` | INTEGER | Número de Matrículas da Educação Especial em Classes Comuns - Educação Infantil |
| `quantidade_mat_esp_cc_inf_cre` | INTEGER | Número de Matrículas da Educação Especial em Classes Comuns - Educação Infantil - Creche |
| `quantidade_mat_esp_cc_inf_pre` | INTEGER | Número de Matrículas da Educação Especial em Classes Comuns - Educação Infantil - Pré-Escola |
| `quantidade_mat_esp_cc_fund` | INTEGER | Número de Matrículas da Educação Especial em Classes Comuns - Ensino Fundamental |
| `quantidade_mat_esp_cc_fund_ai` | INTEGER | Número de Matrículas da Educação Especial em Classes Comuns - Ensino Fundamental - Anos Iniciais |
| `quantidade_mat_esp_cc_fund_af` | INTEGER | Número de Matrículas da Educação Especial em Classes Comuns - Ensino Fundamental - Anos Finais |
| `quantidade_mat_esp_cc_med` | INTEGER | Número de Matrículas da Educação Especial em Classes Comuns - Ensino Médio |
| `quantidade_mat_esp_cc_prof` | INTEGER | Número de Matrículas da Educação Especial em Classes Comuns - Educação Profissional |
| `quantidade_mat_esp_cc_prof_tec` | INTEGER | Número de Matrículas da Educação Especial em Classes Comuns - Educação Profissional Técnica |
| `quantidade_mat_esp_cc_eja` | INTEGER | Número de Matrículas da Educação Especial em Classes Comuns - Educação de Jovens e Adultos (EJA) |
| `quantidade_mat_esp_cc_eja_fund` | INTEGER | Número de Matrículas da Educação Especial em Classes Comuns - Educação de Jovens e Adultos (EJA) - Ensino Fundamental |
| `quantidade_mat_esp_cc_eja_med` | INTEGER | Número de Matrículas da Educação Especial em Classes Comuns - Educação de Jovens e Adultos (EJA) - Ensino Médio |
| `quantidade_mat_esp_ce_inf` | INTEGER | Número de Matrículas da Educação Especial em Classes Exclusivas - Educação Infantil |
| `quantidade_mat_esp_ce_inf_cre` | INTEGER | Número de Matrículas da Educação Especial em Classes Exclusivas - Educação Infantil - Creche |
| `quantidade_mat_esp_ce_inf_pre` | INTEGER | Número de Matrículas da Educação Especial em Classes Exclusivas - Educação Infantil - Pré-Escola |
| `quantidade_mat_esp_ce_fund` | INTEGER | Número de Matrículas da Educação Especial em Classes Exclusivas - Ensino Fundamental |
| `quantidade_mat_esp_ce_fund_ai` | INTEGER | Número de Matrículas da Educação Especial em Classes Exclusivas - Ensino Fundamental - Anos Iniciais |
| `quantidade_mat_esp_ce_fund_af` | INTEGER | Número de Matrículas da Educação Especial em Classes Exclusivas - Ensino Fundamental - Anos Finais |
| `quantidade_mat_esp_ce_med` | INTEGER | Número de Matrículas da Educação Especial em Classes Exclusivas - Ensino Médio |
| `quantidade_mat_esp_ce_prof` | INTEGER | Número de Matrículas da Educação Especial em Classes Exclusivas - Educação Profissional |
| `quantidade_mat_esp_ce_prof_tec` | INTEGER | Número de Matrículas da Educação Especial em Classes Exclusivas - Educação Profissional Técnica |
| `quantidade_mat_esp_ce_eja` | INTEGER | Número de Matrículas da Educação Especial em Classes Exclusivas - Educação de Jovens e Adultos (EJA) |
| `quantidade_mat_esp_ce_eja_fund` | INTEGER | Número de Matrículas da Educação Especial em Classes Exclusivas - Educação de Jovens e Adultos (EJA) - Ensino Fundamental |
| `quantidade_mat_esp_ce_eja_med` | INTEGER | Número de Matrículas da Educação Especial em Classes Exclusivas - Educação de Jovens e Adultos (EJA) - Ensino Médio |
| `quantidade_mat_bas_0_3_ref_31_03` | INTEGER | Número de Matrículas da Educação Básica - Até 3 anos de idade na data de referência (31 de março de 2025) |
| `quantidade_mat_bas_4_5_ref_31_03` | INTEGER | Número de Matrículas da Educação Básica - Entre 4 e 5 anos de idade na data de referência (31 de março de 2025) |
| `quantidade_mat_bas_6_10_ref_31_03` | INTEGER | Número de Matrículas da Educação Básica - Entre 6 e 10 anos de idade na data de referência (31 de março de 2025) |
| `quantidade_mat_bas_11_14_ref_31_03` | INTEGER | Número de Matrículas da Educação Básica - Entre 11 e 14 anos de idade na data de referência (31 de março de 2025) |
| `quantidade_mat_bas_15_17_ref_31_03` | INTEGER | Número de Matrículas da Educação Básica - Entre 15 e 17 anos de idade na data de referência (31 de março de 2025) |
| `quantidade_mat_bas_18_mais_ref_31_03` | INTEGER | Número de Matrículas da Educação Básica - Com 18 ou mais anos de idade na data de referência do Censo Escolar (última quarta-feira do mês de maio de 2025) |
| `quantidade_mat_bas_dm` | INTEGER | Número de Matrículas da Educação Básica - Turno Diurno - Matutino |
| `quantidade_mat_bas_dv` | INTEGER | Número de Matrículas da Educação Básica - Turno Diurno - Vespertino |
| `quantidade_mat_inf_cre_d` | INTEGER | Número de Matrículas da Educação Infantil - Creche - Turno Diurno |
| `quantidade_mat_inf_cre_dm` | INTEGER | Número de Matrículas da Educação Infantil - Creche - Turno Diurno - Matutino |
| `quantidade_mat_inf_cre_dv` | INTEGER | Número de Matrículas da Educação Infantil - Creche - Turno Diurno - Vespertino |
| `quantidade_mat_inf_cre_n` | INTEGER | Número de Matrículas da Educação Infantil - Creche - Turno Noturno |
| `quantidade_mat_inf_pre_d` | INTEGER | Número de Matrículas da Educação Infantil - Pré-Escola - Turno Diurno |
| `quantidade_mat_inf_pre_dm` | INTEGER | Número de Matrículas da Educação Infantil - Pré-Escola - Turno Diurno - Matutino |
| `quantidade_mat_inf_pre_dv` | INTEGER | Número de Matrículas da Educação Infantil - Pré-Escola - Turno Diurno - Vespertino |
| `quantidade_mat_inf_pre_n` | INTEGER | Número de Matrículas da Educação Infantil - Pré-Escola - Turno Noturno |
| `quantidade_mat_fund_d` | INTEGER | Número de Matrículas do Ensino Fundamental - Turno Diurno |
| `quantidade_mat_fund_dm` | INTEGER | Número de Matrículas do Ensino Fundamental - Turno Diurno - Matutino |
| `quantidade_mat_fund_dv` | INTEGER | Número de Matrículas do Ensino Fundamental - Turno Diurno - Vespertino |
| `quantidade_mat_fund_n` | INTEGER | Número de Matrículas do Ensino Fundamental - Turno Noturno |
| `quantidade_mat_fund_ai_d` | INTEGER | Número de Matrículas do Ensino Fundamental - Anos Iniciais - Turno Diurno |
| `quantidade_mat_fund_ai_dm` | INTEGER | Número de Matrículas do Ensino Fundamental - Anos Iniciais - Turno Diurno - Matutino |
| `quantidade_mat_fund_ai_dv` | INTEGER | Número de Matrículas do Ensino Fundamental - Anos Iniciais - Turno Diurno - Vespertino |
| `quantidade_mat_fund_ai_n` | INTEGER | Número de Matrículas do Ensino Fundamental - Anos Iniciais - Turno Noturno |
| `quantidade_mat_fund_af_d` | INTEGER | Número de Matrículas do Ensino Fundamental - Anos Finais - Turno Diurno |
| `quantidade_mat_fund_af_dm` | INTEGER | Número de Matrículas do Ensino Fundamental - Anos Finais - Turno Diurno - Matutino |
| `quantidade_mat_fund_af_dv` | INTEGER | Número de Matrículas do Ensino Fundamental - Anos Finais - Turno Diurno - Vespertino |
| `quantidade_mat_fund_af_n` | INTEGER | Número de Matrículas do Ensino Fundamental - Anos Finais - Turno Noturno |
| `quantidade_mat_med_d` | INTEGER | Número de Matrículas do Ensino Médio - Turno Diurno |
| `quantidade_mat_med_dm` | INTEGER | Número de Matrículas do Ensino Médio - Turno Diurno - Matutino |
| `quantidade_mat_med_dv` | INTEGER | Número de Matrículas do Ensino Médio - Turno Diurno - Vespertino |
| `quantidade_mat_med_n` | INTEGER | Número de Matrículas do Ensino Médio - Turno Noturno |
| `quantidade_mat_med_ead` | INTEGER | Número de Matrículas do Ensino Médio - Turno não aplicável para turmas semipresenciais ou de Educação a Distância (EAD) |
| `quantidade_mat_prof_d` | INTEGER | Número de Matrículas da Educação Profissional - Turno Diurno |
| `quantidade_mat_prof_dm` | INTEGER | Número de Matrículas da Educação Profissional - Turno Diurno - Matutino |
| `quantidade_mat_prof_dv` | INTEGER | Número de Matrículas da Educação Profissional - Turno Diurno - Vespertino |
| `quantidade_mat_prof_n` | INTEGER | Número de Matrículas da Educação Profissional - Turno Noturno |
| `quantidade_mat_prof_ead` | INTEGER | Número de Matrículas da Educação Profissional - Turno não aplicável para turmas semipresenciais ou de Educação a Distância (EAD) |
| `quantidade_mat_prof_tec_d` | INTEGER | Número de Matrículas da Educação Profissional Técnica - Turno Diurno |
| `quantidade_mat_prof_tec_dm` | INTEGER | Número de Matrículas da Educação Profissional Técnica - Turno Diurno - Matutino |
| `quantidade_mat_prof_tec_dv` | INTEGER | Número de Matrículas da Educação Profissional Técnica - Turno Diurno - Vespertino |
| `quantidade_mat_prof_tec_n` | INTEGER | Número de Matrículas da Educação Profissional Técnica - Turno Noturno |
| `quantidade_mat_prof_tec_ead` | INTEGER | Número de Matrículas da Educação Profissional Técnica - Turno não aplicável para turmas semipresenciais ou de Educação a Distância (EAD) |
| `quantidade_mat_eja_d` | INTEGER | Número de Matrículas da Educação de Jovens e Adultos (EJA) - Turno Diurno |
| `quantidade_mat_eja_dm` | INTEGER | Número de Matrículas da Educação de Jovens e Adultos (EJA) - Turno Diurno - Matutino |
| `quantidade_mat_eja_dv` | INTEGER | Número de Matrículas da Educação de Jovens e Adultos (EJA) - Turno Diurno - Vespertino |
| `quantidade_mat_eja_n` | INTEGER | Número de Matrículas da Educação de Jovens e Adultos (EJA) - Turno Noturno |
| `quantidade_mat_eja_ead` | INTEGER | Número de Matrículas da Educação de Jovens e Adultos (EJA) - Turno não aplicável para turmas semipresenciais ou de Educação a Distância (EAD) |
| `quantidade_mat_eja_fund_d` | INTEGER | Número de Matrículas da Educação de Jovens e Adultos (EJA) - Ensino Fundamental - Turno Diurno |
| `quantidade_mat_eja_fund_dm` | INTEGER | Número de Matrículas da Educação de Jovens e Adultos (EJA) - Ensino Fundamental - Turno Diurno - Matutino |
| `quantidade_mat_eja_fund_dv` | INTEGER | Número de Matrículas da Educação de Jovens e Adultos (EJA) - Ensino Fundamental - Turno Diurno - Vespertino |
| `quantidade_mat_eja_fund_n` | INTEGER | Número de Matrículas da Educação de Jovens e Adultos (EJA) - Ensino Fundamental - Turno Noturno |
| `quantidade_mat_eja_fund_ead` | INTEGER | Número de Matrículas da Educação de Jovens e Adultos (EJA) - Ensino Fundamental - Turno não aplicável para turmas semipresenciais ou de Educação a Distância (EAD) |
| `quantidade_mat_eja_med_d` | INTEGER | Número de Matrículas da Educação de Jovens e Adultos (EJA) - Ensino Médio - Turno Diurno |
| `quantidade_mat_eja_med_dm` | INTEGER | Número de Matrículas da Educação de Jovens e Adultos (EJA) - Ensino Médio - Turno Diurno - Matutino |
| `quantidade_mat_eja_med_dv` | INTEGER | Número de Matrículas da Educação de Jovens e Adultos (EJA) - Ensino Médio - Turno Diurno - Vespertino |
| `quantidade_mat_eja_med_n` | INTEGER | Número de Matrículas da Educação de Jovens e Adultos (EJA) - Ensino Médio - Turno Noturno |
| `quantidade_mat_eja_med_ead` | INTEGER | Número de Matrículas da Educação de Jovens e Adultos (EJA) - Ensino Médio - Turno não aplicável para turmas semipresenciais ou de Educação a Distância (EAD) |
| `quantidade_mat_esp_d` | INTEGER | Número de Matrículas da Educação Especial - Turno Diurno |
| `quantidade_mat_esp_dm` | INTEGER | Número de Matrículas da Educação Especial - Turno Diurno - Matutino |
| `quantidade_mat_esp_dv` | INTEGER | Número de Matrículas da Educação Especial - Turno Diurno - Vespertino |
| `quantidade_mat_esp_n` | INTEGER | Número de Matrículas da Educação Especial - Turno Noturno |
| `quantidade_mat_esp_ead` | INTEGER | Número de Matrículas da Educação Especial - Turno não aplicável para turmas semipresenciais ou de Educação a Distância (EAD) |
| `quantidade_mat_esp_cc_d` | INTEGER | Número de Matrículas da Educação Especial em Classes Comuns - Turno Diurno |
| `quantidade_mat_esp_cc_dm` | INTEGER | Número de Matrículas da Educação Especial em Classes Comuns - Turno Diurno - Matutino |
| `quantidade_mat_esp_cc_dv` | INTEGER | Número de Matrículas da Educação Especial em Classes Comuns - Turno Diurno - Vespertino |
| `quantidade_mat_esp_cc_n` | INTEGER | Número de Matrículas da Educação Especial em Classes Comuns - Turno Noturno |
| `quantidade_mat_esp_cc_ead` | INTEGER | Número de Matrículas da Educação Especial em Classes Comuns - Turno não aplicável para turmas semipresenciais ou de Educação a Distância (EAD) |
| `quantidade_mat_esp_ce_d` | INTEGER | Número de Matrículas da Educação Especial em Classes Exclusivas - Turno Diurno |
| `quantidade_mat_esp_ce_dm` | INTEGER | Número de Matrículas da Educação Especial em Classes Exclusivas - Turno Diurno - Matutino |
| `quantidade_mat_esp_ce_dv` | INTEGER | Número de Matrículas da Educação Especial em Classes Exclusivas - Turno Diurno - Vespertino |
| `quantidade_mat_esp_ce_n` | INTEGER | Número de Matrículas da Educação Especial em Classes Exclusivas - Turno Noturno |
| `quantidade_mat_esp_ce_ead` | INTEGER | Número de Matrículas da Educação Especial em Classes Exclusivas - Turno não aplicável para turmas semipresenciais ou de Educação a Distância (EAD) |
| `quantidade_mat_bas_int` | INTEGER | Número de Matrículas da Educação Básica - Tempo Integral |
| `quantidade_mat_prof_int` | INTEGER | Número de Matrículas da Educação Profissional - Tempo Integral |
| `quantidade_mat_prof_tec_int` | INTEGER | Número de Matrículas da Educação Profissional Técnica - Tempo Integral |
| `quantidade_mat_eja_int` | INTEGER | Número de Matrículas da Educação de Jovens e Adultos (EJA) - Tempo Integral |
| `quantidade_mat_eja_fund_int` | INTEGER | Número de Matrículas da Educação de Jovens e Adultos (EJA) - Ensino Fundamental - Tempo Integral |
| `quantidade_mat_eja_med_int` | INTEGER | Número de Matrículas da Educação de Jovens e Adultos (EJA) - Ensino Médio - Tempo Integral |
| `quantidade_mat_esp_int` | INTEGER | Número de Matrículas da Educação Especial - Tempo Integral |
| `quantidade_mat_esp_cc_int` | INTEGER | Número de Matrículas da Educação Especial em Classes Comuns - Tempo Integral |
| `quantidade_mat_esp_ce_int` | INTEGER | Número de Matrículas da Educação Especial em Classes Exclusivas - Tempo Integral |
| `quantidade_mat_bas_libras` | INTEGER | Número de Matrículas da Educação Básica - Classe bilíngue de surdos tendo a Libras (Língua Brasileira de Sinais) como língua de instrução, ensino, comunicação e interação e a língua portuguesa escrita |

## semantic · obt_inep_censo_municipio_ano

File `semantic__obt_inep_censo_municipio_ano.parquet` · 170,578 rows · 32 columns

Censo Escolar — agregacao por municipio e ano. Grao: 1 linha por (codigo_municipio, ano). Contagens de escolas por dependência e localização + somas de QT_MAT/DOC/TUR. FK: codigo_municipio → obt_ibge_municipio. Origem: semantic/obt_inep_censo_escola/matricula/docente/turma_escola_ano. INEP Censo Escolar dados.gov.br.

**Built from:** `semantic/obt_inep_censo_docente_escola_ano`, `semantic/obt_inep_censo_escola_ano`, `semantic/obt_inep_censo_matricula_escola_ano`, `semantic/obt_inep_censo_turma_escola_ano`

| Column | Type | Description |
|---|---|---|
| `codigo_municipio` | INTEGER | Código IBGE 7 dígitos do município. INT64. PK composta com ano. FK para obt_ibge_municipio. |
| `ano` | INTEGER | Ano do Censo Escolar. INT64. PK composta com codigo_municipio. |
| `nome_municipio` | STRING | Nome do município. |
| `sigla_uf` | STRING | Sigla 2 letras da UF. |
| `codigo_uf` | INTEGER | Código IBGE 2 dígitos da UF. INT64. |
| `nome_uf` | STRING | Nome completo da UF. |
| `codigo_regiao` | INTEGER | Código IBGE 1 dígito da região. INT64. |
| `nome_regiao` | STRING | Nome da região geográfica. |
| `quantidade_escolas` | INTEGER | Total de escolas do município no Censo deste ano. |
| `quantidade_escolas_ativas` | INTEGER | Escolas em situação de funcionamento ativo (TP_SITUACAO_FUNCIONAMENTO = 1). |
| `quantidade_escolas_federal` | INTEGER | Escolas federais (TP_DEPENDENCIA = 1). |
| `quantidade_escolas_estadual` | INTEGER | Escolas estaduais (TP_DEPENDENCIA = 2). |
| `quantidade_escolas_municipal` | INTEGER | Escolas municipais (TP_DEPENDENCIA = 3). |
| `quantidade_escolas_privada` | INTEGER | Escolas privadas (TP_DEPENDENCIA = 4). |
| `quantidade_escolas_urbana` | INTEGER | Escolas em localização urbana (TP_LOCALIZACAO = 1). |
| `quantidade_escolas_rural` | INTEGER | Escolas em localização rural (TP_LOCALIZACAO = 2). |
| `quantidade_mat_total` | INTEGER | Total de matrículas na Educação Básica (QT_MAT_BAS). |
| `quantidade_mat_infantil` | INTEGER | Matrículas em Educação Infantil (QT_MAT_INF). |
| `quantidade_mat_creche` | INTEGER | Matrículas em creche (QT_MAT_INF_CRE). |
| `quantidade_mat_pre_escola` | INTEGER | Matrículas em pré-escola (QT_MAT_INF_PRE). |
| `quantidade_mat_fundamental` | INTEGER | Matrículas no Ensino Fundamental (QT_MAT_FUND). |
| `quantidade_mat_fund_anos_iniciais` | INTEGER | Matrículas nos anos iniciais do Fundamental (QT_MAT_FUND_AI). |
| `quantidade_mat_fund_anos_finais` | INTEGER | Matrículas nos anos finais do Fundamental (QT_MAT_FUND_AF). |
| `quantidade_mat_medio` | INTEGER | Matrículas no Ensino Médio (QT_MAT_MED). |
| `quantidade_mat_eja` | INTEGER | Matrículas na EJA (QT_MAT_EJA). |
| `quantidade_mat_especial` | INTEGER | Matrículas na Educação Especial (QT_MAT_ESP). |
| `quantidade_mat_feminino` | INTEGER | Matrículas femininas na Educação Básica (QT_MAT_BAS_FEM). |
| `quantidade_mat_masculino` | INTEGER | Matrículas masculinas na Educação Básica (QT_MAT_BAS_MASC). |
| `quantidade_docentes` | INTEGER | Total de docentes na Educação Básica (QT_DOC_BAS). |
| `quantidade_turmas` | INTEGER | Total de turmas na Educação Básica (QT_TUR_BAS). |
| `id_municipio_ano` | STRING | ID composto municipio_ano para joins: CAST(codigo_municipio AS STRING) + _ + CAST(ano AS STRING). |
| `data_carga_semantica` | TIMESTAMP | Timestamp UTC de geração da tabela. |

## semantic · obt_inep_censo_municipio_rede_ano

File `semantic__obt_inep_censo_municipio_rede_ano.parquet` · 352,866 rows · 30 columns

Censo Escolar agregado por municipio, ano e dependencia administrativa. Grao: 1 linha por (codigo_municipio, ano, codigo_dependencia_administrativa). Permite filtrar totais por rede Federal, Estadual, Municipal e Privada sem alterar a OBT larga municipio_ano.

**Built from:** `semantic/obt_inep_censo_docente_escola_ano`, `semantic/obt_inep_censo_escola_ano`, `semantic/obt_inep_censo_matricula_escola_ano`, `semantic/obt_inep_censo_turma_escola_ano`

| Column | Type | Description |
|---|---|---|
| `codigo_municipio` | INTEGER | Codigo IBGE 7 digitos do municipio. FK para obt_ibge_municipio. |
| `nome_municipio` | STRING | Nome do municipio. |
| `codigo_uf` | INTEGER | Codigo IBGE da UF. |
| `nome_uf` | STRING | Nome da UF. |
| `sigla_uf` | STRING | Sigla da UF. |
| `codigo_regiao` | INTEGER | Codigo IBGE da regiao. |
| `nome_regiao` | STRING | Nome da regiao geografica. |
| `ano` | INTEGER | Ano do Censo Escolar. |
| `codigo_dependencia_administrativa` | INTEGER | Codigo da dependencia administrativa: 1 Federal, 2 Estadual, 3 Municipal, 4 Privada. |
| `dependencia_administrativa` | STRING | Nome da dependencia administrativa. |
| `quantidade_escolas` | INTEGER | Quantidade total de estabelecimentos cadastrados no município para a rede. — descrição gerada por IA. |
| `quantidade_escolas_ativas` | INTEGER | Quantidade de escolas em funcionamento ativo na referida rede e município. — descrição gerada por IA. |
| `quantidade_escolas_urbana` | INTEGER | Quantidade de escolas localizadas em zona urbana. — descrição gerada por IA. |
| `quantidade_escolas_rural` | INTEGER | Quantidade de escolas localizadas em zona rural. — descrição gerada por IA. |
| `quantidade_mat_total` | INTEGER | Total geral de matrículas na rede de ensino do município no ano. — descrição gerada por IA. |
| `quantidade_mat_infantil` | INTEGER | Total de matrículas na Educação Infantil. — descrição gerada por IA. |
| `quantidade_mat_creche` | INTEGER | Total de matrículas na etapa de Creche. — descrição gerada por IA. |
| `quantidade_mat_pre_escola` | INTEGER | Total de matrículas na etapa de Pré-Escola. — descrição gerada por IA. |
| `quantidade_mat_fundamental` | INTEGER | Total de matrículas no Ensino Fundamental. — descrição gerada por IA. |
| `quantidade_mat_fund_anos_iniciais` | INTEGER | Total de matrículas nos Anos Iniciais do Ensino Fundamental (1º ao 5º ano). — descrição gerada por IA. |
| `quantidade_mat_fund_anos_finais` | INTEGER | Total de matrículas nos Anos Finais do Ensino Fundamental (6º ao 9º ano). — descrição gerada por IA. |
| `quantidade_mat_medio` | INTEGER | Total de matrículas no Ensino Médio. — descrição gerada por IA. |
| `quantidade_mat_eja` | INTEGER | Total de matrículas na Educação de Jovens e Adultos (EJA). — descrição gerada por IA. |
| `quantidade_mat_especial` | INTEGER | Total de matrículas na Educação Especial. — descrição gerada por IA. |
| `quantidade_mat_feminino` | INTEGER | Total de alunos do sexo feminino. — descrição gerada por IA. |
| `quantidade_mat_masculino` | INTEGER | Total de alunos do sexo masculino. — descrição gerada por IA. |
| `quantidade_docentes` | INTEGER | Número total de docentes atuantes. — descrição gerada por IA. |
| `quantidade_turmas` | INTEGER | Número total de turmas ativas. — descrição gerada por IA. |
| `id_municipio_rede_ano` | STRING | Chave primária sintética no formato {codigo_municipio}-{ano}-{codigo_dependencia_administrativa}. — descrição gerada por IA. |
| `data_carga_semantica` | TIMESTAMP | Timestamp UTC de geracao da tabela. |

## semantic · obt_inep_censo_perguntas

File `semantic__obt_inep_censo_perguntas.parquet` · 8,723 rows · 20 columns

Catálogo analítico de todos os campos/variáveis coletados no Censo Escolar INEP. Grão: 1 campo por tabela de domínio. Para cada campo informa: definição oficial (quando disponível no dicionário INEP), tabelas de origem, primeiro e último ano de disponibilidade, lista de anos em que apareceu, tipo de dado, flags de tipo (IN_*, QT_*, TP_*, CO_*, NO_*). Origem: trusted/inep_censo_escolar_dicionario_campos + inep_censo_escolar_colunas_fonte. INEP Censo Escolar dados.gov.br.

**Built from:** `trusted/inep_censo_escolar_colunas_fonte`, `trusted/inep_censo_escolar_dicionario_campos`

| Column | Type | Description |
|---|---|---|
| `campo_codigo` | STRING | Nome normalizado do campo em maiúsculas (ex: CO_ENTIDADE, IN_INTERNET, QT_MAT_BAS). PK composta com tabela_logica. |
| `tabela_logica` | STRING | Nome da tabela lógica de domínio onde o campo aparece (ex: escolas, matricula, docente, turma). PK composta com campo_codigo. |
| `descricao_oficial` | STRING | Definição oficial do campo conforme dicionário de variáveis INEP. NULL se não documentado. |
| `categoria` | STRING | Categoria temática (ex: Identificação, Infraestrutura, Matrícula, Docente). |
| `tipo_inep` | STRING | Tipo de resposta (ex: Indicador, Código, Quantidade, Data, Texto). |
| `fonte_tipo` | STRING | Tipo de documento fonte (ex: xlsx, pdf). |
| `primeiro_ano_disponivel` | INTEGER | Primeiro ano em que o campo apareceu nos arquivos CSV. |
| `ultimo_ano_disponivel` | INTEGER | Último ano em que o campo foi encontrado. Se for o mais recente, ainda está ativo. |
| `qtd_anos_disponivel` | INTEGER | Quantidade total de anos em que o campo consta nos arquivos de dados. — descrição gerada por IA. |
| `anos_disponiveis_lista` | STRING | Lista de anos com o campo, separados por vírgula. |
| `arquivos_fonte` | STRING | Arquivos CSV fonte que continham o campo, separados por vírgula. |
| `flag_indicador_booleano` | INTEGER | 1 se campo IN_* (0=Não/1=Sim); 0 caso contrário. |
| `flag_campo_quantidade` | INTEGER | 1 se campo QT_* (contagem/quantidade); 0 caso contrário. |
| `flag_campo_tipificado` | INTEGER | 1 se campo TP_* (código de tipo); 0 caso contrário. |
| `flag_campo_codigo` | INTEGER | 1 se campo CO_* (identificação/código); 0 caso contrário. |
| `flag_campo_nome` | INTEGER | 1 se campo NO_* (nomenclatura/nome); 0 caso contrário. |
| `flag_tem_definicao_dicionario` | INTEGER | 1 se existe definição oficial no dicionário INEP; 0 se sem documentação. |
| `flag_serie_historica_longa` | INTEGER | 1 se disponível de 2010 a 2020 ou além; 0 caso contrário. |
| `flag_campo_descontinuado` | INTEGER | 1 se ausente nos últimos 3 anos do Censo; 0 se ainda ativo. |
| `data_carga_semantica` | TIMESTAMP | Timestamp UTC de geração da tabela. |

## semantic · obt_inep_censo_turma_escola_ano

File `semantic__obt_inep_censo_turma_escola_ano.parquet` · 7,341,023 rows · 190 columns

Censo Escolar — contagens de turmas por escola e ano. Grao: 1 linha por (codigo_escola, ano). Colunas quantidade_tur_* (alias de QT_TUR_*). FK: codigo_escola = obt_inep_censo_escola_ano.codigo_escola. Para geografia JOIN com obt_inep_censo_escola_ano. INEP Censo Escolar dados.gov.br.

**Built from:** `raw/inep_censo_escolar_censoesc`, `semantic/obt_inep_censo_escola_ano`, `trusted/inep_censo_escolar_turmas`

**Feeds:** `semantic/obt_inep_censo_municipio_ano`, `semantic/obt_inep_censo_municipio_rede_ano`

| Column | Type | Description |
|---|---|---|
| `codigo_escola` | INTEGER | Código único INEP da escola (CO_ENTIDADE, 8 dígitos). PK composta com ano. |
| `ano` | INTEGER | Ano do Censo Escolar (NU_ANO_CENSO). INT64. PK composta com codigo_escola. |
| `quantidade_tur_bas` | INTEGER | Quantidade total de turmas de Educação Básica na escola. — descrição gerada por IA. |
| `quantidade_tur_inf` | INTEGER | Quantidade de turmas de Educação Infantil. — descrição gerada por IA. |
| `quantidade_tur_inf_cre` | INTEGER | Quantidade de turmas de Educação Infantil - Creche. — descrição gerada por IA. |
| `quantidade_tur_inf_pre` | INTEGER | Quantidade de turmas de Educação Infantil - Pré-escola. — descrição gerada por IA. |
| `quantidade_tur_fund` | INTEGER | Quantidade total de turmas de Ensino Fundamental. — descrição gerada por IA. |
| `quantidade_tur_fund_ai` | INTEGER | Quantidade de turmas de Ensino Fundamental - Anos Iniciais (1º ao 5º ano). — descrição gerada por IA. |
| `quantidade_tur_fund_af` | INTEGER | Quantidade de turmas de Ensino Fundamental - Anos Finais (6º ao 9º ano). — descrição gerada por IA. |
| `quantidade_tur_med` | INTEGER | Quantidade total de turmas de Ensino Médio. — descrição gerada por IA. |
| `quantidade_tur_prof` | INTEGER | Quantidade total de turmas de Educação Profissional. — descrição gerada por IA. |
| `quantidade_tur_prof_tec` | INTEGER | Quantidade de turmas de Educação Profissional Técnica de nível médio. — descrição gerada por IA. |
| `quantidade_tur_eja` | INTEGER | Quantidade total de turmas de Educação de Jovens e Adultos (EJA). — descrição gerada por IA. |
| `quantidade_tur_eja_fund` | INTEGER | Quantidade de turmas de EJA do Ensino Fundamental. — descrição gerada por IA. |
| `quantidade_tur_eja_med` | INTEGER | Quantidade de turmas de EJA do Ensino Médio. — descrição gerada por IA. |
| `quantidade_tur_esp` | INTEGER | Quantidade de turmas com atendimento de Educação Especial. — descrição gerada por IA. |
| `quantidade_tur_esp_cc` | INTEGER | Quantidade de turmas de Educação Especial integradas em classes comuns. — descrição gerada por IA. |
| `quantidade_tur_esp_ce` | INTEGER | Quantidade de turmas exclusivas de Educação Especial (classes ou escolas especiais). — descrição gerada por IA. |
| `quantidade_tur_bas_d` | INTEGER | Número de Turmas da Educação Básica - Turno Diurno |
| `quantidade_tur_bas_n` | INTEGER | Número de Turmas da Educação Básica - Turno Noturno |
| `quantidade_tur_bas_ead` | INTEGER | Número de Turmas da Educação Básica - Turno não aplicável para turmas semipresenciais ou de Educação a Distância (EAD) |
| `quantidade_tur_inf_int` | INTEGER | Número de Turmas da Educação Infantil - Tempo Integral |
| `quantidade_tur_inf_cre_int` | INTEGER | Número de Turmas da Educação Infantil - Creche - Tempo Integral |
| `quantidade_tur_inf_pre_int` | INTEGER | Número de Turmas da Educação Infantil - Pré-Escola - Tempo Integral |
| `quantidade_tur_fund_int` | INTEGER | Número de Turmas do Ensino Fundamental - Tempo Integral |
| `quantidade_tur_fund_ai_int` | INTEGER | Número de Turmas do Ensino Fundamental - Anos Iniciais - Tempo Integral |
| `quantidade_tur_fund_af_int` | INTEGER | Número de Turmas do Ensino Fundamental - Anos Finais - Tempo Integral |
| `quantidade_tur_med_int` | INTEGER | Número de Turmas do Ensino Médio - Tempo Integral |
| `quantidade_tur_fund_ai_1` | INTEGER | Número de Turmas do Ensino Fundamental - Anos Iniciais - 1º Ano |
| `quantidade_tur_fund_ai_2` | INTEGER | Número de Turmas do Ensino Fundamental - Anos Iniciais - 2º Ano |
| `quantidade_tur_fund_ai_3` | INTEGER | Número de Turmas do Ensino Fundamental - Anos Iniciais - 3º Ano |
| `quantidade_tur_fund_ai_4` | INTEGER | Número de Turmas do Ensino Fundamental - Anos Iniciais - 4º Ano |
| `quantidade_tur_fund_ai_5` | INTEGER | Número de Turmas do Ensino Fundamental - Anos Iniciais - 5º Ano |
| `quantidade_tur_fund_ai_multietapa` | INTEGER | Número de Turmas do Ensino Fundamental - Educação Infantil e Ensino Fundamental Multietapa |
| `quantidade_tur_fund_af_6` | INTEGER | Número de Turmas do Ensino Fundamental - Anos Finais - 6º Ano |
| `quantidade_tur_fund_af_7` | INTEGER | Número de Turmas do Ensino Fundamental - Anos Finais - 7º Ano |
| `quantidade_tur_fund_af_8` | INTEGER | Número de Turmas do Ensino Fundamental - Anos Finais - 8º Ano |
| `quantidade_tur_fund_af_9` | INTEGER | Número de Turmas do Ensino Fundamental - Anos Finais - 9º Ano |
| `quantidade_tur_fund_af_multi` | INTEGER | Número de Turmas do Ensino Fundamental - Multi |
| `quantidade_tur_fund_af_corrfluxo` | INTEGER | Número de Turmas do Ensino Fundamental - Correção de Fluxo |
| `quantidade_tur_med_prop` | INTEGER | Número de Turmas do Ensino Médio Regular - Propedêutico |
| `quantidade_tur_med_prop_1` | INTEGER | Número de Turmas do Ensino Médio Regular - Propedêutico - 1º ano/1ª Série |
| `quantidade_tur_med_prop_2` | INTEGER | Número de Turmas do Ensino Médio Regular - Propedêutico - 2º ano/2ª Série |
| `quantidade_tur_med_prop_3` | INTEGER | Número de Turmas do Ensino Médio Regular - Propedêutico - 3º ano/3ª Série |
| `quantidade_tur_med_prop_4` | INTEGER | Número de Turmas do Ensino Médio Regular - Propedêutico - 4º ano/4ª Série |
| `quantidade_tur_med_prop_ns` | INTEGER | Número de Turmas do Ensino Médio Regular - Propedêutico - Não Seriado |
| `quantidade_tur_med_iftp_ct` | INTEGER | Número de Turmas do Ensino Médio Regular - Ensino Médio Regular articulado ao Itinerário Formativo Técnico Profissional (IFTP) - Curso Técnico |
| `quantidade_tur_med_iftp_ct_1` | INTEGER | Número de Turmas do Ensino Médio Regular - Ensino Médio Regular articulado ao Itinerário Formativo Técnico Profissional (IFTP) - Curso Técnico - 1º ano/1ª Série |
| `quantidade_tur_med_iftp_ct_2` | INTEGER | Número de Turmas do Ensino Médio Regular - Ensino Médio Regular articulado ao Itinerário Formativo Técnico Profissional (IFTP) - Curso Técnico - 2º ano/2ª Série |
| `quantidade_tur_med_iftp_ct_3` | INTEGER | Número de Turmas do Ensino Médio Regular - Ensino Médio Regular articulado ao Itinerário Formativo Técnico Profissional (IFTP) - Curso Técnico - 3º ano/3ª Série |
| `quantidade_tur_med_iftp_ct_4` | INTEGER | Número de Turmas do Ensino Médio Regular - Ensino Médio Regular articulado ao Itinerário Formativo Técnico Profissional (IFTP) - Curso Técnico - 4º ano/4ª Série |
| `quantidade_tur_med_iftp_ct_ns` | INTEGER | Número de Turmas do Ensino Médio Regular - Ensino Médio Regular articulado ao Itinerário Formativo Técnico Profissional (IFTP) - Curso Técnico - Não Seriado |
| `quantidade_tur_med_iftp_qp` | INTEGER | Número de Turmas do Ensino Médio Regular - Ensino Médio Regular articulado ao Itinerário Formativo Técnico Profissional (IFTP) - Qualificação Profissional |
| `quantidade_tur_med_iftp_qp_1` | INTEGER | Número de Turmas do Ensino Médio Regular - Ensino Médio Regular articulado ao Itinerário Formativo Técnico Profissional (IFTP) - Qualificação Profissional - 1º ano/1ª Série |
| `quantidade_tur_med_iftp_qp_2` | INTEGER | Número de Turmas do Ensino Médio Regular - Ensino Médio Regular articulado ao Itinerário Formativo Técnico Profissional (IFTP) - Qualificação Profissional - 2º ano/2ª Série |
| `quantidade_tur_med_iftp_qp_3` | INTEGER | Número de Turmas do Ensino Médio Regular - Ensino Médio Regular articulado ao Itinerário Formativo Técnico Profissional (IFTP) - Qualificação Profissional - 3º ano/3ª Série |
| `quantidade_tur_med_iftp_qp_4` | INTEGER | Número de Turmas do Ensino Médio Regular - Ensino Médio Regular articulado ao Itinerário Formativo Técnico Profissional (IFTP) - Qualificação Profissional - 4º ano/4ª Série |
| `quantidade_tur_med_iftp_qp_ns` | INTEGER | Número de Turmas do Ensino Médio Regular - Ensino Médio Regular articulado ao Itinerário Formativo Técnico Profissional (IFTP) - Qualificação Profissional - Não Seriado |
| `quantidade_tur_med_nm` | INTEGER | Número de Turmas do Ensino Médio Regular - Modalidade Normal/Magistério |
| `quantidade_tur_med_nm_1` | INTEGER | Número de Turmas do Ensino Médio Regular - Modalidade Normal/Magistério - 1º ano/1ª Série |
| `quantidade_tur_med_nm_2` | INTEGER | Número de Turmas do Ensino Médio Regular - Modalidade Normal/Magistério - 2º ano/2ª Série |
| `quantidade_tur_med_nm_3` | INTEGER | Número de Turmas do Ensino Médio Regular - Modalidade Normal/Magistério - 3º ano/3ª Série |
| `quantidade_tur_med_nm_4` | INTEGER | Número de Turmas do Ensino Médio Regular - Modalidade Normal/Magistério - 4º ano/4ª Série |
| `quantidade_tur_med_ifa_exc` | INTEGER | Número de Turmas do Ensino Médio Regular - Itinerário Formativo Exclusivo - Turma de Itinerário Formativo de Aprofundamento (IFA) - Exclusivo, que possui algum aluno do Ensino Médio Regular |
| `quantidade_tur_med_iftp_exc` | INTEGER | Número de Turmas do Ensino Médio Regular - Itinerário Formativo Técnico Profissional (IFTP) Exclusivo - Curso Técnico, que possui algum aluno do Ensino Médio Regular |
| `quantidade_tur_med_iftp_exc_qp` | INTEGER | Número de Turmas do Ensino Médio Regular - Itinerário Formativo Técnico Profissional (IFTP) Exclusivo - Qualificação Profissional, que possui algum aluno do Ensino Médio Regular |
| `quantidade_tur_med_ifa` | INTEGER | Número de Matrículas do Ensino Médio Regular - Itinerário formativo de aprofundamento (IFA). Percursos educacionais estruturados de livre escolha dos estudantes, que permite aos educandos o aprofundam |
| `quantidade_tur_med_ifa_ling` | INTEGER | Número de Turmas do Ensino Médio Regular - Área do Itinerário formativo de aprofundamento (IFA) - Linguagens e suas tecnologias |
| `quantidade_tur_med_ifa_mate` | INTEGER | Número de Turmas do Ensino Médio Regular - Área do Itinerário formativo de aprofundamento (IFA) - Matemática e suas tecnologias |
| `quantidade_tur_med_ifa_cienc` | INTEGER | Número de Turmas do Ensino Médio Regular - Área do Itinerário formativo de aprofundamento (IFA) - Ciências da natureza e suas tecnologias |
| `quantidade_tur_med_ifa_huma` | INTEGER | Número de Turmas do Ensino Médio Regular - Área do Itinerário formativo de aprofundamento (IFA) - Ciências humanas e sociais aplicadas |
| `quantidade_tur_prof_tec_conc` | INTEGER | Número de Turmas da Educação Profissional Técnica - Curso Técnico Concomitante |
| `quantidade_tur_prof_tec_subs` | INTEGER | Número de Turmas da Educação Profissional Técnica - Curso Técnico Subsequente |
| `quantidade_tur_prof_tec_misto` | INTEGER | Número de Turmas da Educação Profissional Técnica - Curso Técnico Misto (Concomitante e Subsequente) |
| `quantidade_tur_prof_tec_iftp_ct` | INTEGER | Número de Turmas da Educação Profissional Técnica - Itinerário Formativo Técnico Profissional (IFTP) Exclusivo - Curso Técnico (não articulado ao ensino médio regular) |
| `quantidade_tur_prof_nao_tec` | INTEGER | Número de Turmas da Educação Profissional Não-Técnica |
| `quantidade_tur_prof_iftp_qp` | INTEGER | Número de Turmas da Educação Profissional - Itinerário Formativo Técnico Profissional (IFTP) Exclusivo - Qualificação Profissional (não articulado ao ensino médio regular) |
| `quantidade_tur_prof_fic_conc` | INTEGER | Número de Turmas da Educação Profissional - Curso FIC Concomitante |
| `quantidade_tur_eja_fund_nprof` | INTEGER | Número de Turmas da Educação de Jovens e Adultos (EJA) - Ensino Fundamental - Sem componente profissionalizante |
| `quantidade_tur_eja_fund_ai` | INTEGER | Número de Turmas da Educação de Jovens e Adultos (EJA) - Ensino Fundamental - Anos Iniciais |
| `quantidade_tur_eja_fund_af` | INTEGER | Número de Turmas da Educação de Jovens e Adultos (EJA) - Ensino Fundamental - Anos Finais |
| `quantidade_tur_eja_fund_fic` | INTEGER | Número de Turmas da Educação de Jovens e Adultos (EJA) - Ensino Fundamental - Curso FIC Integrado na Modalidade EJA de Nível Fundamental |
| `quantidade_tur_eja_med_nprof` | INTEGER | Número de Turmas da Educação de Jovens e Adultos (EJA) - Ensino Médio - Sem componente profissionalizante |
| `quantidade_tur_eja_med_fic` | INTEGER | Número de Turmas da Educação de Jovens e Adultos (EJA) - Ensino Médio - Curso FIC Integrado na Modalidade EJA de Nível Médio |
| `quantidade_tur_eja_med_tec` | INTEGER | Número de Turmas da Educação de Jovens e Adultos (EJA) - Ensino Médio - Curso Técnico Integrado na Modalidade EJA de Nível Médio |
| `quantidade_tur_bas_dm` | INTEGER | Número de Turmas da Educação Básica - Turno Diurno - Matutino |
| `quantidade_tur_bas_dv` | INTEGER | Número de Turmas da Educação Básica - Turno Diurno - Vespertino |
| `quantidade_tur_inf_cre_d` | INTEGER | Número de Turmas da Educação Infantil - Creche - Turno Diurno |
| `quantidade_tur_inf_cre_dm` | INTEGER | Número de Turmas da Educação Infantil - Creche - Turno Diurno - Matutino |
| `quantidade_tur_inf_cre_dv` | INTEGER | Número de Turmas da Educação Infantil - Creche - Turno Diurno - Vespertino |
| `quantidade_tur_inf_cre_n` | INTEGER | Número de Turmas da Educação Infantil - Creche - Turno Noturno |
| `quantidade_tur_inf_pre_d` | INTEGER | Número de Turmas da Educação Infantil - Pré-Escola - Turno Diurno |
| `quantidade_tur_inf_pre_dm` | INTEGER | Número de Turmas da Educação Infantil - Pré-Escola - Turno Diurno - Matutino |
| `quantidade_tur_inf_pre_dv` | INTEGER | Número de Turmas da Educação Infantil - Pré-Escola - Turno Diurno - Vespertino |
| `quantidade_tur_inf_pre_n` | INTEGER | Número de Turmas da Educação Infantil - Pré-Escola - Turno Noturno |
| `quantidade_tur_fund_d` | INTEGER | Número de Turmas do Ensino Fundamental - Turno Diurno |
| `quantidade_tur_fund_dm` | INTEGER | Número de Turmas do Ensino Fundamental - Turno Diurno - Matutino |
| `quantidade_tur_fund_dv` | INTEGER | Número de Turmas do Ensino Fundamental - Turno Diurno - Vespertino |
| `quantidade_tur_fund_n` | INTEGER | Número de Turmas do Ensino Fundamental - Turno Noturno |
| `quantidade_tur_fund_ai_d` | INTEGER | Número de Turmas do Ensino Fundamental - Anos Iniciais - Turno Diurno |
| `quantidade_tur_fund_ai_dm` | INTEGER | Número de Turmas do Ensino Fundamental - Anos Iniciais - Turno Diurno - Matutino |
| `quantidade_tur_fund_ai_dv` | INTEGER | Número de Turmas do Ensino Fundamental - Anos Iniciais - Turno Diurno - Vespertino |
| `quantidade_tur_fund_ai_n` | INTEGER | Número de Turmas do Ensino Fundamental - Anos Iniciais - Turno Noturno |
| `quantidade_tur_fund_af_d` | INTEGER | Número de Turmas do Ensino Fundamental - Anos Finais - Turno Diurno |
| `quantidade_tur_fund_af_dm` | INTEGER | Número de Turmas do Ensino Fundamental - Anos Finais - Turno Diurno - Matutino |
| `quantidade_tur_fund_af_dv` | INTEGER | Número de Turmas do Ensino Fundamental - Anos Finais - Turno Diurno - Vespertino |
| `quantidade_tur_fund_af_n` | INTEGER | Número de Turmas do Ensino Fundamental - Anos Finais - Turno Noturno |
| `quantidade_tur_med_d` | INTEGER | Número de Turmas do Ensino Médio - Turno Diurno |
| `quantidade_tur_med_dm` | INTEGER | Número de Turmas do Ensino Médio - Turno Diurno - Matutino |
| `quantidade_tur_med_dv` | INTEGER | Número de Turmas do Ensino Médio - Turno Diurno - Vespertino |
| `quantidade_tur_med_n` | INTEGER | Número de Turmas do Ensino Médio - Turno Noturno |
| `quantidade_tur_med_ead` | INTEGER | Número de Turmas do Ensino Médio - Turno não aplicável para turmas semipresenciais ou de Educação a Distância (EAD) |
| `quantidade_tur_prof_d` | INTEGER | Número de Turmas da Educação Profissional - Turno Diurno |
| `quantidade_tur_prof_dm` | INTEGER | Número de Turmas da Educação Profissional - Turno Diurno - Matutino |
| `quantidade_tur_prof_dv` | INTEGER | Número de Turmas da Educação Profissional - Turno Diurno - Vespertino |
| `quantidade_tur_prof_n` | INTEGER | Número de Turmas da Educação Profissional - Turno Noturno |
| `quantidade_tur_prof_ead` | INTEGER | Número de Turmas da Educação Profissional - Turno não aplicável para turmas semipresenciais ou de Educação a Distância (EAD) |
| `quantidade_tur_prof_tec_d` | INTEGER | Número de Turmas da Educação Profissional Técnica - Turno Diurno |
| `quantidade_tur_prof_tec_dm` | INTEGER | Número de Turmas da Educação Profissional Técnica - Turno Diurno - Matutino |
| `quantidade_tur_prof_tec_dv` | INTEGER | Número de Turmas da Educação Profissional Técnica - Turno Diurno - Vespertino |
| `quantidade_tur_prof_tec_n` | INTEGER | Número de Turmas da Educação Profissional Técnica - Turno Noturno |
| `quantidade_tur_prof_tec_ead` | INTEGER | Número de Turmas da Educação Profissional Técnica - Turno não aplicável para turmas semipresenciais ou de Educação a Distância (EAD) |
| `quantidade_tur_eja_d` | INTEGER | Número de Turmas da Educação de Jovens e Adultos (EJA) - Turno Diurno |
| `quantidade_tur_eja_dm` | INTEGER | Número de Turmas da Educação de Jovens e Adultos (EJA) - Turno Diurno - Matutino |
| `quantidade_tur_eja_dv` | INTEGER | Número de Turmas da Educação de Jovens e Adultos (EJA) - Turno Diurno - Vespertino |
| `quantidade_tur_eja_n` | INTEGER | Número de Turmas da Educação de Jovens e Adultos (EJA) - Turno Noturno |
| `quantidade_tur_eja_ead` | INTEGER | Número de Turmas da Educação de Jovens e Adultos (EJA) - Turno não aplicável para turmas semipresenciais ou de Educação a Distância (EAD) |
| `quantidade_tur_eja_fund_d` | INTEGER | Número de Turmas da Educação de Jovens e Adultos (EJA) - Ensino Fundamental - Turno Diurno |
| `quantidade_tur_eja_fund_dm` | INTEGER | Número de Turmas da Educação de Jovens e Adultos (EJA) - Ensino Fundamental - Turno Diurno - Matutino |
| `quantidade_tur_eja_fund_dv` | INTEGER | Número de Turmas da Educação de Jovens e Adultos (EJA) - Ensino Fundamental - Turno Diurno - Vespertino |
| `quantidade_tur_eja_fund_n` | INTEGER | Número de Turmas da Educação de Jovens e Adultos (EJA) - Ensino Fundamental - Turno Noturno |
| `quantidade_tur_eja_fund_ead` | INTEGER | Número de Turmas da Educação de Jovens e Adultos (EJA) - Ensino Fundamental - Turno não aplicável para turmas semipresenciais ou de Educação a Distância (EAD) |
| `quantidade_tur_eja_med_d` | INTEGER | Número de Turmas da Educação de Jovens e Adultos (EJA) - Ensino Médio - Turno Diurno |
| `quantidade_tur_eja_med_dm` | INTEGER | Número de Turmas da Educação de Jovens e Adultos (EJA) - Ensino Médio - Turno Diurno - Matutino |
| `quantidade_tur_eja_med_dv` | INTEGER | Número de Turmas da Educação de Jovens e Adultos (EJA) - Ensino Médio - Turno Diurno - Vespertino |
| `quantidade_tur_eja_med_n` | INTEGER | Número de Turmas da Educação de Jovens e Adultos (EJA) - Ensino Médio - Turno Noturno |
| `quantidade_tur_eja_med_ead` | INTEGER | Número de Turmas da Educação de Jovens e Adultos (EJA) - Ensino Médio - Turno não aplicável para turmas semipresenciais ou de Educação a Distância (EAD) |
| `quantidade_tur_esp_d` | INTEGER | Número de Turmas da Educação Especial - Turno Diurno |
| `quantidade_tur_esp_dm` | INTEGER | Número de Turmas da Educação Especial - Turno Diurno - Matutino |
| `quantidade_tur_esp_dv` | INTEGER | Número de Turmas da Educação Especial - Turno Diurno - Vespertino |
| `quantidade_tur_esp_n` | INTEGER | Número de Turmas da Educação Especial - Turno Noturno |
| `quantidade_tur_esp_ead` | INTEGER | Número de Turmas da Educação Especial - Turno não aplicável para turmas semipresenciais ou de Educação a Distância (EAD) |
| `quantidade_tur_esp_cc_d` | INTEGER | Número de Turmas da Educação Especial em Classes Comuns - Turno Diurno |
| `quantidade_tur_esp_cc_dm` | INTEGER | Número de Turmas da Educação Especial em Classes Comuns - Turno Diurno - Matutino |
| `quantidade_tur_esp_cc_dv` | INTEGER | Número de Turmas da Educação Especial em Classes Comuns - Turno Diurno - Vespertino |
| `quantidade_tur_esp_cc_n` | INTEGER | Número de Turmas da Educação Especial em Classes Comuns - Turno Noturno |
| `quantidade_tur_esp_cc_ead` | INTEGER | Número de Turmas da Educação Especial em Classes Comuns - Turno não aplicável para turmas semipresenciais ou de Educação a Distância (EAD) |
| `quantidade_tur_esp_ce_d` | INTEGER | Número de Turmas da Educação Especial em Classes Exclusivas - Turno Diurno |
| `quantidade_tur_esp_ce_dm` | INTEGER | Número de Turmas da Educação Especial em Classes Exclusivas - Turno Diurno - Matutino |
| `quantidade_tur_esp_ce_dv` | INTEGER | Número de Turmas da Educação Especial em Classes Exclusivas - Turno Diurno - Vespertino |
| `quantidade_tur_esp_ce_n` | INTEGER | Número de Turmas da Educação Especial em Classes Exclusivas - Turno Noturno |
| `quantidade_tur_esp_ce_ead` | INTEGER | Número de Turmas da Educação Especial em Classes Exclusivas - Turno não aplicável para turmas semipresenciais ou de Educação a Distância (EAD) |
| `quantidade_tur_bas_int` | INTEGER | Número de Turmas da Educação Básica - Tempo Integral |
| `quantidade_tur_prof_int` | INTEGER | Número de Turmas da Educação Profissional - Tempo Integral |
| `quantidade_tur_prof_tec_int` | INTEGER | Número de Turmas da Educação Profissional Técnica - Tempo Integral |
| `quantidade_tur_eja_int` | INTEGER | Número de Turmas da Educação de Jovens e Adultos (EJA) - Tempo Integral |
| `quantidade_tur_eja_fund_int` | INTEGER | Número de Turmas da Educação de Jovens e Adultos (EJA) - Ensino Fundamental - Tempo Integral |
| `quantidade_tur_eja_med_int` | INTEGER | Número de Turmas da Educação de Jovens e Adultos (EJA) - Ensino Médio - Tempo Integral |
| `quantidade_tur_esp_int` | INTEGER | Número de Turmas da Educação Especial - Tempo Integral |
| `quantidade_tur_esp_cc_int` | INTEGER | Número de Turmas da Educação Especial em Classes Comuns - Tempo Integral |
| `quantidade_tur_esp_ce_int` | INTEGER | Número de Turmas da Educação Especial em Classes Exclusivas - Tempo Integral |
| `quantidade_tur_bas_disc_lingua_port` | INTEGER | Áreas do conhecimento/Componentes curriculares - Língua/ Literatura Portuguesa |
| `quantidade_tur_bas_disc_educ_fisica` | INTEGER | Áreas do conhecimento/Componentes curriculares - Educação Física |
| `quantidade_tur_bas_disc_artes` | INTEGER | Áreas do conhecimento/Componentes curriculares - Artes (Educação Artística, Teatro, Dança, Música, Artes Plásticas e outras) |
| `quantidade_tur_bas_disc_lingua_ing` | INTEGER | Áreas do conhecimento/Componentes curriculares - Língua/ Literatura estrangeira - Inglês |
| `quantidade_tur_bas_disc_lingua_espa` | INTEGER | Áreas do conhecimento/Componentes curriculares - Língua/ Literatura estrangeira - Espanhol |
| `quantidade_tur_bas_disc_lingua_franc` | INTEGER | Áreas do conhecimento/Componentes curriculares - Língua/ Literatura estrangeira - Francês |
| `quantidade_tur_bas_disc_lingua_outra` | INTEGER | Áreas do conhecimento/Componentes curriculares - Língua/ Literatura estrangeira - Outra |
| `quantidade_tur_bas_disc_libras` | INTEGER | Áreas do conhecimento/Componentes curriculares - Libras |
| `quantidade_tur_bas_disc_lingua_indig` | INTEGER | Áreas do conhecimento/Componentes curriculares - Língua Indígena |
| `quantidade_tur_bas_disc_port_seg_lingua` | INTEGER | Áreas do conhecimento/Componentes curriculares - Língua Portuguesa como segunda língua |
| `quantidade_tur_bas_disc_matematica` | INTEGER | Áreas do conhecimento/Componentes curriculares - Matemática |
| `quantidade_tur_bas_disc_ciencias` | INTEGER | Áreas do conhecimento/Componentes curriculares - Ciências |
| `quantidade_tur_bas_disc_fisica` | INTEGER | Áreas do conhecimento/Componentes curriculares - Física |
| `quantidade_tur_bas_disc_quimica` | INTEGER | Áreas do conhecimento/Componentes curriculares - Química |
| `quantidade_tur_bas_disc_biologia` | INTEGER | Áreas do conhecimento/Componentes curriculares - Biologia |
| `quantidade_tur_bas_disc_historia` | INTEGER | Áreas do conhecimento/Componentes curriculares - História |
| `quantidade_tur_bas_disc_geografia` | INTEGER | Áreas do conhecimento/Componentes curriculares - Geografia |
| `quantidade_tur_bas_disc_sociologia` | INTEGER | Áreas do conhecimento/Componentes curriculares - Sociologia |
| `quantidade_tur_bas_disc_filosofia` | INTEGER | Áreas do conhecimento/Componentes curriculares - Filosofia |
| `quantidade_tur_bas_disc_est_sociais` | INTEGER | Áreas do conhecimento/Componentes curriculares - Estudos Sociais |
| `quantidade_tur_bas_disc_est_sociais_soci` | INTEGER | Áreas do conhecimento/Componentes curriculares - Estudos Sociais ou Sociologia |
| `quantidade_tur_bas_disc_info_computacao` | INTEGER | Áreas do conhecimento/Componentes curriculares - Informática / Computação |
| `quantidade_tur_bas_disc_ensino_religioso` | INTEGER | Áreas do conhecimento/Componentes curriculares - Ensino Religioso |
| `quantidade_tur_bas_disc_profissiona` | INTEGER | Áreas do conhecimento/Componentes curriculares - Disciplinas dos cursos técnicos profissionais |
| `quantidade_tur_bas_disc_estagio_super` | INTEGER | Áreas do conhecimento/Componentes curriculares - Estágio curricular supervisionado |
| `quantidade_tur_bas_disc_pedagogicas` | INTEGER | Áreas do conhecimento/Componentes curriculares - Disciplinas pedagógicas |
| `quantidade_tur_bas_disc_projeto_de_vida` | INTEGER | Áreas do conhecimento/Componentes curriculares - Projeto de vida |
| `quantidade_tur_bas_disc_outras` | INTEGER | Áreas do conhecimento/Componentes curriculares - Outras disciplinas |
| `quantidade_tur_bas_libras` | INTEGER | Número de Turmas da Educação Básica - Classe bilíngue de surdos tendo a Libras (Língua Brasileira de Sinais) como língua de instrução, ensino, comunicação e interação e a língua portuguesa escrita com |
