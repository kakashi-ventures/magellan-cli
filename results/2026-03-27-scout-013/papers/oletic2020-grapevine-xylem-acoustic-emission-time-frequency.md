# Time-Frequency Features of Grapevine's Xylem Acoustic Emissions for Detection of Drought Stress

**Authors:** Oletic D, Rosner S, Zovko M, Bilas V
**Year:** 2020
**Journal:** Computers and Electronics in Agriculture
**DOI:** 10.1016/j.compag.2020.105797
**URL:** https://www.sciencedirect.com/science/article/abs/pii/S0168169920313648

## Abstract
Development of acoustic emission (AE) analysis methods to detect water stress in grapevines. Uses piezoelectric sensors to capture ultrasonic signals (100 kHz–1 MHz) from plant xylem cavitations. Software frequency-response compensation enables wideband spectral analysis with miniature resonant transducers.

## Key Findings Relevant to Candidate 4 (ML-AE × Plant Xylem Cavitation)

1. **AE source frequency signatures:** Three characteristic AE groups discriminated by spectral composition: (a) single-component near 200 kHz during stress, (b) multi-component 200–600 kHz under drought, (c) broadband emissions.
2. **Frequency-domain feature extraction:** Partial powers in frequency ranges 0–100 kHz, 100–200 kHz, 200–400 kHz, 400–800 kHz used as features — analogous to wavelet packet decomposition energy bands.
3. **No CNN/deep learning:** Feature extraction is manual/rule-based. Signal discrimination relies on pre-defined spectral criteria, NOT learned features from CWT scalogram + CNN pipeline.
4. **Drought sensitivity:** Feature set detects drought stress at leaf water potentials −0.7 to −1.2 MPa, across four grapevine cultivars.

## Gap Identified
This paper represents the current state of the plant AE field: manual frequency-band feature extraction. The gap to Candidate 4 is precisely that the full CWT scalogram generation + CNN classification pipeline from composite NDT has never been applied. Oletic 2020 does not use: continuous wavelet transform scalograms, convolutional neural networks, domain adaptation, or transfer learning from engineered materials.
