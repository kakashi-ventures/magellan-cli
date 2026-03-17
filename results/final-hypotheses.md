# Final Hypotheses — Session 2026-03-17-scout-002
# Topological Defects in Active Matter x Stem Cell Niche Architecture
# Status: SUCCESS (3/3 passed Quality Gate)

---

```
=====================================================
HYPOTHESIS 1: Organoid Symmetry Breaking Is a
Topological Defect Nucleation Event -- Predictable
by Active Nematic Theory and Controllable by
Geometric Confinement
=====================================================
CONNECTION: Active nematic physics (Poincare-Hopf
  theorem on closed surfaces) -->> Topological defect
  nucleation at mathematically required positions
  -->> Organoid bud formation at defect sites
CONFIDENCE: 6/10 -- Topological argument is
  mathematically certain; biological substrate
  (organoid nematic order) is uncertain but testable
NOVELTY: Novel (provisional -- web verification
  unavailable)
GROUNDEDNESS: Medium (5/10) -- Mathematics: GROUNDED.
  Organoid biology: GROUNDED. Connection: SPECULATIVE
  but immediately testable.
IMPACT IF TRUE: Transformative -- would provide a
  predictive, controllable framework for organoid
  engineering in regenerative medicine

MECHANISM
A spherical organoid is a 2D nematic on a sphere. By
the Poincare-Hopf theorem, a nematic on a sphere must
have total topological charge +2, typically distributed
as four +1/2 defects in the "tennis ball" configuration.
These four defect positions are where compressive stress
is maximal and where budding should initiate.

The framework is controllable: in shaped microwells
(ellipsoidal, cylindrical, toroidal), the confining
geometry changes the Euler characteristic and thus the
required defect count and positions. Prolate spheroids
should produce 2 polar buds; oblate spheroids should
produce equatorial buds. A toroidal organoid (Euler
characteristic = 0) would have NO topological defects
and thus NO spontaneous budding.

[GROUNDED: Poincare-Hopf theorem -- established
mathematics. Shaped microwell culture -- Nikolaev et
al. 2020 Nature. Organoid symmetry breaking --
standard organoid biology.]
[SPECULATIVE: Organoid cells forming nematic order.
Defect-bud correspondence.]

SUPPORTING EVIDENCE
- From Field A: Poincare-Hopf theorem guarantees
  defects on any nematic field on a closed surface
  (mathematical certainty). Tennis ball configuration
  is the ground state for nematics on spheres
  (Lubensky & Prost 1992).
- From Field C: Organoid symmetry breaking produces
  buds at seemingly stochastic positions (standard
  observation). Organoids grown in shaped microwells
  can be geometrically confined (Nikolaev et al. 2020).
- Bridge: If organoid epithelium is nematic,
  Poincare-Hopf constrains bud positions.

COUNTER-EVIDENCE & RISKS
- Organoid cells in early cysts are columnar; in-plane
  elongation may be insufficient for nematic order
- Budding may be driven by differential proliferation
  (ISC vs transit-amplifying cells), not defect mechanics
- Tennis ball configuration requires specific elastic
  anisotropy that may not hold in cell monolayers
- Variable bud numbers (1-4) in real organoids may
  reflect defect merging (+1/2 pairs merging to +1)
  or insufficient nematic order

HOW TO TEST
1. Grow intestinal organoids in spherical, ellipsoidal,
   and toroidal microwells. Image cell orientation via
   confocal at the moment of symmetry breaking.
   Expected if TRUE: 4 buds on sphere, 2 polar buds
   on prolate, 0 buds on torus.
   Expected if FALSE: Bud number/position uncorrelated
   with geometry.
2. Map nematic director field of organoid epithelium
   using cell body elongation analysis. Locate defect
   positions. Overlay with bud initiation sites.
3. Effort: 3-6 months, standard organoid lab +
   microwell fabrication. Cost: ~$20-50K.
=====================================================
```

---

