---
name: discovery-engine
description: Core methodology for AI-powered scientific hypothesis generation. Auto-loaded when discovering connections, generating hypotheses, exploring cross-disciplinary links. Includes facet recombination, adversarial prompting, evolutionary refinement, groundedness checking, and hypothesis card format.
user-invocable: false
---

# Scientific Discovery Engine v4 — Core Methodology

## Hypothesis Generation Techniques

### Facet Recombination (from Scideator, Radensky et al. 2024)
Decompose findings into {Purpose, Mechanism, Evaluation}.
Novel ideas: take MECHANISM from Field A → apply to PURPOSE of Field C.

### Adversarial Prompting
- "What would a [distant-field expert] say about this [domain] problem?"
- "What if the opposite of [established belief] were true?"

### Evolutionary Refinement (from MOOSE-Chem, Yang et al. ICLR 2025)
Generate N variants → Select best → Crossover → Mutate → Re-evaluate.

### Null Hypothesis Inversion
"What would have to be true for A to NOT connect to C?"
If non-connection requirements are implausible, the connection is worth exploring.

### Scale Bridging
"Does [phenomenon at scale X] have an analogue at scale Y?"

## Hypothesis Card Format

```
═══════════════════════════════════════════
HYPOTHESIS: [One-line title]
═══════════════════════════════════════════
CONNECTION: [Field A] →→ [Bridge] →→ [Field C]
CONFIDENCE: [1-10] — [justification]
NOVELTY: [Novel / Partially explored / Known]
GROUNDEDNESS: [High / Medium / Low] — [what's grounded vs speculative]
IMPACT IF TRUE: [Low / Medium / High / Transformative]

MECHANISM
[2-4 paragraphs. Specific details: molecules, equations, pathways.
Mark which claims are literature-grounded vs parametric-speculative.]

SUPPORTING EVIDENCE
• From Field A: [finding + source if known]
• From Field C: [finding + source if known]
• Bridge: [what links them]

COUNTER-EVIDENCE & RISKS
• [specific reasons this could be wrong]

HOW TO TEST
1. [approach]
2. [expected result if TRUE]
3. [expected result if FALSE]
4. [effort estimate]
═══════════════════════════════════════════
```

## Grounding Protocol (AFTER generation)
1. Novelty search: "[Field A] [Field C] [bridge concept]"
2. Counter-evidence: evidence AGAINST the hypothesis
3. Review articles in both fields
4. Preprint check: arXiv, bioRxiv
Update confidence, novelty, AND groundedness based on findings.
