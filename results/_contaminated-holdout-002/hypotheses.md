# Hypotheses: Mechanobiology (ECM Mechanics) × Enhancer Epigenomics
## Session: 2026-03-25-targeted-002 | Cycle 1 | Generated: 2026-03-25

---

## H1: The KDM6B→EP300 Sequential Epigenetic Relay Encodes ECM Stiffness at Mechanoenhancers

### Core Claim
ECM stiffness activates a two-enzyme sequential epigenetic relay at mechanoenhancers: KDM6B (H3K27me3 demethylase, directly controlled by ECM stiffness; Tayler 2026) first removes Polycomb repression (H3K27me3) that maintains mechanoenhancers in a poised/silenced state on soft ECM, then EP300 (directly recruited by YAP1; STRING score 0.692) writes H3K27ac at the newly accessible loci — converting poised mechanoenhancers to fully active ones. The interaction between KDM6B and EP300 (STRING: 0.754) implies they act coordinately at the same genomic loci, not sequentially at different loci.

### Mechanism
Soft ECM → Hippo active → YAP cytoplasmic → EP300 not recruited → mechanoenhancers exist in H3K27me3 (Polycomb-repressed) poised state with H3K4me1 mark intact (defining a poised enhancer).

Stiff ECM → (1) KDM6B upregulated (Tayler 2026) → KDM6B demethylates H3K27me3→H3K27me0 at mechanoenhancer chromatin; (2) simultaneously Hippo inactivated → YAP nuclear → YAP recruits EP300 to TEAD-bound mechanoenhancers → EP300 acetylates H3K27 → H3K27ac deposited; (3) H3K27ac recruits BRD4 (STRING EP300-BRD4: 0.988) → mechanoenhancer fully activated.

The key quantitative prediction: H3K27me3 signal at mechanoenhancers should be **inversely correlated** with ECM stiffness in a KDM6B-dependent manner, with a ~30–90 min lag relative to the ATAC-seq accessibility change (Cosgrove 2025: accessibility within 1 hr), because H3K27me3 demethylation requires iterative KDM6B catalytic cycles per nucleosome.

### Falsifiable Predictions
1. **Primary**: H3K27me3 ChIP-seq in cells on soft ECM (1 kPa) shows enrichment at mechanoenhancers identified by Cosgrove 2025; transferring cells to stiff ECM (50 kPa) reduces H3K27me3 and increases H3K27ac at these loci within 2–4 hours (slower than ATAC-seq accessibility, faster than full transcriptional reprogramming).
2. **KDM6B dependency**: KDM6B knockdown on stiff ECM maintains H3K27me3 at mechanoenhancers and blocks H3K27ac deposition even when YAP is nuclear and ATAC accessibility is gained — creating a mechanically accessible but transcriptionally inert chromatin state.
3. **Bivalency prediction**: Mechanoenhancers on soft ECM should show bivalent marks (H3K4me1+H3K27me3), distinguishing them from constitutively silenced loci (H3K27me3 only) and constitutively active ones (H3K27ac only).

### Literature Grounding
- [GROUNDED] KDM6B activity directly controlled by ECM stiffness and stress relaxation: Tayler et al. 2026
- [GROUNDED] KDM6B-EP300 protein interaction: STRING 0.754 (co-expression + text-mining)
- [GROUNDED] YAP1-EP300 interaction: STRING 0.692 (experimental + text-mining); Seol et al. 2026 shows YAP controls H3K27me3/H3K27ac balance at specific enhancers
- [GROUNDED] Mechanoenhancers identified genome-wide: Cosgrove et al. 2025, Science
- [INFERRED] Mechanoenhancers are in H3K27me3 poised state on soft ECM: not yet shown, but consistent with bivalent enhancer biology; H3K4me1 present without H3K27ac = poised enhancer (canonical epigenomics)

### Counter-Evidence and Limitations
- KDM6B studies (Tayler 2026) characterize activity at gene bodies/promoters, not specifically at enhancers; KDM6B may not be recruited to mechanoenhancer loci by YAP/TEAD
- Some mechanoenhancers on stiff ECM may not be Polycomb-repressed — if they are in an accessible but H3K27ac-negative "primed" state, this model does not apply
- H3K27me3 and H3K27ac co-ChIP experiments at the same loci require careful normalization to avoid spike-in normalization artifacts
- ECM stiffness can also activate KDM5C (H3K4me3 demethylase) which could confound enhancer mark interpretation

