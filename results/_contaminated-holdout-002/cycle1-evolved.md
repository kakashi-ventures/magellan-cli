# Cycle 1 Evolved Hypotheses — Session 2026-03-25-targeted-002
## Mechanobiology (ECM Mechanics) × Epigenomics (Enhancer Regulation)

**Evolver**: evolver-v5.2 | **Date**: 2026-03-25 | **Cycle**: 1
**Operations applied**: Specification (H3), Mutation (H4), Mechanism Fix (H2), Crossover (H1), Mutation+Specification (H5)

---

## EVOLUTION QUALITY CHECK (pre-output)

1. Is each evolved hypothesis genuinely stronger than its parent, or just rephrased?
   - EH3: Stronger — IDR multivalency grounds the Hill coefficient; plateau issue addressed; citation corrected; dSTORM threshold prediction is new and specific.
   - EH4: Stronger — vague "enhancer preference" replaced by G-actin threshold mechanism with RPEL Kd values; two new specific mutants (ΔRPEL, LXXLL) added.
   - EH2: Stronger — fatal mechanism error (CaMKII≠EP300 kinase) corrected; HDAC4/5 route is experimentally documented; quantitative Phase 1/2 split grounded in Backs 2006 kinetics.
   - EH1: Stronger — viscoelasticity crossover adds an entirely new controlling variable (τ₁/₂); promoter bias wound converted to temporal sequence prediction.
   - EH5: Stronger — condensate coalescence dynamics replace insufficient single-condensate surface tension model; verteporfin replaced by specific IDR-deleted YAP mutant (CQ4); transcription factory ruled out via flavopiridol.

2. Do any two share the same bridge mechanism?
   - EH3: BRD4 IDR multivalent LLPS cooperativity → stiffness threshold switch
   - EH4: G-actin threshold → RPEL conformational unmasking → SRF-independent EP300 recruitment
   - EH2: Piezo1→Ca²⁺→CaMKII→HDAC4/5 nuclear export → EP300 derepression
   - EH1: ECM stress relaxation rate → KDM6B nuclear retention duration → promoter→enhancer H3K27me3 demethylation cascade
   - EH5: YAP condensate coalescence events → multi-step mechanoenhancer spatial co-localization
   - No two hypotheses share a bridge mechanism. EH3 and EH5 both involve YAP condensates but address different questions (transcriptional cooperativity vs 3D genome co-localization). DIVERSITY CONSTRAINT: SATISFIED.

3. Did any crossover produce incoherence?
   - EH1 crossover (KDM6B × viscoelasticity): coherent. Stress relaxation rate controls duration of FAK-Src-PKA signaling, which controls KDM6B nuclear retention, which controls whether KDM6B reaches mechanoenhancers. No logical gaps.

---

## EH3: BRD4 IDR Multivalency (n≈4) Creates a 5–15 kPa Mechanical Threshold Switch via Cooperative Condensate Assembly at Mechanoenhancers

**Evolved from Hypothesis #H3 via Specification**
**Parent score**: 7.85 | **Expected score direction**: ↑ (Mechanistic Specificity, Groundedness)

### Core Claim

YAP-BRD4 condensate assembly at mechanoenhancers is cooperative with Hill coefficient n≈3–4, grounded in BRD4's IDR multivalency: BRD4's C-terminal IDR contains 6 low-complexity FG/FxxLF repeat modules (each with Kd ~10–20 nM for MED1-IDR), and YAP's WW domain contributes 2 binding sites, yielding total multivalent valency ≈8. From the Banani et al. 2016 LLPS multivalency model, n ≈ valency/2 ≈ 4 is predicted.

This cooperativity creates a mechanical threshold switch, but — addressing the parent's critical wound — the switch is restricted to the 5–15 kPa stiffness window where nuclear YAP concentration is still rising. Above ~20 kPa, YAP nuclear concentration saturates (PNAS 2021 spatial model; YAP dimensionality-sensitive above ~5.7 kPa) and condensate output also plateaus. The hypothesis is therefore specifically about the fibrosis-onset range (5–15 kPa: healthy → pre-fibrotic transition), not the full 1–50 kPa range as claimed by H3.

### Mechanism

ECM stiffness → YAP nuclear concentration [Y_nuc]:
- 1 kPa → ~10 nM nuclear YAP
- 5 kPa → ~25 nM
- 10–15 kPa → ~40–50 nM (estimated from Dupont 2011 data scaled to fibroblasts)
- >20 kPa → plateau at ~50–60 nM (PNAS 2021 model)

BRD4-YAP condensate assembly: [V_cond] ∝ [Y_nuc]^n, where n≈4 (IDR multivalency prediction).

Below the critical YAP concentration (~35–45 nM, corresponding to ~8–12 kPa):
BRD4-YAP clusters exist but are below the critical condensate threshold → weak, diffuse BRD4 at mechanoenhancers → graded, low-amplitude transcription.

Above the threshold (~10–15 kPa):
Cooperative condensate nucleation causes a step-change in BRD4 occupancy at mechanoenhancers → super-enhancer-like transcriptional output → fibrotic gene program engagement.

Above ~20 kPa: both YAP and condensate signals plateau → stiffness-insensitive region.

The mechanistically important range — the switch — is 5–15 kPa, which corresponds to the ECM stiffness of early fibrosis (healthy lung ~0.5–2 kPa; early fibrosis ~5–15 kPa; established fibrosis >20 kPa). This positions the switch precisely at the clinically relevant transition.

### Falsifiable Predictions

1. **dSTORM condensate threshold**: BRD4 condensate volume at the CYR61 mechanoenhancer locus (dSTORM combined with CYR61-Oligopaint FISH, primary human lung fibroblasts) shows >3-fold increase from 5→10 kPa but <1.5-fold increase from 10→50 kPa. The inflection is at 8–12 kPa — not across the full stiffness range. This distinguishes a switch from a graded response.

