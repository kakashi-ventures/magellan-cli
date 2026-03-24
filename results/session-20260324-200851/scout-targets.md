# Scout Targets — Session session-20260324-200851
## Mode: SCOUT (autonomous)
## Creativity Constraint: Tool/technique transfer across disciplines (session 13 mod 5 = 3)
## Date: 2026-03-24

---

## Strategy Diversification Check
- Last 2 sessions: contradiction_mining (S012), structural_isomorphism (S011)
- Strategies with < 2 primary data points (exploration slot candidates): evolutionary_conservation_gap (0), dimensional_mismatch (0), Swanson_ABC_bridging (1)
- This session uses: tool_repurposing (primary), network_gap_analysis, Swanson_ABC_bridging, evolutionary_conservation_gap, scale_bridging

---

## Target 1: Cryo-EM single-particle analysis techniques x Bacterial outer membrane vesicle (OMV) cargo sorting
**Strategy**: tool_repurposing
**Field A**: Cryo-EM structural biology — single-particle analysis (SPA), 3D classification, heterogeneity analysis (3DVA, cryoDRGN, RELION 5 continuous flexibility). Mature technique (>30 years, Nobel 2017) with recent revolution in heterogeneity analysis (2020-2025).
**Field C**: Bacterial OMV biogenesis and cargo sorting — selective enrichment of virulence factors, sRNA, immunomodulatory lipids in OMVs. Mechanism of selective cargo loading is the #1 unsolved question in the field. Current methods: proteomics, lipidomics, fluorescence. NO structural data on cargo-loading intermediates.
**Bridge concepts**:
- Cryo-EM 3D classification of OMV populations by size/density/cargo content (never attempted)
- CryoDRGN continuous heterogeneity analysis of outer membrane protein (OMP) conformational states during OMV budding
- Subtomogram averaging of OMV budding intermediates at bacterial poles
- In situ cryo-ET of OMV biogenesis sites (VipA/VipB, OmpA depletion zones)
- 3DVA of OMP barrel flexibility linked to cargo capture
**Scout confidence**: 8.5/10
**Rationale**: Cryo-EM heterogeneity analysis has transformed eukaryotic vesicle biology (ESCRT, COPI/COPII) but has NEVER been applied to bacterial OMV biogenesis. The cargo sorting problem is explicitly identified as the field's top priority (Schwechheimer & Kuehn 2015, Toyofuku et al. 2019). OMV diameter (20-250 nm) is within cryo-EM resolution range. The bridge is a genuine tool transfer with immediate experimental actionability.

---

## Target 2: Patch-clamp electrophysiology techniques x Plant cell mechanosensation (turgor sensing)
**Strategy**: tool_repurposing
**Field A**: Patch-clamp electrophysiology — voltage clamp, current clamp, single-channel recording, automated patch clamp (planar chip arrays), inside-out/outside-out configurations. Gold standard for ion channel characterization in animal cells (established 1976, Nobel 1991).
**Field C**: Plant turgor pressure sensing and osmoregulation — guard cell stomatal control, root hydrotropic response, osmosensor candidates (OSCA1, MSL channels, CNGC channels). Turgor sensing is the "dark matter" of plant physiology — known to exist for >100 years but molecular mechanism unknown.
**Bridge concepts**:
- Patch-clamp of plant protoplasts with pressure clamp (never combined with single-channel recording at turgor-relevant pressures 0.1-1 MPa)
- Automated planar patch clamp adapted for plant protoplasts (cell wall removal standardization)
- Pressure-clamp ramp protocols to measure activation thresholds of candidate turgor sensors (OSCA1, MSL8/10)
- Inside-out patches to test direct membrane tension activation of plant mechanosensors
- Single-channel conductance fingerprinting of unidentified turgor-activated channels
**Scout confidence**: 7.5/10
**Rationale**: Despite massive progress in plant mechanosensor gene discovery (OSCA1 2014, MSL family 2010s), the biophysical characterization of these channels at turgor-relevant pressures is almost entirely absent. Animal electrophysiology tools (pressure-clamp, automated planar arrays) could transform plant mechanosensing within 2-3 years. The barrier is technical (plant cell walls, large vacuoles), not conceptual.

---

