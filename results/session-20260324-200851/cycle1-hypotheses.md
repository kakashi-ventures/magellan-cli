# Cycle 1 Hypotheses — Session session-20260324-200851
## Target: Cryo-EM heterogeneity analysis x OMV cargo sorting
## Field A: Cryo-EM single-particle analysis and heterogeneity methods (3DVA, cryoDRGN, subtomogram averaging)
## Field C: Bacterial outer membrane vesicle (OMV) cargo sorting mechanism

---

## H1: Cryo-EM 3D Classification of P. aeruginosa OMV Populations Reveals Discrete Cargo-Defined Subclasses

**Mechanism**: P. aeruginosa produces OMVs with heterogeneous protein cargo (virulence factors, enzymes, lipoproteins). Apply RELION 3D classification to cryo-EM images of purified OMVs to computationally sort individual OMV particles into structurally distinct subclasses defined by their surface protein density, diameter distribution, and outer membrane protein (OMP) composition. The hypothesis predicts that OMVs cluster into >=3 discrete structural classes (rather than a continuous distribution) corresponding to distinct biogenesis pathways: (1) spontaneous bulging from regions of reduced OmpA cross-linking (small, OmpA-depleted), (2) explosive cell lysis-derived membrane fragments (large, heterogeneous), and (3) actively budded vesicles enriched in specific virulence factors at polar sites.

**Specific prediction**: RELION 3D classification of >50,000 P. aeruginosa OMV particles at 15-20 Angstrom resolution will resolve >=3 structurally distinct classes with <20% overlap in class assignment probability, each showing statistically different mean diameter (p<0.01), surface protein density, and membrane curvature distribution.

**Bridge**: RELION 3D classification (standard tool in structural biology for heterogeneous protein complexes) has never been applied to classify vesicle populations. [GROUNDED: RELION 3D classification established — Scheres 2012 J Struct Biol]

**Counter-evidence**: OMV heterogeneity may be continuous (Gaussian distribution in size/composition) rather than discrete, which would make 3D classification produce arbitrary clusters. Furthermore, sample preparation artifacts (aggregation, fragmentation during ultracentrifugation) could introduce artificial heterogeneity that obscures biological classes.

**Test protocol**: (1) Grow PAO1 in planktonic culture. (2) Purify OMVs by SEC to minimize aggregation. (3) Prepare cryo-EM grids at multiple concentrations. (4) Collect >50,000 particle images on Titan Krios. (5) Apply RELION 3D classification with 3, 4, 5, and 6 classes. (6) Validate classes by cross-validation (split dataset into halves, classify independently, measure concordance). (7) Correlate classes with proteomics of density-gradient-separated OMV fractions.

**Confidence**: 6/10 — RELION is proven technology but OMV heterogeneity may not be resolvable as discrete classes at 15-20 A resolution.
**Groundedness**: 7/10 — All technical components verified. The key uncertainty is whether biological heterogeneity maps to structurally resolvable classes.
**Novelty**: 9/10 — No published application of cryo-EM 3D classification to vesicle population heterogeneity.

---

## H2: Subtomogram Averaging of OMV Budding Sites Reveals a Conserved Protein Architecture at the Point of Membrane Scission

**Mechanism**: OMV biogenesis requires localized outer membrane curvature and scission without the ESCRT machinery used by eukaryotic cells. The mechanism of scission is unknown. Perform in situ cryo-electron tomography (cryo-ET) of P. aeruginosa cells at the stage of active OMV budding (induced by stress conditions: sub-MIC gentamicin). Apply subtomogram averaging to aligned budding site structures to resolve the protein architecture at the scission neck. The hypothesis predicts that a conserved proteinaceous collar is present at the budding neck, analogous to dynamin in eukaryotic endocytosis, and that this collar will show characteristic dimensions (diameter, periodicity) identifiable by subtomogram averaging.

**Specific prediction**: Subtomogram averaging of >=100 OMV budding intermediates from cryo-ET of sub-MIC gentamicin-stressed P. aeruginosa will reveal a ring-like protein density at the budding neck with 2-5 nm resolution, showing 5-10 nm periodicity and a constriction diameter of 15-25 nm. If no conserved structure exists, subtomogram averaging will produce featureless averaged density (null result distinguishable from positive).

**Bridge**: Subtomogram averaging has resolved bacterial molecular machines in situ (flagellar motor — Yonekura et al. 2003, T6SS — Basler et al. 2012, type IV pilus — Chang et al. 2016) but has NEVER been applied to OMV budding sites. [GROUNDED: Subtomogram averaging methodology well-established for bacterial in situ structures]