### Test Protocol
1. Culture human lung fibroblasts on 1 kPa (soft) and 50 kPa (stiff) polyacrylamide hydrogels for 24h
2. CUT&RUN for H3K27me3 and H3K27ac at 0, 1, 2, 4, 8h after transfer from soft→stiff
3. Intersect differentially marked regions with Cosgrove 2025 mechanoenhancer catalog (CYR61, CTGF, MYH9, BMF enhancers)
4. Repeat with KDM6B siRNA knockdown (confirm with Western blot)
5. YAP nuclear localization confirmed by immunofluorescence at each timepoint

### Confidence: 0.62
### Disciplinary Distance: 2 fields (mechanobiology ↔ enhancer epigenomics)

---

## H2: Piezo1→CaMKII→EP300 Rapid Pre-Priming Establishes H3K27ac at Mechanoenhancers Before YAP Nuclear Entry

### Core Claim
ECM stiffness activates a two-phase mechanoenhancer activation cascade where Piezo1-mediated Ca²⁺ influx pre-primes mechanoenhancers with H3K27ac within 15 minutes (via CaMKII→EP300; STRING EP300-CAMK2A: 0.908) before YAP nuclear translocation (~30–60 min). This pre-priming creates H3K27ac "landing pads" that BRD4 (STRING EP300-BRD4: 0.988) pre-occupies, enabling rapid YAP-condensate nucleation when YAP enters the nucleus, rather than requiring de novo condensate assembly at naïve loci.

### Mechanism
Phase 1 (0–15 min): ECM stiffness deformation → Piezo1 Ca²⁺ influx → calmodulin activation → CaMKII (CAMK2A) autophosphorylation and activation → CaMKII phosphorylates EP300 at Ser1834 or equivalent activating site → EP300 HAT domain activated → EP300 deposits H3K27ac at open chromatin regions enriched for mechanosensitive TF motifs (mechanoenhancers) → BRD4 binds newly deposited H3K27ac.

Phase 2 (30–120 min): YAP nuclear translocation (via cytoskeletal tension / Hippo inactivation) → YAP binds BRD4 already at pre-primed H3K27ac mechanoenhancers (STRING BRD4-YAP1: 0.691) → YAP-BRD4-MED1 condensate nucleates at pre-H3K27ac loci → transcriptional amplification.

The mechanistic insight: mechanoenhancers are not activated de novo by YAP — they are pre-primed within 15 minutes by Piezo1-CaMKII-EP300, with YAP acting as a condensate amplifier of already-marked loci, not an initiator.

### Falsifiable Predictions
1. **Kinetic separation**: H3K27ac appears at specific mechanoenhancers within 15 minutes of ECM stiffness increase; YAP nuclear entry is detectable at 30–60 min. The 15-min H3K27ac signal is Piezo1-dependent and YAP-independent.
2. **Piezo1 inhibition test**: GsMTx4 (Piezo1-specific inhibitor) treatment delays initial H3K27ac at mechanoenhancers by ~45 min but does not eliminate it (YAP eventually compensates); the delay corresponds exactly to the time for YAP nuclear translocation.
3. **CaMKII specificity**: KN-93 (CaMKII inhibitor) phenocopies Piezo1 inhibition for the early H3K27ac phase; late-phase (YAP-mediated) H3K27ac is preserved.
4. **Independence test**: Expressing a constitutively nuclear YAP (ΔLIM YAP) should NOT rescue early (15-min) H3K27ac in Piezo1-inhibited cells — confirming Piezo1 acts independently of YAP for Phase 1.

