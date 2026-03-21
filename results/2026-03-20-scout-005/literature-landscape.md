# Literature Landscape — Session 2026-03-20-scout-005

## Executive Summary

Literature retrieval across 6 domains and 3 target pairs reveals:
- **Target 1** (Cristae × Lyotropic LC): PARTIALLY CONNECTED — shared conceptual substrate through cardiolipin polymorphism and non-bilayer phases, but no paper explicitly frames cristae remodeling as lyotropic LC phase transitions. Strong bridge opportunity.
- **Target 2** (Acoustic mechanotransduction × Topological phononics): WEAKLY CONNECTED — the 2025 Nature Materials "Topological acoustofluidics" paper bridges topology and bioparticle manipulation, but cellular-scale phononic bandgap engineering for mechanotransduction remains unexplored.
- **Target 3** (Ferroptosis × Serpentinization): DISJOINT — zero cross-citations found. Shared Fe(II)/Fe(III) Fenton cycling chemistry is well-characterized independently in each field but never compared.

---

## Target 1: Mitochondrial Cristae Remodeling × Lyotropic Liquid Crystal Phase Transitions

### Domain A: Cristae Remodeling — Recent Breakthroughs

**Yu et al. (2025)** provide the most comprehensive review to date of cristae dynamics (DOI: 10.1016/j.cellin.2025.100285). Key regulators: OPA1 proteolytic processing, MICOS complex scaffolding at crista junctions, F1Fo-ATP synthase dimerization creating high-curvature ridges, and **cardiolipin** stabilizing inner-membrane architecture. Cristae remodel number, length, width, curvature/stiffness, and junction geometry in response to physiological and stress cues.

**Golla, Boyd & May (2024)** used coarse-grained MD to show cardiolipin preferentially partitions to regions of **negative mean curvature** in cristae-scale geometries (DOI: 10.1038/s42003-023-05657-6). Partitioning dominated by mean curvature; **weaker Gaussian curvature correlation** — a critical finding for the bridge concept.

**Venkatraman, Lee & Budin (2024)** reviewed lipid biophysics in mitochondrial form/function (DOI: 10.1016/j.jlr.2024.100643), emphasizing the intrinsic curvature of the bulk phospholipid pool and the nuances of cardiolipin. They highlight emerging questions about ether lipids and sterols.

**Cardiolipin remodeling in saturated lipidomes (2024)**: Loss of CL remodeling in microaerobic yeast causes **characteristic loss of cristae membranes**, showing CL's structural role is lipid-environment dependent (PMID: 39038656).

**Integrative modelling of mitochondrial cristae (2025)**: New computational framework quantifying mean and Gaussian curvature distributions across cristae (DOI: 10.1038/s42003-025-08381-5).

### Domain C: Lyotropic Liquid Crystal Phase Transitions

**Light-driven hexagonal-to-cubic phase switching (2024)**: JACS demonstrated photo-switchable LLC transitions in arylazopyrazole systems (DOI: 10.1021/jacs.4c02709) — showing phase transitions can be controlled by external stimuli.

**Millisecond phase transition kinetics in cubosomes/hexosomes (2025)**: Nanosecond IR laser T-jump with time-resolved SAXS reveals H_II ↔ cubic transition dynamics on millisecond timescales (PMID: 40293325).

**Lipid nanoparticle phase behavior (2024)**: PNAS showed lipid shape/packing parameter determines H_II vs. cubic phase, with direct implications for mRNA delivery (DOI: 10.1073/pnas.2311700120).

**LLC nanoparticles for drug delivery (2025)**: Frontiers review covers stimuli-responsive LLC phase transitions (DOI: 10.3389/frsfm.2025.1658466).

### Bridge Analysis: Gaussian Curvature Elasticity & Cardiolipin Packing Parameter

**The conceptual bridge is strong but unexploited:**

Cardiolipin is a well-known **cone-shaped lipid** (packing parameter > 1) that promotes the inverted hexagonal (H_II) phase in the presence of divalent cations. This is textbook lipid polymorphism. However:

1. **No paper frames cristae remodeling as a lyotropic LC phase transition.** The cristae literature treats curvature as a protein-driven process (OPA1, MICOS, ATP synthase), while the LLC literature treats phase transitions as thermodynamic phenomena in model systems.

