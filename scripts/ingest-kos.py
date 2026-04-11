#!/usr/bin/env python3
"""CLI entry point for KO ingestion from MAGELLAN session results.

Usage:
  python3 scripts/ingest-kos.py results/2026-04-08-autonomous-022
  python3 scripts/ingest-kos.py results/2026-04-08-autonomous-022 --verbose
  python3 scripts/ingest-kos.py --all    # Ingest all sessions in results/
"""

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from epistemic.ingest import SessionIngester
from epistemic import store


def main():
    parser = argparse.ArgumentParser(description="Ingest MAGELLAN session results into KO graph")
    parser.add_argument("results_dir", nargs="?",
                        help="Path to session results directory")
    parser.add_argument("--all", action="store_true",
                        help="Ingest all sessions in results/")
    parser.add_argument("--verbose", action="store_true",
                        help="Show detailed ingestion output")
    parser.add_argument("--dry-run", action="store_true",
                        help="Parse without writing to graph")
    args = parser.parse_args()

    if not args.results_dir and not args.all:
        parser.error("Provide a results directory or use --all")

    dirs = []
    if args.all:
        results_root = os.path.join(os.path.dirname(os.path.dirname(
            os.path.abspath(__file__))), "results")
        if os.path.isdir(results_root):
            for entry in sorted(os.listdir(results_root)):
                full = os.path.join(results_root, entry)
                if os.path.isdir(full) and entry != ".gitkeep":
                    dirs.append(full)
        if not dirs:
            print("No session directories found in results/")
            return
    else:
        if not os.path.isdir(args.results_dir):
            print(f"Error: {args.results_dir} is not a directory")
            sys.exit(1)
        dirs.append(args.results_dir)

    total_kos = 0
    total_edges = 0

    for d in dirs:
        session_id = os.path.basename(d)
        print(f"Ingesting session: {session_id}")

        ingester = SessionIngester(d, session_id)
        result = ingester.ingest_all()

        total_kos += result["kos_created"]
        total_edges += result["edges_created"]

        print(f"  KOs created: {result['kos_created']}")
        print(f"  Edges created: {result['edges_created']}")

        if args.verbose:
            for ko_id in result["ko_ids"]:
                ko = store.get_ko(ko_id)
                if ko:
                    print(f"    {ko_id} [{ko['class']}] {ko.get('summary', '')[:80]}")

    print(f"\nTotal: {total_kos} KOs, {total_edges} edges across {len(dirs)} session(s)")
    stats = store.graph_stats()
    print(f"Graph now: {stats['total_kos']} KOs, {stats['total_edges']} edges")


if __name__ == "__main__":
    main()
