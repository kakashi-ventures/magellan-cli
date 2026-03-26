# Literature Context: Mechanobiology (ECM Mechanics) × Enhancer Epigenomics

**Session**: 2026-03-25-targeted-002
**Generated**: 2026-03-25
**Scout**: Literature Scout v5.2

---

## Recent Breakthroughs in Field A — Mechanobiology (ECM Mechanics)

- **Mechanoenhancers defined genome-wide (Cosgrove et al. 2025, *Science*)**: First systematic mapping of genomic enhancers that respond to ECM stiffness. ATAC-seq + CRISPRi screening in human fibroblasts on soft (1 kPa) vs stiff (50 kPa) hydrogels reveals ~200+ functional mechanoenhancer–gene connections. Stiff ECM activates enhancers with TEAD, AP-1, SP1, SRF/CaRG motifs; soft ECM activates distinct AP-1 and RUNX1/FOXF1/CEBPE enhancers. **Critical finding**: only 13.8% of mechanoenhancer–gene connections involve annotated chromatin loops — the looping-independent regulatory mechanism is entirely unknown. Chromatin accessibility changes within 1 hour of contractile perturbation.

- **Viscoelastic ECM → epigenome remodeling (Zhang et al. 2025, *Nat Commun*)**: Viscoelastic (slow-relaxing) substrates reduce lamin A/C expression, increase nuclear size, decrease chromatin compaction, and increase chromatin accessibility at cis-regulatory elements associated with neuronal and pluripotent genes. Viscoelastic substrates improve fibroblast → neuron and fibroblast → iPSC reprogramming efficiency. Demonstrates ECM mechanical property beyond stiffness (viscoelasticity) drives epigenetic reprogramming.

- **ECM stiffness → 3D genome reorganization (Li et al. 2024, Hi-C in MSCs)**: First comprehensive Hi-C mapping of 3D genome under ECM stiffness. Stiff ECM → more long-range chromatin interactions, compartment B-to-A switching at cytoskeletal genes, TAD merging around osteogenic TFs (SP1, ETS1). Direct causal link: ECM stiffness → TAD restructuring → osteogenic gene co-regulation. TAD-level resolution only; enhancer-promoter loop dynamics unstudied.

- **Matrix stress relaxation controls KDM4B/KDM6B histone demethylases (Tayler et al. 2026)**: ECM stiffness AND stress relaxation profile directly regulate activity of histone demethylases KDM4B (H3K9me3) and KDM6B (H3K27me3). KDM6B demethylates H3K27me3 at gene loci driving osteogenesis — the same mark that must be removed for enhancer activation (H3K27me3 = Polycomb-repressed/poised enhancers). First direct ECM mechanics → specific histone demethylase → specific epigenetic mark chain.

- **Piezo1 → Rho-ROCK → H3K acetylation → epigenetic mechanical memory (Science Advances 2025)**: Compressive mechanical stress → Piezo1 Ca²⁺ influx → Rho-ROCK → H3K acetylation → open chromatin at cancer genes. Critically: cells retain this epigenetic imprint after force removal ("epigenetic mechanical memory"). A parallel study shows Piezo1 → F-actin → YAP nuclear localization, linking Piezo1 to the YAP-enhancer axis.

- **Pulsatile flow → H3K9me3 via lamin (Chen et al. 2025, *PNAS*)**: Shear mechanical stress → chromatin interaction with lamin-associated proteins → enrichment of H3K9me3 (repressive methylation) at lamin-associated heterochromatin. First direct ChIP-seq mapping of a mechanosensitive histone mark. Establishes bidirectional epigenomic response: force opens chromatin at TEAD/YAP targets AND compacts lamin-associated heterochromatin.

---

## Recent Breakthroughs in Field C — Enhancer Epigenomics

- **YAP/TAZ-VGLL3 epigenetically reprograms PPARγ target enhancers (Seol et al. 2026)**: YAP/TAZ and antagonist VGLL3 compete at TEAD-bound PPARγ target enhancers, controlling H3K27me3↔H3K27ac switching and adipocyte fate. Demonstrates YAP/TAZ have direct, named-enhancer-specific epigenetic effects (not just TF binding). YAP/TAZ at enhancers = H3K27me3 maintenance; VGLL3 displacement = H3K27ac activation.

