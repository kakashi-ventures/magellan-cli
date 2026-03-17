#!/usr/bin/env python3
"""Literature Scout SubagentStop gate. Validates outputs but allows degraded mode
when MCP/web tools are unavailable (papers may be empty).
Supports session-scoped results directories."""
import sys, json, os

try:
    state_path = "state/session.json"
    errors = []
    warnings = []
    results_dir = "results"

    # Read state to get results_dir
    if os.path.exists(state_path):
        d = json.load(open(state_path))
        results_dir = d.get("results_dir", "results")
        papers = d.get("papers_retrieved", [])
        lit_unavailable = d.get("metadata", {}).get("literature_unavailable", False)
        if not papers and not lit_unavailable:
            warnings.append("state/session.json papers_retrieved is empty")
    else:
        errors.append("state/session.json not found")

    # Check papers directory
    papers_dir = os.path.join(results_dir, "papers")
    paper_count = 0
    if os.path.isdir(papers_dir):
        paper_files = [f for f in os.listdir(papers_dir) if f.endswith('.md')]
        paper_count = len(paper_files)
        if paper_count == 0:
            warnings.append(f"{papers_dir}/ has 0 paper files (MCP/web may be unavailable)")
    else:
        warnings.append(f"{papers_dir}/ directory does not exist")

    # Check literature output file exists (check both session-scoped and legacy paths)
    lit_found = False
    for base in [results_dir, "results"]:
        if os.path.exists(os.path.join(base, "literature-context.md")):
            lit_found = True
        if os.path.exists(os.path.join(base, "literature-landscape.md")):
            lit_found = True
    if not lit_found:
        errors.append(f"No literature output file in {results_dir}/ (literature-context.md or literature-landscape.md)")

    if errors:
        print(json.dumps({
            "decision": "block",
            "reason": f"BLOCKED: Literature scout missing critical outputs: {'; '.join(errors)}. Fix before completing."
        }), file=sys.stderr)
        sys.exit(2)
    elif warnings:
        print(json.dumps({
            "feedback": f"Literature scout gate PASSED with warnings: {'; '.join(warnings)}. Pipeline will proceed in degraded mode."
        }))
        sys.exit(0)
    else:
        print(json.dumps({
            "feedback": f"Literature scout gate PASSED: {paper_count} papers saved."
        }))
        sys.exit(0)

except Exception as e:
    print(json.dumps({"feedback": f"WARNING: literature-scout gate error: {e}. Allowing through."}))
    sys.exit(0)