**Counter-evidence**: OMV budding may not involve a conserved protein collar — budding could be driven purely by lipid asymmetry (LPS accumulation in the outer leaflet) and peptidoglycan weakening, producing no resolvable protein structure at the scission site. Additionally, budding events may be rare in single tomograms, limiting the number of subtomograms available for averaging.

**Test protocol**: (1) Grow PAO1 with sub-MIC gentamicin (known to increase OMV production 5-10x). (2) Vitrify by plunge-freezing for cryo-ET. (3) Collect tilt series on 300 kV Titan Krios with Falcon 4/K3 detector. (4) Reconstruct tomograms with IMOD or AreTomo2. (5) Identify budding sites manually or with neural network particle picking. (6) Extract and align subtomograms. (7) Average with EMAN2 or RELION. (8) Assess resolution by gold-standard FSC. (9) Dock known OMP structures into averaged map to identify components.

**Confidence**: 5/10 — High technical difficulty. Success depends on (a) frequency of observable budding events, (b) existence of a conserved structure, and (c) resolution achievable with ~100 subtomograms.
**Groundedness**: 8/10 — All technical methodology verified and published for analogous systems. The biological outcome is uncertain.
**Novelty**: 10/10 — No published subtomogram averaging of OMV budding sites.

---

## H3: CryoDRGN Reveals Conformational Gating in OmpA That Controls OMV-Luminal Cargo Access

**Mechanism**: OmpA is the most abundant OMP and a key structural tether between the outer membrane and peptidoglycan. OmpA-depleted regions show increased OMV production. CryoDRGN can resolve continuous conformational heterogeneity of proteins. Apply cryoDRGN to OmpA reconstituted in nanodiscs to map its conformational landscape. The hypothesis predicts that OmpA exists in at least two major conformational states: (1) a "closed" state with the periplasmic domain tightly bound to peptidoglycan (OMV-inhibiting) and (2) an "open" state with detached periplasmic domain exposing a transient pore through which periplasmic cargo proteins could access the OMV lumen during budding.

**Specific prediction**: CryoDRGN analysis of >200,000 OmpA-nanodisc particles will identify >=2 conformational states separated by >=5 Angstrom RMSD in the periplasmic domain position, with the minor state (open) representing 10-30% of the population. The open state will show a channel of >=2 nm diameter connecting the periplasmic space to the nanodisc interior.

**Bridge**: CryoDRGN (Zhong et al. 2021 Nature Methods) maps continuous conformational heterogeneity of protein complexes. It has been applied to ribosomes, spliceosomes, and GPCRs but NEVER to outer membrane proteins or vesicle biogenesis components. [GROUNDED: cryoDRGN methodology validated — Zhong et al. 2021]

**Counter-evidence**: OmpA is a small protein (~35 kDa) at the lower resolution limit for cryoDRGN. The conformational states may not be resolvable at this size. Furthermore, the "gating" model for OmpA is speculative — OmpA may be a passive structural element with no cargo-access function. The nanodisc reconstitution removes the peptidoglycan interaction that may be essential for the conformational switch.

**Test protocol**: (1) Express and purify OmpA from E. coli. (2) Reconstitute in MSP1D1 nanodiscs. (3) Prepare cryo-EM grids. (4) Collect >200,000 particle images. (5) Run cryoDRGN latent space analysis. (6) Identify conformational clusters. (7) Generate 3D volumes for each state. (8) If two states found: (8a) map periplasmic domain position, (8b) measure channel dimensions, (8c) validate by mutagenesis of hinge residues, (8d) test OMV production in mutant locked in each state.

**Confidence**: 4/10 — OmpA at 35 kDa is at the edge of cryoDRGN resolution. The "gating" model is highly speculative.
**Groundedness**: 5/10 — CryoDRGN methodology is established but has never been tested on proteins this small. OmpA conformational flexibility is supported by crystallography but the cargo-gating function is entirely hypothetical.
**Novelty**: 9/10 — No published cryoDRGN analysis of OMPs; the cargo gating model for OmpA is novel.

---

## H4: 3D Variability Analysis (3DVA) of OMV-Associated T6SS Components Reveals a Membrane-Piercing Cargo Injection Mechanism

**Mechanism**: The Type VI Secretion System (T6SS) delivers effector proteins into neighboring cells via a contractile injection mechanism. Some T6SS effectors are also found in OMVs (Liang et al. 2019), raising the question of how membrane-impermeable effectors cross the outer membrane into the OMV lumen. Apply 3DVA (Punjani & Fleet 2021) to the T6SS baseplate complex on the inner surface of the outer membrane to visualize continuous structural transitions. The hypothesis predicts that T6SS contraction creates transient outer membrane openings through which effector proteins are injected into nascent OMV lumens — a "membrane-piercing injection" model analogous to the T6SS inter-cell injection.

