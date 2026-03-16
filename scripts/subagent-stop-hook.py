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

        if agent_type == "sde-scout":
            targets = d.get("scout_targets", [])
            if not targets:
                warnings.append("Scout finished but scout_targets is empty in state")

        elif agent_type == "sde-generator":
            hyps = d.get("metadata", {}).get("total_hypotheses_generated", 0)
            if hyps == 0:
                warnings.append("Generator finished but no hypotheses recorded in state")

        elif agent_type == "sde-critic":
            cycle = d.get("cycle", 1)
            critiqued = d.get("hypotheses", {}).get(f"cycle{cycle}", {}).get("critiqued", None)
            if not critiqued:
                warnings.append(f"Critic finished but no critiqued data for cycle{cycle} in state")

        elif agent_type == "sde-ranker":
            cycle = d.get("cycle", 1)
            ranked = d.get("hypotheses", {}).get(f"cycle{cycle}", {}).get("ranked", None)
            if not ranked:
                warnings.append(f"Ranker finished but no ranked data for cycle{cycle} in state")

        elif agent_type == "sde-evolver":
            cycle = d.get("cycle", 1)
            evolved = d.get("hypotheses", {}).get(f"cycle{cycle}", {}).get("evolved", None)
            if not evolved:
                warnings.append(f"Evolver finished but no evolved data for cycle{cycle} in state")

    feedback = f"Subagent [{agent_type}] completed."
    if warnings:
        feedback += " WARNINGS: " + "; ".join(warnings)
    feedback += " Read state/session.json for current state. Continue with next phase without waiting for user input."

    print(json.dumps({"feedback": feedback}))

except Exception as e:
    print(json.dumps({"feedback": f"Subagent completed. WARNING: hook error: {e}. Read state/session.json and continue."}))