```
=====================================================
HYPOTHESIS 2: Activity-Dependent Crypt Fission Is
Triggered When Local Epithelial Contractility Exceeds
the Nematic Defect-Splitting Threshold
=====================================================
CONNECTION: Active nematic defect splitting instability
  (Giomi et al. 2014) -->> Myosin II contractility
  exceeding critical threshold alpha_c ~ K/R^2
  -->> Intestinal crypt fission initiation
CONFIDENCE: 6/10 -- Physics well-established;
  application to intestinal tissue is novel
  extrapolation with plausible parameters
NOVELTY: Novel (provisional -- web verification
  unavailable)
GROUNDEDNESS: Medium (5/10) -- Defect splitting
  theory: GROUNDED. K values: GROUNDED (Duclos 2017).
  Intestinal application: SPECULATIVE.
IMPACT IF TRUE: High -- would establish mechanical
  physics trigger for a fundamental growth process,
  with implications for CRC (colorectal cancer shows
  increased crypt fission)

MECHANISM
In 2D active nematics, a +1/2 defect becomes unstable
to splitting when active stress alpha exceeds alpha_c
~ K/R^2 (Giomi et al. 2014). If intestinal crypts sit
at +1/2 defects, crypt fission maps to this instability.

Estimated parameters: Frank elastic constant K ~ 10-100
nN (from cell-cell junction elasticity, Duclos et al.
2017). Defect core radius R ~ 10-20 um (half crypt
opening diameter). This gives alpha_c ~ 25-1000 Pa.
Active stress in epithelial monolayers is ~50-500 Pa
(Blanch-Mercader 2021), placing intestinal epithelium
near but below threshold at homeostasis.

Local increases in contractility -- via Rho-ROCK
activation during regeneration, postnatal growth, or
inflammation -- push alpha above alpha_c, triggering
fission. The fission axis aligns with the nematic
director.

[GROUNDED: Defect splitting instability -- Giomi 2014.
Frank constants -- Duclos 2017. Active stress range --
Blanch-Mercader 2021. Rho-ROCK in epithelial
contractility -- standard cell biology.]
[SPECULATIVE: Intestinal epithelium as nematic.
Crypt = defect.]

SUPPORTING EVIDENCE
- From Field A: Defect splitting instability in active
  nematics is a well-characterized theoretical and
  experimental phenomenon (Giomi 2014, DeCamp 2015).
- From Field C: Crypt fission is the primary mechanism
  for expanding crypt number during postnatal intestinal
  growth and regeneration. The trigger mechanism is
  poorly understood.
- Bridge: Myosin II contractility (measurable via pMLC)
  as the activity parameter crossing the splitting
  threshold.

COUNTER-EVIDENCE & RISKS
- Crypt fission occurs in organoids grown in Matrigel
  without clear nematic order -- suggesting fission CAN
  occur without defect dynamics
- 2D nematic theory may not apply to the 3D crypt
  geometry
- ISC neutral drift dynamics may fully explain fission
  (stochastic stem cell population reaching critical
  size), making mechanical trigger unnecessary
- Intestinal epithelium nematic order is unverified

HOW TO TEST
1. pMLC immunostaining of mouse intestinal sections.
   Quantify pMLC intensity at crypt openings. Correlate
   with fission events (identified by morphology).
   Expected if TRUE: Higher pMLC at fissioning crypts.
2. Blebbistatin treatment of intestinal organoids with
   Wnt/R-spondin supplementation. Dose-response curve.
   Expected if TRUE: Fission blocked even with high Wnt.
   Expected if FALSE: Fission proceeds regardless of
   contractility.
3. Map nematic director field near fission events.
   Measure angle between fission axis and director.
   Expected if TRUE: <30 degrees for >70% of events.
4. Effort: 6-12 months, standard GI biology lab.
   Cost: ~$30-80K.
=====================================================
```

---

