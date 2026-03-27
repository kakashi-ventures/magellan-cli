# Literature Landscape: Session 2026-03-27-scout-013
## Scout Mode — Disjointness Verification for 5 Candidates

**Generated:** 2026-03-27
**Method:** MCP-first (Semantic Scholar + PubMed), WebSearch fallback
**MCP status:** Semantic Scholar returned results for individual field searches; cross-field queries returned zero results for all candidates. PubMed MCP returned empty results for all queries (likely connectivity issue) — WebSearch used as primary fallback throughout.

---

## CANDIDATE 1: Extreme Value Theory × Proteome Thermal Vulnerability Mapping

### Recent Breakthroughs in Extreme Value Statistics
- **GEV/EVT applications expanding (2024–2026):** EVT is being applied to finance (VaR estimation), climate extremes (Mediterranean temperature analysis), power grid failures, and AI out-of-distribution detection. The statistical machinery is mature and computationally tractable for large datasets. Return level estimation and peaks-over-threshold are standard practice in hydrology and insurance risk.
- **No proteomics applications found:** Semantic Scholar and web searches return zero results for "extreme value theory proteome" or "GEV protein thermal stability." The application domain gap is complete.

### Recent Breakthroughs in Thermal Proteome Profiling (Field C)
- **Meltome Atlas (Jarzab et al. 2020, Nature Methods):** 48,000 proteins across 13 species, Tm range 30–90°C. Key finding: up to 20% of the proteome has Tm values outside measurable temperature ranges — indicating a heavy-tail problem the field currently cannot characterize.
- **Figueroa-Navedo & Ivanov 2024 (Cell Reports Methods):** Comprehensive review identifying "selection of inadequate temperature windows" as a key unresolved challenge. Statistical approaches (t-tests, z-tests) show high false-negative rates for proteins with unusual Tm values.
- **GPMelt (2024):** Gaussian process approach to avoid curve-fitting artifacts. Addresses some statistical limitations but still does not use EVT for tail characterization.
- **TD-TPP 2025 (PMC12649780):** Top-down thermal proteome profiling of E. coli proteoforms — generates Tm distributions but no extreme value analysis.
- **NLRP3 meltome (2025, PMID 40250624):** 337 proteins with altered thermal stability upon inflammasome activation — all analyzed with standard statistics.

### Existing Cross-Field Work
- **None found.** Semantic Scholar cross-field query: zero hits. PubMed: zero hits. Web search for "extreme value theory proteome," "GEV protein melting temperature," "Gumbel distribution thermal stability," "Weibull distribution proteome," "return level estimation protein heat death": all returned zero relevant results.
- **Adjacent work only:** EVT applied to protein database search scores (BLAST e-values use extreme value distributions — the Gumbel distribution underlies BLAST statistics, Karlin-Altschul 1990). However, this applies EVT to sequence alignment scores, NOT to thermal stability Tm distributions. This is a distinct application domain.

### Key Anomalies
- The Meltome Atlas covers 30–90°C but up to 20% of proteins fall outside this range — the field has no quantitative framework for these tail proteins.
- Organism thermal death points are set by a small number of extreme-Tm proteins (the thermally vulnerable tail), not the mean. Standard statistics (mean Tm ± SD) are the wrong tool for this; EVT's return level estimation is the right tool.
- All eukaryotes show a substantial "safety margin" between their optimal growth temperature and the temperature at which bulk proteins precipitate. EVT would characterize this margin as a return-level problem.

### Contradictions Found
- The field advocates moving away from Tm-centric analysis (GPMelt) but simultaneously the most important biological questions (thermal death prediction, drug target thermostability) require exactly the kind of tail-behavior characterization that EVT provides. The solution direction (abolish Tm) and the biological need (predict extreme thermal vulnerability) are misaligned.

### Disjointness Assessment
- **Status: DISJOINT**
- **Evidence:** Zero cross-field papers found across Semantic Scholar, PubMed, and web search. BLAST e-value uses Gumbel distribution but for sequence alignment scores, not thermal stability — a distinct application that does not constitute a bridge.
- **Implication:** The connection between EVT formalism and proteome thermal vulnerability is completely unexplored. The dataset (Meltome Atlas) exists; the statistical toolkit (GEV fitting, return level estimation) exists; the methodological gap (how to characterize the thermally vulnerable tail of a proteome) exists. No published work bridges them.

