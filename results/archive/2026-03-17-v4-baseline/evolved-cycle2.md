# Evolved Hypotheses — Cycle 2 (Final)
## Session: 2026-03-17-scout-001

## Evolution Strategy
- E1 retained as lead hypothesis (highest score, strongest grounding)
- E3 refined with more specific molecular targets
- E2 + C2-H5 fused: circadian renewal + tissue vulnerability = "chronovulnerability" framework
- C2-H2 retained as distinct application hypothesis (wound healing)
- E4 absorbed into C2-H5 fusion

---

## FINAL-1: V-ATPase pH-Condensate Nodes as the Molecular Effector Layer of the Bioelectric Code

**Lineage:** H3 -> E1 (refined)

**Core claim:** V-ATPase proton pumps — central components of the bioelectric signaling machinery — create pH microenvironments near organellar and plasma membranes that nucleate biomolecular condensates of specific intrinsically disordered proteins. These "bioelectric-condensate nodes" are self-reinforcing through a positive feedback loop: condensate Donnan potentials (~10 mV) locally reinforce the electrochemical gradient that sustains V-ATPase activity. The spatial distribution of these nodes across a tissue implements the bioelectric code at the molecular level, with each node existing in one of two bistable states (condensate-present/hyperpolarized or condensate-absent/depolarized).

**A -> B -> C structure:**
- A (Bioelectric signaling): V-ATPase activity patterns across tissue, regulated by gap junction network
- B (Bridge): Local pH microenvironments near V-ATPase sites shift IDPs across phase separation threshold
- C (Condensate organization): Spatial pattern of condensate nodes encodes morphogenetic state

**Mechanism (grounded claims marked [G], parametric [P], speculative [S]):**
1. V-ATPase creates local pH gradients of 0.2-0.5 pH units near organellar membranes [G — V-ATPase function well-characterized]
2. IDPs like FUS, TDP-43, and LAF-1 have pH-dependent phase separation thresholds near cytoplasmic pH [G — TDP-43 phase separation pH-dependent per in vitro studies]
3. Local pH reduction near V-ATPase sites shifts the effective pH past the condensation threshold for specific IDPs [P — logically follows from 1+2 but not directly demonstrated]
4. Formed condensates generate Donnan potentials of ~10 mV at their interfaces [G — Bhatt 2024 Cell]
5. Donnan potentials reinforce local membrane potential, sustaining V-ATPase activity [P — voltage-dependent V-ATPase regulation exists but Donnan potential magnitude may be insufficient]
6. Bistable node states create tissue-level condensate pattern that encodes morphogenetic target [S — theoretical framework, not yet demonstrated]

**Counter-evidence and risks:**
- Cytoplasmic pH buffering may attenuate V-ATPase-driven pH microdomains (partial mitigation: effect strongest near organellar membranes where buffering capacity is locally exhausted)
- Donnan potential from condensates (~10 mV) may be too small to meaningfully influence V-ATPase activity (critical quantitative uncertainty)
- Many other factors control condensate formation (crowding, RNA, temperature, post-translational modifications) — pH may not be the dominant factor in vivo

**How to test:**
1. Triple-color imaging in Xenopus blastomeres: V-ATPase-GFP + pHluorin + FUS-mCherry condensate reporter. EXPECTED: spatial co-localization of V-ATPase activity, pH depression, and FUS condensation. Time ~3 months, cost ~$15K.
2. Bafilomycin A1 dose-response: measure condensate density at organellar membranes at increasing V-ATPase inhibition. EXPECTED: condensate density decreases with V-ATPase inhibition. Control: measure condensate density at non-organellar sites (should not change). Time ~2 months.
3. If TRUE: co-localization confirmed, dose-dependent response.
4. If FALSE: no spatial correlation between V-ATPase activity and condensate nucleation sites.

**Confidence: 5/10** — Strong mechanistic grounding from independent literatures; key uncertainty is quantitative (are pH microdomains sufficient?).
**Groundedness: Medium-High** — 3 of 6 mechanism steps grounded, 2 parametric, 1 speculative.
**Novelty: Novel** — No published papers connecting V-ATPase to condensate spatial organization.
**Impact: High** — Would provide the missing molecular implementation layer for the bioelectric code.

---

## FINAL-2: Calcium-Gated Condensate Dissolution as the Binary Transduction Step in Bioelectric Pattern Reading

**Lineage:** H1 -> E3 (refined)

**Core claim:** Voltage-gated calcium channels (VGCCs) convert continuous bioelectric gradients into binary condensate ON/OFF decisions by activating CaMKII-mediated phosphorylation of IDP scaffold proteins above a voltage threshold. This creates sharp spatial boundaries between condensate-rich and condensate-poor regions that correspond to morphogenetic compartment boundaries, analogous to how voltage-gated Na+ channels create the all-or-nothing threshold in action potentials.

**A -> B -> C structure:**
- A: Tissue-level Vmem gradient (continuous)
- B: VGCC activation threshold (~-40mV) -> Ca2+ influx -> CaMKII -> phosphorylation of FUS/TDP-43 LCD
- C: Binary condensate state (present below threshold, absent above)

