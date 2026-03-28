# Contributing to MAGELLAN

MAGELLAN is an open-source scientific discovery engine. There are two ways
to contribute: **running discoveries** and **improving the code**.

## Contributing Discoveries

### 1. Install and Run

Clone the repository and run your first discovery session:

```bash
git clone https://github.com/kakashi-ventures/magellan-cli.git
cd magellan-cli
npm install
claude   # launch Claude Code in the project
```

Then in Claude Code:

```
/discover
```

The Scout autonomously identifies where undiscovered scientific connections
might be hiding and runs the full 15-agent pipeline.

### 2. Connect Your Profile

Link your CLI to the MAGELLAN website so discoveries are attributed to you:

1. Create an account at [magellan-discover.ai/sign-in](https://magellan-discover.ai/sign-in)
2. Go to your profile and generate a **Contributor Key**
3. In Claude Code: `/connect mgln_your_key_here`
4. All subsequent sessions are automatically published with your attribution

Without a contributor connection, discoveries are published as "Anonymous"
under CC0 (public domain).

### 3. Leaderboard Ranks

Your rank on the leaderboard reflects your discovery contributions:

| Rank | Requirement |
|------|-------------|
| Cabin Boy | First published session |
| Navigator | 5+ sessions with PASS or CONDITIONAL_PASS hypotheses |
| Cartographer | 15+ sessions, at least 3 different field pairs |
| Captain | 30+ sessions, cross-model validated discoveries |
| Admiral | 50+ sessions, community-recognized contributions |

### 4. Discovery Modes

| Mode | Command | License |
|------|---------|---------|
| Fully autonomous | `/discover` | CC0 1.0 (public domain) |
| Targeted fields | `/discover [A] x [B]` | CC-BY 4.0 |
| Open topic | `/discover [topic]` | CC-BY 4.0 |
| Problem-driven | `/discover solve: [problem]` | CC-BY 4.0 |
| With domain context | `/discover --context "..."` | CC-BY 4.0 |
| With seed papers | `/discover --papers DOI1,DOI2` | CC-BY 4.0 |
| Interactive | `/discover --interactive` | CC-BY 4.0 |

See [DISCOVERY_LICENSE.md](DISCOVERY_LICENSE.md) for full licensing details.

## Contributing Code

### Getting Started

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes
4. Test by running a discovery session
5. Submit a pull request

### What to Contribute

- **Agent improvements**: Better prompts, new strategies, quality refinements
- **New retrieval tools**: Additional MCP integrations, databases, APIs
- **Meta-learning**: Better session analysis, strategy optimization
- **Bug fixes**: Pipeline reliability, state management, edge cases
- **Documentation**: Methodology docs, tutorials, examples

### Code Guidelines

- Follow existing patterns in `.claude/agents/` for agent definitions
- Update all four documentation files when modifying the pipeline:
  - `CLAUDE.md` — Architecture table, design principles
  - `README.md` — Architecture, phase list, project structure
  - `docs/methodology-v5.md` — Full methodology
  - `docs/CHANGELOG.md` — Version history
- Keep pipeline commits separate from session result commits
- Test changes by running at least one full `/discover` session

### Contributor License Agreement

By submitting a pull request, you agree that your code contributions are
licensed under the [Apache License 2.0](LICENSE), consistent with the
project's license.

By running `/discover` and uploading results (via `/connect`), you agree to
the output licensing terms described in [DISCOVERY_LICENSE.md](DISCOVERY_LICENSE.md).

## Questions

- Open an issue on [GitHub](https://github.com/kakashi-ventures/magellan-cli/issues)
- Contact: alberto@kakashi.ventures