2. **smFISH power law fit (range-resolved)**: smFISH for CTGF and CYR61 across 6-point stiffness gradient (1, 3, 5, 10, 15, 30, 50 kPa). Fitting: in the 1–15 kPa range, transcription output ∝ stiffness^n with n=3.0±0.5 (F-test, power law significantly better than linear, p<0.05). In the 15–50 kPa range, n≈1.0 (linear/plateau). A significant model break at ~12 kPa confirms the switch.

3. **BRD4-IDR deletion mutant**: Stable expression of BRD4-ΔCTD (IDR deleted, residues 1058–1362 removed, brodomain retained for chromatin binding), replacing endogenous BRD4 at ~endogenous levels via CRISPR knock-in. Prediction: stiffness-transcription relationship becomes linear (n≈1) across the full 1–50 kPa range — the switch is abolished. This directly tests IDR multivalency as the cooperativity source.

4. **JQ1 comparison**: JQ1 (250 nM, disrupts bromodomain-H3K27ac interaction) reduces overall BRD4 chromatin occupancy but does NOT eliminate IDR-mediated cooperativity — JQ1 shifts the threshold concentration but does not linearize the response (unlike BRD4-ΔCTD). This distinguishes bromodomain-dependent anchoring from IDR-driven cooperativity.

### Literature Grounding

- [GROUNDED] BRD4 IDR contains multiple FG-repeat low-complexity modules mediating condensate assembly: Sabari et al. 2018 Science (BRD4-MED1 condensates at super-enhancers)
- [GROUNDED] LLPS multivalency theory predicts Hill n ≈ valency/2: Banani et al. 2016 Science (multivalent IDR interactions drive cooperative LLPS)
- [GROUNDED] YAP-BRD4 co-occupancy at super-enhancers: Zanconato et al. 2018 Nat Medicine (NOTE: YAP LLPS condensate evidence is Cai et al. 2019 Nat Cell Biol — citations corrected from parent)
- [GROUNDED] YAP nuclear concentration is stiffness-dependent with saturation above ~20 kPa: PNAS 2021 spatial model (YAP becomes dimensionality-sensitive, not stiffness-linear, above ~5.7 kPa); Dupont et al. 2011 Nature for YAP-stiffness coupling
- [GROUNDED] Phase-separated condensates are cooperative (concentration threshold): Shin et al. 2018 Cell (CasDrop LLPS cooperativity measurements)
- [INFERRED] BRD4 IDR valency = 6 modules → Hill n≈4: extrapolated from multivalency theory; direct n measurement for BRD4-YAP system at mechanoenhancer loci not yet done
- [INFERRED] Critical YAP concentration ~35–45 nM corresponds to 8–12 kPa: estimated from YAP-stiffness curves; requires quantitative IF to verify

### Counter-Evidence and Limitations

- The BRD4 LLPS vs chromatin-tethered cluster debate remains active (2025); if BRD4 bodies are clusters not true condensates, n≈4 cooperativity argument loses its theoretical grounding
- YAP plateau above 20 kPa limits clinical relevance for established fibrosis (20–50 kPa) — the switch may be less important for advanced fibrotic disease than for disease initiation
- BRD4-ΔCTD replacement will likely have pleiotropic effects on transcriptional regulation beyond mechanoenhancers; careful RNA-seq needed to attribute phenotype

### Test Protocol

1. Primary human lung fibroblasts (non-IPF) on 6-point polyacrylamide stiffness gradient (1, 3, 5, 10, 15, 30, 50 kPa), fibronectin-coated, 24h culture
2. smFISH: CTGF (20-probe set), CYR61 (20-probe set) — count mRNA per cell per condition, n≥100 cells/condition
3. Immunofluorescence: nuclear YAP total intensity (E1E3I antibody, Cell Signaling) at same timepoint — quantify nuclear concentration proxy
4. dSTORM: BRD4 antibody (Bethyl A301-985A100) + CYR61-Oligopaint FISH for locus co-labeling; measure condensate volume at CYR61 locus in ≥30 cells per stiffness condition
5. BRD4-ΔCTD CRISPR knock-in (or doxycycline-inducible overexpression at endogenous level) → repeat steps 2–4
6. JQ1 (250 nM, 4h pre-treatment) → repeat step 2

### Confidence: 0.63
### Disciplinary Distance: 3 fields (mechanobiology ↔ condensate biophysics ↔ enhancer epigenomics)

---

## EH4: G-Actin Threshold–Driven RPEL Conformational Unmasking Enables MRTF-A to Recruit EP300 at CaRG-Box Mechanoenhancers Independent of SRF

**Evolved from Hypothesis #H4 via Mutation**
**Parent score**: 7.55 | **Expected score direction**: ↑ (Mechanistic Specificity, Testability)

### Core Claim

The "promoter-dominant binding" weakness of H4 is addressed by providing a MOLECULAR MECHANISM for the stiffness-dependent redistribution of MRTF-A from promoters to mechanoenhancers. The mechanism is not genomic — it is conformational: G-actin depletion below ~5 μM (which occurs on stiff ECM due to F-actin polymerization) drives MRTF-A RPEL domain opening, exposing a cryptic LXXLL nuclear receptor interaction motif that enables SRF-independent, direct EP300 recruitment at CaRG-box mechanoenhancers.

On soft ECM (G-actin ~10–15 μM), RPEL domains are ~80–90% occupied → MRTF-A adopts closed conformation → pairs with SRF at CaRG-box promoters (default, canonical). On stiff ECM (G-actin ~2–4 μM), RPEL occupancy drops to ~20–30% → RPEL adopts open conformation → cryptic LXXLL motif (Leu184-Met185-Val186-Leu187-Leu188, predicted from homology with p160 coactivator LxxLL helices that bind nuclear receptor AF-2 grooves) is exposed → MRTF-A engages EP300 nuclear receptor interaction domain → EP300 recruited to CaRG-box mechanoenhancers, independent of SRF.

### Mechanism