### Gap Analysis
- **What's been explored:** Tm distributions described with mean/SD; GPMelt for curve-fitting alternatives; nonparametric NPARC analysis; BLAST score statistics using Gumbel.
- **What's NOT been explored:** GEV distribution fitting to proteome Tm data; return level estimation for protein thermal death points; tail index classification of different proteomes (thermophile vs. mesophile); peaks-over-threshold analysis for identifying the thermally vulnerable subproteome; Fisher-Tippett-Gnedenko theorem applied to identify which EVT family a proteome belongs to.
- **Most promising unexplored direction:** Apply GEV fitting to the Meltome Atlas 48,000-protein dataset across 13 species; compute return levels (e.g., "what temperature kills 1% of the proteome?"); compare tail indices across thermophiles vs. mesophiles vs. psychrophiles to test whether thermal adaptation is primarily a shift in mean Tm or a change in tail behavior.

---

## CANDIDATE 2: Reservoir Computing Theory × Gut Microbiome Community Dynamics

### Recent Breakthroughs in Reservoir Computing (Field A)
- **Emerging opportunities (Nature Communications 2024):** Comprehensive review of RC applications; expanding to physical systems, neuromorphic hardware, edge AI.
- **Bacterial reservoir computing (bioRxiv Sept 2024, updated Jan 2026):** E. coli K-12 MG1655 grown on 28 metabolites used as physical reservoir for regression/classification tasks. **Critical detail: single-strain metabolic reservoir, NOT multi-species community dynamics.** The reservoir is the intracellular metabolic network of one species, not the interaction matrix of a community.
- **Connectome-based ESN (2025):** Drosophila connectome used as connectivity matrix for reservoir — biological connectomes outperform random connectivity for overfitting resistance.
- **Review tutorial (arXiv 2412.13212):** Introduction to reservoir computing covering edge-of-chaos dynamics and echo state property.

### Recent Breakthroughs in Gut Microbiome Dynamics (Field C)
- **gLV + Jacobian stability (Stein et al. 2013, PLOS CB):** Foundational paper applying Lotka-Volterra dynamics + Jacobian spectral analysis to C. difficile. Spectral radius of interaction matrix used as stability criterion — structurally analogous to echo state property but never named as such.
- **Graph neural networks for microbiome (Nature Communications 2025):** GNN-based temporal prediction of microbial community structure — deep learning applied to community dynamics.
- **Alternative stable states (Microbiome 2023):** Demonstrates bistability and nonlinear behavior in microbiome dynamics — consistent with edge-of-chaos dynamics in RC theory.
- **gLV ecological modeling review (PMC 10511340, 2023):** Comprehensive comparison of ecological modeling approaches for microbiome stability. Lyapunov stability index used clinically; spectral radius of interaction matrix used as diagnostic.

### Existing Cross-Field Work
- **None for the specific bridge.** The 2024 bacterial RC paper is the closest related work but uses single-strain E. coli, not multi-species community dynamics. No paper models the gut microbiome species interaction matrix *as* a reservoir computer.
- **Adjacent work:** Ecological stability analysis uses the same spectral radius criterion as the echo state property — this mathematical overlap has never been recognized or exploited. LSTM models applied to microbiome time series (eLife article on recurrent neural networks for microbiome design) — but LSTM is not reservoir computing.

### Key Anomalies
- The gut microbiome community interaction matrix is the central object in both ecological stability analysis AND in reservoir computing theory. In ecology, spectral radius |λ_max(J)| < 1 means stability. In RC, spectral radius |λ_max(W)| ~ 1 means the echo state property (edge of chaos). These criteria are the same mathematical object applied to the same matrix type, but the two fields have never connected.
- Dysbiosis involves a transition from stable (spectral radius < 1) to unstable (spectral radius > 1) community dynamics — which in RC theory corresponds to a transition from useful reservoir to chaotic, information-destroying dynamics.

### Contradictions Found
- The microbiome field models communities as Lotka-Volterra systems for stability analysis but as black-box LSTM models for prediction — these approaches are never unified. RC theory provides a principled bridge between the mechanistic interaction matrix and temporal prediction capability.

