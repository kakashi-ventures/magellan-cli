# MAGELLAN — Changelog

Storia evolutiva del pipeline. Per la metodologia corrente, vedi `methodology-v5.md`.
Per la reference operativa, vedi `CLAUDE.md`.

---

## v5.13 — Empirical Validation Layer + Holdout Framework (25 marzo 2026)

**Motivazione**: MAGELLAN genera ipotesi scientificamente plausibili (13 sessioni, ~189 ipotesi), ma la validazione si limita a reasoning-based checks (Critic, Quality Gate, Cross-Model). Manca evidenza empirica da dati reali e non c'è un framework formale per dimostrare che il sistema funziona.

Due obiettivi distinti: (1) arricchire la pipeline produzione con evidenza computazionale da database bioinformatici e segnali di convergenza indipendente, (2) creare un framework separato per validazione formale via holdout test (rediscovery di scoperte note post-cutoff).

### Overlap Analysis (design decision critica)
Quality Gate e Critic già cercano sul web senza filtro temporale. La "retrodiction pura" (cercare paper post-cutoff che confermano ipotesi) soffre del "paradosso della retrodiction": se un paper conferma il meccanismo, il QG lo troverebbe e killerebbe l'ipotesi come "not novel". Soluzione: separare validazione formale (Track 2, holdout) dalla pipeline produzione (Track 1, convergence + dataset evidence).

### Track 1: Production Pipeline — 2 nuovi agenti post-Quality-Gate

**Convergence Scanner** (Sonnet/high):
- Cerca segnali di convergenza su fonti MAI consultate dalla pipeline: ClinicalTrials.gov, NIH Reporter, brevetti
- Trova conferme parziali di sub-meccanismi usando query DIVERSE dal Quality Gate
- CONSTRAINT: legge `quality-gate.md` per evitare contare paper già trovati come "nuova evidenza"
- Output: `convergence.json` + `convergence-report.md`

**Dataset Evidence Miner** (Sonnet/high):
- Query su 5+ API bioinformatiche mai usate dalla pipeline: Human Protein Atlas (espressione tissutale), GWAS Catalog (associazioni genetiche), ChEMBL (compound-target), UniProt (funzione proteine), PDB/AlphaFold (struttura)
- DISTINCTION dal Computational Validator: CV opera su bridge concepts PRE-generazione; DEM opera su claim specifici POST-generazione
- Script `scripts/query-biodata.py` (stdlib Python, 7 API handlers, timeout + retry)
- CONSTRAINT: legge `computational-validation.md` per non ri-queryare STRING/KEGG sugli stessi bridge concepts
- Output: `dataset-evidence.json` + `dataset-evidence-report.md`

**Empirical Evidence Score (EES)**: Score parallelo al composite (non lo sostituisce). `dataset_weight=0.55, convergence_weight=0.45`. Riportato in ingest.json e session summary.

### Track 2: Holdout Validation Framework

**Principio**: Prendi una scoperta post-Maggio 2025. Dai a MAGELLAN `[Field A] × [Field C]`. Pipeline gira normalmente (nessun handicap). Poi confronti con contamination check post-hoc.

**Holdout Evaluator** (Opus/max):
- Contamination check: cerca DOI/PMID/titolo del paper holdout in TUTTI i file della sessione
- Se NON trovato e l'ipotesi matcha → GENUINE_REDISCOVERY (prova fortissima)
- Se trovato → CONTAMINATED (non conclusivo)
- Verdicts: GENUINE_REDISCOVERY, PARTIAL_REDISCOVERY, ADJACENT_DISCOVERY, CONTAMINATED, MISSED

**Comando `/validate-holdout`**: esegue il test. `--curate` per aggiungere holdout, `--report` per aggregati.

**Database iniziale**: 3 scoperte curate (vaccinologia×immuno-oncologia, gut microbiome×neuroscienza, mechanobiologia×epigenomica).

### Files aggiunti
- `.claude/agents/convergence-scanner.md`
- `.claude/agents/dataset-evidence-miner.md`
- `.claude/agents/holdout-evaluator.md`
- `.claude/commands/validate-holdout.md`
- `scripts/query-biodata.py` (7 API handlers)
- `scripts/convergence-scanner-stop-gate.py`
- `scripts/dataset-evidence-miner-stop-gate.py`
- `scripts/holdout-evaluator-stop-gate.py`
- `validation/holdout-discoveries.json`

