# PNCP item-route smoke record

**Date:** 2026-09-28  
**Scope:** local source-access check; not a dataset release

The item client was checked against one bounded public PNCP publication window: 2026-09-20, modality 6. The publication request returned 25 normalized records. All 25 carried the organization, year, and sequence values required by the documented item route.

The check selected one eligible parent locally and called the item route. It returned five normalized item records. The client observed the endpoint's direct JSON-list response shape and now supports that shape alongside paginated object responses.

The resulting records contained no raw `descricao` field and no `source_record_url` field. The check did not retain the source records, item descriptions, organization identifiers, or endpoint parameters in this evidence file.

This proves a bounded source-access path and the release boundary for one response. It does not establish coverage, current availability, source terms, recommendation quality, or approval for Kaggle publication.