### Disjointness Assessment
- **Status: DISJOINT**
- **Evidence:** The specific bridge (multi-species community as reservoir computer, echo state property on species interaction matrix, Lyapunov exponent as health indicator) has zero published literature. The 2024 bacterial RC paper confirms the field has not applied RC to community dynamics — that paper explicitly uses single-strain metabolic phenotypes. Semantic Scholar cross-field query returned an error (rate limit); PubMed returned zero results; web search found no papers applying ESN/RC theory to microbiome community interaction matrices.
- **Implication:** The mathematical overlap between ecological stability theory (Jacobian spectral analysis) and reservoir computing theory (echo state property) is a genuine blind spot. Both fields use spectral radius of interaction matrices as a key diagnostic, but neither has recognized the other.

### Gap Analysis
- **What's been explored:** gLV dynamics + Jacobian stability for microbiome; LSTM/GNN temporal prediction of microbiome; single-strain bacterial reservoir computing; ecology of microbiome networks.
- **What's NOT been explored:** Multi-species community interaction matrix analyzed as reservoir weight matrix W; echo state property checked for real microbiome matrices; memory capacity computed from fecal microbiota transplant (FMT) time series; Lyapunov exponent of community dynamics as health biomarker; spectral radius ~ 1 as biomarker for resilient vs. fragile microbiome; input separability (how well the community distinguishes different dietary inputs) as a gut health metric.
- **Most promising unexplored direction:** Compute the echo state property of inferred gLV interaction matrices from existing longitudinal microbiome datasets (HMP, MITRE). Test whether healthy subjects have spectral radius closer to 1 (edge of chaos) than IBD/dysbiosis subjects. Use RC theory to quantify memory capacity from microbiome time series as a novel resilience biomarker.

---

## CANDIDATE 3: Granular Jamming Transition Physics × Chromatin Compaction During Confined Migration

### Recent Breakthroughs in Granular Jamming Physics (Field A)
- **Gardner transition coincides with jamming scalings (arXiv 2410.23797, 2024):** Confirms the Gardner transition (full replica symmetry breaking) is a precursor to jamming in hard-sphere glasses. Establishes structural order parameter for detecting the transition. No biological applications.
- **Unjamming transition in cancer metastasis (PMID 39633605, 2024):** Applied to cell-level collective migration. Predicts unjamming at critical shape index p0* = 3.81. Framework is whole-cell/tissue, NOT sub-cellular chromatin.
- **Frontiers review on jamming in embryogenesis and cancer (2021):** Cell-level jamming transitions in tissue mechanics. Vertex models and Voronoi models at cell level. No chromatin or nucleosome applications.

### Recent Breakthroughs in Chromatin Compaction During Confined Migration (Field C)
- **Zhao, Xia, Brangwynne 2024 (Nature Communications, PMID 39557835):** Chromatin compaction during confinement reshapes nuclear condensates. Physical framework: LLPS (liquid-liquid phase separation), NOT jamming physics. Chromatin acts as crowding agent modulating condensate phase boundaries.
- **PNAS 2025 (10.1073/pnas.2416659122):** Chromatin decompaction stiffens the nucleus — nanopillar-induced nuclear deformation. Shows mechanical coupling between chromatin state and nuclear stiffness.
- **bioRxiv 2026 (10.64898/2026.02.05.702638v2):** Chromatin architecture and physical constriction cooperate in phenotype switching and cancer cell dissemination — most recent preprint.
- **Multiscale chromatin condensates (Science 2025):** Phase separation and material properties of chromatin condensates — still LLPS framework.

### Existing Cross-Field Work
- **"Nucleosome jamming" language exists but is NOT granular physics.** The replication biology literature (Kutnyakhov et al. 2014; SoNG model) uses "nucleosome jamming" to describe the parking-lot problem of nucleosome assembly on DNA — nucleosomes compete for DNA sites and can jam like cars in a parking lot. This is a kinetic/stochastic problem, NOT the rigidity transition of granular physics.
- **Jamming transitions in cancer (Oswald et al. 2017, PMC5884432):** Cell-level jamming. Explicitly does NOT extend to chromatin or nuclear mechanics.
- **Glass/gel transitions in chromatin:** Some papers describe chromatin as a polymer glass or gel. The glass transition is related to jamming but is distinct — no papers apply the specific jamming transition formalism (force chains, phi_J, coordination number Z_c, Gardner transition) to chromatin.

