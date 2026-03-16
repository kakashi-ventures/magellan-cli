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

| Swanson (1986) | MAGELLAN v4 (2026) |
|---|---|
| Il problema: UPK esiste tra letterature disgiunte | Stesso problema, stessa motivazione |
| Il bridge: concetto B condiviso tra A e C | **Bridge concepts obbligatori** in ogni target dello Scout |
| Il metodo: analisi bibliometrica (MeSH, citazioni) | **Conoscenza parametrica** dell'LLM come lettore universale |
| Rilevamento: co-occorrenze statistiche | **Elicitazione**: Structured Relationship Map, facet recombination, adversarial probing |
| Validazione: ricerca manuale in database | **Retrieval automatico**: Literature Scout + WebFetch + verifica disgiunzione |
| Scala: una coppia A-C per studio, mesi di lavoro | **8 strategie parallele**, 2 cicli evolutivi, 15-45 minuti |

Il modello ABC resta la struttura portante dell'output: ogni ipotesi MAGELLAN ha la forma `Field A → Bridge mechanism → Field C`. La differenza è *come* si arriva al bridge — non con statistiche citazionali, ma con il ragionamento parametrico di un modello che ha già letto entrambe le letterature.

---

## Architettura: 8 agenti, 3 fasi

L'architettura v4 introduce un **Literature Scout** dedicato e un **Diversity Gate**, risolvendo le due lacune critiche della v3: assenza di retrieval sistematico e convergenza delle ipotesi.

```
FASE 1 — ESPLORAZIONE (Agent Teams: parallela)
┌──────────────┐  ┌──────────────────┐
│    Scout      │  │ Literature Scout  │
│ (parametric)  │  │ (retrieval-based) │
│ 6+2 strategie │  │ Semantic Scholar  │
│ → targets     │  │ PubMed, arXiv     │
└──────┬───────┘  └────────┬──────────┘
       └──────────┬────────┘
                  ▼
           Orchestrator
           (merge + select)

FASE 2 — GENERAZIONE & CRITICA (2 cicli)
┌────────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
│  Generator  │──▶│  Critic   │──▶│  Ranker   │──▶│  Evolver  │
│ parametric  │   │ adversar. │   │ 6 dimens. │   │ evolution │
│ + lit.context│  │ + web     │   │ + grounded│   │ + diversit│
└────────────┘   └──────────┘   └──────────┘   └──────┬────┘
       ▲                                              │
       └──────────── ciclo 2 ◀────────────────────────┘

FASE 3 — VALIDAZIONE FINALE
┌──────────────────┐
│  Quality Gate     │
│ (ex Meta-Reviewer)│
│ checklist + score │
│ portfolio-level   │
└──────────┬───────┘
           ▼
    Session Health → results/*.md + state/session.json

LAYER TRASVERSALE — GUARD & HOOKS
┌─────────────────────────────────────────────────┐
│  Post-fase guards (retry → fallback → abort)    │
│  Blocking SubagentStop hooks (exit 2)           │
│  Stop hook (anti-terminazione prematura)        │
│  PreCompact/PostCompact (backup/restore state)  │
│  PostToolUseFailure (tracking WebSearch fails)  │
└─────────────────────────────────────────────────┘
```

### Perché 8 agenti e non 7

La v3 aveva un overlap funzionale tra Critic e Meta-Reviewer. La v4:
- **Elimina il Meta-Reviewer come agente separato** → diventa il Quality Gate integrato nell'Orchestrator
- **Aggiunge il Literature Scout** → retrieval sistematico da database scientifici (Semantic Scholar API, PubMed, arXiv via web search)
- **Aggiunge logica di Diversity Check** nel Ranker → previene convergenza

