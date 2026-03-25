# Literature Context: 6-Candidate Disjointness Verification
## Session: session-20260325-000727 | Date: 2026-03-25

> **MCP Status:** Semantic Scholar MCP rate-limited (all 6 parallel calls failed). PubMed MCP returned empty/garbage results.
> Fell back to WebSearch + WebFetch for all retrieval. WebFetch returned 403 for several paywalled papers; PMC alternatives used where available.

---

## CANDIDATE T1: Percolation Theory × T Cell Infiltration

### Field A: Statistical Physics — Percolation Theory on Collagen Lattices

**What exists:**
- Percolation theory is a mature field (bond/site percolation on random lattices, p_c, correlation length exponent ν ~ 0.88 in 3D)
- Anomalous diffusion on percolation clusters is well-characterized near p_c
- Finite-size scaling theory for predicting threshold behavior

**Recent Breakthroughs (2024–2025):**
- Percolation theory broadly applied to disordered networks in biology (e.g., vascular networks)
- No specific 2024–2025 breakthrough in physical percolation relevant to ECM

### Field C: Tumor Immunology — T Cell Exclusion by ECM

**What exists:**
- Collagen density regulates T cell activity (PMC6417085, 2019)
- Tumor stiffening via LOX crosslinking inhibits T cell infiltration (Nicolas-Boluda 2021, eLife)
- Macrophages shape collagen topography to dictate T cell localization (Science Immunology, 2025)
- Collagen III deposition creates intermingled networks that FAVOR T cell infiltration; dense parallel fibers EXCLUDE T cells

**Recent Breakthroughs (2024–2025):**
- Science Immunology 2025: Macrophages control fibrillar collagen topography via Tcf4-Collagen3 axis
- Collagen dynamics in breast cancer TME and therapeutic perspectives (Springer 2025)
- LOX/LOXL1 restrict CD8+ T cell infiltration in colorectal cancer (2024)

### Existing Cross-Field Work

**One paper exists at the intersection:**
- Ashworth et al. 2015 (Adv Healthcare Mat, PMID 25881025): "Cell Invasion in Collagen Scaffold Architectures Characterized by Percolation Theory"
  - **What it does:** Applies site/pore percolation to characterize scaffold interconnectivity for generic connective tissue cell invasion in tissue engineering scaffolds
  - **What it does NOT do:** Study T cells, tumor ECM, bond percolation on crosslinking networks, LOX as bond probability, immune exclusion thresholds

**No other cross-field papers found.**

### Key Anomalies
- Collagen density predicts immune exclusion but there is no quantitative threshold model — a percolation threshold would provide exactly this
- LOX crosslinking increases stiffness continuously, but immune exclusion appears threshold-like (tumor "deserts" vs "inflamed" tumors)

### Disjointness Assessment
- **Status: PARTIALLY_EXPLORED**
- **Evidence:** One 2015 paper applies percolation to generic cell invasion in engineered collagen scaffolds. The tumor immunology community has characterized LOX-T cell connections empirically. These two bodies of literature have NOT been connected.
- **Implication:** The hypothesis has moderate novelty. The percolation framework applied to T cell-specific immune exclusion in tumor ECM with bond percolation (LOX as bond) is new, but the searcher will find Ashworth 2015 as a precedent. Generator should acknowledge this prior work and explain what's fundamentally different (bond vs. site percolation, immune cell vs. generic cell, tumor ECM vs. engineered scaffold, LOX as bond probability mechanism).

---

## CANDIDATE T2: Acoustic Filter-Bank Theory × Plant Sound Detection

### Field A: Acoustic Engineering — Matched-Filter Detection and Filter-Bank Architecture

**What exists:**
- Matched-filter detection theory: SNR = 2E/N₀, maximized when filter is matched to signal
- Parallel filter-bank architectures: multiple bandpass filters with different center frequencies and bandwidths processing the same input simultaneously
- Well-developed in hearing research (cochlea as biological filter bank), radar, communications

