---
description: "Run another evolutionary cycle on current hypotheses."
allowed-tools: Agent, Read, Write, Glob
---

# Evolve Current Hypotheses

Read state/session.json to get current hypotheses.
Feed them to evolver for another round of recombination.
Then pass evolved versions through critic and ranker.
Save improved versions with incremented version suffix.
After evolution, present a diff summary: what changed and why.
