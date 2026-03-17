# Evolved Hypotheses — Cycle 1
## Session: 2026-03-17-scout-001

## Evolution Strategy
- Recombine H3 (strongest) with H4 (highest testability) into a unified framework
- Strengthen H7 with more specific mechanism from H1
- Refine H1 to address specificity concern
- Evolve H5 to address causal direction problem
- Drop H6 (too speculative) and H2 (quantitatively weak)

---

## E1: V-ATPase pH-Condensate Axis as the Molecular Effector of Bioelectric Morphogenesis (H3 + H4 fusion)

**Evolved from:** H3 (V-ATPase pH nucleation) + H4 (bidirectional feedback)

**Core claim:** V-ATPase proton pumps — already known as key bioelectric signaling components — create local pH microenvironments that serve as condensate nucleation sites near organellar and plasma membranes. Once formed, these condensates generate Donnan potentials that reinforce the local electrochemical gradient, creating self-sustaining "bioelectric-condensate nodes." The spatial pattern of these nodes across a tissue constitutes the molecular implementation of the bioelectric code, with bistable node states (condensate-present/hyperpolarized vs condensate-absent/depolarized) mediating morphogenetic decisions.

**Improvement over parents:** Combines the strong mechanistic grounding of H3 (V-ATPase -> pH -> condensate) with the systems-level insight of H4 (bidirectional feedback) into a single testable framework. The "bioelectric-condensate node" concept is more specific than either parent.

**Specific mechanism:**
1. V-ATPase activity (regulated by bioelectric signaling network) acidifies local cytoplasmic regions near organellar membranes
2. Local pH reduction (even 0.2-0.3 pH units, within documented V-ATPase capability) shifts specific IDPs past their phase separation threshold
3. Condensate nucleation at V-ATPase-adjacent sites
4. Condensate Donnan potential (~10 mV, per bioRxiv 2024) reinforces local membrane potential
5. Reinforced membrane potential sustains V-ATPase activity through voltage-dependent regulation
6. Bistable outcome: cells lock into condensate-node-rich (differentiated) or condensate-node-poor (proliferative) states

**Falsifiable prediction:** In Xenopus blastomeres, simultaneous imaging of V-ATPase-GFP, pH-sensitive fluorescent protein (pHluorin), and IDP condensate reporter (FUS-mCherry) should reveal spatial co-localization of V-ATPase activity, local pH depression, and condensate nucleation. Bafilomycin A1 treatment should disrupt all three simultaneously. Additionally, cells at morphogenetic boundaries should show bimodal distributions of condensate-node density.

**Groundedness:** V-ATPase bioelectric role (GROUNDED, Levin lab). pH-dependent condensate formation (GROUNDED, Nat Chem 2025). Condensate Donnan potentials (GROUNDED, Bhatt 2024). Node bistability concept (PARAMETRIC). Three-way co-localization (SPECULATIVE but testable).

---

## E2: Circadian V-ATPase Oscillations Reset Condensate Material State to Prevent Pathological Aging (H7 + H3 fusion)

**Evolved from:** H7 (circadian condensate renewal) + H3 (V-ATPase pH mechanism)

**Core claim:** Circadian clock-regulated oscillation of V-ATPase expression/activity creates daily cycles of condensate dissolution and reformation, resetting condensate material properties before they undergo the pathological liquid-to-gel transition. This "condensate maintenance cycle" depends on rhythmic V-ATPase-driven pH oscillations and is compromised by both circadian disruption and age-related V-ATPase decline.

**Improvement over parents:** Specifies the MOLECULAR MECHANISM of circadian condensate renewal (V-ATPase oscillation -> pH cycles) rather than the vague "bioelectric oscillation" of H7. Incorporates the V-ATPase aging decline evidence.

**Specific mechanism:**
1. Clock genes (BMAL1/CLOCK) drive rhythmic V-ATPase subunit expression (specifically V0a1 in neurons)
2. V-ATPase activity oscillates -> local pH oscillates (amplitude ~0.1-0.2 pH units)
3. During pH nadir: condensate formation is favored, condensates nucleate with fresh components
4. During pH zenith: existing condensates partially dissolve, releasing aged/modified proteins
5. Net effect: daily material state reset prevents accumulation of cross-linked/fibrillized protein within condensates
6. With aging: V-ATPase expression drops -> pH oscillation amplitude decreases -> condensate renewal incomplete -> material aging accelerates -> aggregation threshold crossed

**Falsifiable prediction:** (1) V-ATPase V0a1 subunit mRNA should show circadian oscillation in neurons (testable by RT-qPCR on time-course samples). (2) Condensate FRAP half-time should oscillate with circadian period, with maximum fluidity correlated with peak V-ATPase expression. (3) In V-ATPase-hypomorphic neurons, condensate material aging (measured by FRAP) should accelerate compared to wild-type, and this acceleration should be phenocopied by constant-light circadian disruption.

**Groundedness:** Clock regulation of ion channels (GROUNDED). V-ATPase in neurons (GROUNDED). V-ATPase decline with aging (GROUNDED, Burrinha 2023). Condensate material aging (GROUNDED). Clock-V-ATPase rhythmic coupling (PARAMETRIC). pH-driven condensate renewal (SPECULATIVE but mechanistically sound).

---

