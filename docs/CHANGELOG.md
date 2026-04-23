# MAGELLAN — Changelog

Storia evolutiva del pipeline. Per la metodologia corrente, vedi `methodology-v5.md`.
Per la reference operativa, vedi `CLAUDE.md`.

---

## v5.24 — Gemini Deep Research Max migration (23 aprile 2026)

**Motivazione**: Il 21 aprile 2026 Google ha rilasciato Deep Research e Deep Research Max, agent autonomi di ricerca esposti sulla nuova Interactions API del Gemini. Sono workflow agentici (plan → search → read → code → synthesize), non generazioni single-shot. MAGELLAN usava Gemini 3.1 Pro come validatore one-shot tramite `generateContentStream` (~90-150s per chiamata), ottenendo thinking + risposta + code execution inline + grounding sources. Il nuovo agente Max esegue ~80-160 web search + URL context reads + code execution iterativamente, dura 10-30 min tipici (fino a 60 min), e restituisce un report completamente citato. Per il Cross-Model Validator di MAGELLAN questo e' un upgrade sostanziale: ogni ipotesi survived riceve un check strutturale piu' profondo, con review della letteratura e verifiche quantitative code-eseguite piu' estese.

**Decisioni**:
1. **`scripts/validate-crossmodel.mjs::callGemini` riscritta** sulla Interactions API del SDK `@google/genai` (v1.46 gia' esposta come `client.interactions.create` / `.get`). Streaming con reconnection (pattern documentato: il connection timeout e' ~10 min, il SDK permette resume via `last_event_id`). Agent pinned a `deep-research-max-preview-04-2026`. Tools impliciti dal default del tipo agent deep-research: `google_search`, `url_context`, `code_execution`. `background: true`, `stream: true`, `agent_config.type: 'deep-research'`, `thinking_summaries: 'auto'`, `visualization: 'auto'`, `collaborative_planning: false` (vogliamo one-shot autonomous, non plan review cycles). Wall-clock budget: 90 min (margine sui 60 min max documentati). Output markdown strutturato: thinking process, report citato, visualizations (se presenti), citations (dedup per URI).
2. **`prompts/validation-prompt-gemini.md` esteso** con preamble da research agent ("usa tutto il budget: 80-160 search + URL reads + code iterativamente; verifica i DOI; spot-check arithmetic con Python") e nuova sezione obbligatoria **LITERATURE REVIEW** per ipotesi (5-10 paper recenti, ciascuno con DOI, con annotazione supporta/contraddice/adjacent). Le sezioni STRUCTURAL CONNECTION / FORMAL MAPPING / PREDICTION / VERIFICATION APPROACH / COMPUTATIONAL CHECK / CONFIDENCE / DEPTH sono preservate identiche per non rompere il downstream consensus synthesis.
3. **`.claude/agents/cross-model-validator.md` aggiornato**: model name ("Gemini 3.1 Pro" → "Gemini Deep Research Max"), tool description (code execution + Google Search grounding → google_search + url_context + code_execution), aspettativa runtime (10-30 min tipico, fino a 60 min max, script gestisce polling/reconnection internally). `cross-model.json` schema esteso con `gemini_model: 'deep-research-max-preview-04-2026'` e `gemini_tools: ['google_search', 'url_context', 'code_execution']`. Dispatch pattern e consensus logic invariati.
4. **`.claude/commands/export.md` aggiornato**: le user instructions per il file di export Gemini puntano ora a Google AI Studio > Deep Research Max, con link ai docs ufficiali (`ai.google.dev/gemini-api/docs/deep-research`).
5. **Docs sync** (CLAUDE.md architecture table + cross-model validation principle; README.md phase 7 + automatic-fallback + directory layout; methodology-v5.md agent table + ASCII diagram + prompt reference + external models table + reference benchmarks con nuova entry Deep Research Max).

**Design decisions**:
- **SDK, non REST**: i docs ufficiali mostrano esempi Node verbatim con `client.interactions.create` / `.get`. Codice piu' pulito, type-safe, future-proofed. (Prima del user pushback pensavo di usare REST perche' avevo fatto un WebFetch che non aveva mostrato esempi JS; il user ha corretto facendomi rifare il fetch. Lezione annotata.)
- **Max, non standard Deep Research**: user request esplicita "in its full potential". ~4x costo per synthesis piu' profonda e report piu' citato.
- **No MCP passthrough**: MAGELLAN's `.mcp.json` espone PubMed + Semantic Scholar MCP server via `npx` stdio. Deep Research Max accetta solo remote HTTPS MCP endpoints, non stdio. Future work se deployiamo remote MCP servers.
- **Streaming con reconnection, non pure polling**: preserva la UX corrente (progress in stderr), e il pattern di reconnection documentato e' robusto contro il connection timeout di ~10 min.

**File modificati**:
- `scripts/validate-crossmodel.mjs` (callGemini rewrite)
- `prompts/validation-prompt-gemini.md` (research agent preamble + LITERATURE REVIEW required section)
- `.claude/agents/cross-model-validator.md` (model name, runtime, tools, JSON schema)
- `.claude/commands/export.md` (user instructions per export-gemini)
- `CLAUDE.md` (architecture table + cross-model validation principle)
- `README.md` (setup + phase 7 + automatic-fallback + directory layout + architecture list)
- `docs/methodology-v5.md` (ASCII diagram, agent table, pipeline description, prompt reference, external models table, reference benchmarks)
- `docs/CHANGELOG.md` (questa entry)