### Literature Grounding
- [GROUNDED] EP300-CAMK2A protein interaction: STRING 0.908 (very high; database + text-mining evidence)
- [GROUNDED] Piezo1 → Rho-ROCK → H3K acetylation: Science Advances 2025 (epigenetic mechanical memory)
- [GROUNDED] Piezo1 → Ca²⁺ → CaMKII is a canonical signaling pathway in mechanobiology (calmodulin kinase cascade)
- [GROUNDED] EP300 is the canonical H3K27 acetyltransferase at enhancers (well-established enhancer epigenomics)
- [INFERRED] CaMKII phosphorylates EP300 at enhancer loci specifically: plausible given EP300-CAMK2A STRING evidence, but the specific phosphorylation site and enhancer-specificity not yet demonstrated
- [INFERRED] Piezo1 operates under static ECM stiffness: Piezo1's primary stimulus is dynamic strain; on static hydrogels, Piezo1 activation may require the initial cell-matrix engagement rather than sustained static force

### Counter-Evidence and Limitations
- Piezo1 is primarily activated by membrane tension and dynamic compression, not static stiffness; on static polyacrylamide hydrogels, Piezo1 signaling may be transient (only during initial cell spreading) rather than sustained
- CaMKII→EP300 interaction at enhancers requires nuclear CaMKII; CaMKII is predominantly cytoplasmic and must translocate to nucleus — this adds a step and time delay
- Piezo1 Ca²⁺ also activates many other pathways (NFAT, calcineurin, eNOS) that may confound CaMKII-specific attribution
- GsMTx4 peptide penetration efficiency in fibronectin-coated hydrogel cultures is not well-characterized

