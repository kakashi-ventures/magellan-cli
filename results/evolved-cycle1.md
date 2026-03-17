# Evolved Hypotheses — Cycle 1
# Session: 2026-03-17-scout-002
# Fields: Active Matter Topological Defects x Stem Cell Niche Architecture

---

## E1: Activity-Dependent Crypt Fission Is Triggered When Local Epithelial Contractility Exceeds the Nematic Defect-Splitting Threshold

**Evolved from**: H4 (Crypt Fission = Defect Splitting) via **Specification + Combination with H1**

**Connection**: Active nematic defect splitting instability → activity threshold crossing via myosin II → crypt fission initiation

**Mechanism**: In 2D active nematics, a +1/2 defect becomes unstable to splitting when the active stress alpha exceeds a critical value alpha_c ~ K/R^2, where K is the Frank elastic constant of the cell layer and R is the defect core radius (Giomi et al. 2014). If each intestinal crypt sits at a +1/2 topological defect (per H1), then crypt fission maps directly to this instability: when local epithelial contractility (set by myosin II activity, which is regulated by the Rho-ROCK pathway) exceeds the critical threshold, the +1/2 defect at a given crypt opening splits into two +1/2 defects that repel each other, nucleating two daughter crypts.

The critical active stress alpha_c can be estimated. In epithelial monolayers, the Frank elastic constant K is approximately 10-100 nN (from cell-cell junction elasticity measurements, Duclos et al. 2017). The defect core radius R for intestinal crypt openings is approximately 10-20 um (half the crypt opening diameter of 20-40 um). This gives alpha_c ~ K/R^2 ~ 10-100 nN / (10-20 um)^2 ~ 25-1000 Pa. Active stress in MDCK monolayers is ~50-500 Pa (Blanch-Mercader 2021), so intestinal epithelium at homeostasis likely sits near but below alpha_c. Local increases in contractility — from Rho activation during regeneration, growth factor signaling during postnatal development, or inflammation — could push alpha above alpha_c, triggering fission.

Three quantitative predictions: (1) Crypt fission rate should correlate with local phospho-myosin-light-chain (pMLC) intensity at the crypt opening — measurable by immunostaining in intestinal sections. Crypts with higher pMLC should have higher fission probability. (2) Blebbistatin treatment (reducing alpha below alpha_c) should block crypt fission even in the presence of elevated Wnt/R-spondin. Dose-response: at alpha/alpha_c < 1, fission probability should drop to near-zero, regardless of growth factor levels. This distinguishes the defect model from purely molecular models. (3) During fission, the two daughter crypt openings should initially be oriented along the tissue's nematic director (the dominant cell alignment axis), NOT randomly. The angle between the fission axis and the nematic director should be <30 degrees for >70% of fission events. This is a signature unique to the defect-splitting mechanism.

**Lineage**: H4 (mechanism) + H1 (crypt-defect identity) → Unified with quantitative threshold
**Why stronger than parent**: Quantifies the critical threshold (alpha_c ~ K/R^2), provides numerical estimates for intestinal tissue, adds pMLC correlation as a new testable prediction, and unifies H1 and H4 into a single coherent framework.

**Confidence**: 6/10 (up from 5) — The quantitative framework makes the hypothesis more falsifiable and the parameter estimates are in a plausible range.
**Groundedness**: MEDIUM — Defect splitting theory: GROUNDED. K values: GROUNDED (Duclos 2017). alpha_c estimation: PARAMETRIC (correct dimensional analysis, uncertain numerical coefficients). pMLC-fission correlation: TESTABLE prediction.

---

## E2: Wound-Induced Topological Defects Serve as Transient Stem Cell Attractors That Become Permanent Niches When Pinned by ECM Stiffness Gradients

**Evolved from**: H8 (Wound Defects -> Niche Reformation) via **Specification**

**Connection**: Wound-edge nematic alignment → transient +1/2 defects at boundary features → compressive stress activating YAP/TAZ-dependent stemness → defect pinning by ECM stiffness heterogeneity → permanent new niche

