# Deep Learning Approach for Damage Classification Based on Acoustic Emission Data in Composite Materials

**Authors:** Guo F, Li W, Jiang P, Chen F, Liu Y
**Year:** 2022
**Journal:** Materials (MDPI)
**DOI:** 10.3390/ma15124270
**PMID:** N/A (engineering journal)
**URL:** https://pmc.ncbi.nlm.nih.gov/articles/PMC9227811/

## Abstract
Application of acoustic emission (AE) techniques to detect three damage types in carbon fiber-reinforced polymer composites: fiber breakage, matrix cracking, and delamination. The InceptionTime deep learning model is compared to wavelet-based CNN approaches for time series classification of raw AE signals.

## Key Findings Relevant to Candidate 4 (ML-AE × Plant Xylem Cavitation)

1. **CWT+CNN pipeline:** Converting AE signals to CWT scalograms for CNN classification achieves ~84.6–94.3% accuracy for composite damage mode classification.
2. **InceptionTime surpasses CWT+CNN:** Raw time-series InceptionTime achieves ~99.8% accuracy — but CWT scalogram approach remains the dominant published method for failure mode discrimination (interpretable feature space matching physical damage modes).
3. **Feature space:** Damage modes discriminated by characteristic frequency ranges: fiber breakage (high frequency), matrix cracking (mid), delamination (low-mid). This frequency-domain signature principle is directly analogous to plant AE source discrimination (cavitation vs. mechanical cracking vs. embolism propagation).
4. **Domain specificity:** Entirely focused on composite NDT. No plant biology or hydraulic applications.

## Relevance to Disjointness
This paper represents the composites NDT state of the art. The CWT+CNN pipeline is mature in this domain (2018–2025 literature) but has never been transferred to plant xylem AE source classification. The frequency signature concept maps directly: plant AE sources (cavitation, bark cracking, embolism) each have distinct frequency bands that CWT scalogram + CNN could discriminate — the bridge exists methodologically but has never been made.
