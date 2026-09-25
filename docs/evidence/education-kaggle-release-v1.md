# Education Kaggle release, version 1

The public dataset [Brazil Education Data Lake: SIOPE 2019-2023](https://www.kaggle.com/datasets/lucasrangelss/brazil-education-data-lake) was released on 2026-09-25. It holds 27,830 municipality-year records in each raw, trusted, and semantic layer: the annual (sixth-bimester) municipal declarations to FNDE's SIOPE for 2019 through 2023, joined to the IBGE municipality reference.

## Build

`capture-siope` queried the public SIOPE OData service (`Dados_Gerais_Siope` and `Indicadores_Siope`, filtered server-side to municipal rows and five indicator codes) for 27 states and five years, and the IBGE Localidades municipalities endpoint once. The capture finished at 2026-09-25T13:05:09Z with 5,565 to 5,567 declarations per year; the Federal District files no municipal declaration. Every SIOPE six-digit code matched an IBGE seven-digit code.

`build-education-release` ran twice from that capture at commit `379da099a0eeaf75d11be51d16e26f2620b67b79`. Both manifests were byte-identical. The privacy audit passed with zero violations. A schema diff found no column outside the allowlist, and a byte-level scan of the package found no private path, credential, or environment identifier; the only external reference is the public source URL.

## Verification

Published manifest SHA-256: `44f259602a688432dddbae6b0306a6957514a634d57d94a0abd3cff30f4b3506`.

A clean download of version 1 through `kagglehub`, with the Kaggle configuration directory pointed at an empty location, returned the seven package files. Every file listed in the manifest matched its SHA-256.

## Data quality notes

Values are as declared. Null rates per column stay below 1.5% in every year. Some declarations are implausible: `education_share_of_total_expenditure_pct` reaches about 1.27e11, one `mde_minimum_share_pct` is negative, and 30 rows report zero investment per student. The release keeps them because the companion MLOps project studies such outliers for human review.

## Terms

Neither the FNDE open-data pages nor the IBGE API documentation states a dataset-specific license. The release relies on Decree 8,777/2016, art. 2, III, which defines federal open data as released under a license that allows free use limited to crediting the source. The package uses Kaggle's `other` setting and credits FNDE and IBGE. The full assessment and decision are in [the release review](../release-reviews/education-siope-2019-2023-v1.md).