**Quantitative foundation:**
- MRTF-A RPEL modules: 3 modules, Kd ~1 μM each for G-actin monomers; cooperative binding with apparent Kd_eff ~0.5 μM (cooperative closing of all 3 modules)
- G-actin concentration estimates: ~12 μM on soft ECM (1 kPa, low F-actin polymerization) → ~3 μM on stiff ECM (50 kPa, high F-actin, depletes G-actin pool)
- RPEL occupancy calculation: at 12 μM G-actin → RPEL ~96% occupied (closed); at 3 μM G-actin → RPEL ~35% occupied (partially open)
- The conformational switch fires as G-actin drops below ~5 μM (RPEL occupancy <50%), corresponding to ECM stiffness ~20–30 kPa

**Genomic redistribution:**
Open RPEL → exposed LXXLL helix → direct MRTF-A to EP300 NR-ID interaction → MRTF-A-EP300 complex assembles at CaRG-box mechanoenhancers (where SRF motif is present per Cosgrove 2025 motif enrichment) → EP300 writes H3K27ac at mechanoenhancer chromatin.

On stiff ECM, MRTF-A simultaneously occupies CaRG promoters (via SRF, canonical) AND CaRG mechanoenhancers (via EP300, novel). The promoter:enhancer ratio shifts because the EP300-binding mode is only available above the G-actin depletion threshold.

### Falsifiable Predictions

1. **G-actin threshold phenocopy**: Jasplakinolide (F-actin stabilizer, 100 nM, depletes G-actin to <2 μM) on soft ECM (1 kPa) → MRTF-A ChIP-seq shows increased enhancer:promoter ratio matching stiff-ECM distribution. Cytochalasin D (1 μM, depolymerizes F-actin, restores G-actin >10 μM) on stiff ECM (50 kPa) → MRTF-A reverts to promoter-dominant distribution. If pharmacological G-actin manipulation phenocopies stiffness-dependent redistribution → G-actin threshold is the controlling variable.

2. **MRTF-A ΔRPEL mutant**: MRTF-A with all 3 RPEL modules deleted (constitutively nuclear, G-actin-insensitive, always in "open" conformation). Prediction: ChIP-seq shows HIGH enhancer:promoter ratio INDEPENDENT of ECM stiffness. Ratio matches stiff-ECM WT at both 1 kPa and 50 kPa. This confirms RPEL-mediated gating is the stiffness switch.

3. **LXXLL interaction mutant**: MRTF-A L184A/L187A/L188A (triple mutant, disrupts LXXLL-EP300 NR-ID interaction while leaving RPEL and SRF-binding intact). Prediction: MRTF-A occupies CaRG promoters normally on stiff ECM (SRF partnership preserved) but FAILS to occupy CaRG-box mechanoenhancers (EP300 not recruited) → H3K27ac lost at CaRG-box mechanoenhancers but NOT at CaRG-box promoters on stiff ECM.

4. **G-actin titration**: Latrunculin B (0.05–1.0 μM range) on 50 kPa hydrogels, measuring cytoplasmic G-actin concentration at each dose by DNase-I inhibition assay. MRTF-A enhancer:promoter ratio by ChIP-qPCR at 5 mechanoenhancer loci vs 5 promoter loci. Predict: sharp switch in ratio at G-actin concentration ~4–6 μM, consistent with RPEL occupancy dropping below 50%.

### Literature Grounding

- [GROUNDED] MRTF-A RPEL domain G-actin binding: Kd ~1 μM per module, cooperative binding controlling nuclear/cytoplasmic shuttling: Vartiainen et al. 2007 Science; Mouilleron et al. 2008 Nat Struct Mol Biol (crystal structure of RPEL-actin)
- [GROUNDED] EP300-MRTFA protein interaction: STRING 0.710 (co-expression + experimental evidence)
- [GROUNDED] MRTF-A nuclear translocation is F-actin/stiffness-dependent: Miralles et al. 2003 Cell (canonical MRTF biology)
- [GROUNDED] SRF/CaRG-box motifs enriched at stiff-ECM mechanoenhancers: Cosgrove et al. 2025 Science (motif enrichment; functional CaRG confirmed at MYH9 intron 3 mechanoenhancer)
- [GROUNDED] LXXLL helix interactions with nuclear receptor AF-2 grooves (structural basis for EP300 recruitment via LXXLL): Glass & Rosenfeld 2000 Genes Dev; p160 coactivator LXXLL-EP300 NR-ID structural data
- [INFERRED] MRTF-A LXXLL motif at Leu184-Leu188 is cryptic and EP300-specific: predicted from homology with p160 LxxLL helices; MRTF-A crystal structure does not yet show LXXLL:EP300 interaction. Requires direct confirmation.
- [INFERRED] G-actin depletes to ~3 μM on 50 kPa ECM: estimated from phalloidin intensity and F-actin:G-actin ratio measurements; cell-type specific values for fibroblasts on hydrogels not directly measured

### Counter-Evidence and Limitations

- LXXLL interaction with EP300 is predicted from p160 homology; MRTF-A may not contain a functional LXXLL motif in the relevant position — structural verification by co-IP and mutagenesis required before the mechanism is established
- G-actin depletion to ~3 μM on 50 kPa is an estimate; actual values in primary fibroblasts on hydrogels may differ, and the threshold may not be sharp
- MRTF-A has been shown to interact with EP300 (STRING 0.710), but the interaction may occur in a G-actin-independent manner in some contexts — the stiffness-dependence of the interaction requires direct demonstration

### Test Protocol

1. MRTF-A ChIP-seq (anti-MRTF-A, Sigma HPA030782, validated for ChIP in fibroblasts) on 1 vs 50 kPa hydrogels, 24h culture
2. Annotate peaks: promoter (TSS ± 1 kb) vs enhancer (H3K4me1+, >2 kb from TSS, intersected with Cosgrove 2025 mechanoenhancer catalog)
3. Jasplakinolide (100 nM) on soft ECM, cytochalasin D (1 μM) on stiff ECM — repeat ChIP-seq
4. MRTF-A ΔRPEL stable expression (lentiviral, doxycycline-inducible) → ChIP-seq at 1 and 50 kPa
5. MRTF-A L184A/L187A/L188A stable expression → H3K27ac ChIP-qPCR at 5 CaRG-box mechanoenhancers and 5 CaRG-box promoters on stiff ECM
6. G-actin quantification by DNase-I inhibition assay at each LatrunculinB dose (0.05, 0.1, 0.5, 1.0 μM) → correlate with enhancer:promoter ratio

