# Released data tables

These TSV files are the rights-safe aggregate data layer released with the manuscript companion. They preserve the principal frozen denominators and evidence summaries without redistributing publisher-restricted full texts or licensed database exports.

## `corpus_snapshot.tsv`

Frozen accounting for the primary search snapshot closed on **4 August 2026**.

Columns:

- `layer`: named screening, evidence-tier, or database-reconciliation stage.
- `count`: frozen count for that stage; `NA` is used for the post-freeze hold-out because it is deliberately outside the primary denominator.
- `interpretation`: concise statement of how the layer is used.

Key invariants are `2,613 Scopus unique + 754 WoS-only = 3,367`, `171 outside scope + 117 contextual + 93 priority-supporting + 82 central = 463`, and `93 + 82 = 175`.

## `construct_evidence_profile.tsv`

Aggregate construct-level profile for the **82 central full-text publications**.

Columns:

- `construct`: reliability construct.
- `reported`: construct explicitly represented or discussed.
- `empirically_evaluated`: construct manipulated, compared, or empirically interrogated.
- `criterion_satisfying`: the prespecified construct-specific high-specificity criterion is met.
- `denominator`: fixed at 82.

The three evidence levels are nested. `criterion_satisfying` is deliberately construct-specific and is not a generic synonym for “numerically measured.” A zero indicates that the conservative pass did not identify an unambiguous criterion-satisfying case; it is not a universal absence claim.

## `evidence_control_appraisal.tsv`

Dimensional appraisal of the same **82-study central nucleus**.

Columns:

- `dimension`: evidence-control dimension.
- `strong`, `partial`, `reported_only`, `limited`: mutually exclusive release categories within that dimension.
- `denominator`: fixed at 82.

Each row sums to 82. These dimensions are **not** combined into a scalar study-quality score.

## `rif_external_coverage.tsv`

Fixed post-freeze applicability/coverage set for the RIF reference/evaluation model. These records are **not** pooled with the frozen 175/82 evidence counts.

Columns:

- `candidate_id`, `title`, `doi`: public identity fields.
- `status`: `FULLTEXT_CODED` or `TECHNICAL_EXCLUSION`.
- `source_quality`, `dependence`, `uncertainty_calibration`, `provenance`, `topology_fusion`, `faults`, `recovery_abstention`, `resources`: RIF coverage dimensions.

Coding symbols are defined in `../protocol/rif_coverage_check.md`: `R` = reported, `E` = empirically evaluated, `C` = criterion-satisfying, `--` = no unambiguous retained evidence at that level, and `NA` = not assessed because of technical exclusion.

## Validation

Run:

```bash
python scripts/validate_release.py
```

from the repository root to check the frozen counts, arithmetic, denominators, table identities, and external-coverage coding invariants.