**No recent breakthroughs relevant to plant biology.**

### Field C: Plant Bioacoustics — Detecting Airborne Ultrasonic Stress Emissions

**What exists:**
- Plants emit airborne ultrasonic sounds under stress (20–150 kHz, peaks at 40–80 kHz): confirmed by multiple labs 2019–2024
- Source: xylem cavitation (Bonisoli 2024, Plant Signal Behav)
- Plants can respond to external sounds: MCA2 channel activation → Ca²⁺ influx → CPK29 signaling → auxin transport (PMC reports, 2020–2024)
- MSL10 participates in wound signaling and perception of mechanical oscillations caused by wind (PNAS 2021)
- MSL10 frequency response: channel kinetics characterized at 1 Hz, 3 Hz, 30 Hz using High-Speed Pressure Clamp
- Merdan & Akan 2025 (arXiv 2512.01096): first end-to-end acoustic communication model for plants; uses biological kinetic models, NOT filter-bank/matched-filter theory
- Plant-animal acoustic interaction confirmed 2025 (phys.org): moths avoid plants emitting stress sounds

**Recent Breakthroughs (2025):**
- First evidence of auditory interaction between plants and animals (2025)
- First end-to-end acoustic communication model for plants (arXiv 2512.01096)

### Existing Cross-Field Work

**None found.** No paper applies:
- Matched-filter theory to plant sound detection
- Filter-bank architecture to MSL channel diversity
- SNR analysis of plant-to-plant acoustic communication
- Trichome resonant frequency analysis

### Key Anomalies
- MSL channels have diverse kinetic properties (frequency response characterized at 1–30 Hz in patch-clamp) — suggesting frequency discrimination is possible but unexplored
- Plants respond to specific frequencies (200 Hz modeled by Merdan & Akan) — mechanism for frequency selection unknown
- Multiple MSL paralogues (MSL2, 3, 9, 10) form heteromeric channels with different properties — parallel bank architecture unexplored

### Disjointness Assessment
- **Status: DISJOINT**
- **Evidence:** Extensive search of both plant bioacoustics and acoustic engineering literature found ZERO papers connecting filter-bank/matched-filter theory to plant mechanosensitive channel architecture. The most recent plant acoustics paper (arXiv 2512.01096, 2025) explicitly uses biological models, not the engineering framework.
- **Implication:** Strong novelty. Generator should build on MSL10 kinetics data (PNAS 2021) and the multiple MSL paralogues as the physical basis for a filter bank, with matched-filter SNR analysis for detecting intraspecific UEs.

---

## CANDIDATE T3: Jamming Phase Diagram × Chromatin Compaction

### Field A: Granular Physics — Jamming Transition, Liu-Nagel Phase Diagram

**What exists:**
- Liu-Nagel jamming phase diagram (1998, Nature): axes of density (φ), temperature (T), applied stress (Σ); jamming point J
- Jamming criticality: contact number z → z_c, diverging length scales, force chain emergence
- Edwards entropy (compactivity) as thermodynamic framework for jammed states
- Jamming applied to CELLS in tissues: well-established (2015–2025), Quanta Magazine feature, multiple reviews

**Recent work applying jamming to biology:**
- Cell-level jamming in epithelial monolayers, cancer metastasis, embryogenesis (extensively reviewed 2021–2025)
- Key insight from literature: "Cell jamming theories consistently emphasize cell shapes rather than nucleus shapes because whole cells are volume-filling the tissue"

### Field C: Chromatin Biology — Eu/Heterochromatin Transitions

**What exists:**
- Chromatin described as liquid-like (euchromatin) vs. gel-like (heterochromatin) — Bhattacharjee-style analogy
- Phase separation models dominant: Bajpai 2021 (eLife), HP1-driven liquid-liquid LLPS, condensate formation
- Active hydrodynamic theory: Rautu et al. 2025 (arXiv 2503.20964) — no jamming
- Chromatin heterogeneity modulates condensate dynamics (Nature Comms 2025)
- Chromatin condensate material properties: liquid-like in diverse conditions (PNAS 2023)
- Science 2025: Multiscale structure explains phase separation and material properties

