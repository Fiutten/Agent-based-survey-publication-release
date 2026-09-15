# Public reproducibility and audit guide

## What this repository can reproduce

This public companion is intentionally a **rights-safe audit layer**. It exposes the executed search logic, frozen accounting, aggregate full-text evidence summaries, dimensional evidence-control appraisal, review governance, and post-freeze RIF coverage set used to inspect the principal reported results.

Because publisher-restricted PDFs and licensed Scopus/Web of Science exports cannot be redistributed here, an external user cannot reconstruct every screening and full-text coding decision from raw source files using this repository alone. The public release instead supports reproducible validation of the released aggregate artefacts and transparent inspection of the protocol that produced them.

This distinction is deliberate: **auditability of the reported public artefacts is reproducible here; full re-execution from restricted primary inputs is not claimed.**

## Frozen primary snapshot

The primary search closes on **4 August 2026**. The released quantitative hierarchy is:

```text
3,367 reconciled screening records
  -> 463 explicit evidence-tier assessments
      -> 175 publications in the structured evidence map
          -> 82 central publications in the full-text nucleus
```

The 175-study evidence map contains 82 central and 93 priority-supporting publications. Post-freeze venue/frontier and RIF coverage records remain outside these denominators.

## Validate the public release

Requirements: Python 3.10+; no third-party packages.

From the repository root:

```bash
python scripts/validate_release.py
```

The validator checks:

1. frozen Scopus/Web of Science and evidence-tier arithmetic;
2. exact released construct-profile counts for the 82-study nucleus;
3. evidence-control appraisal row totals and frozen counts;
4. the fixed identity and status of the eight post-freeze RIF coverage candidates;
5. allowed RIF coding symbols, duplicate IDs, and duplicate DOIs.

A successful run ends with:

```text
Public release validation passed.
Frozen accounting: 3,367 -> 463 -> 175 -> 82.
```

## Suggested audit path

For a compact independent review of the public evidence trail:

1. Read `protocol/search_strategy.md` and check the query families, eligibility filters, and reconciliation accounting.
2. Inspect `data/corpus_snapshot.tsv` and run the validator to verify the frozen funnel arithmetic.
3. Read `protocol/review_governance.md` before interpreting the full-text aggregate tables.
4. Inspect `data/construct_evidence_profile.tsv`, paying particular attention to the distinction among `reported`, `empirically_evaluated`, and `criterion_satisfying`.
5. Inspect `data/evidence_control_appraisal.tsv`; its dimensions are intentionally non-additive and are not a scalar quality score.
6. Read `protocol/rif_coverage_check.md` before using `data/rif_external_coverage.tsv`; those records are a post-freeze applicability/coverage stress test, not prevalence data or predictive validation.

`data/README.md` provides the public data dictionary and `protocol/README.md` provides the protocol index.

## Interpretation guards

The following constraints are part of the release and should be preserved in derivative use:

- `0/82` at the criterion-satisfying level means that the conservative pass did not identify an unambiguous qualifying case; it is not proof of universal absence.
- Machine or AI-assisted non-detection was not automatically converted into a scientific `NO` decision.
- The 18-study later coauthor check was a targeted scientific sign-off, not a second item-by-item inter-rater study; no new agreement statistic is inferred from it.
- The evidence-control appraisal is dimensional; no scalar study-quality score is defined.
- The post-freeze RIF coverage set is excluded from the frozen 175/82 quantitative denominators.
- RIF is a survey-derived reference/evaluation model. The public coverage check does not establish predictive validity, causal benefit, or superiority over alternative frameworks.
- The unresolved historical Web of Science interface collection label is retained as a provenance limitation rather than reconstructed from memory.

## Restricted material not redistributed

This repository does not contain:

- publisher-restricted full-text PDFs;
- licensed Scopus exports;
- licensed Web of Science exports;
- private full-text evidence packs or other restricted source material.

Their absence is a rights constraint, not an indication that they were absent from the underlying review process.

## Versioning

Scientific denominators in this release are tied to the **4 August 2026 frozen snapshot**. Any final pre-submission database update must be represented as a separate dated extension rather than silently overwriting these values.

When a permanent DOI or archived release is minted, its identifier should be added to the root `README.md` and `CITATION.md` without changing the frozen historical denominators.
