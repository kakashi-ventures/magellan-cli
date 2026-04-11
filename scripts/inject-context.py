#!/usr/bin/env python3
"""CLI entry point for epistemic context injection.

Generates salience-filtered KO context for a specific agent.

Usage:
  python3 scripts/inject-context.py scout              # Context briefing for Scout
  python3 scripts/inject-context.py generator --json    # JSON output
  python3 scripts/inject-context.py critic --tensions   # Include tension fields
  python3 scripts/inject-context.py --all               # All agents summary
  python3 scripts/inject-context.py --dialectic         # Tension report only
"""

import argparse
import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from epistemic import context, dialectic, salience, store, config


def main():
    parser = argparse.ArgumentParser(description="Generate epistemic context for MAGELLAN agents")
    parser.add_argument("agent", nargs="?",
                        help="Agent ID (scout, generator, critic, etc.)")
    parser.add_argument("--json", action="store_true",
                        help="Output as JSON instead of formatted text")
    parser.add_argument("--tensions", action="store_true",
                        help="Include tension field briefing")
    parser.add_argument("--all", action="store_true",
                        help="Show context summary for all agents")
    parser.add_argument("--dialectic", action="store_true",
                        help="Show tension field report only")
    args = parser.parse_args()

    if args.dialectic:
        tensions = dialectic.detect_all_tensions(min_urgency=0.3)
        if args.json:
            print(json.dumps(tensions, indent=2))
        else:
            print(f"=== Dialectic Engine — Tension Report ===")
            print(f"Total tensions: {tensions.get('total_tensions', 0)}\n")
            for category, items in tensions.items():
                if isinstance(items, list) and items:
                    print(f"## {category} ({len(items)})")
                    for t in items:
                        print(f"  {context.format_tension_for_context(t)}")
                    print()
        return

    if args.all:
        stats = store.graph_stats()
        print(f"Graph: {stats['total_kos']} KOs, {stats['total_edges']} edges\n")
        print(f"{'Agent':<25} {'ρ':>5} {'KOs':>5} {'~Tokens':>8}")
        print("-" * 48)
        for agent_id in sorted(config.AGENT_RHO.keys()):
            ctx = context.build_agent_context(agent_id, include_tensions=False)
            s = ctx["stats"]
            print(f"{agent_id:<25} {s['rho']:>5.2f} {s['injected_kos']:>5} {s['estimated_tokens']:>8}")
        return

    if not args.agent:
        parser.error("Provide an agent ID or use --all / --dialectic")

    if args.agent not in config.AGENT_RHO:
        print(f"Unknown agent: {args.agent}")
        print(f"Valid agents: {', '.join(sorted(config.AGENT_RHO.keys()))}")
        sys.exit(1)

    ctx = context.build_agent_context(args.agent, include_tensions=args.tensions)

    if args.json:
        output = {
            "stats": ctx["stats"],
            "kos": [
                {"salience": round(s, 4), "id": ko["id"], "class": ko["class"],
                 "summary": ko.get("summary", ""), "K": ko["scores"]["K"]}
                for s, ko in ctx["kos"]
            ],
            "tensions": ctx.get("tensions", []),
        }
        print(json.dumps(output, indent=2))
    else:
        print(ctx["briefing"])
        s = ctx["stats"]
        print(f"\n--- {s['injected_kos']} KOs, ~{s['estimated_tokens']} tokens, ρ={s['rho']} ---")


if __name__ == "__main__":
    main()
