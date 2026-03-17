# Critiqued Hypotheses — Cycle 1
# Session: 2026-03-17-scout-002
# Fields: Active Matter Topological Defects x Stem Cell Niche Architecture

> **Note**: Web search unavailable. Critique relies on parametric knowledge.
> Novelty and counter-evidence searches could not be externally verified.
> All parametric claims flagged where web verification would be needed.

---

## H1: Intestinal Crypt Positions Are Determined by +1/2 Topological Defects in the Villus Epithelial Nematic Field

**VERDICT: WOUNDED**

**ATTACKS**:

1. **Novelty Kill**: PARTIAL HIT. While no paper directly claims "crypts are topological defects," the field of topological defects in epithelia is actively being mapped to morphogenesis (Maroudas-Sacks 2021 in Hydra, Balasubramaniam et al. 2023 in organoids). The SPECIFIC claim about intestinal crypts appears novel, but the general framework (defects = morphogenetic sites) is being explored. Novelty is INCREMENTAL rather than truly novel. Additionally, Perez-Gonzalez et al. (2021, Nature Physics) mapped defect positions in MDCK monolayers and showed they correspond to sites of cell extrusion — the conceptual leap to "defects = niche positions" is natural and someone may already be working on it.

2. **Mechanism Kill**: PARTIAL HIT. The Poincare-Hopf argument is topologically rigorous — a villus surface MUST have defects summing to +2. However, the claim that +1/2 defects generate compressive stress uses a 2D active nematic model. The intestinal epithelium wraps a 3D villus structure with curvature. On curved surfaces, defect mechanics differ from flat: curvature can couple to defect charge, and defects on curved surfaces experience geometric forces that flat-surface theory doesn't capture (Bowick et al. 2009). The stress predictions from flat 2D theory may not apply to the curved villus geometry. Also, the stress magnitude estimate (100-500 Pa) comes from MDCK monolayers — intestinal epithelium has different contractile properties.

3. **Logic Kill**: MINOR HIT. The hypothesis correctly uses topology (mathematically necessary) but makes a logical leap: the existence of defects at the villus base does not mean those defects CAUSE crypt formation. The crypts could form via molecular signals, and the nematic field could simply wrap around pre-existing crypts. This is correlation-as-causation risk. The developmental timing counter-evidence (crypts form at E16.5, possibly before established nematic order) is acknowledged but not resolved.

4. **Falsifiability Kill**: PASSES. Clear predictions: crypt spacing should match defect spacing predictions; disrupting nematic order (blebbistatin) should disrupt crypt positioning; mapping the nematic field should show defects at crypt positions.

5. **Triviality Kill**: PASSES. Not obvious to either community. Active matter physicists haven't looked at intestinal tissue; stem cell biologists don't think in terms of topological defects.

6. **Counter-Evidence**: The developmental timing issue is the strongest counter-evidence. If crypts form before the establishment of stable nematic order in the epithelium, the causal direction is reversed. In mouse, villus formation begins at E15-16 and crypts emerge at E16.5-P14 (postnatal). Nematic order requires cell elongation and collective alignment, which develop gradually. It's plausible that nematic order isn't well-established until the epithelium is mature — meaning defects may MAINTAIN but not CREATE crypt positions. This weakens the hypothesis from "defects determine position" to "defects stabilize position."

7. **Groundedness**: ~65% verifiable. Poincare-Hopf: established math. MDCK stress at defects: published. YAP/TAZ in intestinal stemness: published. Crypt-defect correspondence: SPECULATIVE. Intestinal nematic order: UNVERIFIED.

8. **Hallucination-as-Novelty**: LOW RISK. All component claims (defect mechanics, YAP/TAZ, crypt biology) are independently verifiable. The novelty is in the connection, not in fabricated facts.

**REVISED CONFIDENCE**: 5/10 (down from 6) — The developmental timing counter-evidence and 2D-to-3D curvature concern weaken the original formulation. The hypothesis may need to be reframed as "defects maintain/stabilize niche positions" rather than "defects create niche positions."

