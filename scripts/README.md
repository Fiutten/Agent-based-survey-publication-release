# Public validation scripts

This directory contains only rights-safe validation utilities for the public companion release. It does **not** contain the private full-text extraction pipeline or licensed database-processing workflow used in the authorial working archive.

## `validate_release.py`

Run from the repository root:

```bash
python scripts/validate_release.py
```

The validator uses only the Python standard library. It checks that:

- the frozen screening and evidence-tier accounting remains `3,367 -> 463 -> 175 -> 82`;
- Scopus/Web of Science reconciliation remains arithmetically consistent;
- the seven construct-profile rows retain the released `reported / empirically evaluated / criterion-satisfying` counts with denominator 82;
- each evidence-control appraisal dimension sums to the 82-study central nucleus and retains the released counts;
- the post-freeze RIF coverage set contains the same eight fixed candidate identities, with seven full-text-coded records and one visible technical exclusion;
- duplicate candidate IDs or DOIs and invalid RIF coding symbols are rejected.

The script intentionally validates the released aggregate artefacts rather than attempting to recreate restricted inputs that cannot lawfully be redistributed here.