- **YAP/TAZ-BRD4 phase-separated condensates at super-enhancers (Zanconato et al. 2018, *Nat Cancer*, 269 citations)**: YAP/TAZ recruit BRD4, MED1, CDK9 into liquid-like phase-separated condensates at super-enhancer loci. This transcriptional addiction mechanism concentrates the full transcriptional machinery at H3K27ac-marked super-enhancers. BRD4 reads H3K27ac → recruits YAP complex → condensate forms. Condensate dissolution (verteporfin, 4h) reverses chromatin topological changes.

- **Phase-separated condensates mechanically sense chromatin stiffness (Shin et al. 2018, *Cell*)**: Nuclear condensates preferentially nucleate in euchromatic (softer) genomic regions via lower mechanical energy cost. Condensates mechanically exclude denser heterochromatin. Can physically pull targeted genomic loci together via surface tension (without chromatin looping). Condensates function as "mechano-active chromatin filters" — creates looping-independent regulatory contacts.

- **Single-cell Micro-C identifies promoter-multi-enhancer hubs (*Nat Genetics* 2025)**: scMicro-C resolves "promoter stripes" — single promoters contacting multiple downstream enhancers simultaneously. Relevant: mechanoenhancers may form multi-enhancer hubs that collectively drive target genes, explaining why individual E-P loops are weak/absent.

- **YAP/TAZ genome-wide enhancer binding: >90% of targets are distal enhancers (Piccolo lab, Nat Cell Biol 2015, ENCODE data)**: Well-established baseline. YAP/TAZ-TEAD co-occupy composite TEAD + AP-1 motif elements at distal enhancers marked by H3K27ac. AP-1 is essential co-factor at YAP/TAZ enhancers.

- **pH-responsive transcriptional condensates dissolve at acidic pH (*Cell* 2025)**: Acidic microenvironment dissolves BRD4/MED1 condensates at inflammatory enhancers. Demonstrates condensates are regulated by physical/chemical microenvironment — not just protein concentration. First example of environmental physical property (pH) directly dissolving transcriptional condensates at specific enhancers.

---

## Existing Cross-Field Work

### WELL-ESTABLISHED connections:

1. **YAP/TAZ: ECM stiffness sensor → enhancer-binding transcription factor**: The full chain ECM stiffness → Hippo pathway → YAP/TAZ nuclear translocation → TEAD binding at distal enhancers is established. The mechanobiology field established the stiffness-YAP link; the epigenomics field established YAP-TEAD enhancer binding. Their combination is implicit but the stiffness-specific genome-wide enhancer binding landscape has NOT been mapped (existing YAP ChIP-seq mostly from cancer cells on rigid plastic).

2. **SRF/CaRG: actin-MRTF mechanosensor → CaRG-box elements at mechanoenhancers**: MRTF nuclear translocation is actin polymerization-dependent (ECM stiffness drives F-actin), and SRF/CaRG motifs are enriched at stiff-ECM mechanoenhancers (Cosgrove 2025). However, MRTF ChIP-seq under mechanical force conditions has not been performed.

3. **ECM stiffness → general chromatin accessibility (ATAC-seq)**: Well-established by Cosgrove 2025 and NAR Cancer 2025 prostate paper. Stiffness changes drive global chromatin accessibility differences detectable by ATAC-seq.

4. **Nuclear mechanics (lamin/LINC complex) → chromatin organization**: Lamin A/C governs nuclear stiffness and chromatin interaction with nuclear lamina. LINC complex (nesprin/SUN) transmits cytoskeletal forces to nucleus. Mutations in laminopathies cause chromatin disorganization.

### NEWLY ESTABLISHED connections (2024-2026):

5. **Mechanoenhancers as a functional class** (Cosgrove 2025): ECM stiffness-specific enhancers with functional gene connections established genome-wide. **Implication for Generator**: mechanoenhancers exist; now explain their mechanisms.

6. **ECM stiffness → 3D genome compartments/TADs** (Li 2024 Hi-C): TAD merging and compartment switching with ECM stiffness shown in MSCs. Demonstrates 3D architectural response to mechanical signals.

7. **ECM viscoelasticity → cis-regulatory element accessibility** (Zhang 2025): Viscoelastic property (beyond stiffness) drives epigenomic changes specifically at cis-regulatory loci.

8. **ECM mechanics → KDM histone demethylase activity** (Tayler 2026, Yu 2025): Direct mechanical signal → epigenetic enzyme → histone mark change.

