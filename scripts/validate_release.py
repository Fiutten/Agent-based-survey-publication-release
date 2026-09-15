#!/usr/bin/env python3
"""Validate the frozen, rights-safe public reproducibility release.

The public companion deliberately excludes publisher-restricted PDFs and licensed
Scopus/Web of Science exports. This validator therefore checks the internal
consistency and frozen identities of the rights-safe aggregate artefacts that are
actually released here; it does not recreate the underlying literature search or
full-text coding from restricted source material.
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


class ValidationError(RuntimeError):
    pass


def load_tsv(name: str) -> list[dict[str, str]]:
    path = DATA / name
    if not path.exists():
        raise ValidationError(f"Missing required file: {path.relative_to(ROOT)}")
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    if not rows:
        raise ValidationError(f"Empty TSV: {path.relative_to(ROOT)}")
    return rows


def as_int(value: str, label: str) -> int:
    try:
        return int(value)
    except (TypeError, ValueError) as exc:
        raise ValidationError(f"Expected integer for {label}, found {value!r}") from exc


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def validate_corpus_snapshot() -> None:
    rows = load_tsv("corpus_snapshot.tsv")
    by_layer = {row["layer"]: row["count"] for row in rows}

    expected = {
        "screening_universe": 3367,
        "explicit_evidence_assessment": 463,
        "outside_scope": 171,
        "contextual": 117,
        "priority_supporting": 93,
        "central_full_text": 82,
        "structured_evidence_map": 175,
        "scopus_rows_across_S1_S8": 4632,
        "scopus_unique_eids": 2613,
        "wos_raw_rows": 1296,
        "wos_eligible_rows": 1277,
        "wos_unique_records": 885,
        "wos_scopus_overlap": 131,
        "wos_only_records": 754,
    }

    for layer, value in expected.items():
        require(layer in by_layer, f"Missing corpus layer: {layer}")
        observed = as_int(by_layer[layer], f"corpus_snapshot:{layer}")
        require(observed == value, f"Frozen corpus value drift for {layer}: {observed} != {value}")

    require(
        by_layer.get("post_freeze_frontier_holdout") == "NA",
        "post_freeze_frontier_holdout must remain outside the frozen denominator and use count=NA",
    )

    require(expected["outside_scope"] + expected["contextual"] + expected["priority_supporting"] + expected["central_full_text"] == expected["explicit_evidence_assessment"],
            "Evidence-tier accounting no longer sums to 463")
    require(expected["priority_supporting"] + expected["central_full_text"] == expected["structured_evidence_map"],
            "Structured evidence-map accounting no longer sums to 175")
    require(expected["scopus_unique_eids"] + expected["wos_only_records"] == expected["screening_universe"],
            "Scopus + WoS-only accounting no longer sums to 3,367")
    require(expected["wos_unique_records"] - expected["wos_scopus_overlap"] == expected["wos_only_records"],
            "WoS reconciliation no longer yields 754 WoS-only records")


def validate_construct_profile() -> None:
    rows = load_tsv("construct_evidence_profile.tsv")
    expected = {
        "Dependence": (10, 1, 0),
        "Confidence calibration": (53, 10, 3),
        "Benign failure": (29, 9, 2),
        "Adversarial failure": (21, 11, 2),
        "Recovery": (25, 5, 2),
        "Provenance": (18, 2, 0),
        "Resource use and matched-fairness evidence": (61, 24, 0),
    }
    require(len(rows) == len(expected), f"Expected {len(expected)} construct rows, found {len(rows)}")

    seen: set[str] = set()
    for row in rows:
        construct = row["construct"]
        require(construct in expected, f"Unexpected construct row: {construct}")
        require(construct not in seen, f"Duplicate construct row: {construct}")
        seen.add(construct)

        reported = as_int(row["reported"], f"{construct}:reported")
        evaluated = as_int(row["empirically_evaluated"], f"{construct}:empirically_evaluated")
        criterion = as_int(row["criterion_satisfying"], f"{construct}:criterion_satisfying")
        denominator = as_int(row["denominator"], f"{construct}:denominator")

        require(denominator == 82, f"Construct denominator drift for {construct}: {denominator} != 82")
        require(0 <= criterion <= evaluated <= reported <= denominator,
                f"Construct evidence levels are not nested for {construct}")
        require((reported, evaluated, criterion) == expected[construct],
                f"Frozen construct counts drift for {construct}: {(reported, evaluated, criterion)} != {expected[construct]}")


def validate_evidence_control_appraisal() -> None:
    rows = load_tsv("evidence_control_appraisal.tsv")
    expected = {
        "Baseline adequacy": (43, 28, 0, 11),
        "Resource parity": (0, 24, 37, 21),
        "Statistical robustness": (12, 32, 0, 38),
        "Dependence control": (0, 1, 9, 72),
        "Failure testing": (4, 16, 22, 40),
        "Reproducibility": (8, 34, 0, 40),
        "Resource reporting": (14, 64, 0, 4),
    }
    require(len(rows) == len(expected), f"Expected {len(expected)} appraisal rows, found {len(rows)}")

    seen: set[str] = set()
    for row in rows:
        dimension = row["dimension"]
        require(dimension in expected, f"Unexpected appraisal dimension: {dimension}")
        require(dimension not in seen, f"Duplicate appraisal dimension: {dimension}")
        seen.add(dimension)

        values = tuple(as_int(row[key], f"{dimension}:{key}") for key in ("strong", "partial", "reported_only", "limited"))
        denominator = as_int(row["denominator"], f"{dimension}:denominator")
        require(denominator == 82, f"Appraisal denominator drift for {dimension}: {denominator} != 82")
        require(sum(values) == denominator, f"Appraisal categories do not sum to 82 for {dimension}: {values}")
        require(values == expected[dimension], f"Frozen appraisal counts drift for {dimension}: {values} != {expected[dimension]}")


def validate_external_coverage() -> None:
    rows = load_tsv("rif_external_coverage.tsv")
    require(len(rows) == 8, f"Expected 8 fixed post-freeze coverage candidates, found {len(rows)}")

    expected_ids = {"COV-001", "COV-002", "COV-003", "COV-004", "COV-005", "COV-006", "COV-016", "COV-017"}
    ids = [row["candidate_id"] for row in rows]
    require(set(ids) == expected_ids, f"Coverage candidate identity drift: {sorted(set(ids))}")
    require(len(ids) == len(set(ids)), "Duplicate candidate_id in rif_external_coverage.tsv")

    dois = [row["doi"].strip().lower() for row in rows if row["doi"].strip()]
    require(len(dois) == len(set(dois)), "Duplicate DOI in rif_external_coverage.tsv")

    statuses = [row["status"] for row in rows]
    require(statuses.count("FULLTEXT_CODED") == 7, "External coverage must retain exactly seven FULLTEXT_CODED records")
    require(statuses.count("TECHNICAL_EXCLUSION") == 1, "External coverage must retain exactly one TECHNICAL_EXCLUSION")

    code_columns = [
        "source_quality",
        "dependence",
        "uncertainty_calibration",
        "provenance",
        "topology_fusion",
        "faults",
        "recovery_abstention",
        "resources",
    ]
    allowed = {"R", "E", "C", "--", "NA"}

    for row in rows:
        for column in code_columns:
            require(row[column] in allowed, f"Invalid RIF code {row[column]!r} in {row['candidate_id']}:{column}")
        if row["status"] == "TECHNICAL_EXCLUSION":
            require(row["candidate_id"] == "COV-006", "The technical exclusion must remain COV-006")
            require(all(row[column] == "NA" for column in code_columns),
                    "Technical exclusion must use NA across all RIF coding columns")
        else:
            require(all(row[column] != "NA" for column in code_columns),
                    f"FULLTEXT_CODED record {row['candidate_id']} contains NA")


def main() -> int:
    checks = [
        validate_corpus_snapshot,
        validate_construct_profile,
        validate_evidence_control_appraisal,
        validate_external_coverage,
    ]
    try:
        for check in checks:
            check()
    except ValidationError as exc:
        print(f"VALIDATION FAILED: {exc}", file=sys.stderr)
        return 1

    print("Public release validation passed.")
    print("Frozen accounting: 3,367 -> 463 -> 175 -> 82.")
    print("Rights-safe aggregate tables and the eight-record post-freeze coverage set are internally consistent.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