**Specific prediction**: 3DVA analysis of >100,000 T6SS baseplate particles in situ (from cryo-ET data) will reveal a continuous motion trajectory showing membrane displacement of >=3 nm during contraction, with a transient pore diameter of >=5 nm sufficient for effector translocation. The motion amplitude measured by 3DVA eigenvalue analysis will be >=10 Angstrom for the first principal component.

**Bridge**: 3DVA resolves continuous conformational motion in single-particle cryo-EM datasets. Applied to T6SS (Ge et al. 2015 Nature, Basler et al. 2012) for contraction mechanism but NEVER analyzed for membrane effects during contraction. [GROUNDED: T6SS structure well-characterized, 3DVA methodology published]

**Counter-evidence**: T6SS effectors may enter OMVs through general secretion pathways (Sec/Tat) rather than T6SS-mediated injection. The membrane-piercing model requires T6SS contraction to occur at sites of active OMV budding — the spatial co-localization may be coincidental. Also, in situ 3DVA from tomographic data is at the edge of current computational methods — resolution may be insufficient to resolve membrane deformation.

**Test protocol**: (1) Image P. aeruginosa by cryo-ET during T6SS firing (T6SS-active mutant). (2) Extract subtomograms of T6SS baseplates in contracted vs extended states. (3) Run 3DVA on the combined dataset. (4) Analyze motion components for membrane deformation. (5) Validate by comparing OMV effector content in T6SS knockout vs wild-type (if injection model correct, T6SS KO OMVs should lack specific effectors). (6) Correlate T6SS firing frequency with OMV budding rate.

**Confidence**: 4/10 — The co-injection model is speculative and the in situ 3DVA technical challenge is high.
**Groundedness**: 6/10 — T6SS structure is well-established. T6SS effectors in OMVs are documented but the mechanism is unknown. The injection model is novel and testable.
**Novelty**: 9/10 — No published model for T6SS-mediated OMV cargo loading.

---

## H5: Cryo-EM Classification of OMV Lipid Asymmetry Identifies LPS O-antigen Length as the Primary Sorting Signal

**Mechanism**: OMVs are enriched in specific LPS chemotypes relative to the parent bacterial outer membrane. LPS O-antigen length (short, medium, long) determines the effective diameter of the LPS hydrophilic head group, which directly affects local membrane curvature. Apply cryo-EM 2D classification to resolve the LPS corona (O-antigen chain) on individual OMVs, then correlate O-antigen density with OMV diameter and cargo content. The hypothesis predicts that OMVs preferentially bud from membrane regions enriched in short-chain LPS variants, because short O-antigen creates lower steric barrier to membrane curvature, and that cargo sorting is a passive consequence of LPS-defined membrane domains.

**Specific prediction**: 2D classification of >10,000 OMV particles will show an inverse correlation (r < -0.5, p < 0.01) between LPS corona thickness (measurable by cryo-EM as electron-dense layer above the outer leaflet) and OMV curvature (inversely related to diameter). OMVs with thin corona (<5 nm) will be 50-100 nm in diameter; OMVs with thick corona (>15 nm) will be 150-250 nm.

**Bridge**: Cryo-EM 2D classification can distinguish particle populations by radial density profiles. LPS corona is electron-dense and resolvable by cryo-EM (Samsudin et al. 2020 showed LPS by cryo-ET). [GROUNDED: LPS structural variability well-documented; cryo-EM radial density analysis established]

**Counter-evidence**: The LPS corona may not be resolvable at the single-OMV level — LPS is flexible and O-antigen is polydisperse within a single cell, producing blurred density rather than discrete classes. Also, smooth (S-form) and rough (R-form) LPS variants affect OMV production (Haurat et al. 2015), but this is KNOWN — the novelty must go beyond existing LPS-OMV size correlations.

**Test protocol**: (1) Prepare cryo-EM grids of OMVs from P. aeruginosa PAO1 (smooth LPS) and wbpL mutant (rough LPS). (2) 2D classify particles by radial profile. (3) Measure corona thickness per particle. (4) Correlate with diameter. (5) Proteomics comparison of size-fractionated OMVs (nanoFACS or asymmetric flow field-flow fractionation) to test if small, thin-corona OMVs carry different cargo. (6) Test prediction: wbpL (rough LPS) mutant should produce smaller OMVs with altered cargo distribution.