**Recent Breakthroughs (2024–2025):**
- arXiv 2503.20964 (Rautu 2025): most advanced active hydrodynamic theory — uses phase separation, NOT jamming
- Nature Comms 2025: Condensate dynamics modulated by epigenetics — liquid-to-gel transition characterized, no jamming
- Science Advances 2025: Replication-dependent histone labeling reveals euchromatin/heterochromatin physical properties in living cells

### Existing Cross-Field Work

**None found.** "Jamming" applied to chromatin within the nucleus does not appear in any paper found. The search explicitly confirmed:
- "Jamming transition in cancer" papers focus on CELL-LEVEL jamming in tissues
- Nucleus-level jamming is mentioned only as a corollary to cell jamming ("nuclei influenced by cytoskeletal tension")
- NO paper applies Liu-Nagel diagram, z_c, force chains, or Edwards entropy to chromatin compaction

### Key Anomalies
- The eu/heterochromatin transition is abrupt (transcriptional activation/silencing) yet current models treat it as a continuous phase separation — a jamming threshold would explain abruptness
- HP1-driven bridging interactions increase with heterochromatin formation — analogous to increasing contact number z approaching z_c
- Force-chain-like transmission of mechanical stress through heterochromatic regions is observed but unmodeled

### Disjointness Assessment
- **Status: DISJOINT**
- **Evidence:** Jamming literature applied to cells in tissues is well-explored; chromatin physics literature uses phase separation and active matter frameworks. The intersection (Liu-Nagel jamming applied to nucleosome arrays within the nucleus) is completely absent.
- **Implication:** High novelty. The structural analogy is compelling: nucleosome stacks as jammed particles, HP1 bridging interactions as bond contacts, nuclear tension as applied stress. Generator should map Liu-Nagel axes explicitly onto chromatin parameters.

---

## CANDIDATE T4: Thermodynamic Uncertainty Relation × Bacterial Cell Size Homeostasis

### Field A: Stochastic Thermodynamics — TUR and Entropy Production Bounds

**What exists:**
- TUR (Barato & Seifert 2015): CV² × σ̇ × τ ≥ 2kT — fundamental bound on precision vs. entropy cost
- Applied to: biochemical clocks (Marsland 2019), molecular motors, signaling systems, active matter
- Extended TUR for active systems, inverse TUR, TUR for active Ornstein-Uhlenbeck particles (2024–2025)
- TUR applied to cell signaling information transmission (Verma 2025, bioRxiv): yeast TF localization

**Recent Breakthroughs (2024–2025):**
- Verma 2025: TUR constrains information transmission in yeast transcription factor systems
- Extended TUR for active systems (PMC12202210)
- Inverse TUR and entropy production: Phys. Rev. Lett. 2025

### Field C: Bacterial Cell Biology — Cell Size Homeostasis via Adder Model

**What exists:**
- Adder model: cells add constant size (ΔV) between divisions regardless of birth size — achieved homeostasis
- DnaA-ATP initiates replication; DnaA/cell number correlates with cell volume
- Stochastic models of adder: master equation framework (ScienceDirect 2025), precision-metabolism trade-off found
- Nonlinear memory in cell division across species (PNAS 2025)
- Growth rate sets cell size (nutrient-dependent); cell size scales with growth rate
- Stochastic thermodynamics applied to cell size models (sizer, timer, adder): entropy production analysis shows "entropy production of resetting is negative, branching is positive"

**Recent Breakthroughs (2024–2025):**
- 2025 paper applies stochastic thermodynamics framework to adder/sizer/timer models — closest existing work
- Shows precision-metabolism trade-off in cell division timing
- BUT: uses general entropy production formalism, NOT the TUR bound specifically

