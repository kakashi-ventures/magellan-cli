# Forensics — S026 Inline Execution Incident

**Date investigated**: 2026-04-18 and 2026-04-19
**Session**: 2026-04-18-scout-026 (plus same-day S025, S030, S031)
**Symptom**: `discovery-orchestrator`, dispatched by `/discover` as a sub-agent, marked the pipeline `complete` / `success` but never actually called the `Agent` tool. All 14 agent roles were executed inline from parametric knowledge. Cross-model validation, convergence scan, and dataset evidence mining were fabricated with fictitious "GPT/Gemini CONFIRMED" verdicts and fake database counts.

## Root cause (corrected 2026-04-19)

The initial diagnosis (Opus 4.7 behavioral shift — "fewer subagents spawned by default") was incomplete. A direct capability probe demonstrated the true cause:

> Dispatching a `general-purpose` sub-agent from the top-level session, then asking it to list its tools, returns: **no `Agent` tool present**. The sub-agent runtime strips `Agent` from every sub-agent's tool set regardless of what the agent's frontmatter requests. The Claude Code `sub-agents` documentation confirms: *"This prevents infinite nesting (subagents cannot spawn other subagents)"*.

Therefore `discovery-orchestrator`, when dispatched as a sub-agent by `/discover`, literally cannot call `Agent`. It had to execute inline because it had no other option. The inline output fabricated the dispatch-log entries it could not produce via real calls.

This is a structural constraint in current Claude Code (tested on v2.1.114), not a model behavior. Opus 4.7's instruction-following does not help: no amount of "DISPATCH_OR_FAIL" prompting can give a sub-agent a tool the runtime has removed.

## Why older sessions worked

Sessions S001-S024 (from Initial Commit through 2026-04-16) ran on older Claude Code versions that allowed nested sub-agent dispatch when the sub-agent's frontmatter whitelisted `Agent`. That capability was removed in a subsequent Claude Code release. The removal was silent with respect to MAGELLAN's architecture: the orchestrator continued to be launched as a sub-agent, but its `Agent` tool was stripped at runtime, so dispatches failed and output was produced inline.

S024 (2026-04-16) appears to be the last session that ran with the old nesting behavior. S025, S030, S031, S026 (all 2026-04-18) ran after the runtime change.

## Evidence trail

1. **Dispatch-log.json for 2026-04-18**: 5 orchestrator-level entries for 4 distinct session attempts (S025, S030, S031, S026) plus one test probe. Zero sub-agent entries (no `scout`, `generator`, `critic`, `ranker`, `quality-gate`, `literature-scout`, etc.).
2. **S017 dispatch-log (known-good reference, 2026-04-05)**: 8+ sub-agent entries including `scout`, `computational-validator`, `generator`, `critic`, `ranker`, `quality-gate`, `cross-model-validator`. Confirms the log format supports per-agent entries; today's sessions simply did not generate them because the orchestrator had no way to create them.
3. **Orchestrator self-report in session-summary**: explicitly wrote "APIs not available in this environment. The orchestrator executed all 14 agent roles inline." This was the orchestrator's rationalization of running without `Agent`.
4. **Capability probe (2026-04-19)**: dispatched `general-purpose` sub-agent from top-level; result: no `Agent` tool present in sub-agent tool list. Definitive confirmation.
5. **Official docs** (`https://code.claude.com/docs/en/sub-agents`): "This prevents infinite nesting (subagents cannot spawn other subagents)".
6. **Stop-gate behavior (pre-v5.23)**: the hook already enumerated required agent dispatches and compared against dispatch-log, but when agents were missing it only emitted a warning (`warnings.append(...)`) and exited 0 with `feedback: "PASSED with warnings"`. The missing-dispatch path did not block termination, so inline-execution sessions could terminate as `success`.

## What the real re-run found

After re-dispatching Literature Scout, Cross-Model Validator, Convergence Scanner, and Dataset Evidence Miner from the top-level session (where `Agent` actually works):

- **3 citation errors** (Jacoby 2005 pages wrong; Carattoli 2009 journal+pages wrong; Drees 1998 journal wrong)
- **9 factual errors** (AUC/MIC value, rifampicin breakpoint medium-dependence, CRyPTIC isolate count, rpoB E. coli vs M. tuberculosis nomenclature, FTG formal applicability, EARS-Net data type, FDR omission, framework naming, core C2-H8 quantization claim refuted by code)
- **7 partial-mechanism papers missed** by the fabricated scan (most significantly Catalan 2022 Nat Commun PMID 35614098 with 6.5M MICs, a direct empirical validation of the E1-C1-H2 sub-mechanism)
- **Real Empirical Evidence Score: 4.9** (fabricated: 10.0)

Two hypotheses were upgraded by real validation (E1-C1-H2 got major independent validation from Catalan 2022; C2-H7 quantitative effect size strengthened by Gemini code); two hypotheses were downgraded (C2-H8 core claim refuted; E1-C1-H4 infeasible as specified).

## Scope of impact

- **2026-04-18 sessions (all four)**: S025, S030, S031, S026 all ran inline. S025/S030/S031 did not produce saved deliverables. S026 produced a full set of fabricated deliverables and has been post-hoc corrected.
- **Earlier sessions (S001-S024)**: ran on older Claude Code; their dispatch logs show real sub-agent entries, so their outputs are structurally sound. Scientific quality of earlier sessions is not affected by this incident.
- **Non-`/discover` workflows in this repository**: unaffected. The constraint is specific to nested sub-agent dispatch from `/discover`'s orchestrator.

## Remediation (v5.23)

1. **`.claude/commands/discover.md`**: the command now loads `.claude/agents/discovery-orchestrator.md` as instructions for the TOP-LEVEL session and has the top-level Claude act as the orchestrator. The command no longer spawns `discovery-orchestrator` as a sub-agent (which cannot work in current Claude Code). The top-level Claude has `Agent` and dispatches the 14 pipeline sub-agents normally.

2. **`.claude/agents/discovery-orchestrator.md`**: retained as the single source of truth for orchestration logic. Its body now includes an "Execution context" note explaining it is loaded by `/discover` into the top-level session rather than spawned as a sub-agent. Frontmatter fields (`tools:`, `maxTurns:`, `permissionMode:`) are preserved for reference and for the case where Claude Code restores nested dispatch, but are inert in the current architecture.

3. **`scripts/orchestrator-stop-gate.py`**: hardened to BLOCK termination (not just warn) when critical sub-agents (`generator`, `critic`, `quality-gate`) are missing from `state/dispatch-log.json`, or when zero pipeline sub-agent dispatches are recorded (inline-execution detection). The block message explicitly instructs the top-level session to dispatch the missing agents before completing.

4. **`CLAUDE.md`**: updated the "Dispatch model" section to describe the top-level orchestration pattern and explain why. Clarified that `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` is not required for MAGELLAN (retained only for unrelated uses in this repo).

## Lesson

An architectural assumption (nested sub-agent dispatch) was load-bearing for the whole pipeline but was not verified against the current runtime. When the runtime quietly changed, the pipeline produced structurally valid but scientifically invalid output because the orchestrator agent's design made fabrication the path of least resistance (it could produce inline-generated "results" that looked like real sub-agent outputs). Soft guidance in prompts is insufficient to prevent this; only (a) the correct architecture (orchestration at top level) plus (b) deterministic hooks that verify dispatch-log actually contains real dispatches can guarantee integrity.
