# Session Summary Formatting Guide

Write {results_dir}/session-summary.md and {results_dir}/final-hypotheses.md.
Start session-summary with health status and contributor attribution (if connected):

```markdown
# Session Summary
## Status: [SUCCESS|PARTIAL|DEGRADED|FAILED]
## Reason: [1 sentence explanation]
## Contributor: [display_name from .magellan/config.json, or "Anonymous" if not connected]
```

## By Status Type

### FAILED
- Do NOT present hypothesis cards
- Write cause of failure with specific phase and reason
- Write: "Run `/discover` again to retry, or `/discover [topic]` with a specific target."
- Include kill reasons if available

### DEGRADED
- Present cards with warning: "**Warning: Did not pass Quality Gate — for reference only.**"
- Explain what failed in Quality Gate
- Suggest running `/validate [hypothesis]` for deeper analysis

### PARTIAL and SUCCESS
Include:
- Mode used, target selected, why
- Pipeline stats: generated → survived → ranked → evolved → approved
- Each final hypothesis card
- Cross-model recommendations
- Remaining targets for future sessions
- Suggested follow-ups

## Cross-Model Validation Results

If cross_model_validation.status == "completed":
- Include the consensus summary from {results_dir}/cross-model-consensus.md
- Highlight HIGH PRIORITY candidates (where both models agree)
- Flag divergences that need investigation
- "Cross-model validation was performed automatically by GPT-5.4 Pro and Gemini 3.1 Pro."

If cross_model_validation.status == "manual_export_only":
- "Export files were generated for manual validation (no API keys configured)."
- Include instructions:
  1. "Open `{results_dir}/export-gpt.md` and paste into ChatGPT with GPT-5.4 Pro"
  2. "Open `{results_dir}/export-gemini.md` and paste into Gemini AI Studio with 3.1 Pro"
  3. "Hypotheses where 2+ models agree on high novelty + confidence are your best candidates"
- "To enable automatic validation in future sessions, set OPENAI_API_KEY and/or GEMINI_API_KEY."

## Impact Assessment (v5.14)

If impact_assessment data is available (Scout provided impact_potential):
- **Target impact potential**: X/10 (type: translational|paradigm|enabling_technology|conceptual_framework)
- **Application pathway**: [from Scout output]
- **Convergence signals**: X clinical trials, X grants, X patents (from Convergence Scanner)
- **Impact Potential Score (IPS)**: X.X/10 (weighted: Scout 0.4, convergence 0.6)
- **Per-hypothesis impact annotations** (from Quality Gate):
  - [Hypothesis ID]: [application pathway] | [applied domain] | [validation horizon]

## For Non-Expert User
List specific types of domain experts who could evaluate each hypothesis.