**Behavior shift**:
- **Runtime phase cross-model**: era GPT-bound a ~45 min (Gemini 3.1 Pro completava in ~2 min). Ora entrambi possono prendere 30-60 min, run in parallelo. Phase totale ~45-60 min (invariato nel peggiore caso).
- **Costo Gemini-side**: da ~$0.50 a ~$4.80 per sessione. Totale cross-model Gemini+GPT ora ~$5-15 per sessione, a seconda del numero di ipotesi e profondita' ricerca.
- **Paid tier required**: Deep Research Max non disponibile sul free tier Gemini API (per i docs). User esistenti con GEMINI_API_KEY su free tier devono fare upgrade a Pro tier.
- **Citazione depth**: DR Max ritorna report "fully cited" con ~20-50 riferimenti a paper per task, vs le ~5-10 grounding sources di 3.1 Pro single-shot. Il Cross-Model Consensus report beneficia: piu' citation checks, piu' cross-paper mapping verifications.

**Preview-stage disclaimer**: `deep-research-max-preview-04-2026` e' un preview agent ID. Google potrebbe revisionare schema di output (delta types, output types, annotations format) prima del GA. Il codice fa defensive field parsing (legge sia `status` sia `state`, sia `id` sia `name`; logga delta/output types sconosciuti a stderr). Quando il GA rilascia un ID stabile, bump in `scripts/validate-crossmodel.mjs::GEMINI_AGENT` e verify con smoke test.

**Non-regressione**: La fallback path (chiavi API assenti → `/export gemini` file generation) e' invariata. `cross-model.json` schema e' backward-compatible (chiavi nuove sono additive: `gemini_agent`, `interaction_id`, `visualizations`; chiavi esistenti come `models_used`, `status`, `files` sono preservate). Il consensus synthesis in `cross-model-validator.md` non richiede modifiche perche' l'output contract di `validation-gemini.md` resta "thinking + report + citations" e il prompt preserva le sezioni STRUCTURAL CONNECTION / FORMAL MAPPING / CONFIDENCE / DEPTH.

