# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in MAGELLAN, please report it
responsibly via email:

**hello@magellan-discover.ai**

Please include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact

We aim to respond within 72 hours and will coordinate disclosure with you.

## Scope

**In scope:**
- Secret leakage (API keys, contributor keys, tokens in code or history)
- Prompt injection via agent definitions or hook configurations
- Abuse of the upload endpoint (session impersonation, data tampering)
- Hook bypass allowing unauthorized pipeline modifications

**Out of scope:**
- Hypothesis quality or scientific accuracy
- Bugs in the Claude Code platform itself (report to [Anthropic](https://github.com/anthropics/claude-code/issues))
- Issues with third-party MCP servers (Semantic Scholar, PubMed)
- Denial of service via expensive `/discover` sessions (expected usage)

## Supported Versions

Only the latest version on the `main` branch is supported.