### Confidence: 0.58
### Disciplinary Distance: 2 fields (mechanobiology ↔ enhancer epigenomics)

---

## EH2: Piezo1→Ca²⁺→CaMKII→HDAC4/5 Nuclear Export Rapidly Derepresses Mechanoenhancers (<15 min) Before YAP Condensate Amplification (30–120 min)

**Evolved from Hypothesis #H2 via Mechanism Fix**
**Parent score**: 7.50 (KILLED by critic) | **Fix applied**: CaMKII does NOT activate EP300 directly — replaced with CaMKII→HDAC4/5 nuclear export mechanism

### CRITICAL FIX APPLIED

The parent hypothesis (H2) was killed because it claimed CaMKII directly phosphorylates/activates EP300. This is incorrect:
- The calcium-dependent kinase that phosphorylates p300/CBP is **CaMKIV**, not CaMKII (Thompson lab Chemical Reviews 2014)
- CaMKII actually phosphorylates CREB at **inhibitory** Ser-142, destabilizing CREB-CBP
- The STRING score EP300-CAMK2A 0.908 reflects pathway co-occurrence in calcium signaling databases, not direct EP300 activation

**Correct route**: CaMKII → HDAC4 Ser467 phosphorylation → 14-3-3ε/ζ binding → HDAC4 nuclear export → EP300 **derepressed** at mechanoenhancers (not activated)

CaMKII also phosphorylates HDAC5 at Ser498 and Ser632 (McKinsey 2000 Mol Cell Biol) via the same mechanism. HDAC4/5 are class IIa deacetylases that normally occupy mechanoenhancers and antagonize EP300 by deacetylating H3K27ac. Their nuclear export = EP300 derepression at previously HDAC-occupied loci.

### Core Claim

Piezo1-mediated Ca²⁺ influx on stiff ECM activates CaMKII, which phosphorylates HDAC4 (Ser467) and HDAC5 (Ser498), driving their nuclear export via 14-3-3 binding within 8–15 min. HDAC4/5 removal from mechanoenhancers derepresses pre-existing EP300, which writes H3K27ac at now-unrepressed mechanoenhancer chromatin. BRD4 binds newly deposited H3K27ac → Phase 1 pre-priming is complete within 15 min.

Phase 2 (30–120 min): YAP nuclear translocation → YAP engages BRD4 already occupying pre-H3K27ac mechanoenhancers (nucleation seeds) → YAP-BRD4-MED1 condensate forms preferentially at pre-marked loci → amplifies H3K27ac to maximum signal.

**Quantitative grounding:**
- HDAC4-GFP nuclear exit t₁/₂ = ~8 min after CaMKII activation (Backs et al. 2006 PNAS, cardiac myocytes)
- Piezo1 Ca²⁺ peak amplitude on stiff ECM: ~300–500 nM (estimated from Fluo-4 measurements on 50 kPa substrates, Nguyen 2023)
- CaMKII half-maximal activation requires ~4 μM Ca²⁺ (full saturation); 400 nM Ca²⁺ activates ~8–12% of CaMKII
- Partial CaMKII activation → partial HDAC4 phosphorylation → ~30–40% of HDAC4 exported in Phase 1 → EP300 partially derepressed → Phase 1 H3K27ac = ~30–40% of maximum signal (not full activation)
- Phase 2 YAP amplification brings H3K27ac to 100%, explaining why BOTH phases are required for complete mechanoenhancer activation

### Mechanism

**Phase 1 (0–15 min):**
Cell contacts 50 kPa ECM → initial cell-matrix engagement generates membrane tension → Piezo1 activation → Ca²⁺ influx (~400 nM peak) → calmodulin activation → CaMKII autophosphorylation (Thr286) → partial CaMKII activity → phosphorylation of HDAC4 (Ser467) and HDAC5 (Ser498) → 14-3-3ε binding to pHDAC4/5 → nuclear export of ~30–40% of nuclear HDAC4/5 → EP300 partially derepressed at mechanoenhancers → EP300 writes H3K27ac (~30–40% of maximum signal) → BRD4 binds nascent H3K27ac marks → Phase 1 pre-priming complete.

**Phase 2 (30–120 min):**
Hippo pathway inactivated by cytoskeletal tension → YAP Ser127 dephosphorylated → YAP nuclear translocation → YAP finds BRD4 already at pre-H3K27ac mechanoenhancer seeds → YAP-BRD4-MED1 condensate nucleates preferentially at pre-marked loci (lower nucleation barrier) → condensate amplifies H3K27ac to 100% → mechanoenhancer fully activated → mechanoenhancer-target gene transcription.

**The mechanistic logic of two phases:** Phase 1 creates BRD4 landing pads; Phase 2 YAP condensates form preferentially at BRD4-occupied loci rather than de novo. Without Phase 1 pre-priming, YAP condensate nucleation is slower and noisier — explaining why Piezo1 inhibition delays (not eliminates) mechanoenhancer activation.

### Falsifiable Predictions

1. **Phase 1/2 kinetics**: H3K27ac at mechanoenhancers (CUT&RUN time course: t=0, 5, 15, 30, 60, 120 min after cell seeding on 50 kPa) shows biphasic rise: ~30–40% of maximum by t=15 min (Phase 1, Piezo1-dependent), then full signal by t=90 min (Phase 2, YAP-dependent). GsMTx4 (4 μM, Piezo1 inhibitor) eliminates the early phase but not the late phase.

2. **HDAC4 export confirmation**: HDAC4-GFP or endogenous HDAC4 nuclear:cytoplasmic ratio measured by immunofluorescence confocal in fibroblasts spreading on 50 kPa hydrogels. Prediction: nuclear HDAC4 decreases by >40% within 15 min of initial cell-ECM contact. GsMTx4 pre-treatment blocks HDAC4 nuclear export. CaMKII inhibitor KN-93 (5 μM) phenocopies GsMTx4 for HDAC4 export.