**Mechanism**: When epithelial tissue is wounded, cells at the wound edge collectively polarize and migrate toward the wound center. This creates a nematic alignment field with the director oriented perpendicular to the wound edge. At geometric irregularities of the wound boundary (convex protrusions, sharp corners), the alignment field cannot smoothly adapt, generating +1/2 topological defects. These defects are initially transient — they move, annihilate in pairs, and reorganize as the wound geometry changes during healing.

However, some defects become "pinned" when they encounter regions of elevated ECM stiffness. In liquid crystal physics, defect pinning occurs when the elastic energy cost of moving the defect through a stiffness heterogeneity exceeds the defect's kinetic energy (Kleman & Lavrentovich, 2003). In biological tissue, wound healing generates ECM stiffness gradients (fibrosis, collagen deposition, crosslinking by LOX family enzymes). When a migrating defect reaches a stiffness boundary where the tissue transitions from normal (~1 kPa) to fibrotic (~10-50 kPa), the energy barrier for defect passage is approximately delta_E ~ K * ln(kappa_fibrotic/kappa_normal) per unit length, where kappa is the local Frank constant (proportional to substrate stiffness via cell-substrate adhesion). For a 10x stiffness increase, delta_E ~ K * 2.3 ~ 20-230 nN * um. The thermal fluctuation energy at cellular scale is ~kT ~ 4 pN*nm — negligible. The pinning is therefore robust.

At each pinned +1/2 defect, two processes establish a new stem cell niche: (1) compressive stress (~100-500 Pa) at the defect core activates YAP cytoplasmic retention (low mechanical signaling), which in intestinal cells promotes Lgr5 expression and stemness (Yui et al. 2018). (2) The converging flow pattern at the defect concentrates wound-secreted R-spondin (which signals through LGR5 to potentiate Wnt) at the defect core. R-spondin is partially membrane-tethered (via GPI anchors), giving it an effective diffusion coefficient of ~1-5 um^2/s rather than the ~10 um^2/s of freely diffusing factors, making advective concentration meaningful (enhancement factor ~1.5-3x for D ~ 1-5 um^2/s).

Specific predictions: (1) In full-thickness wound healing (e.g., mouse ear punch model), map cell orientation (nematic director field) at days 3, 5, 7 post-wounding. +1/2 defect positions should coincide with subsequent hair follicle neogenesis sites (wound-induced hair neogenesis, WIHN). This is testable because WIHN is well-documented in large mouse wounds (Ito et al. 2007) and the follicle positions are measurable. (2) LOX inhibitor treatment (BAPN, reducing collagen crosslinking and fibrosis) should prevent defect pinning, leading to fewer and more randomly positioned new follicles. (3) Chronic wounds (which maintain wound-edge topology for extended periods) should accumulate more pinned defects, increasing the number of persistent stemness-activating sites and contributing to Marjolin's ulcer cancer risk.

