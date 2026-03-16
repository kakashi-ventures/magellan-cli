---
description: "Deep-validate a hypothesis with web search for novelty, counter-evidence, and experimental feasibility. Usage: /validate [hypothesis title or description]"
allowed-tools: Agent, WebSearch, WebFetch, Read, Write
---

# Validate Hypothesis v4

## Target
$ARGUMENTS

Look for the full hypothesis in results/*.md or state/session.json.

## Validation Steps (launch Steps 1-2 as parallel subagents)

**Step 1 — Novelty Verification:**
> Search thoroughly for:
> - Direct papers on this A→C connection
> - Review articles in both fields mentioning the connection
> - Preprints on arXiv/bioRxiv
> - Patents indicating commercial interest
> Verdict: NOVEL / PARTIALLY EXPLORED / ALREADY KNOWN

**Step 2 — Counter-Evidence Deep Dive:**
> Search for:
> - Evidence CONTRADICTING the hypothesis
> - Failed experiments in related areas
> - Theoretical reasons the mechanism shouldn't work

**Step 3 — Experimental Feasibility (after Steps 1-2):**
> Based on mechanism, assess: approach, equipment, timeline, cost,
> what positive/negative results look like.

**Step 4 — Update:**
> Save updated hypothesis card with "-validated" suffix to results/.
> Update Novelty, Counter-evidence, Experimental protocol, and Confidence.