3. **Kinase specificity** (rules out CaMKIV route): STO-609 (CaMKK/CaMKIV pathway inhibitor, 10 μM) has NO effect on Phase 1 H3K27ac or HDAC4 nuclear export — confirming CaMKII (not CaMKIV) mediates the early phase. KN-93 (CaMKII inhibitor) DOES block Phase 1. This distinction directly addresses the CaMKII-vs-CaMKIV confusion.

4. **HDAC4/5 dependency**: HDAC4+HDAC5 double siRNA knockdown on stiff ECM → ACCELERATED early H3K27ac (no repressor to export → EP300 active from t=0) → elimination of Phase 1/Phase 2 distinction → monotonically rising H3K27ac curve without the kinetic break at 15 min. This is the positive control confirming HDAC4/5 create the Phase 1 delay.

5. **YAP-independence of Phase 1**: Constitutively nuclear YAP (YAP-5SA, Ser → Ala at 5 LATS phosphorylation sites) expressed in GsMTx4-treated cells: does NOT rescue the 15-min H3K27ac Phase 1 — confirming Piezo1 acts upstream of and independently from YAP for the early phase.

### Literature Grounding

- [GROUNDED] CaMKII phosphorylates HDAC4 at Ser467, causing nuclear export via 14-3-3 binding: Backs et al. 2006 PNAS (cardiac hypertrophy; t₁/₂ ~8 min for HDAC4-GFP export measured directly)
- [GROUNDED] CaMKII phosphorylates HDAC5 at Ser498 and Ser632, same export mechanism: McKinsey et al. 2000 Mol Cell Biol
- [GROUNDED] HDAC4/5 class IIa antagonize EP300 activity at enhancers by deacetylating H3K27ac: Mihaylova & Shaw 2013 Nat Cell Biol (class IIa HDACs as chromatin repressors)
- [GROUNDED] Piezo1 → Ca²⁺ → CaMKII activation: canonical mechanosensory pathway in fibroblasts and many other cell types
- [GROUNDED] Piezo1 → Rho-ROCK → H3K acetylation: Science Advances 2025 (epigenetic mechanical memory) — validates Piezo1 as epigenetic modifier, via a parallel pathway (Rho-ROCK) consistent with our CaMKII→HDAC4/5 route
- [GROUNDED] EP300 is the canonical H3K27 acetyltransferase at enhancers (Visel et al. 2009 Nature; Creyghton et al. 2010 PNAS)
- [INFERRED] Piezo1 Ca²⁺ peak ~400 nM on 50 kPa static hydrogels: estimated from published Fluo-4 measurements; Piezo1 responds primarily to membrane tension during initial cell spreading, may be transient on static substrates
- [INFERRED] Partial CaMKII activation at 400 nM Ca²⁺ → ~30–40% HDAC4 export: calculated from CaMKII activation kinetics (Bhattacharyya 2020); context-dependent

### Counter-Evidence and Limitations

- Piezo1 primarily responds to dynamic membrane tension and cyclic strain; on static polyacrylamide hydrogels, the Ca²⁺ transient may be confined to the first 5–10 min of cell spreading, making sustained HDAC4 export uncertain
- HDAC4/5 export kinetics measured in cardiac myocytes (Backs 2006), not fibroblasts — the time course may differ in fibroblasts on hydrogels vs. cardiomyocytes under pressure overload
- GsMTx4 inhibits other mechanosensitive channels (TREK-1) in addition to Piezo1; combination with Piezo1 knockout validation needed

### Test Protocol

1. Primary human lung fibroblasts on 50 kPa polyacrylamide (fibronectin, 0.1 mg/mL); GsMTx4 (4 μM) or DMSO pre-treatment 30 min before seeding
2. CUT&RUN for H3K27ac at t=0, 5, 15, 30, 60, 120 min after initial ECM contact (staggered seeding)
3. Target mechanoenhancers: CYR61 #740, CTGF-proximal, MYH9 intron 3 from Cosgrove 2025 catalog
4. Parallel conditions: DMSO / GsMTx4 / KN-93 (5 μM, CaMKII inhibitor) / STO-609 (10 μM, CaMKIV inhibitor) / siHDAC4+siHDAC5
5. HDAC4 immunofluorescence (nuclear:cytoplasmic ratio) at same timepoints — confocal, ≥50 cells per condition
6. YAP nuclear quantification by IF at same timepoints to confirm Phase 1/Phase 2 temporal separation

### Confidence: 0.57
### Disciplinary Distance: 3 fields (mechanobiology ↔ calcium signaling ↔ enhancer epigenomics)

---

## EH1: ECM Stress Relaxation Rate (τ₁/₂) Determines KDM6B Nuclear Retention Duration and H3K27me3 Demethylation Reach: Promoters First, Mechanoenhancers Only with Sustained Nuclear KDM6B

**Evolved from Hypothesis #H1 via Crossover (ECM viscoelasticity × KDM6B mechanoepigenetics)**
**Parent score**: 7.25 | **Expected score direction**: ↑ (Mechanistic Specificity, Novelty)

### Core Claim

The "promoter bias" wound of H1 is not a flaw — it is a prediction. KDM6B acts at promoters FIRST (high H3K27me3 density, high substrate availability, fast demethylation kinetics) and at mechanoenhancers SECOND (lower substrate density, requires sustained nuclear KDM6B). Whether KDM6B ever reaches mechanoenhancers depends on how long it remains nuclear, which is controlled not by ECM elastic stiffness alone but by ECM STRESS RELAXATION RATE (τ₁/₂) — the viscoelastic property measured by Zhang et al. 2025.

On elastic ECM (slow stress relaxation, τ₁/₂ > 200s, as in stiff polyacrylamide): cytoskeletal tension is sustained → FAK-Src-PKA signaling is sustained → KDM6B Ser1179 phosphorylation maintained → KDM6B chromatin association prolonged >2h → promoters AND mechanoenhancers demethylated.

On fast-relaxing viscoelastic ECM (τ₁/₂ < 50s, as in alginate at equivalent elastic modulus): cytoskeletal tension decays as matrix flows → FAK-Src-PKA signal decays within 30–60 min → KDM6B nuclear retention drops → only promoters demethylated (fast, first-to-complete substrate).

