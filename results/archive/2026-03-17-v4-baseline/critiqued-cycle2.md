# Critiqued Hypotheses — Cycle 2
## Session: 2026-03-17-scout-001

---

## C2-H1: Membrane Lipid Packing as Vmem-Sensitive Condensate Wetting Switch

### Attack 1: Voltage-dependent lipid redistribution evidence
**Counter-evidence:** While the theoretical basis for voltage-dependent lipid flip-flop exists (charged lipids respond to intramembrane potential gradient), the in vivo evidence is thin. PS redistribution is primarily controlled by ATP-dependent flippases and scramblases, not passive voltage-driven redistribution. The voltage effect may be negligible compared to enzymatic control.

### Attack 2: Physiological voltage range
**Counter-evidence:** The Nat Commun 2025 paper on lipid packing and condensate wetting studied LARGE changes in lipid composition (different chain lengths, cholesterol content). Whether the lipid packing changes caused by physiological Vmem shifts (~20-80 mV) are sufficient to detectably alter condensate wetting is highly uncertain. The effect size is likely very small.

### Attack 3: Novelty check
**Web search:** No papers connect Vmem -> lipid reorganization -> condensate wetting. NOVEL.

### Attack 4: GUV test feasibility
The proposed GUV experiment is elegant but would test an artificial system. Translating to in vivo relevance would remain uncertain.

### Verdict: SURVIVES (weakened)
Interesting DIRECT physical mechanism but quantitative plausibility is uncertain. The lipid packing changes from physiological Vmem may be too small.
**Confidence: 3/10**

---

## C2-H2: Wound-Induced Injury Currents Trigger Condensate Reorganization

### Attack 1: Injury current magnitude
**SUPPORTING:** Wound-edge electric fields (~200 mV/mm) are MUCH larger than normal tissue bioelectric gradients (~1-10 mV/mm). This makes the biophysical case stronger — if any bioelectric effect on condensates exists, wound edges are where it would be most dramatic.

### Attack 2: Existing wound-healing explanations
**Counter-evidence:** Wound-edge gene activation is already well-explained by calcium waves, ROS signaling, damage-associated molecular patterns (DAMPs), and growth factor release. Adding "condensate dissolution" as a mechanism risks being redundant with these established pathways.

### Attack 3: Timing argument is weak
**Counter-evidence:** The claim that condensate dissolution explains why wound healing starts "within minutes" is misleading — calcium waves and ROS signaling also operate on minute timescales. Condensate dissolution would not be uniquely fast.

### Attack 4: Novelty check
**Web search:** No papers propose condensate reorganization as a wound healing mechanism. NOVEL.

### Attack 5: V-ATPase link in wound healing
**SUPPORTING:** V-ATPase activation IS known to be critical for wound healing and regeneration initiation (Levin lab). The connection V-ATPase -> pH -> condensate dissolution at wound edge is mechanistically specific and builds on E1.

### Verdict: SURVIVES
Strong bioelectric signal at wounds makes biophysical case more convincing. V-ATPase connection is specific. But competes with established wound-healing mechanisms for explanatory priority.
**Confidence: 4/10**

---

## C2-H3: Cancer Depolarization Drives Condensate Dissolution, Explaining Stem-Cell-Like State

### Attack 1: Condensate changes in cancer — existing data
**Counter-evidence:** Existing research shows condensates in cancer are ABERRANT, not simply dissolved. Mutant p53 forms irreversible dense condensates. Tumor cells form tumor-specific transcriptional condensates at superenhancers. The picture is complex — not a simple "depolarization dissolves condensates" story. Some condensates are lost, others are gained or altered.

### Attack 2: Repressive condensate specificity
**Counter-evidence:** The claim focuses on "repressive condensates" (Polycomb/heterochromatin), but Polycomb-mediated gene silencing involves complex chromatin mechanisms that are not primarily phase-separation-dependent in many contexts. While Polycomb bodies do show phase separation properties, attributing cancer gene reactivation specifically to condensate dissolution (rather than chromatin remodeling, mutation, etc.) is a large claim.

### Attack 3: Novelty check
**Web search:** Condensates in cancer are an active area. But specific connection of cancer depolarization -> condensate dissolution -> stem-like state is NOT published. NOVEL.

### Attack 4: Ivermectin test
**SUPPORTING:** Ivermectin has been shown to have anti-cancer properties and does hyperpolarize cells. This creates a natural experimental test, though ivermectin has many off-target effects.

