#!/usr/bin/env python3
"""Cross-Model Validator SubagentStop gate. WARN-ONLY — never blocks.
Checks that export files and/or validation outputs were produced."""
import sys, json, os

try:
    state_path = "state/session.json"
    results_dir = "results"

    if os.path.exists(state_path):
        d = json.load(open(state_path))
        results_dir = d.get("results_dir", "results")

    export_gpt = os.path.join(results_dir, "export-gpt.md")
    export_gemini = os.path.join(results_dir, "export-gemini.md")
    validation_gpt = os.path.join(results_dir, "validation-gpt.md")
    validation_gemini = os.path.join(results_dir, "validation-gemini.md")
    consensus = os.path.join(results_dir, "cross-model-consensus.md")

    exports = []
    validations = []
    warnings = []

    if os.path.exists(export_gpt):
        exports.append("GPT")
    if os.path.exists(export_gemini):
        exports.append("Gemini")
    if not exports:
        warnings.append("No export files generated")

    if os.path.exists(validation_gpt):
        validations.append(f"GPT ({os.path.getsize(validation_gpt)}B)")
    if os.path.exists(validation_gemini):
        validations.append(f"Gemini ({os.path.getsize(validation_gemini)}B)")

    # Detect wrong-named files (legacy naming: gpt-validation.md instead of validation-gpt.md)
    wrong_gpt = os.path.join(results_dir, "gpt-validation.md")
    wrong_gemini = os.path.join(results_dir, "gemini-validation.md")
    if os.path.exists(wrong_gpt) and not os.path.exists(validation_gpt):
        warnings.append("Found gpt-validation.md (wrong name) without validation-gpt.md")
    if os.path.exists(wrong_gemini) and not os.path.exists(validation_gemini):
        warnings.append("Found gemini-validation.md (wrong name) without validation-gemini.md")

    has_consensus = os.path.exists(consensus)

    # Check state was updated
    cmv = d.get("cross_model_validation", {}) if os.path.exists(state_path) else {}
    status = cmv.get("status", "unknown")

    parts = [f"status={status}"]
    if exports:
        parts.append(f"exports=[{','.join(exports)}]")
    if validations:
        parts.append(f"validations=[{','.join(validations)}]")
    if has_consensus:
        parts.append(f"consensus={os.path.getsize(consensus)}B")
    if warnings:
        parts.append(f"warnings=[{'; '.join(warnings)}]")

    print(json.dumps({
        "feedback": f"Cross-model validator PASSED: {', '.join(parts)}"
    }))
    sys.exit(0)

except Exception as e:
    print(json.dumps({"feedback": f"WARNING: cross-model-validator gate error: {e}. Allowing through."}))
    sys.exit(0)
