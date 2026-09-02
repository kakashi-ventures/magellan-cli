# MAGELLAN — Changelog

Storia evolutiva del pipeline. Per la metodologia corrente, vedi `methodology-v5.md`.
Per la reference operativa, vedi `CLAUDE.md`.

---

## v5.35 (fase 5): allineamento del documento pubblico di metodologia (2 settembre 2026)

**Motivazione**: `docs/pdf/methodology.html` — il sorgente del PDF pubblicato — era
l'unico file toccato da v5.33 che la migrazione a Fable 5.1 non aveva mai aggiornato.
Ultimo commit sul file: f0c8fe0. Restava quindi il solo artefatto che dichiarava una
pipeline su Opus 5, ed e' anche quello che leggono i lettori esterni.

**Cosa e' cambiato**:

1. **31 badge `Opus 5` → `Fable 5.1`** nel diagramma dei 15 agenti, nella tabella
   agente/modello/effort e nell'intro. Classe CSS `.badge-opus` rinominata in
   `.badge-model`: un badge di classe "opus" che stampa "Fable 5.1" e' la trappola
   che qualcuno decodifica alle 3 di notte. Colore invariato.

2. **Tabella di ripartizione dell'effort**: `Fable 5.1 · max` per i 7 deep,
   `Fable 5.1 · high` per gli 8 structured.

3. **Bullet di riferimento del modello**: sostituito Opus 5 con Fable 5.1 (1M
   contesto, 128k output, effort `low`–`max` con default `high`, $10/$50 per MTok con
   cache write a $12.50, Covered Model con retention a 30 giorni). Opus 5 resta come
   voce successiva, dichiarato rollback target con la ragione: classificatori
   cyber-only. Intestazione della sezione da "March 2026" a "September 2026".

4. **La frase sul tier split** diceva ancora *"Opus for deep, creative reasoning;
   Sonnet for structured, search-intensive tasks"*. Descriveva l'assetto v4.3–v5.31:
   Sonnet e' uscito dal frontmatter degli 8 agenti structured in v5.31 (99d5a99),
   quando la distinzione deep/structured e' passata dal tier di modello all'effort, e
   dal fallback del Guard Protocol in v5.33. Ora la frase dice "un modello, due tier
   di effort". Cancellata anche `.badge-sonnet`, unica classe CSS senza usi.

5. **Validatori esterni fermi a pre-v5.24/v5.25 in otto punti** (non solo nel box del
   Cross-Model Validator): `GPT-5.4 Pro` → `GPT-5.5 Pro` e `Gemini 3.1 Pro` →
   `Gemini Deep Research Max`, con i dettagli ripresi da `methodology-v5.md` invece
   che riscritti. Rimossa la claim "33% fewer factual errors vs GPT-5.2", specifica
   di GPT-5.4. Gemini 3.1 Pro resta dove e' corretto: modello base di DR Max e voce
   benchmark dei modelli di frontiera.

6. **`docs/methodology-v5.md`**: il box del Computational Validator nello schema
   ASCII diceva ancora `[Sonnet + Bash]`, unica occorrenza sfuggita alla fase 1.
   Ora `[Fable 5.1 + Bash]`, larghezza del box invariata.

**Non toccato, deliberato**: la riga "Frontier models (Opus 5, GPT-5.5 Pro, Gemini
3.1 Pro) score 91–94% on GPQA Diamond" e' identica in HTML e in `methodology-v5.md`.
E' un'affermazione sui modelli di frontiera, non un badge di pipeline; cambiarla in un
file solo produrrebbe drift fra i due.

**Copertura di f0c8fe0**: con questa fase i file toccati da v5.33 sono tutti allineati
a Fable 5.1. Cio' che resta oltre f0c8fe0 e' la validazione end-to-end, che v5.33 non
aveva: una sessione `/discover` completa piu' l'A/B holdout contro Opus 5.

**Da rigenerare a mano**: il PDF distribuito. Nel repo non esiste uno script che lo
produca da `docs/pdf/methodology.html`.

**File modificati**:
- `docs/pdf/methodology.html` -- badge, tabella effort, bullet del modello, frase del tier split, validatori esterni, CSS morto
- `docs/methodology-v5.md` -- schema ASCII del Computational Validator
- `docs/CHANGELOG.md` -- questa entry

---

## v5.36: Riparazione contratti fra agenti (difetti pre-esistenti emersi dall'audit di fase 4) (2 settembre 2026)

**Motivazione**: l'audit per-agente della fase 4 (lettura riga per riga dei 15 file
contro Fable 5.1, piu' i 18 hook, l'orchestratore e `upload-session.mjs`) ha fatto
emergere una serie di difetti di correttezza indipendenti dal modello — sbagliati su
qualunque modello, ma piu' probabili su uno che legge letteralmente. Stanno in un
commit separato dalla fase 4 per la stessa ragione per cui v5.34 era separata da
v5.33: mescolarli renderebbe impossibile attribuire all'A/B una variazione di
qualita'. Nessuno di questi e' un difetto introdotto dalla migrazione.

**Deliverable richiesti che nessuno scriveva** (la classe piu' costosa: il gate
deliverables li segnala MISSING e ri-dispatcha l'agente, che scrive di nuovo un file
con un altro nome):

1. **`computational.json` non esisteva.** Il Computational Validator scriveva solo il
   markdown e `computational_readiness` in `session.json`, ma l'orchestratore legge
   `{results_dir}/computational.json` per il dispatch del Generator, il gate
   deliverables lo richiede, e `upload-session.mjs` lo legge (con fallback su
   `computational-validation.json`, che nessuno scrive nemmeno): la validazione
   computazionale non e' mai arrivata al sito. Ora e' nel contratto dell'agente,
   con verdetto PLAUSIBLE/INCONCLUSIVE/IMPLAUSIBLE per check.

2. **`{results_dir}/meta-insights.json` non esisteva.** Il Session Analyst scriveva
   `session-analysis.md` e `knowledge/meta-insights.md`, mai il JSON di fase. Ma
   l'orchestratore lo legge subito dopo il dispatch e ne ricava la voce di
   `knowledge/discovery-log.json`: il loop di meta-apprendimento leggeva un file
   inesistente. Aggiunto al contratto con le metriche strutturate che
   l'orchestratore inoltra.

3. **`contributor-context.md`** era richiesto dal gate in modalita' guidata e non lo
   scriveva ne' un agente, ne' un comando, ne' uno script. Ora lo scrive
   l'orchestratore dal testo di `--context`: e' anche il record di provenienza della
   licenza CC-BY-4.0.

4. **Nomi dei due markdown post-QG.** Convergence Scanner e Dataset Evidence Miner
   scrivono `convergence-report.md` e `dataset-evidence-report.md` (ed e' quello che
   controllano i rispettivi stop gate); il gate deliverables dell'orchestratore
   chiedeva `convergence.md` e `dataset-evidence.md`. Allineato l'orchestratore agli
   agenti, cioe' ai file che vengono davvero prodotti e che l'upload ha sempre
   pubblicato.

5. **Lo Scout scriveva `results/scout-targets.md`**, senza il segmento
   `{session-id}/` — identico al difetto dell'Evolver corretto in v5.34.

**Contratti di dati sbagliati**:

6. **Il tag `[GROUNDED]`/`[PARAMETRIC]` non era mai richiesto.** E' il difetto piu'
   grave trovato. Critic (vettore 9), Quality Gate (check 2b) e Dataset Evidence
   Miner iterano tutti "su ogni claim taggato `[GROUNDED]`", il DEM legge
   `final-hypotheses.md` "for full tagged text", e il Groundedness score (20% del
   composite) e' il rapporto fra i due tag. Ma il Generator non aveva nessuna
   istruzione di emettere quei letterali: il constraint diceva soltanto "note which
   parts come from parametric knowledge vs literature context", l'output format
   chiedeva un giudizio HIGH/MEDIUM/LOW, e l'esempio di calibrazione non conteneva un
   solo tag. Con lettura letterale il meccanismo esce senza marcatori e i tre
   controlli anti-allucinazione non hanno su cosa operare. Ora il tag inline e'
   dichiarato come contratto (constraint 2), compare nell'output format e l'esempio
   STRONG e' taggato claim per claim.

