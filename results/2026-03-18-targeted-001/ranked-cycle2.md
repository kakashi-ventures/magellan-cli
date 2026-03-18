# Ranked Hypotheses — Cycle 2
# Session: 2026-03-18-targeted-001
# Fields: Ferroptosis biology x Bacterial quorum sensing biochemistry
# Ranker: Sonnet 4.6 | Date: 2026-03-18
# Candidates scored: 8 (cycle 2 survivors/wounded + cycle 1 evolved still in play)

---

## Candidates Pool

**Cycle 2 survivors:**
- C2-3 SURVIVES (revised conf 5) — Pyocyanin/DHODH Ferroptosis
- C2-7 SURVIVES (revised conf 4) — Fur-PQS Functional Switch

**Cycle 2 wounded:**
- C2-5 WOUNDED (revised conf 3) — Bacterial GSH Scavenging / GSH Desert
- C2-6 WOUNDED (revised conf 3) — HNE-Cys Thiazolidine as SdiA Agonist

**Cycle 1 evolved, still in play:**
- E-H8 (conf 6) — System Xc- Inhibition / GSH Depletion
- E-H7 (conf 5) — ACSL4 rs2278190 Myeloid Balancing Selection
- E-H5 (conf 5) — HNE-GL AHL Lactonase Inter-Kingdom Detoxification
- E-H1 (conf 4) — 4-HNE-GSH SdiA Partial Agonist via MRP1

---

## Per-Hypothesis Scoring

---

### Hypothesis: C2-3 — Pyocyanin-Initiated Mitochondrial Lipid Peroxidation Induces DHODH-Pathway-Specific Ferroptosis

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 8 | No published paper connects pyocyanin to ferroptosis specifically, and the Critic's searches (March 2026) confirmed absence of any ferrostatin/C11-BODIPY study on pyocyanin. Prior cell-death classifications (Usher 2002; Muller 2006) predated ferroptosis as a defined category (Dixon et al. 2012) and used non-specific assays. The DHODH-compartment framing adds a second layer of novelty beyond simple reclassification. |
| Mechanistic Specificity | 20% | 8 | Names specific molecules throughout: pyocyanin, DHODH, NADPH, GSH, CoQ10, FSP1, GPX4; invokes measured redox potential (Em = -34 mV, Chem Sci 2021); cites quantified GSH depletion (Ran et al. 2003, Am J Physiol). The main gap is that the superoxide generation rate (5 nmol/min/10^6 cells) is parametric and unverified for Fenton-chain initiation in the mitochondrial compartment. |
| Cross-field Distance | 10% | 7 | Connects P. aeruginosa phenazine biochemistry (microbiology/infectious disease) to iron-dependent regulated cell death machinery (cell biology/redox biology). These communities share some overlap through oxidative stress literature, but ferroptosis is a distinct cell biology sub-field that infection microbiologists rarely engage with, and vice versa. |
| Testability | 20% | 9 | Four specific independently falsifiable predictions: (1) ferrostatin-1 or MitoTEMPO rescues pyocyanin-induced death; (2) DHODH overexpression rescues but GPX4 overexpression alone does not fully rescue; (3) brequinar potentiates pyocyanin toxicity; (4) mitochondria-targeted C11-BODIPY shows mitochondrial lipid peroxidation before cytoplasmic. Each experiment uses standard ferroptosis tools. A PhD student could complete this in 3 months with accessible reagents. |
| Impact | 10% | 7 | If confirmed, this reframes 40+ years of pyocyanin toxicity literature under the ferroptosis paradigm, opens ferrostatin-1 as a potential therapeutic in P. aeruginosa lung infections (including CF), and provides a QS-regulated mechanism for iron-dependent cell death in infectious disease. It would not open an entirely new field but would substantially redirect both P. aeruginosa pathogenesis research and the emerging ferroptosis-infection biology interface. |
| Groundedness | 20% | 7 | Critic assessed ~75% of load-bearing claims as grounded. Pyocyanin concentrations in CF sputum (Wilson et al. 1988), redox potential (Chem Sci 2021), GSH depletion (Ran et al. 2003), DHODH as mitochondrial ferroptosis suppressor (Mao et al. 2021, Nature), and NADPH depletion are all verified from cited literature. Two parametric claims: superoxide generation rate and compartment-specific prediction. The core mechanistic link (pyocyanin attacks precisely the three axes that define ferroptosis) is nearly fully grounded. |
| **Composite** | | **7.90** | (8×0.20) + (8×0.20) + (7×0.10) + (9×0.20) + (7×0.10) + (7×0.20) = 1.60+1.60+0.70+1.80+0.70+1.40 |

