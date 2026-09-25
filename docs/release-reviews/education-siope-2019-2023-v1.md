# Release approval: Brazil Education Data Lake, version 1

## Candidate

The Kaggle slug is `lucasrangelss/brazil-education-data-lake`. It covers the annual (sixth-bimester) municipal SIOPE declarations for reporting years 2019 through 2023, joined to the IBGE municipality reference.

The sources are the FNDE SIOPE OData service (`Dados_Gerais_Siope` and `Indicadores_Siope`) and the IBGE Localidades municipalities endpoint. The local capture finished at 2026-09-25T13:05:09+00:00 and was built at commit `379da099a0eeaf75d11be51d16e26f2620b67b79`.

Each layer contains 27,830 rows. The privacy gate passed with zero violations.

## Field allowlist

id, updated_at, year, municipality_code, municipality_name, state_code, population, total_revenue_realized, total_expenditure_paid, mde_minimum_share_pct, fundeb_remuneration_share_pct, fundeb_unspent_share_pct, education_share_of_total_expenditure_pct, investment_per_basic_education_student, plus pipeline fields identifier_classification, natural_key, and (raw only) source_id.

## Excluded

The SIOPE responsible-person entity (names, emails, phones, addresses, CNPJ, residence codes), free-text justifications and rectification narratives, receipt numbers, declaration-method flags, and every other source column. State-level declarations are out of scope.

## Source and redistribution assessment

FNDE publishes SIOPE through its open-data service and open-data plan. IBGE publishes the municipality reference through a public API. Neither page states a dataset-specific license; the gov.br site footer license covers site content, not these datasets. Decree 8,777/2016, art. 2, III, which sets the federal open-data policy, defines open data as released under an open license permitting free use, consumption, and cross-referencing, limited to crediting authorship or source. This supports an attributed derivative release. The package uses the Kaggle `other` setting, credits FNDE and IBGE, and claims no new license over their data. Apache-2.0 applies only to the companion repository's code.

## Build and verification evidence

Two independent builds from the same capture at the commit above produced byte-identical manifests. Before upload, the package passed a schema diff against the allowlist, the layer-wide privacy audit, and a byte-level scan for private paths, credentials, and environment identifiers.

## Decision

Approved for an attributed public Kaggle release by the release owner, Lucas Rangel, on 2026-09-25, under his instruction to complete the portfolio specification's Kaggle releases. The approval covers only the coverage and fields described here. A later version requires a new manifest, privacy review, and approval record.
