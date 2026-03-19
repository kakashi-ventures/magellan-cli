---
name: cross-model-validator
description: Validates hypotheses by calling OpenAI (GPT-5.4 Pro) and Google Gemini (3.1 Pro) APIs directly. Generates export prompts, runs API calls, and produces cross-model consensus report.
model: sonnet
tools: Read, Write, Bash, Glob
permissionMode: bypassPermissions
---

# Cross-Model Validator Agent

## GOAL

Validate MAGELLAN hypotheses by dispatching them to GPT-5.4 Pro and
Gemini 3.1 Pro simultaneously, then synthesizing a cross-model consensus
report. This agent handles both automatic API validation AND manual
export file generation (fallback when API keys are not set).

## CONSTRAINTS

- All file writes go to the session-scoped `{results_dir}/` directory
- Never fabricate validation results — only report what the APIs return
- If both API keys are missing, generate export files and exit with clear instructions
- Read prompt templates but ADAPT them to the specific hypotheses — never use verbatim
- Do NOT use pipeline jargon in export prompts (no "composite score", "Quality Gate", etc.)

## PROCESS

### Step 1: Read State

Read `state/session.json` to extract:
- `final` array — hypothesis cards with verdict, score, confidence, novelty
- `results_dir` — session-scoped output directory
- `session_id`
- `selected_target` — fields A and C

Only process hypotheses with `verdict` = `PASS` or `CONDITIONAL_PASS`.
If no hypotheses passed, write a note and exit.

### Step 2: Generate Export Prompts

Read prompt templates:
- `prompts/gpt-validation.md` — GPT validation structure
- `prompts/gemini-deep-think.md` — Gemini structural analysis format

For each passing hypothesis, create a self-contained prompt that includes:
- Context: what this is (AI-generated hypothesis, request for validation)
- The full hypothesis: mechanism, supporting evidence, counter-evidence, proposed test
- All cited papers with enough detail for verification
- Specific validation tasks

**GPT prompt** (`{results_dir}/export-gpt.md`):
- Focus on: empirical novelty verification, citation checking, mechanism plausibility,
  counter-evidence search, experimental design review
- Use the template structure but adapt to the specific hypothesis content
- Explain any technical terms from the pipeline in plain language

**Gemini prompt** (`{results_dir}/export-gemini.md`):
- Focus on: mathematical structure detection, formal mappings, structural isomorphisms,
  quantitative predictions, verification approaches
- Use the template's output format (STRUCTURAL CONNECTION / FORMAL MAPPING / PREDICTION)

### Step 3: Check API Availability

The validation script auto-loads `.env.local` if present (keys don't need to be
exported to shell). Check both shell env AND .env.local:

```bash
# Check shell env
echo "OPENAI_ENV=$([ -n "$OPENAI_API_KEY" ] && echo 'available' || echo 'not set')"
echo "GEMINI_ENV=$([ -n "$GEMINI_API_KEY" ] && echo 'available' || echo 'not set')"
# Check .env.local
grep -q 'OPENAI_API_KEY' .env.local 2>/dev/null && echo "OPENAI_FILE=available" || echo "OPENAI_FILE=not set"
grep -q 'GEMINI_API_KEY' .env.local 2>/dev/null && echo "GEMINI_FILE=available" || echo "GEMINI_FILE=not set"
```

Keys are available if present in EITHER shell env OR .env.local.

If BOTH keys are unset:
- Write export files (already done in Step 2)
- Update `state/session.json`:
  ```json
  {
    "cross_model_validation": {
      "status": "manual_export_only",
      "reason": "No API keys configured",
      "export_files": {
        "gpt": "{results_dir}/export-gpt.md",
        "gemini": "{results_dir}/export-gemini.md"
      }
    }
  }
  ```
- Exit with message:
  > Export files generated for manual validation.
  > To enable automatic validation, set OPENAI_API_KEY and/or GEMINI_API_KEY.

### Step 4: Install Dependencies and Run Validation

```bash
cd /home/ameft/kva/magellan && npm install --silent 2>&1 | tail -1
```

Then run the validation script with `--env-file` to load API keys from `.env.local`:

```bash
cd /home/ameft/kva/magellan && node --env-file=.env.local scripts/validate-crossmodel.mjs \
  --gpt-prompt "{results_dir}/export-gpt.md" \
  --gpt-out "{results_dir}/validation-gpt.md" \
  --gemini-prompt "{results_dir}/export-gemini.md" \
  --gemini-out "{results_dir}/validation-gemini.md"
```

The script runs both API calls in parallel and outputs a JSON status report.
If only one API key is available, only that model runs.

**Timeout**: Allow up to 10 minutes for the script (GPT-5.4 Pro with reasoning
can take several minutes on complex scientific prompts).

### Step 5: Parse Results and Generate Consensus Report

Read the validation outputs:
- `{results_dir}/validation-gpt.md` — GPT-5.4 Pro response
- `{results_dir}/validation-gemini.md` — Gemini 3.1 Pro response

For each hypothesis, extract and compare:

**From GPT**: Novelty verdict, confidence update, counter-evidence, experimental feasibility
**From Gemini**: Structural depth, formal mapping type, confidence, predictions

Write `{results_dir}/cross-model-consensus.md`:

```markdown
# Cross-Model Validation Consensus — Session {session_id}

## Methodology
- **GPT-5.4 Pro** (reasoning: high): Empirical validation — novelty, citations,
  mechanism plausibility, counter-evidence, experimental design
- **Gemini 3.1 Pro** (thinking: HIGH): Structural analysis — mathematical
  mappings, formal isomorphisms, quantitative predictions

## Per-Hypothesis Consensus

### {Hypothesis Title}

| Dimension | GPT-5.4 Pro | Gemini 3.1 Pro | Consensus |
|-----------|-------------|----------------|-----------|
| Novelty | {verdict} | {structural depth} | {agree/diverge} |
| Confidence | {X}/10 | {Y}/10 | {averaged or range} |
| Mechanism | {plausibility} | {mapping type} | {synthesis} |
| Testability | {feasibility} | {verification approach} | {combined} |

**Agreement areas**: {where both models converge}
**Divergence areas**: {where they disagree — investigate these}
**Combined recommendation**: {HIGH PRIORITY / PROMISING / NEEDS WORK / UNLIKELY}

---

## Summary

### High-Priority Candidates (2+ models agree, high confidence)
- ...

### Needs Investigation (models diverge)
- ...

### Next Steps
1. {specific recommendations}
2. {domain experts to consult}
```

If only one model ran, note this and provide single-model analysis.

### Step 6: Update State

Update `state/session.json` with:

```json
{
  "cross_model_validation": {
    "status": "completed",
    "gpt_model": "gpt-5.4-pro",
    "gemini_model": "gemini-3.1-pro-preview",
    "models_used": ["openai", "gemini"],
    "consensus": {
      "{hypothesis_id}": {
        "gpt_confidence": null,
        "gemini_confidence": null,
        "gpt_novelty": null,
        "gemini_depth": null,
        "agreement": "high|medium|low",
        "combined_recommendation": "..."
      }
    },
    "files": {
      "gpt_validation": "{results_dir}/validation-gpt.md",
      "gemini_validation": "{results_dir}/validation-gemini.md",
      "consensus": "{results_dir}/cross-model-consensus.md"
    }
  }
}
```

Fill in actual values from the parsed responses.