### Verdict: SURVIVES (weakened)
The overall direction (depolarization alters condensate landscape in cancer) is plausible, but oversimplifies the complex condensate changes in cancer. Needs refinement to account for both condensate loss AND aberrant condensate gain.
**Confidence: 3/10**

---

## C2-H4: V-ATPase Node Network as Computational Substrate

### Attack 1: Mathematical formalism is premature
**Counter-evidence:** The neural network analogy is elegant but lacks quantitative grounding. The coupling strength w_ij through gap junctions, the condensate formation threshold, and the Donnan potential propagation range are all unknown. Without these parameters, the "attractor state" claim is untestable.

### Attack 2: Scaling law prediction
**Counter-evidence:** The prediction that morphological complexity scales with V-ATPase node number assumes all nodes are equivalent, which is biologically implausible. Different cell types express different IDPs and different V-ATPase subunits, breaking the homogeneity assumption required for simple attractor network scaling.

### Attack 3: Gap junction disruption test
**Counter-evidence:** Gap junction disruption causes massive developmental defects through MANY mechanisms (nutrient sharing, second messenger propagation, etc.). Attributing any observed simplification of anatomy to disrupted "condensate node computation" would be uninterpretable.

### Attack 4: Novelty check
The computational substrate concept for bioelectric-condensate networks is NOVEL. But "bioelectric computation" is partially explored (Levin's framework). The condensate-specific version is new.

### Verdict: SURVIVES (weakened)
Conceptually interesting but currently unfalsifiable in practice. The analogy is suggestive but lacks quantitative parameters needed for specific predictions.
**Confidence: 2/10**

---

## C2-H5: pH-Dependent Condensate Phase Diagram Predicts Tissue-Specific Vulnerability

### Attack 1: TDP-43 pH behavior
**SUPPORTING:** TDP-43 phase separation IS pH-dependent — low pH actually REDUCES LLPS propensity (by protonating charged residues, increasing repulsion). This is opposite to what H5 predicts (V-ATPase decline -> pH increase -> enhanced LLPS). Wait — V-ATPase decline leads to endolysosomal deacidification (pH increase from 4.5 to ~5.5), but cytoplasmic pH may actually INCREASE slightly. For TDP-43, higher pH favors LLPS. This actually SUPPORTS the hypothesis if reformulated: V-ATPase decline -> slight cytoplasmic pH increase -> TDP-43 crosses phase boundary into condensate-forming regime -> increased aggregation risk.

### Attack 2: Tissue-specific IDP repertoire data availability
**Counter-evidence:** While proteomics data exists for tissue-specific protein expression, the PHASE DIAGRAMS of tissue-specific IDP combinations under varying pH have not been systematically measured. The prediction requires data that does not yet exist — making it prospective rather than immediately testable.

### Attack 3: Tissue vulnerability is multifactorial
**Counter-evidence:** Tissue-selective vulnerability in neurodegeneration involves many factors: protein expression levels, chaperone capacity, metabolic rate, connectivity, excitotoxicity vulnerability. Reducing it to IDP phase diagram proximity to pH boundary oversimplifies dramatically.

### Attack 4: Novelty check
**Web search:** Tissue-specific IDP phase diagrams as vulnerability predictors is NOVEL. The general concept of pH affecting condensate formation is known but applying it to tissue vulnerability prediction is new.

### Verdict: SURVIVES
The strongest translational prediction of the set. TDP-43 pH behavior actually supports the mechanism once correctly formulated. The tissue-specific phase diagram framework is novel and could generate testable predictions even if the full picture is multifactorial.
**Confidence: 4/10**

---

## SUMMARY — Cycle 2

| Hypothesis | Verdict | Post-Critique Confidence |
|---|---|---|
| C2-H1 (Lipid Wetting Switch) | SURVIVES (weakened) | 3/10 |
| C2-H2 (Wound Condensate Reorganization) | SURVIVES | 4/10 |
| C2-H3 (Cancer Depolarization-Condensate) | SURVIVES (weakened) | 3/10 |
| C2-H4 (Computational Substrate) | SURVIVES (weakened) | 2/10 |
| C2-H5 (Tissue Vulnerability Prediction) | SURVIVES | 4/10 |

**Survivors:** 5 of 5
**Killed:** 0
