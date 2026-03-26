# Hypothesis Rankings — Cycle 1

**Session:** 2026-03-26-targeted-001
**Fields:** Mechanobiology (ECM stiffness) x Epigenomics (genomic enhancer regulation)
**Ranker model:** claude-sonnet-4-6
**Date:** 2026-03-26
**Hypotheses evaluated:** 4 surviving (H3 killed by Critic)

---

## Per-Hypothesis Scoring Tables

### Hypothesis H1: Stiffness-Dependent Super-Enhancer Nucleation via YAP-Recruited BRD4-MED1 Phase Condensates

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 5 | Zanconato et al. (Nat Med 2018) directly demonstrated that YAP/TAZ/TEAD recruits BRD4 to super-enhancers in breast cancer, which the Critic confirmed is not cited. The stiffness trigger as upstream activator (rather than oncogenic transformation) is a meaningful but single-degree novelty increment — the conceptual space is already occupied. PubMed co-occurrence confirms zero papers for "ECM stiffness + H3K27ac" or "matrix stiffness + super-enhancer," which preserves some novelty at the experimental level, but the core mechanistic claim is partially pre-empted. |
| Mechanistic Specificity | 20% | 8 | Exemplary specificity: names ITGB1, PTK2/FAK, LATS1/2, YAP1, TEAD1, EP300, BRD4, MED1 with STRING scores attached; provides the phase separation critical concentration (~100-300 nM from Sabari 2018); predicts Hill coefficient >2 as a quantitative diagnostic; specifies the ROSE algorithm for super-enhancer calling. The only gap is an in vivo quantitative estimate of BRD4 local concentration at TEAD-clustered loci, which the Critic's questions flag as missing. |
| Cross-field Distance | 10% | 4 | Mechanobiology (integrin/FAK/YAP) and enhancer epigenomics (BRD4/MED1/H3K27ac) are adjacent fields within cell and molecular biology that share investigators, journals, and methodology. The phase separation layer adds biophysics, but all three sub-communities operate within a shared life-sciences infrastructure. Not a cross-disciplinary leap. |
| Testability | 20% | 7 | PAA hydrogel stiffness gradients, H3K27ac ChIP-seq with ROSE algorithm, and BRD4 ChIP-seq are fully established methods available at any well-equipped epigenomics lab. The hexanediol condensate test is non-specific (Critic flagged this) and the more rigorous OptoDroplet/Corelet alternative requires specialized reagents, adding cost and time. Core experiment is PhD-feasible in 4-5 months; condensate-specificity test adds another 2-3 months. |
| Impact | 10% | 6 | Establishing ECM stiffness as a trigger for the typical-to-super-enhancer transition would connect the mechanobiology and super-enhancer literatures and has implications for fibrosis and mechanically driven cancer progression. However, the mechanistic novelty is limited given Zanconato 2018 — the conceptual advance is the stiffness input, not the super-enhancer output, which is already known in the cancer context. |
| Groundedness | 20% | 5 | The YAP/FAK/LATS cascade and BRD4/MED1 condensates at super-enhancers are correctly cited from established literature. However: (1) Zanconato 2018 is absent — the most directly relevant grounding paper is missing; (2) the in vitro critical concentration (100-300 nM) is misapplied as an in vivo threshold when the original paper cautioned against this; (3) TEAD1-EP300 STRING score of 0.537 is medium-low and represents a weak link in the chain. Critic independently estimated ~60% grounded; score reflects this. |
| **Composite** | | **6.00** | 0.20×5 + 0.20×8 + 0.10×4 + 0.20×7 + 0.10×6 + 0.20×5 = 1.00 + 1.60 + 0.40 + 1.40 + 0.60 + 1.00 |

---