### Files modificati
- `.claude/agents/discovery-orchestrator.md` — 2 dispatch blocks post-QG
- `.claude/settings.json` — 3 SubagentStop hooks
- `prompts/ingest-schema.json` — campo `empirical_validation`
- `scripts/upload-session.mjs` — lettura convergence.json + dataset-evidence.json
- `CLAUDE.md` — architettura (12→15 agenti), design principles, comando
- `README.md` — architettura (15 agenti), pipeline flow, commands table
- `docs/methodology-v5.md` — sezione "Validazione empirica", tabella agenti (15), overlap analysis
- `docs/CHANGELOG.md` — questa entry

---

## v5.12 — Cross-Model Validation Tool Upgrade (24 marzo 2026)

**Motivazione**: Il Cross-Model Validator chiamava GPT-5.4 Pro e Gemini 3.1 Pro senza alcun tool API abilitato. GPT non poteva cercare letteratura recente (il reasoning summary diceva esplicitamente "my knowledge cuts off at June 2024") e non poteva verificare aritmetica computazionalmente. Gemini non poteva eseguire codice per verificare i mapping matematici che descriveva.

Evidenza dalla sessione 2026-03-24: GPT ha trovato un errore aritmetico di quattro ordini di grandezza ((50/3)^3 × (0.1)^-2 ≈ 4.6×10^5, non 200-500 come dichiarato) usando calcolo mentale. Con code interpreter, questa verifica sarebbe immediata e meno soggetta a errore per calcoli più sottili.

### Tool aggiunti

**GPT-5.4 Pro** (OpenAI Responses API):
- `web_search_preview` (search_context_size: `"high"`) — Ricerca letteratura in tempo reale. Novelty verdicts ora basati su letteratura corrente, non solo conoscenza parametrica pre-giugno 2024
- `code_interpreter` (container: `auto`) — Verifica aritmetica, power analysis, calcoli di ordine di grandezza. $0.03/container

**Gemini 3.1 Pro** (Google GenAI SDK):
- `codeExecution` — Verifica computazionale dei mapping formali (algebra simbolica, analisi dimensionale, predizioni numeriche)
- `googleSearch` — Grounding claims in letteratura via Google Search

### Modifiche allo script (`scripts/validate-crossmodel.mjs`)
- Tool params aggiunti a entrambe le chiamate API
- Gestione nuovi event types nello streaming (web_search_call.*, code_interpreter_call.*, executableCode, codeExecutionResult)
- Estrazione grounding metadata (Gemini) e annotazioni arricchite (GPT)
- Output file include sezioni Code Execution Outputs / Computational Verification / Grounding Sources
- Return JSON include tool usage stats (web_searches, code_executions, grounding_sources)

### Aggiornamenti prompt
- `prompts/gpt-validation.md` — Istruzioni esplicite per usare web search e code execution
- `prompts/gemini-deep-think.md` — Istruzioni per verifica computazionale dei mapping e sezione COMPUTATIONAL CHECK nell'output format

### Costo stimato incrementale
- Web search (GPT): ~$0.01-0.05 per sessione (search_context_size: high)
- Code interpreter (GPT): $0.03 per container per sessione
- Code execution (Gemini): incluso nel costo API Gemini
- Google Search grounding (Gemini): billed per query, tipicamente < $0.01 per sessione
- Totale: ~$0.05-0.10 per sessione, trascurabile per un pipeline che gira ~1x/giorno

---

## v5.11 — Orchestrator Turn Budget & State Robustness (24 marzo 2026)

**Motivazione**: Sessione 013 (cryo-EM × OMV cargo sorting) ha rivelato che l'orchestratore esauriva i turni dopo il ranking di Cycle 2. Con maxTurns=80 e 89 tool_uses consumate, le fasi finali (Quality Gate, Cross-Model Validation, Session Analysis, Summary) dovevano essere dispatched manualmente. Root cause: una pipeline completa a 2 cicli richiede ~100-110 tool calls.

### Fix critici
- **maxTurns rimosso da tutti i sub-agent** — I sub-agent (scout, generator, critic, ranker, etc.) non hanno più limite di turni. La qualità dell'output è validata dagli stop hooks, non dal conteggio turni. Un maxTurns troppo basso causa troncamento silenzioso — peggio che nessun limite.
- **Orchestratore: maxTurns 80 → 200** — Puro circuit breaker anti-loop infinito. Non è il meccanismo di controllo qualità (quello è lo stop gate). 200 turni sono ~2x il massimo osservato in 13 sessioni.

- **Context Efficiency Protocol** — Nuove linee guida per l'orchestratore: batch state updates, non ri-leggere file appena scritti, dispatch prompt lean, combinare date+state in un turno. Obiettivo: ridurre tool_uses per fase da ~5 a ~3.