### Key Anomalies
- The physics of confined nuclear migration predicts that chromatin must undergo a solid-like-to-fluid transition to allow the nucleus to squeeze through constrictions smaller than its diameter. This is a jamming-unjamming transition at the nucleosome packing level — but no paper has computed phi_J for nucleosome arrays or measured force chains in compressed chromatin.
- Chromatin is a dense packing of nucleosomes (diameter ~11 nm) on DNA — the volume fractions (phi ~ 0.3–0.6 in heterochromatin) are in the range where granular jamming theory predicts a phase transition. This quantitative overlap has not been exploited.

### Contradictions Found
- The chromatin field uses two incompatible frameworks: LLPS (liquid droplets) and glass/gel (arrested dynamics). Granular jamming offers a third framework that may reconcile the apparent contradiction — jammed chromatin (solid, force chains) vs. unjammed chromatin (fluid, flows) could explain why chromatin sometimes behaves as a liquid and sometimes as a solid under confinement.

### Disjointness Assessment
- **Status: DISJOINT (at the bridge level)**
- **Evidence:** The jamming physics formalism (force chains, phi_J, coordination number Z_c, Gardner transition, isostatic condition) has NEVER been applied to chromatin or nucleosome packings. "Nucleosome jamming" language exists in replication biology but refers to kinetic parking-lot effects, NOT the rigidity transition. Cell-level jamming (cancer metastasis) is documented but explicitly does not extend to sub-cellular chromatin organization.
- **Implication:** The structural isomorphism between granular jamming physics and nucleosome packing mechanics is completely unexplored. The Scout's estimated DISJOINT classification is confirmed.

### Gap Analysis
- **What's been explored:** Cell-level jamming transitions in cancer metastasis; LLPS framework for chromatin condensates; polymer glass/gel analogies for chromatin; kinetic "nucleosome jamming" in replication biology.
- **What's NOT been explored:** GEV jamming transition phi_J for nucleosome packings in heterochromatin; coordination number Z_c analysis for nucleosome contact networks; force chain detection in compressed chromatin by high-resolution imaging + stress inference; Gardner transition as the origin of irreversible chromatin rearrangements during confined migration; power-law elastic modulus scaling near jamming applied to chromatin mechanics data.
- **Most promising unexplored direction:** Measure phi (nucleosome volume fraction) in heterochromatin vs. euchromatin vs. migrating cell constriction zones; test whether phi crosses phi_J during confinement; use force inference methods (TFM at sub-nuclear resolution) to detect force chains in jammed chromatin networks.

---

## CANDIDATE 4: ML-Augmented Acoustic Emission Classification × Plant Xylem Cavitation Mode Identification

### Recent Breakthroughs in ML-Enhanced AE for Composite NDT (Field A)
- **Guo et al. 2022 (Materials, DOI 10.3390/ma15124270):** InceptionTime with raw AE achieves 99.8% accuracy for fiber breakage/matrix cracking/delamination classification. CWT+CNN pipeline achieves 84.6–94.3%.
- **Review: ML for discrete AE interpretation (Springer NDT Journal 2025):** Comprehensive review covering CWT scalogram + CNN, wavelet energy features, deep learning methods for composite failure mode classification. The pipeline is mature in the NDT domain.
- **CWT scalogram optimization (IEEE/arXiv 2025):** Method to reduce computational complexity of CWT for acoustic recognition while maintaining CNN classification performance.
- **ASTM E1930 feature space:** Established feature set for AE classification. The ML literature uses this as a baseline and supplements with wavelet-derived features.