### Hypothesis H2: Coordinated Bivalent-to-Active Enhancer Conversion via Dual ECM-Stiffness-Controlled Enzymes (KDM6B + EP300)

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 7 | No paper has combined stiffness-controlled KDM6B with stiffness-controlled EP300 at enhancers. Yu 2025 covers KDM6B at promoters in thyroid cancer; Whitworth 2024 covers EP300 under shear stress — neither combines them nor studies enhancers under ECM stiffness gradients. The "stiffness as upstream coordinator of two convergent enzymes acting on the same residue" framing is genuinely novel. The bivalent-to-active concept itself is canonical developmental biology (Rada-Iglesias 2011), but the mechanical trigger is unexplored. |
| Mechanistic Specificity | 20% | 7 | Names both enzymes (KDM6B, EP300), the target residue (H3K27), the mutual exclusivity biochemistry, specific inhibitors (GSK-J4 5 uM, A-485 3 uM), developmental gene loci (RUNX2, SOX9, PPARG), and a cell type (MSCs on PAA). The temporal asynchrony issue (EP300 fast, KDM6B slow) is acknowledged. The specificity of KDM6B vs UTX at enhancers is unresolved, representing the mechanism's main ambiguity. Genetic experiments (siKDM6B/siKDM6A) are recommended by the Critic as mandatory revisions. |
| Cross-field Distance | 10% | 4 | Mechanobiology + developmental epigenomics. Both fields fall within cell and molecular biology; the bridge is between extracellular mechanical sensing and nuclear epigenome reprogramming. The developmental epigenomics angle (bivalent enhancers, lineage commitment) adds a dimension not present in H1 or H5, but the disciplinary gap remains within life sciences. |
| Testability | 20% | 7 | CUT&Tag for H3K27me3/H3K27ac/H3K4me1, sequential re-ChIP at candidate loci, and pharmacological inhibition with GSK-J4/A-485 are all established in primary MSCs. Bone marrow MSCs from Lonza are commercially available. The main complication is CBP compensation (unaddressed in the protocol), and the need for genetic knockdowns (siKDM6B vs siKDM6A) adds experimental complexity. Core experiment is PhD-feasible in 3-4 months with available tools. |
| Impact | 10% | 7 | Establishing that ECM stiffness governs developmental potential through coordinated bivalent enhancer switching would directly explain how mechanical niche signals prime stem cell epigenomes for lineage commitment. This has strong translational value for regenerative medicine, tissue engineering, and understanding pathological fibrosis where stiffness drives aberrant differentiation. The dual-enzyme coordination principle, if confirmed, would be a significant mechanistic advance. |
| Groundedness | 20% | 6 | KDM6B stiffness-responsiveness is directly grounded in Yu 2025 (though in thyroid cancer, not MSCs — an extrapolation the Critic flags). Bivalent enhancers are grounded in Rada-Iglesias 2011. H3K27me3/H3K27ac mutual exclusivity is canonical biochemistry. EP300's role under mechanical stimuli is supported by Whitworth 2024 (shear stress, not stiffness). The core novel claim — coordinated KDM6B + EP300 activity at distal enhancers under stiffness — is parametric, and KDM6B's preference for promoters over enhancers is an unresolved concern. Critic estimated ~65-70% grounded. |
| **Composite** | | **6.50** | 0.20×7 + 0.20×7 + 0.10×4 + 0.20×7 + 0.10×7 + 0.20×6 = 1.40 + 1.40 + 0.40 + 1.40 + 0.70 + 1.20 |

---

