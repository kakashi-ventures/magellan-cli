# MAGELLAN — Changelog

Storia evolutiva del pipeline. Per la metodologia corrente, vedi `methodology-v5.md`.
Per la reference operativa, vedi `CLAUDE.md`.

---

## v5.5 — Meta-learning e validazione computazionale (19 marzo 2026)

**Motivazione**: Confronto critico con Aletheia (Gemini Deep Think, DeepMind) e Google AI Co-Scientist. Analisi dei gap emersi dalle sessioni 1-3.

### Gap identificati
1. Sessioni sprecate su target deboli (Scout opera in isolamento)
2. 43% delle ipotesi uccise per ragioni quantitative verificabili programmaticamente
3. Nessun apprendimento strutturato tra sessioni (lessons_learned in prosa, non metriche)
4. Path-lock strategico (strategie simili dominano ogni sessione)

### Ispirazione da sistemi comparabili
- **Aletheia**: "balanced prompting" (prova O refutazione) → principio del Target Evaluator
- **Google AI Co-Scientist**: Elo tournament ranking → sanity check nel Ranker
- **Entrambi**: validazione computazionale (code-assisted verification) → Computational Validator

### Modifiche
- **3 nuovi agenti**: Target Evaluator [Opus], Computational Validator [Sonnet+Bash], Session Analyst [Sonnet]
- **3 nuovi hooks**: target-evaluator-stop-gate.py (blocking), computational-validator-stop-gate.py (warn-only), session-analyst-stop-gate.py (warn-only)
- **Scout**: Strategy diversification constraint (almeno 2 strategie diverse, almeno 1 non usata nelle ultime 2 sessioni). Legge `knowledge/meta-insights.md`. Campo `strategy` obbligatorio in scout_targets
- **Ranker**: Elo tournament sanity check (15 confronti pairwise per top-6). maxTurns 10→15
- **Orchestrator**: 3 nuovi dispatch points (Phase 0c, 1b, post-QG). Computational validation context nel Generator dispatch. Meta-learning metrics nel discovery-log
- **orchestrator-stop-gate.py**: Required agents condizionali su mode (scout+target-evaluator solo in scout mode)
- **Nuovi campi state**: target_quality_scores, computational_readiness, session_meta_insights, strategy_performance
- **Nuovo file persistente**: `knowledge/meta-insights.md` (scritto dal Session Analyst, letto da Scout e Generator)
- **Pipeline**: da 8 a 11 agenti. Runtime stimato +5-10 min

---

## v5.4 — Verifica claim-level (17 marzo 2026)

**Motivazione**: Post-mortem delle 7 ipotesi delle sessioni 1-2 rivela il failure mode più critico: claim meccanistici fabbricati che passano come [GROUNDED].

### Evidenze dal post-mortem

| Sessione | Ipotesi | Claim fabbricato | Tipo di errore |
|---|---|---|---|
| S1 | FINAL-1 | "Bhatt et al., Cell 2024" | Citation hallucination (paper è Dai et al.) |
| S1 | FINAL-2 | "CaMKII fosforila FUS" | Kinase-substrate relationship inesistente |
| S1 | FINAL-3 | "V-ATPase acidifica citoplasma" | Errore compartimentale (acidifica lumen) |
| S2 | E2 | "R-spondin è GPI-ancorata" | Protein property fabbricata (è secreta) |

### Fix a tre livelli
1. **Generator SELF-CRITIQUE**: 5 nuovi check (citation specificity, directionality, compartmental, quantitative sanity, protein property). Ogni [GROUNDED] deve avere author+year+journal
2. **Critic attack vector 9**: "Claim-Level Fact Verification" — web search ogni [GROUNDED] individualmente. Hallucination = KILL automatico
3. **Quality Gate rubric point 10**: "Per-Claim Grounding Verification" — maxTurns 25→35. Automatic FAIL per citation hallucination, fabricated protein property, inverted directionality, compartmental error

### Impatto stimato
4/7 errori catturati a livello Generator; i restanti 3 da Critic o Quality Gate.