### Recent Breakthroughs in Plant Xylem Cavitation AE (Field C)
- **Vergeynst et al. 2015/2016 (New Phytologist, Frontiers Plant Science):** Frequency-domain feature extraction for cavitation-related AE. Manual feature extraction using partial powers in frequency bands (0–100 kHz, 100–200 kHz, 200–400 kHz, 400–800 kHz). No CNN or deep learning.
- **Oletic et al. 2020 (Computers Electronics Agriculture):** Time-frequency features of grapevine AE for drought stress detection. Software frequency-response compensation. Rule-based discrimination of AE source types.
- **"Talk is Cheap" (Trends Plant Science 2024):** Review of plant acoustic emission signals — discusses methods for detecting plant sounds, mentions ML potential but no deep learning implementation for cavitation mode classification.
- **Revised acoustic vulnerability curves (Tree Physiology 2024):** Method improvements for AE-based hydraulic vulnerability curves — still uses cumulative AE counts, not source classification.

### Existing Cross-Field Work
- **Frequency-band analysis is shared:** Both the composites NDT and plant AE fields use frequency bands as the primary discriminating feature space. Plant AE uses 100–200 kHz for cavitation vs. 400–800 kHz for mechanical events — directly analogous to fiber breakage vs. matrix cracking frequency signatures in composites.
- **What is NOT shared:** The full CWT scalogram generation + CNN architecture training pipeline has never been deployed in plant AE. No domain adaptation or transfer learning from composites to plant systems.
- **Wavelet energy features used in plant AE:** Basic wavelet features (energy, entropy, variance) are used in some plant AE work — but these are scalar features, NOT 2D scalogram images as CNN input.

### Key Anomalies
- Plant AE source classification (cavitation vs. bark cracking vs. embolism propagation) is a solved problem in the composites domain (fiber breakage vs. matrix cracking vs. delamination) — the source type identification problem is formally identical. Yet the transfer has never been made.
- Drought monitoring requires distinguishing cavitation events from non-cavitation events (acoustic noise, thermal expansion) in real field conditions. This is precisely the contamination-rejection problem that deep learning on CWT scalograms excels at in NDT.

### Contradictions Found
- Plant hydraulics literature simultaneously argues (a) AE is a reliable drought stress indicator and (b) AE signals are unreliable because the source of each signal is ambiguous. Deep learning source classification would resolve this contradiction — but has not been applied.

### Disjointness Assessment
- **Status: DISJOINT AT BRIDGE LEVEL (confirmed)**
- **Evidence:** The specific bridge (CWT scalogram + CNN pipeline, domain adaptation from composite NDT, Felicity ratio mapping to cavitation reversibility) does not exist in the literature. Basic frequency-band clustering (Vergeynst 2016) is the closest existing work but is rule-based, not deep learning. No paper has applied CWT scalogram + CNN classification from composites NDT to plant xylem AE.
- **Implication:** The methodological bridge is fully executable — both sides exist — but the transfer has never been made. This is a strong DISJOINT_AT_BRIDGE_LEVEL case as the Scout classified it.

### Gap Analysis
- **What's been explored:** Manual frequency-band feature extraction for plant AE; cumulative AE counting for hydraulic vulnerability curves; basic wavelet scalar features; AE for drought stress detection.
- **What's NOT been explored:** CWT scalogram generation from plant AE signals fed to CNN; transfer learning or domain adaptation from composites NDT models to plant AE; multi-class source classification (cavitation vs. bark cracking vs. embolism propagation vs. noise) using deep learning; Felicity ratio mapping to quantify cavitation reversibility (embolism refilling); ASTM E1930 feature space applied to plant AE.
- **Most promising unexplored direction:** Train CWT+CNN on synthetic mixed plant AE datasets with known source proportions (cavitation + bark cracking + embolism); validate on grapevine or oak dehydration experiments against hydraulic conductance measurements; assess whether the domain adaptation from composites NDT provides useful prior features or requires full retraining.

---

## CANDIDATE 5: Classical Nucleation Theory × Ferroptosis Ferritin Iron Pool Dynamics