9. **YAP/TAZ direct epigenetic effects at specific named enhancers** (Seol 2026): YAP/TAZ control H3K27me3/H3K27ac balance at PPARγ enhancers.

### NOT YET ESTABLISHED:
- H3K27ac/H3K4me1 ChIP-seq specifically at mechanoenhancers under ECM stiffness gradients
- Enhancer-promoter loop dynamics at mechanoenhancer resolution (Hi-C/Micro-C)
- Phase-separated YAP-BRD4 condensates forming as function of ECM stiffness at specific mechanoenhancers
- MRTF-SRF genome-wide enhancer binding under mechanical force
- Piezo1 → HAT (p300/CBP) → H3K27ac at enhancers circuit
- Nuclear deformation magnitude → specific E-P loop restructuring
- Mechanoepigenetic code across fiber architecture (stiffness + viscoelasticity + anisotropy)

---

## Key Anomalies

1. **86.2% of mechanoenhancer–gene connections lack annotated chromatin loops (Cosgrove 2025)**: The dominant regulatory mechanism at mechanoenhancers is NOT canonical enhancer-promoter looping. This is a fundamental gap — how do ~200 identified mechanoenhancers communicate with target genes without physical loops? Possible mechanisms: phase-separated hub contacts (Shin 2018 + Zanconato 2018), RNA-mediated (eRNA tracking), direct TF scanning, or tracking/transcription factory mechanisms.

2. **Opposing mechanical signals from stiffness vs viscoelasticity on lamin A/C**: Stiff ELASTIC ECM → high lamin A/C (classic mechanobiology dogma). But slow-relaxing VISCOELASTIC ECM → reduced lamin A/C (Zhang 2025). This means nuclear stiffness and chromatin organization respond differently to these two orthogonal mechanical parameters. The epigenomic consequences of this bifurcation are unstudied.

3. **Soft ECM opens more chromatin globally (prostate cancer) vs stiff ECM activates mechanoenhancers (Cosgrove 2025)**: Paradox: soft ECM = global chromatin opening, stiff ECM = specific mechanoenhancer activation. Resolution: global accessibility ≠ targeted enhancer activation. Soft ECM may create a permissive but unfocused chromatin landscape; stiff ECM focuses activation at specific TEAD/AP-1 mechanoenhancers via YAP/TAZ nuclear recruitment.

4. **Bimodal epigenomic response to mechanical force**: Mechanical force simultaneously opens chromatin at TEAD/YAP targets (active enhancers) AND compacts chromatin at lamin-associated heterochromatin (H3K9me3, Chen 2025 PNAS). The same mechanical input creates opposing epigenomic outcomes at different genomic locations — suggesting a mechanical "sorting" of the epigenome.

---

## Contradictions Found

1. **Soft ECM = more H3K27ac at promoters (NAR Cancer 2025)** vs **Stiff ECM = mechanoenhancer activation (Cosgrove 2025)**: Cell-type-dependent (prostate cancer vs fibroblasts); promoter vs enhancer distinction; not truly contradictory but apparently paradoxical. Suggests stiffness effects on epigenome are highly context-dependent.

2. **Phase-separated condensates prefer euchromatin (soft; Shin 2018)** vs **YAP-BRD4 condensates at super-enhancers on rigid plastic (Zanconato 2018)**: Apparent contradiction. Resolution: YAP/TAZ nuclear localization is driven by stiff ECM → once nuclear, YAP seeks euchromatic super-enhancer loci (which are soft relative to heterochromatin) to nucleate condensates. Both observations can be simultaneously true.

---

## Full-Text Papers Retrieved

