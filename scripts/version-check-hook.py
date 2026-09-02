#!/usr/bin/env python3
"""SessionStart hook: warn (via the canonical `systemMessage` field) when the running
Claude Code version is below the floor this MAGELLAN pipeline depends on.

Fail-open by design: it never blocks startup and never errors loudly. If the version
cannot be determined, it stays silent.

Floor = v2.1.257. Rationale (features the pipeline now uses):
  - canonical hook output `systemMessage`/`additionalContext` (v2.1.163)
  - `terminalSequence` desktop notifications from hooks (v2.1.141)
  - hook exec-form `args: [...]` (v2.1.139)
  - `--fallback-model` / `fallbackModel` resilience (v2.1.166)
  - `claude-fable-5-1` available as a model (the pipeline's primary model, pinned by
    full ID in every agent's frontmatter). This is the floor-setting feature: it
    enters as an option in v2.1.240 and becomes the default Fable model in
    v2.1.257, which is the floor taken here. On older builds the model ID is
    unknown, which fails loudly, unlike the previous alias-based pin.
  - `claude-opus-5` still addressable by full model ID in agent frontmatter (the
    persistent rollback target for classifier declines; the Agent tool's
    per-invocation `model` parameter accepts only aliases, so a full ID cannot be
    used there).
NOTE: the orchestrator itself runs on the SESSION model, not frontmatter, so a
correct version is necessary but not sufficient: the user must also select
Fable 5.1 via `/model claude-fable-5-1` before `/discover`.

Org-managed alternative: set `requiredMinimumVersion` in managed settings to refuse
startup below the floor (this hook only warns, which suits a distributable repo)."""
import sys, json, os, re, subprocess

MIN_VERSION = (2, 1, 257)
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
                "notifications, hook exec-form, the `claude-fable-5-1` model) "
                "need a newer version. Run `claude update`."
            )
        }))
    # Version OK or undetectable: stay silent (fail-open).
    sys.exit(0)
except Exception:
    sys.exit(0)