### Hypothesis H4: LAD-Embedded Enhancers as Stiffness-Resistant Mechanical Selectivity Filter

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 7 | Sun 2020 established the interior/periphery differential at the gene level; extending this specifically to enhancers as a "selectivity filter" is an untested step. No paper has asked whether LAD-embedded enhancers are stiffness-resistant while their non-LAD counterparts are stiffness-responsive, nor proposed this as a mechanism for mechanical gene selectivity. The lamin A/C reinforcement angle (stiff ECM -> more lamin A/C -> tighter LAD anchoring -> enhanced filter) adds a novel regulatory layer on top of Sun 2020. The Critic confirms novelty holds. |
| Mechanistic Specificity | 20% | 7 | Names lamin A/C, lamin B1, LAP2beta, emerin, H3K9me2/3, LAD boundaries (constitutive vs facultative), specific publications for each claim, siLMNA as the perturbation, and ENCODE data sources for LAD maps. Predicts >90% of stiffness-responsive enhancers in non-LAD compartment (though the Critic correctly notes this needs comparison to the ~65% null expectation). The mechanism integrates two independently grounded systems without requiring new molecular interactions — a hallmark of high-quality specificity. |
| Cross-field Distance | 10% | 5 | Mechanobiology + 3D nuclear organization/epigenomics. The LAD/nuclear architecture literature (van Steensel lab, Swift/Discher lab) and the mechanobiology literature are more separated than typical epigenomics subcommunities — they attend different conferences and use different primary methods (DamID vs ChIP-seq vs atomic force microscopy). The bridge between physical ECM properties and nuclear compartmentalization is a meaningful cross-community connection, scoring slightly above the other hypotheses. |
| Testability | 20% | 9 | The most testable hypothesis in the set. The experiment requires only H3K27ac CUT&Tag + lamin B1 CUT&RUN (both standard) plus computational overlay with publicly available ENCODE LAD maps. No specialized equipment, no exotic reagents. The siLMNA rescue experiment is standard molecular biology. A motivated PhD student could complete the primary experiment in 3 months and the siLMNA validation in another 4-6 weeks. The Critic identified this as the strongest hypothesis precisely because of its experimental accessibility. |
| Impact | 10% | 8 | If true, this would explain a long-standing puzzle: why does YAP nuclear localization activate only a subset of genes with TEAD binding sites? The LAD filter answer — "because some TEAD enhancers are locked in LADs regardless of YAP activity" — would reframe how we think about mechanical gene regulation and cell-type specificity. It would have immediate implications for understanding which genes can be mechanically reprogrammed (relevant to fibrosis, cancer, development, and tissue engineering). The concept of the mechanical response repertoire being jointly encoded by ECM stiffness AND nuclear architecture is a genuinely conceptual advance. |
| Groundedness | 20% | 7 | The best-grounded hypothesis in the set. LAD biology is built on foundational papers: Guelen et al. Nature 2008 (DamID), Kind et al. Cell 2015 (LAD repressive environment), Peric-Hupkes et al. Mol Cell 2010 (LAD dynamics during differentiation). Swift et al. Science 2013 (lamin A scales with tissue stiffness) is one of the most cited papers in nuclear mechanobiology. Sun 2020 (interior genes respond to force, periphery genes resist) is directly relevant and grounded. The only parametric element is the inference that increased lamin A/C expression directly reinforces H3K9me3 at existing LADs — a mechanistically reasonable but unverified claim. Critic explicitly confirmed all grounded claims and rated groundedness as correctly assessed. |
| **Composite** | | **7.30** | 0.20×7 + 0.20×7 + 0.10×5 + 0.20×9 + 0.10×8 + 0.20×7 = 1.40 + 1.40 + 0.50 + 1.80 + 0.80 + 1.40 |

---

### Hypothesis H5: Enhancer-Encoded Mechanical Memory via Self-Reinforcing H3K27ac-BRD4-EP300 Positive Feedback

| Dimension | Weight | Score (1-10) | Justification |
|-----------|--------|-------------|---------------|
| Novelty | 20% | 7 | Yang et al. Nat Mater 2014 attributed mechanical memory to YAP nuclear retention, not to histone marks. Hsia 2023 proposed chromatin-level memory conceptually but without experimental data. No paper has conducted a stiff-to-soft transfer experiment with time-course H3K27ac CUT&Tag at enhancer resolution, nor proposed EP300-BRD4 positive feedback as the specific memory mechanism. This is the most experimentally and mechanistically novel framing of mechanical memory in the set. |
| Mechanistic Specificity | 20% | 7 | Names EP300, BRD4, H3K27ac, HDAC activity, BRD4 bromodomain Kd values (~1-10 uM monovalent), EP300-BRD4 STRING score (0.988); provides specific timepoints (0, 6, 12, 24, 48, 72 hr), inhibitor doses (JQ1 500 nM, SAHA 1 uM), and a quantitative prediction (half-life 24-72 hr, collapsible to <6 hr by JQ1). The Critic's mandatory revision is to lower the predicted half-life to 6-24 hr based on H3K27ac turnover kinetics, which would refine but not eliminate the mechanistic specificity. |
| Cross-field Distance | 10% | 4 | Mechanobiology + chromatin biochemistry/epigenetic memory. This falls within the same disciplinary cluster as the other hypotheses. The positive feedback loop concept borrowed from heterochromatin maintenance (HP1/SUV39H1) adds a chromatin biophysics angle, but the methodological and conceptual communities substantially overlap. |
| Testability | 20% | 7 | The stiff-to-soft transfer design with time-course CUT&Tag is elegant and technically feasible. JQ1 and SAHA are widely available. YAP immunofluorescence for nuclear localization is routine. The primary complication is the interpretation ambiguity identified by the Critic: SAHA extends H3K27ac globally (not specifically via the BRD4-EP300 loop), and transcription-dependent H3K27ac maintenance is a confound that requires a triptolide control. These additions increase the experiment's duration to ~5-6 months but remain within standard capabilities. |
| Impact | 10% | 6 | Mechanical memory at the enhancer epigenome level would be impactful for understanding fibrosis (cells that "remember" having been in a stiff matrix continue expressing profibrotic genes even after returning to softer tissue), cancer invasion, and tissue engineering. However, the Yang 2014 mechanical memory paper already exists and the field has moved on. The enhancement is the enhancer-resolution mechanism, which is valuable but not transformative — it explains the molecular basis of a phenomenon already described phenotypically. |
| Groundedness | 20% | 5 | BRD4 bromodomain function (Filippakopoulos 2010) and EP300-BRD4 interaction (STRING 0.988) are grounded. YAP rapid relocalization on soft substrates (Dupont 2011) is grounded. The critical mechanistic claim — that BRD4 maintains locus-specific EP300 targeting after YAP departure — is parametric; BRD4 is a general reader that occupies thousands of enhancers, so locus-specific EP300 retention via BRD4 is an inference not supported by direct evidence. The Zheng 2019 H3K27ac turnover citation is approximate (Critic flagged as unverified in blind mode). Most importantly, the predicted 24-72 hr memory half-life is quantitatively inconsistent with the measured 2-6 hr H3K27ac turnover — this is a grounding failure for the central quantitative claim. |
| **Composite** | | **6.20** | 0.20×7 + 0.20×7 + 0.10×4 + 0.20×7 + 0.10×6 + 0.20×5 = 1.40 + 1.40 + 0.40 + 1.40 + 0.60 + 1.00 |