| File | Paper | Why Selected |
|------|-------|--------------|
| `cosgrove2025-mechanoenhancers-ecm-stiffness.md` | Cosgrove et al. 2025, *Science* | LANDMARK: First genome-wide mechanoenhancer mapping |
| `zhang2025-viscoelastic-ecm-epigenome.md` | Zhang et al. 2025, *Nat Commun* | ECM viscoelasticity → cis-regulatory element accessibility |
| `li2024-ecm-stiffness-3d-genome-msc.md` | Li et al. 2024 | Hi-C: ECM stiffness → 3D genome TAD reorganization |
| `zanconato2018-yaptaz-brd4-superenhancer.md` | Zanconato et al. 2018, *Nat Cancer* | YAP/TAZ-BRD4 condensates at super-enhancers (foundational) |
| `shin2018-nuclear-condensates-chromatin-mechanics.md` | Shin et al. 2018, *Cell* | Condensates mechanically sense and restructure chromatin |
| `chen2025-pulsatile-flow-h3k9-lamin.md` | Chen et al. 2025, *PNAS* | First mechanosensitive histone mark (H3K9me3) ChIP-seq |
| `tayler2026-matrix-stiffness-kdm4b-kdm6b.md` | Tayler et al. 2026 | ECM mechanics → KDM histone demethylase activity |
| `hsia2023-epigenome-mechanobiology-review.md` | Hsia et al. 2023, *J Mol Biol* | Comprehensive review, establishes framework |
| `seol2026-yaptaz-vgll3-pparg-enhancers.md` | Seol et al. 2026 | YAP/TAZ direct epigenetic effects at named enhancers |
| `piezo1-compressive-stress-epigenetic-memory.md` | Sci Adv 2025 | Piezo1 → H3K acetylation → epigenetic mechanical memory |

---

## Disjointness Assessment

- **Status: PARTIALLY EXPLORED** (newly opened, 2024–2026)
- **Evidence**: One landmark paper (Cosgrove 2025, *Science*) defines mechanoenhancers genome-wide. ECM stiffness → 3D genome shown (Li 2024). ECM viscoelasticity → cis-regulatory accessibility shown (Zhang 2025). YAP/TAZ enhancer binding well-established (multiple papers, mostly oncology). Histone demethylase control by ECM mechanics shown (Tayler 2026).
- **Implication for Generator**: DO NOT re-derive mechanoenhancer existence (Cosgrove 2025 established this). Focus on unresolved mechanisms: (1) H3K27ac/H3K4me1 marking of mechanoenhancers, (2) phase-separated condensate assembly as ECM stiffness function at mechanoenhancers, (3) MRTF enhancer binding, (4) E-P loop formation at mechanoenhancers, (5) Piezo1→HAT→H3K27ac circuit. These are genuinely open.

---

## Gap Analysis

### What has been explored:
- Mechanoenhancers genome-wide — ATAC-seq chromatin accessibility (Cosgrove 2025)
- ECM stiffness → 3D genome at TAD/compartment level — Hi-C (Li 2024)
- ECM viscoelasticity → cis-regulatory element accessibility — ATAC-seq (Zhang 2025)
- YAP/TAZ genome-wide binding at TEAD-occupied distal enhancers — ChIP-seq (multiple, oncology)
- YAP/TAZ-BRD4 phase-separated condensates at super-enhancers — imaging (Zanconato 2018)
- Phase-separated condensates mechanically sensing chromatin stiffness — optogenetics (Shin 2018)
- ECM mechanics → KDM histone demethylase activity — biochemistry (Tayler 2026)
- Shear force → H3K9me3 at lamin-associated heterochromatin — ChIP-seq (Chen 2025)
- YAP/TAZ direct effects on specific named enhancers — ChIP + histone marks (Seol 2026)
- Piezo1 → H3K acetylation → epigenetic mechanical memory — immunofluorescence (Sci Adv 2025)

### What has NOT been explored (specific gaps):

**GAP 1 (HIGH PRIORITY)**: H3K27ac and H3K4me1 ChIP-seq at mechanoenhancers under ECM stiffness gradients
- Cosgrove 2025 used ATAC-seq (accessibility proxy); canonical enhancer marks at mechanoenhancers never mapped
- Critical experiment: ChIP-seq H3K27ac + H3K4me1 in cells on soft/stiff hydrogels → maps active vs poised mechanoenhancers
- Hypothesis: stiff ECM → YAP-p300 recruitment → H3K27ac at stiff-ECM mechanoenhancers; soft ECM → H3K27me3 (Polycomb) deposition at those same loci

**GAP 2 (HIGH PRIORITY)**: ECM stiffness → enhancer-promoter loop formation/disruption (Hi-C/Micro-C at E-P resolution)
- Li 2024 Hi-C: TAD-level only. Cosgrove 2025: only 13.8% of E-P connections have annotated loops (Micro-C)
- Experiment needed: high-resolution Micro-C on soft vs stiff hydrogels at specific mechanoenhancer loci
- Hypothesis: ECM stiffness drives YAP-mediated phase-separated hub formation that contacts multiple mechanoenhancers simultaneously without forming canonical CTCF/cohesin loops