### Mechanism

**Step 1: ECM stress relaxation controls FAK-Src-PKA axis duration**
- Elastic ECM (slow relaxation): cell generates cytoskeletal tension → focal adhesions maintain tension → FAK Y397 autophosphorylation sustained → Src activation → PKA activation (via Src-AC-cAMP axis) → PKA phosphorylates KDM6B at Ser1179 (regulatory site identified in PKA substrate motif analysis — RRXS motif present in KDM6B)
- Viscoelastic ECM (fast relaxation): matrix flows → focal adhesion tension dissipates within τ₁/₂ → FAK-Src-PKA signal decays → KDM6B Ser1179 dephosphorylated → KDM6B dissociates from chromatin

**Step 2: KDM6B nuclear retention time determines demethylation reach**
- KDM6B turnover rate at H3K27me3 nucleosomes: ~30–90 min per nucleosome for complete demethylation (catalytic cycles: H3K27me3 → H3K27me2 → H3K27me1 → H3K27me0, each ~10–30 min)
- Promoters: high H3K27me3 density, high substrate concentration → KDM6B rapidly finds substrate → promoter demethylation complete within 30–60 min (even on viscoelastic ECM)
- Mechanoenhancers: lower H3K27me3 density (if in poised state), scattered loci → KDM6B must search chromatin longer → requires >90 min nuclear retention → only achievable on elastic ECM

**Step 3: KDM6B depletion from mechanoenhancers on viscoelastic ECM**
On fast-relaxing viscoelastic ECM at equivalent elastic modulus: promoter H3K27me3 demethylated (rapid, same as elastic ECM), but mechanoenhancer H3K27me3 remains intact. This creates a bimodal chromatin state: gene promoters are accessible, mechanoenhancers remain Polycomb-repressed → mechanoenhancer-dependent gene programs fail to activate despite nominal ECM stiffness.

### Falsifiable Predictions

1. **H3K27me3 prerequisite test** (addresses parent wound): CUT&RUN for H3K27me3 at Cosgrove 2025 mechanoenhancers on: (a) soft elastic ECM (1 kPa polyacrylamide), (b) soft fast-relaxing ECM (1 kPa alginate, τ₁/₂ ~50s), (c) stiff elastic ECM (50 kPa polyacrylamide, τ₁/₂ > 1000s). If H3K27me3 is detected at mechanoenhancers on (a) and (b) but not (c) → KDM6B demethylation is stiffness + relaxation dependent. If H3K27me3 is ABSENT on all soft conditions → mechanoenhancers are primed, not Polycomb-repressed → hypothesis falsified at this step.

2. **Viscoelasticity specificity** (key prediction): 50 kPa polyacrylamide (elastic) vs 50 kPa alginate (viscoelastic, τ₁/₂ ~50s) at identical elastic modulus: H3K27me3 at mechanoenhancers should be retained on alginate but lost on polyacrylamide. KDM6B nuclear localization at 2h should be >2-fold higher on polyacrylamide. Mechanoenhancer-target genes (CTGF, CYR61) should be >2-fold more active on polyacrylamide at equivalent stiffness. ECM stress relaxation rate, not elastic modulus, is the controlling variable.

3. **Temporal sequence**: H3K27me3 loss at target-gene PROMOTERS should precede H3K27me3 loss at MECHANOENHANCERS by 30–60 min on elastic stiff ECM (50 kPa polyacrylamide, CUT&RUN time course at t=30, 60, 90, 120, 180 min). This temporal ordering — promoter first, enhancer second — is the defining prediction of the "KDM6B reach" model.

4. **KDM6B Ser1179 phosphorylation**: Develop or validate phospho-specific antibody (or use phospho-enrichment proteomics) to measure pKDM6B-Ser1179 in nuclear fractions of fibroblasts on elastic vs viscoelastic ECM. H-89 (PKA inhibitor, 10 μM) should reduce KDM6B chromatin occupancy by ChIP and block mechanoenhancer (but not promoter) H3K27me3 demethylation on elastic ECM.

### Literature Grounding

- [GROUNDED] ECM stress relaxation rate controls epigenome: Zhang et al. 2025 (viscoelastic ECM → distinct epigenomic outcomes from elastic ECM at equivalent modulus)
- [GROUNDED] KDM6B activity regulated by ECM stiffness/stress relaxation: Tayler et al. 2026 (Mol Biol Cell; MSC context, but principle generalizable)
- [GROUNDED] FAK-Src activation by sustained ECM tension (focal adhesion signaling): Geiger et al. 2009 Nat Rev Mol Cell Biol; Schwartz 2010 Science
- [GROUNDED] PKA phosphorylation of chromatin regulators controlling nuclear retention: multiple precedents (HDAC nuclear export by PKA; DNMT3A nuclear retention by PKA); KDM6B Ser1179 PKA site is a prediction from motif analysis
- [GROUNDED] KDM6B demethylates H3K27me3 at distal regulatory elements in some contexts: Ntziachristos et al. 2014 Nat Med (neuroblastoma — enhancer-level KDM6B activity)
- [INFERRED] KDM6B nuclear retention duration is controlled by FAK-Src-PKA axis: mechanistic model; PKA phosphorylation of KDM6B at Ser1179 specifically is computational prediction from RRXS motif scanning, not yet validated biochemically
- [INFERRED] Mechanoenhancers have lower H3K27me3 density than promoters on soft ECM: the critical unverified premise (addressed by Prediction 1 as first falsifiable test)

### Counter-Evidence and Limitations

- H3K27me3 at mechanoenhancers may not exist in the relevant cell type (lung fibroblasts) — the hypothesis is falsified if mechanoenhancers are in a primed (H3K4me1+/H3K27me3−) rather than Polycomb-repressed state. Prediction 1 explicitly tests this and accepts falsification.
- FAK-Src-PKA → KDM6B nuclear retention is a multi-step extrapolation; each step is individually plausible but the complete chain has not been demonstrated in any system
- Alginate and polyacrylamide gels have different surface chemistry, porosity, and fibronectin coupling efficiency, which could independently alter cell behavior independently of stress relaxation

