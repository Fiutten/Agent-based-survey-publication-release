# Frozen database search strategy

Primary snapshot close: **4 August 2026**. Searches covered 2023-2026, English-language Article / Conference Paper (Proceedings Paper in Web of Science) / Review records. Counts in the manuscript remain frozen to this snapshot. Any later frontier or venue records are excluded from the 175/82 quantitative denominators.

## Scopus common filters

- Publication years: 2023-2026 inclusive (`PUBYEAR > 2022 AND PUBYEAR < 2027`).
- Language: English.
- Document types: Article, Conference Paper, Review.
- Source types: Journal, Conference Proceeding.
- Eight complementary query families S1-S8.
- Rows considered across S1-S8: 4,632; unique Scopus EIDs after cross-search consolidation: 2,613.

### S1 - reliability core (679 rows)

```text
TITLE-ABS-KEY(
  ("large language model*" OR "language model agent*" OR "LLM-based agent*" OR "LLM agent*" OR "foundation model agent*")
  AND
  ("multi-agent debate" OR "multiagent debate" OR "multi-agent collaboration" OR "multiagent collaboration" OR "multi-agent reasoning" OR "multiagent reasoning" OR "multi-agent framework*" OR "multi-agent architecture*" OR "LLM-based multi-agent*" OR "multi-agent LLM*" OR "agent team*" OR "collective reasoning")
  AND
  (reliab* OR robust* OR trustworth* OR failure* OR "faulty agent*" OR resilience OR uncertainty OR confidence OR calibration OR "error propagation" OR "failure propagation")
)
AND PUBYEAR > 2022
AND PUBYEAR < 2027
```

### S2 - fusion, aggregation and consensus (535 rows)

```text
TITLE-ABS-KEY(
  ("large language model*" OR "LLM agent*" OR "LLM-based agent*" OR "language model agent*" OR "foundation model agent*" OR "generative agent*")
  AND
  ("multi-agent" OR multiagent OR "agent team*" OR "agent debate" OR "agent collaboration" OR "collective reasoning")
  AND
  ("information fusion" OR "decision fusion" OR "evidence fusion" OR "belief fusion" OR "opinion fusion" OR aggregat* OR consensus OR voting OR ensemble* OR deliberation OR debate OR "collective intelligence")
)
AND PUBYEAR > 2022
AND PUBYEAR < 2027
```

### S3 - debate and collaborative reasoning (701 rows)

```text
TITLE-ABS-KEY(
  ("large language model*" OR "LLM agent*" OR "LLM-based agent*" OR "language model agent*" OR "foundation model agent*" OR "generative agent*")
  AND
  ("multi-agent debate" OR "multiagent debate" OR "agent debate" OR "LLM debate" OR "multi-agent collaboration" OR "multiagent collaboration" OR "collaborative LLM*" OR "multi-agent reasoning" OR "multiagent reasoning" OR "collaborative reasoning" OR "collective reasoning" OR "agent deliberation" OR "multi-agent discussion")
)
AND PUBYEAR > 2022
AND PUBYEAR < 2027
```

### S4 - uncertainty, confidence and calibration (266 rows)

```text
TITLE-ABS-KEY(
  ("large language model*" OR "LLM agent*" OR "LLM-based agent*" OR "language model agent*" OR "foundation model agent*" OR "generative agent*")
  AND
  ("multi-agent" OR multiagent OR "agent team*" OR "agent debate" OR "agent collaboration" OR "collective reasoning")
  AND
  (uncertainty OR "uncertainty quantification" OR "uncertainty estimation" OR confidence OR calibration OR "confidence calibration" OR "calibrated confidence" OR abstention OR "selective prediction" OR "selective generation" OR "risk-aware" OR "belief estimation" OR "confidence aggregation")
)
AND PUBYEAR > 2022
AND PUBYEAR < 2027
```

### S5 - failures, propagation and resilience (313 valid rows)

```text
TITLE-ABS-KEY(
  ("large language model*" OR "LLM agent*" OR "LLM-based agent*" OR "language model agent*" OR "foundation model agent*" OR "generative agent*")
  AND
  ("multi-agent" OR multiagent OR "agent team*" OR "agent debate" OR "agent collaboration" OR "collective reasoning")
  AND
  (failure OR failures OR "failure analysis" OR "failure mode*" OR "faulty agent*" OR "agent fault*" OR "fault tolerance" OR "error propagation" OR "failure propagation" OR "cascading failure*" OR resilience OR Byzantine OR "malicious agent*" OR "compromised agent*" OR "adversarial agent*" OR "communication attack*")
)
AND PUBYEAR > 2022
AND PUBYEAR < 2027
```

The S5 correction retained Article / Conference Paper / Review, not Conference Review. Two valid records found only in the earlier export were retained and eight ineligible Conference Review records were discarded.

### S6 - diversity, dependence and redundancy (401 rows)

