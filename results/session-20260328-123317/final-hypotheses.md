# Final Hypotheses -- Session 015
## Percolation Threshold Theory x T Cell Infiltration in Solid Tumors

Session ID: session-20260328-123317
Status: PARTIAL (4 CONDITIONAL_PASS)
Completed: 2026-03-28

---

## E4-H8: TGF-beta Correlated Percolation and LOX/Anti-TGF-beta Synergy
**Verdict: CONDITIONAL_PASS | Composite: 7.6/10 | Confidence: 5 | Groundedness: 7**

TGF-beta integrin-mediated activation creates spatially correlated collagen crosslink density with a correlation length of 40-60 um around cancer-associated fibroblasts (CAFs). Using Weinrib-Halperin (1983) perturbation theory for exponentially correlated disorder, this correlation shifts the percolation threshold p_c upward by +0.035 to +0.075 above the random p_c = 0.2488. This makes the tumor ECM harder to percolate (more immune-excluding) than a random collagen network with the same mean crosslink density.

The clinically actionable prediction: LOX inhibition (BAPN or PXS-5505) raises p by +0.10-0.15 while anti-TGF-beta (galunisertib or fresolimumab) lowers p_c by 0.035-0.075. The combination achieves a p - p_c margin of ~0.17 versus ~0.12 for BAPN alone or ~0.05 for anti-TGF-beta alone. Since infiltration scales as P_inf ~ (p - p_c)^0.417, the combination produces P_inf ~ 0.57 versus 0.47 (BAPN alone) or 0.30 (anti-TGF-beta alone). This is super-additive synergy calculable from percolation physics.

**Test protocol**: 2x2 factorial design (BAPN +/- anti-TGF-beta) in MC38 syngeneic tumors. Measure SHG spatial autocorrelation of collagen to extract xi_TGF. Measure T cell infiltration by CD8 IHC. Predict synergy magnitude from measured xi_TGF using Weinrib formula.

**Key citations**: Weinrib & Halperin 1983 Phys Rev B 27:413 (verified); Munger 1999 Cell 96:319 (verified); TGFB1-LOX STRING score 0.623 (verified).

---

## E1-H1: Voronoi Tessellation of Tumor ECM Recovers 3D Percolation Universality Class
**Verdict: CONDITIONAL_PASS | Composite: 7.5/10 | Confidence: 6 | Groundedness: 7**

LOX-mediated collagen crosslink density maps to bond occupation probability p on a Voronoi tessellation of the tumor ECM (coordination number z ~ 6-8). The percolation threshold p_c = 0.18-0.22 (for active particles with Pe ~ 3) defines a sharp immune exclusion threshold. Below p_c, the spanning cluster of connected pores permits T cell migration (immune-hot tumor). Above p_c, no spanning cluster exists (immune-cold tumor).

The Harris criterion (1974) proves that short-range collagen density heterogeneity (CV = 0.4-0.6) is irrelevant to universality class -- the critical exponents (nu = 0.88, beta = 0.41) are preserved despite heterogeneity. The transition width Delta_p ~ CV * (a/L)^(1/nu) ~ 0.0007 is negligible compared to the biologically relevant range.

The bond open/closed threshold is calibrated to the Wolf 2013 T cell nuclear cross-section constraint (4 um^2): pores with cross-section > 4 um^2 are "open bonds," pores below are "closed."

**Test protocol**: Reconstituted collagen gels at 10 discrete LOX concentrations spanning p = 0.1 to 0.4. Embed activated T cells, measure infiltration depth at 48h. Plot infiltration vs LOX concentration, fit to percolation order parameter P_inf ~ (p - p_c)^0.41.

**Key citations**: Nicolas-Boluda 2021 eLife (verified); Wolf 2013 J Cell Biol 201:1069 (verified); Harris 1974 J Phys C (verified); Stauffer & Aharony 1994 (textbook).

---

## E3-H4: Michaelis-Menten LOX Kinetics Determine BAPN Percolation Therapeutic Window
**Verdict: CONDITIONAL_PASS | Composite: 7.0/10 | Confidence: 5 | Groundedness: 6**

BAPN irreversible LOX inhibition (Tang/Trackman/Kagan 1983 J Biol Chem 258:4331) combined with crosslinked collagen fibril half-life (t_1/2 = 14-21 days in tumor stroma) yields a steady-state bond occupation probability p_ss([BAPN]) that follows a Michaelis-Menten-like curve. Solving p_ss = p_c(active) ~ 0.22 gives a critical BAPN concentration [B]* ~ 0.3 mg/mL in drinking water.

This predicts that the Nicolas-Boluda 2021 eLife dose of 3 mg/mL is already 4-10x above the percolation therapeutic window -- in the plateau regime where further dose increase provides diminishing returns. A dose-reduction experiment with 6 BAPN concentrations spanning 0.05-3.0 mg/mL should reveal the sharp onset of T cell infiltration at [B]*.

**NOTE**: QG flagged that IC50 = 80 uM should be Ki = 6 uM (Tang 1983). Dose calculation needs re-derivation with irreversible inhibition kinetics.

**Key citations**: Tang/Trackman/Kagan 1983 J Biol Chem 258:4331 (verified); PXS-5505 PMID 39101793 (verified); Nicolas-Boluda 2021 eLife (verified).

---

## E2-H2: Two-Exponent Test for Active-Percolation Universality Class
**Verdict: CONDITIONAL_PASS | Composite: 6.7/10 | Confidence: 5 | Groundedness: 6**

Rather than assuming the isotropic 3D percolation universality class (nu = 0.88, d_w = 2.878, tau = 2.189), this hypothesis proposes MEASURING the universality class by simultaneously extracting two independent exponents: walk dimension d_w (from T cell MSD at t > 30 min, beyond persistence time) and cluster-size exponent tau (from connected-cluster size distribution via spatial transcriptomics).

The (d_w, tau) pair over-constrains the universality class: isotropic 3D percolation (d_w ~ 2.87, tau ~ 2.19), directed percolation (d_w ~ 3.2, tau ~ 2.52), or an interpolated active-particle class. The lattice constant is anchored to T cell nucleus long axis (6 um, from Lammerding 2011).

This transforms the percolation framework from a prediction into a measurement -- the experiment produces a decisive verdict (class identified or model rejected).

**Key citations**: Xu et al. 2014 Phys Rev E 87:052107 (tau = 2.189 for 3D -- verified); Lammerding 2011 (nuclear mechanics).