---

## Cross-Domain Bonus Assessment

This session bridges mechanobiology (extracellular matrix mechanics) and epigenomics (genomic enhancer regulation). Both fields reside within the life sciences cluster — they share investigators, publication venues (Nature Cell Biology, Cell, Molecular Cell), and experimental infrastructure (fluorescence microscopy, ChIP-seq, cell culture). The distance is meaningful (mechanobiology is more biophysical; epigenomics more molecular), but it does not cross 2+ disciplinary boundaries as required for the +0.5 bonus (e.g., materials science to neuroscience, topology to developmental biology). **No cross-domain bonus applied to any hypothesis.**

---

## Summary Scoring Table

| ID | Title | Novelty (20%) | Mech. Spec. (20%) | Cross-field (10%) | Testability (20%) | Impact (10%) | Groundedness (20%) | Composite |
|----|-------|--------------|-------------------|-------------------|-------------------|--------------|-------------------|-----------|
| H4 | LAD-Embedded Enhancers as Stiffness-Resistant Mechanical Selectivity Filter | 7 | 7 | 5 | 9 | 8 | 7 | **7.30** |
| H2 | Coordinated Bivalent-to-Active Enhancer Conversion (KDM6B + EP300) | 7 | 7 | 4 | 7 | 7 | 6 | **6.50** |
| H5 | Enhancer-Encoded Mechanical Memory via EP300-BRD4 Positive Feedback | 7 | 7 | 4 | 7 | 6 | 5 | **6.20** |
| H1 | Stiffness-Dependent Super-Enhancer Nucleation via YAP-BRD4-MED1 Condensates | 5 | 8 | 4 | 7 | 6 | 5 | **6.00** |

---

## Diversity Check

After scoring, all 4 surviving hypotheses are examined for mechanistic clustering:

| ID | Primary Mechanism |
|----|------------------|
| H4 | Lamin A/C -> LAD geometry filter (nuclear architecture, emergent property from two grounded systems) |
| H2 | KDM6B + EP300 coordinated dual enzyme action (bivalent-to-active, developmental epigenomics) |
| H5 | EP300 -> BRD4 -> EP300 positive feedback (self-reinforcing circuit) |
| H1 | YAP -> BRD4 phase condensate nucleation (phase separation biophysics bridge) |

**Mechanism overlap assessment:**