2. **Cubic membranes in mitochondria** have been reported in stressed/virally infected cells (Chaos amoeba starvation), but these are treated as pathological curiosities rather than as evidence of LLC phase behavior in vivo.

3. **Golla et al. (2024)** found Gaussian curvature has a weaker effect on lipid partitioning than mean curvature — but the Gaussian curvature modulus (κ̄) is precisely what determines lamellar → H_II → cubic transitions in LLC theory. This disconnect between the biophysics and materials science literatures is the hypothesis-generating gap.

4. **Basu Ball (2018)** explicitly describes cardiolipin's role in nonbilayer phase formation but does not connect this to cristae remodeling dynamics or LLC phase diagrams.

### Disjointness Verification: PARTIALLY CONNECTED
- Shared concepts: cardiolipin, membrane curvature, non-bilayer phases
- Gap: No paper applies LLC phase diagram formalism (Helfrich bending energy, Gaussian curvature modulus, packing parameter) to predict cristae remodeling transitions
- Cross-citation estimate: ~5-10 papers discuss cubic membranes in mitochondria, but none use LLC phase transition theory to predict or explain cristae morphology changes

---

## Target 2: Acoustic Mechanotransduction × Topological Phononics

### Domain A: Acoustic Mechanotransduction — Recent Breakthroughs

**He et al. (2025)** published a comprehensive review in Science Advances (DOI: 10.1126/sciadv.adu4759) covering acoustic orchestration of cellular functions: stem cell differentiation, immune cell activation, neural modulation. Covers ultrasound, surface acoustic waves, and bulk acoustic waves.

**Hahmann et al. (2024)** reviewed sonogenetics in Angewandte Chemie (DOI: 10.1002/anie.202317112, 32 citations): mechanosensitive ion channels as sonogenetic mediators, ultrasound reaching tens of cm depth with high spatiotemporal precision.

**Yang et al. (2026)** demonstrated precision acoustofluidics for high-throughput mechanobiology in suspension cells — directly applying acoustic forces to study cellular mechanotransduction.

**Sonomechanobiology review (2023)**: Audible acoustic waves and low-vibration stimulation affect cellular growth, differentiation, and migration through ion channels, primary cilia, and cytoskeletal networks.

**Key finding**: Acoustic mechanotransduction research uses bulk acoustic waves or surface acoustic waves, but does NOT engineer phononic bandgaps to control which frequencies reach cells.

### Domain C: Topological Phononics — Recent Breakthroughs

**Zhao et al. (2025)** — "Topological acoustofluidics" in **Nature Materials** (DOI: 10.1038/s41563-025-02169-y, 28 citations). **LANDMARK.** Valley-Hall topological acoustofluidic chips creating valley streaming vortices, chiral swirling patterns, and nanoscale topological pressure wells for DNA manipulation. 93.2% bandwidth modulation of edge states.

**Huang et al. (2026)** demonstrated topological acoustic tweezing in Science Advances (DOI: 10.1126/sciadv.adz4301): topological interfaces create confined standing-wave fields for robust particle transport.

**The 2024 Phononic Crystals Roadmap (2025)**: 40+ experts covering topological, non-Hermitian, active, chiral phononic crystals. Applications expanding to biosensing, acoustic tweezers.

**Reversible tunable topological phononic crystals (2025)**: Thermosensitive hydrogels for reconfigurable edge states (DOI: 10.1038/s41378-025-01121-z).

**Phononic crystal biosensor (2025)**: Coupling topological edge state with defect modes for biosensing (DOI: 10.1038/s41598-025-85195-9).

### Bridge Analysis: Phononic Bandgap Engineering at Cellular Scales

**The bridge is emerging but underdeveloped:**

1. **Zhao et al. (2025)** explicitly state their work reveals "potential for topological-material applications in life sciences" — they manipulate DNA using topological pressure wells. But they do NOT engineer bandgaps to selectively filter acoustic frequencies for mechanotransduction.

