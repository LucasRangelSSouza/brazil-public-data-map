# PNCP table catalogue

The versioned inventory in [`sources/pncp_table_catalog.json`](../sources/pncp_table_catalog.json) maps each known PNCP table to its data layer, source route or derivation, and release state. [`sources/pncp_publication_plan.json`](../sources/pncp_publication_plan.json) maps those table-layer pairs to Kaggle datasets grouped by subject.

The current inventory snapshot contains 47 table-layer pairs: 13 raw, 28 trusted, and 6 semantic. It records the requested data cutoff as 2026-07-31. The canonical [PNCP Reference Codes](https://www.kaggle.com/datasets/lucasrangelss/pncp-reference-codes-data) dataset, version 2, groups 12 trusted tables in one release. Kaggle still hosts eleven of those tables in their earlier standalone datasets, which we retain unchanged as legacy releases. The grouped release adds `pncp_dom_tipos_parte_envolvida`. The catalogue also retains the prior standalone releases for [modalities](https://www.kaggle.com/datasets/lucasrangelss/pncp-trusted-dom-modalidades), [legal grounds](https://www.kaggle.com/datasets/lucasrangelss/pncp-trusted-dom-amparos-legais), [catalogues](https://www.kaggle.com/datasets/lucasrangelss/pncp-trusted-dom-catalogos), [PCA item categories](https://www.kaggle.com/datasets/lucasrangelss/pncp-trusted-dom-categoria-item-pca), [judgment criteria](https://www.kaggle.com/datasets/lucasrangelss/pncp-trusted-dom-criterios-julgamento), [budget sources](https://www.kaggle.com/datasets/lucasrangelss/pncp-trusted-dom-fontes-orcamentarias), [company sizes](https://www.kaggle.com/datasets/lucasrangelss/pncp-trusted-dom-portes-empresa), [contract types](https://www.kaggle.com/datasets/lucasrangelss/pncp-trusted-dom-tipos-contrato), [dispute modes](https://www.kaggle.com/datasets/lucasrangelss/pncp-trusted-dom-modos-disputa), [document types](https://www.kaggle.com/datasets/lucasrangelss/pncp-trusted-dom-tipos-documento), [billing instrument types](https://www.kaggle.com/datasets/lucasrangelss/pncp-trusted-dom-tipos-instrumento-cobranca), and [notice instrument types](https://www.kaggle.com/datasets/lucasrangelss/pncp-trusted-dom-tipos-instrumento-convocatorio). Twelve of the 47 table-layer entries now point to the published grouped release; the other 35 remain `inventory-only` (16 trusted, 13 raw, and 6 semantic). The PNCP catalogue as a whole is not complete. See the [grouped-release evidence](evidence/pncp-reference-codes-grouped-v2-2026-09-29.md) and the [legacy release evidence](evidence/pncp-trusted-reference-batch-2026-09-29.md).

The table map and API route catalogue answer different questions: one links data tables to source routes or derivations; the other records operations in the [consulta API](https://pncp.gov.br/api/consulta/v3/api-docs) and the [PNCP integration API](https://pncp.gov.br/api/pncp/v3/api-docs). A single route may feed several tables, while a derived table may have no direct endpoint. The inventory lists 219 operations. Twelve collection `GET` operations currently link to released datasets; detail routes, write operations, and unreleased public-data operations still need evidence or a documented exclusion rationale.

Validate the subject grouping and full table-layer coverage locally:

```console
python -m brazil_data_map validate-pncp-publication-plan
```

The plan maps 47 table-layer pairs to 14 subject datasets. We published `pncp-reference-codes-data` version 2 and verified a clean download. The other targets do not imply completed exports. The release process measures each package directly and splits a subject-layer bundle only when the measured size or Kaggle's file-count limit requires it. See [`sources/pncp_release_registry.json`](../sources/pncp_release_registry.json) for published grouped-dataset versions.

After downloading a candidate dataset, verify every planned table, Parquet row count, schema and privacy-audit hash, dataset metadata, and total package size:

```console
python -m brazil_data_map validate-pncp-release-bundle \
  --dataset-slug pncp-procurement-items-data \
  --package-dir .local/pncp-procurement-items-data
```

The bundle verifier checks declared files against the published manifest and enforces the configured 200 GB and top-level-file limits. It does not certify the upstream source or replace source-specific acquisition checks.

Refresh the route inventory from those public OpenAPI documents with `python -m brazil_data_map sync-pncp-endpoints`. This records operation methods, paths, parameter names, authentication metadata, and current release status. It does not call protected endpoints or publish data. Validate an existing snapshot offline with `python -m brazil_data_map sync-pncp-endpoints --validate`.

## Layer meanings

- `raw` retains the bounded, source-aligned capture for a route or endpoint family.
- `trusted` contains typed and deterministically deduplicated records.
- `semantic` contains documented analytical projections and retrieval-ready records.

The canonical publication unit is a subject bundle. Related `raw` and `trusted` Parquet files share a Kaggle dataset; the subject's `semantic` layer uses a separate dataset. A bundle is split only when its measured upload size or Kaggle file-count limit requires it. The catalogue maps every table-layer pair to its subject, dataset slug/version, and path. Already-published standalone lookup datasets remain unchanged as legacy references. A table is `ready` only when its file has schema, manifest/hash, scan, and clean-download evidence. The catalogue is complete only when every entry reaches `ready`, `excluded-with-rationale`, or `unavailable-with-evidence`; any `inventory-only` entry rules out a complete-catalogue claim.

The release process measures each generated bundle directly; source-system storage metrics are not a substitute for exported Parquet sizes. Apply the sizing gate to each subject/layer dataset independently and keep a safety margin below Kaggle's 200 GB limit.

## Release record

The table inventory contains no source rows. Each release record names its cutoff field and extraction interval, then records row count, schema and file hashes, scan result, and clean-download result. A snapshot shows one point in time; it cannot establish a complete historical series.

The modality dataset pins a historical snapshot. On 29 September 2026, the live endpoint returned 19 records. Nine had current source timestamps through the July cutoff. The Kaggle release preserves pre-cutoff values for the other ten, which the mutable endpoint no longer returns. Download this release to reproduce that snapshot; a query today cannot recover the superseded values. See the [release verification record](evidence/pncp-trusted-dom-modalidades-2026-09-29.md).

Download and verify the public package locally:

```powershell
kaggle datasets download lucasrangelss/pncp-trusted-dom-modalidades --path .local/pncp-trusted-dom-modalidades --unzip
python -m brazil_data_map validate-pncp-release-package --dataset-slug pncp-trusted-dom-modalidades --package-dir .local/pncp-trusted-dom-modalidades
```

The verifier checks the release identity, cutoff, Parquet row count, schema hash, privacy audit, and file hashes. It runs without private source access. Use the Kaggle release to reproduce the historical snapshot; each call to the mutable source endpoint returns a new observation.
