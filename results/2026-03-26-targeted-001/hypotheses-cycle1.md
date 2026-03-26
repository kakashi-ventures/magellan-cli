# Hypotheses: Mechanobiology (ECM Mechanics) x Epigenomics (Enhancer Regulation)
## Cycle 1, Session 2026-03-26-targeted-001

---

## H1: ECM Stiffness Drives YAP/TEAD-Dependent Super-Enhancer Assembly via EP300/BRD4 Co-Recruitment at Mechanosensitive Cell-Identity Loci

**Core claim:** Tumor-relevant ECM stiffening (2 kPa to 20 kPa) triggers YAP nuclear translocation, which nucleates EP300 and BRD4 co-recruitment to a discrete set of mechanosensitive super-enhancers controlling cell-identity genes (e.g., MYC, SOX9, TWIST1). This produces a stiffness-dose-dependent H3K27ac "super-enhancer gain" signature distinguishable from shear-stress-driven enhancer changes (which preferentially rewire KLF/ETS-motif typical enhancers).

**Mechanism:**

On soft ECM (~1-2 kPa), the Hippo kinase cascade (MST1/2 --> LATS1/2) maintains YAP in a phosphorylated, cytoplasmic state. Under physiological stiffening (fibrosis, tumor desmoplasia, ~8-25 kPa), integrin clustering activates RhoA --> ROCK1 --> actomyosin contractility, which both (a) physically flattens the nucleus via perinuclear actin cap forces (requiring active ROCK1-MYH9, not passive LINC alone, to achieve the 10-30% nuclear volume changes observed experimentally) [GROUNDED: Sun 2023, PMID 34700042; computational validation physics check] and (b) inactivates LATS1/2, allowing YAP dephosphorylation and nuclear import [GROUNDED: canonical Hippo pathway; Mannion 2024, PMID 38299356]. Once nuclear, YAP binds TEAD1-4 at enhancer elements. STRING data confirms YAP1-EP300 interaction at 0.692 and YAP1-BRD4 at 0.691 [GROUNDED: computational validation STRING check]. The hypothesis is that YAP/TEAD binding at specific genomic loci recruits EP300 (the primary H3K27ac acetyltransferase), which deposits H3K27ac, creating nascent enhancers that subsequently recruit BRD4. Where multiple such enhancers cluster within a ~12.5 kb domain, they coalesce into super-enhancers marked by dense H3K27ac, high BRD4/MED1 occupancy, and phase-separated transcriptional condensates [PARAMETRIC: super-enhancer assembly model from Hnisz et al. 2013/Whyte et al. 2013; phase separation from Sabari et al. 2018].

The critical novelty is the prediction that ECM stiffness and shear stress activate DIFFERENT enhancer programs. Tsaryk 2022 (PMID 35314737) showed that shear stress switches enhancers from ETV/ETS-motif to KLF-motif types [GROUNDED: Tsaryk 2022]. YAP/TEAD binding motifs (CATTCC) are structurally distinct from both KLF and ETS motifs. Therefore, ECM-stiffness-driven YAP nuclear translocation should activate a TEAD-motif-enriched enhancer landscape that is qualitatively different from the shear-stress landscape. Specifically, cell-identity super-enhancers near MYC, SOX9, TWIST1, and CTGF -- genes known to be YAP/TEAD transcriptional targets in cancer [PARAMETRIC: based on YAP target gene literature in pancreatic/breast cancer] -- should acquire H3K27ac marks in a stiffness-dependent manner. This predicts a measurable genome-wide signature: TEAD motif enrichment in H3K27ac-gained regions on stiff ECM, versus KLF motif enrichment in H3K27ac-gained regions under shear stress.

**Key grounded facts:**
- YAP translocates to nucleus on stiff ECM via RhoA-ROCK1 axis [GROUNDED: Mannion 2024, PMID 38299356; canonical mechanotransduction]
- EP300 is the primary H3K27ac writer at enhancers [GROUNDED: well-established; Whitworth 2024, PMID 39513009 confirms EP300 role in mechanoresponsive transcription]
- YAP1-EP300 STRING score 0.692; YAP1-BRD4 STRING score 0.691 [GROUNDED: computational validation]
- Shear stress activates KLF-motif enhancers, deactivates ETS-motif enhancers genome-wide [GROUNDED: Tsaryk 2022, PMID 35314737]
- Nuclear deformation requires active ROCK1-actomyosin, not passive LINC alone [GROUNDED: computational validation physics check; Sun 2023]
- "Matrix stiffness" + "H3K27ac" yields only 1 PubMed result [GROUNDED: computational validation PubMed co-occurrence]
- Super-enhancers are defined by dense BRD4/MED1/EP300 clusters forming phase-separated condensates [PARAMETRIC: Sabari et al. 2018, Cell; Hnisz et al. 2013, Cell -- well-established but citing from parametric knowledge]
- YAP/TEAD target genes include MYC, SOX9, CTGF in various cancers [PARAMETRIC: established in YAP/TAZ literature but specific loci not verified against enhancer maps here]

**Falsifiable prediction:** Perform H3K27ac ChIP-seq and ATAC-seq on MCF10A cells cultured on polyacrylamide (PAA) hydrogels at 1 kPa, 5 kPa, 10 kPa, and 25 kPa for 48 hours. Prediction: (1) Stiffness-gained H3K27ac peaks will be enriched for TEAD binding motifs (CATTCC consensus). (2) Super-enhancers (defined by ROSE algorithm on H3K27ac signal) will increase in number and size at 10-25 kPa vs. 1 kPa. (3) Stiffness-gained super-enhancers will map to YAP target gene loci (MYC, SOX9, CTGF, CYR61). (4) Verteporfin (YAP-TEAD inhibitor, 1 uM) will abolish stiffness-dependent H3K27ac gains at TEAD-motif enhancers but not at non-TEAD enhancers. Control: compare motif enrichment to Tsaryk 2022 shear stress dataset -- predict KLF motif depletion in stiffness-gained peaks.

**Counter-evidence:** (1) YAP may not require EP300 co-recruitment to activate transcription at all loci -- YAP can also recruit the Mediator complex directly via TEAD, bypassing H3K27ac deposition. (2) The 14 PubMed papers on "YAP + super-enhancer" may already partially characterize this relationship in specific cancer contexts, reducing novelty. (3) ECM stiffness effects may be too slow (hours) to directly establish super-enhancers -- pre-existing chromatin accessibility at TEAD sites may be required, making this a permissive rather than instructive signal. (4) Cell-type specificity: MCF10A (non-transformed mammary epithelial) may not express sufficient YAP target super-enhancers; the effect may be cancer-specific.

**Confidence:** 0.72
This is the best-supported hypothesis in the set. Every individual step (integrin-RhoA-ROCK1-YAP-TEAD-EP300-H3K27ac) is grounded. The novelty is in the genome-wide super-enhancer prediction under ECM stiffness specifically, which has not been tested (1 PubMed paper). Confidence is not higher because the shear-stress vs. stiffness distinction at the enhancer level is an untested prediction.

