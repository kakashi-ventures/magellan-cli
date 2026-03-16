---
name: hypothesis-validation
description: Validation methodology for scientific hypotheses. Auto-loaded when checking novelty, searching for counter-evidence, designing experiments, or assessing confidence calibration. Includes groundedness assessment protocol.
user-invocable: false
---

# Hypothesis Validation Protocol v4

## Novelty Verification
Search for direct papers, mechanism papers, reviews, preprints, patents.
Verdicts: NOVEL / PARTIALLY EXPLORED / ALREADY KNOWN / CONTESTED

## Groundedness Assessment (NEW v4)
For each factual claim in the hypothesis:
1. Is it from literature context provided? → GROUNDED (cite source)
2. Is it verifiable via web search? → VERIFIABLE (cite search result)
3. Is it from parametric knowledge only? → PARAMETRIC (flag as requiring verification)
4. Is it pure speculation? → SPECULATIVE (flag clearly)

Groundedness score = (GROUNDED + VERIFIABLE) / total claims

## Counter-Evidence Hierarchy
1. Direct experimental contradiction (strongest)
2. Theoretical impossibility (energy/time scale mismatch)
3. Failed attempts in adjacent areas
4. Confounding variables not accounted for
5. Simpler alternative explanations (Occam's razor)

## Confidence Calibration
- 1-2: Wild speculation, no mechanistic basis
- 3-4: Interesting analogy but no direct evidence
- 5-6: Plausible mechanism with some indirect support
- 7-8: Strong indirect evidence, specific testable prediction
- 9-10: Near-certain (reserve for connections with direct evidence)

Most genuine discoveries land at 4-6. If all hypotheses are 7+,
the Critic isn't working hard enough.

## Experimental Design Template
- Approach: computational / wet lab / clinical / observational / theoretical
- Positive control, negative control
- Minimum sample size for statistical significance
- Expected effect size based on related work
- Total estimated cost and time
- Required expertise
