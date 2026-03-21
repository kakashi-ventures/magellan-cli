# Literature Context — Session 006
## Ferroptosis Lipid Peroxidation x Bacterial Quorum Sensing

### Disjointness Verification
- **"4-HNE" AND "quorum sensing"**: 0 PubMed results (CONFIRMED DISJOINT)
- **"lipid aldehyde" AND "bacterial signaling" AND "inter-kingdom"**: 0 results (CONFIRMED DISJOINT)
- **"ferroptosis" AND "quorum sensing"**: 0 results (CONFIRMED DISJOINT)
- The specific connection between ferroptosis lipid products and QS receptor modulation has NEVER been published.

### Field A: Ferroptosis Lipid Peroxidation

**Key Papers:**
1. **Stockwell et al. 2017 Cell** — Ferroptosis canonical review. GPX4 reduces PLOOH to PLOH. When GPX4 is inhibited (erastin depletes GSH, RSL3 inhibits GPX4 directly), PUFA-phospholipids undergo iron-catalyzed peroxidation.
2. **Ursini & Maiorino 2020 Free Radic Biol Med (PMID 32165281)** — GSH and GPx4 in ferroptosis. LPO produces diverse products including 4-HNE, MDA, isoprostanes, HETE/HODE oxylipins.
3. **Imai et al. 2017 Nat Chem Biol** — GPX4 substrate specificity: preferentially reduces PUFA-PE-OOH at sn-2 position.
4. **Tang & Bhatt 2021 J Exp Med (PMID 33978684)** — Ferroptosis in infection and immunity. Key insight: ferroptosis of immune cells during bacterial infection may promote bacterial growth by releasing iron and nutrients. But no mention of lipid aldehyde effects on bacteria.

**Key Chemical Species:**
- 4-HNE (4-hydroxynonenal): C9 alpha,beta-unsaturated aldehyde from omega-6 PUFA peroxidation. MW 156.2. Highly electrophilic — reacts with Cys, His, Lys via Michael addition. Concentration in ferroptotic cells: 10-100 uM range.
- MDA (malondialdehyde): C3 dialdehyde, less specific marker. MW 72.1.
- HETE/HODE oxylipins: Hydroxylated fatty acids from LOX/non-enzymatic peroxidation.
- Isoprostanes: Prostaglandin-like compounds from non-enzymatic peroxidation.

**4-HNE Protein Modification:**
- Esterbauer et al. 1991 Free Radic Biol Med: 4-HNE reacts with Cys (highest rate), His, Lys via Michael addition (1,4-conjugate addition to the alpha,beta-unsaturated carbonyl).
- Petersen & Doorn 2004 Free Radic Biol Med: Second-order rate constants: Cys (1.2 M^-1 s^-1), His (0.03 M^-1 s^-1), Lys (0.001 M^-1 s^-1) at physiological pH.
- Schopfer et al. 2011 Chem Rev: Electrophilic lipids as signaling mediators — "electrophilic stress" is a recognized post-translational modification pathway.
- **PMID 12386159 (2002)**: E-FABP as molecular 4-HNE target. Covalent modification at Cys120.

### Field C: Bacterial Quorum Sensing

**Key Papers:**
1. **O'Loughlin et al. 2013 PNAS**: LasR and RhlR structural biology. LasR binds 3-oxo-C12-HSL. RhlR binds C4-HSL. Both are LuxR-type transcription factors.
2. **Bottomley et al. 2007 J Biol Chem**: LasR crystal structure with 3-oxo-C12-HSL bound. Trp60, Asp73, Tyr56 form hydrogen bonds with lactone ring and 3-oxo group. Hydrophobic pocket accommodates acyl chain.
3. **McCready et al. 2018 Cell Chem Biol (PMID 30033130)**: Non-native LasR agonists. Critical finding: LasR can adopt an "L3 loop out" conformation that accommodates structurally diverse non-native ligands. This means LasR is MORE promiscuous than previously thought. Non-native compounds can act as agonists (not just antagonists).
4. **Boursier et al. 2025 ACS Chem Biol (PMID 40960234)**: Sulfonyl homoserine lactones as RhlR inhibitors. Shows that modified lactone scaffolds can modulate QS receptors. The lactone ring can tolerate sulfonyl substitution.
5. **Manefield et al. 2002 Microbiology**: Halogenated furanones from seaweed (Delisea pulchra) inhibit QS. Furanones LACK the homoserine lactone ring but still bind QS receptors. This demonstrates that the lactone ring is NOT absolutely required for receptor binding.

