#!/usr/bin/env python3
"""Literature Scout SubagentStop gate. BLOCKS if mandatory outputs are missing."""
import sys, json, os, glob

try:
    state_path = "state/session.json"
    papers_dir = "results/papers"
    errors = []

    # Check papers directory has at least 1 file
    if os.path.isdir(papers_dir):
        paper_files = [f for f in os.listdir(papers_dir) if f.endswith('.md')]
        if len(paper_files) == 0:
            errors.append("results/papers/ has 0 paper files (need at least 1)")
    else:
        errors.append("results/papers/ directory does not exist")

    # Check state has papers_retrieved
    if os.path.exists(state_path):
        d = json.load(open(state_path))
        papers = d.get("papers_retrieved", [])
        if not papers:
            errors.append("state/session.json papers_retrieved is empty")
    else:
        errors.append("state/session.json not found")

    # Check literature output file exists
    lit_context = os.path.exists("results/literature-context.md")
    lit_landscape = os.path.exists("results/literature-landscape.md")
    if not lit_context and not lit_landscape:
        errors.append("No literature output file (results/literature-context.md or results/literature-landscape.md)")

    if errors:
        print(json.dumps({
            "decision": "block",
            "reason": f"BLOCKED: Literature scout missing outputs: {'; '.join(errors)}. Fix before completing."
        }), file=sys.stderr)
        sys.exit(2)
    else:
        paper_count = len(paper_files) if os.path.isdir(papers_dir) else 0
        print(json.dumps({
            "feedback": f"Literature scout gate PASSED: {paper_count} papers saved."
        }))
        sys.exit(0)

except Exception as e:
    print(json.dumps({"feedback": f"WARNING: literature-scout gate error: {e}. Allowing through."}))
    sys.exit(0)