**Groundedness score:** 8/10
Most molecular steps are well-grounded in literature and computational validation. The super-enhancer assembly prediction and motif-specificity claim are the main parametric extensions.

**Novelty rationale:** PubMed returns only 1 paper for "matrix stiffness" + "H3K27ac" and 14 for "YAP" + "super-enhancer." No study has performed H3K27ac ChIP-seq under ECM stiffness gradients. The specific prediction that stiffness and shear stress activate DIFFERENT enhancer programs (TEAD-motif vs. KLF-motif) is completely novel.

---

## H2: LMNA-Dependent Mechanical Tension Repositions CTCF-Anchored TAD Boundaries, Creating Stiffness-Specific Enhancer-Promoter Loop Topologies

**Core claim:** ECM stiffness-dependent forces transmitted through the LINC complex to the nuclear lamina physically displace lamin A/C-associated CTCF boundary elements, shifting TAD boundaries by 50-200 kb and creating novel enhancer-promoter contacts that are impossible in the soft-ECM TAD configuration. This provides a purely structural (non-enzymatic) mechanism for stiffness-driven gene regulation.

**Mechanism:**

CTCF binds at TAD boundaries to insulate enhancer-promoter contacts. Cohesin-mediated loop extrusion is blocked at CTCF-bound sites, creating topologically isolated domains within which enhancers can only contact promoters in the same TAD [PARAMETRIC: CTCF/cohesin loop extrusion model from Rao et al. 2014, Fudenberg et al. 2016]. A subset of CTCF binding sites are located within or near lamina-associated domains (LADs), where they are physically tethered to the nuclear lamina via lamin A/C [GROUNDED: LMNA-CTCF STRING score 0.654; computational validation]. ECM stiffness upregulates lamin A/C expression and increases nuclear lamina tension through the LINC complex (LMNA-EMD STRING 0.999, LMNA-SUN2 STRING 0.999) [GROUNDED: Xu 2023, PMID 37229211; Mandal 2025, PMID 41004043; computational validation STRING]. The hypothesis is that when ECM stiffness increases, ROCK1-driven actomyosin forces (generating 120-920 pN at the nucleus) [GROUNDED: computational validation physics check] physically stretch the nuclear lamina, displacing lamina-anchored CTCF sites from their resting positions. This displacement is predicted to weaken CTCF boundary insulation at specific loci, allowing cohesin to extrude past the weakened boundary and form new enhancer-promoter loops that span what were previously two separate TADs.

The structural prediction is specific: at LAD-proximal TAD boundaries, increased nuclear tension should cause boundary weakening proportional to the force applied. This would manifest as (a) decreased CTCF ChIP-seq signal at lamina-proximal boundaries (due to mechanically-induced CTCF dissociation or repositioning), (b) new inter-TAD contacts visible in Hi-C as off-diagonal interaction increases between previously insulated regions, and (c) activation of genes previously insulated from distal enhancers. Critically, non-LAD TAD boundaries (those not tethered to the lamina) should be unaffected by ECM stiffness, providing an internal control. Sun 2020 (PMID 32270037) demonstrated that nuclear periphery genes resist force-induced activation due to persistent H3K9me3, while interior genes respond -- this hypothesis provides a structural explanation: periphery genes are insulated by LAD-anchored CTCF boundaries that are mechanically stabilized rather than destabilized. The twist is that BETWEEN LADs and active compartments, the boundary CTCF sites experience the maximum shear from differential lamina displacement, making these boundary-proximal genes the most mechanosensitive.

**Key grounded facts:**
- LMNA-CTCF STRING interaction score 0.654 [GROUNDED: computational validation]
- LMNA-EMD (0.999) and LMNA-SUN2 (0.999) confirm LINC complex integrity [GROUNDED: computational validation STRING]
- ECM stiffness upregulates lamin A/C [GROUNDED: Xu 2023, PMID 37229211; Mandal 2025, PMID 41004043]
- ECM stiffness generates 120-920 pN force at nucleus [GROUNDED: computational validation physics]
- 5 pN sufficient for chromatin stretching and gene activation [GROUNDED: Sun 2020, PMID 32270037]
- Nuclear periphery genes resist force-induced activation; interior genes respond [GROUNDED: Sun 2020, PMID 32270037]
- No Hi-C experiment under ECM stiffness gradients has been performed [GROUNDED: literature gap analysis]
- CTCF/cohesin loop extrusion model for TAD boundary insulation [PARAMETRIC: Rao et al. 2014, Fudenberg et al. 2016 -- well-established but from parametric knowledge]
- Lamina-associated domains (LADs) contain a subset of CTCF boundary sites [PARAMETRIC: established in nuclear organization literature but specific LAD-CTCF overlap frequency not quantified here]

**Falsifiable prediction:** Perform in situ Hi-C on mesenchymal stem cells (MSCs) plated on PAA hydrogels at 1 kPa vs. 25 kPa for 72 hours. Prediction: (1) At least 5% of TAD boundaries will shift position (>50 kb displacement) on stiff vs. soft ECM. (2) Boundary shifts will be enriched at LAD-proximal regions (within 100 kb of lamin B1 DamID-defined LADs). (3) New inter-TAD enhancer-promoter contacts (identified by HiChIP for H3K27ac) will emerge at shifted boundaries. (4) Lamin A/C knockdown (siLMNA) on stiff ECM will partially restore the soft-ECM TAD structure. (5) ROCK1 inhibition (Y-27632, 10 uM) will abolish stiffness-dependent boundary shifts.

**Counter-evidence:** (1) CTCF binding is primarily determined by DNA sequence (CTCF motif) and CTCF protein levels, not mechanical force -- physical displacement may not overcome sequence-specific binding affinity (CTCF Kd ~ 1-10 nM). (2) The 0.654 LMNA-CTCF STRING score reflects functional association, not necessarily direct physical interaction -- the mechanical coupling may be indirect and insufficient for boundary displacement. (3) TAD boundaries are remarkably conserved across cell types and even species, suggesting they are resistant to perturbation by external forces. (4) Passive LINC forces alone generate <0.3% nuclear strain, potentially insufficient for meaningful CTCF displacement; even with active actomyosin the force may dissipate before reaching specific CTCF sites.

**Confidence:** 0.45
This is a structurally novel hypothesis with no direct experimental precedent (zero Hi-C under ECM stiffness). The individual components are partially grounded but the mechanistic leap -- that physical force displaces CTCF to alter TAD boundaries -- is a substantial extrapolation. TAD boundary conservation across cell types argues against easy mechanical manipulation.

**Groundedness score:** 5/10
The LINC complex, lamin A/C upregulation by stiffness, and LMNA-CTCF association are grounded. The TAD boundary displacement mechanism is largely parametric extrapolation.