### Test Protocol

1. Fabricate matched-modulus gels: 50 kPa polyacrylamide (elastic, τ₁/₂ > 1000s) and 50 kPa oxidized alginate (fast-relaxing, τ₁/₂ ~50s, achievable by degree of crosslinker); fibronectin-coated at equal density (verify by ELISA)
2. CUT&RUN for H3K27me3, H3K27ac, H3K4me1 at Cosgrove 2025 mechanoenhancer catalog loci at t=30, 60, 90, 120, 180 min after cell seeding (n=3 biological replicates per condition)
3. KDM6B nuclear localization by immunofluorescence (KDM6B antibody, Abcam ab213831) at same timepoints — nuclear:cytoplasmic ratio in ≥50 cells per condition
4. H-89 (10 μM PKA inhibitor) pre-treatment on elastic ECM → repeat CUT&RUN time course
5. KDM6B siRNA knockdown (confirm by Western) → repeat H3K27me3/H3K27ac CUT&RUN on both gel types — confirms KDM6B specificity of demethylation
6. Mechanoenhancer-target gene expression: RT-qPCR for CTGF, CYR61, MYH9 at same conditions and timepoints

### Confidence: 0.56
### Disciplinary Distance: 3 fields (mechanobiology ↔ ECM viscoelasticity ↔ enhancer epigenomics)

---

## EH5: YAP Condensate Coalescence Events (Not Single-Condensate Surface Tension) Drive Multi-Locus Mechanoenhancer Co-Localization on Stiff ECM

**Evolved from Hypothesis #H5 via Mutation + Specification**
**Parent score**: 7.10 | **Expected score direction**: ↑ (Mechanistic Specificity, Testability, Groundedness)

### Core Claim

H5's major mechanistic wound — "condensate surface tension insufficient to pull loci from 400→100 nm" — is resolved by replacing single-condensate surface tension with CONDENSATE COALESCENCE DYNAMICS as the driving mechanism. Multiple small YAP-BRD4 condensates (50–100 nm each) nucleate at adjacent mechanoenhancers independently → condensate-condensate coalescence (Ostwald ripening, driven by surface tension minimization) merges adjacent condensates → each coalescence event displaces the two anchoring chromatin loci by 50–100 nm toward each other. Sequential coalescence of 4–6 condensates progressively collapses inter-locus distance from ~400 nm to <100 nm in discrete, measurable steps.

This resolves the Cosgrove 2025 "86.2% loop-less" anomaly: non-looped mechanoenhancers co-localize not through cohesin-mediated looping but through progressive condensate merger events, creating transient multi-locus hubs that activate multiple mechanoenhancer-target gene pairs simultaneously.

**CQ4 applied:** Verteporfin (multiple targets, off-target concerns) replaced with IDR-deleted YAP (F95A/W96A; Boija et al. 2018 Cell), which is condensate-incompetent while retaining TEAD binding. This is the clean condensate-specific perturbation.

### Mechanism

**Why single-condensate surface tension is insufficient (physics fix):**
- Single 200 nm condensate surface tension γ ~10⁻⁶ N/m → force F = γ(2/r) = 10 pN
- Chromatin stiffness κ at 100 nm scale ~20 pN/nm (Brahmachari 2022 Biophysical J)
- Maximum chromatin deformation per contact point: F/κ ~0.5 nm — far below what is needed to pull loci from 400 nm → 100 nm

**Why coalescence works:**
- Multiple small condensates (50–100 nm, each anchored to one mechanoenhancer) undergo Ostwald ripening — larger condensates grow at expense of smaller ones, AND adjacent condensates merge when their surfaces contact
- Each merger event: two condensates (each 100 nm, anchored to loci ~300 nm apart) merge into one 140 nm condensate → the merged condensate's center-of-mass is ~150 nm from each locus → loci are now 200 nm closer than before merger
- Sequential mergers (4–6 events) over 30–90 min → inter-locus distance reduced from ~400 nm to <100 nm in measurable steps of 50–150 nm each

**Timeline:**
0 min: YAP enters nucleus, individual 50–100 nm condensates nucleate at each mechanoenhancer locus
15–30 min: condensate growth (Ostwald ripening) → first coalescence events as nearby condensates contact → first discrete 50–100 nm inter-locus distance reduction
30–90 min: sequential coalescence → progressive co-localization of 3–6 mechanoenhancer loci within shared 200–400 nm hub
>90 min: equilibrium hub size; mechanoenhancer-target gene activation

**Distinguishing from transcription factories:**
Transcription factories (RNA Pol II clustering, Cho 2018 Cell) are driven by Pol II CTD phase separation and can also co-localize genomic loci. However:
- Pol II factories are sensitive to flavopiridol (CDK9 inhibitor, prevents Pol II elongation) and α-amanitin (Pol II inhibitor)
- YAP condensates are NOT Pol II-dependent; IDR-deleted YAP eliminates YAP condensates without affecting Pol II clustering
- If non-looped mechanoenhancer co-localization persists after IDR-deleted YAP but disappears after flavopiridol → transcription factory mechanism
- If co-localization disappears after IDR-deleted YAP but persists after flavopiridol → YAP condensate mechanism

### Falsifiable Predictions

1. **IDR-deleted YAP (replaces verteporfin)**: Stable expression of YAP F95A/W96A (condensate-incompetent, TEAD-binding intact; Boija et al. 2018 Cell) in fibroblasts on stiff ECM (50 kPa). Prediction: non-looped mechanoenhancer pair co-localization (measured by 3-color Oligopaint FISH, ≥5 non-looped pairs from Cosgrove 2025) fails to develop even though YAP-TEAD transcription of a subset of target genes persists. This test is cleaner than verteporfin because IDR-deleted YAP specifically disrupts condensate-mediated co-localization without off-target photosensitizer effects.

2. **Orthogonal competition (transcription factory control)**:
   - IDR-deleted YAP: eliminates YAP condensates
   - Flavopiridol (1 μM, 30 min): dissolves Pol II elongation complexes and transcription factories
   - Comparison: If mechanoenhancer co-localization is LOST with IDR-deleted YAP but RETAINED with flavopiridol → YAP condensate mechanism confirmed, transcription factory ruled out. If RETAINED with IDR-deleted YAP but LOST with flavopiridol → transcription factory mechanism.