**Lineage**: H8 → Specified with ECM stiffness pinning mechanism, R-spondin as restricted-diffusion morphogen, wound-induced hair neogenesis as test system
**Why stronger than parent**: Names specific ECM mechanism (LOX-mediated crosslinking), quantifies pinning energy, identifies R-spondin as the morphogen with restricted diffusion (addresses Critic's question from H6), and provides the WIHN model as a concrete experimental system.

**Confidence**: 6/10 (up from 5) — The WIHN experimental system provides a direct test, and the defect pinning physics is well-established.
**Groundedness**: MEDIUM-HIGH — Wound-edge nematic alignment: GROUNDED. Defect pinning: GROUNDED (liquid crystal physics). ECM stiffening in wound healing: GROUNDED. LOX in collagen crosslinking: GROUNDED. R-spondin GPI anchor: GROUNDED. WIHN: GROUNDED (Ito 2007). Defect-WIHN correspondence: SPECULATIVE (the novel claim).

---

## E3: Nematic Defects Template Restricted-Diffusion Morphogen Maxima That Set the Pre-Pattern for Signaling Center Spacing in Curved Epithelia

**Evolved from**: H6 (Defect Morphogen Concentration) via **Specification + Mutation** (replacing free diffusion with restricted diffusion as default; adding curvature coupling)

**Connection**: Active nematic defects on curved epithelial surfaces → advective concentration of membrane-tethered morphogens (R-spondin, Shh via cytonemes) → signaling center pre-patterning

**Mechanism**: The Critic's key attack on H6 was that concentration enhancement is negligible for freely diffusing morphogens. This evolved version addresses that directly: the hypothesis now specifically targets RESTRICTED-DIFFUSION morphogens — those that are membrane-tethered, lipid-modified, or transported via cytonemes.

Key morphogens with restricted diffusion: (a) R-spondin family (RSPO1-4): GPI-anchored, effective D ~ 1-5 um^2/s, critical for Wnt potentiation in intestinal stem cells. (b) Shh (Sonic hedgehog): lipid-modified (cholesterol + palmitoyl), transported on cytonemes with effective D ~ 0.5-2 um^2/s. (c) Wnt3a: palmitoylated, requires Wntless for secretion, often transported on cytonemes or exosomes rather than free diffusion.

On curved surfaces (villus, hair follicle, lung airway), Gaussian curvature couples to defect positions — defects are attracted to regions of like-sign curvature (positive Gaussian curvature attracts +1/2 defects, negative attracts -1/2; Bowick et al. 2009). This provides an additional organizing principle: the pre-pattern of signaling centers isn't just set by active nematic defect spacing on a flat surface, but is further refined by curvature, which pins defects to specific geometric features of the tissue.

For curved intestinal villi (approximately prolate ellipsoid, positive Gaussian curvature at tip, negative at villus-crypt junction), +1/2 defects should localize at the curvature-matched positions — and these are precisely the crypt base positions where R-spondin concentration is highest. The defect-mediated advective enhancement for R-spondin (D ~ 2 um^2/s) at active flow velocities of 0.1-1 um/min over a correlation length of 50-100 um gives: c_defect/c_0 ~ 1 + v*L/D ~ 1 + (0.5 um/min * 75 um) / (2 um^2/s * 60 s/min) ~ 1 + 37.5 / 120 ~ 1.31. This 31% enhancement, combined with curvature-mediated defect pinning, creates a robust morphogen maximum without Turing instability.

The distinguishing experiment remains clean: pattern wavelength should depend on cell contractility (set alpha by titrating blebbistatin) and be independent of R-spondin degradation rate (manipulable via RSPO1 vs RSPO3, which have different half-lives). If Turing mechanism: wavelength depends on degradation rate, not contractility.

**Lineage**: H6 → Specified to restricted-diffusion morphogens only. Mutated from flat to curved surfaces (curvature coupling). Enhanced with specific morphogen identities.
**Why stronger than parent**: Addresses Critic's quantitative objection by targeting restricted-diffusion morphogens. Adds curvature coupling as a second organizing principle. Names three specific morphogens with their diffusion characteristics. Enhancement factor is now 1.31 (biologically meaningful for R-spondin) rather than the negligible 1.01 for free diffusion.

**Confidence**: 5/10 (unchanged, but now quantitatively better justified) — The restricted-diffusion condition is met by biologically important morphogens. Curvature coupling adds robustness.
**Groundedness**: MEDIUM — Active nematic flows: GROUNDED. Curvature-defect coupling: GROUNDED (Bowick 2009). R-spondin GPI anchor: GROUNDED. Shh lipid modification: GROUNDED. Enhancement calculation: PARAMETRIC (correct form, uncertain exact parameters). Villus curvature values: VERIFIABLE.

---

## Evolution Quality Check

1. **E1 vs parent H4**: Significantly stronger — adds quantitative threshold (alpha_c ~ K/R^2), numerical estimates for intestinal tissue, pMLC correlation prediction, and unifies H1+H4. PASS.

2. **E2 vs parent H8**: Significantly stronger — adds ECM pinning mechanism with energy calculation, identifies R-spondin as restricted-diffusion morphogen, provides WIHN as concrete experimental system. PASS.

3. **E3 vs parent H6**: Stronger — addresses main critique (free diffusion too weak), names specific morphogens, adds curvature coupling. PASS.

4. **Diversity check**: Three distinct bridge mechanisms:
   - E1: Myosin II-mediated activity threshold → defect splitting
   - E2: ECM stiffness gradient → defect pinning → niche establishment
   - E3: Restricted-diffusion morphogen advection at curved-surface defects
   All distinct. PASS.

5. **No incoherent crossovers**: All three are self-consistent. PASS.
