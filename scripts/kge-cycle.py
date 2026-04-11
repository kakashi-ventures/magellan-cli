#!/usr/bin/env python3
"""CLI entry point for the Knowledge Graph Engine cycle.

Usage:
  python3 scripts/kge-cycle.py                    # Single cycle
  python3 scripts/kge-cycle.py --converge          # Run until convergence
  python3 scripts/kge-cycle.py --converge --verbose # With per-KO deltas
  python3 scripts/kge-cycle.py --stats             # Graph statistics only
"""

import argparse
import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from epistemic import kge, store


def main():
    parser = argparse.ArgumentParser(description="Run KGE cycle on the epistemic graph")
    parser.add_argument("--converge", action="store_true",
                        help="Run cycles until K-scores converge")
    parser.add_argument("--max-iterations", type=int, default=50,
                        help="Max iterations for convergence mode (default: 50)")
    parser.add_argument("--verbose", action="store_true",
                        help="Show per-KO score changes")
    parser.add_argument("--stats", action="store_true",
                        help="Print graph statistics and exit")
    args = parser.parse_args()

    if args.stats:
        stats = store.graph_stats()
        print(json.dumps(stats, indent=2))
        return

    if args.converge:
        results = kge.run_until_convergence(
            max_iterations=args.max_iterations, verbose=args.verbose
        )
        final = results[-1] if results else {}
        print(f"KGE converged after {len(results)} iterations")
        print(f"  KOs processed: {final.get('kos_processed', 0)}")
        print(f"  Max delta (final): {final.get('max_delta', 0):.6f}")
        print(f"  Zones: {json.dumps(final.get('zone_distribution', {}))}")
        if final.get("converged") is False:
            print(f"  WARNING: Did not converge within {args.max_iterations} iterations")
    else:
        stats = kge.run_cycle(verbose=args.verbose)
        print(f"KGE cycle completed")
        print(f"  KOs processed: {stats.get('kos_processed', 0)}")
        print(f"  Edges processed: {stats.get('edges_processed', 0)}")
        print(f"  Max delta: {stats.get('max_delta', 0):.6f}")
        print(f"  Zones: {json.dumps(stats.get('zone_distribution', {}))}")

        if args.verbose and stats.get("updates"):
            print(f"\n  Updates ({len(stats['updates'])} KOs changed):")
            for u in stats["updates"]:
                print(f"    {u['id']} [{u['class']}]: {u['old_K']:.4f} → {u['new_K']:.4f} ({u['delta']:+.4f}) [{u['zone']}]")


if __name__ == "__main__":
    main()