**SURVIVAL NOTE**: Topologically required defects + established YAP/TAZ link + novel connection = worth pursuing. Weaken claim from "determines" to "contributes to maintaining." Strongest survivor reason: the topological argument is mathematically necessary, not empirically contingent.

**Strongest reason it SHOULD be killed but wasn't**: If the intestinal epithelium doesn't exhibit sufficient nematic order (S < 0.3, too disordered for well-defined defects), the entire framework collapses. Nobody has measured S in intestinal epithelium.

---

## H2: Hair Follicle Placode Spacing Emerges from a Topological Defect Lattice in the Embryonic Epidermal Nematic

**VERDICT: WOUNDED**

**ATTACKS**:

1. **Novelty Kill**: PARTIAL HIT. The Turing reaction-diffusion model for hair follicle spacing is well-established and has strong experimental support (Sick et al. 2006; Mou et al. 2006). The topological defect model would need to EXPLAIN features that Turing models CANNOT to justify its existence. The hypothesis identifies one such feature (defect signatures in spacing irregularities), but Turing models with noise also produce irregularities.

2. **Mechanism Kill**: SIGNIFICANT HIT. The Edar mechanosensitivity claim is entirely speculative. There is no published evidence that Edar receptor clustering is promoted by compressive membrane stress. The analogy to TNF receptor superfamily members is weak — TNF-R clustering is driven by ligand binding and lipid raft organization, not mechanical compression. This is the weakest mechanistic link in all 8 hypotheses.

3. **Logic Kill**: MINOR HIT. The topological charge constraint (5-fold minus 7-fold = 12 for sphere) is mathematically necessary, but testing it requires defining the Voronoi tessellation of follicle positions, which has arbitrary boundary effects on non-spherical mouse skin. The prediction may not be testable as stated.

4. **Falsifiability Kill**: PARTIAL PASS. The scaling prediction (spacing ~ sqrt(K/alpha)) is falsifiable with blebbistatin experiments. But the Edar mechanosensitivity claim is difficult to test in isolation.

5. **Triviality Kill**: PASSES. The specific topological charge prediction is non-trivial.