7. **`CONDITIONAL_PASS` non era definito da nessuna parte.** Orchestratore,
   Convergence Scanner, Dataset Evidence Miner, Cross-Model Validator, Holdout
   Evaluator e `upload-session.mjs` instradano tutti su
   `PASS or CONDITIONAL_PASS`, e il `summary` del Quality Gate deve contenere
   `conditional_pass` e `conditional_pass_ids`. Ma il file del Quality Gate diceva
   "PASS/FAIL" nel GOAL, nei verdetti e nell'output format, e nominava
   `CONDITIONAL_PASS` una volta sola, di passaggio. Un modello letterale non emette
   un verdetto che il suo prompt non prevede: le ipotesi marginali cadevano come
   FAIL. Ora i tre verdetti sono definiti, con il criterio e il limite (un bridge
   non verificabile non e' mai CONDITIONAL_PASS), e i trigger di FAIL automatico
   sono un constraint separato.

8. **Chiavi IPS sbagliate.** L'orchestratore leggeva `clinical_trials_found`,
   `grants_found`, `patents_found`; `convergence.json` li espone come
   `total_trials_found`, `total_grants_found`, `total_patents_found` sotto
   `convergence.aggregate`. Il `signal_count` era quindi sempre 0 e l'IPS collassava
   sul 40% del solo stimato dello Scout. Stessa correzione, per esplicitezza, sul
   punteggio di convergenza dell'EES.

9. **`cross-model.json` non trasportava i dati delle Post-QG Amendments.**
   L'orchestratore scrive la sezione di errata leggendo arithmetic, correzioni di
   citazione e counter-evidence da quel file; lo schema conteneva solo confidenze,
   novelty e raccomandazione. Aggiunti i tre campi, con la distinzione fra
   "controllato, niente trovato" e "non controllato".

10. **Etichette di disgiunzione divergenti.** Il Literature Scout scriveva
    `WELL-EXPLORED` (trattino) mentre l'orchestratore esclude i candidati
    confrontando `WELL_EXPLORED` (underscore), e `knowledge-schema.json` usava
    `PARTIALLY EXPLORED` con lo spazio. Il filtro piu' importante del narrowing
    dipende da un match letterale. Standardizzato sugli underscore in tutti i punti
    del contratto (invariato il vocabolario NOVEL / PARTIALLY EXPLORED / ALREADY
    KNOWN dei prompt di validazione, che e' un'altra cosa).

11. **Un solo nome per il deliverable del Literature Scout.** Scriveva
    `literature-landscape.md` in scout mode e `literature-context.md` in targeted
    mode, ma il gate deliverables richiede il primo in ogni modalita'. Ora e' sempre
    `literature-landscape.md` (l'upload lo mappa comunque sulla sezione
    `literature-context` del sito).

12. **Tre scrittori su `knowledge/discovery-log.json`.** Scout, Literature Scout e
    Orchestratore. Scout e Literature Scout scrivevano prima che l'esito della
    sessione esistesse, e con una forma diversa da `prompts/knowledge-schema.json`:
    la stessa sessione finiva nel log due volte, e quel log e' esattamente cio' da
    cui lo Scout conta "quali strategie nelle ultime 2 sessioni" per i propri
    constraint di diversificazione ed exploration slot. Ora lo scrittore e' solo
    l'Orchestratore, a fine pipeline; i due agenti leggono.

13. **Il Session Analyst leggeva la fonte dati sbagliata.** Il constraint 1 diceva
    "state/session.json (current) + discovery-log.json", ma `session.json` per
    architettura non contiene contenuto di ipotesi: kill reason, composite e verdetti
    stanno nei JSON di fase. Le metriche richieste dai constraint 2 e 3 non erano
    calcolabili dalla fonte indicata. Ora il constraint elenca i file di
    `{results_dir}/`.

14. **Il Target Evaluator leggeva i candidati non filtrati.** Il suo GOAL dice
    "receive the Orchestrator's top 3 pre-filtered candidates", ma le strategie
    dicevano "Read state/session.json for scout_targets", cioe' tutti i 5-6
    candidati, WELL_EXPLORED inclusi, che l'orchestratore aveva appena escluso. E'
    la lettura diretta di stato che v5.34 aveva lasciato "da valutare in un
    passaggio separato". Ora prende i tre dal dispatch prompt e i dettagli da
    `scout.json`.

15. **L'Evolver leggeva "ranked hypotheses from state"**, dove non ci sono mai
    state. Corretto al file di ranking del dispatch prompt (v5.34 aveva corretto il
    lato output dello stesso agente).

**Contraddizioni interne** (due parti dello stesso prompt che dicono cose diverse —
Fable 5.1 non le smussa):

16. **Ranker**: il constraint 7 fissa "una o due frasi per dimensione", le strategie
    chiedevano "2+ sentence justifications" e l'header della tabella diceva
    "Justification (2+ sentences)". Allineati al constraint, che e' la fonte unica.

17. **Scout**: il constraint 4 chiede almeno 3 strategie distinte, la TARGET QUALITY
    CHECK ne chiedeva almeno 2. Allineata a 3. `CLAUDE.md` e `methodology-v5.md`
    riportavano ancora "almeno 2 su 3 target", denominatore pre-v5.34.

18. **Quality Gate**: l'annotazione di impatto era numerata "11." dentro il
    constraint "10-point rubric (ALL required for PASS)", pur dichiarandosi
    informativa. De-numerata.

19. **Critic**: l'esempio di calibrazione mostrava 8 attacchi su 9 (mancava il
    vettore 9, Claim-Level Verification, che il file stesso definisce "the most
    important attack vector"). E' la stessa classe del template ATTACKS corretto in
    v5.33: un modello letterale copia il formato dell'esempio.

**Verificato e trovato in ordine**: l'allowlist MCP dei 4 agenti con retrieval
strutturato (Literature Scout, Critic, Quality Gate, Convergence Scanner) dichiara
ancora sia i pattern `mcp__*` in `tools:` sia `mcpServers:`, coerenti con i nomi in
`.mcp.json` — nessuna regressione del fix piu' importante di v5.33. Nessun recall
suppressor rientrato (il solo filtro temporale rimasto nel Literature Scout e'
quello correttamente circoscritto da v5.33). Contratti di Holdout Evaluator e degli
stop gate per-agente coerenti. Dopo le correzioni, ogni artefatto richiesto dal gate
deliverables ha un produttore dichiarato (verificato programmaticamente).

**Aperto, non corretto perche' non verificabile da qui**: `upload-session.mjs` non ha
alias per `convergence-report` e `dataset-evidence-report`, quindi le due narrative
post-QG arrivano al sito con quelle chiavi. Se `PHASE_ORDER` del frontend attende
`convergence`/`dataset-evidence`, le due sezioni non si sono mai renderizzate e
servono due voci di alias; indovinare il nome canonico da questo repo
rischia di rompere una sezione che funziona, quindi la verifica va fatta in
`magellan-web`.

**Stato di validazione**: correzioni statiche. Contratti verificati incrociando
agenti, orchestratore, stop gate e upload script; hook Python e upload script
ricompilati; `knowledge-schema.json` e `settings.json` riparsati. Il comportamento
end-to-end va confermato nella stessa sessione `/discover` che deve validare la
migrazione a Fable 5.1.

**File modificati**:
- `.claude/agents/computational-validator.md` -- contratto a due file, `computational.json`
- `.claude/agents/session-analyst.md` -- `meta-insights.json`, fonti dati corrette
- `.claude/agents/generator.md` -- tag inline come contratto, output format, esempio taggato
- `.claude/agents/quality-gate.md` -- tre verdetti definiti, trigger di FAIL separati, annotazione impatto de-numerata, constraint rinumerati
- `.claude/agents/scout.md` -- percorso session-scoped, soglia di diversita', discovery-log in sola lettura
- `.claude/agents/literature-scout.md` -- nome unico del deliverable, `WELL_EXPLORED`, discovery-log in sola lettura
- `.claude/agents/target-evaluator.md` -- candidati dal dispatch prompt
- `.claude/agents/evolver.md` -- ranked dal file di fase
- `.claude/agents/ranker.md` -- lunghezza delle giustificazioni allineata
- `.claude/agents/critic.md` -- vettore 9 nell'esempio
- `.claude/agents/cross-model-validator.md` -- campi per le Post-QG Amendments
- `.claude/agents/discovery-orchestrator.md` -- nomi dei markdown post-QG, chiavi IPS/EES, scrittura di `contributor-context.md`
- `prompts/knowledge-schema.json` -- enum di disjointness
- `CLAUDE.md` -- diversificazione strategie, contratto dei tag
- `README.md` -- albero dei risultati (file mancanti)
- `docs/methodology-v5.md` -- diversificazione, etichette di disgiunzione, scrittore della discovery-log
- `docs/CHANGELOG.md` -- questa entry

---

## v5.35 (fase 4): rilevamento dei rifiuti sugli artefatti invece che sulla risposta (2 settembre 2026)

**Motivazione**: l'audit per-agente della fase 4 ha trovato un solo elemento
davvero legato a Fable 5.1; sta qui, separato dai difetti pre-esistenti che lo
stesso audit ha fatto emergere (quelli sono in v5.36, per la stessa disciplina di
attribuzione delle fasi precedenti).

**Il problema**: la Guard Protocol decideva "questo output sembra un rifiuto"
guardando cosa torna dal sub-agente — "nessun output reale, un messaggio esplicito
di rifiuto, o un file vuoto". Su Fable 5.1 il testo che il modello scrive *fra* le
tool call torna come blocco di thinking di progresso, vuoto sotto il default
`omitted`. Le due situazioni diventano quindi indistinguibili dalla lunghezza della
risposta: un agente sano che ha scritto entrambi gli artefatti puo' rispondere
quasi nulla, e un rifiuto puo' arrivare senza nessun messaggio visibile. Con la
regola scritta per i modelli precedenti, il layer 1 (re-dispatch su `model: opus`)
scatta sui falsi positivi e non scatta sui rifiuti silenziosi.

**La correzione**: il discriminante e' il controllo di artefatti che
l'orchestratore ha gia' (Guard Protocol passo 4). JSON di fase E markdown entrambi
assenti = rifiuto, si applica il layer 1. File presenti ma sotto la soglia di fase
= quality miss ordinaria, re-dispatch con guidance. Una risposta breve sopra due
file scritti non e' nessuna delle due.

**Stato di validazione**: statica, come le fasi 1-3. La verifica vera resta quella
gia' in agenda: una sessione `/discover` completa in cui si osservi
`stop_reason: refusal` e si confermi che il re-dispatch su `opus` scatta.

**File modificati**:
- `.claude/agents/discovery-orchestrator.md` -- blocco "Model-refusal fallback"
- `CLAUDE.md` -- "Refusal fallback principle"
- `docs/methodology-v5.md` -- paragrafo "Fallback (safety classifiers)"
- `docs/CHANGELOG.md` -- questa entry

---

## v5.35 (fase 3): harvest di prompting per Claude Fable 5.1 (2 settembre 2026)

**Motivazione**: la fase 1 ha spostato i 15 agenti su Fable 5.1 lasciando fuori di
proposito l'adeguamento dei prompt, calibrati per Opus 5 in v5.33. Questa e' quella
parte. Tenuta separata perche' un A/B possa attribuire una variazione di qualita' al
modello o ai prompt, non a entrambi.

**Cosa e' cambiato davvero** (poco, ed e' il risultato interessante):

1. **Preambolo di dispatch, in coda a ogni prompt di dispatch.** Due frasi, aggiunte
   dall'orchestratore: scrivi il deliverable una volta sola (pianifica nel
   ragionamento, scrivi nell'output), apri con l'esito, dillo in modo letterale
   invece che per metafora, usa struttura dove aiuta la lettura.

   Il primo pezzo e' il comportamento Fable-specifico piu' costoso per questa
   pipeline: a effort `xhigh`/`max` il modello tende a comporre un deliverable lungo
   dentro il ragionamento e poi a riscriverlo come risposta — stesso risultato,
   circa il doppio di token di output e di attesa. Sette agenti girano a `max` e
   tutti e sette scrivono un markdown lungo. Il secondo pezzo inverte la direzione
   rispetto ai modelli precedenti: Fable 5.1 formatta di MENO (meno header e liste)
   e scrive piu' denso, e i deliverable MAGELLAN finiscono pubblicati sul sito.

   Sta in coda al prompt di dispatch e non nei file degli agenti perche' e' li' che
   le istruzioni di stile tengono davvero — la stessa frase nel system prompt del
   sub-agente rende misurabilmente meno.

2. **Retirata la regola "niente scaffolding di verifica" di v5.33.** La guida di
   migrazione a Fable 5.1 dice esplicitamente di TENERE le istruzioni di verifica
   quando si migra: il consiglio di Opus 5 non vale qui. La regola e' quindi
   ritirata, non invertita: non e' stato tolto nient'altro, e i passi rimossi da
   v5.33 non sono stati ripristinati alla cieca — rimetterli senza misura
   contaminerebbe lo stesso A/B per cui questi commit sono separati.

3. **Due difetti di enumerazione corretti.** La SELF-CRITIQUE del Generator era
   numerata 1, 5, 3; i constraint del Target Evaluator saltavano il 5. Su un modello
   che legge letteralmente, un'enumerazione rotta e' un rischio concreto, non un
   refuso estetico.

**Audit di prescrittivita' (l'avvertimento principale della guida): la pipeline lo
precede in larga parte.** La guida avverte che i prompt scritti per modelli
precedenti sono troppo prescrittivi e abbassano la qualita' su Fable 5.1. Misurato
sui 15 agenti: la struttura GOAL/CONSTRAINTS/STRATEGIES gia' enuncia obiettivo e
vincoli invece di elencare passi, e v5.33 aveva gia' portato la densita' di marcatori
enfatici (MUST/CRITICAL/MANDATORY/ALWAYS/NEVER) a 0-2 per sub-agente. Quel che resta
sono guardrail funzionali — "usa lo script", "esegui in background", "il controllo di
contaminazione viene prima del confronto" — cioe' l'eccezione gia' documentata. Non
e' stato riscritto nessun agente: una de-prescrizione di massa senza A/B e'
esattamente cio' che la guida dice di misurare, non di presumere.

**Cercato e non trovato**: linguaggio anti-formattazione ("niente elenchi puntati",
"solo prosa", "nessun header"), che sotto questa guida andrebbe rimosso perche'
Fable 5.1 gia' sotto-formatta. Nessuna occorrenza nei 15 agenti, quindi nessuna
cancellazione.

**Non applicato, con la ragione**:
- *Nudge di batching delle tool call*: la guida lo condiziona a una misura (quota di
  turni con piu' di una tool call) che non abbiamo, e avverte che aggiungerlo alla
  cieca produce chiamate emesse prima dei risultati da cui dipendono.
- *Delega asincrona ai sub-agenti*: e' una modifica al modello di dispatch, non ai
  prompt. Fuori scope di un harvest di prompting.
- *Istruzioni su aggiornamenti di progresso, autonomia e "ansia da contesto"*: gia'
  presenti nell'orchestratore da v5.33 (blocchi "Autonomous Operation" e "Context
  Efficiency"), verificate riga per riga contro il testo della guida. Nessuna
  modifica necessaria.

**Stato di validazione**: come la fase 1, statica. L'effetto del preambolo di
dispatch si misura solo su una sessione reale, confrontando la lunghezza dei
deliverable e i token di output per agente a effort `max`. Da fare nello stesso A/B
raccomandato dopo la fase 1.

**File modificati**:
- `.claude/agents/discovery-orchestrator.md` -- preambolo di dispatch
- `.claude/agents/generator.md` -- numerazione della SELF-CRITIQUE
- `.claude/agents/target-evaluator.md` -- numerazione dei constraint
- `CLAUDE.md` -- principio "Dispatch preamble"
- `docs/methodology-v5.md` -- sezione Model-specific tuning (tre voci nuove, una regola ritirata), voce benchmark Fable 5.1
- `docs/CHANGELOG.md` -- questa entry

---

## v5.35 (fase 1): migrazione della pipeline a Claude Fable 5.1 (2 settembre 2026)

**Motivazione**: la fase 0 ha verificato che la migrazione e' fattibile (ID completo
accettato nel frontmatter, org non bloccata dal vincolo di retention, floor Claude
Code 2.1.257) e la fase 2 ha riparato il layer anti-rifiuto che era rotto dal 30
luglio. Questo commit fa la migrazione vera: cambia il modello primario dei 15
agenti da Claude Opus 5 a Claude Fable 5.1 (`claude-fable-5-1`, rilasciato il 1
settembre 2026).

**Cambiamenti**:

1. **Quindici agenti passano a `model: claude-fable-5-1`.** Si pinna l'ID completo,
   non l'alias `fable`, per la ragione registrata in fase 0: la 2.1.243 ha mantenuto
   `fable` su Fable 5 nelle sessioni gateway, quindi lo stesso alias risolve a
   modelli diversi a seconda del tipo di sessione. E' la stessa classe di bug
   silenzioso che il repo ha gia' subito con `opus`. Il frontmatter accetta gli ID
   completi (verificato in fase 0 via `modelUsage`/`canonicalModel`).

2. **L'orchestratore resta l'eccezione.** Gira sul modello di sessione perche'
   `/discover` lo carica top-level: l'istruzione ora e' `/model claude-fable-5-1`,
   non `/model opus`. Il suo `model:` di frontmatter e' informativo.

3. **Portata dei classificatori: si inverte rispetto alla fase 2.** Su Opus 5
   l'esposizione life-sciences non esisteva (classificatori cyber-only). Fable 5.1
   ne esegue un insieme piu' ampio che include `bio`, la categoria la cui stessa
   documentazione avverte che il lavoro benigno in scienze della vita puo' farla
   scattare. Per una pipeline life-sciences-optimized il layer anti-rifiuto passa da
   precauzionale a portante: e' il costo di merito principale di questa migrazione,
   non un dettaglio.

4. **Bersaglio del layer 1: da `sonnet` a `opus`.** Con un primario Fable-tier,
   `opus` smette di essere circolare e diventa il fallback corretto: Claude Opus 5 e'
   cyber-only, quindi non porta il classificatore che con maggiore probabilita' e'
   scattato, e a differenza di `sonnet`/`haiku` non e' un downgrade di capacita'.
   Resta l'unico alias sensato fra i quattro ammessi dal tool Agent.

5. **Bersaglio del layer 2: da `claude-opus-4-8` a `claude-opus-5`.** Il rollback
   persistente via frontmatter punta ora alla baseline precedente della pipeline.