---

### Hypothesis: C2-7 — Fur-Mediated Transcriptional Rewiring Under Ferroptotic Iron Excess Decouples PQS from Iron Scavenging, Enabling Repurposing as Cytotoxic Ferroptosis-Amplification Signal

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 7 | The Fur-PrrF-antR-PQS regulatory circuit is extensively published (Wilderman et al. 2004; Oglesby et al. 2008). However, the specific reframing — that ferroptotic iron excess produces a PQS functional switch from iron-scavenging to cytotoxic amplifier — is not published. The 2025 Nature Comms PQS-CNMT-TFR1 paper provides the cytotoxic arm, and the connection to ferroptotic iron as the triggering iron source is novel. Partial novelty: the individual components are known; the synthesis is new. |
| Mechanistic Specificity | 20% | 7 | Names Fur, PrrF sRNAs, antR, pvdS, PQS, phuR, hasAp, CNMT, TFR1; references PQS-Fe3+ chelation (Diggle et al. 2007); invokes the 2025 Nature Comms mechanism. Weakened by the PrrF-antR complication: the Critic showed that iron excess actually reduces anthranilate via antR de-repression, which contradicts "PQS continues unaffected." The mechanism as stated has an internal inconsistency that is partially resolved by the kynurenine pathway compensatory supply. |
| Cross-field Distance | 10% | 7 | Bridges iron metabolism regulatory genetics in P. aeruginosa (microbiology) with iron-dependent cell death biology (cell biology/biochemistry). These domains share iron as vocabulary but almost never interact at the mechanistic signaling level. A ferroptosis biologist would not read Fur regulation papers; a Pseudomonas microbiologist would not read CNMT ferroptosis papers. |
| Testability | 20% | 8 | Clear RT-qPCR predictions (reduced pvd, maintained/increased pqs, increased phu/has expression) in P. aeruginosa exposed to ferroptotic cell supernatant or defined iron excess. Cytotoxicity against fresh macrophages in co-culture is measurable. Each step in the amplification loop (Fur activation, pvd repression, pqs maintained, TFR1 upregulation) is independently measurable with standard tools. Single-experiment feasibility within 3 months. |
| Impact | 10% | 7 | Establishes a mechanistic positive feedback loop between host ferroptosis and bacterial QS-mediated cytotoxicity — a bistable amplification mechanism in infection. If validated, it would explain why P. aeruginosa infections can transition rapidly from contained to overwhelming in iron-rich microenvironments (e.g., hemoptysis in CF), and suggest iron chelation as a therapeutic strategy to break the loop. Meaningful but not field-opening. |
| Groundedness | 20% | 6 | Critic assessed ~65% of load-bearing claims as grounded. Fur regulation (Cornelis et al. 2009), PQS-Fe3+ (Diggle et al. 2007), phu/has systems (Ochsner et al. 2000), PQS-CNMT-TFR1 (Nature Comms 2025) are all grounded. The "PQS production continues under iron excess" claim is oversimplified — the Critic identified the PrrF-antR pathway contradicts this. Ferroptotic iron release magnitude (10-50 uM) is parametric. Temporal switch model is logically derived but unverified. |
| **Composite** | | **7.10** | (7×0.20) + (7×0.20) + (7×0.10) + (8×0.20) + (7×0.10) + (6×0.20) = 1.40+1.40+0.70+1.60+0.70+1.20 |

---