## Target 3: Fluorescence lifetime imaging (FLIM) and Forster resonance energy transfer (FRET) biosensors x Bacterial persister cell metabolism
**Strategy**: network_gap_analysis
**Field A**: FLIM-FRET biosensors — genetically encoded biosensors for metabolite concentrations (ATP, NADH, pH, Ca2+, cAMP), fluorescence lifetime imaging for quantitative, ratiometric measurement independent of expression level. Widely used in mammalian cell biology (>5000 papers). Recent advances: FLIM-FRET for NAD+/NADH ratio (SoNar, 2020), ATP (QUEEN, 2019).
**Field C**: Bacterial persistence — stochastic, non-genetic antibiotic tolerance. The metabolic state of persister cells is the central debate: are they dormant, metabolically active, or in a specific low-energy state? Population-level metabolomics cannot resolve this because persisters are <0.01% of the population. Single-cell resolution is essential but unavailable for metabolite quantification.
**Bridge concepts**:
- FLIM-FRET ATP biosensor (QUEEN) expressed in E. coli/P. aeruginosa to quantify ATP in individual persister cells
- NAD+/NADH FLIM biosensor (SoNar) to test the "metabolic dormancy" model of persistence at single-cell resolution
- FLIM pH biosensor (pHluorin variant) to measure persister proton motive force
- Time-resolved FLIM to distinguish persisters from dead cells (lifetime vs intensity)
- Microfluidic FLIM for longitudinal tracking of individual cells through persistence-resuscitation cycle
**Scout confidence**: 8.0/10
**Rationale**: The persister metabolism debate cannot be resolved without single-cell metabolite measurements. Genetically encoded FLIM-FRET biosensors provide exactly this capability but have NEVER been deployed for persister phenotyping. PubMed search "FLIM persister" = 0 results. "FRET biosensor persister" = 0 results. The tools exist in mammalian biology; the need exists in microbiology; the gap is a pure transfer problem.

---

## Target 4: Optogenetic actuators x Biofilm dispersal signaling (c-di-GMP regulation)
**Strategy**: Swanson_ABC_bridging
**Field A**: Optogenetics — light-activated protein tools (channelrhodopsins, LOV domains, phytochrome-based switches, CRY2/CIB1 dimerizers). Primarily developed and used in neuroscience (established 2005, massive expansion 2010-2025). Recent: light-activated phosphodiesterases (LAPD, 2016), light-activated adenylate cyclases (bPAC, PAC).
**Field C**: Biofilm dispersal — c-di-GMP as master biofilm regulator (high = sessile biofilm, low = planktonic dispersal). Dispersal is the critical therapeutic target for chronic biofilm infections. Current tools: chemical dispersers (NO donors, D-amino acids) with poor spatiotemporal control. NO way to trigger dispersal in specific biofilm regions.
**B-term bridge**: Light-activated phosphodiesterases (LAPD) from Idiomarina and BphS/BphG from Rhodobacter — these are bacterial phytochrome-based enzymes that ALREADY degrade c-di-GMP upon red/near-infrared light activation. Existed since 2016 but used only in synthetic biology circuits, NEVER deployed as biofilm dispersal tools.
**Bridge concepts**:
- LAPD expression in P. aeruginosa biofilm for spatially targeted c-di-GMP degradation and regional dispersal
- BphS/BphG dual system for reversible biofilm-to-planktonic switching with red/NIR light
- Optogenetic c-di-GMP pulse protocols to determine minimum dispersal signal duration and amplitude
- Two-photon optogenetic activation for depth-resolved biofilm dispersal (target deep biofilm layers)
- Combinatorial optogenetic dispersal + antibiotic timing for enhanced biofilm eradication
**Scout confidence**: 7.0/10
**Rationale**: LAPD and BphS/BphG already exist as tools that degrade the exact molecule (c-di-GMP) that controls biofilm dispersal. The Swanson B-term is perfectly positioned: optogenetics literature describes these tools, biofilm literature describes c-di-GMP as the master regulator, but NO paper connects optogenetic c-di-GMP control to therapeutic biofilm dispersal. The near-infrared wavelengths (700-780 nm) penetrate tissue to ~2-3 cm, making clinical biofilm targeting feasible.

---

## Target 5: Atomic force microscopy (AFM) force spectroscopy x Intrinsically disordered protein (IDP) phase separation
**Strategy**: scale_bridging
**Field A**: AFM single-molecule force spectroscopy (SMFS) — pulling individual protein molecules to measure unfolding forces, binding energies, conformational landscape (established 1994). Recent: high-speed AFM (2010s), multiparametric AFM (2015+), correlative AFM-fluorescence (2020+). Quantitative measurement of intramolecular and intermolecular forces at piconewton resolution.
**Field C**: Biomolecular condensate physics — intrinsically disordered proteins (FUS, TDP-43, hnRNPA1, DDX4) undergo liquid-liquid phase separation (LLPS). The molecular grammar of LLPS (which residues drive condensation, what are the interaction energies) is understood only from mutagenesis and theory. Direct force measurements on individual IDP chains within condensates have NEVER been performed.
**Bridge concepts**:
- AFM-SMFS pulling of individual IDP chains (FUS LCD) out of condensate droplets to measure extraction force (partitioning energy)
- Force-distance curves to quantify condensate cohesive energy per residue
- Temperature-dependent SMFS to extract enthalpic vs entropic contributions to condensation
- AFM nanoindentation of condensate droplets to correlate single-chain forces with bulk material properties
- Multiparametric AFM mapping of condensate surface properties (adhesion, stiffness, deformation) during aging/maturation
**Scout confidence**: 7.5/10
**Rationale**: The condensate field has exploded since 2017 but relies almost entirely on bulk measurements (turbidity, FRAP, DIC microscopy) and computational models (coarse-grained MD). Direct measurement of the intermolecular forces holding condensates together at single-molecule resolution has never been attempted. AFM-SMFS provides exactly this capability — piconewton force resolution, aqueous environment compatible, no labeling required. The bridge is scale_bridging: connecting molecular-level forces to mesoscale condensate properties.