**Confidence**: 5/10 — The LPS-curvature-cargo model is physically reasonable but may recapitulate known LPS effects without significant new insight.
**Groundedness**: 7/10 — LPS variability in OMVs is well-documented. The cryo-EM quantitative approach is novel.
**Novelty**: 6/10 — LPS role in OMV biogenesis is partially known; the cryo-EM quantification approach is novel but the concept is not entirely new.

---

## H6: Cryo-ET and Subtomogram Averaging Reveal That OMV Cargo Enrichment Occurs Through OMP Barrel Clustering at Bacterial Pole Sites

**Mechanism**: Many bacteria (including P. aeruginosa and E. coli) produce OMVs preferentially at cell poles. Specific OMPs are also enriched at poles (IcsA in Shigella, PagC in Salmonella). Use cryo-ET of whole bacterial cells combined with subtomogram averaging to test whether OMV budding sites show clustered OMP barrels (resolved as ~3 nm diameter transmembrane densities) with a specific inter-barrel spacing that creates a curvature-favorable packing geometry. The hypothesis predicts that OMV budding sites have a characteristic OMP barrel packing pattern distinct from non-budding membrane regions, and that this packing geometry selectively includes specific barrel sizes (cargo) while excluding others (structural OMPs).

**Specific prediction**: Subtomogram averaging of >50 OMV budding sites and >50 non-budding polar membrane regions from the same tomograms will show a statistically significant difference in OMP barrel density (p < 0.01), with budding sites showing >=1.5x higher barrel density and a characteristic inter-barrel distance of 8-12 nm (vs 15-25 nm at non-budding sites). Barrel diameter distribution at budding sites will be biased toward larger barrels (>=3 nm outer diameter, consistent with cargo OMPs like OprF, OprD) relative to smaller barrels at non-budding sites.

**Bridge**: Subtomogram averaging with particle classification applied to membrane protein distributions. This approach was pioneered for nuclear pore complexes (Zimmerli et al. 2021 Science) and gap junctions (Myers et al. 2018 Nature) but has NEVER been applied to bacterial outer membrane protein distributions. [GROUNDED: Subtomogram averaging of membrane protein arrays established in eukaryotic systems]

**Counter-evidence**: OMP density in the bacterial outer membrane may be too high (~2 million copies/cell) for individual barrel resolution at typical cryo-ET resolution (~3 nm). The distinction between "budding site" and "non-budding site" may be arbitrary in a dynamic system. OMP mobility in the outer membrane may redistribute barrels faster than budding occurs.

**Test protocol**: (1) Image P. aeruginosa by cryo-ET (300 kV, dose-symmetric tilt scheme). (2) Segment outer membrane regions at poles. (3) Classify membrane patches as "budding" (visible curvature, neck) or "non-budding." (4) Extract subtomograms of membrane patches. (5) Average and compare density distributions. (6) Quantify barrel density and spacing. (7) Validate with OMP-specific gold labeling or GFP-OMP strains (fluorescence-guided cryo-ET).

**Confidence**: 6/10 — Technically challenging but the quantitative comparison (budding vs non-budding) provides a clear falsification route.
**Groundedness**: 7/10 — Polar OMV budding is well-documented. OMP enrichment at poles is established. The cryo-ET quantitative approach is the novel contribution.
**Novelty**: 8/10 — No published quantitative comparison of OMP distribution at budding vs non-budding sites.

---

## SELF-CRITIQUE

### Claim verification
- [GROUNDED] RELION 3D classification: YES — Scheres 2012, standard tool
- [GROUNDED] cryoDRGN: YES — Zhong et al. 2021 Nature Methods
- [GROUNDED] 3DVA: YES — Punjani & Fleet 2021 J Struct Biol
- [GROUNDED] Subtomogram averaging of bacterial machines: YES — flagellar motor, T6SS, T4P all resolved
- [GROUNDED] OMV budding at poles: YES — multiple references
- [GROUNDED] T6SS effectors in OMVs: YES — Liang et al. 2019 (needs verification of specific paper)
- [GROUNDED] OmpA depletion increases OMV production: YES — Song et al. 2008, Schwechheimer & Kuehn 2015

### Weakness identification
1. H3 (CryoDRGN on OmpA): 35 kDa is likely too small for cryoDRGN — this is the weakest hypothesis technically
2. H4 (T6SS cargo injection): The co-localization model is highly speculative; T6SS fires INTO cells, not into OMVs
3. H5 (LPS O-antigen sorting): Risk of low novelty — LPS effects on OMVs are partially known
4. Overall: Most hypotheses are "apply technique X to system Y" which is a measurement transfer pattern — this should score well based on meta-insights (measurement transfer > model transfer)