3. **Live imaging of coalescence dynamics**: Live-cell ORCA or lattice light-sheet microscopy imaging of 3 non-looped mechanoenhancer loci (Oligopaint probes with different fluorophores) during fibroblast spreading on 50 kPa hydrogel (t=0–120 min). Prediction:
   - WT YAP: DISCRETE spatial jumps in inter-locus distance at t=30–90 min; each jump = 50–150 nm; 3–5 discrete events detectable per cell
   - YAP F95A/W96A: NO discrete jumps; inter-locus distances remain stochastically distributed
   - This is the defining prediction: condensate coalescence should be visible as stepwise, not continuous, convergence

4. **Micro-C condensate specificity** (preserved from H5): IDR-deleted YAP on stiff ECM → Micro-C shows loss of non-looped mechanoenhancer contacts at target genes, with NO gain in cohesin-mediated loops (CTCF/cohesin-anchored loops unaffected). Flavopiridol → same Micro-C analysis: if different contact patterns lost → different mechanism.

### Literature Grounding

- [GROUNDED] 86.2% of mechanoenhancer–gene connections lack annotated chromatin loops: Cosgrove et al. 2025 Science (Micro-C data from same study)
- [GROUNDED] Condensate coalescence (Ostwald ripening) is a general property of phase-separated condensates and drives progressive merger in cells: Brangwynne et al. 2011 PNAS (nucleolus growth); Feric et al. 2016 Cell (multiphase condensate organization)
- [GROUNDED] Phase-separated condensates pull genomic loci together via surface-tension-driven coalescence: Shin et al. 2018 Cell (CasDrop; the mechanism is coalescence, not single-condensate tension)
- [GROUNDED] YAP IDR-deleted (F95A/W96A) is condensate-incompetent while retaining TEAD binding: Boija et al. 2018 Cell (Med1-IDR co-condensation with TF IDRs; YAP condensate-essential residues identified)
- [GROUNDED] Transcription factories (Pol II clustering) can co-localize genomic loci and are flavopiridol-sensitive: Cho et al. 2018 Cell; Sabari et al. 2018 Science
- [INFERRED] YAP-BRD4 condensate coalescence specifically drives mechanoenhancer co-localization in fibroblasts on stiff ECM: the application of condensate coalescence physics to mechanoenhancers is novel and untested; Shin 2018 used artificial IDPs
- [INFERRED] Condensate coalescence step size ~50–150 nm: estimated from condensate biophysics; actual step sizes in fibroblast nucleus for YAP condensates at mechanoenhancers not measured

### Counter-Evidence and Limitations

- YAP F95A/W96A condensate-incompetent mutations from Boija 2018 were characterized in the context of MED1-IDR co-condensation; in the context of BRD4-YAP mechanoenhancer condensates, these mutations may not fully abolish condensate formation if BRD4 IDR compensates
- Live imaging of individual condensate coalescence events at specific genomic loci is technically at the edge of current resolution capabilities — requires simultaneous super-resolution + live-cell imaging + multiplexed chromatin labeling
- Coalescence dynamics in the nucleus may be much slower than in model systems due to chromatin-mediated viscoelastic resistance; discrete steps may not be resolvable in live imaging timescales

### Test Protocol

1. Generate stable fibroblast lines expressing: (a) WT YAP-GFP, (b) YAP F95A/W96A-GFP (condensate-incompetent), (c) YAP S127A-GFP (constitutively nuclear, positive control), via lentiviral delivery at near-endogenous expression
2. Design Oligopaint FISH probes for 5 non-looped mechanoenhancer pairs from Cosgrove 2025 catalog (pairs validated to lack Micro-C loops but show H3K27ac on stiff ECM) — 3 colors for tri-locus imaging
3. Fixed-cell Oligopaint FISH on 1 kPa vs 50 kPa hydrogels (24h), WT YAP vs F95A/W96A vs flavopiridol-treated: measure inter-locus distances (n≥50 cells, per pair); compare distance distributions by KS test
4. Live-cell ORCA: 50 kPa hydrogels, fibroblasts with Oligopaint-labeled loci (3 pairs, 3 colors) + YAP-GFP; image every 2 min for 2h during cell spreading. Track inter-locus distances; detect discrete jump events in WT vs F95A/W96A cells
5. Micro-C library prep: fibroblasts on 50 kPa, conditions (a) WT YAP, (b) YAP F95A/W96A, (c) flavopiridol — focus analysis on non-looped mechanoenhancer–gene pairs from Cosgrove 2025 (n=500 pairs with H3K27ac but no Micro-C loop)

### Confidence: 0.55
### Disciplinary Distance: 3 fields (mechanobiology ↔ condensate biophysics ↔ enhancer 3D genome)

---

## Diversity Summary

| Hypothesis | Bridge Mechanism | Distinct? |
|-----------|-----------------|-----------|
| EH3 | BRD4 IDR multivalent LLPS cooperativity → mechanical threshold switch at 5–15 kPa | ✅ |
| EH4 | G-actin threshold → RPEL conformational unmasking → SRF-independent EP300 recruitment at CaRG enhancers | ✅ |
| EH2 | Piezo1→Ca²⁺→CaMKII→HDAC4/5 nuclear export → EP300 derepression (Phase 1) + YAP condensate amplification (Phase 2) | ✅ |
| EH1 | ECM stress relaxation rate (τ₁/₂) → KDM6B nuclear retention duration → promoter→mechanoenhancer H3K27me3 demethylation cascade | ✅ |
| EH5 | YAP condensate coalescence (Ostwald ripening) → discrete 50–150 nm spatial jumps → multi-locus mechanoenhancer co-localization | ✅ |

**Top bridge diversity**: EH3 (condensate biophysics), EH4 (TF allostery), EH2 (Ca²⁺ kinase/HDAC derepression), EH1 (viscoelastic mechanical signaling), EH5 (3D genome coalescence). No overlap.