### Hypothesis: E-H8 — 3-oxo-C12-HSL Induces Host Ferroptosis via System Xc- Competitive Inhibition and GSH Depletion

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 8 | No published paper proposes 3-oxo-C12-HSL as a System Xc- (SLC7A11) competitive inhibitor. The Critic's cycle 1 searches confirmed absence of direct connection. The revised mechanism (acyl-chain competition at SLC7A11's amphipathic substrate channel) is distinct from the discredited direct GPX4 covalent modification. TRIM25-GPX4 was published (Li et al. 2023), but SLC7A11 competitive inhibition by AHL is uncharacterized. |
| Mechanistic Specificity | 20% | 7 | Names specific components: SLC7A11 subunit, acyl-chain competitive inhibition, GSH depletion below GPX4 co-substrate threshold, lipid hydroperoxide accumulation. Identifies the mechanism as competitive at the amphipathic substrate channel. Gaps: SLC7A11's amphipathic binding properties are not specifically characterized for C12-acyl chains; the threshold GSH concentration for GPX4 impairment is not stated as a verifiable number; no specific predicted IC50 for the SLC7A11 interaction. |
| Cross-field Distance | 10% | 8 | Connects P. aeruginosa quorum sensing biochemistry (AHL structure/function) to membrane transporter pharmacology (SLC7A11/xCT) to iron-dependent cell death (ferroptosis/GSH). The three domains rarely interact: QS chemists don't read xCT pharmacology papers; ferroptosis biologists don't read AHL structure-activity papers. |
| Testability | 20% | 8 | Testable with existing tools: SLC7A11 cystine import assay (radiolabeled [14C]-cystine) + 3-oxo-C12-HSL competition; cellular GSH measurement via Ellman's reagent; ferrostatin-1 rescue; SLC7A11 knockout comparison. Competitive inhibition kinetics (Ki) can be measured with standard enzyme kinetics. Full experiment feasible within 3 months in a cell biology lab. |
| Impact | 10% | 7 | Provides a second mechanistic arm for how P. aeruginosa QS hijacks host GSH/GPX4 axis to induce ferroptosis, complementing the PQS-CNMT-TFR1 pathway. Therapeutic implications: SLC7A11 agonism (system Xc- activation) could protect against AHL-mediated ferroptosis in CF lung epithelium. Reframes AHL as a multifunctional virulence molecule operating on redox homeostasis, not just immune modulation. |
| Groundedness | 20% | 5 | 3-oxo-C12-HSL's amphipathic structure is grounded. System Xc- inhibition by amphipathic molecules is documented for other lipids (lysophospholipids). GSH depletion -> ferroptosis sensitization is grounded. However: the specific SLC7A11 competitive inhibition by C12-AHL has no published evidence; GPX4 Km for GSH is uncertain; the threshold model requires quantitative support. Critic assessed as MEDIUM groundedness. Roughly 50-55% grounded. |
| **Composite** | | **7.00** | (8×0.20) + (7×0.20) + (8×0.10) + (8×0.20) + (7×0.10) + (5×0.20) = 1.60+1.40+0.80+1.60+0.70+1.00 |

---

### Hypothesis: E-H7 — ACSL4 rs2278190 Myeloid-Specific Regulatory Variant Under Pathogen-Driven Balancing Selection in Pre-Antibiotic-Era Populations

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 8 | No published study connects ACSL4 genetic variation specifically to ferroptosis susceptibility in the context of bacterial QS-induced virulence. The rs2278190 myeloid regulatory variant and balancing selection framing are not in the literature. The broader ACSL4-selection pressure story is speculative enough to be novel without being impossible — a genuine gap. |
| Mechanistic Specificity | 20% | 5 | Names specific components: rs2278190, myeloid isoform, ExoU phospholipase, AA liberation from PE, ACSL4 in ferroptosis. However the evolutionary genetics arm is underspecified: no population genetics statistics (FST, dN/dS, iHS scores for rs2278190), no specific selection coefficient estimate, no prediction of derived vs ancestral allele direction of effect. The mechanistic biology chain (ExoU -> AA -> ferroptosis) is more specific than the genetics arm. |
| Cross-field Distance | 10% | 9 | Bridges three widely separated disciplines: bacterial quorum sensing biochemistry, ferroptosis cell biology, and human population genetics/evolutionary genomics. Each pair of disciplines is distant; the three-way connection is highly cross-disciplinary. A QS researcher, a ferroptosis biologist, and a population geneticist would each find the other two fields entirely unfamiliar in this context. |
| Testability | 20% | 5 | The evolutionary genetics arm requires access to ancient DNA datasets or archaic genome databases to detect pre-antibiotic-era selection signatures — feasible with 1000 Genomes + ancient DNA repositories but analytically complex. The myeloid isoform expression difference can be tested with eQTL data. The ferroptosis susceptibility per genotype can be tested with myeloid cell differentiation + ExoU challenge. Overall 6-9 months of work, borderline for a solo PhD student. |
| Impact | 10% | 8 | If validated, this would explain why ACSL4 (a ferroptosis sensitizer) is under balancing selection rather than purifying selection, and would link the evolution of human ferroptosis susceptibility to ancient microbial QS-mediated virulence. It would establish a new connection between population genetics, ferroptosis biology, and infectious disease ecology — genuinely field-spanning if true. |
| Groundedness | 20% | 4 | The ACSL4 role in ferroptosis is grounded. ExoU phospholipase function is grounded. rs2278190 as a regulatory variant: PARAMETRIC — no published eQTL data for this specific SNP verified. Myeloid-specific isoform expression: PARAMETRIC. Balancing selection evidence: SPECULATIVE — no published selection statistics. Pre-antibiotic-era population inference: SPECULATIVE. Critic assessed as MEDIUM-LOW groundedness. Roughly 35-40% grounded. |
| **Composite** | | **5.90** | (8×0.20) + (5×0.20) + (9×0.10) + (5×0.20) + (8×0.10) + (4×0.20) = 1.60+1.00+0.90+1.00+0.80+0.80 |

