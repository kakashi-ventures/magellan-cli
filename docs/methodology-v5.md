# MAGELLAN — Methodology
### Multi-Agent Generative Exploration of Latent Links Across kNowledge

## Principio guida

MAGELLAN è un **esperimento sulla capacità dei sistemi agentici AI moderni di fare scoperte scientifiche autonome**. L'ipotesi di fondo: una buona architettura multi-agente con modelli frontier (marzo 2026) è in grado di trovare connessioni reali tra corpi di conoscenza esistenti che gli umani non hanno ancora collegato — operando in totale autonomia, senza input di dominio da parte dell'utente.

Non è uno strumento per ricercatori. È un test di capability. L'utente lancia `/discover`, esce dalla stanza, e torna a trovare ipotesi scientifiche testabili. Queste vengono poi validate cross-model e, idealmente, sottoposte a esperti di dominio per valutazione.

Progettato per Claude Code (marzo 2026) con Opus 4.6 (ragionamento profondo) e Sonnet 4.6 (task strutturati), sfrutta Agent Teams, hooks deterministici, MCP servers per retrieval strutturato, e un paradigma ibrido **parametric-generation + retrieval-validation**.

---

## Fondamento concettuale: l'Undiscovered Public Knowledge di Swanson

MAGELLAN è, nella sua essenza, una macchina per trovare **Undiscovered Public Knowledge (UPK)** — un concetto formulato da Don R. Swanson nel 1986.

### Il concetto

Swanson osservò che la letteratura scientifica contiene connessioni logiche che nessuno ha ancora fatto, non perché l'informazione sia segreta, ma perché risiede in **letterature disgiunte** — corpi di conoscenza che non si citano reciprocamente. L'esempio fondativo: la letteratura sul magnesio (effetti vasodilatatori, anti-aggreganti piastrinici) e la letteratura sull'emicrania (vasocostrizione, aggregazione piastrinica) contenevano tutte le premesse per ipotizzare che il magnesio potesse trattare l'emicrania. Nessuno aveva fatto il collegamento perché i due campi non dialogavano. Swanson lo fece nel 1988, e studi clinici successivi confermarono l'ipotesi.

Swanson formalizzò questo nel modello **ABC**: il Campo A e il Campo C non si citano, ma condividono un concetto intermedio B (il *bridge term*) che compare in entrambi. La scoperta consiste nell'identificare B e nel costruire l'inferenza A→B→C.

### Il metodo originale (superato)

Per trovare queste connessioni, Swanson sviluppò un metodo **bibliometrico**: analisi di co-occorrenze di MeSH terms, grafi citazionali, matrici di frequenza. Sistemi come Arrowsmith, BITOLA, e più recentemente LBD automatizzati hanno raffinato questo approccio per decenni.

Questo metodo è **superato dai modelli frontier del 2026**, per una ragione fondamentale: il problema dell'UPK esiste perché nessun ricercatore umano può leggere entrambe le letterature. Un LLM addestrato su milioni di paper ha già *assorbito* entrambe. Il problema non è più rilevare la disgiunzione citazionale — è **elicitare le connessioni latenti** dalla conoscenza parametrica del modello.

Le evidenze lo confermano: nessuno dei breakthrough AI-driven del 2025-2026 (GPT-5 + Ginkgo, Google AI Co-Scientist, Aletheia) ha usato analisi bibliometrica. Tutti usano conoscenza parametrica + architettura multi-agente + debate/evoluzione.

### Come MAGELLAN eredita il concetto e supera il metodo

| Swanson (1986) | MAGELLAN (2026) |
|---|---|
| Il problema: UPK esiste tra letterature disgiunte | Stesso problema, stessa motivazione |
| Il bridge: concetto B condiviso tra A e C | **Bridge concepts obbligatori** in ogni target dello Scout |
| Il metodo: analisi bibliometrica (MeSH, citazioni) | **Conoscenza parametrica** dell'LLM come lettore universale |
| Rilevamento: co-occorrenze statistiche | **Elicitazione**: Structured Relationship Map, facet recombination, adversarial probing |
| Validazione: ricerca manuale in database | **Retrieval automatico**: Literature Scout + MCP servers + verifica disgiunzione |
| Scala: una coppia A-C per studio, mesi di lavoro | **10 strategie parallele**, 2 cicli evolutivi, 15-45 minuti |

Il modello ABC resta la struttura portante dell'output: ogni ipotesi MAGELLAN ha la forma `Field A → Bridge mechanism → Field C`. La differenza è *come* si arriva al bridge — non con statistiche citazionali, ma con il ragionamento parametrico di un modello che ha già letto entrambe le letterature.

---

## Architettura: 15 agenti, 3 fasi (v5.13)

```
FASE 1 — ESPLORAZIONE (Sequential Narrowing — v5.8)
┌──────────────┐
│    Scout      │  Phase 0a: genera 5-6 candidati
│  [Opus]       │
│ 10 strategie  │
│ + diversif.   │
│ + exploration │
│   slot        │
│ + creativity  │
│   constraint  │
└──────┬───────┘
       ▼
┌──────────────────┐
│ Literature Scout  │  Phase 0b: verifica disjointness per TUTTI
│    [Sonnet]       │  + domain-aware retrieval
│ MCP + WebSearch   │  + bridge validation
└──────┬───────────┘
       ▼
  Orchestrator [Opus]   Phase 0c: narrow da 5-6 a 3
  (DISJOINT priority    (WELL_EXPLORED esclusi, DISJOINT preferiti)
   + strategy diversity)
       ▼
┌──────────────────────┐
│  Target Evaluator     │  Phase 0d: adversarial challenge
│  [Opus] 4 attack axes │
└──────────┬───────────┘
       ▼
  Orchestrator [Opus]   Phase 1: select + dispatch
  (disjointness hard constraint)
       ▼
┌──────────────────────────┐
│  Computational Validator  │  KEGG, STRING, PubMed
│  [Sonnet + Bash]         │  co-occurrence, physics
└──────────┬───────────────┘
       ▼

FASE 2 — GENERAZIONE & CRITICA (2 cicli)
┌────────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
│  Generator  │──▶│  Critic   │──▶│  Ranker   │──▶│  Evolver  │
│   [Opus]    │   │  [Opus]   │   │ [Sonnet]  │   │ [Sonnet]  │
│ parametric  │   │ 9 attack  │   │ 6 dimens. │   │ evolution │
│ + lit.contxt│   │ + web     │   │ + grounded│   │ + diversit│
│ + comp.val. │   │           │   │ + Elo chk │   │           │
│ + bisociat. │   │           │   │           │   │           │
│ + multi-lvl │   │           │   │           │   │           │
└────────────┘   └──────────┘   └──────────┘   └──────┬────┘
       ▲                                              │
       └──────────── ciclo 2 ◀────────────────────────┘

FASE 3 — VALIDAZIONE FINALE + META-LEARNING
┌──────────────────┐   ┌──────────────────┐
│  Quality Gate     │   │ Session Analyst   │  ← v5.5
│    [Opus]         │──▶│   [Sonnet]        │
│ 10-point rubric   │   │ meta-learning     │
│ + web grounding   │   │ → meta-insights   │
└──────────┬───────┘   └──────────┬───────┘
           └──────────┬───────────┘
                      ▼
    Session Health → results/{session-id}/*.md + state/session.json
                   + knowledge/meta-insights.md

LAYER TRASVERSALE — GUARD & HOOKS
┌─────────────────────────────────────────────────┐
│  Post-fase guards (retry → fallback → abort)    │
│  Blocking SubagentStop hooks (exit 2)           │
│  Stop hook (anti-terminazione prematura)        │
│  PostToolUse dispatch logging (verify-dispatch)  │
│  PreCompact/PostCompact (backup/restore state)  │
│  PostToolUseFailure (tracking WebSearch fails)  │
└─────────────────────────────────────────────────┘
```

### I 15 agenti

