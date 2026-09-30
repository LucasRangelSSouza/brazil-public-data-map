# PNCP v2 item candidate record

**Date:** 2026-09-28  
**Status:** local candidate only; distribution version `not_published`

A bounded candidate was built from the public PNCP publication window for 2026-09-20, modality 6. The local capture contained 25 deduplicated parent procurements. The item candidate builder produced 513 records in each raw, trusted, and semantic layer.

The privacy audit passed with no violations. The manifest records source ID `pncp-v2`, retrieval timestamp `2026-09-28T00:00:00Z`, extractor commit `1cb4316`, row counts, and hashes for the privacy audit plus all three Parquet layers. An independent local check recomputed every declared hash successfully.

The first build wrote a 279,356-byte ignored normalized-item capture after it completed the documented item-route requests. A second build used that capture, made no item-route request, and produced an identical manifest: the input digest was `7eb9d048ec5681664e90b6b0c60621ae8ad951828dbc4c3915816c123e80bc82`; every declared artifact hash matched. This establishes deterministic reconstruction for this fixed, bounded local input.

The candidate directory is ignored by Git. This record intentionally omits source records, organization identifiers, item descriptions, URLs, and item-level values. The output retains only the v2 contract's approved structured fields and controlled categories.

This evidence does not approve a Kaggle release. Publication remains blocked on the source and distribution review, a dated release approval, and a clean-download verification after upload.