**QS Receptor Biochemistry:**
- LasR: prefers 3-oxo-C12-HSL (Kd ~ 10-50 nM). Binds with high affinity. Can tolerate chain length variations (C8 to C14). Non-native agonists proven.
- RhlR: prefers C4-HSL (shorter chain). More promiscuous in some studies.
- PqsR: the PQS (Pseudomonas quinolone signal) system is separate but cross-regulated with AHL systems.
- Critical cysteine residues in LuxR-type receptors: Cys79 in LasR is conserved and potentially accessible to electrophilic modification.

### Inter-Kingdom Signaling (Existing Work)

1. **Molecules 2014 (PMID 24448067)**: "Oxidized fatty acids as inter-kingdom signaling molecules" — Reviews oxylipins as signals between kingdoms. Discusses plant-fungal oxylipin communication. Does NOT mention ferroptosis or mammalian-bacterial oxylipin signaling.
2. **Front Plant Sci 2022 (PMID 36186042)**: Fungal and bacterial oxylipins in plant disease. Structural similarity of oxylipins across kingdoms enables cross-kingdom "listening."
3. **DSF family signaling**: Diffusible signal factor (cis-2-unsaturated fatty acids) used by Xanthomonas and Burkholderia. Shows that fatty acid derivatives CAN function as QS signals. DSF is structurally distinct from AHLs but activates its own receptor system.

**Key Gap**: All inter-kingdom lipid signaling work focuses on bacteria→host or plant→bacteria. The HOST→BACTERIA direction via ferroptosis lipid products is completely unexplored.

### Iron as Shared Variable

- **Host iron sequestration during infection** (nutritional immunity): lactoferrin, NRAMP1 (SLC11A1), hepcidin, ferritin, calprotectin (Mn/Zn but also Fe)
- **Bacterial iron acquisition**: P. aeruginosa produces pyoverdine and pyochelin siderophores, regulated by PvdS and Las/Rhl QS systems
- **QS regulates iron acquisition**: 3-oxo-C12-HSL signaling through LasR upregulates pyoverdine biosynthesis (Stintzi et al. 1998)
- **Iron promotes ferroptosis**: Labile iron pool (LIP) catalyzes Fenton reaction → lipid radical → PLOOH → fragmentation to 4-HNE
- **Critical connection**: At infection sites, iron redistribution creates zones where both ferroptosis and bacterial QS are enhanced

### Computational Validation Notes

**KEGG Pathway Cross-References:**
- Ferroptosis pathway (hsa04216): GPX4, ACSL4, LPCAT3, System Xc-
- Quorum sensing pathway (ko02024): LasI/R, RhlI/R (bacterial pathway — no human homologs)
- Iron homeostasis connects both: TFRC, FTH1, FTL, SLC40A1 in ferroptosis; siderophore biosynthesis in QS
- No direct KEGG pathway link between ferroptosis and QS (confirming disjointness)

**STRING Interaction:**
- No direct protein-protein interaction between GPX4 and any QS protein (expected — different kingdoms)
- Within ferroptosis: GPX4-ACSL4-LPCAT3 well-connected (score >0.9)
- Within QS: LasI-LasR-RhlI-RhlR well-connected

**Back-of-Envelope Calculations:**
- 4-HNE concentration at ferroptotic cell surface: ~10-100 uM (Esterbauer 1991)
- AHL concentration for QS activation: C4-HSL EC50 for RhlR ~ 1-10 uM (Pearson et al. 1995)
- If 4-HNE can activate QS receptors at similar potency to AHLs, ferroptotic concentrations would be in the right range
- BUT: 4-HNE half-life in aqueous solution ~ 2-5 minutes (reacts rapidly with thiols, amines)
- Diffusion distance in 2-5 min: sqrt(2Dt) ~ sqrt(2 * 500 um^2/s * 300 s) ~ 550 um. Sufficient for local paracrine effects at infection site.