6. **Floor Claude Code: da 2.1.219 a 2.1.257** (`scripts/version-check-hook.py`),
   la voce che dichiara `claude-fable-5-1` come modello Fable di default. Nota di
   robustezza: con l'ID completo un build vecchio fallisce in modo rumoroso, mentre
   il pin ad alias falliva in silenzio eseguendo il modello sbagliato.

7. **Vincolo operativo nuovo, documentato nei prerequisiti del README**: Fable 5.1 e'
   Covered Model e richiede 30 giorni di retention. Un'org sotto zero data retention
   riceve `400 invalid_request_error` su ogni chiamata e non puo' eseguire la
   pipeline cosi' configurata; il rimedio e' il rollback a `claude-opus-5`, che sotto
   ZDR e' disponibile. Opus 5 non aveva questo vincolo, quindi non poteva essere
   ereditato dal setup precedente.

8. **Costo**: $10/$50 per MTok contro i $5/$25 di Opus 5, cache write $12.50 contro
   $6.25, cache read $0.25. Su 15 agenti che partono ciascuno dal proprio system
   prompt il peso maggiore e' sul cache write, come rilevato in fase 0.

9. **Breaking changes di Fable 5.1 verificati inerti qui**: forced tool use
   (`tool_choice` `any`/`tool`) restituisce 400, i thinking block sono legati al
   modello che li produce, e l'edit di turni precedenti li invalida ("preserved
   thinking"). MAGELLAN non imposta `tool_choice`, `thinking`, `max_tokens` ne'
   parametri di sampling, e la gestione della history e' dell'harness Claude Code.

**Deliberatamente NON in questo commit**: l'harvest di prompting per Fable 5.1. La
sua guida avverte che i prompt scritti per modelli precedenti sono spesso troppo
prescrittivi e abbassano la qualita' dell'output — gli 15 agenti sono stati calibrati
per Opus 5 in v5.33. Tenerlo separato e' la stessa disciplina di v5.34: se l'A/B
mostra una variazione di qualita', dev'essere attribuibile o al modello o ai prompt,
non a entrambi insieme.

**Stato di validazione**: non validata end-to-end. Serve una sessione `/discover`
completa (osservando `stop_reason: refusal` e verificando che il re-dispatch su
`opus` scatti davvero) piu' un A/B `/validate-holdout` contro Opus 5. La cautela di
merito della fase 0 resta in piedi e non e' stata rimossa dalla documentazione:
Anthropic indica questo tier quando gli eval su Opus 5 a effort piu' alto risultano
insufficienti, e MAGELLAN quegli eval non li ha mai eseguiti. L'ultima validazione
end-to-end reale resta su Opus 4.7.

**File modificati**:
- `.claude/agents/*.md` (15 file) -- `model: claude-fable-5-1`
- `.claude/agents/discovery-orchestrator.md` -- modello di sessione, portata dei classificatori, bersagli dei due layer
- `scripts/version-check-hook.py` -- floor 2.1.257, rationale e messaggio
- `scripts/init-session.sh` -- `metadata.model`
- `prompts/validation-prompt-gpt.md` -- attribuzione del modello generatore
- `CLAUDE.md` -- tabella agenti, principio di selezione modello/effort, principio di fallback, pinning per ID completo
- `README.md` -- prerequisiti (floor, `/model`, avviso ZDR), tabella e lista agenti, sezione Architecture
- `docs/methodology-v5.md` -- abstract, diagrammi, tabelle agenti, sezione multi-model, benchmark di riferimento (voce Fable 5.1 aggiunta, Opus 5 ridefinito come bersaglio di rollback)
- `docs/CHANGELOG.md` -- questa entry

---

## v5.35 (fase 2): riparazione del fallback anti-rifiuto e correzione della portata dei classificatori (2 settembre 2026)

**Motivazione**: la fase 0 ha confermato che il layer 1 della mitigazione
anti-rifiuto scritto da v5.33 non puo' eseguire, e la doc di migrazione a Fable 5.1
ha corretto un presupposto di merito su cui v5.33 aveva costruito l'intero
paragrafo. Le due cose si riparano insieme perche' toccano lo stesso testo.
**Entrambe le correzioni valgono sulla baseline attuale (Opus 5) e restano valide
anche se la migrazione a Fable 5.1 non viene fatta.**

**Correzioni**:

1. **Portata dei classificatori: Opus 5 e' cyber-only.** v5.33 affermava che "Opus 5
   runs safety classifiers that can decline biology and life-sciences content" e
   costruiva su questo l'esposizione di sette agenti. L'inferenza veniva dalla
   tabella generale delle categorie di rifiuto, che elenca le categorie esistenti
   ma non la loro attribuzione per-modello. La guida di migrazione a Fable 5.1
   fornisce l'attribuzione esplicita: i classificatori di Fable 5.1 coprono "a
   broader set than **Claude Opus 5's cybersecurity-only classifiers**". Sul
   primario attuale la categoria attesa e' `cyber`, non `bio`: il rischio
   life-sciences descritto dal paragrafo non esiste su Opus 5.

   Il layer resta comunque, per due ragioni: `cyber` puo' scattare su lavoro
   benigno, e l'esposizione rientra per intero se il primario passa a un modello
   Fable-tier. Il testo ora distingue le due situazioni invece di descriverne una
   sola come se valesse sempre.

2. **Layer 1 riparato: il tool Agent accetta solo alias.** Verificato in fase 0 che
   `model: claude-opus-4-8` produce `InputValidationError: expected one of
   "sonnet"|"opus"|"haiku"|"fable"`. Il re-dispatch per-invocazione ora usa
   `model: sonnet`, che e' l'unico alias contemporaneamente non circolare (`opus` e'
   il modello che ha appena rifiutato), non un aumento di copertura dei
   classificatori (`fable` risolve a un modello Fable-tier, che ne porta di piu'), e
   non elencato fra i modelli che eseguono questi classificatori.

3. **L'asimmetria della piattaforma e' ora documentata come tale**: il parametro
   `model` per-invocazione del tool Agent accetta solo i quattro alias, mentre il
   frontmatter degli agenti accetta gli ID completi (entrambi verificati in fase 0).
   Il layer 2 (rollback persistente a `claude-opus-4-8`) e' quindi l'unica via verso
   un modello privo di alias, ed e' una modifica di file, non un'azione di sessione.
   Distinguere i due layer evita che la prossima migrazione ripeta l'errore.

4. **Precisione sulla fatturazione**: v5.33 diceva "a refused request is not
   billed". Vale solo per un rifiuto che arriva prima di qualunque output; un
   rifiuto a meta' stream fattura la parte gia' trasmessa.

5. **Aggiunto che il branch va su `stop_reason`**, mai sui campi interni di
   `stop_details`: `category` ed `explanation` possono essere `null`, ed e' un
   valore normale e permanente, non un placeholder.

**Nessun cambiamento di modello in questo commit.** Il primario resta `opus`
(Claude Opus 5). La fase 1 della migrazione e' separata: quando il primario diventa
Fable-tier, il bersaglio del layer 1 va rivalutato, perche' `opus` smettera' di
essere circolare e diventera' il fallback corretto (Opus 5 e' un target permesso per
Fable 5.1 e non esegue il classificatore `bio`).

**Stato di validazione**: correzioni statiche. Il layer 1 riparato non e' stato
esercitato end-to-end, perche' richiede un rifiuto reale; il difetto che sostituisce
era invece dimostrabile staticamente e lo e' stato.

**File modificati**:
- `.claude/agents/discovery-orchestrator.md` -- blocco "Model-refusal fallback" riscritto: portata per-modello, asimmetria alias/ID, due layer separati, fatturazione
- `CLAUDE.md` -- "Refusal fallback principle" riscritto; nota di validazione allineata a `sonnet`
- `docs/methodology-v5.md` -- paragrafo "Fallback" riscritto in coerenza
- `scripts/version-check-hook.py` -- rationale: `claude-opus-4-8` raggiungibile solo via frontmatter
- `docs/CHANGELOG.md` -- questa entry

---

## v5.35 (fase 0): verifiche preliminari alla migrazione a Claude Fable 5.1 (2 settembre 2026)

**Motivazione**: il 1 settembre 2026 Anthropic ha rilasciato Claude Fable 5.1
(`claude-fable-5-1`), che estende Fable 5 allo stesso prezzo di listino
($10/$50 per MTok) con cache read a $0.25/MTok. Prima di toccare i 15 agenti,
quattro verifiche bloccanti: due riguardano la fattibilita' della migrazione, una
il floor di versione, e una ha fatto emergere un difetto pre-esistente.

**Questo commit non cambia nessun comportamento**: registra soltanto le prove, che
sono il presupposto delle fasi successive. La migrazione vera e' un commit separato.

**Cautela sul merito, prima delle verifiche**: la doc Anthropic raccomanda Opus 5
come default e indica Fable 5.1 per "demanding reasoning and long-horizon agentic
work, **or when your evals on Claude Opus 5 at higher effort still fall short**".
MAGELLAN quegli eval non li ha mai eseguiti: v5.33 chiude ammettendo che Opus 5
non e' validato end-to-end e che l'ultima validazione reale e' su Opus 4.7. La
migrazione raddoppia il costo per token senza la misura che la giustifica, e
sarebbe la terza migrazione non validata in tre mesi. Resta consigliato un
`/validate-holdout` su Opus 5 a effort `max` prima di procedere.

**Verifiche**:

1. **Alias contro ID completo -- si pinna l'ID.** Su Claude Code 2.1.258 e provider
   `firstParty`, sia `fable` sia `claude-fable-5-1` risolvono a `claude-fable-5-1`
   (campo `canonicalModel` in `--output-format json`). L'alias oggi funzionerebbe,
   ma non e' stabile: il changelog di Claude Code 2.1.243 recita "Changed `fable`
   and `best` in Claude apps gateway sessions to keep resolving to Fable 5 for
   now". Lo stesso alias risolve a modelli diversi a seconda del tipo di sessione,
   ed e' esattamente il fallimento silenzioso che v5.33 ha documentato per `opus`.
   Per un repo che gira sulle macchine altrui, l'alias e' la classe di bug, non la
   soluzione.

   **Verificato che il frontmatter dei sub-agenti accetta gli ID completi**: probe
   temporanea con `model: claude-opus-4-8`, dispatch via CLI annidata, `modelUsage`
   riporta due voci distinte (`claude-opus-5` per la sessione padre,
   `claude-opus-4-8` con `canonicalModel: "claude-opus-4-8"` per il sub-agente). Il
   sub-agente ha davvero girato sul modello dichiarato nel frontmatter. La fase 1
   usera' quindi `model: claude-fable-5-1`, non `model: fable`.