---

### Hypothesis: E-H5 — Gut Microbiome AHL Lactonases Hydrolyze 4-Hydroxy-Nonenoic Acid Gamma-Lactone (HNE-GL) as Novel Inter-Kingdom Detoxification

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 8 | No published paper proposes gut microbiome AHL lactonases hydrolyzing ferroptosis-derived lipid lactones. The specific substrate identity (4-hydroxy-nonenoic acid gamma-lactone formed via ALDH3A1 oxidation) is a novel hypothesis, and the inter-kingdom detoxification framing (bacteria protecting host tissue from lipid peroxidation products) has no precedent in this form. The Evolver's correction from cyclic ethers to gamma-lactones resolves the cycle 1 chemical error and makes the mechanism chemically defensible. |
| Mechanistic Specificity | 20% | 7 | Names the full pathway: 4-HNE -> ALDH3A1 oxidation to 4-HNA -> spontaneous gamma-lactonization to HNE-GL -> AiiA/QsdA AHL lactonase hydrolysis. ALDH3A1 as the oxidase is a specific testable claim. The gamma-lactonization equilibrium is a known reaction class. AiiA and QsdA are named enzymes. Gaps: gamma-lactonization yield under physiological conditions (competing hydrations/reductions), HNE-GL stability, and the precise Km of AiiA/QsdA for HNE-GL versus cognate AHL substrates. |
| Cross-field Distance | 10% | 8 | Connects ferroptosis lipid peroxidation biochemistry (cell biology/redox), aldehyde detoxification enzymology (biochemistry), gamma-lactonization chemistry (organic chemistry), and bacterial quorum-quenching enzymology (microbiology). The bridge from host lipid peroxidation products to bacterial enzyme substrate promiscuity crosses substantial disciplinary distance. |
| Testability | 20% | 8 | Highly testable: synthesize HNE-GL (or chemically) and test against purified AiiA/QsdA with standard lactonase activity assays (pH indicator, HPLC). Test ALDH3A1 oxidation of 4-HNE to 4-HNA in ferroptotic lysates. Test gamma-lactonization equilibrium by NMR. Test gut microbiome conditioned media for HNE-GL-hydrolyzing activity. Each experiment is independent and accessible. A PhD student could complete the in vitro biochemistry in 3 months. |
| Impact | 10% | 6 | If true, it would establish gut bacteria as active participants in host lipid peroxidation detoxification — a new functional relationship beyond metabolic cross-feeding. It would suggest that microbiome composition (AHL lactonase abundance) modulates host ferroptosis susceptibility. Therapeutically, lactonase-expressing probiotics could protect against ferroptotic pathology. Meaningful but not field-opening by itself. |
| Groundedness | 20% | 5 | ALDH3A1 oxidation of 4-HNE to 4-HNA: GROUNDED (ALDH3A1 is a known 4-HNE-metabolizing enzyme). Gamma-lactonization of hydroxy acids: GROUNDED as a reaction class (well-established organic chemistry). AiiA/QsdA lactonase structures and mechanisms: GROUNDED. The specific claim that HNE-GL is a substrate: SPECULATIVE (no binding or activity data). 4-HNE to 4-HNA flux in ferroptotic cells: PARAMETRIC. Gut commensal lactonase prevalence: PARAMETRIC. Critic assessed as MEDIUM groundedness. |
| **Composite** | | **6.90** | (8×0.20) + (7×0.20) + (8×0.10) + (8×0.20) + (6×0.10) + (5×0.20) = 1.60+1.40+0.80+1.60+0.60+1.00 |