```text
TITLE-ABS-KEY(
  ("large language model*" OR "LLM agent*" OR "LLM-based agent*" OR "language model agent*" OR "foundation model agent*" OR "generative agent*")
  AND
  ("multi-agent" OR multiagent OR "agent team*" OR "agent debate" OR "agent collaboration" OR "collective reasoning")
  AND
  (diversity OR redundancy OR correlation OR dependence OR dependency OR "dependent evidence" OR "correlated evidence" OR "error correlation" OR "shared bias" OR "model diversity" OR "agent diversity" OR "response diversity" OR "reasoning diversity" OR "homogeneous agent*" OR "heterogeneous agent*")
)
AND PUBYEAR > 2022
AND PUBYEAR < 2027
```

### S7 - evaluation and resource-aware comparison (1,036 exported rows; 1,010 unique internal EIDs)

```text
TITLE-ABS-KEY(
  ("large language model*" OR "LLM agent*" OR "LLM-based agent*" OR "language model agent*" OR "foundation model agent*" OR "generative agent*")
  AND
  ("multi-agent" OR multiagent OR "agent team*" OR "agent debate" OR "agent collaboration" OR "collective reasoning")
  AND
  (benchmark* OR ablation OR "evaluation framework*" OR "evaluation protocol*" OR "comparative evaluation" OR "cost-aware evaluation" OR "budget-matched" OR "compute-matched" OR "inference budget" OR "token budget" OR "test-time compute" OR "single-agent baseline*" OR "multi-agent baseline*" OR "fair comparison" OR "cost efficiency" OR "performance-cost trade-off")
)
AND PUBYEAR > 2022
AND PUBYEAR < 2027
```

### S8 - provenance, attribution and evidence quality (701 rows)

```text
TITLE-ABS-KEY(
  ("large language model*" OR "LLM agent*" OR "LLM-based agent*" OR "language model agent*" OR "foundation model agent*" OR "generative agent*")
  AND
  ("multi-agent" OR multiagent OR "agent team*" OR "agent debate" OR "agent collaboration" OR "collective reasoning")
  AND
  (provenance OR traceability OR attribution OR "evidence quality" OR "evidence attribution" OR "source reliability" OR "source credibility" OR verification OR fact-checking OR hallucination OR misinformation OR "retrieval contamination" OR "citation verification" OR "reasoning trace*" OR "trace analysis")
)
AND PUBYEAR > 2022
AND PUBYEAR < 2027
```

## Web of Science Topic-query families

The archived search plan specified Web of Science Core Collection, years 2023-2026, English, Article / Proceedings Paper / Review Article, and SCI-EXPANDED, SSCI, ESCI, CPCI-S and CPCI-SSH where available. The exact historical interface collection label cannot be independently reconstructed from the retained licensed exports and is therefore not guessed. The Topic-query strings and reconciliation rules are preserved below.

### W1 - core reliability and failure mechanisms

```text
TS=(
  ("large language model*" OR "LLM agent*" OR "LLM-based agent*" OR "generative agent*")
  AND
  ("multi-agent" OR multiagent OR "agent team*" OR "multi-agent debate")
  AND
  (reliab* OR trustworth* OR robust* OR failure* OR "fault tolerance" OR "error propagation" OR resilience OR Byzantine OR adversarial)
)
```

### W2 - fusion, debate and consensus

```text
TS=(
  ("large language model*" OR "LLM agent*" OR "LLM-based agent*" OR "generative agent*")
  AND
  ("multi-agent" OR multiagent OR "agent debate" OR "collective reasoning")
  AND
  ("information fusion" OR "evidence fusion" OR consensus OR voting OR aggregation OR deliberation OR debate OR reconciliation)
)
```

### W3 - uncertainty, calibration and confidence

```text
TS=(
  ("large language model*" OR "LLM agent*" OR "LLM-based agent*" OR "generative agent*")
  AND
  ("multi-agent" OR multiagent OR "agent team*")
  AND
  (uncertainty OR calibration OR confidence OR abstention OR "selective prediction" OR "confidence aggregation")
)
```

### W4 - provenance, verification and correlated evidence

```text
TS=(
  ("large language model*" OR "LLM agent*" OR "LLM-based agent*" OR "generative agent*")
  AND
  ("multi-agent" OR multiagent OR "agent collaboration")
  AND
  (provenance OR traceability OR verification OR fact-checking OR hallucination OR "source reliability" OR diversity OR dependence OR correlation OR "shared bias")
)
```

## Reconciliation

Deduplication used DOI exact match, normalized-title exact match, fuzzy title plus year/first-author verification, and explicit version-family resolution for conference/journal pairs. Web of Science contributed 1,277 eligible rows, 885 within-database unique records, of which 131 overlapped the Scopus set and 754 were Web-of-Science-only. The resulting primary screening universe contains 3,367 unique records.

Licensed raw exports are not redistributed. This file is the rights-safe record of the executed query logic and frozen accounting used by the manuscript.
