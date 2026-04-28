---
description: "Export hypothesis cards as a self-contained prompt ready to paste into GPT-5.5 Pro or Gemini Deep Research Max for validation. Usage: /export [gpt|gemini|both]"
allowed-tools: Read, Write, Glob
---

# Export for Cross-Model Validation

## Target
$ARGUMENTS

Read `session_id` and `results_dir` from `state/session.json`.
Read final hypothesis cards from `{results_dir}/final.json`.
If that file is missing, try `state/session.json` `final` array as fallback.
If `results_dir` is missing, use `results/` as fallback.

### For GPT (argument: gpt or empty)

Create a SINGLE self-contained file in `{results_dir}/export-gpt.md`.

The file must be **completely self-contained** — GPT has NO context about
MAGELLAN, the pipeline, scoring systems, or prior sessions. Structure:

1. **Context section (top)**: Explain what this is in 2-3 sentences —
   an AI generated hypotheses connecting disjoint scientific fields,
   and this is a request for independent validation.
2. **What we need**: List the specific validation tasks (novelty check,
   citation verification, mechanism plausibility, counter-evidence,
   experimental design review, final assessment).
3. **The hypothesis**: Full mechanism, supporting evidence, counter-evidence,
   proposed test. Include all cited papers with enough detail for GPT to verify.
4. **Constraints**: Only cite found sources, be adversarial, check citations.

Do NOT use pipeline jargon (composite score, Quality Gate, groundedness %).
Instead explain in plain language what these mean.

Do NOT use the generic template from `prompts/validation-prompt-gpt.md` verbatim —
adapt it to the specific hypothesis being exported.

At the end, tell the user:
"File saved to {results_dir}/export-gpt.md.
Steps:
1. Open the file and copy all its content
2. Open ChatGPT → select GPT-5.5 Pro
3. Paste everything and send
4. Wait 30-90 min for the validation report (no streaming on gpt-5.5-pro;
   ChatGPT shows a 'Working...' indicator while the model reasons)"

### For Gemini (argument: gemini)

Same approach adapted for Gemini's strengths (mathematical structure,
formal reasoning, quantitative verification).
Save to `{results_dir}/export-gemini.md`.

Tell user:
"File saved to {results_dir}/export-gemini.md.
Steps:
1. Copy all content
2. Open Google AI Studio (aistudio.google.com) and select the Deep Research Max agent,
   OR paste the prompt into a Gemini Interactions API call with
   agent='deep-research-max-preview-04-2026' (see docs: ai.google.dev/gemini-api/docs/deep-research)
3. Paste and send
4. Wait 10-30 min for the cited research report (up to 60 min for complex prompts)"

### For both
Generate both files. Show both sets of instructions.
