# Grouped PNCP reference-code release

Version 2 of [PNCP Reference Codes](https://www.kaggle.com/datasets/lucasrangelss/pncp-reference-codes-data) is the canonical reference-code release. It groups 12 trusted PNCP tables in one Kaggle dataset, with each Parquet available as a direct download under a `trusted__<table>.parquet` filename. The declared cutoff is 2026-07-31T23:59:59Z.

Across the 12 Parquet files, the release contains 272 rows. That total adds each table's row count, so it does not count unique values across the reference domain. Kaggle serves 38 files totaling 84,770 bytes. SHA-256 for `release_manifest.json`: `f198d763c96efa159ba56d0420ffc12cae393ecbd9d898575be5d11335b711f8`.

We downloaded the release into a fresh local directory and ran the bundle verifier, which checked all 12 planned table-layer entries and all 38 files. It reported zero hash mismatches, and every Parquet row count matched. Kaggle omits `dataset-metadata.json` from downloads. The manifest stores that upload-control file's hash separately; the verifier allows its absence.

`pncp_dom_tipos_parte_envolvida` has three rows and no row-level business timestamp. Source snapshot metadata records a last modification at 2026-07-23T03:15:21Z, before the cutoff. For the other 11 tables, we reused previously verified trusted candidates and kept the standalone Kaggle releases as legacy references.

To verify a fresh download:

```powershell
kaggle datasets download lucasrangelss/pncp-reference-codes-data --path .local/pncp-reference-codes-data --unzip
python -m brazil_data_map validate-pncp-release-bundle --dataset-slug pncp-reference-codes-data --package-dir .local/pncp-reference-codes-data
```

The public publication plan remains a target catalogue. This release verifies only the `reference-codes` dataset; it does not establish completion of the other PNCP subject datasets or the full PNCP endpoint inventory.