| Agente | Modello | Effort | Ruolo |
|---|---|---|---|
| **Scout** | Opus | max | Identifica DOVE cercare: 10 strategie (incl. isomorfismo strutturale + serendipity), bridge concepts obbligatori, strategy diversification, exploration slot, rotating creativity constraint, TARGET QUALITY CHECK reflection |
| **Target Evaluator** | Opus | max | Sfida avversariale dei target Scout su 4 assi: popularity bias, vagueness, structural impossibility, local-optima |
| **Literature Scout** | Sonnet | high | Retrieval strutturato: MCP servers (Semantic Scholar, PubMed) obbligatorio + WebSearch fallback + full-text + disgiunzione + RETRIEVAL QUALITY CHECK reflection |
| **Computational Validator** | Sonnet | high | Verifica programmatica dei bridge concepts: KEGG pathway cross-check, STRING interaction scores, PubMed co-occurrence, back-of-envelope physics |
| **Generator** | Opus | max | Structured Relationship Map + 6-8 ipotesi (parametric + lit. context + validazione computazionale) + SELF-CRITIQUE con verifica claim-level |
| **Critic** | Opus | max | 9 attack vectors (incl. claim-level fact verification) + META-CRITIQUE reflection + critic_questions feedback |
| **Ranker** | Sonnet | high | Scoring su 6 dimensioni con pesi fissi canonici + tabella obbligatoria + diversity check + Elo tournament sanity check |
| **Evolver** | Sonnet | high | Operazioni evolutive con diversity constraint + EVOLUTION QUALITY CHECK reflection. Condizionalmente skippabile |
| **Quality Gate** | Opus | max | Rubrica a 10 punti (incl. per-claim grounding verification) + web grounding + META-VALIDATION reflection |
| **Session Analyst** | Sonnet | high | Meta-learning post-pipeline: strategy performance, kill patterns, bridge type analysis → knowledge/meta-insights.md |
| **Cross-Model Validator** | Sonnet | high | Chiama GPT-5.4 Pro (reasoning high, web search, code interpreter) + Gemini 3.1 Pro (thinking HIGH, code execution, Google Search grounding) via API per validazione indipendente → consensus report. Fallback a file di export se API keys assenti |
| **Convergence Scanner** | Sonnet | high | Post-QG: cerca segnali di convergenza su ClinicalTrials.gov, NIH Reporter, brevetti + conferme parziali di sub-meccanismi da fonti non consultate dalla pipeline |
| **Dataset Evidence Miner** | Sonnet | high | Post-QG: verifica claim molecolari specifici su HPA, GWAS Catalog, ChEMBL, UniProt, PDB via `scripts/query-biodata.py`. Complementare al CV pre-generazione |
| **Holdout Evaluator** | Opus | max | Framework di validazione: confronta output MAGELLAN con scoperte note post-cutoff. Contamination check + similarity scoring meccanistico |
| **Orchestrator** | Opus | max | Dispatch obbligatorio, cicli adattivi, guard logic, session health, knowledge log, meta-learning metrics |

La scelta del modello segue un principio: **Opus per il ragionamento profondo e creativo, Sonnet per i task strutturati e search-intensive**. I livelli di effort sono fissati per agente (Opus: max, Sonnet: high) per garantire la qualità indipendentemente dall'effort di sessione dell'utente. Scout, Target Evaluator, Generator, Critic, Quality Gate e Holdout Evaluator richiedono ragionamento cross-disciplinare e valutazione profonda. Literature Scout, Computational Validator, Ranker, Evolver, Session Analyst, Cross-Model Validator, Convergence Scanner e Dataset Evidence Miner eseguono task più strutturati dove la capacità di giudizio è importante ma non richiede la profondità di Opus.

### Dispatch obbligatorio

L'Orchestratore è un puro coordinatore: NON ha accesso a WebSearch/WebFetch e NON può eseguire fasi inline. Ogni fase viene dispatched al sub-agente specializzato via Agent tool. Questo garantisce:
- **Isolamento dei tool**: il Generator non può fare web search, il Critic non può generare ipotesi
- **Specializzazione**: ogni agente carica solo le skill rilevanti
- **Contesto fresco**: ogni dispatch ha un contesto conversazionale pulito, evitando degradazione nelle fasi tardive
- **Verificabilità**: `state/dispatch-log.json` traccia ogni dispatch per audit post-sessione

### Struttura prompt GOAL/CONSTRAINTS/STRATEGIES

