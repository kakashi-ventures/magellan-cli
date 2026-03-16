---
description: "Run another evolutionary cycle on current hypotheses."
allowed-tools: Agent, Read, Write, Glob
---

# Evolve Current Hypotheses

Read state/session.json to get current hypotheses.
Feed them to sde-evolver for another round of recombination.
Then pass evolved versions through sde-critic and sde-ranker.
Save improved versions with incremented version suffix.
After evolution, present a diff summary: what changed and why.
