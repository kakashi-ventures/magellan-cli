# MAGELLAN — Changelog

Storia evolutiva del pipeline. Per la metodologia corrente, vedi `methodology-v5.md`.
Per la reference operativa, vedi `CLAUDE.md`.

---

## v5.8 — Creativity-First Ideation (22 marzo 2026)

**Motivazione**: L'analisi di 9 sessioni ha rivelato che il pipeline convergeva naturalmente verso strategie "safe" (network_gap_analysis al 39% QG pass rate, 3 sessioni primarie) mentre 5 delle 8 strategie più creative non avevano mai dati primari. Inoltre, le connessioni più potenti (isomorfismi strutturali, bisociazioni) non erano esplicitamente elicitate dal prompting. La fase di ideazione (Scout + Generator) necessitava di meccanismi per facilitare connessioni creative, non solo per filtrare quelle deboli.

### Scout: 10 strategie (da 8)
- **Strategia 9: Structural Isomorphism Discovery** — Cerca campi che condividono la stessa struttura formale (equazioni, topologia, vincoli information-theoretic) con substrati fisici completamente diversi. Il bridge è l'oggetto matematico stesso. Domain-agnostic.
- **Strategia 10: Serendipity Through Random Encounter** — Esposizione a conoscenza inattesa: dominio mai esplorato → scoperta più sorprendente → "quale campo distante sarebbe più trasformato?". Mima la serendipità di sfogliare una biblioteca fisica.

### Scout: Exploration slot obbligatorio
- Almeno 1 dei 3 target DEVE usare una strategia con < 2 sessioni di dati primari. Previene la convergenza verso strategie ad alto QG pass rate a scapito della creatività.

### Orchestratore: Rotating creativity constraint
- Vincolo creativo diverso ad ogni sessione (mod 5): ponte cross-disciplina, ponte matematico/formale, gap temporale, tool transfer, unsolved problem. Forza esplorazione di territori che lo Scout altrimenti eviterebbe.

### Orchestratore: Hard constraint disjointness
- Se esistono target DISJOINT con score >= 5, l'orchestratore NON seleziona mai PARTIALLY_EXPLORED. Basato su 9 sessioni: DISJOINT 84% pass+cond rate vs PARTIALLY_EXPLORED 30%.

### Generator: Bisociazione + Multi-Level Abstraction
- **Bisociazione (Koestler)**: Tecnica di generazione basata su CONCETTI astratti (non molecole) con clash tra vocabolari di domini incompatibili.
- **Multi-Level Abstraction**: Almeno 2 delle 6-8 ipotesi devono articolare il bridge a livelli multipli (molecolare + sistemico + formale/matematico + informazionale).

### Sequential Narrowing (Phase 0 ristrutturata)
- **Scout genera 5-6 candidati** (non più 3) — pool più ampio per permettere filtraggio
- **Literature Scout verifica disjointness per TUTTI i candidati** — non più broad scan parallelo, ma verifica target-specific sequenziale dopo lo Scout
- **Orchestrator narrow da 5-6 a 3** — filtra per disjointness (WELL_EXPLORED esclusi, DISJOINT preferiti), bridge validation, e strategy diversity
- **Target Evaluator riceve i 3 migliori** — già pre-filtrati per disjointness
- Questo elimina il problema S009: la disjointness è verificata PRIMA della selezione, non dopo

### Ranker: Cross-Domain Creativity Bonus
- +0.5 al composite score per ipotesi che attraversano 2+ confini disciplinari (es. materials science → neuroscience). Compensa la penalizzazione sistematica dell'infrastruttura bio-centrica (PubMed/KEGG/STRING) su ipotesi non-biomediche.

### Session Analyst: Creativity Metrics
- Tre nuove metriche per-ipotesi: **Disciplinary Distance** (0-3), **Abstraction Level** (1-3), **Novelty Type** (1-4).
- Tracking cross-sessione: se la creatività è in calo, il Session Analyst lo segnala esplicitamente con azioni correttive.
- Sezione "Creativity Metrics" aggiunta sia al meta-insights cumulativo che all'analisi per-sessione.

### Literature Scout: Domain-Agnostic Retrieval
- Sorgenti di retrieval domain-aware: arXiv per fisica/math, SSRN per social sciences, patent DB per engineering — non più solo PubMed/Semantic Scholar
- Per target cross-domain, usa sorgenti da ENTRAMBI i domini

### Documentazione
- CLAUDE.md, README.md, methodology-v5.md, CHANGELOG.md aggiornati.

---

## v5.7 — Unified Results Directory (22 marzo 2026)

**Motivazione**: `state/phases/{session-id}/` duplicava la struttura directory di `results/{session-id}/` — stessi dati, stessa sessione, due posti diversi. Il directory `state/` conteneva sia l'indice di coordinamento (session.json) sia dati per-sessione (phases/), creando confusione su dove vivono i dati. Semplificazione: tutto il contenuto per-sessione (markdown + JSON) vive in `results/{session-id}/`.

### Refactor: Elimina state/phases/
- **`state/phases/` eliminata** — Directory rimossa completamente
- **File JSON migrati in `results/{session-id}/`** — Phase JSON files (scout.json, cycle{N}-raw.json, final.json, etc.) vivono accanto ai file markdown nella stessa directory
- **`state/` contiene solo coordinamento** — session.json (indice slim ~3KB) + dispatch-log.json. Nessun dato per-sessione
- **Orchestratore aggiornato** — Tutti i path phase file usano `{results_dir}/` (già definito come `results/{SESSION_ID}`)
- **Stop gate aggiornato** — `orchestrator-stop-gate.py` legge da `results/{session_id}/` con fallback legacy
- **Cross-model validator aggiornato** — Legge `{results_dir}/final.json` e scrive `{results_dir}/cross-model.json`
- **Export command aggiornato** — Legge `{results_dir}/final.json`
- **CLAUDE.md, README.md, methodology-v5.md aggiornati** — Documentazione allineata