- H4 vs H2: Different. H4 is about which enhancers can respond (nuclear architecture filter); H2 is about how bivalent enhancers are converted. No shared bridge.
- H4 vs H5: Different. H4 is a selectivity filter; H5 is a temporal persistence mechanism.
- H4 vs H1: Different. H4 involves lamin/LAD biology; H1 is about phase condensates at YAP targets.
- H2 vs H5: Partially overlapping — both involve EP300 activity, but H2 coordinates it with KDM6B for mark conversion while H5 uses EP300-BRD4 feedback for mark persistence. They address different aspects of the same molecular actor.
- H2 vs H1: Partially overlapping — both involve YAP as upstream input and EP300 as the writer, but H2's distinguishing element is KDM6B and developmental enhancers; H1's distinguishing element is BRD4 condensates and super-enhancers.
- H1 vs H5: Overlapping upstream (both YAP -> EP300 -> BRD4), but H1 predicts a qualitative stiffness-dependent switch while H5 predicts temporal persistence after stiffness removal.

**Convergence verdict:** H1 and H5 share the most mechanistic territory (both depend on YAP-EP300-BRD4 as the core axis). However, they address different biological questions (switch vs persistence) and make orthogonal experimental predictions. The top 3 (H4, H2, H5) represent genuinely distinct mechanisms: nuclear architecture filter, dual-enzyme bivalent conversion, and feedback-mediated memory. No diversity adjustment is needed; the ranking already places the most mechanistically distinct hypothesis (H4) first.

**No diversity bonus applied.** The top 3 represent three non-redundant mechanistic routes.

---

## Elo Tournament Sanity Check

With 4 hypotheses, there are 6 pairwise comparisons (4x3/2 = 6). For each pair, the question is: which hypothesis would a senior faculty reviewer at a research-intensive university choose to test first, and why?

### Pairwise Comparisons

**H4 vs H2:**
H4 wins. A senior reviewer would choose H4 first because it is both more testable (primarily computational overlay with existing data + one CUT&Tag experiment) and more conceptually parsimonious. H2 requires resolving the KDM6B vs UTX ambiguity, temporal asynchrony, and CBP compensation issues before the central claim can be interpreted. H4's experimental path is cleaner and could yield interpretable data within a single graduate student rotation. **H4 wins.**

**H4 vs H5:**
H4 wins. H4's quantitative predictions are grounded in known biology (LAD positions, lamin A/C scaling), while H5's key prediction (24-72 hr memory half-life) is in quantitative tension with measured H3K27ac turnover (2-6 hr). Even after the Critic's mandatory revision to 6-24 hr, the expected effect may be difficult to distinguish from simple HDAC-mediated decay. H4 has a cleaner expected effect size and cleaner falsification. **H4 wins.**

**H4 vs H1:**
H4 wins. H1 is partially pre-empted by Zanconato 2018 and has the weakest novelty score. A senior reviewer would ask "what does this add beyond what we already know about YAP and super-enhancers?" before committing resources. H4 asks a question with no existing answer. **H4 wins.**

**H2 vs H5:**
H2 wins. Both share EP300 as a key actor, but H2's claim is more robust to revision — the KDM6B vs UTX question has a definitive experimental answer (siRNA knockdown), whereas H5's central quantitative prediction may simply be wrong given H3K27ac turnover kinetics. H2's impact score is also higher (direct developmental implications for MSC lineage commitment). A reviewer interested in stem cell biology would prioritize H2. **H2 wins.**

**H2 vs H1:**
H2 wins. H2 addresses developmental enhancers with a novel dual-enzyme framing while H1 is partially pre-empted by Zanconato 2018 and relies on contested phase separation biology. H2's novelty claim is stronger, its impact on regenerative medicine is more direct, and its experimental path (though complex) does not depend on resolving the phase separation debate. **H2 wins.**

**H5 vs H1:**
H5 wins. H5's novelty is intact (no direct precedent for enhancer-level mechanical memory with H3K27ac time-course), while H1 must grapple with Zanconato 2018. A reviewer would prefer H5 because the experiment (stiff-to-soft transfer with CUT&Tag time-course) is definitive even if the quantitative predictions are wrong — the data would be informative regardless of outcome. H1's key experiment (distinguishing phase-separated condensates from cooperative binding) is technically harder and more ambiguous in interpretation. **H5 wins.**

### Elo Win Tally

| Hypothesis | Wins | Losses | Win Rate | Elo Rank |
|-----------|------|--------|----------|----------|
| H4 | 3 | 0 | 3/3 = 100% | 1st |
| H2 | 2 | 1 | 2/3 = 67% | 2nd |
| H5 | 1 | 2 | 1/3 = 33% | 3rd |
| H1 | 0 | 3 | 0/3 = 0% | 4th |

