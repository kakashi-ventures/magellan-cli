# Raw Hypotheses — Cycle 2
## Fields: Bioelectric Morphogenetic Signaling x Biomolecular Condensate Phase Transitions
## Session: 2026-03-17-scout-001

## Building on Cycle 1 Evolved Hypotheses (E1-E4) + Fresh Angles

---

## C2-H1: Membrane Lipid Packing as a Vmem-Sensitive Condensate Wetting Switch (FRESH — new bridge mechanism)

**Core claim:** Changes in transmembrane voltage (Vmem) alter the lateral organization of membrane lipids (voltage-dependent lipid redistribution is documented), which in turn modulates condensate-membrane wetting affinity. Since lipid packing determines condensate wetting behavior (Nat Commun 2025 — increased packing decreases wetting), Vmem-driven lipid reorganization serves as a switch that controls whether condensates wet membrane surfaces or remain cytoplasmic. This provides a DIRECT physical mechanism (not requiring calcium or kinases) for bioelectric control of condensate spatial organization.

**Mechanism chain:** Vmem change -> voltage-dependent lipid redistribution (e.g., phosphatidylserine flip-flop, cholesterol redistribution) -> altered lipid packing density -> changed condensate-membrane wetting affinity -> condensates either adhere to membrane (partial wetting) or release into cytoplasm (dewetting) -> spatial reorganization of condensate-associated functions

**Key prediction:** In giant unilamellar vesicles (GUVs) with reconstituted IDP condensates, application of a transmembrane voltage should shift the condensate-membrane contact angle in a voltage-dependent manner, with depolarization favoring dewetting and hyperpolarization favoring complete wetting.

**Generation technique:** New bridge mechanism (lipid packing, not calcium/pH)

---

## C2-H2: Wound-Induced Injury Currents Trigger Condensate Reorganization to Activate Regenerative Programs (FRESH — new context)

**Core claim:** The large injury potential gradient at wound sites (~200 mV/mm) is sufficient to trigger dramatic condensate reorganization in wound-edge cells through multiple converging mechanisms (pH shift from V-ATPase activation, calcium influx from voltage-gated channels, and potentially direct electric field effects on charged condensate-membrane interactions). This condensate reorganization activates the regenerative transcriptional program, and the speed of condensate response explains why wound healing begins within minutes of injury.

**Mechanism chain:** Tissue injury -> TEP disruption -> injury current (1-10 microA/cm2) -> strong local electric field at wound edge -> V-ATPase activation (rapid repolarization response) -> pH + Ca2+ changes -> condensate dissolution at wound edge -> release of sequestered mRNAs and transcription factors -> rapid activation of wound-healing gene expression

**Key prediction:** At wound edges, condensate density (measured by tagged IDP reporters) should drop dramatically within minutes of injury, faster than transcriptional responses. The drop should propagate from wound edge inward, following the injury current gradient. V-ATPase inhibition (bafilomycin A1) should block both the condensate dissolution wave and wound healing initiation.

**Generation technique:** Context transfer (wound healing as natural bioelectric perturbation experiment)

---

## C2-H3: Cancer Depolarization Drives Condensate Dissolution, Explaining the Stem-Cell-Like Transcriptional State (FRESH — new context)

**Core claim:** The constitutive depolarization of cancer cells (well-documented) dissolves a specific subset of repressive condensates that normally maintain differentiated gene silencing, releasing sequestered transcription factors and mRNAs. This provides a direct biophysical mechanism linking cancer-associated depolarization to the stem-cell-like transcriptional state that drives tumor aggressiveness, independent of genomic mutations.

**Mechanism chain:** Oncogenic transformation -> membrane depolarization (via K+ channel downregulation, Na+ influx) -> sustained Ca2+ elevation + pH alkalinization -> dissolution of repressive condensates containing Polycomb-group proteins or heterochromatin-associated phase-separated domains -> release of normally silenced developmental transcription factors -> stem-cell-like gene expression program -> increased proliferation and motility

**Key prediction:** (1) Cancer cells should have measurably lower condensate density of specific repressive condensates compared to their normal tissue counterparts. (2) Artificially hyperpolarizing cancer cells (e.g., ivermectin, which opens Cl- channels) should restore repressive condensate formation and reduce expression of stem-cell markers. (3) The condensate dissolution effect should correlate with degree of depolarization across a panel of cancer cell lines.

**Generation technique:** Adversarial inversion (cancer as failed bioelectric-condensate regulation)

---

## C2-H4: Evolved E1 Refinement — V-ATPase Node Network as a Computational Substrate (Building on E1)

**Core claim:** The V-ATPase-pH-condensate nodes described in E1 form a NETWORK via gap junction coupling that implements computation analogous to a neural network but using condensate states instead of action potentials. Each node has a binary state (condensate-present or condensate-absent), gap junctions share the electrochemical consequences of state changes between nodes, and the network settles into stable attractor states that correspond to specific morphological outcomes. This makes the condensate node network the physical substrate of Levin's "bioelectric code."

**Mechanism:** V-ATPase node i is in state S_i (1 = condensate present, 0 = absent). Gap junctions couple node i to neighbors j with coupling strength w_ij (determined by connexin expression). When node i forms a condensate, its Donnan potential propagates via gap junctions, shifting neighbors' electrochemical environment toward (or away from) their own condensate formation threshold. Network dynamics: dS_i/dt = f(V-ATPase_i, pH_i, sum_j(w_ij * S_j)). Stable attractors = morphogenetic target states.

**Key prediction:** The number of distinct stable morphological outcomes in a tissue should scale with the number of gap-junction-connected V-ATPase nodes, following attractor network scaling laws. Disrupting gap junction connectivity (but not V-ATPase function itself) should reduce the number of accessible morphological states, producing simpler (less differentiated) anatomical outcomes.

**Generation technique:** Analogy transfer (neural network attractor dynamics -> condensate node network)

---

## C2-H5: pH-Dependent Condensate Phase Diagram Predicts Tissue-Specific Vulnerability to Bioelectric Disruption (Building on E1 + E4)

**Core claim:** Different tissues express different IDP repertoires with different pH-dependent phase separation thresholds. Tissues where the dominant IDPs phase-separate near the normal cytoplasmic pH (~7.2) are most vulnerable to V-ATPase disruption because even small pH changes push them across the phase boundary. This predicts which tissues will show the earliest pathology upon bioelectric dysregulation and explains the tissue-selective vulnerability observed in neurodegenerative diseases.

**Mechanism:** Each tissue has a characteristic "condensate phase diagram" determined by its IDP proteome. The distance between normal operating pH and the phase boundary determines vulnerability. Neurons express TDP-43 and FUS (phase boundary near pH 7.0-7.3, close to cytoplasmic pH) -> high vulnerability. Muscle cells express different IDPs with phase boundaries further from operating pH -> lower vulnerability. V-ATPase decline shifts effective pH -> neurons cross phase boundary first.

**Key prediction:** Rank tissues by the proximity of their dominant IDP phase separation boundaries to cytoplasmic pH. This ranking should correlate with the known tissue vulnerability ordering in ALS (motor neurons first), Alzheimer's (hippocampus first), Parkinson's (substantia nigra first), and also with the tissue-specific expression of V-ATPase subunits.

**Generation technique:** Quantitative refinement of E4 using phase diagram framework