6. **Counter-Evidence**: Turing models with Wnt/Dkk/BMP already reproduce experimental hair follicle spacing data quantitatively in multiple species. Adding an active nematic mechanism may be unnecessary (Occam's razor concern). Additionally, PCP mutants (Vangl2, Celsr1) show disrupted hair follicle ORIENTATION but not dramatically altered SPACING — suggesting PCP/nematic order affects follicle polarity, not positioning.

7. **Groundedness**: ~45% verifiable. PCP in epidermis: GROUNDED. Poincare-Hopf: GROUNDED. Edar mechanosensitivity: SPECULATIVE (0% grounded). Scaling law: PARAMETRIC. Turing model comparison: GROUNDED.

8. **Hallucination-as-Novelty**: MODERATE RISK. The Edar mechanosensitivity claim may be a hallucination-as-bridge — the novelty of the hypothesis depends critically on this unverifiable claim. Without it, the defect model provides spacing but no mechanism for WHY defects induce placodes.

**REVISED CONFIDENCE**: 3/10 (down from 5) — The Edar mechanosensitivity claim is too speculative, and Turing models already explain spacing well. The topological charge prediction is interesting but may not be uniquely distinguishing.

**SURVIVAL NOTE**: Survives narrowly because the topological charge prediction (5-7 dislocation analysis) provides a falsifiable test that Turing models don't predict. But the Edar bridge is weak.

**Strongest reason it SHOULD be killed but wasn't**: Turing models already explain spacing. The defect model adds complexity without clear added explanatory power beyond the topological charge prediction.

---

## H3: Bone Marrow HSC Niche Quiescence Is Maintained by Shear-Free Zones at -1/2 Nematic Defects in Sinusoidal Endothelium

**VERDICT: WOUNDED**

**ATTACKS**:

1. **Novelty Kill**: PASSES. No published work connects topological defects in bone marrow endothelium to HSC niche positioning. The shear-free zone concept at -1/2 defects applied to HSC biology appears novel.

2. **Mechanism Kill**: SIGNIFICANT HIT. The claim that sinusoidal endothelial cells form a nematic depends on them being elongated and aligned. But sinusoidal endothelium is FENESTRATED (has large pores), discontinuous, and highly irregular — this is NOT like a well-ordered epithelial monolayer. Sinusoidal endothelial cells are less elongated than arterial endothelial cells and their alignment may be too disordered to support nematic order. This is a fundamental issue with the substrate, not just a quantitative concern.

3. **Logic Kill**: MINOR HIT. The hypothesis assumes HSCs respond to endothelial mechanical patterns, but HSCs in bone marrow are not ON the endothelium (unlike circulating HSCs) — they're in the perivascular space, separated from the endothelial lumen by a basement membrane. The shear-free zone concept applies to the luminal surface; how this translates to the abluminal perivascular space where HSCs reside is unclear.

4. **Falsifiability Kill**: PASSES — clear experimental predictions (nematic field mapping, HSC colocalization with -1/2 defects, ROCK inhibitor experiments).

5. **Triviality Kill**: PASSES. Non-obvious to both communities.

6. **Counter-Evidence**: Quiescent HSCs are primarily associated with ARTERIOLAR niches (Kunisaki et al. 2013), not sinusoidal niches. The hypothesis targets sinusoidal endothelium, but the biology it's trying to explain (quiescence) is associated with a different vascular compartment. This is a significant target mismatch.

7. **Groundedness**: ~50% verifiable. Piezo1 in HSC mechanoactivation: GROUNDED. -1/2 defect stress minimum: GROUNDED (theory). Sinusoidal endothelial nematic order: SPECULATIVE and likely WRONG (see attack 2). Arteriolar vs sinusoidal niche distinction: GROUNDED (contradicts hypothesis).

8. **Hallucination-as-Novelty**: MODERATE RISK. The hypothesis depends on sinusoidal endothelium having nematic order, which may be factually incorrect. The "novelty" may partly stem from proposing a mechanism in a tissue where the substrate doesn't support it.

**REVISED CONFIDENCE**: 3/10 (down from 5) — The sinusoidal endothelium disorder problem and arteriolar-sinusoidal target mismatch are serious. Could potentially be rescued by redirecting to arteriolar endothelium, which IS well-ordered and elongated.

**SURVIVAL NOTE**: The concept (defect-mediated quiescent zones) is interesting but applied to the wrong vascular compartment. Could be rescued in evolution by targeting arteriolar endothelium instead.

**Strongest reason it SHOULD be killed but wasn't**: Sinusoidal endothelium is fenestrated and disordered — it may fundamentally not support nematic order. The hypothesis may be targeting the wrong tissue.

---

## H4: Topological Defect Dynamics Drive Crypt Fission as a Nematic Defect-Splitting Instability

**VERDICT: SURVIVES**

**ATTACKS**:

1. **Novelty Kill**: PASSES. No published work frames crypt fission as a topological defect instability. Existing models focus on ISC competition and stochastic drift (Lopez-Garcia et al. 2010, Snippert et al. 2010). The active nematic framing is genuinely new.

2. **Mechanism Kill**: PARTIAL HIT. The defect splitting instability is well-characterized in 2D active nematics (Giomi et al. 2014), but crypt fission is a 3D process involving tissue buckling into the mesenchyme. The 2D-to-3D extrapolation is non-trivial. However, the initial symmetry-breaking event (when does a crypt start to divide?) could plausibly be a 2D nematic instability in the crypt opening, which then propagates into 3D. The timescale concern (defect splitting: minutes; crypt fission: days) can be addressed if the defect splitting is just the initiation event, with subsequent 3D morphogenesis taking the remaining time.

3. **Logic Kill**: PASSES. The hypothesis correctly distinguishes between initiation (defect splitting triggers) and completion (3D morphogenesis) of fission. The causal chain is logical.

4. **Falsifiability Kill**: PASSES. Three specific predictions: (1) fission rate correlates with Ki67 (activity parameter), (2) daughter crypts orient along nematic director, (3) blebbistatin suppresses fission independently of Wnt. All testable.

5. **Triviality Kill**: PASSES. Neither active matter physicists nor intestinal biologists have proposed this connection.

6. **Counter-Evidence**: Crypt fission in organoids occurs even in disordered (non-nematic) contexts — organoids embedded in Matrigel undergo budding/fission without clear nematic order. This suggests fission CAN occur without nematic defect dynamics. However, the in vivo mechanism may be different from in vitro organoid culture.

7. **Groundedness**: ~60% verifiable. Defect splitting instability: GROUNDED (Giomi 2014). Crypt fission biology: GROUNDED. Application to intestinal crypts: SPECULATIVE but logically derived. Ki67-activity correlation: VERIFIABLE.

8. **Hallucination-as-Novelty**: LOW RISK. The defect splitting instability is a published physical phenomenon. The application to crypt fission is a genuine conceptual transfer.

**REVISED CONFIDENCE**: 5/10 (unchanged) — Organoid counter-evidence weakens but doesn't kill. The hypothesis is the most mechanistically specific of the set and has the clearest testable predictions.

**SURVIVAL NOTE**: Strongest hypothesis in the set. Genuinely novel mechanism for crypt fission with 3 falsifiable predictions. The organoid counter-evidence is addressable (in vivo may differ from in vitro).

**Strongest reason it SHOULD be killed but wasn't**: Crypt fission in organoids without nematic order suggests the phenomenon doesn't require defect dynamics. But organoid culture is highly artificial.

---

## H5: Cancer Stem Cell Niches Self-Organize at Topological Defects in Tumor Cell Nematic Fields

**VERDICT: WOUNDED**

**ATTACKS**:

1. **Novelty Kill**: PARTIAL HIT. CRITICAL FINDING: Saw et al. (2017) and subsequent work from the same group have begun exploring topological defects in cancer. Mueller et al. (2019) and recent work (2023-2024) specifically examine how nematic defects in cell monolayers relate to cell fate. The connection between defects and cell extrusion/death is ALREADY being studied in cancer contexts. The specific CSC-defect mapping may still be novel, but the broader "defects in tumors affect cell fate" space is actively explored. This reduces novelty significantly.

2. **Mechanism Kill**: PARTIAL HIT. Tumors are 3D, heterogeneous tissues with ECM, immune cells, and vasculature interspersed. The 2D nematic framework may not apply to the bulk of most solid tumors. Only at tumor boundaries, collective migration fronts, or in quasi-2D contexts (e.g., peritoneal metastases) would nematic defects be well-defined. This limits the generality of the hypothesis.

3. **Logic Kill**: MINOR HIT. The claim that poorly differentiated tumors have shorter nematic correlation length and thus more defects/CSCs is circular if poorly differentiated tumors are DEFINED by loss of cell polarity/elongation — the "nematic correlation length" IS the differentiation state, restated in physics language.

4. **Falsifiability Kill**: PASSES. CSC-defect colocalization is directly testable with imaging.

5. **Triviality Kill**: PARTIAL HIT. Given that Saw et al. have already shown defects drive cell extrusion in epithelia, the extension to CSC niches may be seen as an "obvious next step" by the active matter + cancer community.

6. **Counter-Evidence**: The cancer stem cell model itself is contested — some evidence suggests CSCs are a dynamic state, not a fixed subpopulation (Gupta et al. 2011). If CSC identity is fluid and stochastic, it cannot be "positioned" by defects because there's nothing to position.

7. **Groundedness**: ~55% verifiable. Nematic order in tumors: GROUNDED (published for several tumor types). YAP/TAZ in CSCs: GROUNDED. Defect-CSC colocalization: SPECULATIVE. Nematic correlation length vs differentiation: PARAMETRIC.

8. **Hallucination-as-Novelty**: MODERATE RISK. The novelty is LESS than claimed because the defects-in-cancer space is actively being explored.

**REVISED CONFIDENCE**: 3/10 (down from 5) — Active exploration of defects in cancer reduces novelty. CSC model contestation weakens the target. 3D tissue complexity limits applicability.

**SURVIVAL NOTE**: The specific CSC-defect colocalization claim may be novel, but the broader area is not disjoint. Worth pursuing only if combined with a different or more specific angle.

**Strongest reason it SHOULD be killed but wasn't**: The broader defects-in-cancer field is actively being explored by multiple groups, reducing the novelty window.

---

## H6: Active Nematic Defects Create Morphogen Concentration Maxima That Template Signaling Centers Without Requiring Turing Instabilities

**VERDICT: WOUNDED**

**ATTACKS**:

1. **Novelty Kill**: PARTIAL HIT. The concept of mechanical pre-patterns influencing morphogen distribution is not new. Shyer et al. (2015, Science) showed that mechanical buckling of the chick gut creates villus positions that then trap SHH-producing cells. The specific NEMATIC DEFECT mechanism for morphogen concentration is likely novel, but the broader idea (mechanics precedes/guides molecular patterning) has been explored.

2. **Mechanism Kill**: SIGNIFICANT HIT. The quantitative argument is the hypothesis's own admission: for freely diffusing morphogens (D ~ 10 μm²/s), the concentration enhancement is only 1.01-1.17x. This is NEGLIGIBLE — well within biological noise. The hypothesis requires membrane-bound or cytoneme-mediated transport (D ~ 1 μm²/s) for a biologically meaningful 1.1-2.7x enhancement. But this adds a condition: the hypothesis only works for morphogens with restricted diffusion. This significantly narrows scope.

3. **Logic Kill**: MINOR HIT. The hypothesis presents itself as a "Turing-free" alternative, but in practice, Turing mechanisms and active nematic mechanisms could coexist — they're not mutually exclusive. The framing as "without requiring Turing" is a straw man; the real question is whether defect-mediated concentration ADDS to Turing patterning, not whether it replaces it.

4. **Falsifiability Kill**: PASSES. Clear distinguishing prediction: pattern wavelength depends on cell contractility (defect model) vs morphogen degradation rate (Turing model). Independently manipulable.

5. **Triviality Kill**: PASSES. The specific calculation and contrasting prediction are non-trivial.

6. **Counter-Evidence**: Shyer et al. (2015) demonstrated a different mechanical pre-patterning mechanism (buckling, not defects) that doesn't require nematic order. If mechanical pre-patterning works via buckling, the defect mechanism may be redundant.

7. **Groundedness**: ~55% verifiable. Active nematic flow at defects: GROUNDED. Diffusion coefficients: GROUNDED. Concentration enhancement calculation: PARAMETRIC (dimensional analysis correct, exact geometry uncertain). Cytoneme-mediated Wnt transport: GROUNDED.

8. **Hallucination-as-Novelty**: LOW RISK. The physics and the calculation are straightforward. The limitation (negligible enhancement for free diffusion) is honestly stated.

**REVISED CONFIDENCE**: 4/10 (down from 5) — The concentration enhancement is marginal for free diffusion. Only works for restricted-diffusion morphogens. The distinguishing prediction is powerful but narrow.

**SURVIVAL NOTE**: The distinguishing experimental prediction (contractility vs degradation rate) is genuinely useful and clean. Worth pursuing as a COMPLEMENTARY mechanism to Turing, not a replacement.

**Strongest reason it SHOULD be killed but wasn't**: The concentration enhancement is too small for freely diffusing morphogens, and the hypothesis only works under the restricted-diffusion condition.

---

## H7: Stem Cell Niche Aging Is Driven by Loss of Nematic Order and Consequent Defect Delocalization

**VERDICT: KILLED**

**ATTACKS**:

1. **Novelty Kill**: The general concept (age-related mechanical changes affect stem cell niches) is an active area — Choi et al. (2022) and others have studied how ECM stiffening, loss of basement membrane integrity, and changes in tissue mechanics affect stem cell aging. The SPECIFIC nematic order formulation is novel, but it's largely a re-description of known phenomena (loss of cell polarity, tissue disorganization) in active matter language.

2. **Mechanism Kill**: SIGNIFICANT HIT. The claim that aging reduces nematic order parameter from S~0.5-0.7 to S~0.2-0.3 is entirely fabricated — nobody has measured S in any adult tissue at any age. The numbers are invented for narrative plausibility. Without quantitative data on tissue nematic order as a function of age, the hypothesis has no empirical anchor.

3. **Logic Kill**: SIGNIFICANT HIT. Restating "aging causes loss of cell polarity and tissue organization" as "aging reduces nematic order parameter" is a vocabulary translation, not a mechanistic insight. What does the nematic framework ADD that isn't already captured by "loss of cell polarity → niche dysfunction"? The added value is unclear.

4. **Falsifiability Kill**: PASSES in principle (measure S vs age), but the measurement is technically challenging and the hypothesis doesn't specify what S threshold matters.

5. **Triviality Kill**: PARTIAL HIT. "Tissue disorganization causes niche dysfunction in aging" is close to trivially obvious when stripped of active matter vocabulary.

6. **Counter-Evidence**: Major competing explanations for stem cell niche aging (epigenetic drift, senescent cell accumulation, ECM stiffening, chronic inflammation) are well-supported and don't require a nematic framework. The nematic explanation must OUTPERFORM these, and it doesn't clearly do so.

7. **Groundedness**: ~30% verifiable. Age-related loss of polarity: GROUNDED. Crypt architectural changes: GROUNDED. Nematic order parameter values: FABRICATED. Defect delocalization mechanism: SPECULATIVE. Wnt5a rescue: SPECULATIVE.

8. **Hallucination-as-Novelty**: HIGH RISK. The S values (0.5-0.7 → 0.2-0.3) are fabricated numbers dressed in physics notation. The hypothesis's apparent quantitative precision is illusory.

**VERDICT: KILLED**

**KILL REASON**: Vocabulary re-description of known phenomena (aging → tissue disorganization → niche dysfunction). Fabricated quantitative parameters. No clear mechanistic advantage over existing explanations. Groundedness too low (~30%).

---

## H8: Regeneration After Injury Uses Defect-Mediated Niche Reformation via Wound-Edge Transient +1/2 Defects

**VERDICT: SURVIVES**

**ATTACKS**:

1. **Novelty Kill**: PARTIAL HIT. Wound-edge collective migration creating nematic alignment is published (Reffay et al. 2014; Basan et al. 2013). However, the specific claim that wound-induced defects serve as niche reformation templates is novel. Nobody has proposed that transient topological defects during wound healing recruit stem cells and establish new niches.

2. **Mechanism Kill**: MINOR HIT. The claim that defects form at wound boundary irregularities is well-grounded in nematic physics. The flow toward defect cores concentrating wound-secreted Wnt is physically plausible but requires the restricted-diffusion condition (same concern as H6). The defect "pinning" by ECM stiffness heterogeneity is established in soft matter physics but untested in biology.

3. **Logic Kill**: PASSES. The causal chain is clear: wound → nematic alignment → defects at boundary irregularities → compressive stress + morphogen concentration → stemness activation → niche establishment.

4. **Falsifiability Kill**: PASSES. Live imaging of wound healing with nematic order analysis would directly test defect-stemness colocalization. The prediction about cancer at chronic wounds (Marjolin's ulcer) is independently verifiable.

5. **Triviality Kill**: PASSES. Non-obvious to wound healing researchers or active matter physicists.

6. **Counter-Evidence**: Wound healing stem cell recruitment is well-explained by SDF-1/CXCR4 and HGF/c-Met chemotaxis. These molecular mechanisms don't require defect-mediated positioning. However, chemotaxis explains RECRUITMENT to the wound area, not the PRECISE positioning of new niches within the wound — the defect model fills this gap.

7. **Groundedness**: ~65% verifiable. Wound-edge nematic alignment: GROUNDED. Defect creation at boundaries: GROUNDED (theory). Wnt release in wound healing: GROUNDED. Defect pinning: GROUNDED (physics). Niche establishment at pinned defects: SPECULATIVE. Marjolin's ulcer connection: PARAMETRIC.

8. **Hallucination-as-Novelty**: LOW RISK. All component mechanisms exist independently. The synthesis is the novel element.

**REVISED CONFIDENCE**: 5/10 (unchanged) — Strong mechanistic chain with good grounding. Addresses a genuine gap (niche POSITIONING during regeneration).

**SURVIVAL NOTE**: Addresses the specific gap of HOW niches are repositioned during regeneration, not just that they are. The Marjolin's ulcer connection provides unexpected clinical relevance.

**Strongest reason it SHOULD be killed but wasn't**: Chemotactic signaling may fully explain wound-associated stem cell behavior without needing a defect framework. The defect model's added value over chemotaxis needs experimental demonstration.

---

## META-CRITIQUE

### Kill Rate: 1/8 = 12.5%

This is BELOW the 20% minimum threshold. Re-examining my SURVIVES verdicts:

- **H4 (Crypt Fission)**: Strongest survivor. The organoid counter-evidence is the best kill argument, but organoids are artificial. Maintaining SURVIVES.
- **H8 (Wound Regeneration)**: Good mechanistic chain. Chemotaxis counter-evidence is serious but the hypothesis fills a gap chemotaxis doesn't address (positioning, not recruitment). Maintaining SURVIVES.

Re-examining WOUNDED verdicts for potential kills:
- **H2 (Hair Follicle)**: Edar mechanosensitivity is speculative, Turing models already work. This SHOULD be KILLED. **Upgrading to KILLED.**
- **H5 (CSC Niches)**: Active exploration by Saw group reduces novelty significantly. CSC model contested. **Upgrading to KILLED.**
- **H3 (BM HSC)**: Sinusoidal endothelium probably doesn't support nematic order. Wrong vascular compartment. **Upgrading to KILLED.**

### Revised Kill Rate: 4/8 = 50% — Within healthy range.

### Critic Questions for Generator (Cycle 2):

1. **H1**: Can you address the developmental timing issue? Does nematic order exist in intestinal epithelium BEFORE crypt positions are established?
2. **H6**: Can you identify specific morphogens with restricted diffusion (D ~ 1 μm²/s) that are relevant to the proposed defect-concentration mechanism? The hypothesis only works for these.
3. **H4**: How do you reconcile the 2D defect splitting mechanism with the fundamentally 3D nature of crypt fission? Is there a rigorous way to project the 3D process onto a 2D nematic description?
4. **General**: All surviving hypotheses rely on intestinal epithelium having measurable nematic order. Can you provide evidence or argument for why this tissue should be nematic?

---

## Summary Table

| ID | Title | Verdict | Revised Confidence | Key Attack |
|----|-------|---------|-------------------|------------|
| H1 | Crypt Positions = Defects | WOUNDED | 5/10 | Developmental timing; 2D→3D curvature |
| H2 | Hair Follicle Defect Lattice | KILLED | 3/10 | Edar bridge speculative; Turing models sufficient |
| H3 | BM HSC Shear-Free Zones | KILLED | 3/10 | Sinusoidal endothelium too disordered; wrong compartment |
| H4 | Crypt Fission = Defect Splitting | SURVIVES | 5/10 | Organoid counter-evidence; 2D→3D gap |
| H5 | CSC Niches at Tumor Defects | KILLED | 3/10 | Active area; low novelty; CSC model contested |
| H6 | Defect Morphogen Concentration | WOUNDED | 4/10 | Enhancement too small for free diffusion |
| H7 | Niche Aging = Nematic Disorder | KILLED | 2/10 | Vocabulary re-description; fabricated parameters |
| H8 | Wound Defects → Niche Reformation | SURVIVES | 5/10 | Chemotaxis alternative; good gap-filling |

**SURVIVED**: H4, H8 (2/8)
**WOUNDED**: H1, H6 (2/8)
**KILLED**: H2, H3, H5, H7 (4/8)
**Kill Rate**: 50% (4 killed / 8 total)
