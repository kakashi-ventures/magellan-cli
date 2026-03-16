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

## Logical Fallacy Checklist (for Critic)

For each hypothesis, systematically verify absence of:

**Causation fallacies**
- Post hoc ergo propter hoc (temporal sequence ≠ causation)
- Correlation treated as causation (shared upstream cause?)
- Reverse causation (effect mistaken for cause)
- Single cause attribution (complex phenomena reduced to one mechanism)

**Generalization fallacies**
- Hasty generalization (broad conclusions from limited data)
- Anecdotal evidence presented as proof
- Cherry-picking (selective citation of supporting evidence, ignoring contradictions)
- Ecological fallacy (group-level patterns assumed to hold at individual level)

**Statistical fallacies**
- Base rate neglect (ignoring prevalence when interpreting results)
- Texas sharpshooter (finding pattern in noise, then claiming it was predicted)
- Multiple comparisons without correction (p-hacking risk)
- Prosecutor's fallacy (confusing P(evidence|innocent) with P(innocent|evidence))

**Science-specific fallacies**
- Galileo gambit ("ridiculed therefore true")
- Argument from ignorance ("not disproven therefore true")
- Unfalsifiability (hypothesis structured to be untestable)
- Appeal to mechanism plausibility without empirical support

## Claim Strength Assessment (for Quality Gate)

For each claim in the hypothesis:
1. **Classify claim type**: causal / associative / descriptive
2. **Match language to evidence**: the strength of the wording must correspond to the strength of supporting evidence
3. **Red flags** — reject or downgrade if any are present:
   - Causal language derived from correlational data only
   - Absolute certainty without direct experimental evidence
   - Contradictory evidence acknowledged but dismissed without justification
   - Selective citation (only supporting references, known counter-evidence omitted)

Claim strength scale:
- **Established**: replicated experimental evidence directly supports the claim
- **Supported**: indirect evidence or strong mechanistic reasoning
- **Suggested**: correlational or analogical evidence only
- **Speculative**: no direct evidence, plausibility argument only

If claim language exceeds its evidence tier, flag for revision.

## Experimental Design Template
- Approach: computational / wet lab / clinical / observational / theoretical
- Positive control, negative control
- Minimum sample size for statistical significance
- Expected effect size based on related work
- Total estimated cost and time
- Required expertise