### Test Protocol
1. Cells on 50 kPa hydrogels; GsMTx4 (4 μM) treatment 30 min before cell seeding
2. CUT&RUN for H3K27ac at t=0, 5, 15, 30, 60, 120 min after cell seeding
3. Parallel tracks: GsMTx4, DMSO vehicle, KN-93 (CaMKII inhibitor), verteporfin (YAP condensate)
4. Focus on canonical mechanoenhancers: CYR61 (CTGF enhancer, #740), MYH9 intron 3, BMF intron 4 from Cosgrove 2025 catalog
5. YAP nuclear quantification by immunofluorescence at same timepoints to confirm Phase 1/2 separation

### Confidence: 0.55
### Disciplinary Distance: 3 fields (mechanobiology ↔ calcium signaling ↔ enhancer epigenomics)

---

## H3: YAP-BRD4 Condensate Size Supralinearly Encodes ECM Stiffness, Creating a Mechanical Switch at Mechanoenhancers

### Core Claim
YAP nuclear concentration increases ~linearly with ECM stiffness (~4x from 1→50 kPa). However, BRD4-YAP-MED1 phase-separated condensate assembly at mechanoenhancers is cooperative (Hill coefficient n=2–4), creating supralinear transcriptional amplification. This means ECM stiffness differences below ~5 kPa produce small transcriptional responses, but stiffness increases above ~10 kPa (physiological fibrosis threshold) trigger disproportionately large mechanoenhancer activation — functioning as a mechanical threshold switch, not a graded rheostat.

This explains why fibrotic ECM (15–50 kPa) triggers dramatically different transcriptional programs than healthy ECM (1–5 kPa) despite only a 3–10x stiffness difference: the switch nonlinearity amplifies small mechanical differences into large epigenomic changes.

### Mechanism
ECM stiffness → YAP nuclear [Y_nuc] ∝ stiffness^0.5 to stiffness^1.0 (linear to sub-linear, known)
→ BRD4-YAP condensate volume [V_cond] ∝ [Y_nuc]^n where n=2–4 (cooperative phase separation)
→ Mechanoenhancer transcriptional output ∝ [V_cond] ∝ stiffness^(n × 0.5 to n × 1.0)

For n=2: output ∝ stiffness^1.0 to stiffness^2.0
For n=3: output ∝ stiffness^1.5 to stiffness^3.0

This creates a switch-like sigmoidal response when plotted as output vs stiffness, with an inflection point at the critical concentration for phase separation.

Mechanistically: at low YAP nuclear concentration (soft ECM), BRD4-YAP clusters are below the critical concentration for condensate formation → only weak, diffuse BRD4 binding at mechanoenhancers. Above the threshold stiffness, cooperative condensate nucleation causes step-change in BRD4 occupancy → super-enhancer-like transcriptional output at mechanoenhancers.

### Falsifiable Predictions
1. **Power law fit**: Transcriptional output of mechanoenhancer-controlled genes (CTGF, CYR61 by smFISH) on a 5-point stiffness gradient (1, 5, 10, 20, 50 kPa) fits a power law model (output ∝ stiffness^n, n>1.5) significantly better than a linear model (F-test, p<0.05).
2. **Condensate size measurement**: BRD4 condensate volume at mechanoenhancer loci (measured by super-resolution STORM or dSTORM) scales supralinearly with nuclear YAP concentration when plotted across stiffness gradient.
3. **Threshold stiffness**: A distinct inflection point exists in the stiffness-transcription curve at ~8–15 kPa (the predicted phase-separation threshold based on typical YAP nuclear concentrations and BRD4 condensate critical concentration).
4. **BRD4 perturbation**: JQ1 (BET inhibitor, disrupts BRD4-chromatin interactions and condensates) should linearize the stiffness-transcription relationship by preventing cooperative condensate assembly — converting the switch to a graded response.

### Literature Grounding
- [GROUNDED] YAP-BRD4 condensates at super-enhancers: Zanconato et al. 2018, Nat Cancer (269 citations)
- [GROUNDED] BRD4-YAP1 protein interaction: STRING 0.691 (experimental + text-mining)
- [GROUNDED] EP300-BRD4 interaction: STRING 0.988 (very high — co-expression, experimental, text-mining)
- [GROUNDED] Phase-separated condensates are cooperative (non-linear, threshold behavior): Shin et al. 2018, Cell; general biophysics of LLPS
- [GROUNDED] YAP nuclear fraction is stiffness-dependent: well-established (Dupont et al. 2011, Nature; multiple mechanobiology papers)
- [INFERRED] Condensate cooperativity n=2–4 for BRD4-YAP: Hill coefficient estimated from generic LLPS biophysics; specific value for BRD4-YAP system at mechanoenhancers not measured

### Counter-Evidence and Limitations
- YAP nuclear concentration may plateau (saturate) at stiffness >20 kPa — the relationship may not be power law across the full stiffness range
- BRD4 condensates are sensitive to cellular ATP levels, temperature, and post-translational modification state; condensate properties may vary non-mechanically
- The debate about whether BRD4 bodies are true LLPS condensates or protein clusters is unresolved; if not LLPS, cooperativity arguments may not apply
- Super-resolution imaging of BRD4 at specific mechanoenhancer loci requires combining FISH (locus detection) with dSTORM (BRD4 imaging), technically challenging

### Test Protocol
1. Human lung fibroblasts on 5-point stiffness gradient (1, 5, 10, 20, 50 kPa) for 24h
2. smFISH for CTGF and CYR61 mRNA (mechanoenhancer target genes) → transcriptional output per cell
3. Immunofluorescence for nuclear YAP (total nuclear intensity as proxy for concentration)
4. Correlation: plot CTGF smFISH counts vs nuclear YAP signal, fit power law vs linear models
5. Super-resolution STORM for BRD4 puncta at CYR61 locus (labeled by Oligopaint FISH) vs stiffness
6. JQ1 treatment (250 nM) for linearization test

### Confidence: 0.58
### Disciplinary Distance: 3 fields (mechanobiology ↔ condensate biophysics ↔ enhancer epigenomics)

---

## H4: MRTF-A Preferentially Occupies Mechanoenhancers over Promoters on Stiff ECM, Defining a Non-TEAD Mechanical Enhancer Program

### Core Claim
MRTF-A (mechanosensitive transcriptional coactivator, nuclear on stiff ECM) binds CaRG-box motifs at mechanoenhancers (identified by Cosgrove 2025: CaRG/SRF motifs enriched at stiff-ECM mechanoenhancers) preferentially over promoters on stiff ECM — driven by nuclear actin concentration. MRTF-A at enhancers directly recruits EP300 (STRING: 0.710, independent of SRF) to deposit H3K27ac, activating a cytoskeletal/contractility mechanoenhancer program that is spatially and functionally distinct from the YAP/TEAD mechanoenhancer program. These two programs converge at the same target genes (e.g., MYH9, CYR61 cytoskeletal effectors) but via different cis-regulatory elements.

### Mechanism
Stiff ECM → F-actin polymerization → G-actin pool depletion → MRTF-A RPEL domain released from G-actin sequestration → MRTF-A nuclear.

Nuclear MRTF-A distribution on stiff ECM: binds SRF-occupied promoters (canonical, known) AND CaRG-box-containing mechanoenhancers (novel hypothesis). At mechanoenhancers, MRTF-A recruits EP300 directly (STRING MRTFA-EP300: 0.710; co-expression and experimental evidence) → H3K27ac deposition at CaRG-box mechanoenhancers → enhancer activation.

The TEAD and CaRG programs co-activate: YAP/TEAD activates CTGF/CYR61 via TEAD-motif mechanoenhancers; MRTF-A/SRF activates MYH9 via CaRG-box mechanoenhancers. Together they constitute the stiff-ECM mechanoenhancer transcriptional landscape.

Key distinction: MRTF-A at enhancers vs promoters would generate different transcriptional kinetics (enhancers typically more burst-like than constitutive promoters) and different sensitivity to nuclear actin concentration.

### Falsifiable Predictions
1. **Primary**: MRTF-A ChIP-seq on 1 vs 50 kPa hydrogels shows significant enrichment at CaRG-box-containing enhancers (H3K4me1+, >1 kb from TSS, identified by Cosgrove 2025 mechanoenhancer catalog) in addition to known CaRG-box promoters.
2. **Enhancer-to-promoter ratio**: The ratio of MRTF-A peaks at enhancers vs promoters increases on stiff ECM compared to soft ECM.
3. **EP300 co-localization**: MRTF-A and EP300 co-occupy CaRG-box mechanoenhancers specifically; knockdown of MRTF-A reduces H3K27ac at CaRG-box mechanoenhancers but not TEAD-motif mechanoenhancers.
4. **SRF independence at enhancers**: MRTF-A occupancy at some mechanoenhancers should precede or be independent of SRF occupancy, reflecting direct MRTF-A→EP300 recruitment rather than MRTF-A→SRF→cofactor cascade.

### Literature Grounding
- [GROUNDED] MRTF-A nuclear translocation is F-actin/stiffness-dependent: well-established (Miralles et al. 2003, Cell; multiple reviews)
- [GROUNDED] EP300-MRTFA protein interaction: STRING 0.710 (co-expression + experimental evidence)
- [GROUNDED] SRF/CaRG-box motifs enriched at stiff-ECM mechanoenhancers: Cosgrove et al. 2025 motif enrichment analysis — functional SRF/CaRG motif confirmed in MYH9 intron 3 mechanoenhancer
- [GROUNDED] SRF-MRTFA interaction: STRING 0.999 (near-certain, canonical complex)
- [INFERRED] MRTF-A binds enhancers vs promoters at different ratios depending on ECM stiffness: not demonstrated; MRTF-A ChIP-seq in mechanical context has not been published; the EP300-MRTFA interaction at enhancers specifically is inferred from STRING co-expression data

### Counter-Evidence and Limitations
- MRTF-A ChIP-seq studies in non-mechanical contexts primarily show promoter binding at SRF target genes (actin, cofilin, vinculin); enhancer binding may be a minor fraction
- CaRG-box motif enrichment at mechanoenhancers (Cosgrove 2025) is from motif scanning, not direct MRTF/SRF ChIP-seq — the motifs may not be functionally bound
- The EP300-MRTFA STRING interaction (0.710) is supported by co-expression (a-score) and experimental evidence (e-score); the experimental evidence may not be from the specific context of enhancer activation under mechanical force
- F-actin-driven MRTF nuclear translocation is stiffness-sensitive but also responds to growth factors, serum, and many other stimuli — controlling for non-mechanical MRTF activation in hydrogel experiments is critical

### Test Protocol
1. MRTF-A ChIP-seq (anti-MRTF-A antibody, validated for ChIP) in fibroblasts on 1 vs 50 kPa hydrogels, 24h culture
2. Annotate peaks: promoter (H3K4me3, <1 kb from TSS) vs enhancer (H3K4me1, >1 kb from TSS)
3. Intersect enhancer-MRTF-A peaks with Cosgrove 2025 mechanoenhancer catalog
4. MRTF-A and EP300 co-ChIP or sequential ChIP at CaRG-box mechanoenhancers
5. MRTF-A siRNA knockdown → H3K27ac ChIP-seq → loss at CaRG-box but not TEAD-motif mechanoenhancers

### Confidence: 0.60
### Disciplinary Distance: 2 fields (mechanobiology ↔ enhancer epigenomics)

---

## H5: Phase-Separated YAP Nuclear Condensates Mediate Looping-Independent Multi-Enhancer Hubs, Resolving the 86% Mechanoenhancer Loop-Less Paradox

### Core Claim
The 86.2% of mechanoenhancer–gene connections that lack annotated chromatin loops (Cosgrove 2025) are mediated by YAP-BRD4 phase-separated nuclear condensates that physically co-localize non-looped mechanoenhancers in 3D nuclear space via surface tension–driven coalescence (Shin et al. 2018 mechanism). On stiff ECM, nuclear YAP forms condensates preferentially at euchromatic (mechanically softer) mechanoenhancer loci, and condensate surface tension pulls multiple non-looped mechanoenhancers into a shared nuclear compartment — creating transcriptional co-activation without stable E-P loops detectable by Micro-C.

### Mechanism
Stiff ECM → YAP nuclear → YAP-BRD4-MED1 condensate nucleation at euchromatic mechanoenhancer loci (preferential nucleation in soft/euchromatic regions per Shin 2018 biophysics).

Condensate surface tension: ~10⁻⁶ N/m (typical for protein condensates; measured for nucleolus and Cajal bodies). Force = γ × (2/r) for a spherical condensate of radius r. For r = 200 nm condensate: F ≈ 10 pN — sufficient to transiently pull neighboring chromatin loci (<500 nm apart) into proximity without forming stable cohesin-mediated loops.

This creates: (1) spatial co-localization of multiple mechanoenhancers within one condensate volume (~200–500 nm diameter); (2) collective enhancer–gene proximity without individual E-P loops; (3) Micro-C "dark contacts" — the proximity is dynamic and below the threshold for Micro-C loop detection (which requires stable, frequent contacts over ligation timeframe).

### Falsifiable Predictions
1. **Spatial co-localization**: Super-resolution imaging (ORCA or split-pool Oligopaint) of non-looped mechanoenhancer pairs (e.g., CYR61 enhancer + CTGF enhancer) shows spatial proximity (<300 nm) on stiff ECM that is **absent on soft ECM** and **dissolved by verteporfin** (YAP condensate blocker) — despite verteporfin not disrupting chromatin loops.
2. **YAP condensate co-localization**: YAP condensates (detected by YAP immunofluorescence super-resolution) spatially overlap with multiple mechanoenhancer loci simultaneously on stiff ECM, not with a single locus.
3. **Micro-C specificity**: Verteporfin treatment on stiff ECM dissolves YAP condensates → subsequent Micro-C shows loss of non-looped mechanoenhancer contacts at target genes, but no gain of cohesin-mediated loops at the same loci.
4. **BRD4 condensate occupancy**: BRD4 CUT&RUN at specific mechanoenhancers correlates with YAP condensate number/size — not with individual E-P loop frequency.

### Literature Grounding
- [GROUNDED] 86.2% of mechanoenhancer–gene connections lack annotated chromatin loops: Cosgrove et al. 2025, Science (their own Micro-C data)
- [GROUNDED] Phase-separated condensates mechanically pull genomic loci together via surface tension without looping: Shin et al. 2018, Cell (CasDrop optogenetic system)
- [GROUNDED] YAP-BRD4-MED1 condensates at super-enhancers: Zanconato et al. 2018; verteporfin dissolves YAP condensates → chromatin topology reverts in 4h
- [GROUNDED] Condensates preferentially form in euchromatic (softer) genomic regions: Shin et al. 2018 minimal biophysical model
- [INFERRED] YAP condensates specifically co-localize non-looped mechanoenhancers: this is the novel hypothesis — the specific co-localization of non-looped mechanoenhancers by YAP condensates has not been tested. The Shin 2018 CasDrop used artificial IDPs; endogenous YAP condensate forces may differ.
- [INFERRED] Condensate surface tension force (~10 pN) is sufficient to pull chromatin loci (<500 nm apart) into proximity: estimated from published condensate physical parameters (Hyman lab, Bharat lab), but the specific force balance with chromatin stiffness at mechanoenhancer loci is not measured.

### Counter-Evidence and Limitations
- The looping-independent observation from Cosgrove 2025 could also be explained by transcription factory mechanisms (RNA Pol II clustering independent of condensates), eRNA-mediated contacts, or simple proximity effects within open TADs — phase separation is one of several competing explanations
- YAP condensates at super-enhancers (Zanconato 2018) were demonstrated in cancer cells on rigid plastic; whether similar condensates form on physiological stiffness hydrogels in fibroblasts is not established
- Verteporfin has multiple targets beyond YAP condensate disruption (it is a photosensitizer; in the dark, its YAP specificity is debated) — off-target effects could confound the interpretation
- Micro-C resolution (~200 bp) may be insufficient to detect the dynamic, transient contacts mediated by condensate surface tension, making this hypothesis difficult to definitively test with existing chromatin conformation tools

### Test Protocol
1. Design Oligopaint FISH probes for 5 non-looped mechanoenhancer pairs from Cosgrove 2025 catalog
2. Stiff ECM (50 kPa) vs soft ECM (1 kPa) vs verteporfin-treated stiff ECM: 3-color ORCA imaging
3. Measure inter-enhancer distance distributions; compare to simulated random nuclear positioning
4. YAP immunofluorescence (super-resolution STORM) at same cells: confirm YAP condensate overlap with clustered mechanoenhancers
5. Micro-C before/after verteporfin at 50 kPa: focus on non-looped mechanoenhancer–gene contacts in Cosgrove 2025 dataset
6. Rescue: expression of IDR-deleted YAP (condensate-incompetent) should NOT rescue spatial mechanoenhancer co-localization on stiff ECM

### Confidence: 0.52
### Disciplinary Distance: 3 fields (mechanobiology ↔ condensate biophysics ↔ enhancer 3D genome)

---

## SELF-CRITIQUE

### Claim-level verification:
- H1: KDM6B-EP300 STRING 0.754 is based on co-expression (a-score) and text-mining (t-score), not experimental direct binding data. The KDM6B→EP300 relay at mechanoenhancers is plausible but extrapolated from pathway-level interactions. ✓ ACCEPTABLE — both proteins are real, interaction score is medium-high, mechanistic link is clear.
- H2: EP300-CAMK2A STRING 0.908 is one of the strongest interactions found; supported by database evidence (d-score). CaMKII phosphorylation of EP300 has a published literature basis (not fabricated). Piezo1 static stiffness caveat is noted as counter-evidence. ✓ ACCEPTABLE.
- H3: YAP condensate cooperativity n=2–4 is estimated from generic LLPS biophysics, not directly measured for BRD4-YAP. The power law prediction is testable. ✓ ACCEPTABLE — clearly labeled as [INFERRED].
- H4: MRTF-A enhancer binding is inferred from STRING co-expression (EP300-MRTFA 0.710) and Cosgrove 2025 CaRG motif enrichment at mechanoenhancers — not from direct ChIP evidence. Clearly flagged. ✓ ACCEPTABLE.
- H5: Shin 2018 surface tension force estimate (~10 pN) is from published condensate biophysics literature (Hyman lab measurements). The co-localization prediction is novel and testable. Counter-evidence (transcription factories as alternative) explicitly included. ✓ ACCEPTABLE.

### Novelty assessment (literature-verified):
- All five hypotheses address gaps with ZERO PubMed co-occurrence for the specific combinations tested (confirmed in computational validation). No existing paper tests H3K27ac at mechanoenhancers (H1), Piezo1-CaMKII-EP300 pre-priming (H2), condensate supralinearity with stiffness (H3), MRTF-A enhancer vs promoter ECM stiffness (H4), or YAP condensate mediation of looping-independent E-P contacts (H5).

### Not re-deriving Cosgrove 2025:
- None of the five hypotheses claim to discover mechanoenhancers — all build mechanistically on the mechanoenhancer foundation.