2. **Zero data retention: nessun blocco.** Fable 5.1 richiede 30 giorni di
   retention, e' designato Covered Model e non e' disponibile sotto ZDR se non con
   autorizzazione esplicita di Anthropic; un'org ZDR riceve `400
   invalid_request_error` su ogni chiamata. Opus 5 invece e' disponibile sotto ZDR,
   quindi questo vincolo e' nuovo e non poteva essere ereditato. Due chiamate di
   prova a `claude-fable-5-1` sono andate a buon fine: l'org non e' bloccata.

3. **Floor Claude Code: 2.1.257.** Fable 5.1 entra come opzione in 2.1.240; la
   2.1.257 e' la voce che dichiara "Added Claude Fable 5.1 (`claude-fable-5-1`), now
   the default Fable model". Il floor attuale del repo e' 2.1.219 (alzato da v5.33).
   Versione locale di sviluppo: 2.1.258.

4. **Difetto pre-esistente confermato: il fallback anti-rifiuto di v5.33 non puo'
   eseguire.** Il parametro `model` del tool Agent accetta soltanto i quattro alias.
   Verificato empiricamente:

   ```
   InputValidationError: expected one of "sonnet"|"opus"|"haiku"|"fable"
       path: ["model"]
   ```

   L'istruzione scritta da v5.33 -- "re-dispatch the SAME agent ONCE with `model:
   claude-opus-4-8`. Use the full model ID, not an alias" -- fallisce in validazione
   prima di partire. Il **layer 1** della mitigazione anti-rifiuto e' quindi non
   funzionante dal 30 luglio 2026. Il **layer 2** (rollback persistente via
   frontmatter con ID completo) funziona, come dimostrato dalla verifica 1.

   L'asimmetria e' precisa e vale la pena fissarla: **il frontmatter accetta gli ID
   completi, il parametro per-invocazione del tool Agent accetta solo i quattro
   alias**. Correzione in fase 2.

**Dati raccolti di passaggio** (rilevanti per i budget di lunghezza e per il costo):
- Claude Code espone `contextWindow: 1000000` ma `maxOutputTokens: 64000`, cioe'
  meta' dei 128K che l'API dichiara per Fable 5.1.
- Il cache write di Fable 5.1 e' $12.50/MTok contro i $6.25 di Opus 5. Una chiamata
  banale con 9.6K token di cache creation e' costata $0.195. Su 15 agenti che
  partono ciascuno da un system prompt proprio, il raddoppio pesa soprattutto sul
  cache write, non sugli input.

**Conseguenza sul piano**: la fase 2 (fallback anti-rifiuto) va riscritta piu' a
fondo del previsto, perche' deve sostituire un meccanismo che non valida, non solo
aggiornarne il bersaglio.

**File modificati**:
- `docs/CHANGELOG.md` -- questa entry

---

## v5.34: Riparazione contratti fra agenti (difetti pre-esistenti emersi dall'audit v5.33) (30 luglio 2026)

**Motivazione**: l'audit per-agente condotto per la migrazione a Opus 5 ha fatto emergere una serie di difetti di correttezza che NON dipendono dal modello: sono sbagliati su qualunque modello, ma la maggiore letteralita' di Opus 5 li rende piu' probabili. Sono tenuti in un commit separato da v5.33 di proposito: mescolarli alla migrazione renderebbe impossibile attribuire al modello un'eventuale variazione di qualita' nell'A/B.

**Difetti corretti**:

1. **L'Evolver non produceva nessuno dei due artefatti che la pipeline consuma.** Il constraint diceva di scrivere `results/evolved-cycle{N}.md` (senza il segmento `{session-id}/`) e di aggiornare `state/session.json`; `cycle{N}-evolved.json` non era mai nominato. Ma l'orchestratore lo legge (righe 442 e 470) e il deliverables gate lo richiede esplicitamente (riga 672). Ora il constraint dichiara entrambi i file sotto `{results_dir}/`.

2. **`subagent-stop-hook.py` avvisava su chiavi che nessuno scrive.** I controlli per critic, ranker ed evolver cercavano `hypotheses.cycle{N}.{critiqued,ranked,evolved}` dentro `session.json`, che per architettura non contiene mai contenuto di ipotesi (verificato: l'orchestratore non scrive quella chiave). Riscritti per verificare i file effettivi in `{results_dir}/`, cioe' la stessa fonte che legge l'orchestratore.

3. **Loop di feedback bidirezionale rotto silenziosamente.** `critic.md` diceva di scrivere `critic_questions` in `state/session.json`, mentre il constraint 5 dello stesso file e l'orchestratore (riga 437) usano `{results_dir}/cycle{N}-critiqued.json`. Con la lettura letterale le domande non arrivavano mai al Generator nel ciclo 2, e il principio di design documentato falliva senza errori.

4. **Critic, conteggio dei vettori**: il GOAL diceva "all 8 attack vectors", il constraint 1 dice 9. Corretto a 9 (gia' in v5.33, perche' era prerequisito del fix sul template ATTACKS).

5. **Critic, tre soglie di kill rate incompatibili**: constraint 4 "30-50% sano, sotto 15% insufficiente" contro constraint 6 "50-70% e' normale e sano". Un tasso del 55% era simultaneamente fuori banda e normale. Ora il constraint 4 e' l'unica fonte.

6. **Quality Gate, rubrica 9 contro 10**: il `description` del frontmatter diceva "9-point rubric" mentre GOAL, constraint 1 e la tabella dicono 10.

7. **Quality Gate, verdetti duplicati in `session.json`**: il constraint chiedeva di scriverli sia li' sia in `quality-gate.json`. Ma il flusso documentato e' che l'orchestratore costruisce `final.json` leggendo `quality-gate.json` DA DISCO, proprio per non fidarsi della memoria conversazionale. Ora l'agente aggiorna solo il contatore `health.passed_quality_gate`, che e' l'unico campo letto da `orchestrator-stop-gate.py`.

8. **Scout, denominatore sbagliato nelle quote**: i constraint 6 e 11 dicono 5-6 candidati, ma GOAL, constraint 4, 4b e la riga 180 dicevano 3. Le quote di diversita' ed exploration slot erano quindi espresse contro il numero sbagliato ("almeno 2 strategie diverse su 3" applicato a un pool di 6 e' molto piu' debole). Allineato tutto a 5-6, con la riduzione a 3 dichiarata come lavoro dell'Orchestratore.

9. **`maxTurns` documentato in modo scorretto**: `CLAUDE.md` diceva 200, il frontmatter dice 500, e al top-level il valore di frontmatter e' comunque informativo. Ora la doc descrive il comportamento reale invece di scegliere un numero.

**Non corretto (deliberato)**: `scout.md` continua a scrivere `scout_targets` in `session.json`. Non e' una violazione: sono metadati di coordinamento, non contenuto di ipotesi, e `scout-stop-gate.py` legge esattamente quel campo. Restano da valutare in un passaggio separato le letture dirette di `session.json` da parte di target-evaluator, convergence-scanner, session-analyst e dataset-evidence-miner, che sono in tensione con il principio "gli agenti ricevono i dati dal dispatch prompt" ma non sono rotte.

**Stato di validazione**: correzioni statiche verificate (hook Python parsano, contratti di file coerenti fra agente, orchestratore e gate). Il comportamento end-to-end va confermato nella stessa sessione `/discover` che valida v5.33.

**File modificati**:
- `.claude/agents/evolver.md` -- contratto di output a due file sotto `{results_dir}/`
- `.claude/agents/critic.md` -- percorso di `critic_questions`, banda di kill rate unica
- `.claude/agents/quality-gate.md` -- rubrica 10 punti nel description, solo contatore health in state
- `.claude/agents/scout.md` -- quote allineate a 5-6 candidati
- `scripts/subagent-stop-hook.py` -- controlli critic/ranker/evolver su file reali invece che su chiavi di state inesistenti
- `CLAUDE.md` -- descrizione corretta di `maxTurns`
- `docs/CHANGELOG.md` -- questa entry

---

## v5.33: Migrazione pipeline a Claude Opus 5 + harvest prompting + ripristino accesso MCP (30 luglio 2026)

**Motivazione**: il 24 luglio 2026 Anthropic ha rilasciato Claude Opus 5 (`claude-opus-5`, alias `opus`). Tre ragioni per adottarlo come default al posto di Fable 5: (1) **costo dimezzato**, $5/$25 per MTok contro $10/$50, restando entro lo 0,5% del picco di Fable 5 su CursorBench 3.2 a effort max; (2) **guadagni proprio nel dominio di MAGELLAN** rispetto a Opus 4.8: chimica organica +10,2pp, predizione proteica +7,7pp, genomica descritta come "more like a careful scientist than any model"; (3) **coordinamento multi-agente** citato come miglioramento di punta (pattern writer-verifier, pochi casi di agenti che si sovrascrivono). La superficie API e' invariata (adaptive-thinking-only, niente parametri di sampling, niente prefill), quindi nessuna modifica di codice.

**Le due breaking change di Opus 5 sono inerti qui** (verificato, non assunto): thinking ON di default puo' troncare `max_tokens` stretti, e `thinking: disabled` con effort `xhigh`/`max` da' 400. MAGELLAN non imposta mai `thinking`, `max_tokens`, `temperature`, `top_p` o `top_k`: Claude Code gestisce tutto. Verificato anche che non esiste esposizione alla categoria di rifiuto `reasoning_extraction`, perche' i reflection loop producono artefatti, mai catene di ragionamento.

**Il problema dei classificatori NON sparisce**: la doc sui rifiuti nomina esplicitamente sia Fable 5 sia Opus 5 come modelli con classificatori di sicurezza, e la categoria `bio` avverte che "Beneficial life sciences work can also trigger this category". Il layer di fallback resta; cambia solo il bersaglio.

**Cambiamenti**:

1. **Modello**: tutti i 15 file `.claude/agents/*.md` passano da `model: fable` a `model: opus`. Effort INVARIATO (`max` sui 7 deep, `high` sugli 8 structured). Scelta deliberata: migrare una variabile alla volta, cosi' un'eventuale variazione di qualita' e' attribuibile al modello e non all'effort. La doc Opus 5 raccomanda un nuovo sweep di effort perche' la scala e' calibrata per-modello, ma quello e' un cambiamento separato e misurabile, da fare con `/validate-holdout`.

2. **Eccezione orchestratore (importante)**: l'orchestratore NON e' coperto dalla modifica di frontmatter. `/discover` lo carica nella sessione top-level, quindi gira sul modello di **sessione**. Chi lascia la sessione su un altro modello ottiene una pipeline mista: modello vecchio che coordina sub-agenti Opus 5. Documentato in `CLAUDE.md`, `README.md` e nel file dell'orchestratore: **`/model opus` prima di `/discover`**.

3. **Fallback anti-rifiuto ri-mirato**: dopo il cambio di alias il blocco esistente era diventato **circolare** (diceva di recuperare da un rifiuto ri-dispatchando con `model: opus`, cioe' il modello che aveva appena rifiutato). Ora il fallback e' unico: `model: claude-opus-4-8`, scritto come ID completo proprio perche' l'alias `opus` ora risolve a Opus 5. Opus 4.8 e' il fallback che Anthropic documenta per i rifiuti di Opus 5 e non e' fra i modelli elencati come portatori di questi classificatori. Aggiunto che un rifiuto arriva come HTTP 200 con `stop_reason: "refusal"` e `stop_details.category`, quindi e' invisibile a qualsiasi monitoraggio basato sugli errori. Mantenuto il re-dispatch manuale a livello di orchestratore: il parametro server-side `fallbacks` NON si propaga alle chiamate fatte dentro l'esecuzione di un tool, che e' esattamente come questa architettura invoca i sub-agenti.

4. **Ripristino accesso MCP (il fix di maggior valore di questa release)**: `tools:` nel frontmatter e' una **allowlist**, e nessun agente elencava pattern `mcp__*`. Risultato: ogni sub-agente dispatchato perdeva silenziosamente tutti i tool MCP, pur con i server connessi a livello di sessione e abilitati in `.mcp.json`. Il principio documentato "MCP-first retrieval (mandatory)" era di fatto non funzionante e la pipeline ripiegava su WebSearch. Riscontro empirico: la memoria dell'agente Literature Scout registra dalla sessione 2026-06-10-scout-033 che "every `mcp__semantic-scholar__*` and `mcp__pubmed__*` call returns No such tool available". Aggiunti `mcp__semantic-scholar__*, mcp__pubmed__*` in `tools:` piu' un blocco `mcpServers:` su literature-scout, critic, quality-gate e convergence-scanner (quest'ultimo istruiva l'uso di MCP senza averne i permessi). Critic e Quality Gate ora possono risolvere i PMID sulla fonte autoritativa invece che via ricerca web, il che serve direttamente il design anti-allucinazione.

5. **Recall suppressor rimossi (5)**: Opus 5 segue letteralmente le istruzioni di selettivita' e riporta meno. Erano tutti a monte della qualita' delle ipotesi:
   - `critic.md` "Be selective rather than exhaustive" (introdotto in v5.31 per Fable 5) contraddiceva il constraint "tutti e 9 i vettori". Ora copertura e lunghezza della prosa sono separate: riporta tutto, scrivi ogni finding in modo stringato.
   - `critic.md` template ATTACKS: elencava 5 righe per 9 vettori, quindi un modello letterale emetteva 5 attacchi e considerava il formato soddisfatto. Difetto strutturale, non stilistico.
   - `critic.md` "a strong novelty kill makes other vectors moot": permesso di uscita anticipata.
   - `quality-gate.md` "A novelty or mechanism failure makes other checks unnecessary": produceva tabelle rubrica mezze vuote, che `upload-session.mjs` poi pubblica.
   - `literature-scout.md` "Prioritize recent sources (2025-2026)": non era limitato alle sezioni giuste, quindi si applicava anche alle ricerche di **disgiunzione**. La disgiunzione e' un verdetto per evidenza negativa: un solo paper del 2011 che collega i due campi ribalta DISJOINT in PARTIALLY_EXPLORED, e la sotto-retrieval produce un falso DISJOINT indistinguibile da uno pulito.
   - `scout.md` "If you can only find 3-4 strong candidates, that's acceptable": permesso esplicito di sotto-consegnare.

6. **Reflection loop: taglio chirurgico, non rimozione**: la guida Opus 5 dice di rimuovere le istruzioni di verifica perche' il modello si auto-verifica. Applicata con una regola precisa, non alla lettera: *si taglia un item di reflection solo quando ripete una soglia di qualita' gia' presente in `<constraints>`; non si tocca mai un pavimento di copertura sulle chiamate a tool esterni*, perche' il suo ramo di fallimento genera altre ricerche reali e l'auto-verifica del ragionamento non le produce. Conseguenza pratica: i tre controlli "hai davvero fatto le ricerche?" (Critic, Quality Gate, Literature Scout) restano, riscritti in forma imperativa. Il grosso del taglio e' nel Generator (5 check introspettivi su 9). **Non toccato** il blocco che definisce il letterale `[GROUNDED]`/`[PARAMETRIC]`: e' l'unica definizione nel file ed e' contratto di input per `critic.md`, `quality-gate.md` e `dataset-evidence-miner.md`. Rimossi i parentetici "(before finalizing)" dagli header e riscritte le lede "review your own verdicts". **Nomi dei loop invariati**: compaiono in CLAUDE.md, README, methodology, CHANGELOG e nei file di lancio.

7. **Budget di lunghezza e disciplina di scope**: mancavano in tutti gli agenti esaminati. Opus 5 scrive piu' lungo dei modelli precedenti e **l'effort non e' la leva** (abbassarlo riduce il thinking senza accorciare in modo affidabile l'output), quindi la lunghezza va prescritta. Aggiunto un constraint per agente che fissa un budget e dichiara quali file scrivere e quale lavoro NON invadere. Rilevante in concreto: `upload-session.mjs` pubblica ogni `.md` nella results dir, quindi un file extra di iniziativa dell'agente finisce sul sito.

8. **Orchestratore**:
   - Riga 64: "If the agent wrote to {results_dir}/, trust it, don't re-read just to confirm it exists" era un permesso esplicito di saltare i due guard (Guard Protocol step 4 e DELIVERABLES VERIFICATION) che intercettano un sub-agente che salta silenziosamente il markdown. Ristretto a "non rileggere il CONTENUTO che hai scritto tu".
   - Self-check pre-`phase: complete`: contava i dispatch "you have dispatched this session", cioe' dal contesto, violando la regola dello stesso file. Ora legge `state/dispatch-log.json`, la stessa fonte su cui blocca lo Stop hook.
   - Session summary: aggiunto target 400-700 parole. Il blocco esistente diceva "readability matters more than raw brevity", che su Opus 5 punta nella direzione sbagliata sull'artefatto piu' letto della sessione.
   - Corretta la giustificazione dell'architettura top-level: non e' piu' vero che i sub-agenti non possano dispatchare (da v2.1.219 il default e' profondita' 3). Il design resta, con la ragione reale: un unico dispatch-log validato dagli hook.

9. **Ranker (due difetti critici)**: la step sequence ometteva il torneo Elo e il bonus cross-domain e diceva "file" al singolare dove i file richiesti sono due, quindi un modello letterale produceva un report incompleto. E il GOAL diceva "each surviving hypothesis": con il vocabolario del Critic (SURVIVES/WOUNDED/KILLED) una lettura letterale scarta tutte le WOUNDED dal ranking, e quindi da Evolver e Quality Gate. Ora e' esplicito che si classificano SURVIVES e WOUNDED, e le KILLED si elencano per far quadrare i conti.

10. **Script e floor di versione**: `init-session.sh` timbra `claude-opus-5`. `version-check-hook.py` alza `MIN_VERSION` a **(2,1,219)**, la versione in cui l'alias `opus` ha iniziato a risolvere a Opus 5: sotto quel floor ogni `model: opus` risolve silenziosamente a un Opus 4.x, che e' un fallimento invisibile e non un errore.

**Costo**: $5/$25 per MTok contro i $10/$50 di Fable 5, quindi il prezzo per token si dimezza rispetto a v5.31. Il risparmio reale per sessione e' inferiore alla meta': Opus 5 fa thinking di default e scrive output piu' lunghi, ed e' proprio per questo che i budget di lunghezza del punto 7 fanno parte della migrazione e non sono un extra.

**Stato di validazione (NON validato end-to-end)**: nessuna sessione `/discover` completa e' stata eseguita su Opus 5. Da fare prima di dichiararla validata: (1) una sessione completa monitorando `stop_reason: refusal` e l'effettivo scatto del fallback a `claude-opus-4-8`; (2) verifica che `dispatch-log.json` contenga tutti i dispatch critici, perche' l'inlining di una fase e' il modo specifico in cui un orchestratore Opus 5 che espande lo scope fallirebbe; (3) conferma che il Literature Scout usi davvero i tool MCP e non il fallback E-utilities; (4) confronto del kill rate del Critic con la baseline in `meta-insights.md`, dove un CALO indicherebbe un recall suppressor sopravvissuto; (5) A/B `/validate-holdout` contro la baseline. Da notare che anche la baseline Fable 5 di v5.31 non era mai stata validata: l'ultima validazione end-to-end completa resta su Opus 4.7.

**Nota sul fix MCP**: la diagnosi (allowlist che esclude i pattern `mcp__*`) e' documentata ufficialmente e corroborata dalla memoria dell'agente, ma **il fix non e' stato verificato in questa sessione**. Un test controllato ha mostrato che le definizioni degli agenti risultavano congelate all'avvio della sessione: un tool marcatore aggiunto al frontmatter non compariva nel sub-agente dispatchato, quindi le probe stavano leggendo la definizione pre-modifica. La verifica va rifatta in una sessione nuova (probe: un sub-agente che tenta `mcp__pubmed__pubmed_search` e riporta se il tool esiste).

**Non-modifiche deliberate** (guida Opus 5 che romperebbe MAGELLAN se raccolta alla lettera):
- *"Never use subagents to verify or double-check your own work"*: Critic, Quality Gate, Cross-Model Validator, Convergence Scanner e DEM verificano l'output di un **altro** agente, non il proprio. Raccoglierla cancellerebbe l'intero layer avversariale.
- *"Keep spawn counts low"*: `orchestrator-stop-gate.py` BLOCCA la terminazione se mancano `scout`/`generator`/`critic`/`quality-gate` dal dispatch log. Meno spawn e' un fallimento duro, non un risparmio.
- *"Remove the final verification step"* applicato ai gate su artefatti e deliverable: quelli controllano gli effetti collaterali su filesystem di un altro agente. Nessuna auto-verifica vede una scrittura che non e' mai avvenuta.
- *"Avoid re-checks it already performs"* applicato a "leggi `quality-gate.json` da disco, mai dalla memoria": Opus 5 si auto-verifica sul proprio contesto, che dopo ~100 tool call e' esattamente la fonte corrotta che quelle righe aggirano.
- *"Use effort to control response length"*: la doc dice che l'effort non accorcia in modo affidabile. Abbassarlo su Generator/Critic/Quality Gate degraderebbe il ragionamento lasciando i deliverable altrettanto lunghi.
- Nessuna adozione di sub-agenti annidati (ora possibili fino a profondita' 3) e nessuna modifica a `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`, che pero' non e' inerte: con Opus 5 che delega piu' volentieri, resta un elemento da osservare alla prima sessione di validazione.
- Skill, `settings.json`, `.mcp.json` e i 20 stop-gate: verificati, nessuna modifica necessaria. `domain-life-sciences` resta quello che aumenta di piu' l'esposizione al classificatore `bio`, perche' inietta contenuto molecolare.

**File modificati**:
- `.claude/agents/*.md` (15 file) -- `model: fable` a `model: opus`; effort invariato
- `.claude/agents/discovery-orchestrator.md` -- fallback ri-mirato a `claude-opus-4-8`; guard read ristretto; conteggio dispatch da disco; budget summary; giustificazione top-level corretta; nota `/model opus`
- `.claude/agents/literature-scout.md`, `critic.md`, `quality-gate.md`, `convergence-scanner.md` -- accesso MCP (`tools:` + `mcpServers:`)
- `.claude/agents/critic.md`, `quality-gate.md`, `literature-scout.md`, `scout.md`, `generator.md`, `evolver.md`, `ranker.md` -- recall suppressor, taglio reflection, budget di lunghezza e scope
- `scripts/init-session.sh` -- timbro modello `claude-opus-5`
- `scripts/version-check-hook.py` -- `MIN_VERSION` (2,1,219) e messaggio utente
- `prompts/validation-prompt-gpt.md` -- attribuzione del modello generatore a Opus 5
- `CLAUDE.md` -- tabella agenti, tre paragrafi di policy riscritti, nuovo paragrafo sull'allowlist MCP, correzione della claim sul nesting
- `README.md` -- prerequisiti (floor 2.1.219 e `/model opus`), tag per-agente, paragrafo architettura
- `docs/methodology-v5.md` -- diagramma e tabella agenti (erano rimasti a Opus/Sonnet da prima di v5.31), tabella reflection, sezione tuning per-modello riscritta per Opus 5, voce Opus 5 nei benchmark di riferimento
- `docs/pdf/methodology.html` -- badge e tabella modelli (erano fermi all'era Opus 4.6)
- `launch-posts.md`, `launch-creators.md`, `launch-media-pitches.md` -- claim sui modelli
- `docs/CHANGELOG.md` -- questa entry

---

## v5.32: Cross-Model Validator -- split per-ipotesi GPT-5.5 Pro (completa la cura TPM di v5.30) (10 giugno 2026)

**Motivazione**: completa la cura del problema TPM diagnosticato in v5.30. Test in ISOLAMENTO (nessuna response concorrente): una singola validazione GPT-5.5 Pro a `xhigh` che copre ENTRAMBE le ipotesi esegue ~23-26 web_search ad alto consumo e raggiunge ~970k/1.000.000 token-al-minuto dell'org, fallendo con `rate_limit_exceeded`. Quindi NON era (solo) colpa delle verifiche lanciate in parallelo durante il debug: anche una sola response satura il tier TPM con questo carico. (Perche' non si vedeva prima: il validator e' stato migrato a gpt-5.5-pro solo di recente; il precedente gpt-5.4-pro era piu' leggero per-minuto. Vedi v5.30.)

**Decisione**: validare UNA ipotesi per chiamata GPT. Dimezza i tool call (e quindi i token/minuto) per response, cosi' ogni chiamata resta sotto il limite e completa in stato `completed` invece di essere salvata da `failed`. Chiamate SEQUENZIALI (mai concorrenti: la concorrenza ricrea la contesa TPM). medium context + `max_tool_calls` da soli riducono il picco ma non bastano (il test in isolamento lo conferma); il dimezzamento per-ipotesi e' la leva strutturale.

**Implementazione** (`scripts/validate-crossmodel.mjs`): nuovo `callOpenAISplit` divide il prompt sui marker `## HYPOTHESIS`, riusa `callOpenAI` per-ipotesi (eredita medium context, `max_tool_calls`, salvage-on-failed, resume), e concatena gli output in `validation-gpt.md`. Fallback automatico al singolo invio se le ipotesi sono <2. Guard di resume: una ipotesi gia' validata (output presente, nessun `.response-id` residuo) viene riusata senza ri-fatturare. Gemini NON e' splittato (modello unico, non consuma il pool TPM OpenAI). Logica di split verificata in unit-test sul prompt reale (2 sotto-prompt, preambolo condiviso); conferma end-to-end alla prossima sessione reale.

**File modificati**:
- `scripts/validate-crossmodel.mjs` -- `splitGptPrompt` + `callOpenAISplit`; `main()` usa `callOpenAISplit` per il task OpenAI (Gemini invariato)
- `docs/methodology-v5.md` -- riga GPT-5.5 Pro aggiornata: medium context, `max_tool_calls`, split per-ipotesi, salvage-on-failed (allineata alla v5.30/v5.32, prima diceva ancora "high")

---

## v5.31: Migrazione pipeline a Claude Fable 5 + harvest prompting + fallback anti-refusal (10 giugno 2026)

**Motivazione**: Il 9 giugno 2026 Anthropic ha rilasciato Claude Fable 5
(`claude-fable-5`, alias `fable`), il flagship GA piu' capace, e Claude Mythos 5
(`claude-mythos-5`, stesse capacita' senza classificatori, gated su Project
Glasswing). Fable 5 migliora Opus 4.8 in autonomia long-horizon, correttezza
al primo colpo, vision, recall di code review/debugging, e soprattutto delega
di sub-agenti in parallelo: capacita' centrali per una pipeline a 15 agenti.
Decisione dell'autore: testare Fable 5 il piu' possibile in tutta la pipeline,
con rollback per-agente dove i classificatori dovessero rifiutare.

**Tensione strutturale (dichiarata, non ipotizzata)**: la guida ufficiale dice
che Fable 5 esegue classificatori che possono rifiutare contenuti di biologia e
scienze della vita (`molecular mechanisms`, `lab methods`) con
`stop_reason: "refusal"`, e che "Claude Fable 5 is not intended for ... biology
and life sciences work". MAGELLAN e' ottimizzato proprio per le scienze della
vita, quindi gli agenti che generano/verificano meccanismi molecolari sono i
piu' esposti. Questa e' la ragione del layer di fallback sotto.

**Cambiamenti**:
1. **Modello**: tutti i 15 file `.claude/agents/*.md` passano da
   `model: opus` / `model: sonnet` a `model: fable`. Effort INVARIATO (`max`
   per i 7 deep, `high` per gli 8 structured: entrambi validi su Fable 5,
   verificato sulla doc sub-agents di Claude Code). La distinzione deep/structured
   ora la porta l'effort, non il tier di modello.
2. **Orchestratore**: gira sul modello di sessione (`/model`), non sul
   frontmatter (al top-level il `model:`/`effort:` di frontmatter e' informativo).
   Esteso il commento "Execution context" per documentarlo; il rollback
   dell'orchestratore e' un `/model`, non una modifica al file.
3. **Fallback anti-refusal nel Guard Protocol**: se un sub-agente ritorna un
   refusal o output vuoto/stub, l'orchestratore lo ri-dispatcha UNA volta con
   override `model: opus` (deep) o `model: sonnet` (structured) come parametro
   per-invocazione del tool Agent (ha priorita' sul frontmatter; verificato
   sull'ordine di risoluzione: env > per-invocation > frontmatter > sessione).
   Un refusal non e' fatturato, quindi il fallback e' economico. Rollback
   persistente per i refuser sistematici: frontmatter a `opus`/`sonnet`.
   Mappa di esposizione (dal piu' esposto): generator, critic, quality-gate,
   computational-validator, literature-scout, dataset-evidence-miner,
   convergence-scanner (alta); holdout-evaluator, scout (media); il resto bassa.
4. **Harvest prompting (model-agnostic + Fable-5)** su `discovery-orchestrator.md`:
   reminder di operazione autonoma (non chiedere conferma mid-pipeline; non
   chiudere il turno su un intento, esegui la tool call); rassicurazione
   context-budget ("economia != bailout: non interrompere/riassumere/proporre
   nuova sessione per i limiti di contesto"); grounding di ogni progress/health
   claim su un tool result letto da disco; "when you have enough info, act";
   "give the reason, not only the task" nei dispatch; dispatch concorrente di
   convergence-scanner + dataset-evidence-miner (in overlap col poll lungo del
   cross-model). Addendum brevita'/leggibilita' (lead-with-outcome, frasi
   complete, niente arrow-chain) su session summary e sulle sezioni output di
   Critic, Quality-Gate, Session-Analyst. I contratti di output validati dagli
   hook (campi JSON, tag `[GROUNDED]`, rubriche, tassonomie di verdetto) sono
   stati preservati: la concisione tocca solo la prosa.
5. **Audit reasoning_extraction (rischio basso, nessuna modifica)**: la guida
   Fable 5 avverte che istruzioni a "trascrivere/echeggiare il ragionamento"
   possono scatenare il refuso `reasoning_extraction`. Verificato: nessun prompt
   o `output_format` chiede una trascrizione del ragionamento interno. Le
   reflection loop (SELF-CRITIQUE, META-CRITIQUE, ecc.) producono output
   strutturato (ipotesi riviste, verdetti, punteggi), non chain-of-thought:
   restano invariate. Nota: l'auto-verifica via sub-agent a contesto fresco che
   Fable 5 raccomanda MAGELLAN ce l'ha gia' (Critic e Quality Gate separati).
6. **Audit skills (nessuna modifica)**: le 5 skill (`discovery-engine`,
   `domain-life-sciences`, `domain-physics-math`, `hypothesis-validation`,
   `literature-retrieval`) sono snelle (36-136 righe) e referenziali (zone di
   connessione, pattern di ricerca, scoring), non istruzioni comportamentali
   sovra-prescrittive: nessuna potatura giustificata. Nota: `domain-life-sciences`
   inietta contenuto molecolare nei prompt che la caricano, contribuendo
   all'esposizione ai refusal.
7. **Docs sync**: CLAUDE.md (tabella architettura -> Fable; principio
   modello+effort; nuovo principio fallback; alias resolution); README.md
   (prerequisiti, tag agenti, principio); methodology-v5.md (overview, tabella
   modelli interni, nuova reference benchmark Fable 5); `scripts/init-session.sh`
   (stamp `model` -> `claude-fable-5`); `scripts/version-check-hook.py`
   (rationale e messaggio: alias `fable`, floor da confermare contro il changelog
   CC per il supporto Fable 5).

**Costo**: Fable 5 e' $10/$50 per MTok, contro Opus 4.8 $5/$25 e Sonnet 4.6
$3/$15. La migrazione alza il costo Anthropic ~2x sugli agenti gia' Opus e ~3.3x
su quelli gia' Sonnet (~2-3x per sessione). Gli agenti structured/search sono
dove Fable 5 costa di piu' e porta meno valore di ragionamento: opzione informata
se il costo diventa un problema, tenerli su Sonnet 4.6.

**Stato di validazione (NON ancora validato end-to-end)**: questa e' una
migrazione di alias + harvest + fallback; il request surface di Fable 5 e' lo
stesso su cui girava la pipeline (adaptive-thinking-only, no sampling params, no
prefill), quindi nessuna modifica API/codice. Da fare prima di dichiararla
validata: (1) una sessione `/discover` completa su Fable 5, monitorando
`stop_reason: refusal`, output vuoti/troncati, trigger degli stop-gate e
l'effettivo scatto del fallback automatico; (2) un confronto A/B
`/validate-holdout` Fable 5 vs baseline Opus 4.8/Sonnet 4.6 (verdetto di
rediscovery, similarita' di meccanismo, composito/groundedness QG) per misurare
il beneficio reale, non solo l'assenza di refusal. La pipeline e' stata
validata end-to-end l'ultima volta su Opus 4.7.

---

## v5.30: Cross-Model Validator GPT-5.5 Pro -- causa reale (saturazione TPM), shell rimossa, hardening (9 giugno 2026)

**Motivazione**: Nella sessione S032 (`2026-06-09-scout-032`) la validazione GPT-5.5 Pro non si e' mai completata: la response restava `in_progress` per oltre 7 ore (431 min), ben oltre il cap di 4 ore, senza output, senza errore, senza `required_action`. Gemini DR Max invece completava regolarmente (~14 min). Indagine con probe controllati + documentazione ufficiale OpenAI (guides/tools-shell): `scripts/validate-crossmodel.mjs` passava il tool `{ type: 'shell' }`, che l'API espande di default a una shell CLIENT-SIDE (`environment.type: 'local'`). Una local shell richiede che l'integratore esegua i `shell_call` e rimandi `shell_call_output` in un turno successivo; lo script fa solo submit in background + polling e non serve mai quelle chiamate, quindi alla prima invocazione della shell la response si bloccherebbe. ATTENZIONE (correzione lasciata a memoria): questa era la PRIMA ipotesi ed era SBAGLIATA come causa del blocco S032 -- un re-run SENZA shell si e' bloccato ugualmente per 4 ore. La shell e' un bug latente reale (rimosso comunque), ma NON la causa di questo blocco. La prova "0 output = stallo" era anch'essa errata: per le response background `in_progress`, `output[]` e' sempre vuoto fino allo stato terminale.

**Probe di isolamento** (hanno anche corretto una mia prima diagnosi sbagliata, "0 output = stallo", in realta' `output[]` e' vuoto per qualsiasi response background `in_progress`): response minimale (no tool, effort high) completa in 15s; `web_search_preview` + `code_interpreter` (no shell, effort high) completa in 45s con web search + code realmente eseguiti. Quindi background mode e tool server-side funzionano: l'unica differenza nel caso bloccato era la local shell.

**Scoperta API (mutua esclusione)**: l'unica shell background-safe e' quella HOSTED (`environment.type: 'container_auto'`, server-side come code_interpreter), MA l'API rifiuta code_interpreter + hosted shell insieme: *"code_interpreter and shell with an OpenAI-managed container cannot be used together at the same time"* (`mutually_exclusive_parameters`). Tenere la shell imporrebbe quindi di rimuovere code_interpreter. La config originale (code_interpreter + shell:local) era la peggiore: teneva code_interpreter ma aggiungeva una local shell che si blocca, e non avrebbe potuto usare la hosted shell comunque.

**Decisione**: per la validazione (verifica aritmetica/statistica + novelty) il sandbox Python di `code_interpreter` e' lo strumento managed-container piu' utile (gli errori che il QG ha trovato su E5 erano proprio esponenti/aritmetica); `web_search_preview` copre la novelty. La capacita' shell (curl/wget/pip/CLI per dataset reali) e' secondaria. Quindi: rimossa la shell, mantenuti `code_interpreter` + `web_search_preview`. Se in futuro servisse il data-fetching, usare hosted-shell-DA-SOLA (senza code_interpreter) e aggiornare la logica di estrazione `shell_call_output`.

**Aggiunto**: flag `--effort` in `validate-crossmodel.mjs` (default invariato `xhigh`, scelta confermata dall'autore) per poter usare `high` quando la latenza conta. Default produzione resta `xhigh` (l'orchestratore chiama lo script senza flag). Nota operativa: con `xhigh` la response GPT-5.5 Pro impiega 30-90 min, quindi la finestra di attesa dell'orchestratore deve tollerare l'intero range (lo script polla fino a 4 ore). La causa del blocco S032 NON era la shell ma la saturazione del rate-limit TPM (vedi sotto).

**Causa reale (misurata, non ipotizzata)**: la validazione di 2 ipotesi a `xhigh` con ~30 tool call (web_search ad alto contesto + code_interpreter) consuma ~1.000.000 token/minuto e satura il tier TPM dell'org. Probe controllati: response minimale 15s; web+code con prompt banale 45s; ma il prompt di validazione completo (147 righe, 2 ipotesi) genera 23-26 web_search ad alto contesto e fallisce con `rate_limit_exceeded` ("Used 990297 / Limit 1000000 TPM"). Senza cap la response viene strozzata e resta `in_progress` per ore; con `max_tool_calls` termina in 7-16 min ma puo' toccare il limite TPM ALLA FINE, dopo aver gia' prodotto il report completo.

**Fix TPM**: (1) `search_context_size` `'high'`->`'medium'` (ogni ricerca ad alto contesto inietta molti token; con ~30 ricerche e' la leva principale); (2) `max_tool_calls: 40` (la response termina sempre); (3) **salvage-on-failed** (se `failed` ma con un messaggio gia' generato, recupera il report invece di scartarlo -- cosi' e' stato recuperato il report reale di S032: E7 4/10, E5 4/10); (4) output **report-first** (verdetti prima del reasoning verboso, cosi' l'estratto da 5000 char caricato da `upload-session.mjs` contiene i verdetti). Per il completamento PULITO senza toccare il TPM: validare UNA ipotesi per chiamata (dimezza i token/min per call) o alzare il tier TPM dell'org.

**File modificati**:
- `scripts/validate-crossmodel.mjs` -- `search_context_size` medium, `max_tool_calls: 40`, salvage-on-failed, output report-first; rimosso `{ type: 'shell' }` (bug latente local-shell + mutua esclusione con code_interpreter, NON la causa del blocco); aggiunto flag `--effort` (default xhigh); aggiornati commenti header e log di submit
- `CLAUDE.md`, `README.md`, `docs/methodology-v5.md`, `.claude/agents/cross-model-validator.md` -- rimosso "shell" dalla descrizione dei tool GPT-5.5 Pro effettivamente usati e dall'array `gpt_tools`. Mantenuta in `methodology-v5.md` (sezione reference benchmark) la riga che elenca i tool *supportati dal modello* (che includono davvero shell/file_search/MCP): e' un dato di fatto sul modello, non sulla nostra config

---

## v5.29: Allineamento hook allo schema canonico + quick wins changelog CC (9 giugno 2026)

**Motivazione**: Review del changelog ufficiale di Claude Code (maggio-giugno 2026) per individuare nuove funzioni utili alla pipeline (esclusi i bugfix). La verifica sui file reali ha rivelato un difetto di correttezza: tutti gli stop-gate emettevano la guida non bloccante nel campo `feedback`, che NON e' un campo riconosciuto dallo schema hook di Claude Code (campi validi: `decision`, `reason`, `continue`, `stopReason`, `suppressOutput`, `systemMessage`, `terminalSequence`, `hookSpecificOutput.additionalContext`). Claude Code lo scartava in silenzio: i blocchi hard funzionavano (usano `decision:block` o `exit 2` + stderr) ma i messaggi "PASSED", i warning e i "continue" non arrivavano da nessuna parte. Inoltre l'orchestrator-stop-gate usava `decision:"approve"`, valore inesistente (per consentire lo stop si omette `decision`).

**Decisioni (quick wins implementati)**:

1. **Output hook canonico**: migrato ogni `feedback` non bloccante a `systemMessage` (visibile all'utente) in tutti gli stop-gate, `subagent-stop-hook.py`, i compact hook e `tool-failure-hook.py`. Scelto `systemMessage` e non `additionalContext` perche' su un percorso di PASS `additionalContext` farebbe continuare il turno (impedirebbe lo stop o terrebbe vivo il sub-agente). Rimosso `decision:"approve"` dall'orchestrator-stop-gate (ora omette `decision`). `post-write-hook.py` reso silenzioso in caso di successo (scatta ad ogni Write) e con `systemMessage` solo su errore. Blocchi hard invariati.

2. **Notifica desktop (`terminalSequence`, v2.1.141)**: l'orchestrator-stop-gate emette una notifica OSC 9 al completamento della sessione ("session X complete, N hypotheses passed QG"). Utile per le sessioni autonome lunghe (30-90 min) dove l'utente torna a fine run.

3. **Hook in exec-form (`args`, v2.1.139)**: tutte le voci hook in `.claude/settings.json` convertite da shell-form (`python3 "$CLAUDE_PROJECT_DIR/..."`) a `command` + `args` con `${CLAUDE_PROJECT_DIR}`. Elimina la fragilita' di quoting e il problema Windows (bash invocato esplicitamente). I blocchi `hooks.stop` inline in `generator.md`/`critic.md` usavano uno schema NON documentato (lista diretta sotto chiave lowercase `stop`; lo schema corretto e' `hooks.<Event>: - matcher/hooks: [...]`), quasi certamente non scattavano mai ed erano ridondanti coi matcher `SubagentStop` in settings.json: rimossi (i gate restano attivi via settings.json).

4. **Version floor (v2.1.166)**: nuovo hook `SessionStart` `scripts/version-check-hook.py` (fail-open) che avvisa via `systemMessage` se la versione CC e' < 2.1.166. Il floor copre le funzioni adottate piu' `opus`=Opus 4.8 (che richiede 2.1.154). Per le org si puo' usare la managed setting `requiredMinimumVersion`. Documentato in README (Prerequisites).

5. **`fallbackModel` (v2.1.166) NON persistito in settings**: la chiave non e' ancora nello schema pubblicato (aggiunta il 6 giugno, lo schema e' indietro) e non e' confermato se cascata ai dispatch dei sub-agenti. Un fallback silenzioso a Sonnet su Generator/Critic/Quality-Gate (pinnati Opus per il ragionamento cross-disciplinare) degraderebbe la qualita' senza fallire. Raccomandato invece il flag di lancio `claude --fallback-model <model>` (session-scoped, confermato in `--help` su 2.1.168). Da rivalutare quando schema e comportamento di cascata saranno documentati.

**Non adottato ora (Tier 2)**: dynamic Workflows (v2.1.154) come possibile architettura v6 (prototipo consigliato sul fan-out post-QG, oggi sequenziale); `background_tasks`/`session_crons` negli hook (v2.1.145) solo come guardia difensiva nel gate cross-model, dato che l'ordine e' gia' garantito dal wait sincrono dell'orchestratore e il poller bash vive nel contesto del sub-agente; `continueOnBlock` su PostToolUse (v2.1.139); `/goal` (v2.1.139).

**Note di correttezza**: `PostToolUseFailure` e `PostCompact` sono eventi hook validi (nessun bug latente). NON impostare `CLAUDE_CODE_SUBAGENT_MODEL` (sovrascriverebbe il pin per-agente opus/sonnet di tutti i sub-agenti). Corretto in questa entry: i blocchi `hooks.stop` inline in `generator.md`/`critic.md` usavano uno schema non documentato (non scattavano) ed erano ridondanti coi matcher `SubagentStop` in `settings.json`; rimossi.

**File modificati**:
- `scripts/orchestrator-stop-gate.py` -- feedback->systemMessage, rimosso decision:approve, terminalSequence al completamento, fix em dash nel docstring
- 13 stop-gate/stop-hook (`subagent-stop-hook.py`, `scout-`, `generator-`, `critic-`, `literature-scout-`, `ranker-`, `target-evaluator-`, `computational-validator-`, `session-analyst-`, `cross-model-validator-`, `convergence-scanner-`, `dataset-evidence-miner-`, `holdout-evaluator-`) -- feedback->systemMessage
- `scripts/pre-compact-hook.py`, `scripts/post-compact-hook.py`, `scripts/tool-failure-hook.py` -- feedback->systemMessage
- `scripts/post-write-hook.py` -- silenzioso su successo, systemMessage su errore
- `scripts/version-check-hook.py` -- nuovo (SessionStart version floor)
- `.claude/settings.json` -- hook in exec-form + registrazione hook SessionStart
- `.claude/agents/generator.md`, `.claude/agents/critic.md` -- rimosso blocco `hooks.stop` malformato/ridondante dal frontmatter (schema non documentato; gate attivi via matcher SubagentStop in settings.json)
- `CLAUDE.md` -- bullet "Hook schema" riscritto (campi canonici), "exit 0 = allow"
- `README.md` -- Prerequisites: floor versione Claude Code 2.1.166
- `docs/methodology-v5.md` -- sezione hook: version-check-hook, output canonico, exec-form
- `docs/CHANGELOG.md` -- questa entry

---

## v5.28: Migrazione Opus 4.8 (9 giugno 2026)

**Motivazione**: Anthropic ha rilasciato Claude Opus 4.8, nuovo modello Opus di default (model id `claude-opus-4-8`). Costruisce su Opus 4.7 e ne eredita invariata la superficie API: adaptive-thinking-only (`thinking: {type: "enabled", budget_tokens: N}` restituisce 400), nessun parametro di sampling (`temperature`/`top_p`/`top_k`), nessun prefill sull'ultimo turno assistant. Pricing identico ($5/$25 per 1M token), contesto 1M, output max 128K. Codice che gira su 4.7 gira su 4.8 senza modifiche, e la guida ufficiale indica che 4.8 funziona bene out of the box sui prompt 4.7. I miglioramenti rilevanti per una pipeline multi-agent: coding agentico long-horizon (meno compaction, miglior recovery dopo compaction, miglior gestione del long-context), calibrazione dell'effort più affidabile per livello, e tool-triggering migliore (meno casi di tool-call richieste ma saltate, problema occasionale di 4.7). Novità a livello API/feature: mid-conversation system messages (senza beta header), fast mode in research preview (`speed: "fast"`), minimo cacheable prompt sceso a 1024 token, effort default `high`.

**Stato empirico**: MAGELLAN non fa chiamate dirette all'API Anthropic; Claude è invocato solo via dispatch di Claude Code con gli alias di frontmatter `model: opus`/`model: sonnet`. L'alias `opus` risolve al modello Opus current-latest al momento del dispatch, quindi risolve già a 4.8 senza modifiche al frontmatter. L'ultima validazione end-to-end completa è stata su Opus 4.7 (14 agenti dispatchati, tool usage abbondante, esiti PASS + CONDITIONAL_PASS). Una validazione equivalente su 4.8 è raccomandata come follow-up e NON è stata eseguita in questa migrazione (scelta esplicita: documentare ora, validare dopo). I doc quindi non dichiarano "validato su 4.8".

**Decisioni**:

1. **Alias `model: opus` mantenuto, niente pinning esplicito a `claude-opus-4-8`**. L'alias preserva l'auto-risoluzione al modello più recente ed è coerente col design documentato (sezione "Model alias resolution" in CLAUDE.md). Pinnare darebbe riproducibilità esplicita ma richiederebbe un bump manuale ad ogni release futura e perderebbe l'auto-risoluzione: valutato e scartato per questa migrazione.

2. **Effort Opus mantenuto a `max`** per i 5 agenti Opus (Scout, Target Evaluator, Generator, Critic, Quality Gate) più Holdout Evaluator e Orchestrator. La guida 4.8 indica `xhigh` come ottimo per il lavoro agentico e avverte che `max` può portare a overthinking con rendimenti decrescenti, ma per un esperimento quality-first tollerante a latenza e costo si mantiene il floor di qualità massimo. Da rivalutare con dati empirici da una sessione di validazione su 4.8 (monitorare overthinking e token spend).

3. **Prompt body degli agenti non re-baseline**. 4.8 eredita la superficie 4.7 e funziona out of the box; la de-emphasis del linguaggio enfatico (Reduced MUST/CRITICAL density) era già stata fatta in v5.2 per adaptive thinking e si applica a 4.8 (che amplifica "more literal instruction following"). I guardrail funzionali dell'Orchestratore (anti-inlining: "you MUST dispatch every role", stop-gate hooks) restano invariati: gli shift comportamentali di 4.8 (meno subagent e meno tool-call di default) non si manifestano in MAGELLAN perché l'Orchestratore non ha WebSearch/WebFetch (non può fare lavoro inline) e gli stop-gate validano deterministicamente la completezza dell'output. Se una validazione su 4.8 mostrasse sotto-retrieval, il fix mirato sarà rinforzare le righe specifiche di tool-triggering già presenti (Literature Scout MCP-first, Critic web-search-per-hypothesis, Quality Gate verifica per-claim), non un softening generalizzato.

4. **Capacità nuove di 4.8 non adottate, e perché**: mid-conversation system messages e fast mode non sono applicabili (nessuna chiamata API diretta; per fast mode la pipeline privilegia qualità a velocità, con pricing premium). Il minimo cacheable prompt a 1024 token è un beneficio automatico lato Claude Code, nessuna azione richiesta.

5. **Doc sync**: aggiornati i riferimenti da Opus 4.7 a 4.8 in `CLAUDE.md` (Model alias resolution), `docs/methodology-v5.md` (overview, tabella agente-modello, benchmark di riferimento con nuova entry 4.8 affiancata a 4.7, language calibration, model-specific tuning, time horizon, metadata example), `prompts/validation-prompt-gpt.md`, `launch-creators.md`, `launch-media-pitches.md`, e l'etichetta metadati in `scripts/init-session.sh` (`opus-4.7` -> `opus-4-8`). `README.md` non contiene una versione Opus esplicita: nessuna modifica. I riferimenti storici (entry CHANGELOG precedenti, descrizioni dello stato del tempo) non sono modificati.

**File modificati**:
- `CLAUDE.md` -- sezione "Model alias resolution" riscritta (4.8, giugno 2026, framing validazione onesto)
- `docs/methodology-v5.md` -- overview, tabella interna agente-modello, benchmark di riferimento (nuova entry Opus 4.8), language calibration, model-specific tuning, time horizon, metadata example
- `scripts/init-session.sh` -- etichetta metadati `model` per le nuove sessioni
- `prompts/validation-prompt-gpt.md` -- riferimento al modello generatore
- `launch-creators.md`, `launch-media-pitches.md` -- riferimenti marketing a Opus
- `docs/CHANGELOG.md` -- questa entry

---

## v5.27: Migrazione schema Gemini Interactions API (12 maggio 2026)

**Motivazione**: Il 7 maggio 2026 Google ha rilasciato la revisione `2026-05-20` dello schema delle Interactions API, con timeline di sunset del legacy schema fissata al 26 maggio (default flip, SDK 1.x ancora ok con legacy responses) e all'8 giugno (legacy schema rimosso, SDK 1.x fail su Interactions API). I cambiamenti rilevanti per il Cross-Model Validator di MAGELLAN sono: (a) `interaction.outputs[]` rinominato a `interaction.steps[]` con type discriminator; (b) il testo del messaggio del modello si trova ora in `step.content[i].text` (con `step.type === 'model_output'` e `content[]` tipizzato come `TextContent | ImageContent | AudioContent | DocumentContent | VideoContent`); il thinking trace e' su step separato `step.type === 'thought'` con field `summary[]` (NON `content[]`); (c) gli eventi streaming sono rinominati: `interaction.start` -> `interaction.created`, `content.delta` -> `step.delta`, `interaction.complete` -> `interaction.completed`, `content.start`/`content.stop` -> `step.start`/`step.stop`; (d) nuovi step type espliciti per i tool server-side (`user_input`, `function_call`/`_result`, `code_execution_call`/`_result`, `url_context_call`/`_result`, `google_search_call`/`_result`, `file_search_call`/`_result`, `mcp_server_tool_call`/`_result`, `google_maps_call`/`_result`); (e) `@google/genai` >=2.0.0 emette automaticamente lo schema nuovo. Senza migrazione, il pipeline si rompe all'8 giugno.

**Doc vs SDK divergenze incontrate**: La doc ufficiale Google (`interactions-breaking-changes-may-2026`) aveva 4 punti che NON corrispondono allo schema effettivamente esposto da `@google/genai@2.1.0`. Verificato leggendo `node_modules/@google/genai/dist/genai.d.ts` prima del dry-run: (1) la doc dichiara `error` rinominato in `interaction.error`, ma l'SDK emette ancora event_type `'error'` (interfaccia `ErrorEvent_2`); (2) la doc dichiara `interaction.status_update` splittato in `interaction.in_progress` + `interaction.requires_action`, ma sull'SSE stream l'evento `interaction.status_update` esiste ancora e il `status` field interno copre tutti gli stati (`in_progress | requires_action | completed | failed | cancelled | incomplete`); lo split webhook-only e' un'altra cosa; (3) la doc parla genericamente di "type: text" e "content[0].text" come pattern singolo, ma in realta' lo step type del modello e' `model_output` (non `message`) e quello del pensiero e' `thought` con `summary[]` (non `content[]`); (4) il delta del citation streaming e' `text_annotation_delta` con `annotations: Array<URLCitation|FileCitation|PlaceCitation>`, non un singolo `text_annotation` o `citation`. Tutti 4 i bug sono stati colti nel codice prima del dry-run e fixati in questa stessa entry.

**Decisioni**:

1. **Bump SDK a `^2.0.0`**. `@google/genai` passa da `^1.45` (risolveva 1.46.0) a `^2.0.0` (risolve 2.1.0). Il nuovo SDK adotta lo schema v2 senza opt-in header. Per l'uso che ne facciamo (Deep Research Max agent autonomo, payload `agent_config` con `deep-research-max-preview-04-2026`, no streaming generation single-shot), non sono attese altre breaking changes oltre allo schema.

2. **Riscrittura `scripts/validate-crossmodel.mjs` su schema v2 solo, niente codice difensivo dual-schema**. La scelta favorisce coerenza/leggibilita' del codice rispetto alla possibilita' di un rollback temporaneo dell'SDK (rischio considerato accettabile, gestibile via re-bump del `package.json` se necessario). Cambiamenti:
   - **`consume(stream)`**: matcha i nomi degli eventi effettivi dell'SDK 2.1.0 (`interaction.created`, `step.delta`, `interaction.completed`, `error`). Gli eventi che non modificano lo state machine (`step.start`/`step.stop`, `interaction.status_update`) non sono gestiti; le terminal failure detection passa dal polling di `client.interactions.get()` come prima. Inner delta type discriminators per `step.delta` (per la union `StepDelta.*`): `text` / `thought_summary` / `image` / `text_annotation_delta` / vari tool deltas. Il citation streaming espande `d.annotations[]` (array di `URLCitation` con `{url, title}` o `FileCitation` con `{document_uri, title}`).
   - **`absorbOutputs` rinominata `absorbSteps`**: discrimina su `step.type === 'model_output'` (legge `content[]` Content_2 union) e `step.type === 'thought'` (legge `summary[]`); skippa esplicitamente tutti i tool call/result step (10 varianti totali: function/code_execution/url_context/google_search/file_search/mcp_server_tool/google_maps + user_input). Citazioni dentro `TextContent.annotations[]` raccolte inline. Tracking unknown step types preservato via `unknownOutputTypes` Set per refinement futuro.
   - **3 callsites** (handler `completed`, handler `failed`, final sweep) aggiornati da `status.outputs` a `status.steps`.

3. **Niente cambiamenti lato request**. La `client.interactions.create()` corrente non usa parametri deprecati (`response_mime_type`, `generation_config.image_config`); il payload `agent_config` di Deep Research Max e' invariato. La create call rimane:
   ```js
   client.interactions.create({
     input: prompt,
     agent: 'deep-research-max-preview-04-2026',
     background: true,
     store: true,
     stream: true,
     agent_config: { type: 'deep-research', thinking_summaries: 'auto', visualization: 'auto', collaborative_planning: false },
   });
   ```

**Note operative**:
- OpenAI / GPT-5.5 Pro non e' coinvolto da questi cambiamenti: e' una API diversa (Responses API), gestita lato OpenAI con un suo lifecycle indipendente.
- Il sito web (`magellan-web/`) consuma i file `validation-gemini.md` downstream, il cui formato Markdown e' invariato. Nessuna modifica needed lato web.
- Verifica end-to-end: lo stderr durante una sessione reale deve mostrare `Interaction: <id>` (event `interaction.created` riconosciuto), `Report streaming` (event `step.delta` con inner type `text`/`output_text`), `interaction.completed` a fine corsa. La presenza di righe `unknown delta types seen` o `unknown output types seen` indica field che la v2 ha aggiunto e che vanno gestiti in un follow-up.
- Dependency note: il bump trascina `protobufjs` ad una versione con CVE critica pendente (GHSA-xq3m-2v4x-88gg, "Arbitrary code execution in protobufjs"). Non bloccante per la pipeline (transitive runtime dep di `@google/genai`); valutare upgrade separato via `npm audit fix` o waiting su un patch upstream.
- **Smoke test eseguito**: prima del merge ho aperto un'interaction reale con il prompt `Briefly characterize UCP1-driven thermogenesis...`, consumato 5 eventi, cancellato. Verificato che SDK 2.1.0 accetta la create call con `agent: 'deep-research-max-preview-04-2026'`, e gli eventi reali sono: `interaction.created` -> `interaction.status_update` (status='in_progress') -> `step.start` (step.type='thought') -> `step.delta` (delta.type='thought_summary' con `content.text`) -> `step.delta` (delta.type='thought_signature'). Questa run ha esposto un ultimo bug: `thought_signature` (hash di validazione backend) e i deltas dei tool autonomi (`arguments_delta`, vari `*_call`/`*_result`) sarebbero finiti in `unknownDeltaTypes` con log spam su stderr durante una sessione lunga. Aggiunto skip esplicito di tutte queste varianti di `StepDelta` (no-op silenzioso). Il `client.interactions.cancel()` ha restituito 500 con messaggio benigno "You will not be charged", non bloccante per il pipeline (la connection drop sufficient a fermare il cost meter).

**File modificati**:
- `package.json` -- `@google/genai` da `^1.45` a `^2.0.0`
- `package-lock.json` -- aggiornato da `npm install` (`@google/genai` 1.46.0 -> 2.1.0; transitive deps cambiate)
- `scripts/validate-crossmodel.mjs` -- top comment block + commento GEMINI_AGENT + `consume()` su eventi v2 + `absorbOutputs` rinominata `absorbSteps` (iteration su `step.content[]`, skip dei server-tool step types) + 3 callsites `status.outputs` -> `status.steps`
- `docs/CHANGELOG.md` -- questa entry

---

## v5.26: Upload script auto-discovery dei file `.md` (6 maggio 2026)

**Motivazione**: La sessione `2026-05-05-targeted-031` (TheraSAM, SFRT × PDAC) ha rivelato un bug latente in `scripts/upload-session.mjs`: la lista hardcoded `mdMappings` era incompleta e diversi file critici della pipeline non venivano caricati sul sito web. File mancanti dall'upload: `raw-hypotheses-cycle1.md`, `raw-hypotheses-cycle2.md` (le ipotesi originali H1-H13 incluse le 3 uccise dal critic in cycle 2), `critiqued-cycle2.md` (mismatch di naming: lo script si aspettava `critique-cycle2.md` o `cycle2-critique.md`, l'agente scriveva `critiqued-cycle2.md`), `ranked-cycle2.md` (cycle 2 ranking completamente assente dalle mappature — solo cycle 1 era mappato), `convergence.md` (output post-QG del Convergence Scanner), `contributor-context.md` (CRITICO per sessioni guidate `--context` come questa). Il problema era invisibile perché lo script falliva silenziosamente sui mapping mancanti.

**Decisione**: Refactoring di `scripts/upload-session.mjs` da whitelist hardcoded a auto-discovery. Lo script ora legge `fs.readdirSync(dir).filter(f => f.endsWith('.md'))` e carica ogni file come entry in `pipelineNarratives`, con la chiave derivata dal filename stem. **Gli alias mappano gli stem agent-written sui nomi canonici che il frontend `magellan-web/app/sessions/[id]/page.tsx::PHASE_ORDER` si aspetta** (es. `critiqued-cycle1` → `critique-cycle1`; `ranked-cycle1` → `ranking-cycle1`; `cycle1-evolved` / `evolution-cycle1` → `evolved-cycle1`; `literature-landscape` → `literature-context`; `raw-hypotheses-cycle{1,2}` → `hypotheses-cycle{1,2}`). Direzione invertita rispetto al primo tentativo: il contratto col frontend ha priorità sullo stem del file. Skiplist svuotata: il frontend renderizza esplicitamente `export-gpt`/`export-gemini` come "GPT/Gemini Validation Prompt" sections, quindi vanno caricati.

**Cosa NON viene caricato (per design)**: il file `meta-insights.json` è cumulativo e forward-looking (strategy_performance, recurring_failure_modes, lezioni che alimentano Scout/Generator in sessioni future), non session-specific. Il contenuto session-specific per la pagina del sito è già in `session-analysis.md` caricato come `pipelineNarratives['session-analysis']`. Lo slot DB `sessionAnalysis` resta NULL per le sessioni v5.13+ — non serve duplicare contenuto in formato strutturato che a un visitatore non interessa.

**Coordinato con frontend** (`magellan-web@c58493e..`): PHASE_ORDER esteso con `convergence` (Convergence Scanning, post-QG agent v5.13) e `contributor-context` (in evidenza nella hero come pannello sextant-gold per sessioni guidate CC-BY-4.0); session-summary appare ora come voce espandibile del pipeline journey con `defaultOpen=true`, sostituendo il vecchio snippet di 15 righe nella hero con un CTA testuale "READ FULL SESSION SUMMARY ↓" che fa scroll-anchor alla card completa (`scroll-mt-24` per offset header). Le card del journey ora hanno `id="phase-{key}"` ancorabile.

**Effetto sulla sessione 2026-05-05-targeted-031**: 12 narrative caricate originariamente → 19 narrative dopo re-upload con script corretto. Aggiunte: `contributor-context`, `convergence`, `critiqued-cycle2`, `ranked-cycle2`, `raw-hypotheses-cycle1`, `raw-hypotheses-cycle2`. La sessione è stata re-uploadata e ora il backend possiede tutti i contenuti (frontend del sito magellan-discover.ai deve essere aggiornato separatamente per renderizzare le nuove chiavi e mettere in evidenza `contributor-context` per sessioni guidate).

**Vantaggi forward-compatibility**: ogni nuovo `.md` che la pipeline produce in futuro viene caricato automaticamente, senza modifiche allo script. Il principio "primary deliverable = markdown narrative" del v5.18+ è ora rispettato end-to-end fino al sito.

**Documentazione**:
- `CLAUDE.md` -- nuovo principio "Upload script auto-discovers `.md` files" nella sezione Operational
- `.claude/agents/discovery-orchestrator.md` -- DELIVERABLES VERIFICATION estesa (aggiunge cycle2 + post-QG + guided sections); aggiunta sezione "Pre-Upload Narrative Audit" con check Bash auto-discovery prima del run di upload-session.mjs

**File modificati**:
- `scripts/upload-session.mjs` -- mdMappings sostituito da auto-discovery + NARRATIVE_ALIASES + NARRATIVE_SKIPLIST
- `.claude/agents/discovery-orchestrator.md` -- DELIVERABLES VERIFICATION rivista; nuova sezione Pre-Upload Narrative Audit
- `CLAUDE.md` -- principio operativo aggiornato

---

## v5.25: Migrazione a GPT-5.5 Pro (28 aprile 2026)

**Motivazione**: Il 28 aprile 2026 OpenAI ha rilasciato `gpt-5.5-pro`, il nuovo modello di punta sulla Responses API (snapshot `gpt-5.5-pro-2026-04-23`, context 1.05M token, output max 128k, knowledge cutoff dicembre 2025). Il Cross-Model Validator di MAGELLAN passa da `gpt-5.4-pro` a `gpt-5.5-pro`. Il nuovo modello introduce quattro vincoli operativi che cambiano la forma del codice: (a) niente streaming, quindi background submit + polling; (b) latenze multi-minuto (decine di minuti tipici, fino a ore); (c) prompt guidance outcome-first che deprecano i pattern legacy (Output Contract, ALWAYS/NEVER, Completeness Checklist); (d) un terzo tool disponibile, `shell`, accanto a `web_search_preview` e `code_interpreter`.

**Decisioni**:

1. **`scripts/validate-crossmodel.mjs::callOpenAI` riscritta**. Pattern submit + poll, mirror del lato Gemini: `client.responses.create({ ..., background: true, store: true })`, poi loop di `client.responses.retrieve(id)` ogni 30 secondi fino a stato terminale. Stati gestiti: `completed` (estrae output), `incomplete` (estrae l'output parziale presente in `response.output[]` e ritorna `status: 'partial'` con `incomplete_reason`), `failed` / `cancelled` (throw e rinomina del response-id file in `.response-id.failed` per forensics). Counter `web_searches` / `code_executions` / `shell_executions` derivati contando gli item type in `response.output[]` finale.

2. **Reasoning effort `xhigh`** con fallback automatico a `high`. Valori accettati da gpt-5.5-pro: `medium`, `high`, `xhigh`. Lo script usa `xhigh` (massimo) di default; se per qualche motivo l'API restituisce 400 menzionando `reasoning`/`effort`/`xhigh`, fa un singolo retry con `effort: 'high'` e logga la downgrade su stderr.

3. **`shell` come terzo tool**. `OPENAI_TOOLS` contiene `web_search_preview` (high), `code_interpreter` (auto container), e `shell`. Il nome del tool nell'API e' `shell` (non `hosted_shell`). L'estrazione gestisce sia `shell_call` (la richiesta del modello) che `shell_call_output` (paired item con `stdout`/`stderr`/`outcome.exit_code`), che vengono renderizzati in una sezione "Shell Execution Outputs" del markdown finale.

4. **Persistenza response.id + auto-resume**. Subito dopo `create()` lo script scrive `response.id` su `${outputFile}.response-id`. All'avvio, se quel file esiste, il polling riparte da quell'id invece di sottomettere una nuova request. Su `completed` il file viene cancellato; su `failed`/`cancelled` rinominato `.response-id.failed`; su `incomplete` rinominato `.response-id.incomplete`. Sul wall-clock cap di 4 ore lo script NON cancella la response su OpenAI: la lascia retrievable e logga istruzioni di recovery. Cosi' una sessione che va oltre 60 minuti (o anche oltre 4 ore) non viene mai persa: il bash background task killato (Ctrl+C, parent death) si recupera rilanciando lo script.

5. **Wall-clock cap esteso da 45 min a 4 ore**. SDK timeout impostato a `cap + 5 min` per non scattare prima del nostro check.

6. **Prompt template ristrutturato per le GPT-5.5 prompt guidance**. `prompts/validation-prompt-gpt.md` riscritto in stile outcome-first ("Shorter, outcome-oriented prompts: describe what good looks like, what constraints matter, what evidence is available"; "Avoid carrying over every instruction from an older prompt stack"). Eliminati: Output Contract con sezioni obbligatorie, Behavioral Constraints in stile ALWAYS/NEVER, Completeness Checklist. Mantenuti come outcome statements: dimensioni da coprire (Novelty / Counter-evidence / Mechanism plausibility / Experimental design / Final assessment), groundedness (no fabricated URLs, citation only of retrieved sources), arithmetic verification via code, "INSUFFICIENT DATA" come outcome valido.

7. **`scripts/validate-gpt54.mjs` rimosso**. Era un fallback ad-hoc per gli errori "terminated" di gpt-5.4-pro; non ha caller esterni e non si applica a gpt-5.5-pro.

8. **Pricing context**: gpt-5.5-pro costa $30/$180 per 1M token vs $5/$15 di gpt-5.4-pro standard (~6x). Accettato come costo del nuovo frontier; non blocca la pipeline.

9. **Docs sync** (CLAUDE.md architecture table + cross-model validation principle; README.md setup + phase 7 + tree + summary; methodology-v5.md ASCII diagram + agent table + Cross-Model Validator description + frontier-models claim + template description + external models table + reference benchmarks con nuova entry GPT-5.5 Pro + risk-table mitigation + operational pointer; `.claude/agents/cross-model-validator.md`; `.claude/commands/export.md`; `prompts/orchestration-guide.md` italiano + `prompts/session-summary-format.md`).

**File modificati**:
- `scripts/validate-crossmodel.mjs` (callOpenAI riscritta)
- `scripts/validate-gpt54.mjs` (rimosso)
- `prompts/validation-prompt-gpt.md` (ristrutturato outcome-first)
- `prompts/orchestration-guide.md`
- `prompts/session-summary-format.md`
- `.claude/agents/cross-model-validator.md`
- `.claude/commands/export.md`
- `CLAUDE.md`
- `README.md`
- `docs/methodology-v5.md`
- `docs/CHANGELOG.md` (questa entry)

**Note operative**:
- `code_interpreter_call.outputs` e' `null` in background mode: lo stdout dell'esecuzione non e' esposto in `response.output[]`, ma il modello referenzia i valori computati nel `message.output_text` finale (che e' quello che il Cross-Model Validator agent legge per il consensus report). Il `code` field con il sorgente Python e' preservato.
- Il prompt di validazione ristrutturato e' moderato: comportamento empirico va osservato sulle prime sessioni reali per capire se serve aggiungere/togliere guidance.

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