2. **No paper designs phononic structures to create frequency-selective acoustic environments for cells.** Mechanotransduction studies use broadband ultrasound; phononic crystal studies optimize for materials applications. The gap is applying topological bandgap engineering to create **frequency-selective mechanotransduction**.

3. **Topologically protected edge modes** could deliver acoustic energy to specific cell populations along interfaces while being immune to scattering from tissue heterogeneity — a concept with no existing literature.

4. **Scale matching**: Phononic bandgaps at cellular scales (~10-100 μm) correspond to MHz frequencies, matching therapeutic ultrasound ranges. This is physically feasible but unaddressed.

### Disjointness Verification: WEAKLY CONNECTED
- Zhao et al. (2025) bridges acoustic manipulation + topology, but for particle transport, not mechanotransduction
- No paper applies phononic bandgap engineering specifically for cellular mechanotransduction
- Cross-citation estimate: ~3-5 papers at the acoustic manipulation/topology interface; 0 for topology/mechanotransduction

---

## Target 3: Ferroptosis × Serpentinization Geochemistry

### Domain A: Ferroptosis — Recent Breakthroughs

**Sun et al. (2025)** provide a comprehensive review of lipid metabolism in ferroptosis (DOI: 10.3389/fimmu.2025.1545339, 34 citations). Fenton reaction (Fe²⁺ + H₂O₂ → Fe³⁺ + •OH + OH⁻) initiates the chain: hydroxyl radical abstracts bis-allylic H from PUFA-phospholipids → phospholipid radical → phospholipid peroxyl radical → **phospholipid hydroperoxide (PLOOH)** formation. GPX4 is the master regulator.

**Balakrishnan & Kenworthy (2024)** — JACS landmark (DOI: 10.1021/jacs.3c10132): Fenton-induced lipid peroxidation **dramatically enhances membrane phase separation**, accumulates peroxidized lipids in disordered phase, disrupts raft protein partitioning. Suggests "disruptions of membrane phase behavior may play a previously unrecognized role in ferroptosis."

**Lotfipour Nasudivar et al. (2024)** — Langmuir (DOI: 10.1021/acs.langmuir.4c03294, 15 citations): Iron-mediated Fenton reactions alter membrane lateral organization, reduce line tension at Lo/Ld boundaries, decrease membrane integrity through LOOH → truncated oxidized phospholipids.

**"Ferroptosis: when metabolism meets cell death" (2024)**: Physiological Reviews (DOI: 10.1152/physrev.00031.2024). Major review linking ferroptosis to metabolism.

**Membrane dynamics in ferroptosis**: Ferroptotic cells show **smaller mitochondria with reduced or vanished cristae**, increased membrane density. Lipid peroxidation modulates membrane curvature.

**Key ferroptosis chemistry**: Fe²⁺/Fe³⁺ cycling is essential. Fe²⁺ decomposes LOOH → alkoxyl radicals (LO•) → propagation. Fe³⁺ decomposes LOOH → peroxyl radicals (LOO•). Optimal peroxidation at Fe²⁺/Fe³⁺ ratio ≈ 1.

### Domain C: Serpentinization Geochemistry — Recent Breakthroughs

**Ross et al. (2025)** — GRL (DOI: 10.1029/2024GL114016): Serpentinization under flow conditions generates ≥76-89 mol% H₂. Olivine remains reactive despite serpentine precipitation. Important for understanding sustained Fe²⁺ oxidation.

**Natural Hydrogen Quantification (2025)**: Empirical models predicting H₂ generation rates. Giles Complex (Australia) potential: ~2.24 × 10¹³ kg H₂ from partial serpentinization (DOI: 10.3390/geosciences15030112).

**Martin et al. (2023)**: Comprehensive Frontiers review (DOI: 10.3389/fmicb.2023.1257597). Core process: Fe²⁺ in olivine/pyroxene oxidized by water → magnetite (Fe₃O₄) + H₂. Vent fluid pH 9-11. Greigite, magnetite, awaruite catalyze CO₂ fixation → formate (200 mM), acetate (100 μM), pyruvate (10 μM).

**Metabolic Origin of Life (2024)**: Accounts of Chemical Research (DOI: 10.1021/acs.accounts.4c00423). Pinpoints conditions for iron-mineral-catalyzed prebiotic synthesis.