**Sources**:
- [Google blog: Deep Research Max](https://blog.google/innovation-and-ai/models-and-research/gemini-models/next-generation-gemini-deep-research/) (2026-04-21 announcement)
- [Gemini Deep Research API docs](https://ai.google.dev/gemini-api/docs/deep-research) (include Node.js SDK examples)
- [Deep Research Max preview model card](https://ai.google.dev/gemini-api/docs/models/deep-research-max-preview-04-2026)

---

## v5.23 — Top-level orchestration + dispatch-log enforcement (18-19 aprile 2026)

**Motivazione**: La sessione 2026-04-18-scout-026 (EVT x MIC distributions) ha rivelato un failure mode critico. `discovery-orchestrator`, dispatchato da `/discover` come sub-agent, ha marcato `phase: complete, status: success` senza mai chiamare il tool `Agent`. Tutti i 14 ruoli pipeline sono stati eseguiti inline usando conoscenza parametrica, producendo 41 file deliverable strutturalmente validi ma scientificamente compromessi. Cross-Model Validator dichiarava "GPT/Gemini APIs not available" quando le API key erano presenti in .env.local e le MCP tool erano registrate. Impatto quantificato: 3 citazioni errate (Jacoby 2005, Carattoli 2009, Drees 1998), 9 errori fattuali (AUC/MIC=271 non 170, rifampicin breakpoint medium-dependent, CRyPTIC 12289 isolati non 15000, rpoB E. coli vs Mtb numbering, FTG formal applicability, EARS-Net data type, FDR omission in H4, PBDH framework naming, core C2-H8 quantization claim refutato da codice Gemini), EES reale 4.9 vs fabbricato 10.0. Il re-run con dispatch reale ha anche trovato 7 paper di partial-mechanism convergence che lo scan fabbricato aveva mancato, incluso Catalan 2022 Nat Commun (PMID 35614098, 6.5M MIC) che valida empiricamente il sub-mechanism di E1-C1-H2.

**Causa radice (corretta il 19 aprile 2026)**: non era un comportamento di Opus 4.7 (la v5.21 aveva ipotizzato "fewer subagents by default" come la causa). La causa vera e' un constraint architetturale del runtime di Claude Code: i sub-agent NON possono dispatchiare altri sub-agent. Il runtime striscia il tool `Agent` da ogni sub-agent indipendentemente da cosa richiede la frontmatter. Il doc ufficiale (code.claude.com/docs/en/sub-agents) conferma: *"This prevents infinite nesting (subagents cannot spawn other subagents)"*. Verificato con un probe diretto il 19 aprile: dispatching general-purpose da top-level e chiedendo la tool list returns: no `Agent` tool present.

Le sessioni S001-S024 (pre-18 aprile 2026) funzionavano perche' Claude Code precedenti permettevano nested dispatch quando la frontmatter whitelisatava `Agent`. Quella capability e' stata rimossa silenziosamente in una release successiva (probabilmente tra 2.1.111 e 2.1.114), e MAGELLAN ha continuato a lanciare l'orchestrator come sub-agent senza accorgersene: il tool `Agent` veniva strippato al runtime, i dispatch fallivano, l'output veniva prodotto inline. Il gap nello stop-gate (warning anziche' block per dispatch mancanti) ha permesso al failure mode di passare i controlli di terminazione.

**Decisioni v5.23 (architetturali, non soft-fix)**:
1. **Orchestrator loaded al top-level da `/discover`**: la command ora istruisce il top-level Claude a leggere `.claude/agents/discovery-orchestrator.md` e seguirne il body come brief di orchestration dal proprio contesto. Il top-level Claude HA `Agent` e puo' dispatchiare i 14 sub-agent della pipeline normalmente. La frontmatter dell'orchestrator e' preservata come reference ma e' inerte nell'architettura attuale (si riattivera' se Claude Code ripristinera' il nested dispatch).
2. **Stop-gate hardened (scripts/orchestrator-stop-gate.py)**: quando `phase` e' complete o status e' terminal, se mancano critical sub-agent (`generator`, `critic`, `quality-gate`) OPPURE il numero totale di pipeline sub-agent dispatch e' zero, il hook emette `decision: block` invece di warning. Enforcement deterministico: impossibile marcare la sessione complete senza dispatch reali loggati in dispatch-log.json.
3. **Orchestrator prompt ripulito**: sezione "Execution context" che spiega il caricamento top-level, DISPATCH_OR_FAIL come role-discipline hard constraint (non piu' come environment capability statement, che nel nuovo modello sarebbe fuorviante — il top-level HA tecnicamente WebSearch/WebFetch, ma non deve usarli per lavoro scientifico).
4. **CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS flag**: declassato da "Required env" a "Optional env". Non serve per MAGELLAN (classic sub-agent dispatch); retained solo per altri workflow in questo repo che usano agent teams. Nessun agent MAGELLAN usa `SendMessage`, `TeamCreate`, o shared task list.
5. **S026 post-hoc recovery**: il 18 aprile ri-dispatchati i 4 post-QG validator (literature-scout, cross-model-validator, convergence-scanner, dataset-evidence-miner) dal top-level dove `Agent` funziona. Aggiornati final-hypotheses.md (Post-QG Amendments section con correzioni reali), session-summary.md (Post-QG Real Validation section), ingest.json. Verdetti QG preservati per consistenza metodologica; 3 hypothesis citation-integrity scores effettivamente scesi da 9 a 7, due hypothesis (C2-H8, E1-C1-H4) sostanzialmente downgraded, due (E1-C1-H2, C2-H7) upgraded. Scope dell'incident: S001-S024 OK (vecchie versioni CC permettevano nested dispatch); S025/S030/S031/S026 failed (nuove versioni CC post ~2.1.114 strippano Agent da sub-agent).

**Lesson 1 — assumption verification**: un'assumption architetturale (nested sub-agent dispatch) era load-bearing per l'intero pipeline ma non era verificata contro il runtime corrente. Quando il runtime e' cambiato silenziosamente, il pipeline ha prodotto output strutturalmente validi ma scientificamente invalidi perche' il design dell'orchestrator rendeva la fabricazione il path of least resistance. Soft guidance nei prompt e' insufficiente; servono (a) l'architettura corretta + (b) hook deterministici che verifichino dispatch reali.

**Lesson 2 — hook che warns != hook che protects**: un hook che emette warning anziche' block non e' un safety mechanism, e' un logging mechanism. Se un constraint e' load-bearing per la correttezza scientifica del pipeline, il hook deve BLOCK, non WARN. La pre-v5.23 orchestrator-stop-gate.py enumerava correttamente i required dispatch ma li downgradeava a warning — precisamente il failure mode che avrebbe dovuto prevenire.

**Lesson 3 — "ha funzionato 20 volte" != "continuera' a funzionare"**: MAGELLAN ha fatto 24 sessioni con Opus 4.6 + Claude Code pre-2.1.114 senza problemi visibili. Questo non garantisce nulla se l'infrastruttura sottostante cambia. Change detection per le assumption architetturali dovrebbe essere parte del pipeline (es. probe di tool availability all'inizio di ogni /discover).

---

## v5.22 — Citation Fabrication Hardening (18 aprile 2026)

**Motivazione**: La sessione 2026-04-16-scout-024 (pulsatile wave physics x vascular aging) ha rivelato un failure mode sistematico nel Generator: 5 di 6 ipotesi cycle-1 avevano errori di citazione, e cycle-2 (tentando repair) ne ha introdotti di nuovi. Pattern specifico: le citazioni non sono completamente inventate, ma author-PMID pairing e' sbagliato. Esempi: "Hashimoto/Ito 2016" citato per PMC5079032 che appartiene a Phan et al.; "Zhang 2016 Aging-US" citato per PMID che appartiene a Guina 2016 psichiatria; "Groenendijk 2005" citato con PMID 15920022 invece del corretto 15920020. I paper esistono, gli autori citati esistono, ma non come autori di QUEL PMID.

**Causa radice**: La SELF-CRITIQUE del Generator (v5.4) verifica "paper exists" ma non author-identifier coherence. I PMID sono interi arbitrari senza contenuto semantico, quindi sono l'elemento piu' facile da confondere nella knowledge parametrica. Topic giusto + autore giusto per il topic + PMID preso da paper adiacente sullo stesso topic = citazione fabbricata che sembra plausibile al check "il paper esiste".

**Decisioni**:
1. **Generator SELF-CRITIQUE step 5 esteso** (v5.4 → v5.5): "Citation specificity" diventa "Citation specificity AND author-identifier pairing". Rule of thumb: se il claim sopravvive con solo "author + year + topic", e' piu' sicuro di "author + year + journal + PMID" quando c'e' dubbio sul pairing. Tre opzioni quando incerti: (a) downgrade a [PARAMETRIC], (b) citare senza identifier specifico, (c) omettere la citazione e usare grounding topic-level.

2. **Critic attack vector 9 esteso** (v5.4 → v5.5): nuovo sotto-check "Verify author-identifier pairing". Il Critic deve cercare il PMID direttamente (pubmed.ncbi.nlm.nih.gov/<PMID>) o cercare "[First author] [Year] [Journal]" e confrontare il PMID restituito con quello citato. Author-PMID mismatch = CITAZIONE FABBRICATA anche se paper e autori esistono separatamente.

3. **META-CRITIQUE reflection esteso**: domanda esplicita su mismatched author-identifier pairing. Cross-hypothesis propagation flaggata come segnale di confusione parametrica sistematica (non slip isolato).

**File modificati**:
- `.claude/agents/generator.md`: SELF-CRITIQUE step 5 riscritto, aggiunta sezione "Why step 5 matters" (descrizione generica del failure mode, session-agnostic)
- `.claude/agents/critic.md`: attack vector 9 esteso, META-CRITIQUE step 4 riscritto
- `CLAUDE.md`: nuovo design principle "Session-agnostic agent prompts" in Architecture, sezione "Where session-specific content belongs" in Documentation Rules
- `.claude/agents/discovery-orchestrator.md`, `cross-model-validator.md`, `holdout-evaluator.md`: esempi di session ID concreti sostituiti con placeholder `{SESSION_ID}` / `<YYYY-MM-DD-mode-NNN>` per coerenza con la nuova regola
- `docs/CHANGELOG.md`: questa entry

**Evidenza**: S024 Quality Gate ha killato E3-H3 (composite 6.0) per "2 fabricated citations inherited from cycle 2 (Zhang 2016 Aging-US / Dijk 2005 Hypertension) at core mechanism claims". GPT-5.4 cross-model ha rilevato 3 issues residui su E2-C2-H8. Layered verification (Critic → QG → cross-model) ha catturato tutte le fabrication a core mechanism, ma il costo computazionale di intercettarle tardi e' alto. Spostare il check al Generator riduce waste nelle cycles successive.

**Correzione mid-drafting**: la prima versione delle modifiche agli agent aveva embedded il session ID "S024" nei prompt ("this is the S024 failure mode"). Errore: gli agent prompt sono distribuiti open source e girano su macchine di altri utenti con sessioni proprie. Riferimenti a sessioni specifiche sono opachi e potenzialmente confondenti per un'installazione fresca. Fixato: descrizioni generiche del failure mode + nuova regola in CLAUDE.md che vieta session ID in `.claude/agents/*.md` (storia per-sessione va in CHANGELOG, meta-insights, result dirs).

**Non-regressione**: il change e' additivo. Le ipotesi che usano citation grounding corretta non sono affette. La tolleranza per "cito senza PMID specifico" e' nuova e concede flessibilita' al Generator quando incerto, invece di forzarlo a inventare un PMID specifico.

---

## v5.21 — Opus 4.7 Migration (18 aprile 2026)

**Motivazione**: Il 16 aprile 2026 Anthropic ha rilasciato Claude Opus 4.7, sostituendo Opus 4.6 come modello Opus di default. La documentazione ufficiale (announcement, what's-new, best-practices, migration-guide) elenca diversi behavioral change potenzialmente impattanti per un pipeline multi-agent: "fewer subagents spawned by default", "fewer tool calls by default", "more literal instruction following", "stricter effort calibration", "response length calibrates to task complexity". Tokenizer nuovo con fino al 35% in piu' di token. Nuovo effort tier `xhigh` consigliato come default per use case agentic.

**Stato empirico**: La sessione 2026-04-16-scout-024 e' stata eseguita con Claude Code aggiornato a Opus 4.7 (frontmatter `model: opus` e' un alias che risolve al modello current-latest). Risultati: pipeline intero dispatchato (14 agenti), 2 cycle completi, 23 markdown deliverables prodotti (vs 8 in S018 con v5.18 regression), cross-model validation completata (GPT-5.4: 73 web search + 7 code execution; Gemini: analysis completa), Dataset Evidence Miner ha verificato 19 claim molecolari, outcome 1 PASS (composite 10.0) + 3 CONDITIONAL_PASS. Nessuna delle preoccupazioni della migration guide si e' manifestata nel pipeline MAGELLAN.

**Perche' i behavioral change non si manifestano qui**:
- "Fewer subagents": l'orchestratore non ha WebSearch/WebFetch disponibili (vincolo architetturale esplicito), quindi non PUO' inlinare le fasi. Deve dispatchare.
- "Fewer tool calls": gli agenti retrieval-heavy (Literature Scout, Critic, Cross-Model Validator via GPT/Gemini) hanno prompt che esplicitano quando e perche' chiamare i tool, e il vincolo "Web search required per hypothesis" e' hard constraint nel Critic.
- "More literal instruction following": la calibrazione "Reduced MUST/CRITICAL density" fatta in v5.2 per Opus 4.6 adaptive thinking si applica naturalmente a 4.7 (che amplifica la stessa tendenza).
- "Stricter effort calibration": gli agenti sono pinned a `high`/`max` via frontmatter, mai a `low`/`medium` che sono i tier affetti da under-thinking.
- Stop-gate hooks deterministici bloccano output incompleti indipendentemente dal comportamento del modello.

**Decisioni**:
1. **Doc sync**: tutti i riferimenti "Opus 4.6" in docs/methodology-v5.md, prompts/validation-prompt-gpt.md, launch-creators.md, launch-media-pitches.md, scripts/init-session.sh aggiornati a "Opus 4.7". I riferimenti storici in CHANGELOG v5.2 e in validation/results/retrospective-retrodiction-all-sessions.md NON sono modificati (descrivono accuratamente lo stato del tempo).

2. **CLAUDE.md**: aggiunta sezione "Model alias resolution" che documenta la strategia di alias (`opus` → Opus 4.7, `sonnet` → Sonnet 4.6 ad aprile 2026) e cita S024 come evidenza empirica che il pipeline e' compatibile con 4.7.

3. **methodology-v5.md**: nuova entry benchmark per Opus 4.7 (affiancata alla entry 4.6 per reference storica), nota su "more literal instruction following" che allinea con la riduzione MUST/CRITICAL gia' fatta.

4. **scripts/init-session.sh**: metadata default `"model": "opus-4.7"` per le nuove sessioni.

**Non-modifiche deliberate**:
- Effort levels non cambiati (Opus=max, Sonnet=high). A/B test `xhigh` vs `max` considerato ma non necessario: S024 ha prodotto output qualitativamente eccellente con `max`, nessun segnale di overthinking o diminishing returns.
- Prompts degli agenti non re-baseline. L'evidenza empirica S024 mostra che funzionano bene su 4.7.
- Scaffolding anti-inlining dell'orchestratore non rinforzato. Il dispatch e' robusto.
- Nessuna adozione di task_budgets (beta, solo Messages API, non accessibile via Claude Code).
- Nessuna modifica per high-resolution image support (MAGELLAN e' text-only).

**File modificati**:
- `CLAUDE.md`: sezione "Model alias resolution" aggiunta
- `docs/methodology-v5.md`: 8 righe aggiornate (linee 12, 207, 219, 490, 611, 622, 687, 700-701, 762)
- `prompts/validation-prompt-gpt.md`: linea 19
- `launch-creators.md`: linea 224
- `launch-media-pitches.md`: linea 150
- `scripts/init-session.sh`: linea 47
- `docs/CHANGELOG.md`: questa entry

**Evidenza**: S024 (2026-04-16-scout-024) con 44 file totali, 23 markdown, phase `complete`, 2 cycle pieni, tutti i post-QG agent completati, 1 PASS + 3 CONDITIONAL_PASS. Confronto con S018 (pre-4.7, post-v5.18 regression): 25 file totali, 8 markdown, phase `complete` ma con deliverables mancanti. S024 e' qualitativamente superiore a S018 lungo ogni dimensione misurabile.

---

## v5.20 — Deliverables Verification Gate (12 aprile 2026)

**Motivazione**: La sessione 2026-04-10-scout-018 (reservoir computing x gut microbiome) ha completato il core pipeline con successo (2 PASS + 3 CONDITIONAL_PASS), ma l'orchestratore ha dichiarato `phase: "complete"` con diversi deliverables mancanti: 5 report markdown (raw-hypotheses, critiqued, ranked, target-evaluation, cross-model-consensus), cross-model validation incompleta, `knowledge/meta-insights.md` non aggiornato, upload 400.

**Causa radice**: La v5.18 ha ristrutturato la State Management dell'orchestratore, passando dalla lettura di `state/session.json hypotheses.cycle{N}` alla lettura di `{results_dir}/cycle{N}-*.json`. Ma le constraint degli agenti (generator, critic, ranker, target-evaluator) non sono state aggiornate -- dicevano ancora `"Write to state: Write to results/X.md. Update state/session.json hypotheses.cycle{N}"`. Gli agenti, vedendo che la parte session.json dell'istruzione era obsoleta (v5.18: "NEVER put hypothesis content into session.json"), hanno inferito di scrivere solo i JSON files che l'orchestratore legge, saltando i markdown. Confermato dal confronto: S017 (pre-v5.18) aveva 15 file markdown, S018 (post-v5.18, prima sessione dopo il commit) ne aveva 8.

**Decisioni**:
1. **Fix constraint agenti** (generator, critic, ranker, target-evaluator): la vecchia istruzione `"Write to state"` che conflava markdown e session.json e' stata sostituita con `"Output files (BOTH required)"` che separa chiaramente: (a) markdown come primary deliverable (testo dettagliato) e (b) JSON come metadata strutturato per il routing. Rimosso il riferimento obsoleto a `state/session.json hypotheses.*`.

2. **Guard Protocol: artifact verification** (orchestrator): dopo ogni dispatch, l'orchestratore verifica che esistano SIA il JSON SIA il markdown. Se il markdown manca, ri-dispatcha l'agente originale per scriverlo (non genera un fallback dal JSON -- il markdown e' il deliverable ricco, il JSON e' metadata leggero).

3. **Deliverables verification gate** (orchestrator): nuova sezione prima del session summary. Esegue un check di esistenza su tutti i file richiesti. Markdown mancanti triggerano un re-dispatch dell'agente. `phase: "complete"` non puo' essere impostato finche' la verifica non passa.

4. **Cross-model completion enforcement** (orchestrator): se cross-model-validator restituisce `manual_export_only`, l'orchestratore controlla i file di validazione effettivi. Usa `cross_model_export_only` in phases_completed se assenti. Divieto esplicito di `run_in_background` per agenti post-QG.

5. **Knowledge persistence duale** (orchestrator): richiede l'aggiornamento di ENTRAMBI `knowledge/discovery-log.json` e `knowledge/meta-insights.md`.

**File modificati**:
- `.claude/agents/generator.md`: constraint #4 riscritta (output files separati)
- `.claude/agents/critic.md`: constraint #5 riscritta (output files separati)
- `.claude/agents/ranker.md`: constraint #5 riscritta (output files separati)
- `.claude/agents/target-evaluator.md`: constraints #4-5 unite e riscritte (output files separati)
- `.claude/agents/discovery-orchestrator.md`: 4 modifiche (Guard Protocol, cross-model, deliverables verification, knowledge persistence)
- `CLAUDE.md`: sezioni Operational e Meta-learning aggiornate
- `docs/methodology-v5.md`: nuova sezione 3 (deliverables verification gate) + knowledge persistence
- `README.md`: phase list aggiornata
- `docs/CHANGELOG.md`: questa entry

**Evidenza**: S017 (pre-v5.18, 5 aprile): 15 markdown. S018 (post-v5.18, 10 aprile): 8 markdown. Le definizioni degli agenti non erano state modificate tra le due sessioni -- solo l'orchestratore. Il mismatch tra le istruzioni degli agenti e le aspettative dell'orchestratore e' la causa.

---

## v5.19 — Computational Verification Integration (7 aprile 2026)

**Motivazione**: Le verifiche computazionali manuali (5 analisi su dati pubblicati) erano visibili solo nella cartella `verification/` del repo CLI, ma assenti dal sito web. Gap significativo: sono la prova piu' forte che le ipotesi MAGELLAN hanno valore scientifico reale.

**Decisioni**:
1. **Manifest-driven verification**: ogni `verification/{slug}/` richiede un `manifest.json` con verdetto, figure, session_id. Questo collega la verifica al DB del sito.
2. **Website integration**: nuovo modello `ComputationalVerification` in Prisma, pagine dedicate (`/verifications`, `/verifications/[slug]`), banner prominente sulla pagina ipotesi, badge "VERIFIED" sulle card, conteggio nella credibility strip homepage.
3. **Figure su Vercel Blob**: le figure PNG vengono caricate su Blob durante sync, i riferimenti nel markdown vengono riscritti con URL Blob.
4. **MarkdownRenderer esteso**: aggiunto supporto per `![alt](url)` per renderizzare figure inline nei report.

**File modificati (CLI)**:
- `verification/*/manifest.json` (5 nuovi): metadati strutturati per sync
- `CLAUDE.md`: sezione "Post-pipeline verification"
- `README.md`: struttura directory aggiornata

**File modificati (magellan-web)**:
- `prisma/schema.prisma`: modello ComputationalVerification + relazioni
- `scripts/sync-verifications.ts` (nuovo): sync manifests -> Blob + DB
- `app/verifications/page.tsx` (nuovo): pagina indice verifiche
- `app/verifications/[slug]/page.tsx` (nuovo): report completo
- `components/computational-verification.tsx` (nuovo): banner ipotesi
- `components/hypothesis-card.tsx`: badge VERIFIED
- `components/markdown-renderer.tsx`: supporto immagini
- `components/cluster-group.tsx`, `discoveries-view.tsx`: propagazione verificationCount
- `components/mobile-nav.tsx`, `app/layout.tsx`: link navigazione
- `lib/db/queries.ts`: 6 query aggiornate, 2 nuove
- `app/page.tsx`: credibility strip
- `app/discoveries/[slug]/page.tsx`: banner verifica

---

## v5.18 — Post-QG Pipeline Fixes (7 aprile 2026)

**Motivazione**: La sessione 2026-04-03-open-015 (leiomyosarcoma) ha rivelato che il session summary veniva scritto PRIMA del completamento degli agenti post-QG (cross-model, convergence, DEM), producendo output incompleto ("Cross-Model Validation: Not performed"). Inoltre final.json mancava dei campi testo (`mechanism`, `supporting_evidence`, `test_protocol`) richiesti dallo script upload, causando errori 400 in fase di pubblicazione. Infine, le correzioni aritmetiche e le citazioni errate trovate dalla cross-model validation non venivano integrate nel deliverable finale.

**Decisioni**:
1. **Fix ordinamento orchestratore**: session-summary.md e ingest.json ora vengono scritti DOPO che tutti gli agenti post-QG hanno completato (o fallito). final-hypotheses.md viene scritto prima (non richiede dati post-QG).

2. **Fix enrichment final.json**: il passo "Enrich final.json" ora estrae anche `mechanism`, `supporting_evidence`, `test_protocol`, `bridge_summary`, `novelty_status` dal markdown delle ipotesi e dal quality-gate.json. Include verifiche di lunghezza minima (mechanism >= 200, evidence >= 50, test >= 100 caratteri).

3. **Post-QG Amendments**: dopo la cross-model validation, l'orchestratore aggiunge una sezione "## Post-QG Amendments" a final-hypotheses.md con discrepanze aritmetiche, correzioni citazioni, e counter-evidence trovate da GPT/Gemini. Non modifica i punteggi QG (canonici).

4. **DEM follow-up suggestions**: il Dataset Evidence Miner ora include una sezione "Suggested Computational Follow-Ups" con query database specifiche e azionabili che un ricercatore potrebbe eseguire per validare ulteriormente le ipotesi senza lavoro di laboratorio.

5. **Session concurrency safety**: `state/session.json` e' un singleton condiviso da tutte le conversazioni Claude Code. Se una sessione viene interrotta (rate limit, crash, cambio conversazione), lo stop hook bloccava TUTTE le conversazioni successive. Tre meccanismi risolvono il problema:
   - **Staleness check**: lo stop hook controlla `metadata.last_updated`: se >30 minuti, la sessione e' considerata abbandonata e lo stop hook approva invece di bloccare.
   - **Per-session state backup**: l'orchestratore copia `state/session.json` in `results/{session-id}/session-state.json` a ogni transizione di fase. `init-session.sh` preserva lo stato della sessione precedente prima di sovrascrivere.
   - **Resume support**: l'orchestratore rileva prompt "Resume session X", ripristina lo stato dal backup per-sessione, e riprende dalla fase interrotta. `/status` mostra le sessioni interrotte recuperabili.

**File modificati**:
- `.claude/agents/discovery-orchestrator.md`: riordinamento fasi, enrichment esteso, Post-QG Amendments, last_updated, session-state backup, resume detection
- `.claude/agents/dataset-evidence-miner.md`: sezione follow-up suggestions
- `.claude/commands/status.md`: mostra sessioni interrotte recuperabili
- `prompts/session-summary-format.md`: sezioni convergence/DEM nel template summary
- `scripts/orchestrator-stop-gate.py`: staleness check con threshold 30 min + fallback su progress timestamps
- `scripts/init-session.sh`: campo `last_updated` nello state iniziale + preservazione stato sessione precedente
- `CLAUDE.md`: design principles operativi aggiornati

---

## v5.17 — Licensing & Attribution Framework (28 marzo 2026)

**Motivazione**: Preparazione al lancio pubblico. Il repository era sotto licenza MIT senza protezione sull'attribuzione (chiunque poteva forkare e rimuovere il credit) e senza licenza sugli output (ipotesi scientifiche). Serviva un framework chiaro sia per il software che per le scoperte.

**Decisioni**:
1. **Software: MIT → Apache 2.0** — Il file NOTICE (obbligatorio in ogni redistribuzione) garantisce che "Alberto Trivero / Kakashi Venture Accelerator" sopravviva a fork e rebrand. Patent grant esplicito protegge da patent trolling sull'architettura multi-agente. Zero costo di adozione rispetto a MIT.

2. **Output: dual-track CC0/CC-BY 4.0** — Le scoperte autonome (`/discover` puro) sono CC0 (pubblico dominio con richiesta volontaria di citazione), onesto sul fatto che il copyright su contenuti AI-generati è incerto. Le scoperte guidate (`/discover A × B`, `--context`, `--papers`, `--interactive`) sono CC-BY 4.0, riconoscendo la direzione creativa del contributore.

3. **Metadata pipeline** — `output_license`, `output_license_reason`, e `attribution` sono ora tracciati in `session.json`, portati in `ingest.json`, e inviati all'API del sito.

**File creati**:
- `NOTICE`: attribuzione Apache 2.0 (obbligatorio in redistribuzioni)
- `DISCOVERY_LICENSE.md`: dual-track licensing per gli output
- `CONTRIBUTING.md`: guida per contributori (scoperte + codice)

**File modificati**:
- `LICENSE`: MIT → Apache 2.0
- `package.json`: `"license": "Apache-2.0"`
- `prompts/ingest-schema.json`: campi `output_license`, `output_license_reason`, `attribution`
- `.claude/commands/discover.md`: determinazione licenza basata su mode/flags
- `scripts/init-session.sh`: campi licenza in session.json iniziale
- `.claude/agents/discovery-orchestrator.md`: istruzioni per popolare licenza in ingest.json
- `scripts/upload-session.mjs`: `outputLicense` e `attribution` nel payload API
- `prompts/session-summary-format.md`: licenza e attribuzione nel summary + footer ipotesi
- `README.md`: sezione License aggiornata
- `CLAUDE.md`: sezione Licensing aggiunta

---

## v5.16 — CLI-Only Publishing (28 marzo 2026)

**Motivazione**: Un contributor esterno ha lanciato `/discover` e a fine sessione l'orchestrator ha suggerito `cd ../magellan-web && npm run sync` per pubblicare i risultati. Quel workflow richiede accesso al repo `magellan-web`, disponibile solo al maintainer del progetto.

**Root cause**: CLAUDE.md conteneva una sezione "Publishing results to the website" con il workflow `npm run sync`. Siccome CLAUDE.md è caricato come contesto di progetto per tutti gli agenti, l'orchestrator lo raccoglieva e lo suggeriva agli utenti.

**Fix**: Rimossa la sezione sync da CLAUDE.md, sostituita con una nota sull'upload automatico via API (`scripts/upload-session.mjs`, già mandatory dal v5.7). Aggiunta sezione "Publishing Status" in `session-summary-format.md` con messaggi espliciti per upload riuscito/fallito/senza key. Il workflow sync resta documentato nel repo `magellan-web` per uso del maintainer.

**File modificati**:
- `CLAUDE.md`: sezione "Publishing results" — rimosso sync, aggiunto upload API
- `prompts/session-summary-format.md`: aggiunta sezione "Publishing Status"

---

## v5.15 — Fix Orchestrator final.json Reliability (28 marzo 2026)

**Motivazione**: Sessione 015 ha rivelato che l'orchestrator riportava status e verdetti sbagliati. Il quality-gate.json conteneva 2 PASS + 4 CONDITIONAL_PASS correttamente, ma il final.json (e di conseguenza il session summary e lo status) diceva "4 CONDITIONAL_PASS, no full PASS".

**Root cause**: `final.json` non era scritto da nessun agente esplicitamente. L'orchestrator lo ricostruiva dalla propria memoria di contesto (spesso compressa dopo ore di sessione), producendo dati corrotti: verdetti downgraded, compositi sbagliati, ipotesi mancanti.

**Fix architetturale** (Opzione B — orchestrator crea da file):
1. L'orchestrator ora CREA `final.json` leggendo `quality-gate.json` da disco (non da memoria)
2. Il quality-gate agent ora scrive esplicitamente `quality-gate.json` con schema definito incluso `summary.session_status`
3. L'orchestrator determina SESSION HEALTH da `quality-gate.json` su disco, non dalla propria memoria
4. Aggiunto step di VERIFICATION post-enrichment: controlla che verdetti e compositi in final.json matchino quality-gate.json
5. Warning espliciti nel prompt: "Context compression corrupts numerical values. Always read the JSON file."

**File modificati**:
- `discovery-orchestrator.md`: sezioni QUALITY GATE, SESSION HEALTH, Enrich final.json
- `quality-gate.md`: constraint 4 (output format) — ora include quality-gate.json con schema esplicito

**Evidence**: Session 015 final.json aveva 4 ipotesi (dovevano essere 6), tutte CONDITIONAL_PASS (dovevano essere 2 PASS + 4 CP), compositi sbagliati (7.6/7.5/7.0/6.7 vs reali 7.85/7.80/6.75/6.25/6.25/6.05).

---

## v5.14 — Impact-Aware Prioritization (26 marzo 2026)

**Motivazione**: MAGELLAN ottimizza per novità e rigore, ma l'impatto reale (traslazionale, sociale, economico) pesa solo 10% nel Ranker e è completamente assente dalla selezione target, dal Quality Gate, e dal meta-learning. Con risorse limitate, la pipeline dovrebbe preferire direzioni che producono scoperte ad alto impatto, non solo nuove.

**Principio di design**: L'impatto entra come segnale parallelo, mai come sostituto della qualità. Il disjointness hard constraint (87% vs 30% pass rate) resta intatto — l'impatto opera solo come tiebreaker dentro il pool DISJOINT.

### Modifiche per fase

**Scout** (`scout.md`):
- Nuovo campo `impact_potential` (1-10) + `impact_type` nell'output format
- Nuovo check #7 nel TARGET QUALITY CHECK: almeno 1 target con impact_potential >= 6
- Campi impact aggiunti al formato discovery-log.json

**Target Evaluator** (`target-evaluator.md`):
- 5° asse informativo: impact potential (non incluso nel composite)
- Output aggiornato con `Impact Potential: Y/10 (informational, not in composite)`
- `impact_potential_scores` array scritto in state

**Orchestrator** (`discovery-orchestrator.md`):
- Impact tiebreaker in Phase 0c (tra candidati con disjointness e confidence simili)
- Impact tiebreaker in Phase 0d (dentro il pool DISJOINT, prima di Scout confidence)
- IPS computation dopo EES: `IPS = scout_ip × 0.4 + (signal_count/3 × 10) × 0.6`
- IPS incluso in ingest.json e session summary

**Ranker** (`ranker.md`):
- Impact (10%) decomposto in Paradigm impact (5%) + Translational impact (5%)
- Tabella di scoring aggiornata con due sotto-righe

**Quality Gate** (`quality-gate.md`):
- Item 11 informativo (non pass/fail): application pathway, applied domain, validation horizon
- Annotazione solo per PASS/CONDITIONAL_PASS

**Session Analyst** (`session-analyst.md`):
- Nuova categoria 7: impact metrics (tipo, dominio, correlazione impact-quality)
- Nuova tabella Impact Metrics in meta-insights.md
- Raccomandazione automatica se impatto e qualità sono anti-correlati

**Schemas e scripts**:
- `ingest-schema.json`: nuova sezione `impact_assessment`
- `knowledge-schema.json`: campo `impact_assessment` per entry
- `init-session.sh`: campo `health.impact_potential_score` nel template session.json
- `session-summary-format.md`: sezione Impact Assessment

### Evidenza a supporto
- 16 sessioni mostrano che Impact al 10% (paradigm-only) non differenzia ipotesi traslazionali da puramente teoriche
- Convergence Scanner (v5.13) già cerca clinical trials, grants, brevetti — segnali traslazionali non sfruttati per prioritizzazione
- Disjointness data: DISJOINT 87% pass rate — il constraint non viene toccato, l'impatto opera solo come tiebreaker

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
- `prompts/validation-prompt-gpt.md` — Istruzioni esplicite per usare web search e code execution
- `prompts/validation-prompt-gemini.md` — Istruzioni per verifica computazionale dei mapping e sezione COMPUTATIONAL CHECK nell'output format

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