## E3: Calcium-Gated Condensate Dissolution as the Transduction Step in Bioelectric Pattern Reading (H1 refined)

**Evolved from:** H1 (Vmem-Ca-Kinase-Condensate) — refined to address specificity concern

**Core claim:** Voltage-gated calcium channels (VGCCs) transduce the tissue-level bioelectric pattern into local condensate dissolution events by activating CaMKII-mediated phosphorylation of specific IDP scaffold proteins (TDP-43, FUS). This does NOT require calcium to be the sole regulator — rather, calcium acts as the GATE that converts a continuous bioelectric gradient into a binary condensate ON/OFF switch, analogous to how voltage-gated sodium channels convert graded potentials into all-or-nothing action potentials.

**Improvement over parent:** Addresses the specificity concern by reframing calcium not as THE controller but as a THRESHOLD GATE. The analogy to action potential generation makes the mechanism more precise and the prediction more specific.

**Specific mechanism:**
1. Tissue-level Vmem gradient (established by gap junction network + V-ATPase)
2. Where local Vmem exceeds VGCC activation threshold (~-40mV for L-type): Ca2+ influx occurs
3. Ca2+ activates CaMKII locally
4. CaMKII phosphorylates FUS at S/T residues in LCD domain (documented in literature)
5. Phosphorylated FUS cannot undergo LLPS -> condensate dissolution
6. Result: sharp boundary between condensate-rich (below VGCC threshold) and condensate-poor (above threshold) regions, corresponding to bioelectric pattern features

**Falsifiable prediction:** In a tissue with a known Vmem gradient (e.g., Xenopus neural tube), FUS-GFP condensate density should show a STEP FUNCTION (not gradual decline) at the spatial position corresponding to the VGCC activation threshold. The step position should shift predictably when VGCCs are pharmacologically modulated (e.g., nifedipine to block L-type channels should extend the condensate-rich region).

**Groundedness:** VGCCs and CaMKII activation (GROUNDED). CaMKII-mediated phosphorylation of FUS (GROUNDED, documented). Phosphorylation-driven FUS condensate dissolution (GROUNDED, Nature Communications 2025 simulations). Step-function behavior (PARAMETRIC — predicted by threshold dynamics). Spatial correlation with Vmem gradient (SPECULATIVE but testable).

---

## E4: V-ATPase Decline as a Convergent Pathomechanism in Neurodegeneration via Condensate Dysregulation (H5 refined)

**Evolved from:** H5 (bioelectric neurodegeneration) — refined to address causal direction problem

**Core claim:** Age-related V-ATPase decline is a CONVERGENT upstream cause — not a downstream consequence — of neurodegenerative protein aggregation, acting through disruption of pH-mediated condensate spatial organization. This is testable because V-ATPase decline is independently caused by non-disease-specific mechanisms (reduced transcription, oxidative damage to V0 subunits) and can be rescued independently of the aggregation pathway.

**Improvement over parent:** Focuses specifically on V-ATPase (not generic "bioelectric decline") to create a more tractable hypothesis with an addressable causal direction concern. The key improvement is identifying V-ATPase decline as independently causeable, breaking the circularity.

**Specific mechanism:**
1. V-ATPase V0a1 expression declines with age (documented, Burrinha 2023)
2. Reduced V-ATPase activity -> endolysosomal deacidification (documented) + reduced perimembrane pH gradients
3. Loss of pH-dependent condensate nucleation templates (from E1)
4. Condensates form in "wrong" locations — away from quality-control-competent organellar membranes
5. Mislocalized condensates lack access to chaperone/autophagy surveillance
6. Accelerated condensate aging -> pathological solid transition -> seeding of TDP-43/tau/alpha-syn aggregates

**Falsifiable prediction:** (1) V-ATPase overexpression in aged neurons should REDUCE condensate mislocalization and delay aggregation onset, even without addressing any other age-related change. (2) V-ATPase-deficient young neurons (genetic knockdown) should show premature condensate mislocalization BEFORE any signs of protein aggregation (establishing temporal priority). (3) The spatial distribution of condensates relative to endolysosomes should change with V-ATPase activity in a dose-dependent manner.

**Groundedness:** V-ATPase age-related decline (GROUNDED). Endolysosomal deacidification (GROUNDED). Condensate-organelle spatial relationship (PARTIALLY GROUNDED — condensates associate with organelles, but not specifically via pH). V-ATPase rescue preventing aggregation (SPECULATIVE but testable). Condensate mislocalization preceding aggregation (SPECULATIVE).

---

## Diversity Assessment
- E1 (V-ATPase bistable nodes): Morphogenetic mechanism — fundamental biology
- E2 (Circadian V-ATPase renewal): Temporal maintenance — chronobiology/disease prevention
- E3 (Calcium gate threshold): Signal transduction — developmental biology
- E4 (V-ATPase neurodegeneration): Disease mechanism — clinical/translational

All four address different contexts (fundamental pattern formation, temporal regulation, signal transduction, disease) despite sharing the V-ATPase/condensate core. Conceptual diversity is maintained.

## Dropped Hypotheses
- H2 (Gap Junction Coherence): Quantitative argument too weak
- H6 (Morphogenetic Memory Storage): Condensate lifetime incompatible with memory duration; no clean test
- H8 (LR Asymmetry): Killed — physics doesn't work