**Mechanism (grounded claims marked):**
1. Tissue-level Vmem gradients exist across morphogenetically active regions [G — documented in neural tube, limb bud, etc.]
2. L-type VGCCs activate at ~-40mV [G — electrophysiology literature]
3. Ca2+ influx activates CaMKII locally [G — calcium signaling literature]
4. CaMKII phosphorylates FUS/TDP-43 at S/T residues in their LCDs [G — Nat Commun 2025 simulations; TDP-43 hyperphosphorylation documented]
5. Phosphorylation of LCD dissolves condensates [G — multiple studies show phospho-FUS/TDP-43 cannot phase-separate]
6. This creates a STEP FUNCTION in condensate density at the spatial position of VGCC threshold [P — follows from threshold dynamics but not directly observed]

**Counter-evidence and risks:**
- Calcium activates hundreds of pathways simultaneously; attributing condensate effects specifically to CaMKII-FUS/TDP-43 pathway is reductionist
- The VGCC threshold may not align with morphogenetic boundaries in all tissues
- In vivo calcium dynamics involve oscillations and waves, not static thresholds — the "binary switch" model may oversimplify

**How to test:**
1. Xenopus neural tube: simultaneous Vmem imaging (ASAP3 voltage indicator) + FUS-mCherry condensate reporter. Map both as a function of dorsoventral position. EXPECTED: step function in FUS condensate density at position corresponding to ~-40mV (VGCC threshold). Time ~4 months, cost ~$20K.
2. Nifedipine (L-type VGCC blocker): should shift the step position, extending the condensate-rich region to encompass previously condensate-poor territory. Time ~1 month additional.
3. CaMKII inhibitor (KN-93): should also extend condensate-rich region, confirming the Ca2+ -> CaMKII -> condensate pathway.
4. If TRUE: step function observed, pharmacology confirms mechanism.
5. If FALSE: gradual decline or no spatial correlation between Vmem and condensate density.

**Confidence: 4/10** — Each individual step is well-grounded but the full chain is untested.
**Groundedness: High** — 5 of 6 mechanism steps grounded in published literature.
**Novelty: Novel** — Threshold-gated condensate dissolution model not proposed.
**Impact: High** — Would provide the transduction mechanism linking bioelectric patterns to molecular states.

---

## FINAL-3: Circadian V-ATPase Rhythms and Tissue-Specific Condensate Phase Diagrams Determine Chronovulnerability to Neurodegeneration

**Lineage:** E2 + C2-H5 (fused)

**Core claim:** (1) Circadian clock-driven V-ATPase expression oscillations create daily condensate dissolution-reformation cycles that reset condensate material properties, preventing pathological solidification. (2) The vulnerability of a given tissue to neurodegeneration depends on how close its dominant IDP phase separation boundary is to normal operating pH — tissues where IDPs phase-separate near cytoplasmic pH are most sensitive to V-ATPase decline. (3) These two factors interact: tissues with high "phase diagram proximity" require stronger daily renewal cycles, and are thus most vulnerable when circadian disruption or aging reduces V-ATPase oscillation amplitude.

**A -> B -> C structure:**
- A: Circadian clock regulation of V-ATPase expression (temporal) + tissue-specific IDP repertoire (spatial)
- B: pH oscillation amplitude determines condensate renewal completeness; phase boundary proximity determines renewal necessity
- C: Tissue-specific vulnerability to condensate aging -> protein aggregation -> neurodegeneration

**Mechanism:**
1. BMAL1/CLOCK drive rhythmic V-ATPase V0a1 expression [P — clock regulates many ion transporters; V-ATPase rhythmicity specifically not yet shown]
2. V-ATPase activity oscillation produces daily pH oscillation (amplitude ~0.1-0.2 pH units) [P — plausible based on V-ATPase proton pumping capacity]
3. pH oscillation periodically dissolves/reforms condensates, resetting material state [P — pH-dependent condensate dynamics demonstrated in vitro]
4. Neurons express TDP-43/FUS with phase boundaries near pH 7.0-7.3 [G — in vitro phase separation studies]
5. Neuronal V-ATPase declines with age (V0a1 reduced) [G — Burrinha 2023]
6. Reduced oscillation amplitude -> incomplete condensate renewal -> accelerated material aging -> aggregation [S — logical chain but no direct evidence]

**Counter-evidence and risks:**
- V-ATPase circadian regulation is hypothesized, not demonstrated
- Condensate renewal via pH cycling is a theoretical mechanism with no in vivo evidence
- Neurodegeneration vulnerability depends on many factors beyond condensate dynamics
- The 0.1-0.2 pH unit oscillation may be too small to trigger meaningful condensate dissolution/reformation cycles