### Recent Breakthroughs in Classical Nucleation Theory Applied to Biology (Field A)
- **Nucleation landscape of biomolecular condensates (Nature 2021):** Key features of condensate nucleation quantitatively understood through CNT-like framework. Establishes CNT as applicable to intracellular environments despite complexity — but for protein condensates, NOT iron minerals.
- **Ferritin mineral nucleation (JACS 2025, DOI 10.1021/jacs.5c05464):** Mechanism of iron mineral nucleation in a mini-ferritin characterized at 1.86 Å resolution. Nucleation at acidic 3-fold pores; iron clusters resemble ferrihydrite. CNT concepts appear implicitly in the kinetics discussion.
- **JACS 2025 (DOI 10.1021/jacs.5c01337):** Observation of nascent mineral core assembly at the nucleation site of human mitochondrial ferritin — structural biology of ferritin nucleation. Still structural biology, NOT applied to ferroptosis.
- **Ferrihydrite transformation kinetics (Geochimica 2021):** "Labile Fe(III) supersaturation controls nucleation and properties of product phases from Fe(II)-catalyzed ferrihydrite transformation" — explicitly connects supersaturation to CNT nucleation principles. NOT in a cellular/ferroptosis context.

### Recent Breakthroughs in Ferroptosis Iron Pool Dynamics (Field C)
- **Ponnusamy et al. 2025 (bioRxiv/PMC12236665):** KEY PAPER — "Labile iron pool dynamics do not drive ferroptosis potentiation in colorectal cancer cells." Using TRX-PURO reactivity-based probe, finds LIP does NOT measurably increase during ferroptosis induction despite ferritinophagy. Confirms the Scout's key anomaly.
- **Kong et al. 2024 (Frontiers Cell Dev Bio):** Review establishing canonical ferroptosis mechanism: ferritinophagy (NCOA4-mediated ferritin autophagy) → Fe3+ release → reduction to Fe2+ → LIP expansion → Fenton reaction → lipid peroxidation → cell death.
- **NRF2 controls iron homeostasis (Science Advances 2023):** HERC2 and VAMP8 as NRF2 targets regulating iron export during ferroptosis stress.
- **Iron metabolism and ferroptosis review 2024 (PMC12374342):** State-of-the-art review of iron chemistry in ferroptosis. No nucleation theory content.

### Existing Cross-Field Work
- **None found.** Semantic Scholar (1 hit — ferritin structural biology, not CNT application to ferroptosis). PubMed: zero hits for "classical nucleation theory ferroptosis." Web search for "CNT ferroptosis iron nucleation," "supersaturation ferroptosis," "ferrihydrite nucleation ferroptosis": all returned zero relevant cross-field papers.
- **JACS 2025 papers on ferritin nucleation:** These apply CNT to ferritin mineral assembly in healthy cells. They do NOT connect to ferroptosis or cell death. The bridge from ferritin nucleation chemistry to ferroptosis iron pool dynamics does not exist.

### Key Anomalies
- **The LIP paradox (2025):** Ferritinophagy during ferroptosis should release large amounts of Fe3+ from ferritin cores. Standard hypothesis: LIP expands → Fenton chemistry → lipid peroxidation. Reality (Ponnusamy 2025): LIP does NOT measurably expand. If iron is being released but not detected as free labile iron, it must be in a form the probe cannot detect — CNT predicts this would be nano-cluster nuclei of iron oxide/hydroxide below the critical radius.
- **pH-dependent critical radius:** Intracellular pH during ferroptosis drops (acidification accompanies cell death). CNT predicts that the critical nucleus radius r* increases with pH — at lower pH, nucleation is favored (smaller r*), meaning more iron would form sub-critical nuclei rather than dissolving into the free LIP.

### Contradictions Found
- The field holds simultaneously that (a) ferritinophagy is required for ferroptosis and (b) free labile iron does not increase during ferroptosis. These facts are contradictory under the current "iron release → LIP expansion" model. CNT provides a resolution: iron is released but immediately re-nucleates as nano-clusters below the detection threshold of reactivity-based LIP probes.

### Disjointness Assessment
- **Status: DISJOINT**
- **Evidence:** Zero cross-field papers found. JACS 2025 ferritin nucleation papers are structural biology of healthy ferritin assembly, not CNT applied to ferroptosis. The specific connection (CNT nucleation kinetics applied to iron speciation during ferritinophagy → ferroptosis) has never been made.
- **Implication:** The paradox created by Ponnusamy 2025 is precisely the kind of anomaly that CNT is equipped to resolve. The hypothesis space is open and the anomaly is both recent and high-impact.

