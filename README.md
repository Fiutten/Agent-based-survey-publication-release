# Reliable Information Fusion in Generative Multi-Agent Systems

Public reproducibility companion for the manuscript **“Reliable Information Fusion in Generative Multi-Agent Systems: A Systematic Evidence Map and Dependence-Aware Evaluation Framework”** by Alberto Fernández-Isabel, Isaac Martín de Diego, and Rubén Fuentes-Fernández.

The manuscript is being prepared for submission to *Information Fusion*.

## Purpose of this repository

This repository is the **rights-safe public audit layer** for the study. It exposes the executed search strategy, frozen screening and reconciliation accounting, aggregate full-text evidence summaries, dimensional evidence-control appraisal, review-governance documentation, and the post-freeze RIF coverage check used to inspect the principal reported results.

It is deliberately separate from restricted source material. Publisher full-text PDFs and licensed Scopus/Web of Science exports are **not redistributed**.

## Frozen scientific snapshot

The primary systematic-search snapshot closes on **4 August 2026**. Its quantitative hierarchy is:

```text
3,367 reconciled screening records
  -> 463 explicit evidence-tier assessments
      -> 175 publications in the structured evidence map
          -> 82 central publications in the full-text nucleus
```

The 175-publication evidence map contains **82 central + 93 priority-supporting** publications. Post-freeze venue/frontier and hold-out records are kept separate from these denominators and are used only for positioning or coverage-sensitivity analyses.

## Repository map

```text
.
├── README.md
├── REPRODUCIBILITY.md          # public audit/reproducibility boundary and workflow
├── CITATION.md                 # citation guidance pending article/archive DOI
├── data/
│   ├── README.md               # data dictionary
│   ├── corpus_snapshot.tsv
│   ├── construct_evidence_profile.tsv
│   ├── evidence_control_appraisal.tsv
│   └── rif_external_coverage.tsv
├── protocol/
│   ├── README.md               # protocol reading order
│   ├── search_strategy.md
│   ├── review_governance.md
│   └── rif_coverage_check.md
└── scripts/
    ├── README.md
    └── validate_release.py      # standard-library consistency validator
```

A read-only GitHub Actions workflow runs the public validator on pushes and pull requests.

## Released material

### Protocol

- `protocol/search_strategy.md` — frozen Scopus S1-S8 and Web of Science W1-W4 query logic, filters, counts, deduplication, and reconciliation rules.
- `protocol/review_governance.md` — three-author calibration, final adjudication boundaries, later coauthor sign-off, and AI-assistance boundary.
- `protocol/rif_coverage_check.md` — interpretation and limits of the post-freeze RIF coverage/applicability check.

### Data

- `data/corpus_snapshot.tsv` — frozen evidence-stratum and database-reconciliation counts.
- `data/construct_evidence_profile.tsv` — reported / empirically evaluated / criterion-satisfying full-text counts for the 82 central publications.
- `data/evidence_control_appraisal.tsv` — non-additive appraisal counts for baseline adequacy, resources, statistics, dependence, failures, and reproducibility.
- `data/rif_external_coverage.tsv` — eight fixed post-freeze coverage candidates and their RIF-level coding; one candidate is retained as a technical exclusion.

See `data/README.md` for field-level interpretation.

## Validate the public release

The released aggregate artefacts can be checked without third-party Python dependencies:

```bash
python scripts/validate_release.py
```

The validator checks the frozen `3,367 -> 463 -> 175 -> 82` accounting, the seven construct-profile rows, the evidence-control appraisal totals, and the identity/status/coding invariants of the eight-record post-freeze RIF coverage set.

For the exact auditability boundary and suggested review path, see `REPRODUCIBILITY.md`.

## Rights and database restrictions

Publisher-restricted full-text PDFs are **not redistributed**. Licensed Scopus and Web of Science export files are also not redistributed. The release instead preserves query logic, public bibliographic identities where appropriate, reconciliation counts, coding semantics, governance, and derived summaries so that the principal reported denominators and claims can be inspected without publishing restricted material.

The historical Web of Science audit preserves the Topic-query strings, filters, date window, export fields, and reconciliation order used in the review. The original historical interface collection label is not reconstructed from memory; this provenance limitation is retained explicitly rather than guessed.

## Evidence-level semantics

The manuscript uses three nested levels for the 82-study full-text construct profile:

- **Reported:** the construct is explicitly represented or discussed.
- **Empirically evaluated:** the construct is manipulated, compared, or empirically interrogated.
- **Criterion-satisfying:** a prespecified construct-specific evidential criterion is met. Depending on the construct, this may require a quantitative dependence diagnostic, calibration against correctness, a direct quantitative failure/recovery outcome, an evaluated lineage property, or an explicitly resource-matched comparison.

The third level is therefore not a generic synonym for “numerically measured.” In particular, numerical cost reporting is distinct from an explicitly resource-matched causal comparison. A `0/82` cell means that the conservative pass did not identify an unambiguous criterion-satisfying case; it is **not** a universal absence claim.

## Human and AI-assisted review governance

A 12-study heterogeneous calibration pilot was completed by all three authors. The later 18-study high-impact check was a targeted two-coauthor scientific sign-off with no requested amendments; it was **not** duplicate construct-by-construct recoding, and no additional inter-rater statistic is claimed from that stage.

AI assistance supported evidence localization, first-pass semantic coding, structural editing, language refinement, and consistency checking. Final eligibility decisions, coding adjudication, scientific interpretation, and manuscript claims remained author decisions. Machine non-detection was never converted automatically into evidence of absence.

## RIF status

RIF is a survey-derived **reference and evaluation model**, not a validated predictive algorithm. Its post-freeze hold-out is a coverage/applicability stress test and its retrospective case matrix is illustrative. Neither is presented as evidence that RIF improves deployed reliability.

## Citation and versioning

Citation guidance is in `CITATION.md`. Until permanent identifiers are available, secondary analyses should record the exact Git commit used.

The article is under preparation for submission to *Information Fusion*. A persistent article/data identifier will be added when available. Any final pre-submission database update must be represented as a separate dated extension and must not silently overwrite the **4 August 2026** frozen snapshot.