### Existing Cross-Field Work

**One near-miss found:**
- An unnamed 2025 paper applies stochastic thermodynamics to cell size models, finding a "precision-metabolism trade-off where suppressing timing variability requires costly protein overproduction"
- This is thermodynamically adjacent to TUR but uses a different formalism (entropy production without the TUR inequality)
- Does NOT connect to DnaA-ATP as the molecular counter
- Does NOT use growth rate as a dissipation proxy
- Does NOT apply TUR inequality (CV² × σ̇ × τ ≥ 2kT) explicitly

**No paper connects TUR specifically to the adder model or DnaA counting.**

### Key Anomalies
- Bacteria achieve remarkable cell size precision (CV of added volume ~ 15-20%) at substantial metabolic cost — TUR predicts this trade-off but hasn't been applied
- DnaA-ATP hydrolysis during replication initiation is a dissipative, irreversible process — making it an ideal TUR "current"
- Nutrient-dependent growth rate sets both the precision (CV) and dissipation rate — a direct test of TUR

### Disjointness Assessment
- **Status: DISJOINT**
- **Evidence:** TUR has been applied to oscillators, motors, signaling, and active matter — but NOT to the bacterial cell size adder model specifically. The closest paper (stochastic thermodynamics of cell size models) uses a different formalism without the TUR inequality. No paper identifies DnaA-ATP as the TUR current for size homeostasis.
- **Implication:** Highest novelty of all 6 candidates. Both fields are mature, quantitative, and increasingly overlapping — but the specific TUR bridge to the adder model has not been made. This is a clean, falsifiable, mechanistically specific hypothesis.

---

## CANDIDATE T5: FLIM Metabolic Imaging × Bacterial Persisters

### Field A: Optical Metabolic Imaging — FLIM NADH/FAD

**What exists:**
- FLIM phasor metabolic fingerprinting of bacteria (Bhattacharjee 2017): NADH autofluorescence, phasor approach, 5 species
- Rapid antibiotic susceptibility testing by FLIM metabolic tracking (ACS Infect Dis 2024, PMID 39572010): differentiates susceptible/resistant phenotypes in 10 min
- FLIM-AST device for antibiotic susceptibility testing (UC Irvine tech transfer)
- FLIM for organoid metabolism (PMC 2023)
- FLIM for P. aeruginosa biofilm cross-feeding detection (ACS Infect Dis 2024)
- Phasor analysis: maps free/bound NAD(P)H ratio without model fitting

**Recent Breakthroughs (2024–2025):**
- ACS Infectious Diseases (2024): FLIM tracking of bacterial metabolism for antibiotic susceptibility — **directly addresses antibiotic tolerance**
- FLIM-AST for rapid phenotyping

### Field C: Antimicrobial Resistance — Persister Cell Metabolic Transitions

**What exists:**
- Persisters are low-ATP, slow-growing cells (PLoS Biology 2022): stochastically formed subpopulation
- Persister cell histories in mother-machine: diverse survival modes revealed (eLife 2022, PMC 8994058)
- Bacterial persisters review 2024 (Signal Transduction): molecular mechanisms, metabolic states
- G3P metabolism, aerobic respiration, TCA cycle implicated in persister dormancy (2024)

### Existing Cross-Field Work

**PARTIALLY EXPLORED — Scout's flag confirmed:**
- **Bhattacharjee 2017:** FLIM phasor metabolic fingerprinting of bacteria — foundational, but NOT persister-specific (endpoint snapshots only)
- **ACS Infect Dis 2024 (PMID 39572010):** FLIM metabolic tracking for antibiotic susceptibility — addresses tolerance phenotype, but not specifically persister transition dynamics; no mother-machine
- **Conceptual overlap exists** but the specific experimental design (phasor-FLIM + mother-machine for real-time persister TRANSITION tracking) is not published

