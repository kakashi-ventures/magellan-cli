#!/usr/bin/env python3
"""SessionStart hook: warn (via the canonical `systemMessage` field) when the running
Claude Code version is below the floor this MAGELLAN pipeline depends on.

Fail-open by design: it never blocks startup and never errors loudly. If the version
cannot be determined, it stays silent.

Floor = v2.1.219. Rationale (features the pipeline now uses):
  - canonical hook output `systemMessage`/`additionalContext` (v2.1.163)
  - `terminalSequence` desktop notifications from hooks (v2.1.141)
  - hook exec-form `args: [...]` (v2.1.139)
  - `--fallback-model` / `fallbackModel` resilience (v2.1.166)
  - `opus` alias resolving to Claude Opus 5 (the pipeline's primary model,
    released 2026-07-24). This is the floor-setting feature: on older builds the
    `opus` alias in every agent's frontmatter resolves to an Opus 4.x model, so
    the pipeline silently runs on the wrong model rather than failing loudly.
  - `claude-opus-4-8` still addressable by full model ID (the documented refusal
    fallback target for Opus 5 `bio`/`cyber` classifier declines).
NOTE: the orchestrator itself runs on the SESSION model, not frontmatter, so a
correct version is necessary but not sufficient: the user must also select Opus 5
via `/model` before `/discover`.

Org-managed alternative: set `requiredMinimumVersion` in managed settings to refuse
startup below the floor (this hook only warns, which suits a distributable repo)."""
import sys, json, os, re, subprocess

MIN_VERSION = (2, 1, 219)
MIN_VERSION_STR = ".".join(map(str, MIN_VERSION))


def parse_version(s):
    m = re.search(r"(\d+)\.(\d+)\.(\d+)", s or "")
    return tuple(int(x) for x in m.groups()) if m else None


def detect_version(stdin_data):
    # 1) hook stdin payload, if it carries a version field
    for key in ("version", "claude_code_version", "cli_version"):
        v = parse_version(str(stdin_data.get(key, "")))
        if v:
            return v
    # 2) environment
    for env_key in ("CLAUDE_CODE_VERSION", "CLAUDECODE_VERSION"):
        v = parse_version(os.environ.get(env_key, ""))
        if v:
            return v
    # 3) subprocess fallback (fast: prints and exits)
    try:
        out = subprocess.run(
            ["claude", "--version"], capture_output=True, text=True, timeout=5
        ).stdout
        return parse_version(out)
    except Exception:
        return None


try:
    try:
        data = json.load(sys.stdin)
    except Exception:
        data = {}
    ver = detect_version(data if isinstance(data, dict) else {})
    if ver and ver < MIN_VERSION:
        running = ".".join(map(str, ver))
        print(json.dumps({
            "systemMessage": (
                f"MAGELLAN expects Claude Code >= {MIN_VERSION_STR} (running {running}). "
                "Some pipeline features (canonical hook output, terminalSequence "
                "notifications, hook exec-form, the `opus` alias = Claude Opus 5) "
                "need a newer version. Run `claude update`."
            )
        }))
    # Version OK or undetectable: stay silent (fail-open).
    sys.exit(0)
except Exception:
    sys.exit(0)