---

## Target 6: Electrochemical impedance spectroscopy (EIS) x Gut microbiome metabolic state monitoring
**Strategy**: evolutionary_conservation_gap (exploration slot)
**Field A**: Electrochemical impedance spectroscopy (EIS) — frequency-swept AC measurement of impedance magnitude and phase across biological samples. Widely used in materials science, corrosion monitoring, battery diagnostics. In biology: EIS for cell culture monitoring (ECIS, Applied BioPhysics), wound healing assays, epithelial barrier integrity (TEER measurements). Established >40 years in materials, ~25 years in mammalian cell biology.
**Field C**: Gut microbiome functional monitoring — current methods for microbiome assessment are 16S rRNA (composition only), shotgun metagenomics (gene catalog), metabolomics (expensive, slow). The field needs REAL-TIME functional readouts of microbiome metabolic activity, not static compositional snapshots. Electrochemical activity of gut microbiota (short-chain fatty acids, H2S, redox mediators, extracellular electron transfer) is well-characterized but not exploited for monitoring.
**Bridge concepts**:
- EIS frequency sweep of fecal/intestinal samples to fingerprint microbiome metabolic state (redox activity, SCFA production, gas generation)
- Impedance-based discrimination of dysbiosis from eubiosis using equivalent circuit models (R_solution, C_biofilm, R_charge_transfer, W_diffusion)
- Miniaturized EIS sensors for ingestible capsule-based gut microbiome monitoring
- EIS tracking of antibiotic-induced microbiome disruption in real time
- Correlation of EIS spectral features with specific metabolic functions (butyrate production, sulfate reduction, methanogenesis)
**Scout confidence**: 7.0/10
**Rationale**: EIS is a mature, cheap, real-time technique that measures exactly the electrochemical properties that distinguish metabolically active from inactive microbial communities. The gut microbiome field is desperately seeking real-time functional readouts beyond composition. PubMed search "impedance spectroscopy gut microbiome" returns very few results, mostly tangential. The ingestible capsule form factor is technically mature (FDA-cleared for pH, temperature). This is an evolutionary_conservation_gap variant: the same electrochemical principles that characterize biofilms on metal surfaces (corrosion) can characterize microbial communities in the gut.

---

## TARGET QUALITY CHECK (Scout Self-Reflection)

### Disjointness Assessment (pre-Literature-Scout estimate)
1. Cryo-EM x OMV cargo sorting: Likely DISJOINT — cryo-EM structural biology and OMV biogenesis communities don't overlap. Some cryo-ET of bacteria exists but NOT focused on cargo sorting mechanism.
2. Patch-clamp x Plant turgor sensing: Likely DISJOINT — electrophysiology community is almost entirely animal-focused. Plant protoplast patch-clamp exists but is a tiny niche (<50 labs).
3. FLIM-FRET x Bacterial persisters: Likely DISJOINT — biosensor development community is mammalian cell biology; persister community is microbiology/AMR.
4. Optogenetics x Biofilm dispersal: Likely PARTIALLY_EXPLORED — optogenetic c-di-GMP tools exist in synthetic biology. The therapeutic application to natural biofilm dispersal may have been proposed.
5. AFM-SMFS x IDP condensates: Likely PARTIALLY_EXPLORED — AFM nanoindentation of condensates has been done (2020+). Single-molecule pulling from condensates may exist.
6. EIS x Gut microbiome: Likely DISJOINT — impedance spectroscopy community (materials/corrosion) and gut microbiome community are completely separate.

### Strategy Diversity Check
- tool_repurposing: Targets 1, 2 (2 candidates)
- network_gap_analysis: Target 3
- Swanson_ABC_bridging: Target 4 (exploration slot for strategy)
- scale_bridging: Target 5
- evolutionary_conservation_gap: Target 6 (exploration slot)
- 5 different strategies across 6 candidates: PASS
- At least 2 strategies with < 2 primary sessions: evolutionary_conservation_gap (0), Swanson_ABC_bridging (1): PASS

### Creativity Constraint Check (tool/technique transfer)
All 6 candidates involve transferring an established technique from one domain to another. PASS.

### Potential Weaknesses
- Target 4 (optogenetics x biofilm): Risk of being PARTIALLY_EXPLORED due to existing synthetic biology work with optogenetic c-di-GMP tools
- Target 5 (AFM x condensates): AFM nanoindentation of condensates may already exist — needs literature verification
- Target 2 (patch-clamp x plants): Technical barriers may be severe enough that the transfer is not feasible, not just unattempted