**ROS-driven Fenton chemistry delocalized from vents (2023)**: Nature Communications (DOI: 10.1038/s41467-023-39917-0). Fe²⁺/Fe³⁺ cycling with H₂O₂ generates •OH across Earth's humid realm, not just at serpentinization sites.

**Key serpentinization chemistry**:
- 3Fe₂SiO₄ + 2H₂O → 2Fe₃O₄ + 3SiO₂ + 2H₂ (fayalite serpentinization)
- Fe²⁺ → Fe³⁺ is the electron source for H₂ production
- Iron cycles between Fe²⁺ (olivine) → Fe³⁺ (magnetite) with water as oxidant

### Bridge Analysis: Fe(II)/Fe(III) Fenton Cycling Kinetics & PLOOH Intermediates

**The bridge is chemically precise and completely unexploited:**

1. **Identical core chemistry**: Both ferroptosis and serpentinization are fundamentally driven by Fe²⁺/Fe³⁺ redox cycling. In ferroptosis: Fe²⁺ + H₂O₂ → Fe³⁺ + •OH; in serpentinization: Fe²⁺(silicate) + H₂O → Fe³⁺(magnetite) + H₂. The Fenton reaction is the kinetic bridge.

2. **Phospholipid hydroperoxides (PLOOH)**: The death-executing molecules of ferroptosis. In serpentinization environments, abiotic fatty acid synthesis occurs (documented). If primitive membrane vesicles contained these fatty acids, the same Fe²⁺/Fe³⁺ cycling that generates H₂ would also generate PLOOH — creating a primordial "ferroptosis-like" membrane destruction mechanism.

3. **No paper connects ferroptosis to prebiotic/geochemical iron cycling.** The ferroptosis literature treats iron as a cellular toxin; the serpentinization literature treats it as an energy source. Neither community recognizes the shared Fenton kinetics.

4. **pH parallel**: Serpentinization vents are pH 9-11; ferroptosis is pH-sensitive through GSH/GPX4 system. Alkaline conditions in serpentinization would modulate Fenton kinetics differently than cellular pH ~7.4.

5. **Evolutionary implication**: If the same Fe²⁺/Fe³⁺ cycling that powered early metabolism also destroyed primitive membranes via PLOOH, then GPX4-like peroxidase defenses may have evolved as one of the earliest survival mechanisms — predating even the need for metabolic enzymes.

### Disjointness Verification: DISJOINT
- Cross-citation: **0 papers found** connecting ferroptosis and serpentinization
- Separate searches for "ferroptosis serpentinization" returned results from each field independently
- The shared chemistry (Fenton reaction, iron redox) is well-characterized in BOTH fields but never compared across fields
- **This is the highest-novelty target**

---

## Cross-Domain Implications Summary

| Target | Disjointness | Bridge Strength | Novelty Potential |
|--------|-------------|-----------------|-------------------|
| 1. Cristae × Lyotropic LC | PARTIALLY CONNECTED | Strong conceptual (cardiolipin packing, Gaussian curvature) | HIGH — LLC phase diagram formalism never applied to cristae |
| 2. Acoustic × Topological phononics | WEAKLY CONNECTED | Emerging (Zhao 2025 paper) | HIGH — frequency-selective mechanotransduction unexplored |
| 3. Ferroptosis × Serpentinization | DISJOINT | Very strong chemical (Fenton kinetics, PLOOH) | VERY HIGH — zero cross-field recognition |

---

## Retrieval Quality Self-Check

- **Semantic Scholar**: Rate-limited, obtained ~25 papers with full metadata. Key papers in cristae remodeling, ferroptosis lipid metabolism, topological acoustofluidics retrieved successfully.
- **WebSearch**: Filled gaps effectively for lyotropic LC, serpentinization, and phononic crystals. Found the key Nature Materials 2025 paper.
- **Disjointness checks**: Performed explicit cross-field searches for all 3 pairs. Target 3 confirmed maximally disjoint.
- **Limitation**: Could not retrieve all planned Semantic Scholar queries due to rate limiting. Compensated with WebSearch.
- **Citation counts**: Verified for key papers via Semantic Scholar metadata.