### Key Anomalies
- FLIM can distinguish metabolic states in bacteria but has not been combined with mother-machine for longitudinal single-cell tracking
- Persister formation is a stochastic, rare event — mother-machine + FLIM would be the ideal platform to catch it in real time
- The cancer DTP (drug-tolerant persister) analogy suggests conserved mechanisms worth exploring with optical metabolic imaging

### Disjointness Assessment
- **Status: PARTIALLY_EXPLORED**
- **Evidence:** FLIM applied to bacterial metabolism is established (2017, 2024). FLIM for antibiotic susceptibility testing exists. These papers have NOT specifically combined phasor-FLIM with mother-machine microfluidics for real-time tracking of the stochastic persister transition event.
- **Implication:** Scout's PARTIALLY_EXPLORED flag is correct. The building blocks exist; the integration is novel. Generator should be explicit about prior art (Bhattacharjee 2017, ACS 2024) and what makes the T5 hypothesis distinct (longitudinal phasor trajectory, mother-machine, pre-persister NADH signature).

---

## CANDIDATE T6: Classical Nucleation Theory × Ferroptosis Iron Release

### Field A: Physical Chemistry — CNT and Ostwald Ripening

**What exists:**
- Classical nucleation theory (CNT): Gibbs free energy barrier, critical nucleus radius r* = 2γΩ/kT·ln(S), nucleation rate J ~ exp(-ΔG*/kT)
- Gibbs-Thomson effect: solubility of nanoparticles increases with decreasing size
- Ostwald ripening: smaller crystals dissolve, larger ones grow — LSW theory (1/r³ coarsening)
- Ferritin iron mineralization: **2025 JACS papers directly address nucleation in ferritin**
  - "Mechanism of Mineral Nucleation and Growth in a Mini-Ferritin" (JACS 2025): nucleation at acidic 3-fold pores, Ostwald ripening of nascent mineral from nucleation site to core
  - "Assembly of Nascent Mineral Core at the Nucleation Site of Human Mitochondrial Ferritin" (JACS 2025): cryo-EM characterization of nucleation site

**Recent Breakthroughs (2025):**
- Two JACS 2025 papers characterize the nucleation mechanism in ferritin at atomic resolution
- Ostwald ripening within ferritin confirmed experimentally
- Ferrihydrite nucleation at acidic pores of ferritin characterized kinetically

### Field C: Ferroptosis Biology — Ferritin to Labile Iron Pool Transition

**What exists:**
- NCOA4-mediated ferritinophagy as dominant source of labile iron (conventional model)
- LIP dynamics DO NOT measurably increase during ferroptosis induction (Ponnusamy 2025, biorxiv/PMC12236665) — challenges dominant model
- Ferroptosis iron sources are "multisourced" — ferritin, lysosomes, mitochondria, heme, Fe-S clusters
- NCOA4 recognizes FTH1, mediating autophagosome sequestration; lysosomal acidification (cathepsin B) triggers ferritin degradation → Fe³⁺ release → Fe²⁺ (by ferroreductases) → Fenton reaction
- Ferritin L subunits associated with "nucleation center" for iron storage (noted in ferroptosis review)

**Recent Breakthroughs (2024–2025):**
- Ponnusamy 2025: LIP does NOT expand during ferroptosis — mechanistic gap opened
- Signal Transduction 2024 review: multisourced iron model
- Frontiers 2025: Ferroptosis at a crossroads — 5 fundamental unanswered questions

### Existing Cross-Field Work

**None found.** No paper applies:
- CNT (Gibbs-Thomson, critical nucleus radius, dissolution rate law) to ferritin iron release during ferroptosis
- Ostwald ripening between ferritin cores (smaller ferritin → larger ferritin stealing iron)
- Supersaturation kinetics to Fe²⁺ release into the LIP under lysosomal pH shift
- NCOA4 ferritinophagy as pH-triggered dissolution modeled thermodynamically

