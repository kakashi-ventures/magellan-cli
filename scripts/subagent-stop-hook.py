#!/usr/bin/env python3
"""SubagentStop hook. Validates expected outputs based on agent type."""
import sys, json, os

try:
    data = json.load(sys.stdin)
    agent_type = data.get("agent_type", "unknown")

    warnings = []
    state_path = "state/session.json"

    if os.path.exists(state_path):
        d = json.load(open(state_path))

        if agent_type == "scout":
            targets = d.get("scout_targets", [])
            if not targets:
                warnings.append("Scout finished but scout_targets is empty in state")

        elif agent_type == "generator":
            hyps = d.get("metadata", {}).get("total_hypotheses_generated", 0)
            if hyps == 0:
                warnings.append("Generator finished but no hypotheses recorded in state")

        # Phase agents write their artifacts to {results_dir}/, never into
        # session.json: it is a slim coordination index and must not carry
        # hypothesis content. Check the files the orchestrator actually reads.
        elif agent_type in ("critic", "ranker", "evolver"):
            cycle = d.get("cycle", 1)
            results_dir = d.get("results_dir", "")
            expected = {
                "critic": (f"cycle{cycle}-critiqued.json", f"critiqued-cycle{cycle}.md"),
                "ranker": (f"cycle{cycle}-ranked.json", f"ranked-cycle{cycle}.md"),
                "evolver": (f"cycle{cycle}-evolved.json", f"evolved-cycle{cycle}.md"),
            }[agent_type]
            if results_dir:
                for fname in expected:
                    if not os.path.exists(os.path.join(results_dir, fname)):
                        warnings.append(
                            f"{agent_type.capitalize()} finished but {fname} is missing from {results_dir}"
                        )

    feedback = f"Subagent [{agent_type}] completed."
    if warnings:
        feedback += " WARNINGS: " + "; ".join(warnings)
    feedback += " Read state/session.json for current state. Continue with next phase without waiting for user input."

    print(json.dumps({"systemMessage": feedback}))

except Exception as e:
    print(json.dumps({"systemMessage": f"Subagent completed. WARNING: hook error: {e}. Read state/session.json and continue."}))