### Altre modifiche
- Life sciences riconosciuto esplicitamente come dominio primario (3 bias strutturali: retrieval, scoring, format)

---

## v5.3 — Fix operativi (17 marzo 2026)

**Motivazione**: Analisi post-sessione della seconda esecuzione (2026-03-17-scout-002).

### Fix
1. **Hook schema compliance**: `"allow"` → `"approve"/"block"` (schema Claude Code)
2. **verify-dispatch.py**: `os.environ["CLAUDE_TOOL_INPUT"]` → stdin (protocollo PostToolUse)
3. **critic-stop-hook.py**: `h.get("status") == "killed"` → `h.get("verdict", "").upper() == "KILLED"`
4. **literature-scout-stop-gate.py**: non blocca più se MCP/web non disponibili; degrada a warning
5. **Session-scoped results**: `results/{session-id}/` per evitare conflitti
6. **Orchestrator maxTurns**: 50 → 80 (sessione 2 esauriva turni prima del Quality Gate)
7. **Plan mode auto-exit**: `/discover` chiama ExitPlanMode automaticamente
8. **Groundedness standardization**: integer 1-10 in JSON (non stringhe "MEDIUM")
9. **Cycle decision labeling**: chiarito che "early_complete" = skip ciclo 2

---

## v5.2 — Prompt engineering alignment (16 marzo 2026)

**Motivazione**: Allineamento ai best practice 2026 per modelli frontier.

### Modifiche
- XML tags per separazione semantica (`<goal>`, `<constraints>`, `<strategies>`, `<reflection>`)
- Role sentences all'inizio di ogni agent prompt
- WHY explanations su ogni constraint
- Riduzione linguaggio enfatico (MUST/CRITICAL) per Opus 4.6 adaptive thinking
- Data-top/task-bottom nei dispatch dell'Orchestratore
- Few-shot examples: Generator (2), Critic (1), Ranker (1), Evolver (1)
- Nuove reflection loops: RETRIEVAL QUALITY CHECK (Literature Scout), EVOLUTION QUALITY CHECK (Evolver)
- Sonnet-specific scaffolding (step sequence esplicita)
- Model-specific export prompts: GPT-5.4 (output contracts), Gemini 3.1 (context-first + strict grounding)

---

## v5.1 — Architettura scalabile (15 marzo 2026)

**Motivazione**: Rendere l'architettura scalabile a modelli futuri più capaci.

### Modifiche
- **GOAL/CONSTRAINTS/STRATEGIES prompt structure**: goal + hard constraints + advisory strategies. Scala con modelli più capaci che trovano percorsi migliori
- **Reflection loops**: SELF-CRITIQUE (Generator), META-CRITIQUE (Critic), TARGET QUALITY CHECK (Scout), META-VALIDATION (Quality Gate)
- **Adaptive cycles**: early-complete (top-3 ≥ 7.0), extended (survival < 30%), standard. Skip Evolver se ciclo 2 top-3 ≥ 6.5
- **Bidirectional feedback**: Critic → critic_questions → state → Orchestrator → Generator ciclo 2

---

## v5.0 — Architettura fondazionale (14 marzo 2026)

### Architettura iniziale
- 8 agenti specializzati (Scout, Literature Scout, Generator, Critic, Ranker, Evolver, Quality Gate, Orchestrator)
- Mandatory agent dispatch (Orchestrator senza WebSearch/WebFetch)
- MCP-first literature retrieval (Semantic Scholar, PubMed)
- Quality Gate come agente Opus dedicato
- Structured state in `state/session.json`
- Groundedness scoring al 20% del peso
- Diversity constraint nel Ranker e nell'Evolver
- SubagentStop blocking hooks
- Agent Teams per Phase 0 (Scout + Literature Scout in parallelo)
- Dispatch log con verify-dispatch.py
- Timestamp protocol (sempre via `date -u`, mai da memoria)
- Kill rate formula esatta con validazione nell'orchestrator-stop-gate