```
=====================================================
HYPOTHESIS 3: Wound-Induced Topological Defects Serve
as Transient Stem Cell Attractors That Become Permanent
Niches When Pinned by ECM Stiffness Gradients
=====================================================
CONNECTION: Wound-edge collective migration (nematic
  alignment) -->> +1/2 defect creation at boundary
  irregularities + ECM stiffness-mediated defect
  pinning (Kleman & Lavrentovich 2003) -->> Permanent
  new stem cell niche establishment at pinned sites
CONFIDENCE: 6/10 -- Best-grounded hypothesis;
  multiple independently verified components converge
  on a novel connection
NOVELTY: Novel (provisional -- web verification
  unavailable)
GROUNDEDNESS: Medium-High (6/10) -- Most individual
  claims are literature-grounded. Only the connection
  itself is speculative.
IMPACT IF TRUE: High-to-Transformative -- mechanistic
  explanation for niche positioning in regeneration +
  clinical relevance for chronic wound cancer risk

MECHANISM
When epithelial tissue is wounded, cells polarize and
migrate collectively, creating a nematic field with
director perpendicular to the wound edge. At boundary
irregularities, +1/2 defects form (geometric necessity).
These are initially transient.

Some defects become pinned at ECM stiffness gradients.
Wound healing generates stiffness transitions from
normal (~1 kPa) to fibrotic (~10-50 kPa) via LOX-
mediated collagen crosslinking. The pinning energy
(delta_E ~ K * ln(kappa_fibrotic/kappa_normal)) far
exceeds thermal noise, making pinning robust.

At pinned +1/2 defects: (1) compressive stress
activates YAP cytoplasmic retention, promoting Lgr5
expression and stemness (Yui et al. 2018); (2)
converging flow concentrates wound-secreted R-spondin
(GPI-anchored, D ~ 1-5 um^2/s) at the defect core,
enhancing concentration by ~1.5-3x.

The wound-induced hair neogenesis (WIHN) model (Ito
et al. 2007) provides a direct test: new hair
follicles that form in large mouse wounds should
correspond to pinned defect positions.

[GROUNDED: Wound-edge nematic alignment -- Reffay 2014,
Basan 2013. Defect pinning -- Kleman & Lavrentovich
2003. ECM stiffening -- standard wound biology. LOX
crosslinking -- standard. R-spondin GPI anchor --
published. WIHN -- Ito 2007. YAP in stemness -- Yui
2018.]
[SPECULATIVE: Defect-niche correspondence at wound
sites. Defect pinning in biological tissue.]

SUPPORTING EVIDENCE
- From Field A: Wound-edge collective migration creates
  measurable nematic alignment (Reffay 2014). Defect
  pinning by substrate heterogeneity is well-established
  in liquid crystal physics (Kleman & Lavrentovich).
- From Field C: WIHN is well-documented -- new follicles
  form at specific positions in large mouse wounds (Ito
  2007). Niche positioning during regeneration is poorly
  understood.
- Bridge: ECM stiffness gradients (LOX-mediated) as the
  pinning mechanism that converts transient wound defects
  into permanent niche positions.

COUNTER-EVIDENCE & RISKS
- SDF-1/CXCR4 chemotaxis may fully explain stem cell
  recruitment, making defect positioning unnecessary
- The distinction between recruitment (chemotaxis) and
  positioning (defects) may be artificial
- Wound healing may be too chaotic for well-defined
  nematic defects
- Marjolin's ulcer has many other risk factors
  (chronic inflammation, immune suppression)

HOW TO TEST
1. Mouse ear punch wound model. Map cell orientation
   at days 3, 5, 7 post-wounding. Identify +1/2
   defect positions. Track WIHN follicle formation.
   Expected if TRUE: Follicle positions coincide with
   defect positions identified at day 3-5.
2. LOX inhibitor (BAPN) treatment during wound healing.
   Expected if TRUE: Fewer follicles, more randomly
   positioned (defect pinning prevented).
   Expected if FALSE: Follicle number and position
   unchanged.
3. Retrospective analysis of chronic wound histology
   for persistent nematic defects near tumor sites.
4. Effort: 6-12 months, wound healing lab + imaging
   analysis pipeline. Cost: ~$40-100K.
=====================================================
```

---

## Pipeline Statistics

- Total hypotheses generated: 15 (8 cycle 1 + 7 cycle 2)
- Killed by Critic: 6 (40% kill rate)
- Survived critique: 9
- Ranked and selected for Quality Gate: 3
- Passed Quality Gate: 3
- Overall attrition: 80% (15 generated -> 3 final)
- Distinct bridge mechanisms in final set: 3
  1. Spherical nematic topology (C2-4)
  2. Myosin II activity threshold / defect splitting (E1)
  3. ECM stiffness-mediated defect pinning (E2)