Tutti i prompt agente (tranne l'Orchestratore) sono ristrutturati in 3 sezioni:

1. **GOAL** (immutabile) — Cosa l'agente deve produrre, definito da criteri di qualità dell'output
2. **CONSTRAINTS** (hard) — Requisiti che devono essere rispettati qualunque sia l'approccio
3. **STRATEGIES** (advisory) — Approcci suggeriti, esplicitamente marcati come raccomandati ma non obbligatori

**Perché scala**: Un modello più capace, dato un goal e vincoli, trova percorsi di ragionamento migliori rispetto a seguire passi prescritti. Le CONSTRAINTS preservano il floor di qualità. Le STRATEGIES restano come guida per modelli meno capaci. I SubagentStop hooks catturano output sotto-soglia indipendentemente dal modello.

L'Orchestratore NON è ristrutturato — è un dispatcher, non un reasoner. Il suo prompt è procedurale per design (leggi state → dispatcha → leggi state → guarda gate → dispatcha successivo).

### Reflection loops

Sei agenti hanno sezioni di self-review prima dell'output finale:

| Agente | Reflection | Cosa fa |
|--------|-----------|---------|
| **Generator** | SELF-CRITIQUE | Verifica specificità meccanismo, duplicazione bridge, ragioni di errore parametrico |
| **Critic** | META-CRITIQUE | Calibra kill rate, identifica la ragione più forte per uccidere ogni SURVIVES, verifica completezza web search |
| **Scout** | TARGET QUALITY CHECK | Verifica specificità bridge, diversità strategica, non-ovvietà |
| **Quality Gate** | META-VALIDATION | Verifica confidenza nei PASS, completezza web search, impatto di claim UNVERIFIABLE |
| **Literature Scout** | RETRIEVAL QUALITY CHECK | Verifica completezza MCP, paper count per campo, specificità gap analysis |
| **Evolver** | EVOLUTION QUALITY CHECK | Verifica genuino miglioramento su parent, duplicazione bridge, coerenza crossover |

La reflection è un moltiplicatore di capacità: un modello migliore riflette più efficacemente. La struttura di valutazione esterna (SubagentStop hooks, ranker 3KB gate) impedisce che la reflection diventi auto-congratulazione.

### Cicli adattivi

L'Orchestratore ha 3 decision points per adattare il pipeline alla qualità dell'output:

1. **Groundedness Reinforcement** (dopo critique ciclo 1): Se la maggior parte delle ipotesi ha Groundedness LOW/SPECULATIVE, ri-dispatcha il Literature Scout con ricerche mirate sui meccanismi specifici. Alimenta il Generator nel ciclo 2.

2. **Adaptive Cycle Decision** (dopo ranking ciclo 1):
   - Top-3 ≥ 7.0 AND diversity passed → **early complete** (dispatcha Quality Gate, skip ciclo 2)
   - Survival < 30% OR top-3 < 4.0 → **extended** (richiedi ciclo 2, considera ciclo 3)
   - Altrimenti → **standard** (ciclo 2 normale)

3. **Conditional Evolution** (ciclo 2, dopo ranking): Se top-3 ≥ 6.5, diversity passed, nessun bridge condiviso → skip Evolver, procedi a Quality Gate. `orchestrator-stop-gate.py` aggiornato per non bloccare su evolver skip legittimo.

**Perché scala**: Un modello migliore produce output di qualità superiore prima nella pipeline. Senza adattività, il sistema spreca compute. Con essa, Opus 5 potrebbe completare in 1 ciclo ciò che Opus 4.6 necessita 2.

### Feedback bidirezionale indiretto

Il Critic può scrivere domande specifiche in `results/{session-id}/cycle{N}-critiqued.json` sotto `critic_questions` quando un meccanismo è troppo vago per essere attaccato propriamente. L'Orchestratore inoltra queste domande al Generator nel dispatch del ciclo 2. Il feedback indiretto (via state JSON) preserva il pattern centralizzato.

---

## Il paradigma ibrido: Parametric Generation + Retrieval Validation

### Le evidenze

I modelli frontier (Opus 4.6, GPT-5.2, Gemini 3.1 Pro) ottengono 91–94% su GPQA Diamond — domande PhD-level in biologia, fisica, chimica. Questo è un salto di 55 punti rispetto a GPT-4 (39%, 2023). La conoscenza parametrica è enormemente migliorata.

Tuttavia:
- **AA-Omniscience** (factual recall aperto): il miglior modello raggiunge solo 55% di accuracy
- **Hallucination rate**: 22–48% a seconda del modello e benchmark
- **FrontierScience-Research** (ricerca aperta): GPT-5.2 raggiunge solo 25.3%
- La letteratura scientifica peer-reviewed dietro paywall è largamente assente dai dati di training

### Il compromesso MAGELLAN

La conoscenza parametrica è **il motore generativo** — è dove risiedono le connessioni cross-disciplinari non ovvie. Ma ogni claim fattuale viene verificato tramite retrieval. Il flusso è:

1. **Scout (parametrico)**: Identifica DOVE cercare usando deep reasoning con 10 strategie. Produce **bridge concepts obbligatori** — meccanismi specifici che connettono Field A a Field C. Genera 5-6 candidati (pool ampio). Consulta `knowledge/discovery-log.json` e `knowledge/meta-insights.md` per evitare ri-esplorazioni, riutilizzare bridge produttivi, e prioritizzare strategie con survival rate alto
1b. **Literature Scout (verifica)**: Verifica la disjointness per TUTTI i 5-6 candidati dello Scout usando sorgenti domain-appropriate. Valida i bridge concepts. L'Orchestratore poi filtra a 3 candidati (priorità DISJOINT)
2. **Target Evaluator (adversariale)**: Sfida i 3 target filtrati su 4 assi: popularity bias, vagueness, structural impossibility, local-optima. Previene sessioni sprecate su target apparentemente interessanti ma in realtà già esplorati, vaghi, o strutturalmente impossibili
3. **Literature Scout (retrieval)**: Verifica che i target non siano già esplorati, trova letteratura recente nei campi target. Usa **MCP servers** (Semantic Scholar, PubMed) come fonte primaria e WebSearch come fallback. **Recupera il testo completo dei top 5-10 paper**. Esegue una **verifica di disgiunzione** per confermare che la connessione è genuinamente UPK
4. **Computational Validator (programmatico)**: Verifica i bridge concepts tramite KEGG pathway cross-check, STRING interaction scores, PubMed co-occurrence, e calcoli back-of-envelope. Cattura meccanismi quantitativamente impossibili prima che il pipeline investa nella generazione. Warn-only: l'assenza di evidenza nei database non è evidenza di assenza
5. **Generator (parametrico + contesto letteratura + validazione computazionale)**: Costruisce prima una **Structured Relationship Map** (KG on-the-fly parametrico) per ciascun campo, poi genera ipotesi usando reasoning + contesto + paper completi + segnali dal Computational Validator
6. **Critic (parametrico + web search)**: Attacca ogni ipotesi con 9 attack vectors (inclusa verifica claim-level), cerca counter-evidence via web, esegue l'hallucination-as-novelty check
7. **Ranker**: Scoring su 6 dimensioni inclusa **Groundedness** (20%), diversity check, Elo tournament sanity check
8. **Evolver**: Opera sulle ipotesi top con **diversity constraint**
9. **Session Analyst**: Post-Quality-Gate, analizza strategy performance, kill patterns, bridge type survival rates, disjointness correlation. Produce `knowledge/meta-insights.md` per le sessioni successive
10. **Cross-Model Validator** (v5.6): Post-Session-Analyst. Genera prompt di validazione adattati alle ipotesi specifiche, poi chiama le API di OpenAI (GPT-5.4 Pro, reasoning high) e Google (Gemini 3.1 Pro, thinking HIGH) in parallelo tramite `scripts/validate-crossmodel.mjs`. Produce un consensus report che identifica convergenze e divergenze tra i modelli. Se le API key non sono configurate, genera solo i file di export per validazione manuale. **Non-blocking**: fallimenti non cambiano lo status della sessione
11. **Knowledge Persistence**: A fine sessione, l'Orchestrator aggiorna `knowledge/discovery-log.json` con coppie esplorate, bridge produttivi, ipotesi sopravvissute e uccise, e metriche di strategy performance

---

## Retrieval strutturato

### MCP Servers (passo obbligatorio)

Il retrieval via WebSearch/WebFetch è fragile e richiede parsing HTML. MAGELLAN integra MCP servers come **primo passo obbligatorio** per la ricerca bibliografica:

- **Semantic Scholar MCP** (`@xbghc/semanticscholar-mcp`): `search_papers`, `get_paper`, `get_paper_citations`, `get_paper_references`, `get_recommendations`, `batch_get_papers`
- **PubMed MCP** (`pubmed-mcp`): `pubmed_search`, `pubmed_abstract`, `pubmed_full_text`, `pubmed_open_access`, `pubmed_cited_by`, `pubmed_cites`, `pubmed_similar`

Configurazione in `.mcp.json` nella root del progetto. Il Literature Scout DEVE chiamare i tool MCP **prima** di qualsiasi WebSearch. Fallback a WebSearch solo se MCP restituisce errore di connessione o risultati insufficienti. Questo fornisce un canale di retrieval strutturato indipendente dal web search generico, con metadata machine-readable (autori, citazioni, abstract, MeSH terms) senza parsing HTML.

### API strutturate (via WebFetch)

Oltre ai MCP servers e al web search, il Literature Scout interroga API REST per dati machine-readable invisibili al web search:

- **PubMed E-Utilities (NCBI)**: Metadata strutturato, termini MeSH, grafi citazionali
- **KEGG REST API**: Cross-referencing di pathway — mappa geni → pathway → malattie → farmaci. Pattern di scoperta: gene da Field A → pathway KEGG → pathway condiviso con gene da Field C → link meccanistico latente
- **STRING Protein Interaction Network**: Dati di interazione proteina-proteina con score di confidenza. Valida se proteine da campi apparentemente non correlati hanno interazioni note o predette

### Full-text paper retrieval

Il Literature Scout non si limita a snippet di ricerca. Per i top 5-10 paper per campo, usa WebFetch per recuperare il testo completo e lo salva in `results/papers/`. Il Generator legge questi paper direttamente, ragionando a livello di frase e meccanismo anziché di abstract.

La differenza: "il Campo A studia l'autofagia" vs. "il paragrafo 3.2 del paper di Zhang et al. descrive un pathway ATG5-BECN1 che è strutturalmente analogo al pathway che Smith et al. descrivono nel Campo C, ma con substrati diversi."

### Verifica di disgiunzione (Novelty Sanity Check)

Prima di finalizzare il contesto letteratura, il Literature Scout verifica che la connessione proposta sia genuinamente underexplored:
- Cerca review, survey e meta-analisi che colleghino esplicitamente i due campi
- Classifica il risultato come **DISJOINT** (nessuna letteratura cross-field), **PARTIALLY EXPLORED** (alcune connessioni ma gap nei meccanismi), o **WELL-EXPLORED** (connessione già ampiamente pubblicata)

Questo previene che il pipeline sprechi cicli su connessioni che non sono genuinamente UPK. Un risultato "WELL-EXPLORED" è informazione di alto valore — non un fallimento.

---

## Lo Scout: 10 strategie

1. **Recent Breakthrough Radiation** — Implicazioni di scoperte recenti su campi non ovvi
2. **Anomaly Hunting** — Fenomeni riproducibili ma inspiegati
3. **Converging Vocabularies** — Campi che usano terminologia/framework simili senza saperlo
4. **Tool Transfer Opportunities** — Strumenti da Field A applicabili a Field C
5. **Scale Bridging Gaps** — Fenomeni compresi a una scala ma assenti a scale adiacenti
6. **Failed Paradigm Recycling** — Idee abbandonate in un campo che potrebbero funzionare altrove
7. **Swanson ABC Bridging** — Identificazione sistematica di letterature disgiunte con concetti intermedi condivisi. Metodo fondazionale della Literature-Based Discovery (Swanson 1986). Il Literature Scout cerca sistematicamente "B terms" che compaiono in entrambi i campi A e C senza che A e C si citino reciprocamente
8. **Contradiction Mining** — Ricerca attiva di contraddizioni nella letteratura come fonti di ipotesi. Ispirata da ContraCrow di FutureHouse. Se due paper in campi diversi affermano cose mutuamente esclusive, la risoluzione della contraddizione spesso rivela una connessione non banale
9. **Structural Isomorphism Discovery** (v5.8) — Cerca campi che condividono la STESSA struttura formale (equazioni matematiche, topologia di network, vincoli information-theoretic, dinamiche di transizione di fase) ma con substrati fisici COMPLETAMENTE diversi. Il bridge concept è l'OGGETTO MATEMATICO stesso, non una molecola o un pathway. Questa strategia è domain-agnostic — funziona per qualsiasi campo scientifico. Esempio: teoria della percolazione connette epidemiologia e frattura dei materiali
10. **Serendipity Through Random Encounter** (v5.8) — Invece di cercare con scopo definito, esposizione a conoscenza inattesa: (1) scegliere un dominio MAI esplorato in sessioni precedenti, (2) cercare la scoperta più SORPRENDENTE recente in quel dominio, (3) chiedersi "quale campo DISTANTE sarebbe più trasformato se sapesse di questa scoperta?". La connessione deve attraversare almeno 2 confini disciplinari. Mima la serendipità di sfogliare una biblioteca fisica

### Bridge concepts obbligatori

I bridge concepts sono **obbligatori per ogni target**, non solo per la strategia Swanson. Anche per Anomaly Hunting, Tool Transfer o Scale Bridging, lo Scout deve articolare il meccanismo concreto di connessione (molecole, pathway, strutture matematiche, principi fisici). Questo forza un ragionamento più strutturato e dà al Generator un punto di partenza più ricco rispetto a una semplice coppia di campi.

### Strategy diversification + exploration slot

Dei 3 target selezionati, almeno 2 devono usare strategie diverse e almeno 1 deve usare una strategia non utilizzata nelle ultime 2 sessioni (verificato tramite discovery-log). Questo previene il path-lock strategico: le strategie meno usate non sono necessariamente peggiori — sono meno esplorate.

**Exploration slot** (v5.8): Almeno 1 dei 3 target DEVE usare una strategia con meno di 2 sessioni di dati primari. Questo impedisce al pipeline di convergere sempre sulla strategia con il miglior QG pass rate (es. network_gap_analysis al 39%) a scapito di strategie più creative ma meno testate.

### Rotating creativity constraint (v5.8)

L'Orchestratore assegna allo Scout un vincolo creativo diverso ad ogni sessione (rotazione mod 5): ponte cross-disciplina, ponte matematico/formale, gap temporale >50 anni, tool transfer, unsolved problem. Questo forza lo Scout a esplorare territori che altrimenti eviterebbe, impedendo la convergenza verso zone "safe".

### Knowledge persistence cross-sessione

Prima di iniziare l'esplorazione, lo Scout consulta `knowledge/discovery-log.json` per:
- Evitare ri-esplorazioni di coppie già investigate
- Riutilizzare bridge concepts che si sono dimostrati produttivi
- Non rigenerare ipotesi già uccise in sessioni precedenti

Consulta anche `knowledge/meta-insights.md` (se esiste) per:
- Prioritizzare strategie e bridge type con survival rate più alto
- Evitare pattern che producono consistentemente ipotesi uccise
- Calibrare la selezione con metriche quantitative accumulate dal Session Analyst

---

## Il Critic: 9 attack vectors

Il Critic è genuinamente adversariale. Il suo obiettivo è distruggere le ipotesi deboli — uccidere il 50-70% è normale e salutare.

1. **Novelty Kill** — WebSearch per verificare se la connessione è già pubblicata
2. **Mechanism Kill** — Plausibilità fisica/chimica/biologica: scale di energia, tempi, concentrazioni
3. **Logic Kill** — Correlazione spacciata per causazione, analogia confusa con relazione strutturale, ragionamento post-hoc
4. **Falsifiability Kill** — Se non può essere provata falsa → KILL
5. **Triviality Kill** — Un dottorando di ciascun campo direbbe "ovviamente"?
6. **Counter-Evidence Search** — WebSearch obbligatorio per contraddizioni e fallimenti del meccanismo proposto
7. **Groundedness Attack** — Per ogni claim fattuale: è dalla letteratura (grounded)? dalla conoscenza parametrica (verifica con web search)? pura speculazione (flag)? Se >50% dei claim è inverificabile → downgrade significativo
8. **Hallucination-as-Novelty Check** — Per ipotesi con alta novelty: "Sembra nuova perché è genuinamente inesplorata, o perché è sbagliata in modi non ovvi?" Verifica via web search che il meccanismo bridge esista indipendentemente dall'ipotesi. Se la novelty dipende interamente da un claim fattuale inverificabile → la "novelty" è probabilmente un artefatto di conoscenza parametrica incorretta → KILL o downgrade severo
9. **Claim-Level Fact Verification** — Web search OGNI claim [GROUNDED] individualmente. Verifica citation specificity (author+year+journal), directionality, compartimento, proprietà proteiche. Citation hallucination o protein property fabbricata = KILL automatico. Questo attack vector affronta il failure mode più critico emerso dalle prime sessioni: claim meccanistici fabbricati che suonano plausibili e specifici

### Minimum adversarial standard e META-CRITIQUE

Un kill rate dello 0% è un red flag. Se il Critic passa tutte le ipotesi, deve ri-esaminarle chiedendosi "Sto essendo troppo generoso?". Un kill rate sano è 30-50%; sotto il 15% indica pressione adversariale insufficiente.

La v5.1 estende questo in una META-CRITIQUE completa: dopo tutti gli attacchi, il Critic (1) calibra il proprio kill rate, (2) per ogni SURVIVES scrive la ragione più forte per cui avrebbe dovuto essere ucciso, (3) verifica di aver eseguito web search per ogni ipotesi. Inoltre, quando un meccanismo è troppo vago, il Critic scrive **critic_questions** nello state JSON, che l'Orchestratore inoltra al Generator nel ciclo 2 — feedback bidirezionale indiretto.

L'attack vector #8 affronta un rischio documentato dallo studio Science/AAAS: la novelty AI-generated crolla dopo test sperimentali (da 5.38 a 3.41 su 10). Le ipotesi possono sembrare nuove solo perché sono sbagliate. L'hallucination-as-novelty check complementa il Groundedness scoring (che misura il supporto evidenziale complessivo) con un check specifico sulla relazione inversa novelty↔correttezza.

---

## Il Ranker: 6 dimensioni

| Dimensione | Peso | Descrizione |
|---|---|---|
| **Novelty** | 20% | Connessione inesplorata? (richiede web search per verificare) |
| **Mechanistic Specificity** | 20% | Quanto concreto è il meccanismo proposto? |
| **Cross-field Distance** | 10% | Quanto lontani sono i campi connessi? |
| **Testability** | 20% | Verificabile con metodi/dati esistenti? |
| **Impact: Paradigm** | 5% | Se vera, quanto cambia la comprensione? |
| **Impact: Translational** | 5% | Se validata, quanto direttamente suggerisce un'applicazione reale? |
| **Groundedness** | 20% | I componenti dell'ipotesi sono supportati da evidenze retrievable? |

Composito = media pesata. I pesi delle 6 dimensioni sono **canonici e immutabili** — evidenziati in grassetto nella definizione dell'agente per evitare drift tra cicli.

### Cross-domain creativity bonus (v5.8)

Dopo il calcolo del composito pesato, si applica un bonus di **+0.5** al punteggio composito per ipotesi che attraversano 2+ confini disciplinari (es. materials science → neuroscience, topology → developmental biology, information theory → genetics). Il bonus compensa la penalizzazione sistematica dell'infrastruttura bio-centrica: le ipotesi non-biomediche ricevono scores strutturalmente più bassi su Testability e Groundedness perché PubMed/KEGG/STRING sono bio-specifici, non perché le ipotesi siano più deboli. I pesi delle dimensioni individuali restano immutabili; il bonus opera sul composito finale.

### Impact-aware prioritization (v5.14)

Impact decomposto in due sotto-dimensioni (peso totale invariato al 10%):
- **Paradigm impact (5%)**: Quanto cambia la comprensione se vera? (apre un nuovo campo = 10)
- **Translational impact (5%)**: Quanto direttamente suggerisce un'applicazione reale? (drug target/diagnostica = 10, puramente accademico = 1)

L'impatto entra nella pipeline come **segnale parallelo**, mai come sostituto della qualità:
1. **Scout**: campo `impact_potential` (1-10) per target, con check nel TARGET QUALITY CHECK (almeno 1 target >= 6)
2. **Target Evaluator**: 5° asse informativo (non nel composite), usato come tiebreaker dall'Orchestrator
3. **Orchestrator**: impact tiebreaker in Phase 0c (tra candidati a pari disjointness) e Phase 0d (dentro il pool DISJOINT)
4. **Ranker**: Impact decomposto in paradigm + translational (tabella di scoring con 2 sotto-righe)
5. **Quality Gate**: annotazione informativa (application pathway, applied domain, validation horizon) — NON influenza PASS/FAIL
6. **Session Analyst**: nuova categoria impact metrics, traccia correlazione impact-qualità cross-sessione

**Impact Potential Score (IPS)**: score composito calcolato dall'Orchestrator dopo EES:
- `IPS = scout_impact_potential × 0.4 + (convergence_signal_count / 3 × 10) × 0.6`
- Convergence signals = clinical trials + grants + patents trovati dal Convergence Scanner (v5.13)
- Se Convergence Scanner non ha girato: `IPS = scout_impact_potential` (fallback)
- Riportato in ingest.json e session summary accanto a QG composite e EES

**Tensione disjointness-impatto risolta**: domini ad alto impatto (cancer, antibiotici) sono spesso PARTIALLY_EXPLORED. L'impatto opera **solo dentro il pool DISJOINT** come tiebreaker — il disjointness hard constraint (87% vs 30% pass rate) resta intatto.

### Formato di scoring obbligatorio

Il Ranker DEVE produrre una tabella per-dimensione per **ogni** ipotesi con giustificazioni di almeno 2 frasi per dimensione. L'output thin (senza scoring individuale dettagliato) viene bloccato dal `ranker-stop-gate.py` che impone un minimo di 3KB per `ranked-cycle{N}.md`.

### Diversity check

Dopo il ranking, il Ranker esamina le top-5 ipotesi. Per ogni coppia valuta: condividono lo stesso bridge mechanism? (ridondante) Connettono gli stessi subcampi? (convergente) Fanno lo stesso tipo di predizione? (monotono) Se 3+ delle top-5 sono concettualmente simili, la più alta rimane e la successiva ipotesi dissimile viene promossa. Questo previene il problema documentato da Si et al. (2024) dove le idee LLM-generated saturano in diversità. Il diversity constraint opera anche nell'Evolver — doppio livello di protezione.

### Elo tournament sanity check

Dopo il ranking lineare, il Ranker confronta ogni coppia di top-6 ipotesi (15 confronti): "Quale di queste due un ricercatore vorrebbe testare prima, e perché?" Il ranking Elo viene confrontato con il ranking lineare. Ispirato da Google AI Co-Scientist, che usa Elo tournament ranking per correlazione migliore con valutazioni esperte.

Non è un override: il ranking lineare resta l'output primario. Le discrepanze sono segnali diagnostici — indicano dimensioni implicite catturate dal confronto diretto ma non dalla media pesata a 6 dimensioni.

---

## Ottimizzazione di dominio: life sciences come dominio primario

### Perché le life sciences

MAGELLAN è strutturalmente ottimizzato per la scoperta cross-disciplinare nelle life sciences. Non è una scelta arbitraria — tre fattori convergono:

1. **Frammentazione strutturale** — Le life sciences sono il dominio con la più alta densità di "missing links" latenti. Sotto-discipline come microbioma, cronobiologia, epigenetica, immunologia e neuroscienze operano con letterature largamente disgiunte nonostante meccanismi molecolari condivisi. Questo è esattamente il terreno dell'Undiscovered Public Knowledge di Swanson.

2. **Infrastruttura di retrieval disponibile** — PubMed (38M+ articoli con abstract strutturati), KEGG (pathway metabolici e di segnalazione), STRING (interazioni proteiche) forniscono grounding strutturato e query programmatiche. Nessun equivalente comparabile esiste per fisica teorica o matematica pura (arXiv non ha API di query semantica; INSPIRE-HEP e MathSciNet non sono integrati come MCP server).

3. **Falsificabilità rapida** — Le ipotesi biomediche cross-disciplinari sono testabili con esperimenti wet-lab o analisi computazionali su dataset esistenti (GEO, TCGA, UK Biobank). Le ipotesi in fisica teorica o matematica spesso richiedono anni di sviluppo formale prima di poter essere valutate.

### I tre bias strutturali

Il pipeline presenta tre bias non indipendenti che favoriscono le life sciences:

| Livello | Bias | Impatto |
|---|---|---|
| **Retrieval** | PubMed, KEGG, STRING sono tutti bio-specifici. Nessun MCP server equivalente per arXiv, INSPIRE-HEP, MathSciNet | Le ipotesi non-bio hanno contesto letterario più debole → Groundedness più basso |
| **Scoring** | Testability (20%) + Groundedness (20%) + Mechanistic Specificity (20%) = **60% del peso** favorisce scienze sperimentali con database strutturati | Ipotesi in fisica/matematica pura ricevono scores strutturalmente più bassi su 3 delle 6 dimensioni |
| **Format** | Template ipotesi, esempi few-shot (Generator, Critic, Ranker, Evolver) usano linguaggio molecolare/pathway | Il Generator tende a produrre ipotesi formulate in termini di meccanismi biologici anche quando il target è cross-domain |

Questi bias non sono difetti da correggere — sono conseguenze naturali dell'infrastruttura disponibile e del fatto che le life sciences sono il dominio con più opportunità di discovery latente. I pesi delle 6 dimensioni del Ranker restano **canonici e immutabili**, ma un bonus cross-domain di +0.5 (v5.8) compensa parzialmente il bias infrastrutturale per ipotesi che attraversano 2+ confini disciplinari (vedi sezione "Cross-domain creativity bonus" sopra).

### Guida all'interpretazione degli scores

Gli scores di ipotesi non-bio **non sono direttamente comparabili** con quelli bio:

- Un'ipotesi in fisica teorica con score composito 5.5 può essere qualitativamente equivalente a un'ipotesi biomedica con score 7.0
- Il gap è principalmente su Testability (mancanza di dataset pubblici per validazione rapida), Groundedness (nessun MCP server per retrieval strutturato), e Mechanistic Specificity (meccanismi formali vs. molecolari)
- Le dimensioni Novelty, Cross-field Distance e Impact (v5.14: decomposta in Paradigm + Translational) sono relativamente domain-agnostiche

Le ipotesi cross-domain con componente bio (es. "topological defects in active matter ↔ stem cell niche organization") beneficiano parzialmente dell'infrastruttura di retrieval e ottengono scores intermedi.

### Roadmap futura per estensione multi-dominio

Per supportare altri domini con qualità comparabile servirebbero:

- **arXiv API / Semantic Scholar per fisica** — MCP server per query strutturate su preprint di fisica e matematica
- **Simulation validation** — Per fisica teorica, la "testabilità" potrebbe includere simulazioni numeriche come proxy di esperimenti
- **Database materiali** — Materials Project, AFLOW per ipotesi in scienza dei materiali
- **Pesi adattivi per dominio** — Profili di scoring domain-specific (es. ridurre peso Testability per matematica, aumentare Formal Rigor)
- **Few-shot multi-dominio** — Esempi nel Generator/Critic/Ranker che coprono diversi stili di ipotesi

Queste estensioni non sono pianificate per v5.4. L'architettura le supporterebbe senza modifiche strutturali al pipeline.

---

## Structured Relationship Map (KG on-the-fly)

Il Generator, prima di produrre ipotesi, costruisce un **Knowledge Graph parametrico on-the-fly** per ciascun campo:
1. Lista 5-10 relazioni chiave (X attiva Y, W inibisce X, Y è analogo a V...)
2. Cerca **nodi condivisi** tra i due campi (stessa molecola/struttura/concetto)
3. Cerca **relazioni analoghe** (A→B in Field A specchia P→Q in Field C)
4. Cerca **relazioni inverse** e **link mancanti** (una relazione in un campo predice una relazione nell'altro non ancora testata)

Questo sfrutta il concetto KG senza infrastruttura KG esterna: l'LLM FA il knowledge graph reasoning internamente — basta chiederglelo esplicitamente nel prompt.

---

## Gestione dello stato: JSON strutturato

Il sistema usa un doppio binario:

- **`results/{session-id}/`** — Tutti gli output per sessione: markdown (*.md) e dati strutturati (*.json) nella stessa directory
- **`state/session.json`** — Indice di coordinamento slim (~3KB): fase, ciclo, status, target, contatori
- **`state/dispatch-log.json`** — Log dei dispatch con timestamp

```json
{
  "session_id": "2026-03-14-abc123",
  "mode": "scout|targeted|open|problem",
  "phase": 0,
  "cycle": 1,
  "status": "running|success|partial|degraded|failed",
  "status_reason": "...",
  "scout_targets": [...],
  "selected_target": {...},
  "literature_context": {...},
  "disjointness_status": "DISJOINT|PARTIALLY EXPLORED|WELL-EXPLORED",
  "papers_retrieved": ["results/papers/zhang2025-atg5.md", "..."],
  "hypotheses": {
    "cycle1": { "raw": [...], "critiqued": [...], "ranked": [...], "evolved": [...] },
    "cycle2": { ... }
  },
  "final": [...],
  "diversity_scores": [...],
  "metadata": {
    "start_time": "...", "model": "opus-4.6",
    "total_hypotheses_generated": 0, "kill_rate": 0,
    "fallback_used": false, "literature_unavailable": false,
    "generation_degraded": false, "web_search_failures": 0,
    "retries_needed": 0,
    "cycle_decision": null,
    "evolver_skipped": false,
    "literature_reinforcement": false
  },
  "progress": {
    "phases_completed": [{"phase": "scout", "outcome": "3 targets", "timestamp": "..."}],
    "current_phase": "generation"
  },
  "health": {
    "scout_targets_found": 3, "hypotheses_generated": 12,
    "survived_critique": 5, "passed_quality_gate": 2,
    "fallback_used": false, "retries_needed": 0,
    "web_search_failures": 0
  }
}
```

Lo stato è diviso in un **indice slim** (`state/session.json`, ~3KB) e **file per-sessione** (`results/{session-id}/*.json` + `results/{session-id}/*.md`). Markdown e JSON vivono nella stessa directory per sessione. Gli agenti ricevono i dati necessari via dispatch prompt dall'Orchestratore — non leggono state files direttamente. Questo previene il bloat dello stato e riduce il consumo di contesto.

Campi chiave:
- **`status`** / **`status_reason`**: Classificazione esplicita dell'esito della sessione con motivazione. Elimina il caso di output silenziosamente vuoti
- **`disjointness_status`**: Risultato della verifica di disgiunzione del Literature Scout. Informa il Generator sulla genuina novità della connessione
- **`papers_retrieved`**: Paper full-text recuperati, salvati in `results/papers/`. Il Generator li legge per ragionamento a livello di meccanismo
- **`progress`**: Timeline delle fasi completate con esito e timestamp. Consultabile via `/status` durante l'esecuzione
- **`health`**: Contatori aggregati per diagnostica rapida
- **`metadata` estesa**: Traccia fallback, degradazione, fallimenti WebSearch, decisioni adattive (`cycle_decision`, `evolver_skipped`, `literature_reinforcement`)

### Timestamp protocol

Per ogni transizione di fase, l'Orchestratore esegue `date -u +%Y-%m-%dT%H:%M:%SZ` via Bash prima e dopo il dispatch. I timestamp non vengono mai scritti da memoria — sempre dal comando `date`. Questo garantisce che i timestamp in `progress.phases_completed` siano reali e verificabili.

### Kill rate

Formula esatta:
- `killed` = conteggio verdetti "KILLED" in TUTTI gli array critiqued (ciclo 1 + ciclo 2)
- `total` = totale ipotesi raw generate in tutti i cicli
- `kill_rate = killed / total * 100`
- `attrition_rate = (total - len(final)) / total * 100`

Entrambi i valori vengono riportati nel session summary e validati dall'`orchestrator-stop-gate.py`.

### Dispatch log

Ogni invocazione di Agent tool viene loggata automaticamente dal `verify-dispatch.py` hook in `state/dispatch-log.json`. A fine sessione, l'orchestrator-stop-gate verifica che tutti gli agenti richiesti (scout, literature-scout, generator, critic, ranker, evolver, quality-gate) siano stati invocati.

---

## Robustezza: guard logic, hooks, session health

Il pipeline deve operare senza supervisione umana. Per evitare degradazione silenziosa (il pipeline procede ciecamente attraverso ogni fase senza verificare l'output), la robustezza opera su tre livelli.

### 1. Guard Logic nell'Orchestratore

Blocchi condizionali dopo ogni fase che verificano l'output. Il flusso è sempre: **verifica → retry → fallback → abort**.

- **Post-Scout**: Se 0 target → retry con soglia più bassa → fallback a 3 target parametrici hardcoded → setta `fallback_used = true`
- **Post-Generation**: Se < 3 ipotesi → blocking hook forza re-esecuzione → retry con tutte le tecniche → degrade gracefully
- **Post-Critique**: Se 0 sopravvissuti → rigenera con meccanismi diversi e claim più conservativi → re-critica → se fallisce due volte: sessione FAILED con causa esplicita

### 2. Blocking Hooks

SubagentStop hooks per-agente che bloccano (exit code 2) quando l'output è insufficiente:

- `scout-stop-gate.py`: blocca se 0 target
- `target-evaluator-stop-gate.py`: blocca se TUTTI i target score < 3
- `generator-stop-gate.py`: blocca se < 3 ipotesi
- `literature-scout-stop-gate.py`: degrada a warning se MCP/web non disponibili; blocca solo se manca il file output principale
- `ranker-stop-gate.py`: blocca se `ranked-cycle{N}.md` < 3KB (previene output thin senza scoring dettagliato)
- `computational-validator-stop-gate.py`: warn-only (mai blocca — l'assenza di dati non è evidenza di assenza)
- `critic-stop-hook.py`: warn-only (il critic può legittimamente uccidere tutto)
- `session-analyst-stop-gate.py`: warn-only (verifica che meta-insights.md sia stato creato)
- `orchestrator-stop-gate.py`: Stop hook che impedisce la terminazione prematura del pipeline + valida kill rate + verifica dispatch log (agenti richiesti condizionali su mode)

Hook aggiuntivi:
- `verify-dispatch.py`: PostToolUse hook su Agent tool — logga ogni dispatch a `state/dispatch-log.json`. L'orchestrator-stop-gate verifica che tutti gli agenti richiesti siano stati invocati
- `PostToolUseFailure`: Traccia fallimenti WebSearch/WebFetch. Dopo 3+ fallimenti lo Scout passa a modo parametric-only
- `PreCompact`: Backup dello stato prima della compaction del contesto
- `PostCompact`: Ripristina da backup se lo stato è corrotto dopo compaction

### 3. Session Health Classification

Ogni sessione termina con uno status esplicito:

- **SUCCESS**: ≥2 ipotesi hanno passato il Quality Gate con Groundedness ≥5
- **PARTIAL**: 1 ipotesi passata, o tutte con bassa Groundedness
- **DEGRADED**: Pipeline completato, 0 passano il Quality Gate (cards presentate con warning)
- **FAILED**: Pipeline non completabile (0 target, tutte uccise, errore agente)

Lo status è la prima riga del `session-summary.md`. Per sessioni FAILED: nessuna hypothesis card, solo causa e azione suggerita.

**Data flow per final.json (v5.15)**: Il quality-gate agent scrive `quality-gate.json` con verdetti, compositi e `summary.session_status`. L'orchestratore poi CREA `final.json` leggendo `quality-gate.json` da disco — mai dalla propria memoria di contesto. Questo previene corruzione da context compression in sessioni lunghe (bug scoperto in S015: orchestratore riportava 4 CONDITIONAL_PASS quando il QG aveva 2 PASS + 4 CONDITIONAL_PASS). Post-enrichment, l'orchestratore verifica che verdetti e compositi in final.json matchino quality-gate.json.

---

## Principi di Prompt Engineering

I prompt degli agenti seguono le best practice 2026 per i modelli frontier. Le scelte sono motivate empiricamente dalle guide ufficiali di Anthropic, OpenAI e Google.

### Struttura e separazione

- **XML tags** (`<goal>`, `<constraints>`, `<strategies>`, `<reflection>`, `<output_format>`): Separano sezioni semantiche in modo non ambiguo. Anthropic: "XML tags help Claude parse complex prompts unambiguously."
- **Role sentences**: Una frase iniziale che definisce il ruolo dell'agente. Focalizza il comportamento senza overhead.
- **Data-top / Task-bottom dispatch**: L'Orchestratore struttura i prompt di dispatch con contesto in alto e istruzioni in fondo. Anthropic: "Put longform data at the top... Queries at the end can improve response quality by up to 30%."

### Calibrazione del linguaggio

- **Riduzione MUST/CRITICAL/MANDATORY**: Opus 4.6 usa adaptive thinking — le istruzioni enfatiche causano overthinking e spreco di token. Le istruzioni normali producono risultati migliori. Eccezione: i guardrail funzionali dell'Orchestratore (anti-inlining) restano invariati.
- **Positive framing**: Istruzioni formulate come azioni da compiere anziché divieti. "Continue autonomously between phases" invece di "Do NOT stop to ask questions."
- **WHY explanations sui constraint**: Spiegare il motivo di un vincolo permette al modello di generalizzare correttamente ai casi limite. Esempio: "bridge concepts required — the Generator uses bridge concepts as seeds, so vague bridges produce vague hypotheses."

### Arricchimento contenutistico

- **Few-shot examples**: Generator (2 esempi: forte + debole), Critic (1 attacco completo), Ranker (1 tabella scoring), Evolver (1 operazione evolutiva). Sia Anthropic ("3-5 examples dramatically improve accuracy") che Google ("Prompts without few-shot examples are likely less effective") lo raccomandano. Esempi sintetici dominio-neutri per non biasare le sessioni future.
- **Reflection loops aggiuntive**: RETRIEVAL QUALITY CHECK per il Literature Scout (verifica completezza MCP, paper count, specificità gap analysis) e EVOLUTION QUALITY CHECK per l'Evolver (verifica genuino miglioramento, duplicazione bridge, coerenza crossover).

### Tuning model-specifico

- **Opus 4.6**: Istruzioni generali anziché step prescrittivi ("general instructions often produce better reasoning than prescriptive plans"). Anti-overengineering: "Select 3 targets and move on" (Scout), "Generate all 6-8 before refining" (Generator). Niente "Think very hard" — l'adaptive thinking decide autonomamente.
- **Sonnet 4.6**: Step sequence esplicita nel Ranker (Sonnet beneficia più di scaffolding). Esempi strutturati come ancora di formato.

### Prompt per modelli esterni

- **GPT-5.4** (`prompts/gpt-validation.md`): Output contract (sezioni obbligatorie per ipotesi), completeness checklist, empty-result recovery, citation grounding esplicito, ricerca Plan→Retrieve→Synthesize.
- **Gemini 3.1 Pro** (`prompts/gemini-deep-think.md`): Behavioral constraints in testa, 1 few-shot example completo, context-first (hypothesis cards in cima, task in fondo), strict grounding ("If you cannot write the formal mapping, do not claim one exists").

---

## Posizionamento nello stato dell'arte (marzo 2026)

### Sistemi comparabili

| Sistema | Architettura | Innovazione Chiave | Status |
|---------|-------------|-------------------|--------|
| **Google AI Co-Scientist** | 6 agenti su Gemini 2.0, ranking Elo a torneo | 3 scoperte validate sperimentalmente (KIRA6/AML, fibrosi epatica, cf-PICIs) | Partnership DOE, 17 National Labs |
| **SciAgents** (MIT) | Ontologist + Scientists + Critic su KG (33K+ nodi) | Cross-disciplinary via graph path sampling | Open source |
| **Kosmos** (FutureHouse) | World model + agenti specializzati | 12h esecuzione, 42K righe codice, 1500 paper | Open source |
| **AI Scientist v2** (Sakana) | Ideation + Tree Search + Paper Gen | Primo paper AI accettato a ICLR 2025 peer review | Open source |
| **POPPER** (Stanford) | Falsification-based con controllo errore Type-I | Comparabile a scienziati umani a 10x velocità | Open source |
| **Virtual Lab** (Nature 2025) | PI agent + scientist agents | 92 nanobody progettati, 2 con binding migliorato | Pubblicato |
| **Aletheia** (DeepMind) | Generator-Verifier-Reviser su Gemini Deep Think | 4 problemi Erdős risolti, ma 68.5% errori su 700 problemi aperti | Interno |

### Come MAGELLAN si differenzia

**Differenziatori unici**:
- **Selezione autonoma del target** (Scout): Quasi tutti gli altri sistemi richiedono obiettivi di ricerca umani. MAGELLAN è tra i pochissimi a decidere autonomamente *cosa esplorare*
- **Groundedness scoring formale** (20%): Non presente come dimensione esplicita in altri sistemi
- **Hallucination-as-novelty check**: Affronta esplicitamente il rischio documentato dallo studio Science/AAAS che la novelty AI-generated crolla dopo test sperimentali
- **Diversity constraint a doppio livello**: Sia nel Ranker che nell'Evolver, mitiga la saturazione documentata da Si et al. (2024)
- **Hook-based autonomy hardening**: Quality gates deterministici via SubagentStop hooks

**Gap noti rispetto allo stato dell'arte**:
- **Nessun Knowledge Graph persistente**: SciAgents dimostra che KG path sampling tra 33K+ nodi trova connessioni che il solo parametric+web search manca. La Structured Relationship Map del Generator è un proto-KG on-the-fly, ma non è persistente né queryable
- **Scoring lineare vs Elo tournament**: Google usa ranking comparativo a coppie che correla meglio con valutazioni esperte
- **Nessuna validazione computazionale**: Virtual Lab e MARS eseguono simulazioni; MAGELLAN si ferma alla validazione letteraria

### Evidenze empiriche chiave

- **FrontierScience Benchmark** (OpenAI, dic 2025): Gap di 52 punti tra task strutturati (77%) e ricerca aperta (25%) — valida la necessità di architetture multi-agente per task open-ended
- **MOOSE-Chem** (ICLR 2025): I LLM codificano "associazioni di conoscenza scientifica latenti non ancora riconosciute dagli umani" — validazione diretta della tesi UPK di MAGELLAN
- **TruthHypo** (IJCAI 2025): I LLM lottano con la generazione di ipotesi veritiere senza supporto di grounding — validazione del paradigma parametric+retrieval
- **Studio Science/AAAS**: Novelty AI-generated crolla dopo test sperimentali (5.38→3.41); la novelty umana cala meno (4.60→3.97). L'AI tende a embellire claim di novelty che non sopravvivono ai test

### Scoperte validate da sistemi AI simili

- **Google AI Co-Scientist + Gemini 2.0**: Vorinostat per fibrosi epatica (validato in lab, pubblicato su *Advanced Science*). Meccanismo di trasferimento genico batterico (pubblicato su *Cell*, confermato dopo 10 anni di ricerca umana)
- **GPT-5 + Ginkgo Bioworks**: 36.000 composizioni per sintesi proteica cell-free, 150.000 data points, riduzione costi del 40%. GPT-5 ha proposto reagenti nuovi che anticipavano ricerche pubblicate non accessibili al modello
- **Aletheia (DeepMind)**: 4 problemi aperti di Erdős risolti autonomamente, 6/10 FirstProof challenge problems
- **FutureHouse Kosmos**: 79.4% accuracy complessiva, ma solo 57.9% su affermazioni di sintesi/interpretazione nuove. Caution: "often goes down rabbit holes"

L'evidenza mostra che:
1. L'architettura multi-agente è il differenziatore — LLM singoli falliscono dove il multi-agente riesce
2. La validazione esterna è essenziale — nessun sistema validato opera senza retrieval
3. La qualità migliore si ottiene con human-in-the-loop per il framing del problema — il che rende l'autonomia totale di MAGELLAN una scommessa più ambiziosa

---

## Strategia multi-modello

### Modelli interni (pipeline MAGELLAN)

| Agente | Modello | Razionale |
|---|---|---|
| Scout, Generator, Critic, Quality Gate, Orchestrator | Claude Opus 4.6 | Ragionamento profondo, creatività cross-disciplinare, valutazione adversariale |
| Literature Scout, Ranker, Evolver | Claude Sonnet 4.6 | Task strutturati e search-intensive, riduzione costi ~30% |

### Modelli esterni (validazione cross-model automatica, v5.6)

| Fase | Modello | API | Razionale |
|---|---|---|---|
| Empirical validation | GPT-5.4 Pro | OpenAI Responses API, `reasoning.effort: "high"`, `web_search_preview` (high), `code_interpreter` | Il più fattuale di OpenAI (33% meno errori vs 5.2), novelty verification grounded via web search, arithmetic verification via code, citation checking, experimental design |
| Structural analysis | Gemini 3.1 Pro | Google GenAI SDK, `thinkingLevel: HIGH`, `codeExecution`, `googleSearch` | ARC-AGI-2 leader, strutture formali, mappature matematiche con verifica computazionale, predizioni quantitative, grounding letterario |

La validazione cross-model è ora **automatica** (v5.6, tool upgrade v5.12): il Cross-Model Validator genera i prompt, chiama entrambe le API in parallelo via `scripts/validate-crossmodel.mjs` con tool attivi (GPT: web search + code interpreter; Gemini: code execution + Google Search grounding), e produce un consensus report. GPT verifica novelty contro la letteratura corrente via web search e controlla aritmetica via code interpreter. Gemini verifica mapping formali computazionalmente via code execution. Richiede `OPENAI_API_KEY` e/o `GEMINI_API_KEY`. Se assenti, genera solo i file di export per validazione manuale (`/export gpt|gemini`).

### Benchmark di riferimento (marzo 2026)
- **Claude Opus 4.6** (feb 2026): GPQA Diamond 91.3%, ARC-AGI-2 68.8%, HLE 53.1% con tools. Time horizon METR: 14h30m. Context: 200K (1M beta)
- **GPT-5.4 / 5.4 Pro** (5 marzo 2026): ARC-AGI-2 73.3% (standard), 83.3% (Pro). SWE-bench ~80%. Context: fino a 1M token. 33% fewer false claims vs GPT-5.2
- **Gemini 3.1 Pro** (feb 2026): GPQA Diamond 94.3%, ARC-AGI-2 77.1%. Deep Think per strutture matematiche

---

## Modi d'uso

| Comando | Modalità | Descrizione |
|---|---|---|
| `/discover` | **Scout Mode (primaria)** | Lo Scout identifica autonomamente i target — zero input umano |
| `/discover [A] × [C]` | Targeted | Per esplorazioni mirate se si vuole testare un'area specifica |
| `/discover [topic]` | Open | Esplorazione da un singolo dominio |
| `/discover solve: [problem]` | Problem-driven | Cerca insight cross-domain per un problema specifico |
| `/discover --context "..."` | Context-enriched | Inietta expertise di dominio nello Scout e Generator |
| `/discover --papers DOI,...` | Paper-seeded | Fornisce paper di riferimento al Literature Scout |
| `/discover --interactive` | Interactive | Pausa dopo lo Scout per approvazione target |
| `/connect <key>` | Contributor | Collega la CLI al profilo web per attribuzione scoperte |
| `/validate [hypothesis]` | Deep Validation | Verifica approfondita post-discovery |
| `/evolve` | Evolution | Altro ciclo evolutivo sulle ipotesi correnti |
| `/export [gpt\|gemini\|both]` | Export | Formatta per validazione cross-model |

### Filosofia dell'autonomia

**`/discover` senza argomenti è la modalità primaria.** L'intero progetto esiste per rispondere alla domanda: "Può un sistema agentico AI trovare autonomamente connessioni scientifiche reali?"

Questo differenzia MAGELLAN da Google AI Co-Scientist (che opera con scientist-in-the-loop) e da FutureHouse Kosmos (che riceve obiettivi di ricerca umani). MAGELLAN è più ambizioso: lo Scout deve decidere autonomamente *cosa è interessante* — una capacità che Demis Hassabis (2026) ritiene sia ancora 5-10 anni lontana per l'AI.

Le modalità targeted/open/problem esistono come alternative per testing e debugging, non come uso primario.

### Modalità per scienziati di dominio

I flag `--context`, `--papers`, e `--interactive` sono progettati per scienziati con competenze di dominio che vogliono **dirigere** la scoperta:

- `--context "I study ferroptosis in hepatocytes"` — Lo Scout usa questa expertise per informare la selezione strategica dei target, senza limitarsi esclusivamente al dominio indicato
- `--papers 10.1038/s41586-024-xxxxx` — Il Literature Scout recupera questi paper per primi e li usa come seed per l'esplorazione della letteratura
- `--interactive` — Dopo che lo Scout produce i target e il Target Evaluator li valuta, il pipeline si ferma e presenta i risultati. Lo scienziato può approvare, selezionare target specifici, o rigettare e ridirezionare

Questo modello preserva l'autonomia del sistema (lo Scout esplora liberamente) aggiungendo la possibilità per l'esperto di **guidare** senza **controllare**. Il valore della serendipity rimane: lo Scout potrebbe trovare connessioni che lo scienziato non avrebbe mai cercato, anche partendo dal suo dominio.

### Contributor connection e attribuzione

Il comando `/connect <mgln_key>` collega la CLI al profilo dell'utente sul [sito MAGELLAN](https://magellan-discover.ai). Ogni sessione `/discover` successiva incorpora la contributor key nei risultati. Quando i risultati vengono pubblicati sul sito, la sessione viene automaticamente attribuita al contributore.

Questo crea un modello di **contributor-owned discovery**: ogni utente usa i propri token Claude per generare scoperte, e queste scoperte sono pubblicamente sue — con profilo, statistiche, e posizione nel leaderboard.

### Cosa rende possibile l'autonomia totale (marzo 2026)

1. **Scout con 10 strategie**: Non sceglie a caso — ha euristiche strutturate (inclusi isomorfismo strutturale e serendipity) per identificare dove la conoscenza non collegata ha la probabilità più alta di nascondersi
2. **Literature Scout parallelo**: Verifica in tempo reale che i target dello Scout non siano già esplorati, fornendo contesto letteratura per arricchire la generazione
3. **Opus 4.6 time horizon 14h30m (METR)**: L'autonomia sostenuta a questo livello è una capability nuova — nessun modello pre-2026 poteva operare in modo coerente su queste durate
4. **MCP servers**: Retrieval strutturato indipendente dal web search generico, riduce fragilità
5. **GPT-5.4 come validatore esterno**: 33% meno errori fattuali rispetto a GPT-5.2, con Deep Research per grounding letterario esaustivo. Riduce il rischio che Claude validi le proprie allucinazioni
6. **Auto Mode (12 marzo 2026)**: Elimina le interruzioni per permessi, permettendo al pipeline di fluire senza intervento
7. **State management via JSON**: Sopravvive alla compaction del contesto, mantenendo coerenza su run di 30-60 minuti

---

## Failure modes e mitigazioni

| Failure mode | Probabilità | Mitigazione |
|---|---|---|
| Scout gravita verso topic popolari (non genuinely underexplored) | Alta | Strategie 7 (Swanson ABC) e 8 (Contradiction Mining) forzano esplorazione non-ovvia. Literature Scout verifica che i target non siano già pubblicati. Discovery-log previene ri-esplorazioni |
| Hallucination cascade (errori si accumulano tra agenti) | Media | Critic con web search obbligatorio. Groundedness scoring. Hallucination-as-novelty check. Cross-model validation con GPT-5.4 |
| Novelty illusoria (sembra nuova perché è sbagliata) | Media | Attack vector #8 del Critic. Studio Science/AAAS: novelty AI crolla da 5.38 a 3.41 dopo test. La triangolazione cross-model riduce il rischio |
| Convergenza delle ipotesi | Media | Diversity check nel Ranker + diversity constraint nell'Evolver — doppio livello |
| Context drift su run lunghi | Media-bassa | State in JSON, non in contesto conversazionale. Ogni agente rilegge lo stato. PreCompact/PostCompact hooks per backup/restore |
| Ipotesi "triviali" travestite da novel | Media | Triviality Kill nel Critic. Web search novelty check. Cross-model validation |
| Rabbit holes (esplorazione di vicoli ciechi) | Media | Cicli adattivi: 1-3 cicli basati sulla qualità. Early complete previene over-processing. Orchestrator ha istruzioni esplicite di procedere |
| Scout produce 0 target | Media | Guard post-Scout: retry con soglia più bassa → fallback a 3 target parametrici hardcoded |
| Generator produce < 3 ipotesi | Media-bassa | Blocking SubagentStop hook (exit 2) forza re-esecuzione. Guard post-Generation: retry con tutte le tecniche → degrade gracefully |
| Critic uccide tutte le ipotesi | Media | Guard post-Critique: rigenera con meccanismi diversi e claim più conservativi → re-critica. Se fallisce due volte: sessione FAILED |
| Pipeline si ferma prematuramente | Media-bassa | Stop hook blocca la terminazione se phase ≠ "complete"/"failed". PostCompact ripristina stato e istruisce la continuazione |
| WebSearch/WebFetch non disponibili | Bassa | PostToolUseFailure hook traccia i fallimenti. MCP servers come canale alternativo. Scout passa a modo parametric-only dopo 3+ fallimenti |
| Output silenziosamente vuoto | **Eliminato** | Session Health Classification: ogni sessione termina con SUCCESS/PARTIAL/DEGRADED/FAILED. Lo status è la prima riga del session-summary.md |
| Orchestratore esegue fasi inline (bypass agenti) | **Eliminato (v5)** | WebSearch/WebFetch rimossi dall'orchestratore, maxTurns=200 (circuit breaker only; sub-agent maxTurns rimossi in v5.11 — stop hooks validano output), direttiva anti-inlining, dispatch log con verifica post-sessione |
| Ranked output thin (senza scoring dettagliato) | **Eliminato (v5)** | `ranker-stop-gate.py` blocca output < 3KB, formato tabella per-ipotesi obbligatorio |
| Literature Scout non salva paper | **Mitigato** | `literature-scout-stop-gate.py` degrada a warning se MCP/web non disponibili; blocca solo se manca il file di output principale |
| Plan mode blocca pipeline autonomo | **Eliminato** | `/discover` chiama ExitPlanMode automaticamente prima di lanciare l'Orchestratore |
| Hook schema invalido causa errori silenziosi | **Eliminato** | Tutti gli hook aggiornati allo schema Claude Code corrente (`"approve"/"block"` non `"allow"`, stdin per PostToolUse, campo `"verdict"` per conteggio kill) |
| Orchestratore si ferma prima del Quality Gate | **Mitigato (v5.11)** | maxTurns=200 (circuit breaker), sub-agent senza limiti turni, Context Efficiency Protocol. Stop hook (`orchestrator-stop-gate.py`) blocca terminazione prematura. State Contract documenta valori terminali esatti (`status: "success"`, `phase: "complete"`). maxTurns rimosso dai sub-agent — stop hooks validano la qualità dell'output, non il conteggio turni |
| File di sessioni diverse si sovrascrivono | **Eliminato** | Ogni sessione scrive in `results/{session-id}/` |


---

## Come valutare i risultati

Dato che l'utente non ha competenza di dominio, il workflow di valutazione è:

1. **MAGELLAN produce ipotesi** → `results/{session-id}/session-summary.md`
2. **Cross-model validation** → `/export gpt` e `/export gemini` → incolla in GPT-5.4 Pro e Gemini Deep Think
3. **Triangolazione**: Se almeno 2 modelli su 3 assegnano alta confidenza e novelty, l'ipotesi è candidata
4. **Expert review**: Le ipotesi candidate vengono presentate a esperti di dominio (professori, ricercatori) per valutazione qualitativa. Questo è il ground truth
5. **Iterazione**: Feedback degli esperti informa le sessioni successive

L'obiettivo non è che ogni ipotesi sia corretta — è che il sistema produca un tasso non-zero di ipotesi genuinely novel e scientificamente valide, misurato tramite expert review.

---

## Validazione empirica (v5.13)

### Il conflitto validazione vs. efficacia

C'è una tensione fondamentale: validare formalmente che MAGELLAN funziona richiederebbe "accecare" il sistema (no web search, solo conoscenza parametrica), ma per massima efficacia serve dargli tutti gli strumenti. La soluzione: separare completamente i due obiettivi.

### Track 1: Arricchimento della pipeline produzione

Due nuovi agenti post-Quality-Gate, NON-BLOCKING, che consultano fonti mai usate dalla pipeline:

**Convergence Scanner**: Cerca segnali di convergenza indipendente su ClinicalTrials.gov (trial attivi), NIH Reporter (grant finanziati), e brevetti. Trova anche conferme parziali di sub-meccanismi usando query diverse dal Quality Gate. CONSTRAINT: deve leggere `quality-gate.md` per non contare paper già trovati come "nuova evidenza".

**Dataset Evidence Miner**: Verifica claim molecolari specifici via `scripts/query-biodata.py` su 5+ API bioinformatiche: Human Protein Atlas (espressione tissutale), GWAS Catalog (associazioni genetiche), ChEMBL (compound-target), UniProt (funzione proteine), PDB/AlphaFold (struttura). DISTINCTION dal Computational Validator: CV opera su bridge concepts pre-generazione, DEM su claim post-generazione.

**Empirical Evidence Score (EES)**: Score parallelo al composite. `EES = dataset_score × 0.55 + convergence_score × 0.45`. Non sostituisce il composite — misura un asse diverso (evidenza empirica vs. qualità del ragionamento).

### Track 2: Holdout Validation Framework

**Il paradosso della retrodiction**: Quality Gate e Critic cercano sul web senza filtro temporale. Se un paper post-cutoff conferma il meccanismo, il QG lo troverebbe e killerebbe l'ipotesi come "not novel" — l'opposto del desiderato. La retrodiction pura dentro la pipeline è problematica.

**Soluzione: Holdout Validation con contamination check post-hoc**:
1. Curiamo scoperte cross-disciplinari pubblicate dopo Maggio 2025 (cutoff Claude)
2. Diamo a MAGELLAN solo `[Field A] × [Field C]` in targeted mode
3. La pipeline gira normalmente (nessun handicap)
4. Dopo, il Holdout Evaluator verifica:
   - **Contamination**: il paper con la "risposta" è stato trovato da qualche agente? (grep DOI/PMID/titolo)
   - **Mechanism similarity**: quanto sono simili le ipotesi MAGELLAN al meccanismo noto?
5. Verdicts: GENUINE_REDISCOVERY (non contaminato + match forte), PARTIAL_REDISCOVERY, ADJACENT_DISCOVERY, CONTAMINATED, MISSED

Questo è più rigoroso dell'accecare perché: preserva il comportamento esatto della pipeline (stai testando il VERO sistema), misura oggettivamente la contaminazione, e un GENUINE_REDISCOVERY è inattaccabile come prova.

### Overlap analysis (design decision)

| Fonte | Usata dalla pipeline? | Usata dal Convergence Scanner? | Usata dal DEM? |
|-------|----------------------|-------------------------------|----------------|
| Web (Google) | Sì (Critic, QG, Scout, Lit) | Solo per patent/grant search | No |
| PubMed MCP | Sì (Literature Scout) | Sì (partial confirmations) | No |
| STRING/KEGG | Sì (Comp. Validator, pre-gen) | No | Solo claim NUOVI |
| ClinicalTrials.gov | **No** | **Sì** | No |
| NIH Reporter | **No** | **Sì** | No |
| Patents (Google) | **No** | **Sì** | No |
| HPA | **No** | No | **Sì** |
| GWAS Catalog | **No** | No | **Sì** |
| ChEMBL | **No** | No | **Sì** |
| UniProt | **No** | No | **Sì** |
| PDB/AlphaFold | **No** | No | **Sì** |

---

## Evoluzione del pipeline

Per la storia completa dell'evoluzione del pipeline con motivazioni, evidenze dal post-mortem delle sessioni, e impatto stimato di ogni modifica, vedi `docs/CHANGELOG.md`.
