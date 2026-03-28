# Cancer Recurrence Times from a Branching Process Model

**Authors:** Stefano Avanzini, Tibor Antal
**Year:** 2019
**Journal:** PLOS Computational Biology
**DOI:** 10.1371/journal.pcbi.1007423
**PMID:** 31751332; PMC: 6871767

## Abstract Summary
Models metastasis formation with a branching process: metastatic lesions initiated at rate depending on primary tumor size; each metastasis evolves as independent birth-death branching process. Parameters estimated for breast, colorectal, head/neck, lung, prostate cancers from clinical data.

## Key Findings

**Wide detectability gap:** Remarkably wide range of resection sizes where metastases are very likely present but undetectable — matches breast cancer dormancy observation.

**Recurrence probability:** Only very early resections can prevent recurrence; small delays in surgery significantly increase recurrence probability.

**Mathematical model:** Non-homogeneous Poisson process for metastasis initiation + independent branching processes for each metastasis growth.

**NOT ETAS/Hawkes:** The model does NOT use ETAS conditional intensity, Omori law, or self-exciting temporal clustering. No branching ratio analogous to ETAS n-parameter. No subcritical/supercritical phase transition analysis.

**Temporal pattern:** Recurrence times follow distributions derived from first-passage analysis of birth-death process — mean recurrence time shows logarithmic increase with detectable size.

## Relevance to MAGELLAN Pipeline
- Field C anchor paper for Candidate 4 (ETAS × Dormancy)
- Confirms: cancer dormancy uses branching processes, but NOT the ETAS-specific formalism
- Critical gap: no self-exciting temporal clustering, no Omori-law decay of recurrence risk, no branching ratio (n) equivalent
- ETAS would add: (1) recurrence events trigger additional recurrences (paracrine cascade), (2) temporal clustering of recurrence events (aftershock-like), (3) subcritical/supercritical phase transition for dormancy → proliferation switch