Agenti v4: Scout, Literature Scout, Orchestrator, Generator, Critic, Ranker (con Diversity + Groundedness), Evolver, Quality Gate (fase finale dell'Orchestrator).

### Differenziazione modelli (v4.3)

Non tutti gli agenti richiedono lo stesso livello di ragionamento:

| Agente | Modello | Razionale |
|---|---|---|
| **Scout** | Opus | Ragionamento profondo per identificare connessioni non ovvie |
| **Generator** | Opus | Creatività cross-disciplinare e costruzione di meccanismi |
| **Critic** | Opus | Valutazione adversariale richiede ragionamento complesso |
| **Orchestrator** | Opus | Coordinamento pipeline, Quality Gate, decisioni strategiche |
| **Literature Scout** | Sonnet | Search-intensive — richiede giudizio su rilevanza, non ragionamento profondo |
| **Ranker** | Sonnet | Task strutturato su 6 dimensioni con pesi fissi |
| **Evolver** | Sonnet | Operazioni evolutive guidate da regole (crossover, mutation, specification) |

Riduzione costi stimata: ~30% rispetto a Opus per tutti. Il ragionamento profondo è riservato agli agenti che ne beneficiano realmente (Scout, Generator, Critic, Orchestrator).

### MCP Servers per retrieval strutturato (v4.3)

Il retrieval via WebSearch/WebFetch è fragile e richiede parsing HTML. MAGELLAN integra MCP servers come fonte primaria per la ricerca bibliografica:

- **Semantic Scholar MCP** (`@xbghc/semanticscholar-mcp`): Search strutturato, metadati autori, reti citazionali, abstract senza parsing HTML
- **PubMed MCP** (`pubmed-mcp`): Letteratura biomedica con termini MeSH, metadata strutturato

Configurazione in `.mcp.json` nella root del progetto. I Literature Scout e gli agenti con accesso web usano i tool MCP come metodo primario, con fallback a WebSearch quando i tool MCP non sono disponibili o restituiscono risultati insufficienti.

Questo risolve il problema del retrieval come single point of failure (R3 nella valutazione dei rischi): i MCP servers forniscono un canale di retrieval indipendente dal web search generico.

---

## Il paradigma ibrido: Parametric Generation + Retrieval Validation

### Cosa dicono le evidenze (marzo 2026)

I modelli frontier (Opus 4.6, GPT-5.2, Gemini 3.1 Pro) ottengono 91–94% su GPQA Diamond — domande PhD-level in biologia, fisica, chimica. Questo è un salto di 55 punti rispetto a GPT-4 (39%, 2023). La conoscenza parametrica è enormemente migliorata.

Tuttavia:
- **AA-Omniscience** (factual recall aperto): il miglior modello raggiunge solo 55% di accuracy
- **Hallucination rate**: 22–48% a seconda del modello e benchmark
- **FrontierScience-Research** (ricerca aperta): GPT-5.2 raggiunge solo 25.3%
- La letteratura scientifica peer-reviewed dietro paywall è largamente assente dai dati di training

### Il compromesso MAGELLAN

La conoscenza parametrica è **il motore generativo** — è dove risiedono le connessioni cross-disciplinari non ovvie. Ma ogni claim fattuale viene verificato tramite retrieval. Il flusso è:

1. **Scout (parametrico)**: Identifica DOVE cercare usando deep reasoning. Produce **bridge concepts obbligatori** — meccanismi specifici che connettono Field A a Field C
2. **Literature Scout (retrieval)**: Verifica che i target non siano già esplorati, trova letteratura recente nei campi target. **Recupera il testo completo dei top 5-10 paper** via WebFetch per sfruttare la finestra da 1M token. Esegue una **verifica di disgiunzione** per confermare che la connessione è genuinamente UPK
3. **Generator (parametrico + contesto letteratura + paper completi)**: Costruisce prima una **Structured Relationship Map** (KG on-the-fly parametrico) per ciascun campo, poi genera ipotesi usando reasoning + contesto + paper completi
4. **Critic (parametrico + web search)**: Attacca ogni ipotesi, cerca counter-evidence via web
5. **Ranker**: Include **Groundedness** come 6ª dimensione di scoring
6. **Evolver**: Opera sulle ipotesi top, con **diversity constraint**
7. **Knowledge Persistence**: A fine sessione, l'Orchestrator aggiorna `knowledge/discovery-log.json` con coppie esplorate, bridge produttivi, ipotesi sopravvissute e uccise — per efficienza cumulativa tra sessioni. Lo Scout riceve istruzione esplicita di leggere il discovery-log prima di iniziare l'esplorazione, per evitare ri-esplorazioni e riutilizzare bridge produttivi

---

## Sfruttamento della finestra da 1M token

Il Literature Scout non si limita più a snippet di ricerca. Per i top 5-10 paper per campo, usa **WebFetch per recuperare il testo completo** e lo salva in `results/papers/`. Il Generator legge questi paper direttamente, ragionando a livello di frase e meccanismo anziché di abstract.

La differenza: "il Campo A studia l'autofagia" vs. "il paragrafo 3.2 del paper di Zhang et al. descrive un pathway ATG5-BECN1 che è strutturalmente analogo al pathway che Smith et al. descrivono nel Campo C, ma con substrati diversi."

## Verifica di disgiunzione (Novelty Sanity Check)

Prima di finalizzare il contesto letteratura, il Literature Scout verifica che la connessione proposta sia genuinamente underexplored:
- Cerca review, survey e meta-analisi che colleghino esplicitamente i due campi
- Classifica il risultato come **DISJOINT** (nessuna letteratura cross-field), **PARTIALLY EXPLORED** (alcune connessioni ma gap nei meccanismi), o **WELL-EXPLORED** (connessione già ampiamente pubblicata)

Questo previene che il pipeline sprechi cicli su connessioni che non sono genuinamente UPK. Un risultato "WELL-EXPLORED" è informazione di alto valore — non un fallimento.

## Structured Relationship Map (KG on-the-fly)

Il Generator, prima di produrre ipotesi, costruisce un **Knowledge Graph parametrico on-the-fly** per ciascun campo:
1. Lista 5-10 relazioni chiave (X attiva Y, W inibisce X, Y è analogo a V...)
2. Cerca **nodi condivisi** tra i due campi (stessa molecola/struttura/concetto)
3. Cerca **relazioni analoghe** (A→B in Field A specchia P→Q in Field C)
4. Cerca **relazioni inverse** e **link mancanti** (una relazione in un campo predice una relazione nell'altro non ancora testata)

Questo sfrutta il concetto KG senza l'infrastruttura KG esterna: l'LLM FA il knowledge graph reasoning internamente — basta chiederglelo esplicitamente nel prompt.

## Knowledge Persistence tra sessioni

L'Orchestrator mantiene un registro strutturato in `knowledge/discovery-log.json`:
- Coppie di campi già investigate e loro esito
- Bridge concepts che si sono dimostrati produttivi
- Ipotesi uccise e relative motivazioni
- Ipotesi sopravvissute

Questo permette allo Scout di evitare ri-esplorazioni, riutilizzare bridge produttivi, e non rigenerare ipotesi già uccise. Il file è consultato all'inizio di ogni sessione.

---

## Lo Scout: 8 strategie (6 originali + 2 nuove)

### Strategie originali (v3)
1. **Recent Breakthrough Radiation** — Implicazioni di scoperte recenti su campi non ovvi
2. **Anomaly Hunting** — Fenomeni riproducibili ma inspiegati
3. **Converging Vocabularies** — Campi che usano terminologia/framework simili senza saperlo
4. **Tool Transfer Opportunities** — Strumenti da Field A applicabili a Field C
5. **Scale Bridging Gaps** — Fenomeni compresi a una scala ma assenti a scale adiacenti
6. **Failed Paradigm Recycling** — Idee abbandonate in un campo che potrebbero funzionare altrove

### Nuove strategie (v4)
7. **Swanson ABC Bridging** — Identificazione sistematica di letterature disgiunte con concetti intermedi condivisi. Metodo fondazionale della Literature-Based Discovery (Swanson 1986). Il Literature Scout cerca sistematicamente "B terms" che compaiono in entrambi i campi A e C senza che A e C si citino reciprocamente.
8. **Contradiction Mining** — Ricerca attiva di contraddizioni nella letteratura come fonti di ipotesi. Ispirata da ContraCrow di FutureHouse. Se due paper in campi diversi affermano cose mutuamente esclusive, la risoluzione della contraddizione spesso rivela una connessione non banale.

### Bridge concepts obbligatori

In v4.2, i bridge concepts sono **obbligatori per ogni target**, non solo per la strategia Swanson. Anche per Anomaly Hunting, Tool Transfer o Scale Bridging, lo Scout deve articolare il meccanismo concreto di connessione (molecole, pathway, strutture matematiche, principi fisici). Questo forza un ragionamento più strutturato e dà al Generator un punto di partenza più ricco rispetto a una semplice coppia di campi.

---

## Il Ranker: 6 dimensioni (5 originali + Groundedness)

| Dimensione | Peso | Descrizione |
|---|---|---|
| **Novelty** | 20% | Connessione inesplorata? (richiede web search per verificare) |
| **Mechanistic Specificity** | 20% | Quanto concreto è il meccanismo proposto? |
| **Cross-field Distance** | 10% | Quanto lontani sono i campi connessi? |
| **Testability** | 20% | Verificabile con metodi/dati esistenti? |
| **Impact** | 10% | Se vera, quanto cambia la comprensione? |
| **Groundedness** | 20% | I componenti dell'ipotesi sono supportati da evidenze retrievable? |

### Hallucination-as-Novelty Check (v4.3)

Lo studio Science/AAAS dimostra che la novelty AI-generated crolla dopo test sperimentali (da 5.38 a 3.41 su 10). Le ipotesi possono sembrare nuove solo perché sono sbagliate. Il Critic include un attack vector dedicato (#8) che affronta questo rischio:

- Per ipotesi con alta novelty, il Critic chiede esplicitamente: "Questa sembra nuova perché è genuinamente inesplorata, o perché è sbagliata in modi non ovvi?"
- Verifica via web search che il meccanismo bridge esista indipendentemente dall'ipotesi
- Se la novelty dipende interamente da un claim fattuale inverificabile su Field A o C, la "novelty" è probabilmente un artefatto di conoscenza parametrica incorretta → KILL o downgrade severo

Questo complementa il Groundedness scoring (che misura il supporto evidenziale complessivo) con un check specifico sulla relazione inversa novelty↔correttezza.

### Diversity Check

Dopo il ranking, il Ranker applica un diversity check: se le top-N ipotesi convergono sullo stesso meccanismo o framing concettuale, ne rimuove alcune a favore di ipotesi più distanti nello spazio delle ipotesi. Questo previene il problema documentato da Si et al. (2024) dove le idee LLM-generated saturano in diversità.

---

## Gestione dello stato: JSON strutturato

La v3 usava solo file markdown nella directory `results/`. La v4 usa un sistema a doppio binario:

- **`results/*.md`** — Output human-readable (hypothesis cards, session summary)
- **`state/session.json`** — Stato strutturato della sessione, leggibile da ogni agente

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
    "retries_needed": 0
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

Questo risolve il problema della perdita di informazioni durante la compaction del contesto. Ogni agente legge e aggiorna `state/session.json` come source of truth, non il contesto conversazionale.

### Campi aggiunti in v4.2 (Deep Grounding)

- **`disjointness_status`**: Risultato della verifica di disgiunzione del Literature Scout (DISJOINT / PARTIALLY EXPLORED / WELL-EXPLORED). Informa il Generator sulla genuina novità della connessione.
- **`papers_retrieved`**: Lista dei paper full-text recuperati via WebFetch, salvati in `results/papers/`. Il Generator li legge per ragionamento a livello di meccanismo.

### Campi aggiunti in v4.1 (Autonomy Hardening)

- **`status`** / **`status_reason`**: Classificazione esplicita dell'esito della sessione (SUCCESS/PARTIAL/DEGRADED/FAILED) con motivazione. Elimina il caso in cui l'utente riceve un summary dall'aspetto completo ma con 0 ipotesi approvate.
- **`progress`**: Timeline delle fasi completate con esito e timestamp. Consultabile via `/status` durante l'esecuzione.
- **`health`**: Contatori aggregati per diagnostica rapida: quanti target trovati, quante ipotesi generate, quante sopravvissute alla critica, quante hanno passato il Quality Gate.
- **`metadata` estesa**: Traccia fallback (target parametrici usati al posto di quelli web-verificati), degradazione (Generator ha prodotto meno del minimo), e fallimenti WebSearch.

---

## Strategia multi-modello (aggiornata marzo 2026)

### Modelli confermati e disponibili
- **Claude Opus 4.6** (feb 2026): GPQA Diamond 91.3%, ARC-AGI-2 68.8%, HLE 53.1% con tools. Time horizon METR: 14h30m. Context: 200K (1M beta).
- **GPT-5.4 / 5.4 Pro** (5 marzo 2026): Modello più recente di OpenAI. Unifica reasoning + coding (da 5.3-Codex) + computer use nativo. 33% fewer false claims vs GPT-5.2, risposte 18% meno propense a contenere errori. Context: fino a 1M token (API/Codex). ARC-AGI-2: 73.3% (standard), 83.3% (Pro). SWE-bench ~80%. Reasoning effort configurabile a 5 livelli. Tool Search riduce il token usage del 47% in workflow tool-heavy.
- **Gemini 3.1 Pro** (feb 2026): GPQA Diamond 94.3%, ARC-AGI-2 77.1%. Deep Think per strutture matematiche.

### Workflow raccomandato (Option B: 2 modelli)

| Fase | Modello | Razionale |
|---|---|---|
| Generation (Scout → Evolve) | Claude Opus 4.6 | Migliore per agentic tool use, time horizon lungo, ragionamento cross-domain |
| Validation | GPT-5.4 (Pro) Deep Research | Il più fattuale di OpenAI (33% meno errori vs 5.2), exhaustive literature search, experimental design |
| Mathematical structures | Gemini Deep Think | ARC-AGI-2 leader (84.6%), strutture formali, 4 problemi Erdős risolti da Aletheia |

### Timeline modelli GPT-5
GPT-5.0 (ago 2025) → 5.1 (ott 2025) → 5.2 (dic 2025) → 5.3-Codex (feb 2026) → **5.4 (5 marzo 2026)**. GPT-5.4 è il modello corrente; 5.2 Thinking sarà ritirato il 5 giugno 2026.

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
- **Groundedness scoring formale** (20%): Non presente come dimensione esplicita in altri sistemi — innovativo rispetto al campo
- **Diversity constraint a doppio livello**: Sia nel Ranker che nell'Evolver, mitiga la saturazione documentata da Si et al. (2024)
- **Hook-based autonomy hardening**: Quality gates deterministici via SubagentStop hooks — pattern unico

**Gap rispetto allo stato dell'arte**:
- **Nessun Knowledge Graph**: SciAgents dimostra che KG path sampling tra 33K+ nodi trova connessioni che il solo parametric+web search manca
- **Scoring lineare vs Elo tournament**: Google usa ranking comparativo a coppie che correla meglio con valutazioni esperte
- **Nessuna validazione computazionale**: Virtual Lab e MARS eseguono simulazioni; MAGELLAN si ferma alla validazione letteraria

### Evidenze empiriche chiave

- **FrontierScience Benchmark** (OpenAI, dic 2025): Gap di 52 punti tra task strutturati (77%) e ricerca aperta (25%) — valida la necessità di architetture multi-agente per task open-ended
- **MOOSE-Chem** (ICLR 2025): I LLM codificano "associazioni di conoscenza scientifica latenti non ancora riconosciute dagli umani" — validazione diretta della tesi UPK di MAGELLAN
- **TruthHypo** (IJCAI 2025): I LLM lottano con la generazione di ipotesi veritiere senza supporto di grounding — validazione del paradigma parametric+retrieval
- **Studio Science/AAAS**: Novelty AI-generated crolla dopo test sperimentali (5.38→3.41); la novelty umana cala meno (4.60→3.97). L'AI tende a embellire claim di novelty che non sopravvivono ai test

---

## Validazione: cosa funziona davvero (evidenze 2025-2026)

### Scoperte validate da sistemi AI simili
- **Google AI Co-Scientist + Gemini 2.0**: Vorinostat per fibrosi epatica (validato in lab, pubblicato su *Advanced Science*). Meccanismo di trasferimento genico batterico (pubblicato su *Cell*, confermato dopo 10 anni di ricerca umana).
- **GPT-5 + Ginkgo Bioworks**: 36.000 composizioni per sintesi proteica cell-free, 150.000 data points, riduzione costi del 40%. GPT-5 ha proposto reagenti nuovi che anticipavano ricerche pubblicate non accessibili al modello.
- **Aletheia (DeepMind)**: 4 problemi aperti di Erdős risolti autonomamente, 6/10 FirstProof challenge problems.
- **FutureHouse Kosmos**: 79.4% accuracy complessiva, ma solo 57.9% su affermazioni di sintesi/interpretazione nuove. Caution: "often goes down rabbit holes."

### Cosa implica per MAGELLAN
L'evidenza mostra che:
1. L'architettura multi-agente è il differenziatore (LLM general-purpose singoli falliscono dove il multi-agente riesce)
2. La validazione esterna è essenziale (nessun sistema validato opera senza retrieval)
3. La qualità migliore si ottiene con human-in-the-loop per il framing del problema

---

## Modi d'uso

| Comando | Modalità | Descrizione |
|---|---|---|
| `/discover` | **Scout Mode (primaria)** | Lo Scout identifica autonomamente i target — zero input umano |
| `/discover [A] × [C]` | Targeted | Per esplorazioni mirate se si vuole testare un'area specifica |
| `/discover [topic]` | Open | Esplorazione da un singolo dominio |
| `/discover solve: [problem]` | Problem-driven | Cerca insight cross-domain per un problema specifico |
| `/validate [hypothesis]` | Deep Validation | Verifica approfondita post-discovery |
| `/evolve` | Evolution | Altro ciclo evolutivo sulle ipotesi correnti |
| `/export [gpt\|gemini\|both]` | Export | Formatta per validazione cross-model |

### Filosofia dell'autonomia

**`/discover` senza argomenti è la modalità primaria.** L'intero progetto esiste per rispondere alla domanda: "Può un sistema agentico AI trovare autonomamente connessioni scientifiche reali?"

Questo differenzia MAGELLAN da Google AI Co-Scientist (che opera con scientist-in-the-loop) e da FutureHouse Kosmos (che riceve obiettivi di ricerca umani). MAGELLAN è più ambizioso: lo Scout deve decidere autonomamente *cosa è interessante* — una capacità che Demis Hassabis (2026) ritiene sia ancora 5-10 anni lontana per l'AI.

Le modalità targeted/open/problem esistono come alternative per testing e debugging, non come uso primario.

### Cosa rende possibile l'autonomia totale (marzo 2026)

1. **Scout con 8 strategie**: Non sceglie a caso — ha euristiche strutturate per identificare dove la conoscenza non collegata ha la probabilità più alta di nascondersi
2. **Literature Scout parallelo**: Verifica in tempo reale che i target dello Scout non siano già esplorati, fornendo contesto letteratura per arricchire la generazione
3. **Opus 4.6 time horizon 14h30m (METR)**: L'autonomia sostenuta a questo livello è una capability nuova — nessun modello pre-2026 poteva operare in modo coerente su queste durate
4. **GPT-5.4 come validatore esterno**: 33% meno errori fattuali rispetto a GPT-5.2, con Deep Research per grounding letterario esaustivo. Riduce il rischio che Claude validi le proprie allucinazioni
5. **Auto Mode (12 marzo 2026)**: Elimina le interruzioni per permessi, permettendo al pipeline di fluire senza intervento
6. **State management via JSON**: Sopravvive alla compaction del contesto, mantenendo coerenza su run di 30-60 minuti

### Failure modes attesi e mitigazioni

| Failure mode | Probabilità | Mitigazione |
|---|---|---|
| Scout gravita verso topic popolari (non genuinely underexplored) | Alta | Strategia 7 (Swanson ABC) e 8 (Contradiction Mining) forzano esplorazione non-ovvia. Literature Scout verifica che i target non siano già pubblicati. |
| Hallucination cascade (errori si accumulano tra agenti) | Media | Critic con web search obbligatorio. Groundedness scoring. Cross-model validation con GPT-5.4. |
| Convergenza delle ipotesi | Media | Diversity check nel Ranker + diversity constraint nell'Evolver. |
| Context drift su run lunghi | Media-bassa | State in JSON, non in contesto conversazionale. Ogni agente rilegge lo stato. PreCompact hook fa backup dello state; PostCompact hook lo ripristina se corrotto. |
| Ipotesi "triviali" travestite da novel | Media | Triviality Kill nel Critic. Web search novelty check. Cross-model validation. |
| Rabbit holes (esplorazione di vicoli ciechi) | Media | 2 cicli max per session. Orchestrator ha istruzioni esplicite di procedere, non approfondire all'infinito. |
| **Scout produce 0 target** | Media | Guard post-Scout: retry con soglia più bassa → fallback a 3 target parametrici hardcoded. |
| **Generator produce < 3 ipotesi** | Media-bassa | Blocking SubagentStop hook (exit 2) forza re-esecuzione. Guard post-Generation: retry con tutte le tecniche → degrade gracefully. |
| **Critic uccide tutte le ipotesi** | Media | Guard post-Critique: rigenera con meccanismi diversi e claim più conservativi → re-critica. Se fallisce due volte: sessione marcata FAILED con causa esplicita. |
| **Pipeline si ferma prematuramente** (compaction, errore agente) | Media-bassa | Stop hook blocca la terminazione se phase ≠ "complete"/"failed". PostCompact ripristina stato e istruisce la continuazione. |
| **WebSearch/WebFetch non disponibili** | Bassa | PostToolUseFailure hook traccia i fallimenti. Scout passa a modo parametric-only dopo 3+ fallimenti. Stato registra `web_search_failures`. |
| **Output silenziosamente vuoto** (worst case v3) | **Eliminato** | Session Health Classification: ogni sessione termina con SUCCESS/PARTIAL/DEGRADED/FAILED. Lo status è la prima riga del session-summary.md. Per FAILED: nessuna hypothesis card, solo causa + azione suggerita. |

### Autonomy Hardening (v4.1)

Il gap più critico della v4 iniziale era la **degradazione silenziosa**: il pipeline procedeva ciecamente attraverso ogni fase senza verificare che l'output fosse valido. L'utente non esperto poteva ricevere un `session-summary.md` dall'aspetto completo ma con 0 ipotesi approvate e nessuna spiegazione.

L'hardening opera su tre livelli:

**1. Guard Logic nell'Orchestratore** — Blocchi condizionali dopo ogni fase che verificano l'output, ritentano con parametri diversi, usano fallback, o abortiscono con causa esplicita. Il flusso è: verifica → retry → fallback → abort.

**2. Blocking Hooks** — SubagentStop hooks per-agente che bloccano (exit code 2) quando l'output è insufficiente:
- `scout-stop-gate.py`: blocca se 0 target
- `generator-stop-gate.py`: blocca se < 3 ipotesi
- `critic-stop-hook.py`: warn-only (il critic può legittimamente uccidere tutto)
- `orchestrator-stop-gate.py`: Stop hook che impedisce la terminazione prematura del pipeline

**3. Session Health Classification** — Ogni sessione termina con uno status esplicito:
- **SUCCESS**: ≥2 ipotesi hanno passato il Quality Gate con Groundedness ≥5
- **PARTIAL**: 1 ipotesi passata, o tutte con bassa Groundedness
- **DEGRADED**: Pipeline completato, 0 passano il Quality Gate (cards presentate con warning)
- **FAILED**: Pipeline non completabile (0 target, tutte uccise, errore agente)

Hook aggiuntivi: `PostToolUseFailure` traccia fallimenti WebSearch/WebFetch, `PreCompact` fa backup dello stato, `PostCompact` ripristina da backup se lo stato è corrotto.

### Come valutare i risultati

Dato che l'utente non ha competenza di dominio, il workflow di valutazione è:

1. **MAGELLAN produce ipotesi** → `results/session-summary.md`
2. **Cross-model validation** → `/export gpt` e `/export gemini` → incolla in GPT-5.4 Pro e Gemini Deep Think
3. **Triangolazione**: Se almeno 2 modelli su 3 assegnano alta confidenza e novelty, l'ipotesi è candidata
4. **Expert review**: Le ipotesi candidate vengono presentate a esperti di dominio (professori, ricercatori) per valutazione qualitativa. Questo è il ground truth.
5. **Iterazione**: Feedback degli esperti informa le sessioni successive

L'obiettivo non è che ogni ipotesi sia corretta — è che il sistema produca un tasso non-zero di ipotesi genuinely novel e scientificamente valide, misurato tramite expert review.