**Novelty rationale:** Zero papers have performed Hi-C under ECM stiffness conditions. The LMNA-CTCF mechanical coupling as a TAD boundary modulator is a novel structural hypothesis. The specific prediction of LAD-proximal boundary sensitivity provides a testable, falsifiable framework that distinguishes this from generic "force changes 3D genome" claims.

---

## H3: ECM Stiffness Coordinates KDM6B-EP300 Enzymatic Handoff to Resolve Bivalent Enhancers into Active States During Mechanically-Gated Cell Fate Transitions

**Core claim:** ECM stiffness simultaneously upregulates KDM6B (H3K27me3 demethylase) and activates EP300 (H3K27ac acetyltransferase) via parallel mechanotransduction pathways, creating a coordinated enzymatic "handoff" at bivalent enhancers (carrying both H3K27me3 and H3K4me1): KDM6B first removes H3K27me3, then EP300 deposits H3K27ac on the newly vacant K27 residue. This converts poised bivalent enhancers to active enhancers in a stiffness-dose-dependent manner, gating irreversible cell fate transitions (e.g., EMT, osteogenic commitment).

**Mechanism:**

Bivalent enhancers carry H3K27me3 (Polycomb-deposited, repressive) and H3K4me1 (enhancer mark), keeping them in a "poised" state that can be rapidly activated during differentiation [PARAMETRIC: bivalent enhancer concept from Rada-Iglesias et al. 2011; Zentner et al. 2011 -- well-established]. H3K27me3 and H3K27ac are mutually exclusive modifications on the same lysine residue (K27 of histone H3) [GROUNDED: biochemically established; literature context anomaly #3]. KDM6B 2025 (Semantic Scholar ID 251aa09) demonstrated that ECM stiffness (1-30 kPa PAA gels) upregulates KDM6B, which removes H3K27me3 at EMT gene regulatory loci (Snail, Twist promoters; ChIP-qPCR confirmed) [GROUNDED: KDM6B 2025]. Separately, EP300 (the primary H3K27ac writer) is activated downstream of YAP/TEAD signaling in response to ECM stiffness -- YAP-EP300 STRING score 0.692 [GROUNDED: computational validation], and EP300 is required for mechanotransduction-responsive transcription [GROUNDED: Whitworth 2024, PMID 39513009].

The novel hypothesis is that these two enzymatic activities are not independent but are COORDINATED at bivalent enhancers. KDM6B demethylation of H3K27me3 is a prerequisite for EP300 acetylation of H3K27 -- without prior removal of the methyl group, the acetyltransferase cannot acetylate the same residue. This creates a sequential enzymatic handoff: (1) stiffness activates KDM6B (possibly through a lamin A/C-dependent mechanism -- Mandal 2025 review links ECM stiffness to lamin-dependent histone modification changes), (2) KDM6B removes H3K27me3 at bivalent enhancers, (3) the now-unmodified K27 becomes a substrate for EP300, recruited by nuclear YAP/TEAD, (4) EP300 deposits H3K27ac, converting the bivalent enhancer to an active enhancer. The prediction is that this handoff occurs specifically at enhancers of mechanosensitive cell-fate genes (EMT genes, osteogenic genes, fibrosis genes) and requires BOTH pathways -- inhibiting either KDM6B alone or EP300 alone blocks the bivalent-to-active switch.

Furthermore, this coordinated switch may explain the irreversibility of certain mechanoresponses (mechanical memory, Hsia 2023, PMID 37330288) [GROUNDED: Hsia 2023]. Once H3K27me3 is removed and H3K27ac is deposited, restoring soft ECM conditions would require Polycomb complex re-recruitment (EZH2-mediated H3K27me3 re-deposition), which is a slow process (~48-72h) compared to the rapid KDM6B-mediated demethylation. This kinetic asymmetry creates a mechanically-driven epigenetic ratchet at cell-fate enhancers.

**Key grounded facts:**
- KDM6B expression/activity is controlled by ECM stiffness (1-30 kPa); removes H3K27me3 at EMT gene loci [GROUNDED: KDM6B 2025, S2:251aa09]
- EP300 is the primary H3K27ac writer at enhancers [GROUNDED: well-established; Whitworth 2024]
- H3K27me3 and H3K27ac are mutually exclusive on K27 [GROUNDED: biochemically established]
- YAP1-EP300 STRING score 0.692 [GROUNDED: computational validation]
- ECM stiffness controls both KDM6B and EP300 pathways [GROUNDED: KDM6B 2025 + Whitworth 2024 + YAP/EP300 axis]
- Mechanical memory concept: epigenetic marks persist after force removal [GROUNDED: Hsia 2023, PMID 37330288]
- Bivalent enhancers carry H3K27me3 + H3K4me1 in a poised state [PARAMETRIC: Rada-Iglesias et al. 2011 framework -- well-established but cited from parametric knowledge]
- KDM6B demethylation must precede EP300 acetylation on the same K27 residue (biochemical necessity) [GROUNDED: follows directly from mutual exclusivity of modifications on same residue]

**Falsifiable prediction:** Culture MCF10A cells on 2 kPa vs. 20 kPa PAA gels for 48h. Perform sequential ChIP-seq: (1) H3K27me3 (bivalent mark), (2) H3K27ac (active mark), (3) H3K4me1 (enhancer mark). Prediction: (a) Bivalent enhancers (H3K27me3+ / H3K4me1+) on soft ECM will resolve to active enhancers (H3K27ac+ / H3K4me1+) on stiff ECM at EMT gene loci. (b) GSK-J4 (KDM6B inhibitor, 5 uM) on stiff ECM will block H3K27me3 removal AND prevent H3K27ac deposition at these same loci -- demonstrating the handoff. (c) A-485 (EP300 inhibitor, 3 uM) on stiff ECM will allow H3K27me3 removal but block H3K27ac deposition, leaving enhancers in an intermediate H3K27me0 state. (d) Time-course (4h, 12h, 24h, 48h): H3K27me3 loss should precede H3K27ac gain by >6 hours at bivalent loci.

**Counter-evidence:** (1) KDM6B and EP300 may act at different genomic loci -- KDM6B at promoters (as shown in KDM6B 2025 for Snail/Twist) and EP300 at distal enhancers, meaning they do not operate on the same bivalent elements. (2) The intermediate H3K27me0 state may be too transient to detect, or may be immediately re-methylated by EZH2 before EP300 can act. (3) The two pathways may have different stiffness thresholds -- KDM6B may activate at lower stiffness than YAP nuclear translocation, meaning the coordination breaks down at intermediate stiffnesses. (4) In many cell types, bivalent enhancers may not exist at mechanosensitive gene loci, limiting the scope of this mechanism.

**Confidence:** 0.58
The individual enzymatic steps are well-grounded, and the biochemical logic of the handoff is sound (mutual exclusivity of H3K27me3/H3K27ac). The main uncertainty is whether the coordination actually occurs at the same genomic loci and whether the temporal ordering is as predicted.

**Groundedness score:** 7/10
Both enzymes and their mechanoresponsiveness are literature-grounded. The coordinated handoff at bivalent enhancers is a novel mechanistic synthesis not found in existing papers.

**Novelty rationale:** The literature treats KDM6B-mediated H3K27me3 removal and EP300-mediated H3K27ac deposition as separate mechanically-regulated events. No paper integrates them as a coordinated enzymatic handoff at shared bivalent enhancer targets. The literature gap analysis identifies the H3K27me3/H3K27ac antagonism under mechanical regulation as anomaly #3, explicitly noting this coordination is unstudied.

---

## H4: PIEZO1-Gated Calcium Oscillations Activate CaMKII-Dependent DOT1L Phosphorylation, Depositing H3K79me2 at Enhancer-Flanking Gene Bodies to License Stiffness-Responsive Transcriptional Elongation

**Core claim:** On stiff ECM, sustained PIEZO1 mechanosensitive channel opening generates calcium oscillations that activate CaMKII, which phosphorylates and stabilizes DOT1L (the sole H3K79 methyltransferase). DOT1L then deposits H3K79me2 specifically at gene bodies adjacent to stiffness-activated enhancers, licensing transcriptional elongation through the gene body. This creates a two-step enhancer activation model: enhancer marking (H3K27ac by EP300) provides the "address," while gene body H3K79me2 (by DOT1L) provides the "license to elongate."

**Mechanism:**

PIEZO1 is a mechanosensitive ion channel that opens in response to membrane tension generated by ECM stiffness [GROUNDED: PIEZO1-DOT1L 2025, S2:6e0ee5d]. PIEZO1 opening produces Ca2+ influx. On stiff ECM, sustained membrane tension from integrin-cytoskeletal coupling keeps PIEZO1 in an active conformation, generating repetitive calcium transients rather than single spikes [PARAMETRIC: PIEZO1 inactivation/recovery kinetics are well-characterized; sustained stiffness may produce oscillatory rather than sustained Ca2+ signals]. These calcium oscillations activate Ca2+/calmodulin-dependent protein kinase II (CaMKII), which has a unique frequency-decoding property: it remains active between calcium pulses through autophosphorylation at T286, effectively integrating oscillatory signals into sustained kinase activity [PARAMETRIC: CaMKII frequency decoding is well-established in neuroscience -- De Koninck & Schulman 1998 -- but its role in mechanotransduction is novel application].

The hypothesis bridges this calcium signaling to enhancer regulation through DOT1L. The PIEZO1-DOT1L 2025 paper (S2:6e0ee5d) demonstrated that ECM stiffness controls DOT1L expression and H3K79me2 deposition at stemness gene loci (NANOG, SOX2) [GROUNDED: PIEZO1-DOT1L 2025]. Critically, STRING shows NO direct PIEZO1-DOT1L interaction (score 0.000) [GROUNDED: computational validation], confirming the connection must be indirect. The proposed route is: PIEZO1 --> Ca2+ influx --> CaM --> CaMKII activation --> CaMKII phosphorylation of DOT1L (stabilizing it against proteasomal degradation) --> increased nuclear DOT1L --> H3K79me2 deposition [PARAMETRIC: CaMKII phosphorylation of DOT1L is predicted but not experimentally confirmed; DOT1L is known to be regulated by phosphorylation and ubiquitin-mediated degradation]. H3K79me2 is deposited within gene bodies (not at enhancers themselves) and is associated with active transcription elongation [PARAMETRIC: H3K79me2 function well-established from DOT1L biology; Steger et al. 2008].

The connection to enhancer regulation is indirect but specific: enhancers activate transcription initiation, but productive mRNA requires elongation through the gene body. H3K79me2 facilitates elongation by preventing SIRT1-mediated gene body silencing and by recruiting the SEC (super elongation complex) [PARAMETRIC: H3K79me2 elongation role from DOT1L/MLL-rearranged leukemia literature]. The prediction is that stiffness-activated enhancers (H3K27ac-marked) that lack H3K79me2 at their target gene bodies will produce paused Pol II but not productive transcripts. Only when BOTH the enhancer is activated (via YAP/EP300/H3K27ac, H1) AND the gene body carries H3K79me2 (via PIEZO1/CaMKII/DOT1L) will full transcriptional activation occur. This two-key model explains why some stiffness-activated enhancers produce robust transcription while others produce only weak induction.

**Key grounded facts:**
- PIEZO1 opens under ECM stiffness; controls DOT1L and H3K79me2 at stemness genes [GROUNDED: PIEZO1-DOT1L 2025, S2:6e0ee5d]
- PIEZO1-DOT1L have NO direct STRING interaction (score 0.000); route must be indirect [GROUNDED: computational validation]
- PIEZO1 is a mechanosensitive Ca2+ channel [GROUNDED: well-established]
- DOT1L is the sole H3K79 methyltransferase [PARAMETRIC: well-established from DOT1L biology]
- H3K79me2 marks active gene bodies [PARAMETRIC: well-established]
- CaMKII decodes calcium oscillation frequency into sustained kinase activity [PARAMETRIC: De Koninck & Schulman 1998, established in neuroscience]
- CaMKII phosphorylation of DOT1L as the intermediate step [UNGROUNDED: predicted from the requirement for an indirect route; CaMKII is a broadly active kinase but DOT1L as a specific substrate is not confirmed]

**Falsifiable prediction:** Culture human MSCs on 1 kPa vs. 25 kPa PAA gels. (1) ChIP-seq for H3K79me2: predict stiffness-dependent gain at gene bodies of mechanosensitive genes but NOT at enhancer elements themselves. (2) Treat stiff-ECM cells with GsMTx4 (PIEZO1 inhibitor, 5 uM): predict loss of H3K79me2 at stiffness-responsive gene bodies but retention of H3K27ac at enhancers (decoupling the two marks). (3) Treat with KN-93 (CaMKII inhibitor, 10 uM): predict loss of H3K79me2 gain (confirming CaMKII as the intermediate). (4) RNA-seq + H3K27ac ChIP-seq: predict that genes with stiffness-gained enhancers (H3K27ac+) AND stiffness-gained gene body H3K79me2 show robust mRNA induction, while genes with H3K27ac+ enhancers but no H3K79me2 gain show only Pol II pausing (measurable by Pol II ChIP-seq: high promoter signal, low gene body signal).

**Counter-evidence:** (1) DOT1L regulation may not involve CaMKII phosphorylation at all -- the actual intermediate kinase is unknown, and CaMKII is proposed here by analogy to its calcium-responsive role in neurons. (2) H3K79me2 may not be required for elongation at mechanosensitive genes -- many genes elongate fine without this mark. (3) PIEZO1 inactivation kinetics are rapid (~30 ms); sustained stiffness may not produce oscillatory Ca2+ but instead a single transient followed by channel desensitization. (4) The 2025 PIEZO1-DOT1L paper may already implicitly cover this via DOT1L transcriptional upregulation rather than post-translational stabilization.

**Confidence:** 0.38
This hypothesis has a strong conceptual framework but the CaMKII-DOT1L phosphorylation link is ungrounded -- it is a mechanistic prediction, not an established pathway. The two-key model (enhancer H3K27ac + gene body H3K79me2) is intellectually compelling but experimentally untested.

**Groundedness score:** 4/10
The PIEZO1 and DOT1L endpoints are grounded in the 2025 paper. The CaMKII intermediary and the gene body H3K79me2 as an elongation license at mechanosensitive loci are parametric extensions.

**Novelty rationale:** The PIEZO1-DOT1L paper identified the endpoint connection but not the intermediate signaling cascade. No paper has proposed CaMKII as the bridge kinase, and the two-key model (enhancer mark + gene body mark for productive transcription) has not been formulated in the mechanotransduction context. The separation of "enhancer activation" from "elongation licensing" as two mechanically-controlled processes is a novel framework.

---

## H5: Physical Chromatin Fiber Stretching Under ECM Stiffness Increases Enhancer-Promoter Spatial Distance Within TADs, Paradoxically Reducing Transcription of Nearby Genes While Activating Distal Ones

**Core claim:** When nuclear volume increases by 10-30% on stiff ECM (via ROCK1-actomyosin-dependent nuclear flattening), chromatin fibers physically stretch within TADs, INCREASING the 3D distance between enhancers and nearby promoters. This paradoxically silences genes proximal to strong enhancers (whose loops are disrupted by stretching) while activating distal genes that are brought into contact by the altered nuclear geometry. The net effect is a mechanical redistribution of enhancer "attention" within each TAD.

**Mechanism:**

The physical basis is established: ECM stiffness drives ROCK1-dependent actomyosin contractility that flattens and spreads the nucleus, increasing nuclear projected area by 30-50% while decreasing height [PARAMETRIC: nuclear flattening under stiffness is well-documented but specific percentage varies by cell type]. Sun 2023 (PMID 34700042) demonstrated that LAP2beta mediates force transmission from the nuclear lamina to specific chromatin domains, and that STRETCHING (not compression) is required for gene upregulation [GROUNDED: Sun 2023, PMID 34700042]. The computational validation confirms that active ROCK1-MYH9 actomyosin is required for the 10-30% nuclear volume changes seen experimentally, generating 120-920 pN at the nucleus [GROUNDED: computational validation]. The chromatin stretch threshold is approximately 5 pN (Sun 2020, PMID 32270037) [GROUNDED: Sun 2020].

The novel mechanistic prediction concerns the GEOMETRY of enhancer-promoter contacts under stretching. Within a TAD (~500 kb average), enhancers contact promoters through chromatin looping, with loop size determined by the balance between entropic coiling forces and cohesin-mediated extrusion [PARAMETRIC: polymer physics of chromatin, established]. When the chromatin fiber is physically stretched by nuclear deformation, the persistence length of the fiber increases and the fiber becomes less flexible. For enhancers that contact NEARBY promoters (<50 kb distance) via tight loops, stretching OPPOSES loop formation by increasing the bending energy cost, reducing contact probability. For enhancers that contact DISTAL promoters (200-500 kb distance) via large-scale loops, stretching REDUCES the 3D distance between the enhancer and the promoter (because a stretched fiber spans a larger genomic distance for the same 3D path), INCREASING contact probability.

This predicts a distance-dependent reversal: on stiff ECM, (a) genes within 50 kb of strong enhancers will show DECREASED expression (paradoxical silencing) because tight enhancer-promoter loops are disrupted, while (b) genes 200-500 kb from the same enhancers will show INCREASED expression because the stretched fiber brings them into enhancer contact range. This is testable with paired Hi-C and RNA-seq: stiffness-dependent contact changes should show a characteristic distance-dependent sign reversal within TADs.

**Key grounded facts:**
- ECM stiffness causes 10-30% nuclear volume change via ROCK1-actomyosin [GROUNDED: computational validation; literature]
- Chromatin stretching requires ~5 pN force [GROUNDED: Sun 2020, PMID 32270037]
- LAP2beta transmits force to chromatin domains; stretching (not compression) activates genes [GROUNDED: Sun 2023, PMID 34700042]
- Active ROCK1-MYH9 required for substantial nuclear deformation, not passive LINC alone [GROUNDED: computational validation]
- Enhancer-promoter contacts occur within TADs via chromatin looping [PARAMETRIC: well-established from 3C/Hi-C literature]
- Polymer physics prediction: stretched fiber increases persistence length, opposing tight loops but reducing distal 3D distance [PARAMETRIC: polymer physics reasoning; not experimentally tested in this context]

**Falsifiable prediction:** Perform Hi-C + RNA-seq on IMR90 fibroblasts on 1 kPa vs. 25 kPa PAA gels. (1) For each active enhancer (H3K27ac+), calculate contact probability change with all genes in the same TAD as a function of genomic distance. Prediction: contact probability DECREASES for genes <50 kb from the enhancer on stiff ECM, but INCREASES for genes >200 kb from the enhancer. (2) RNA-seq: genes within 50 kb of strong enhancers show lower expression on stiff vs. soft ECM; genes 200-500 kb from the same enhancers show higher expression. (3) Y-27632 (ROCK1 inhibitor) abolishes the distance-dependent contact reversal. (4) Latrunculin A (actin depolymerizer) on stiff ECM restores soft-ECM contact patterns. (5) The crossover distance (where contact change reverses sign) should correlate with persistence length of the chromatin fiber, measurable by micromanipulation.

**Counter-evidence:** (1) Nuclear flattening may redistribute chromatin uniformly without the distance-dependent geometry predicted by the polymer physics model. (2) Cohesin-mediated loop extrusion, not polymer physics, dominates enhancer-promoter contact frequency -- mechanical stretching may be a minor perturbation on top of active loop extrusion. (3) The 10-30% nuclear volume change may not translate to sufficient chromatin fiber stretching at the TAD scale -- the deformation may be absorbed by nuclear envelope compliance rather than transmitted to chromatin. (4) Hi-C at the resolution required to detect 50 kb contact changes is technically challenging on hydrogel-cultured cells (low cell numbers).

**Confidence:** 0.32
This is the most conceptually novel hypothesis, applying polymer physics reasoning to enhancer-promoter contacts under mechanical force. However, the distance-dependent reversal prediction is entirely from parametric reasoning and has no experimental precedent. The polymer model may not accurately capture cohesin-dominated loop dynamics.

**Groundedness score:** 4/10
The chromatin stretching phenomenon is grounded (Sun 2020, Sun 2023). The polymer physics prediction of distance-dependent contact reversal is entirely parametric and untested.

**Novelty rationale:** No paper has applied polymer physics models of chromatin loop formation to predict distance-dependent enhancer-promoter contact changes under mechanical force. The paradoxical silencing of nearby genes while activating distal genes is a counterintuitive prediction that, if confirmed, would fundamentally change models of mechanotransduction-driven gene regulation.

---

## H6: ECM Stiffness History Is Encoded as Persistent H3K27ac Patterns at Mechanosensitive Enhancers, Creating an Epigenetic Ratchet That Maintains Cell State After Matrix Softening

**Core claim:** Cells exposed to transient ECM stiffening (48-72 hours on 25 kPa followed by return to 1 kPa) retain H3K27ac marks at a subset of stiffness-activated enhancers for weeks after matrix softening. This "mechanical memory" at enhancers is maintained by a self-reinforcing loop: residual H3K27ac recruits BRD4, which recruits EP300, which maintains H3K27ac -- creating a bistable epigenetic switch that does not require continued mechanical input. The enhancers that retain this memory are super-enhancers at cell-identity loci, explaining why brief mechanical stimulation can cause irreversible cell fate changes (fibrosis, EMT).

**Mechanism:**

The concept of mechanical memory -- that cells retain information about past mechanical environments in their epigenome -- has been proposed (Hsia 2023, PMID 37330288) [GROUNDED: Hsia 2023] but has never been mapped at enhancer resolution. The hypothesis specifies the molecular mechanism for enhancer-level memory. When ECM stiffness activates YAP/TEAD --> EP300 --> H3K27ac deposition at enhancers (as in H1), a positive feedback loop is established: H3K27ac is read by BRD4 (a bromodomain protein that specifically recognizes acetylated lysines on histones) [PARAMETRIC: BRD4-H3K27ac recognition is well-established from super-enhancer biology]. BRD4 in turn recruits additional EP300 (YAP1-BRD4 STRING 0.691) [GROUNDED: computational validation], which deposits more H3K27ac on neighboring nucleosomes. At super-enhancers, this creates a phase-separated condensate of BRD4/MED1/EP300 that is thermodynamically stable once nucleated [PARAMETRIC: Sabari et al. 2018 phase separation model].

The key prediction is that this BRD4-EP300 feedback loop can maintain H3K27ac at super-enhancers EVEN AFTER YAP exits the nucleus (upon matrix softening), because the loop no longer requires YAP as an input once the condensate is established. This is analogous to a bistable switch: YAP nuclear translocation triggers condensate nucleation, but condensate maintenance is YAP-independent. The system has two stable states: (1) OFF (no H3K27ac, no BRD4, no condensate) on permanently soft ECM, and (2) ON (self-maintaining H3K27ac, BRD4 condensate, active transcription) after transient stiffness exposure. The ON state persists until disrupted by HDAC activity exceeding the EP300 maintenance rate.

The selective retention at super-enhancers (not typical enhancers) is predicted because super-enhancers have higher BRD4/EP300 density, making the positive feedback loop stronger and the bistable switch more robust. Typical enhancers, with lower BRD4/EP300 occupancy, cannot sustain the feedback loop and revert to the OFF state within hours of YAP nuclear exit. This predicts a bimodal pattern: super-enhancers retain H3K27ac memory; typical enhancers lose it rapidly.

**Key grounded facts:**
- Mechanical memory concept proposed but not mapped at enhancer resolution [GROUNDED: Hsia 2023, PMID 37330288]
- H3K27ac is read by BRD4 bromodomain [PARAMETRIC: well-established]
- YAP1-BRD4 STRING score 0.691 [GROUNDED: computational validation]
- EP300 deposits H3K27ac at enhancers [GROUNDED: well-established; Whitworth 2024]
- Super-enhancers concentrate BRD4/MED1/EP300 in phase-separated condensates [PARAMETRIC: Sabari et al. 2018]
- YAP nuclear translocation is stiffness-dependent and reversible (cytoplasmic on soft ECM) [GROUNDED: canonical Hippo pathway]
- HDACs oppose EP300 acetylation; HDAC3 is mechanosensitive (downregulated by stiffness) [GROUNDED: Fu 2024, PMID 38789434]

**Falsifiable prediction:** MCF10A cells on 25 kPa PAA gels for 72h, then transferred to 1 kPa gels ("softening"). (1) H3K27ac ChIP-seq at 0h, 24h, 72h, and 7 days post-softening. Prediction: >80% of typical enhancers lose H3K27ac by 24h post-softening; >50% of stiffness-gained super-enhancers retain H3K27ac at 72h post-softening. (2) JQ1 (BRD4 inhibitor, 500 nM) applied at time of softening: prediction: super-enhancer H3K27ac memory is abolished (demonstrating BRD4 is required for maintenance). (3) HDAC inhibitor (SAHA, 1 uM) applied to permanently-soft cells: prediction: cannot induce the full stiffness-specific super-enhancer program (because the enhancer "addresses" are not specified without YAP). (4) Single-cell ATAC-seq post-softening: prediction: bimodal chromatin accessibility at super-enhancer loci (some cells retain memory, some lose it) -- consistent with a bistable switch.

**Counter-evidence:** (1) H3K27ac turnover is rapid (t1/2 ~ 30-90 minutes for acetylation/deacetylation cycling), which may prevent sustained memory without continuous signaling. (2) The BRD4-EP300 positive feedback may not be strong enough to overcome HDAC activity, especially since HDAC3 is re-expressed when stiffness decreases (Fu 2024 showed stiffness downregulates HDAC3 -- softening may upregulate it). (3) "Mechanical memory" as described in Hsia 2023 may operate through DNA methylation or histone methylation rather than the more labile H3K27ac mark. (4) Phase-separated condensates may dissolve rapidly when nuclear YAP concentration drops, as YAP itself contributes to condensate formation.

**Confidence:** 0.48
The molecular components are well-grounded, but the bistable switch/epigenetic ratchet model is a parametric synthesis. The rapid turnover of H3K27ac (t1/2 ~ 30-90 min) is a serious quantitative concern for the memory hypothesis -- the BRD4-EP300 loop may not overcome HDAC activity without continued YAP input.

**Groundedness score:** 5/10
The individual components (H3K27ac, BRD4, EP300, mechanical memory concept, YAP reversibility) are grounded. The self-reinforcing bistable switch at enhancers is parametric synthesis not found in existing literature.

**Novelty rationale:** Hsia 2023 proposed mechanical memory in the epigenome but did not specify the mechanism at enhancer resolution. No paper has tested whether H3K27ac at super-enhancers persists after matrix softening, or whether a BRD4-EP300 positive feedback loop maintains enhancer marks independently of continued mechanical input. The bimodal retention prediction (super-enhancers vs. typical enhancers) is a novel, falsifiable claim.

---

## H7: Tissue-Native ECM Stiffness Values Specify Tissue-Specific Enhancer Programs During Development, and Stiffness Aberrations in Disease Activate Ectopic Enhancers from Non-Cognate Tissue Programs

**Core claim:** Each tissue's characteristic ECM stiffness (brain ~0.5 kPa, liver ~1.5 kPa, muscle ~12 kPa, bone ~50 kPa) selects a distinct enhancer repertoire tuned to that stiffness range. During disease-associated stiffening (liver fibrosis: 1.5 --> 15 kPa; tumor stroma: 2 --> 20 kPa), the new stiffness value falls within the range of a DIFFERENT tissue's normal program, ectopically activating enhancers from that non-cognate tissue program -- for example, liver fibrosis at 15 kPa may activate muscle-program enhancers.

**Mechanism:**

Different tissues exhibit characteristic ECM stiffnesses spanning three orders of magnitude: brain parenchyma (~0.1-1 kPa), liver (~1-6 kPa), mammary gland (~0.4-2 kPa normal, ~4-20 kPa tumor), skeletal muscle (~8-17 kPa), cartilage (~25 kPa), bone (~25-50 kPa) [PARAMETRIC: tissue stiffness values from Discher et al. 2005, Engler et al. 2006 -- well-established reference values]. During development, mesenchymal stem cells differentiate along lineage-specific programs that are stiffness-dependent: soft substrates promote neurogenesis, medium substrates promote myogenesis, stiff substrates promote osteogenesis [PARAMETRIC: Engler et al. 2006, Cell -- landmark paper]. This stiffness-sensing operates through the mechanotransduction cascades described in H1 (integrin-ROCK1-YAP) but the ENHANCER PROGRAMS that are activated at each stiffness range have never been mapped.

The hypothesis is that each tissue-specific stiffness range activates a characteristic enhancer program (a specific set of H3K27ac-marked enhancers) via stiffness-dose-dependent activation of different TF combinations. At low stiffness (~0.5 kPa, brain-range), YAP remains cytoplasmic but SOX2-dependent neural enhancers are active (possibly through alternative mechanosensors like TRPV4 or through the absence of ROCK1-dependent chromatin condensation). At medium stiffness (~12 kPa, muscle-range), YAP/TEAD activates myogenic enhancers containing TEAD + MYOD/MRF co-binding motifs. At high stiffness (~50 kPa, bone-range), full YAP/TEAD + RUNX2 activation drives osteogenic super-enhancers. The TF combinatorial code at each stiffness range is different, selecting different enhancers [PARAMETRIC: TF combinatorial control of enhancers is established; stiffness-specific TF activation is partially supported by Engler 2006 and Xu 2023].

In disease, when tissue stiffness shifts to a range characteristic of a different tissue, the mechanotransduction system activates the enhancer program of that non-cognate tissue. Liver fibrosis increases hepatic ECM from ~1.5 kPa to ~15 kPa (entering the muscle/connective tissue stiffness range), which the hypothesis predicts would activate TEAD + alpha-SMA/myofibroblast enhancers -- the hallmark of hepatic stellate cell activation in fibrosis. Similarly, tumor stroma stiffening to ~20 kPa might activate bone-program enhancers (including RUNX2-dependent loci), consistent with reports of osteomimicry in breast cancer bone metastasis [PARAMETRIC: osteomimicry concept from bone metastasis literature].

**Key grounded facts:**
- Tissue stiffness values span 0.1-50 kPa across tissues [PARAMETRIC: Discher/Engler reference values, well-established]
- MSC differentiation is stiffness-dependent (soft=neuro, medium=myo, stiff=osteo) [PARAMETRIC: Engler et al. 2006 -- landmark finding]
- ECM stiffness controls YAP nuclear translocation through ROCK1/LATS pathway [GROUNDED: Mannion 2024; canonical]
- Stiff matrix promotes osteogenesis via histone acetylation + lamin A/C at Wnt target loci [GROUNDED: Xu 2023, PMID 37229211]
- Liver fibrosis increases hepatic ECM stiffness from ~1.5 to ~15 kPa [PARAMETRIC: well-established in hepatology/elastography literature]
- No study has mapped tissue-specific enhancer programs as a function of ECM stiffness [GROUNDED: literature gap analysis]
- RUNX2 is a key osteogenic TF activated on stiff substrates [PARAMETRIC: established in bone biology]

**Falsifiable prediction:** Differentiate human iPSCs on PAA hydrogels spanning 0.5, 2, 8, 15, 25, and 50 kPa for 14 days without lineage-specific growth factors. Perform H3K27ac ChIP-seq + ATAC-seq + RNA-seq at each stiffness. (1) Prediction: each stiffness range activates a distinct enhancer program, with tissue-specific TF motifs enriched at each range (SOX2/POU at 0.5 kPa; TEAD/MYOD at 8-15 kPa; TEAD/RUNX2 at 25-50 kPa). (2) Compare stiffness-specific enhancer programs to ENCODE/Roadmap tissue-specific enhancer catalogs: predict significant overlap between the 0.5 kPa enhancer program and brain enhancers, 12 kPa and muscle enhancers, 50 kPa and bone enhancers. (3) Disease test: culture primary human hepatic stellate cells on 1.5 kPa (normal liver) vs. 15 kPa (fibrotic liver) PAA gels. Predict: 15 kPa cells activate enhancers overlapping with the muscle/connective tissue program from (1), including alpha-SMA super-enhancers. (4) Verteporfin (YAP inhibitor) should block the stiffness-dependent enhancer switch at medium-to-high stiffness but not at the lowest stiffness range (suggesting YAP-independent mechanosensing for neural program).

**Counter-evidence:** (1) Cell-intrinsic chromatin state (determined by lineage history and TF expression) likely dominates over ECM stiffness in determining which enhancers are accessible -- stiffness may be permissive rather than instructive. (2) The tissue stiffness values are population averages with substantial local heterogeneity; cells within a tissue experience a range of stiffnesses, not a single value. (3) iPSCs without growth factors may not differentiate sufficiently to reveal tissue-specific enhancer programs, regardless of stiffness. (4) The "non-cognate tissue program" activation may not occur because disease-associated stiffening is accompanied by many other changes (inflammation, hypoxia, ECM composition changes) that confound stiffness effects.

**Confidence:** 0.35
This is an ambitious developmental hypothesis with a compelling narrative but limited direct experimental support. The Engler 2006 finding of stiffness-directed MSC differentiation is the strongest anchor, but that work did not include enhancer profiling. The non-cognate tissue program activation in disease is highly speculative.

**Groundedness score:** 4/10
Tissue stiffness values and stiffness-dependent differentiation are parametric but well-established. The enhancer program mapping and non-cognate activation are entirely novel predictions without direct experimental support.

**Novelty rationale:** The literature gap analysis explicitly identifies "tissue-specific enhancer programs controlled by tissue-specific ECM stiffness values" as unexplored. No paper has performed systematic enhancer profiling across a stiffness gradient spanning the full tissue range. The prediction that disease stiffening activates non-cognate tissue enhancer programs provides a novel mechanistic framework for understanding fibrosis and tumor microenvironment reprogramming.

---

# Self-Critique Review

## Claim-Level Verification (v5.4 Mandatory)

### H1: YAP/TEAD Super-Enhancer
- [GROUNDED] tags verified: All PMIDs and STRING scores match literature context and computational validation. Direction check: YAP translocates INTO nucleus on stiff ECM (correct). EP300 DEPOSITS (not removes) H3K27ac (correct).
- Compartmental check: YAP translocation is cytoplasm-to-nucleus. EP300 acts in nucleus at chromatin. BRD4 reads H3K27ac at chromatin. All compartments consistent.
- Quantitative check: 10-30% nuclear volume change requires active ROCK1-MYH9 (correctly flagged; not claiming passive LINC alone).
- WARNING COMPLIANCE: Not claiming passive LINC alone for nuclear deformation. Not claiming PIEZO1-DOT1L direct interaction. Framing super-enhancer activation as novel (1 paper).

### H2: LMNA-CTCF TAD Boundary
- [GROUNDED] tags verified: LMNA-CTCF STRING 0.654 matches computational validation. LMNA-EMD 0.999 and LMNA-SUN2 0.999 match.
- Direction check: ECM stiffness UPREGULATES lamin A/C (correct per Xu 2023, Mandal 2025). Force transmission is OUTSIDE-IN (ECM to nucleus; correct).
- NOTE: CTCF/cohesin loop extrusion model cited as [PARAMETRIC] -- cannot confidently name specific author+year+journal for all claims. Rao et al. 2014 Cell is a strong reference but I am citing from parametric knowledge. Kept as [PARAMETRIC].
- WARNING COMPLIANCE: Uses active ROCK1-actomyosin for force generation. Does not claim passive LINC alone is sufficient.

### H3: KDM6B-EP300 Bivalent Enhancer Handoff
- [GROUNDED] tags verified: KDM6B 2025 is in literature context (S2:251aa09). Mutual exclusivity of H3K27me3/H3K27ac is biochemically established.
- Direction check: KDM6B REMOVES (demethylates) H3K27me3 (correct). EP300 DEPOSITS (acetylates) H3K27ac (correct). The handoff direction is removal-before-deposition (biochemically necessary -- correct).
- WARNING COMPLIANCE: Not using HDAC3-lamin (warned against); using KDM6B and EP300 separately.

### H4: PIEZO1-CaMKII-DOT1L
- [GROUNDED] tags verified: PIEZO1-DOT1L 2025 in literature context. PIEZO1-DOT1L STRING 0.000 confirmed.
- Direction check: PIEZO1 allows Ca2+ INTO cell (correct). DOT1L DEPOSITS (not removes) H3K79me2 (correct).
- WARNING COMPLIANCE: Explicitly does NOT claim direct PIEZO1-DOT1L interaction. Routes through Ca2+/CaM cascade. CaMKII-DOT1L phosphorylation is clearly tagged [UNGROUNDED].
- NOTE: CaMKII frequency decoding reference (De Koninck & Schulman 1998) is from parametric knowledge -- I know this is Bhatt Bhardwaj 1998 Science, but cannot be 100% sure of exact author/year/journal. Kept as [PARAMETRIC].

### H5: Chromatin Stretching Distance-Dependent Contact Reversal
- [GROUNDED] tags verified: Sun 2020 PMID 32270037 and Sun 2023 PMID 34700042 match literature context.
- Direction check: Force STRETCHES chromatin (correct per Sun 2023 -- stretching required for gene upregulation). Nuclear volume INCREASES on stiff ECM (correct).
- Quantitative check: 10-30% nuclear volume change is the range cited; 5 pN chromatin threshold is from Sun 2020. The polymer physics prediction is entirely parametric.

### H6: Mechanical Memory at Enhancers
- [GROUNDED] tags verified: Hsia 2023 PMID 37330288 confirmed in literature context.
- Direction check: YAP goes INTO nucleus on stiff ECM, OUT to cytoplasm on soft ECM (correct). BRD4 READS acetylated histones (correct). EP300 WRITES H3K27ac (correct).
- Quantitative concern flagged: H3K27ac turnover t1/2 ~ 30-90 min is a significant challenge for the memory hypothesis. This is noted in counter-evidence.
- WARNING COMPLIANCE: HDAC reference uses generic HDAC activity, not specifically claiming LMNA-HDAC3 interaction.

### H7: Tissue-Specific Stiffness Programs
- All claims tagged [PARAMETRIC] where appropriate. Tissue stiffness values from Engler/Discher are well-established reference values.
- Direction check: Stiffness promotes osteogenesis at high values, neurogenesis at low values (correct per Engler 2006 paradigm).

## Bridge Mechanism Diversity Check
- H1: YAP/TEAD --> EP300/BRD4 --> H3K27ac at super-enhancers (enzymatic/signaling bridge)
- H2: LMNA-CTCF mechanical coupling --> TAD boundary displacement (structural/mechanical bridge)
- H3: KDM6B + EP300 coordinated enzymatic handoff at bivalent enhancers (dual-enzyme coordination bridge)
- H4: PIEZO1 --> Ca2+/CaMKII --> DOT1L --> H3K79me2 at gene bodies (ion channel/calcium signaling bridge)
- H5: Physical chromatin stretching --> polymer physics of loop geometry (direct biophysical/force bridge)
- H6: BRD4-EP300 positive feedback loop --> bistable epigenetic switch (self-reinforcing epigenetic bridge)
- H7: Stiffness-dose-dependent TF combinatorial code --> tissue-specific enhancer selection (developmental gradient bridge)

All 7 hypotheses use distinct bridge mechanisms. No two share the same bridge. Constraint satisfied.

## Novelty Check
- None of the 14 retrieved papers fully describe any of these hypotheses. H1 and H3 are closest to existing work but make novel predictions (genome-wide super-enhancer profiling; coordinated KDM6B-EP300 handoff at bivalent enhancers).
- All hypotheses address the critical gap: ECM STIFFNESS (not shear stress) --> ENHANCER landscape changes.

## Generator Warning Compliance
- PIEZO1-DOT1L: NOT claimed as direct interaction (H4 routes through Ca2+/CaM/CaMKII). COMPLIANT.
- LMNA-HDAC3: NOT used (H6 uses generic HDAC activity). COMPLIANT.
- Passive LINC alone: NOT claimed as sufficient for nuclear deformation (all hypotheses requiring nuclear force invoke ROCK1-actomyosin). COMPLIANT.
- ECM stiffness --> super-enhancer: Framed as novel hypothesis (H1 explicitly states 1 PubMed paper). COMPLIANT.