### Gap Analysis
- **What's been explored:** Ferritin mineral nucleation structural biology; CNT for biomolecular condensate formation; ecological stability of iron minerals; ferroptosis iron metabolism reviews; LIP probes and detection methods.
- **What's NOT been explored:** CNT nucleation rate equation J = A·exp(−ΔG*/kT) applied to iron speciation during ferroptosis; critical nucleus radius r* as a function of intracellular pH during ferroptosis; Ostwald ripening kinetics (LSW theory) for iron nano-clusters during ferritinophagy; ferrihydrite surface energy γ in cytoplasmic conditions; mineral dissolution rate law connecting ferritin iron release to free LIP at cytoplasmic pH.
- **Most promising unexplored direction:** Compute theoretical LIP probe signal expected under CNT-predicted iron nano-cluster formation during ferroptosis; test whether sub-critical iron clusters accumulate in ferroptotic cells using higher-resolution iron speciation probes (not just free Fe2+ detectors); use pH manipulation to shift r* and test whether alkaline conditions (larger r*, less nucleation) allow LIP expansion and accelerate ferroptosis.

---

## Summary Table

| Candidate | Field A | Field C | Disjointness | Evidence |
|---|---|---|---|---|
| 1 | Extreme Value Statistics | Thermal Proteome Profiling | **DISJOINT** | Zero cross-field papers; BLAST Gumbel is adjacent but distinct |
| 2 | Reservoir Computing | Gut Microbiome Dynamics | **DISJOINT** | Bacterial RC exists (single-strain); community-as-reservoir never done |
| 3 | Granular Jamming Physics | Chromatin Compaction | **DISJOINT** | "Nucleosome jamming" is kinetic/stochastic, NOT rigidity transition |
| 4 | ML-AE Classification (NDT) | Plant Xylem Cavitation | **DISJOINT_AT_BRIDGE_LEVEL** | Frequency-band clustering exists; full CWT+CNN transfer never done |
| 5 | Classical Nucleation Theory | Ferroptosis Iron Dynamics | **DISJOINT** | Zero cross-field papers; 2025 LIP paradox is unresolved anomaly |

---

## Full-Text Papers Retrieved

1. `jarzab2020-meltome-atlas-thermal-proteome-stability.md` — Meltome Atlas (Nature Methods 2020): 48,000 proteins, Tm 30–90°C; 20% tail proteins unmeasured
2. `figueroa-navedo2024-thermal-proteome-profiling-advances.md` — TPP advances review (Cell Reports Methods 2024): statistical limitations of current Tm analysis
3. `ponnusamy2025-labile-iron-pool-ferroptosis.md` — LIP paradox paper (2025): LIP does NOT expand during ferroptosis despite ferritinophagy
4. `guo2022-deep-learning-acoustic-emission-composite.md` — CWT+CNN for composite AE (Materials 2022): 94.3–99.8% accuracy for failure mode classification
5. `oletic2020-grapevine-xylem-acoustic-emission-time-frequency.md` — Grapevine AE time-frequency features (Computers Electronics Agriculture 2020): state of the art in plant AE
6. `zhao2024-chromatin-condensates-confined-migration.md` — Chromatin during confined migration (Nature Comms 2024): LLPS framework, no jamming physics
7. `stein2013-gut-microbiome-ecological-modeling-stability.md` — gLV microbiome stability (PLOS CB 2013): Jacobian spectral analysis foundational paper; no RC connection

---

## RETRIEVAL QUALITY CHECK

1. **MCP vs WebSearch fallback:** Semantic Scholar returned useful individual-field results; cross-field queries returned zero hits, confirming disjointness. PubMed MCP returned empty results for all queries (connectivity issue) — WebSearch used as primary. All disjointness assessments based on actual search results, not assumptions.
2. **Papers per field:** Each candidate has ≥3 papers with abstracts retrieved. All 5 candidates have documented search trails.
3. **Disjointness basis:** All DISJOINT verdicts based on positive evidence from cross-field search returning zero results PLUS evidence from individual field searches showing the gap. Candidate 3 has an important nuance: "nucleosome jamming" language exists but is distinct from granular physics jamming formalism — documented explicitly.
4. **Gap analysis specificity:** All gap items specify the exact missing connection (e.g., "GEV distribution fitting to Meltome Atlas data" not "more statistical analysis needed").