### Convenzione di naming
`results/{session-id}/{fase}.json` dove fase è: `scout`, `literature`, `computational`, `cycle{N}-raw`, `cycle{N}-critiqued`, `cycle{N}-ranked`, `cycle{N}-evolved`, `quality-gate`, `final`, `meta-insights`, `cross-model`

### Struttura risultante
```
state/
  session.json          ← Indice di coordinamento slim (~3KB)
  dispatch-log.json     ← Log dei dispatch con timestamp
results/{session-id}/
  *.md                  ← Output leggibili (ipotesi, report, riassunti)
  *.json                ← Dati strutturati per-fase (scout, cycle, quality-gate, etc.)
  papers/               ← Paper full-text
```

---

## v5.6.2 — Session-Scoped Phase Files (22 marzo 2026)

**Nota**: Superseded da v5.7 — `state/phases/` non esiste più. I file phase vivono in `results/{session-id}/`.

**Motivazione originale**: `state/phases/` era una directory piatta dove file di sessioni diverse si mischiavano. Questa versione aveva introdotto `state/phases/{session-id}/` come sub-directory per sessione. v5.7 elimina completamente `state/phases/` in favore di `results/{session-id}/`.

---

## v5.6.1 — Slim State Architecture (19 marzo 2026)

**Nota**: L'architettura slim index rimane in v5.7. La differenza: i file per-fase ora vivono in `results/{session-id}/` invece di `state/phases/{session-id}/`.

**Motivazione**: `state/session.json` cresceva proporzionalmente alla complessità delle sessioni (28KB+ con 71% occupato dai dati delle ipotesi). Ogni agente consumava contesto leggendo dati che non gli servivano.

### Refactor: Slim Index + Phase Files
- **`state/session.json`** diventa un indice di coordinamento slim (~3KB): fase, ciclo, status, selected_target, health counters, progress. MAI contenuto delle ipotesi
- **`results/{session-id}/*.json`** — File per-fase con dati strutturati leggeri (IDs, titoli, scores, verdicts), isolati per sessione
- **`results/{session-id}/*.md`** — Testo completo delle ipotesi (meccanismi, evidenze, etc.) vive SOLO qui
- **Orchestratore aggiornato** — Legge phase files specifici per ogni dispatch, non l'intero stato
- **Stop gate aggiornato** — `orchestrator-stop-gate.py` legge da phase files con fallback legacy
- **Export command aggiornato** — Legge `results/{session-id}/final.json` con fallback a session.json
- **Cross-model validator aggiornato** — Legge `results/{session-id}/final.json`

---

## v5.6 — Cross-Model Validation automatica (19 marzo 2026)

**Motivazione**: Rendere la pipeline completamente autonoma end-to-end, inclusa la validazione indipendente delle ipotesi da parte di modelli concorrenti. Fino a v5.5, l'utente doveva manualmente copiare i prompt di export in ChatGPT/Gemini. Ora il pipeline chiama direttamente le API.

### Nuovi componenti
- **Cross-Model Validator** [Sonnet] — Nuovo agente che genera prompt di validazione, chiama le API OpenAI (GPT-5.4 Pro con reasoning high) e Google Gemini (3.1 Pro con thinking HIGH) in parallelo, e produce un report di consenso
- **scripts/validate-crossmodel.mjs** — Script Node.js che esegue le chiamate API in parallelo (OpenAI Responses API + Google GenAI SDK)
- **cross-model-validator-stop-gate.py** — Hook warn-only che verifica la produzione degli output
- **package.json** — Dipendenze: `openai` v5+, `@google/genai` v1.45+

### Flusso pipeline aggiornato
- Dopo Session Analyst → Cross-Model Validator (Phase 7)
- Se `OPENAI_API_KEY` e/o `GEMINI_API_KEY` sono configurate: validazione API automatica → consensus report
- Se nessuna API key: genera solo i file di export (fallback al workflow manuale)
- **Non-blocking**: fallimenti nella validazione cross-model non cambiano lo status della sessione

### Modelli utilizzati
- **OpenAI**: `gpt-5.4-pro` via Responses API con `reasoning.effort: "high"` — validazione empirica (novelty, citations, mechanism plausibility, counter-evidence, experimental design)
- **Google**: `gemini-3.1-pro` via `@google/genai` con `thinkingLevel: HIGH` + `includeThoughts: true` — analisi strutturale (mappature formali, isomorfismi, predizioni quantitative)

### Output
- `{results_dir}/export-gpt.md` — Prompt di validazione GPT (sempre generato)
- `{results_dir}/export-gemini.md` — Prompt di validazione Gemini (sempre generato)
- `{results_dir}/validation-gpt.md` — Risposta GPT-5.4 Pro (se API key presente)
- `{results_dir}/validation-gemini.md` — Risposta Gemini 3.1 Pro (se API key presente)
- `{results_dir}/cross-model-consensus.md` — Report di consenso con analisi agreement/divergence

### State
- Nuovo campo `cross_model_validation` in session.json: status, models_used, consensus per ipotesi

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
