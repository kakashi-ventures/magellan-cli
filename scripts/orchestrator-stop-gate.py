#!/usr/bin/env python3
"""Stop hook for orchestrator. Blocks premature termination if pipeline is incomplete.
Also validates kill rate and dispatch log on completion."""
import sys, json, os

try:
    state_path = "state/session.json"
    if os.path.exists(state_path):
        d = json.load(open(state_path))
        phase = d.get("phase", None)
        status = d.get("status", None)

        # Allow stop if no session active (no mode set = not a discovery run)
        if not d.get("mode"):
            print(json.dumps({"decision": "approve"}))
            sys.exit(0)

        # Allow stop if pipeline completed or explicitly failed
        if phase in ("complete", "failed") or status in ("success", "partial", "degraded", "failed"):
            warnings = []

            # Validate kill rate matches formula (v5.6: read from phase files)
            metadata = d.get("metadata", {})
            session_id = d.get("session_id", "")
            total_raw = 0
            total_killed = 0
            for cycle_num in [1, 2, 3]:
                raw_path = f"state/phases/{session_id}/cycle{cycle_num}-raw.json"
                crit_path = f"state/phases/{session_id}/cycle{cycle_num}-critiqued.json"
                if os.path.exists(raw_path):
                    raw_data = json.load(open(raw_path))
                    total_raw += len(raw_data) if isinstance(raw_data, list) else 0
                if os.path.exists(crit_path):
                    crit_data = json.load(open(crit_path))
                    if isinstance(crit_data, list):
                        for h in crit_data:
                            if isinstance(h, dict) and h.get("verdict", "").upper() == "KILLED":
                                total_killed += 1
            # Fallback: try legacy hypotheses object in session.json
            if total_raw == 0:
                hypotheses = d.get("hypotheses", {})
                for cycle_key in sorted(hypotheses.keys()):
                    cycle_data = hypotheses[cycle_key]
                    if not isinstance(cycle_data, dict):
                        continue
                    raw = cycle_data.get("raw", [])
                    total_raw += len(raw) if isinstance(raw, list) else 0
                    critiqued = cycle_data.get("critiqued", [])
                    if isinstance(critiqued, list):
                        for h in critiqued:
                            if isinstance(h, dict) and h.get("verdict", "").upper() == "KILLED":
                                total_killed += 1

            if total_raw > 0:
                expected_kill_rate = round(total_killed / total_raw * 100, 1)
                reported_kill_rate = metadata.get("kill_rate", 0)
                if abs(expected_kill_rate - reported_kill_rate) > 5:
                    warnings.append(
                        f"Kill rate mismatch: reported {reported_kill_rate}%, "
                        f"calculated {expected_kill_rate}% ({total_killed}/{total_raw})"
                    )

            # Check dispatch log for required agents
            dispatch_log_path = "state/dispatch-log.json"
            if os.path.exists(dispatch_log_path):
                dispatch_log = json.load(open(dispatch_log_path))
                dispatches = dispatch_log.get("dispatches", [])
                dispatched = set()
                for entry in dispatches:
                    if isinstance(entry, dict):
                        dispatched.add(entry.get("agent", ""))
                required = {"literature-scout", "generator", "critic", "ranker", "quality-gate",
                            "computational-validator", "session-analyst"}
                # Scout and Target Evaluator are only required in scout mode
                mode = d.get("mode", "")
                if mode == "scout":
                    required.add("scout")
                    required.add("target-evaluator")
                # Evolver is conditionally skippable in v5.1
                evolver_skipped = d.get("metadata", {}).get("evolver_skipped", False)
                if not evolver_skipped:
                    required.add("evolver")
                missing = required - dispatched
                if missing and status not in ("failed",):
                    warnings.append(f"Missing agent dispatches: {', '.join(sorted(missing))}")

            if warnings:
                print(json.dumps({
                    "feedback": f"Orchestrator gate PASSED with warnings: {'; '.join(warnings)}"
                }))
            else:
                print(json.dumps({
                    "feedback": "Orchestrator gate PASSED: pipeline complete."
                }))
            sys.exit(0)

        # Block: pipeline is mid-run
        progress = d.get("progress", {})
        current = progress.get("current_phase", phase)
        print(json.dumps({
            "decision": "block",
            "reason": f"Pipeline at phase {current}, not complete. Read state/session.json and continue from current phase."
        }))
        sys.exit(0)
    else:
        # No state file = not a discovery session, allow stop
        print(json.dumps({"decision": "approve"}))
        sys.exit(0)

except Exception as e:
    # On error, allow stop to prevent deadlock
    print(json.dumps({"decision": "approve"}))
    sys.exit(0)