### Comparison with Linear Composite Ranking

| Rank | Linear Composite | Elo Tournament |
|------|-----------------|----------------|
| 1st | H4 (7.30) | H4 (3-0) |
| 2nd | H2 (6.50) | H2 (2-1) |
| 3rd | H5 (6.20) | H5 (1-2) |
| 4th | H1 (6.00) | H1 (0-3) |

**Elo confirms linear ranking.** Both methods produce the identical top-3 order (H4 > H2 > H5 > H1). The Elo tournament confirms that the composite score's dimension weighting correctly captured the holistic researcher judgment: H4's dominant testability and groundedness translate directly into a "test this first" preference in pairwise comparison. H1's weak novelty (penalized by Zanconato 2018 pre-emption) makes it consistently less preferred, which is consistent with its lowest composite score despite its highest mechanistic specificity score (8/10).

**Diagnostic note:** The pairwise tournament implicitly weights "interpretability of results" more heavily than the 6-dimension linear model. H4's advantage is partly that its results are unambiguous — either stiffness-responsive enhancers cluster in non-LAD regions or they do not — whereas H1 and H5 have ambiguous failure modes (cooperative binding mimics phase separation; H3K27ac decay is hard to attribute specifically to feedback loss vs passive turnover). This is an appropriate caution for the Evolver: H4's evolved versions should maintain this interpretive clarity.

---

## Final Ranking — Top 3 for Evolution (Post-Diversity-Check)

1. **H4** — LAD-Embedded Enhancers as Stiffness-Resistant Mechanical Selectivity Filter — Composite: **7.30**
   Strongest across testability (9/10), impact (8/10), and groundedness (7/10). Parsimonious mechanism. Clean falsification criteria. Highest Elo win rate (3-0). Advances.

2. **H2** — Coordinated Bivalent-to-Active Enhancer Conversion via Dual ECM-Stiffness-Controlled Enzymes (KDM6B + EP300) — Composite: **6.50**
   Highest developmental impact; novel dual-enzyme framing; requires KDM6B vs UTX clarification in evolution. Advances.

3. **H5** — Enhancer-Encoded Mechanical Memory via EP300-BRD4-EP300 Positive Feedback — Composite: **6.20**
   Genuinely novel question (enhancer-level mechanical memory); informative regardless of outcome; needs quantitative revision of memory half-life prediction (6-24 hr replacing 24-72 hr) per Critic mandate. Advances.

---

## Dropped — Cycle 1

| ID | Title | Composite | Reason |
|----|-------|-----------|--------|
| H1 | Stiffness-Dependent Super-Enhancer Nucleation via YAP-Recruited BRD4-MED1 Phase Condensates | 6.00 | Lowest composite; Zanconato 2018 substantially pre-empts core mechanistic claim reducing novelty to 5/10; phase separation biology is contested (McSwiggen 2019); weakest novelty + groundedness combination; ranked 4th by both linear composite and Elo tournament. |

---

## Notes for Evolver

**H4 evolution priorities:**
- Refine the >90% non-LAD enrichment prediction with proper null model (65% expected by chance; must demonstrate >80-85% with statistical power calculation)
- Explore the constitutive vs facultative LAD distinction — the filter may be strongest for cLADs and should be tested in a cell type with well-mapped fLADs
- Consider adding a CRISPR tethering experiment (force a non-LAD TEAD enhancer into the LAD via MS2-Lamin fusion) as a gain-of-function test

**H2 evolution priorities:**
- Add siKDM6B/siKDM6A genetic experiment alongside GSK-J4 to resolve UTX vs KDM6B specificity
- Reframe as a "sequential two-phase model" (EP300/H3K27ac first, KDM6B/H3K27me3 removal second) rather than simultaneous coordination, in line with known temporal kinetics
- Address CBP compensation by using dual EP300+CBP inhibition (A-485 at higher doses covering CBP) or genetic approaches

**H5 evolution priorities:**
- Lower predicted memory half-life to 6-24 hr (mandatory per Critic; more consistent with H3K27ac turnover kinetics)
- Add triptolide transcription-inhibitor control at transfer time to distinguish epigenetic from transcriptional memory
- Distinguish BRD4-mediated locus-specific EP300 retention from global SAHA effect by using dBET6 (BET degrader) vs JQ1 (inhibitor) comparison