### Key Anomalies
- Ferrihydrite dissolution from ferritin under lysosomal pH should follow nucleation-like kinetics (pH shift from 7.4 to 4.5 dramatically changes iron solubility and Fe³⁺/Fe²⁺ thermodynamics) — but this has NEVER been modeled as a dissolution kinetics problem
- Ostwald ripening between ferritin cores (larger, more stable ferrihydrite cores stealing iron from smaller, less stable ones) could explain why LIP doesn't accumulate continuously — directly relevant to Ponnusamy 2025 finding
- The JACS 2025 ferritin nucleation papers exist completely separately from ferroptosis biology

### Disjointness Assessment
- **Status: DISJOINT**
- **Evidence:** CNT/Ostwald ripening applied to ferritin mineral chemistry exists (JACS 2025). Ferroptosis iron release biology is active and questioning its own assumptions (Ponnusamy 2025). The thermodynamic bridge (dissolution kinetics of ferritin iron core under lysosomal conditions modeled as reverse nucleation) is completely absent from both literatures.
- **Implication:** High novelty. The Ponnusamy 2025 finding (LIP doesn't expand as expected) is an anomaly that the CNT framework could explain. Strong candidate for a mechanistically grounded hypothesis.

---

## Cross-Candidate Comparison

| Candidate | Status | Novelty Score | Mechanistic Specificity | Evidence Quality |
|-----------|--------|--------------|------------------------|-----------------|
| T1: Percolation × T cell | PARTIALLY_EXPLORED | Medium | High (bond p_c) | Strong (Ashworth 2015 precedent) |
| T2: Acoustic filter-bank × Plant sound | DISJOINT | Very High | High (matched filter SNR) | Good (MSL10 kinetics exist) |
| T3: Jamming × Chromatin | DISJOINT | High | High (z_c, force chains) | Strong (two fields mature) |
| T4: TUR × Bacterial cell size | DISJOINT | Very High | Very High (CV², DnaA-ATP) | Very Strong (both fields quantitative) |
| T5: FLIM × Bacterial persisters | PARTIALLY_EXPLORED | Medium | Medium (phasor trajectory) | Fair (several existing papers) |
| T6: CNT × Ferroptosis | DISJOINT | High | High (r*, dissolution kinetics) | Strong (JACS 2025 nucleation papers + Ponnusamy 2025 anomaly) |

---

## Full-Text Papers Retrieved

1. `papers/marsland2019-TUR-biochemical-oscillations.md` — TUR in biochemical oscillators; confirms TUR NOT applied to cell size homeostasis
2. `papers/bhattacharjee2017-FLIM-bacterial-metabolism.md` — Foundational FLIM phasor metabolic fingerprinting; no persister-specific analysis
3. `papers/bonisoli2024-plant-ultrasound-detection.md` — Plant UE detection methodology; external detection, no filter-bank
4. `papers/ponnusamy2025-LIP-dynamics-ferroptosis.md` — LIP does not expand during ferroptosis; opens mechanistic gap for T6
5. `papers/bajpai2021-chromatin-phase-separation-elife.md` — Chromatin phase separation; polymer model, no jamming
6. `papers/rautu2025-chromatin-active-hydrodynamics.md` — Latest chromatin active matter theory; no jamming framework
7. `papers/nicolas-boluda2021-LOX-collagen-T-cell-migration.md` — LOX inhibition improves T cell migration; no percolation framework
8. `papers/ashworth2015-percolation-collagen-cell-invasion.md` — Only paper applying percolation to collagen; generic cells, not T cells
9. `papers/merdan2025-acoustic-communication-model-plants.md` — First plant acoustic communication model; no filter-bank theory
10. `papers/marsland-tur-cell-signaling-2025.md` — TUR applied to signaling; confirms NOT applied to cell size

---

## Gap Analysis

### What's Been Explored
- Collagen as T cell barrier (well-established)
- LOX crosslinking and T cell exclusion (multiple papers, including therapeutic interventions)
- Cell invasion in collagen scaffolds using percolation (Ashworth 2015)
- Plant ultrasonic emissions: existence, frequency, source (xylem cavitation)
- Plant responses to sound: MCA2 channels, Ca²⁺ signaling
- Cell-level jamming in tissues (extensively reviewed)
- Chromatin phase separation and condensates (extensive 2020–2025 literature)
- TUR applied to: molecular motors, biochemical clocks, signaling systems
- Stochastic thermodynamics of cell size models (recently connected)
- FLIM metabolic fingerprinting of bacteria (2017–2024)
- FLIM for antibiotic susceptibility testing (2024)
- Ferritin iron mineralization via nucleation (JACS 2025 — just published)
- LIP dynamics during ferroptosis (Ponnusamy 2025 — just published, challenged conventional model)

### What's NOT Been Explored

**T1 Gap:** Bond percolation threshold as collagen crosslink density → T cell infiltration threshold. LOX crosslinking as bond probability p. Correlation length exponent predicting infiltration spatial geometry. Finite-size scaling to predict tumor size effects on immune desert boundaries.

**T2 Gap (cleanest):** Matched-filter detection theory applied to plant mechanosensitive channel architecture. Trichome resonant frequency as transducer. MSL2/3/9/10 as parallel filter-bank with different center frequencies and bandwidths. SNR of ultrasonic stress signal detection via matched filtering. Ca²⁺ frequency-selective signaling as spectral output.

**T3 Gap:** Liu-Nagel jamming phase diagram applied to chromatin within nucleus. Nucleosome arrays as jammed particles. HP1 bridging interactions as contact number z → z_c. Force chains in heterochromatin. Edwards entropy and compactivity of chromatin states. Nuclear tension as applied stress axis.

**T4 Gap (cleanest):** TUR inequality (CV² × σ̇ × τ ≥ 2kT) applied to bacterial cell size adder model. Growth rate as entropy proxy (σ̇). DnaA-ATP as the molecular current whose precision sets CV. Nutrient-dependent precision: higher growth rate → higher dissipation → tighter CV bound. Falsifiable prediction: CV_added × σ̇ × τ_generation = f(nutrient richness), testable with mother-machine + metabolic flux reporters.

**T5 Gap (narrower):** Phasor-FLIM + mother-machine for longitudinal real-time tracking of single-cell persister transition. Pre-persister NADH lifetime signature (predictive marker hours before commitment). Phasor trajectory showing commitment point.

**T6 Gap:** CNT applied to ferrihydrite dissolution from ferritin under lysosomal acidification. Gibbs-Thomson effect on nano-scale iron oxide cores in ferritin. Ostwald ripening between multiple ferritin cores explaining why LIP doesn't accumulate continuously (Ponnusamy 2025 anomaly). Critical pH for dissolution threshold modeled as nucleation/dissolution rate crossover.

### Most Promising Unexplored Directions (Ranked)

1. **T4 (TUR × Cell Size):** Both fields are the most quantitative; the bridge is mechanistically tight; DnaA-ATP as a TUR current is highly specific and falsifiable; nutrient experiments directly testable; no near-miss papers found.

2. **T6 (CNT × Ferroptosis):** The 2025 JACS ferritin nucleation papers and Ponnusamy 2025 LIP anomaly together create a perfect setup for a CNT hypothesis that explains an unexplained observation. High impact if correct (ferroptosis is therapeutically important).

3. **T3 (Jamming × Chromatin):** Clean disjoint; both fields mature; the structural analogy (nucleosome stacks as granular particles, HP1 as contact number) is compelling; active matter already applied to chromatin means physicists are interested in this space.

4. **T2 (Acoustic Filter-Bank × Plant Sound):** Completely disjoint; plant bioacoustics is a young, exciting field; MSL10 kinetic data provides an empirical foundation; matched-filter theory would provide the clearest mechanistic prediction (resonant frequencies of trichomes are measurable).