- **State Contract esplicito** — Valori terminali esatti documentati nel prompt dell'orchestratore:
  - `status`: DEVE essere `"success"` / `"partial"` / `"degraded"` / `"failed"`
  - `phase`: DEVE essere `"complete"` (stringa) a fine pipeline
  - `progress.phases_completed`: DEVE includere TUTTE le fasi eseguite
  - Lo stop hook valida questi valori — nessuna variazione tollerata

- **Early-complete branching esplicito** — Aggiunto flow control chiaro: se `cycle_decision == "early_complete"`, SKIP Phase 5 (Evolve) E Cycle 2 interamente, vai diretto a Quality Gate.

### Fix nello stop hook (orchestrator-stop-gate.py)
- **JSON format handling** — I file `cycle{N}-raw.json` e `cycle{N}-critiqued.json` usano formato `{hypotheses: [...]}`, non array bare. Lo hook ora gestisce entrambi i formati.
- **Dispatch log format** — `state/dispatch-log.json` è un array bare, non `{dispatches: [...]}`. Lo hook ora gestisce entrambi.

### Fix nel init script
- **phase iniziale** — Cambiato da `0` (numerico) a `"init"` (stringa) per coerenza con il contratto di stato.

**Evidenza**: Sessione 013 è la migliore singola sessione (3 PASS, avg 8.31, 0 claim fabricati) ma ha richiesto intervento manuale per le fasi finali. Con maxTurns=120 e il protocollo di efficienza, le future sessioni dovrebbero completare autonomamente.

---

## v5.10 — Orchestrator Context Optimization (24 marzo 2026)

**Motivazione**: L'orchestratore (discovery-orchestrator.md) era 39.4 KB / ~11,300 token — il file agent più grande per un fattore 3x. Con 2 skill caricate al startup (+1,900 token) e CLAUDE.md (+3,400 token), il contesto iniziale era ~16,600 token prima di qualsiasi lavoro effettivo. Per un pipeline di 50-80 minuti con maxTurns=80, lo spazio di contesto si riempiva progressivamente, degradando le prestazioni nelle fasi finali.

Seguendo le best practice di Claude Code di marzo 2026 ("Context window is the most important resource to manage", "dispatch prompts should be focused — sub-agents have their own detailed instructions"):

### Estrazioni a file esterni (read on-demand)
- `scripts/init-session.sh` — Script bash di inizializzazione sessione (da 48 righe inline)
- `scripts/upload-session.mjs` — Script Node.js di upload al website (da 87 righe inline)
- `prompts/session-summary-format.md` — Istruzioni formattazione session summary (da 49 righe)
- `prompts/ingest-schema.json` — Schema del manifest ingest (da 38 righe)
- `prompts/knowledge-schema.json` — Schema del discovery-log entry (da 55 righe)

### Rimozione skill non utilizzate dal frontmatter
- `discovery-engine` e `hypothesis-validation` rimosse dal frontmatter dell'orchestratore
- L'orchestratore non genera mai ipotesi, non valida claim — queste skill sono usate solo dai sub-agent che le caricano autonomamente

### Consolidamento e deduplica
- Guard Protocol generico aggiunto (pattern comune per tutti i post-dispatch guard)
- State Update Protocol unificato (7 ripetizioni di timestamp update rimosse)
- Dispatch prompt accorciati a soli dati di contesto (i sub-agent hanno istruzioni proprie)
- Sezione Targeted/Open/Problem mode condensata da 20 a 4 righe

### Risultato
- Orchestratore: 39,450 → 23,959 byte (-39%), 918 → 491 righe (-46%)
- Contesto startup stimato: ~16,600 → ~11,200 token (-32%)
- Nessun cambio funzionale al pipeline

---

## v5.9 — Pinned Agent Effort Levels (24 marzo 2026)

**Motivazione**: I livelli di effort degli agenti ereditavano il setting di sessione dell'utente. Un utente con effort `low` o `medium` nella propria CLI rischiava di degradare la qualità delle ipotesi generate dal pipeline. La priorità è la qualità, non il costo o i tempi.

### Effort esplicito per tutti i 12 agenti
- **Opus agents** (Scout, Target Evaluator, Generator, Critic, Quality Gate, Orchestrator) → `effort: max`
- **Sonnet agents** (Literature Scout, Computational Validator, Ranker, Evolver, Session Analyst, Cross-Model Validator) → `effort: high`

Il campo `effort` nel frontmatter YAML degli agenti sovrascrive il livello di sessione, garantendo qualità costante indipendentemente dalla configurazione dell'utente.

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
