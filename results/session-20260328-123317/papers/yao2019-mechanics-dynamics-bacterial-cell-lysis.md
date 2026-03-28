---
title: "Mechanics and Dynamics of Bacterial Cell Lysis"
authors: Yao Z, et al.
year: 2019
doi: 10.1016/j.bpj.2019.04.040
pubmed_id: 31174849
url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6588734/
source: PMC (full text available)
relevance: T5 — Key paper on physical mechanics of beta-lactam-induced lysis
---

## Abstract / Key Content

Comprehensive physical model and experimental study of bacterial cell lysis in E. coli. Key findings:

- **Bulging timescale**: ~1 second (rapid formation of initial membrane bulge through cell wall defect)
- **Swelling timescale**: ~100 seconds (progressive enlargement of defect)
- **Lysis occurs when membranes exceed ~20% yield areal strain**
- Only turgor pressure (among turgor, mechanosensitive channels, cell shape) robustly modulates lysis
- Framework: free energy minimization, elastic shell theory for cell wall (rigid orthotropic cylindrical shell), fluid membrane mechanics with area stretch moduli

## What Mechanical Framework Is Used

Continuum elasticity approach with Lagrangian strain energy. The framework explicitly does NOT use:
- Griffith fracture mechanics
- Stress intensity factors K_I
- Energy release rate G
- Crack-tip stress singularities

Instead, it models cell wall defects as geometric openings through which membranes bulge, governed by osmotic pressure and membrane elastic properties.

## Key Finding for T5

The paper is the best existing treatment of physical lysis mechanics, but operates entirely in the membrane mechanics framework. The PG layer is treated as a "rigid shell with holes" — it does NOT model the PG network as a fracture mechanics material with crack tips, toughness parameters, or critical energy release rates.

The paper explicitly notes: "the mechanisms by which beta-lactam antibiotics mediate bacterial cell wall defect formation and cell lysis are poorly understood from a physical standpoint."

## Gap Confirmed

No paper yet asks: what is the fracture toughness K_IC of the PG mesh? What is G for a crosslink defect cluster growing under beta-lactam treatment? These are the T5 bridge concepts.
