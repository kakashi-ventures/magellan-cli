---
description: "Export hypothesis cards as a self-contained prompt ready to paste into GPT-5.4 or Gemini for validation. Usage: /export [gpt|gemini|both]"
allowed-tools: Read, Write, Glob
---

# Export for Cross-Model Validation

## Target
$ARGUMENTS

Read final hypothesis cards from state/session.json `final` array.
If empty, read from results/session-summary.md or results/*.md.

### For GPT (argument: gpt or empty)

Create a SINGLE self-contained file `results/export-gpt.md` that contains:
1. The validation prompt from prompts/gpt-validation.md
2. A separator line
3. ALL final hypothesis cards, formatted clearly

The user should be able to copy-paste the ENTIRE file into ChatGPT
and get a validation report without any additional instructions.

At the end, tell the user:
"File saved to results/export-gpt.md.
Steps:
1. Open the file and copy all its content
2. Open ChatGPT → select GPT-5.4 Thinking or Pro
3. Enable Deep Research if available
4. Paste everything and send
5. Wait 5-30 min for the validation report"

### For Gemini (argument: gemini)

Same approach with prompts/gemini-deep-think.md.
Save to results/export-gemini.md.

Tell user:
"File saved to results/export-gemini.md.
Steps:
1. Copy all content
2. Open Gemini AI Studio → select 3.1 Pro or Deep Think
3. Paste and send"

### For both
Generate both files. Show both sets of instructions.
