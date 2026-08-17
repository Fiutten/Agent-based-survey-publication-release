# Reliable Information Fusion in Generative Multi-Agent Systems

Public reproducibility companion for the manuscript **“Reliable Information Fusion in Generative Multi-Agent Systems: A Systematic Evidence Map and Dependence-Aware Evaluation Framework”** by Alberto Fernández-Isabel, Isaac Martín de Diego, and Rubén Fuentes-Fernández.

## Scope of this release

The primary systematic-search snapshot closes on **4 August 2026**. It contains a 3,367-record screening universe, a 175-publication structured evidence map, and an 82-publication central full-text nucleus. Post-freeze venue/frontier and hold-out records are kept separate from those quantitative denominators and are used only for positioning or coverage-sensitivity analyses.

This repository is the rights-safe public audit layer for the article. The current release exposes the executed database-search strategy, frozen screening and reconciliation accounting, construct-level evidence summaries, evidence-control appraisal summaries, review-governance documentation, and the post-freeze RIF coverage check used to inspect the principal reported results.

## Released material

- `protocol/search_strategy.md`: frozen Scopus S1-S8 and Web of Science W1-W4 query logic, filters, counts, deduplication, and reconciliation rules.
- `protocol/review_governance.md`: three-author calibration, final adjudication boundaries, later coauthor sign-off, and AI-assistance boundary.
- `protocol/rif_coverage_check.md`: interpretation and limits of the post-freeze RIF coverage/applicability check.
- `data/corpus_snapshot.tsv`: frozen evidence-stratum and database-reconciliation counts.
- `data/construct_evidence_profile.tsv`: reported / empirically evaluated / criterion-satisfying full-text counts for the 82 central publications.
- `data/evidence_control_appraisal.tsv`: non-additive appraisal counts for baseline adequacy, resources, statistics, dependence, failures, and reproducibility.
- `data/rif_external_coverage.tsv`: the eight fixed post-freeze coverage candidates and their RIF-level coding; one candidate is retained as a technical exclusion.

## Rights and database restrictions

Publisher-restricted full-text PDFs are **not redistributed**. Licensed Scopus and Web of Science export files are also not redistributed. The release instead preserves query logic, bibliographic identities where reported in rights-safe derived records, reconciliation counts, coding rules, and derived summaries so that the principal reported denominators and claims can be audited without redistributing restricted material.

The historical Web of Science audit preserves the Topic-query strings, filters, date window, export fields, and reconciliation order used in the review. The original historical interface collection label is not reconstructed from memory; this provenance limitation is retained explicitly rather than guessed.

## Evidence-level semantics

The manuscript uses three nested levels for the 82-study full-text construct profile:

- **Reported:** the construct is explicitly represented or discussed.
- **Empirically evaluated:** the construct is manipulated, compared, or empirically interrogated.
- **Criterion-satisfying:** a prespecified construct-specific evidential criterion is met. Depending on the construct, this may require a quantitative dependence diagnostic, calibration against correctness, a direct quantitative failure/recovery outcome, an evaluated lineage property, or an explicitly resource-matched comparison.

The third level is therefore not a generic synonym for “numerically measured.” In particular, numerical cost reporting is distinct from an explicitly resource-matched causal comparison.

## Human and AI-assisted review governance

A 12-study heterogeneous calibration pilot was completed by all three authors. The later 18-study high-impact check was a targeted two-coauthor scientific sign-off with no requested amendments; it was **not** duplicate construct-by-construct recoding, and no additional inter-rater statistic is claimed from that stage.

AI assistance supported evidence localization, first-pass semantic coding, structural editing, and consistency checking. Final eligibility decisions, coding adjudication, scientific interpretation, and manuscript claims remained author decisions. Machine non-detection was never converted automatically into evidence of absence.

## RIF status

RIF is a survey-derived **reference and evaluation model**, not a validated predictive algorithm. Its post-freeze hold-out is a coverage/applicability stress test and its retrospective case matrix is illustrative. Neither is presented as evidence that RIF improves deployed reliability.

## Citation

The article is under preparation for submission to *Information Fusion*. A persistent article/data identifier will be added to this repository when available.