**How to test:**
1. V-ATPase V0a1 mRNA time-course in mouse hippocampal neurons (RT-qPCR every 4h for 48h under 12:12 LD). EXPECTED: circadian oscillation with period ~24h. Time ~2 months, cost ~$5K.
2. FRAP measurements of FUS-GFP condensates at 6 circadian timepoints. EXPECTED: maximum fluidity (shortest FRAP half-time) correlated with peak V-ATPase expression. Time ~3 months, cost ~$10K.
3. Constant-light circadian disruption in neuronal culture -> measure condensate FRAP daily for 7 days. EXPECTED: progressive increase in FRAP half-time (indicating material aging) vs rhythmic controls. Time ~1 month, cost ~$3K.
4. If TRUE: V-ATPase oscillates, FRAP oscillates, constant light accelerates material aging.
5. If FALSE: no V-ATPase rhythm OR no FRAP rhythm correlation.

**Confidence: 4/10** — Novel framework with strong translational potential; key assumption (V-ATPase circadian rhythm) is untested.
**Groundedness: Medium** — 2 grounded, 3 parametric, 1 speculative.
**Novelty: Novel** — "Chronovulnerability" framework integrating circadian V-ATPase rhythms with tissue-specific phase diagrams not proposed.
**Impact: Transformative** — Would unify circadian biology, condensate biophysics, and neurodegeneration into a single predictive framework.

---

## FINAL-4: Wound-Edge V-ATPase Activation Triggers Condensate Dissolution Wave as a Rapid Regenerative Signal

**Lineage:** C2-H2 (refined with E1 mechanism)

**Core claim:** The injury current at wound sites activates V-ATPase-mediated rapid repolarization, which triggers a wave of condensate dissolution propagating from the wound edge inward. This condensate dissolution releases sequestered mRNAs and transcription factors, providing a fast (minutes-scale) activation of regenerative gene expression that precedes and enables the slower transcriptional wound-healing response.

**A -> B -> C structure:**
- A: Wound injury -> injury current (1-10 microA/cm2) -> V-ATPase activation at wound edge
- B: V-ATPase-driven pH change + Ca2+ influx from disrupted membrane -> condensate dissolution at wound edge
- C: Released mRNAs/transcription factors activate early regenerative response; dissolution wave propagation sets the spatial extent of the regenerative zone

**Mechanism:**
1. Tissue injury disrupts transepithelial potential, generating injury current and local electric field (~200 mV/mm) [G — well-documented]
2. V-ATPase rapidly activates at wound edge for repolarization [G — Levin lab, required for regeneration]
3. V-ATPase activation changes local pH and, combined with Ca2+ influx from membrane disruption, shifts conditions past condensate dissolution threshold [P — mechanistically follows from E1 but not directly shown at wound sites]
4. Dissolved condensates release sequestered mRNAs and transcription factors [G — stress granule dissolution releases sequestered mRNAs; documented mechanism]
5. Released factors activate early regenerative gene expression [P — plausible but condensate-specific contribution not separated from other signaling]
6. Dissolution wave propagates from wound edge inward, following V-ATPase activation gradient [S — wave propagation not demonstrated]

**Counter-evidence and risks:**
- Multiple other rapid signaling mechanisms operate at wound edges (Ca2+ waves, ROS, DAMPs, purinergic signaling)
- Condensate dissolution would release ALL sequestered mRNAs, not specifically pro-regenerative ones — selectivity problem
- The "dissolution wave" is speculative — condensate dynamics may be too fast for wave-like propagation

**How to test:**
1. Live imaging of FUS-GFP condensates in zebrafish fin wound healing. EXPECTED: condensate density drops at wound edge within minutes of injury, with gradient extending from wound edge. V-ATPase inhibition (concanamycin A) should prevent the condensate dissolution. Time ~3 months, cost ~$12K.
2. smFISH for known wound-response mRNAs (e.g., wnt, fgf) at wound edge +/- bafilomycin A1. EXPECTED: bafilomycin delays early mRNA release from condensate sequestration. Time ~2 months, cost ~$8K.
3. If TRUE: condensate dissolution observed at wound edge, V-ATPase dependent, correlating with mRNA release.
4. If FALSE: no condensate changes at wound edge, or changes are V-ATPase-independent.

**Confidence: 4/10** — Strong bioelectric signal at wounds makes this the most experimentally accessible test of the general bioelectric-condensate framework.
**Groundedness: Medium** — 3 grounded, 2 parametric, 1 speculative.
**Novelty: Novel** — Condensate dissolution as a wound signaling mechanism not proposed.
**Impact: High** — Would connect wound healing biology to condensate biophysics and suggest new therapeutic targets.

---

## Similarity Check
- FINAL-1 (V-ATPase nodes, morphogenesis) and FINAL-2 (Ca2+ threshold, morphogenesis): Both address morphogenesis but through DISTINCT mechanisms (pH vs Ca2+-kinase) and make different predictions (co-localization vs step function). KEEP BOTH.
- FINAL-3 (chronovulnerability, disease) is DISTINCT from FINAL-1/2 (adds circadian + tissue-specificity).
- FINAL-4 (wound healing) is DISTINCT context entirely.
- All four survive diversity check.