---

### Hypothesis: C2-5 — QS-Regulated Bacterial GSH Import Creates Pericellular GSH Desert That Sensitizes Host Epithelial Cells to Ferroptosis

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 7 | No paper explicitly connects bacterial GSH scavenging to host ferroptosis sensitization. Bacterial GSH import (GsiABCD in E. coli; GGT in P. aeruginosa) is an emerging field (S. pyogenes mBio 2022; S. aureus gisBCD 2023), but the ferroptosis framing is absent from all current literature. The "nutritional immunity inversion" concept (bacteria scavenge redox defenses rather than metals) is genuinely creative. |
| Mechanistic Specificity | 20% | 4 | Invokes named systems (GsiABCD, GGT, rhl QS) but with significant species errors: GsiABCD is characterized in E. coli, not P. aeruginosa; rhl-GGT regulatory link is unverified. GPX4 Km for GSH is stated as "~1-3 mM" but the Critic identified this may be 100x lower (0.01-0.1 mM), which would make the pericellular depletion mechanism ineffective. Quantitative depletion calculation makes unverified assumptions about bacterial density at epithelial surface. The mechanism is named but imprecisely. |
| Cross-field Distance | 10% | 7 | Connects bacterial nutrition/QS regulation (microbiology) to host antioxidant homeostasis (biochemistry) to regulated cell death (cell biology). Reasonable cross-field distance — these communities do not typically share vocabulary around GSH as a contested resource in the infection microenvironment. |
| Testability | 20% | 7 | Co-culture with GGT-knockout versus wild-type P. aeruginosa + pericellular GSH measurement (Ellman's reagent) + host ferroptosis assays (C11-BODIPY, GPX4 activity, ferrostatin rescue). N-acetylcysteine rescue control is specified. The experiment is straightforward. Complicated by host GGT competition (needs GGT inhibitor such as DON to separate bacterial vs host enzyme contribution). |
| Impact | 10% | 6 | Establishes a metabolic warfare mechanism where bacteria weaponize GSH depletion against host ferroptosis defenses. If true, it would add a new dimension to nutritional immunity (beyond metal sequestration) and suggest GSH supplementation or N-acetylcysteine as infection countermeasures. Meaningful in the ferroptosis-infection interface but not transformative. |
| Groundedness | 20% | 4 | GsiABCD in E. coli is grounded (Suzuki et al. 2005; bioRxiv 2024). Bacterial GGT as virulence factor in P. aeruginosa is grounded. QS regulation of GSH import: SPECULATIVE. GsiABCD-equivalent in P. aeruginosa: UNVERIFIED. GPX4 Km = 1-3 mM: CONTESTED (may be 100x lower). Depletion calculation: PARAMETRIC with major assumptions. Host GGT competition: NOT ADDRESSED. Critic assessed ~45% grounded. |
| **Composite** | | **5.50** | (7×0.20) + (4×0.20) + (7×0.10) + (7×0.20) + (6×0.10) + (4×0.20) = 1.40+0.80+0.70+1.40+0.60+0.80 |

---

### Hypothesis: C2-6 — 4-HNE-Cysteine Thiazolidine Ring (from Bacterial GGT Processing of Exported GS-HNE) Activates SdiA as AHL Structural Mimic

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 8 | No paper proposes thiazolidine-as-AHL-mimic for any LuxR-family receptor. SdiA promiscuity studies (Nguyen et al. 2015) tested OCL and xylose but no thiazolidine heterocycles. The multi-step bacterial processing pathway (GS-HNE export -> bacterial GGT -> thiazolidine cyclization -> SdiA) has no precedent. Genuinely uncharted territory. |
| Mechanistic Specificity | 20% | 7 | Fully names the pathway: GST A4-4 conjugation, MRP1 export of GS-HNE, bacterial GGT hydrolysis to 4-HNE-Cys, thiazolidine ring cyclization, SdiA binding via 5-membered heterocyclic ring mimicry. GS-HNE export via MRP1 is grounded (Awasthi et al. 2004). The thiazolidine chemistry is well-characterized (Esterbauer, RSC Chem Commun 2018). The unresolved question is the SdiA binding interaction itself: H-bonding mismatch (thiazolidine NH donor vs lactone O acceptor) is a specific named problem, and the ring equilibrium reversibility is quantitatively unaddressed. |
| Cross-field Distance | 10% | 8 | Connects ferroptosis GSH depletion biochemistry, MRP1 export physiology, bacterial GGT enzymology, heterocyclic chemistry, and LuxR receptor pharmacology. A 5-field bridge across substantial disciplinary distance. The four-step processing chain crosses eukaryotic-prokaryotic boundaries in both directions, which is unusual. |
| Testability | 20% | 8 | The testability is outstanding: synthesize 4-HNE-Cys thiazolidine (straightforward organic synthesis), run computational docking to SdiA crystal structure, then test binding via ITC or fluorescence polarization, then test reporter gene activation. Each step independently falsifiable. A PhD student could complete the in vitro work in 3 months. The Critic emphasized this as one of the hypothesis's genuine strengths. |
| Impact | 10% | 6 | Establishes a novel inter-kingdom signaling loop where host ferroptotic GSH depletion generates a QS agonist for E. coli SdiA. Therapeutic implications: blocking MRP1 export or bacterial GGT would suppress the thiazolidine signal. Interesting but the SdiA-specific scope limits broad impact — SdiA is relevant in enteric infection contexts but not in CF/P. aeruginosa infection where most QS-ferroptosis work is focused. |
| Groundedness | 20% | 5 | GS-HNE formation and MRP1 export: GROUNDED (Awasthi et al. 2004). Bacterial GGT activity and dipeptidase: GROUNDED. Thiazolidine ring chemistry from cysteine + aldehyde: GROUNDED (Esterbauer, RSC). Ring equilibrium at physiological pH: PARAMETRIC (reversible, may not favor closed form). SdiA binding by thiazolidine: SPECULATIVE. SdiA agonism (vs inhibition): SPECULATIVE. Critic assessed ~50% grounded. |
| **Composite** | | **6.80** | (8×0.20) + (7×0.20) + (8×0.10) + (8×0.20) + (6×0.10) + (5×0.20) = 1.60+1.40+0.80+1.60+0.60+1.00 |

---

### Hypothesis: E-H1 — 4-HNE-Glutathione Conjugate (4-HNE-GSH) as a Stable Ring-Bearing SdiA Partial Agonist via MRP1 Export

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 7 | No published paper tests GS-HNE as a LuxR-family agonist. The gamma-glutamyl pseudo-ring concept is creative. However, C2-6 (the evolved descendant) proposes the same MRP1 export route but with a more specific mechanism (bacterial GGT processing -> thiazolidine) that addresses the core ring-structure problem more concretely. E-H1's pseudo-ring concept is original but chemically weaker than C2-6's thiazolidine. |
| Mechanistic Specificity | 20% | 5 | Names GS-HNE, MRP1, SdiA, and the gamma-glutamyl pseudo-ring concept. However the pseudo-ring geometry claim is speculative: the gamma-glutamyl-cysteinyl amide bond of GSH does not form a rigid ring. The "pseudo-ring" language is metaphorical rather than a verifiable molecular structure. Less specific than C2-6 because the chemical identity of the active ring species is not precisely defined. |
| Cross-field Distance | 10% | 8 | Same broad cross-field character as C2-6: connects ferroptosis/GSH metabolism, MRP1 transporter biology, and LuxR-family receptor pharmacology across eukaryotic-prokaryotic domains. |
| Testability | 20% | 7 | Testable: MRP1-overexpressing cells + SdiA reporter assay, radiolabeled GS-HNE export tracking, SdiA binding assay with GS-HNE. But the pseudo-ring concept makes it harder to define specific hypotheses: the "partial agonist" prediction requires dose-response curves and comparison to full agonist standards. Slightly less clean than C2-6's single-step synthesize-and-test design. |
| Impact | 10% | 5 | If the pseudo-ring concept is wrong (as C2-6's critique implied), the impact is low. If it is right, it establishes GS-HNE as an endogenous LuxR agonist, but this would likely be quickly superseded by C2-6's thiazolidine mechanism (which is more specific and more chemically grounded). The impact is constrained by the hypothesis's position as a less-specific ancestor of C2-6. |
| Groundedness | 20% | 4 | 4-HNE-GSH conjugate formation: GROUNDED. MRP1 export of GS-HNE: GROUNDED (Awasthi et al. 2004). SdiA broader promiscuity: GROUNDED (Nguyen et al. 2015). The gamma-glutamyl pseudo-ring as a ring-bearing AHL mimic: SPECULATIVE — no structural or computational evidence that this conformation mimics lactone binding. SdiA partial agonism: SPECULATIVE. Critic assessed as MEDIUM-LOW groundedness. |
| **Composite** | | **5.60** | (7×0.20) + (5×0.20) + (8×0.10) + (7×0.20) + (5×0.10) + (4×0.20) = 1.40+1.00+0.80+1.40+0.50+0.80 |

---

## Final Ranking Table

| Rank | ID | Title (abbreviated) | Composite | Novelty | Mech Spec | X-Field | Testability | Impact | Groundedness |
|------|----|---------------------|-----------|---------|-----------|---------|-------------|--------|--------------|
| 1 | C2-3 | Pyocyanin/DHODH Ferroptosis | **7.90** | 8 | 8 | 7 | 9 | 7 | 7 |
| 2 | C2-7 | Fur-PQS Functional Switch | **7.10** | 7 | 7 | 7 | 8 | 7 | 6 |
| 3 | E-H8 | System Xc- / GSH Depletion | **7.00** | 8 | 7 | 8 | 8 | 7 | 5 |
| 4 | E-H5 | HNE-GL AHL Lactonase | **6.90** | 8 | 7 | 8 | 8 | 6 | 5 |
| 5 | C2-6 | HNE-Cys Thiazolidine / SdiA | **6.80** | 8 | 7 | 8 | 8 | 6 | 5 |
| 6 | E-H7 | ACSL4 rs2278190 Selection | **5.90** | 8 | 5 | 9 | 5 | 8 | 4 |
| 7 | E-H1 | 4-HNE-GSH SdiA Pseudo-Ring | **5.60** | 7 | 5 | 8 | 7 | 5 | 4 |
| 8 | C2-5 | Bacterial GSH Desert | **5.50** | 7 | 4 | 7 | 7 | 6 | 4 |

---

## Diversity Check

Examining top 5: C2-3, C2-7, E-H8, E-H5, C2-6.

### Pairwise Analysis

**C2-3 (Pyocyanin/DHODH) vs C2-7 (Fur-PQS Functional Switch)**
- Bridge mechanism: C2-3 uses pyocyanin redox cycling; C2-7 uses Fur transcriptional regulation of PQS. Different.
- Subfields connected: C2-3 = QS metabolite phenazine -> redox -> ferroptosis (DHODH axis); C2-7 = iron-Fur regulatory genetics -> PQS function -> ferroptosis amplification loop. Different — one is biochemical, one is regulatory/genetic.
- Prediction type: C2-3 predicts a ferrostatin-rescuable death phenotype; C2-7 predicts a gene expression switch. Different.
- Verdict: NOT REDUNDANT.

**C2-3 (Pyocyanin/DHODH) vs E-H8 (System Xc- / GSH Depletion)**
- Bridge mechanism: C2-3 uses pyocyanin oxidizing GSH directly; E-H8 uses 3-oxo-C12-HSL competitively inhibiting System Xc-. Both lead to GSH depletion but via entirely different routes.
- Subfields: Both connect P. aeruginosa QS to ferroptosis, but different QS molecules (pyocyanin vs 3-oxo-C12-HSL) and different entry points (direct GSH oxidation vs transporter inhibition).
- Prediction type: Both involve GSH depletion as proximate cause, so they share an intermediate prediction. However, the proximate mechanism is distinct (pyocyanin-direct vs transporter-blockade). Not identical prediction.
- Verdict: CONVERGENT on GSH depletion but mechanistically distinct. No redundancy flag at the bridge level.

**E-H8 (System Xc-) vs C2-5 (GSH Desert)**
- Both lead to GSH depletion in host cells, but C2-5 is not in the top 5 (rank 8). Not relevant to top-5 diversity check.

**E-H5 (HNE-GL Lactonase) vs C2-6 (HNE-Cys Thiazolidine)**
- Bridge mechanism: E-H5 = ferroptosis lipid peroxidation products -> bacterial detoxification enzyme promiscuity. C2-6 = ferroptosis GSH export -> bacterial processing -> AHL receptor agonism. Both involve bacterial enzymatic processing of ferroptosis-derived substrates, but in opposite directions: E-H5 is host-protective (bacteria detoxify host-damaging lipids); C2-6 generates a QS signal (bacteria convert host waste to a virulence cue).
- Subfields: E-H5 bridges lipid oxidation biochemistry + bacterial quorum-quenching enzymology. C2-6 bridges GSH metabolism + transporter biology + LuxR pharmacology. Different.
- Prediction type: E-H5 predicts enzyme activity assay (lactonase on HNE-GL); C2-6 predicts receptor binding/activation assay. Different experimental readouts.
- Verdict: PARTIALLY CONVERGENT in using bacterial enzymatic promiscuity on host ferroptosis products, but directions and downstream biology are opposite. Not redundant.

**C2-7 (Fur-PQS) vs E-H8 (System Xc-)**
- Completely different mechanisms: regulatory genetics vs transporter pharmacology.
- Verdict: NOT REDUNDANT.

### Diversity Verdict

No 3+ cluster of conceptually identical hypotheses exists among the top 5. The top 5 distribute across:
- Phenazine redox toxicity -> ferroptosis (C2-3)
- Iron-regulatory transcriptional switch -> PQS amplification (C2-7)
- AHL transporter competitive inhibition -> GSH depletion (E-H8)
- Lipid peroxidation product -> bacterial detoxification (E-H5)
- GSH export -> bacterial processing -> AHL mimicry (C2-6)

These five hypotheses span three distinct bridge mechanisms (redox cycling, regulatory rewiring, enzymatic promiscuity/mimicry) and two distinct directionalities (QS-to-ferroptosis amplification and ferroptosis-to-QS signaling). No adjustment required.

**Diversity adjustment made: NONE.**

---

## Evolution Selection (Top 3-5 Post-Diversity-Check)

Selected for evolution: **C2-3, C2-7, E-H8, E-H5, C2-6**

| Rank | ID | Composite | Rationale |
|------|----|-----------|-----------|
| 1 | C2-3 | 7.90 | Highest composite. Strongest groundedness. DHODH-compartment prediction is the single most testable and novel claim. Priority target for Quality Gate. |
| 2 | C2-7 | 7.10 | Strong regulatory mechanism. PrrF-antR complication should be explicitly resolved in evolution: the strongest version reframes as "iron-loaded PQS is MORE cytotoxic under ferroptotic iron conditions" rather than "PQS production is unaffected." |
| 3 | E-H8 | 7.00 | Clean transporter-competition mechanism. Groundedness is the limiting factor. Evolution should seek a published amphipathic molecule with documented SLC7A11 inhibition as structural precedent to anchor groundedness. |
| 4 | E-H5 | 6.90 | Highly testable inter-kingdom detoxification hypothesis. Evolution should quantify gamma-lactonization yield from ALDH3A1 oxidation under ferroptotic conditions, and identify which gut commensals express AiiA/QsdA homologs. |
| 5 | C2-6 | 6.80 | Outstanding testability and novelty. Selected over E-H1 (5.60) because C2-6 provides concrete ring chemistry (thiazolidine) versus E-H1's metaphorical pseudo-ring. H-bonding mismatch should be resolved by computational docking before experimental commitment. |

**Not selected:**
- E-H7 (5.90): High cross-field distance and impact, but insufficient groundedness (speculative rs2278190 eQTL, no selection statistics) and low testability for a solo PhD student. Interesting direction but not ready for Quality Gate.
- E-H1 (5.60): Superseded by C2-6, which shares the same MRP1 export entry point but with more concrete ring chemistry.
- C2-5 (5.50): Species assignment error (GsiABCD is E. coli, not P. aeruginosa), unverified QS regulation of GSH import, and contested GPX4 Km make this too underspecified for productive evolution.

---

*Ranking completed: 2026-03-18 | Ranker: Sonnet 4.6*