**GAP 3 (HIGH PRIORITY)**: ECM stiffness-dependent formation/dissolution of YAP-BRD4 condensates at specific mechanoenhancers
- YAP-BRD4 condensates known from cancer cells on rigid plastic (Zanconato 2018)
- Nobody has varied ECM stiffness and measured condensate number/size at specific mechanoenhancer loci
- Experiment: super-resolution imaging (PALM/STORM) of YAP-BRD4 condensates + CUT&RUN for BRD4 at mechanoenhancers on hydrogels
- Hypothesis: ECM stiffness gradient → proportional YAP nuclear concentration → proportional BRD4-MED1 condensate assembly at mechanoenhancers → analog mechanical encoding of transcriptional output

**GAP 4 (MODERATE)**: Genome-wide MRTF-SRF binding at enhancers vs promoters under ECM mechanical force
- MRTF nuclear translocation is stiffness-dependent (via actin polymerization)
- SRF/CaRG motifs found at MYH9 mechanoenhancer (Cosgrove 2025)
- Experiment: MRTF ChIP-seq on soft vs stiff hydrogels → annotate binding to promoters vs enhancers
- Hypothesis: MRTF preferentially binds mechanoenhancers (vs promoters) on stiff ECM, driven by nuclear actin pool availability

**GAP 5 (MODERATE)**: Piezo1 → p300/CBP HAT → H3K27ac at mechanoenhancers circuit
- Piezo1 → Rho-ROCK → H3K acetylation shown (bulk, Sci Adv 2025)
- Specific HAT (p300/CBP) involved not identified; enhancer-specific deposition not shown
- Hypothesis: Piezo1 Ca²⁺ → CaM-CAMKII → p300 HAT activation → H3K27ac at stiff-ECM mechanoenhancers within 15 minutes of force application (faster than YAP nuclear translocation: mechanism for rapid pre-priming of mechanoenhancers)

**GAP 6 (MODERATE)**: Nuclear deformation magnitude → specific E-P loop restructuring at mechanoenhancers
- Nuclear confinement/deformation changes chromatin organization generally
- Specific mechanoenhancer E-P loop dynamics as function of nuclear strain never quantified
- Hypothesis: threshold nuclear strain (determined by lamin A/C level) irreversibly switches mechanoenhancer chromatin loop structure, encoding mechanical memory

**GAP 7 (EMERGING)**: Mechanoepigenetic code — does ECM fiber architecture (anisotropy, crosslinking) beyond stiffness magnitude drive distinct enhancer programs?
- All mechanoenhancer studies use isotropic hydrogels (stiffness only)
- Fibrous ECM (collagen, fibronectin) has anisotropy, fiber alignment
- Hypothesis: ECM fiber alignment drives distinct integrin clustering patterns → distinct focal adhesion signaling → distinct mechanoenhancer programs not captured by stiffness-only studies

### Most promising unexplored directions (Generator priority):

1. **YAP-BRD4 condensate size as mechanical rheostat at mechanoenhancers**: ECM stiffness → YAP nuclear concentration → condensate assembly → super-enhancer-like transcriptional amplification proportional to mechanical input. Testable, falsifiable, mechanistically grounded.

2. **Mechanoepigenetic histone code at mechanoenhancers (H3K27ac dynamics)**: Time-resolved ChIP-seq after ECM stiffness change. Does H3K27ac appear at mechanoenhancers within 1h (matching ATAC-seq kinetics)? Is this via p300 (YAP-recruited) or KDM6B (H3K27me3 erasure)?

3. **Looping-independent multi-enhancer hubs via phase separation**: 86.2% of mechanoenhancer connections lack loops. Phase-separated YAP hubs (Shin 2018 mechanics + Zanconato 2018 YAP condensates) could co-localize multiple non-looped mechanoenhancers in nuclear space → collective transcriptional regulation without individual E-P loops.

4. **Piezo1 → p300 pre-priming circuit**: Rapid (<15 min) mechanosensitive H3K27ac deposition at mechanoenhancers by Piezo1-CaM-p300 before YAP nuclear entry (~30-60 min lag), establishing a two-phase mechanoenhancer activation model.
