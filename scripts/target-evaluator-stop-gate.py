#!/usr/bin/env python3
"""Target Evaluator SubagentStop gate. BLOCKS if ALL target scores < 3 (all unsuitable).
Warns if any individual target scores < 3."""
import sys, json, os

try:
    state_path = "state/session.json"
    if os.path.exists(state_path):
        d = json.load(open(state_path))
        scores = d.get("target_quality_scores", [])

        if not scores or not isinstance(scores, list):
            # No scores written — warn but allow through
            print(json.dumps({
                "feedback": "WARNING: target-evaluator produced no scores. Allowing through."
            }))
            sys.exit(0)

        all_scores = []
        low_targets = []
        for entry in scores:
            if isinstance(entry, dict):
                score = entry.get("score", 0)
                all_scores.append(score)
                if score < 3:
                    low_targets.append(entry.get("target", "unknown"))

        if not all_scores:
            print(json.dumps({
                "feedback": "WARNING: target-evaluator scores unreadable. Allowing through."
            }))
            sys.exit(0)

        if all(s < 3 for s in all_scores):
            print(json.dumps({
                "decision": "block",
                "reason": f"BLOCKED: ALL {len(all_scores)} targets scored below 3. Scout should re-run with different strategies. Low targets: {', '.join(low_targets)}"
            }), file=sys.stderr)
            sys.exit(2)

        if low_targets:
            print(json.dumps({
                "feedback": f"Target evaluator PASSED with warnings: {len(low_targets)} target(s) scored < 3 ({', '.join(low_targets)}). Consider replacing weak targets."
            }))
        else:
            best = max(all_scores)
            print(json.dumps({
                "feedback": f"Target evaluator PASSED: best score {best}/10. All targets viable."
            }))
        sys.exit(0)
    else:
        print(json.dumps({
            "feedback": "WARNING: state/session.json not found. Allowing through."
        }))
        sys.exit(0)

except Exception as e:
    print(json.dumps({"feedback": f"WARNING: target-evaluator gate error: {e}. Allowing through."}))
    sys.exit(0)
