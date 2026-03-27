# GPT-5.4 Validation — EVT × Proteome Thermal Stability

**Model**: gpt-5.4 (reasoning effort: high, web search: enabled, code interpreter: enabled)
**Duration**: 604s
**Web searches performed**: 25
**Code executions**: 13

---

## Reasoning Summary

**Planning a detailed search**

I need to ensure all factual claims are backed by web search citations because if I use web tools, citations are necessary. I’ll likely need to search for specific papers and maybe use Python for calculations as I verify the current status of the Meltome Atlas. It’s probably best to verify studies from 2024-2026 and focus on primary sources for technical queries. Also, I want to include structured sections per hypothesis and look into recent literature on thermal proteome research.**Exploring estimation issues**

I need to consider an important issue: the standard error estimate depends on the true ξ and block sizes, which isn't independent and identically distributed. I might simulate or refer to known Fisher information. The standard asymptotic approximation of the variance of maximum likelihood estimation could be around 0.03, but I've realized that for around 300 KEGG pathways per species, it seems unrealistic to reach n=5000-7000 block observations. 

So, I need to clarify how they treat proteins by scrutinizing the details. I'll also calculate the standard error and decide whether to derive it using simulations or numerical methods. Let’s search for key papers on this!**Refining search approach**

I’m realizing that my search results aren’t very helpful, so I need to be more targeted. Maybe searching for official DOI pages isn’t necessary, and I should consider using CrossRef as a source instead. I'll focus specifically on finding updates related to Jarzab and the Meltome Atlas. That should lead me to more relevant information! Let’s dig into this to get better results!**Searching for correlations**

I’m looking through a PubMed abstract that mentions over 350 complexes. I need to find correlations between 0.75 and 0.83, possibly from significant TPCA signatures in the paper or its supplementary materials. It might be tricky to extract correlation stoichiometry from the article. To help, I’ll search within the PDF text and look for the right correlations. Maybe I'll also try searching the web for the phrase “0.75” to gather more insight.**Searching for confirmations**

The search results aren't looking great, so I'm thinking about using the Science PDF directly from a specific issue. I believe we can confirm there are over 350 complexes. However, I'm uncertain about the range of r values between 0.75 and 0.83, and I might need to be more precise. I should also consider looking into the supplementary materials of Tan's work, but those might not be easily accessible. I’ll search NatCommun 2023 for references to Tan’s paper and associated numbers.**Exploring thermophilic archaea research**

I’m considering a range for r, maybe 0.75-0.83, from another paper. I should verify this and possibly mark it as unsupported if I can’t find good backing. I need to dig into recent research about cross-species Tm distribution shapes specifically for thermophilic archaea. It might be important to look at supplementary data or check out the Meltome Atlas for a species list. I wonder if the list includes more than 13 species, as it seems to cover human and mouse cell lines, and my focus may need to shift.**Searching for measurements**

I should consider looking for the measurement window and the unmeasured fraction from the supplement, which might be around 20%, although it seems tricky. It would be a good idea to search within the paper for the term "below 30" to see if there's any relevant information that might help me clarify this. I want to gather accurate data to ensure I’m on the right track!**Searching for Tm distribution literature**

I’m looking for recent literature on Tm distribution shapes. I think a targeted search will be the best approach here. I'll aim to find relevant studies or articles that discuss the shapes of Tm distributions in detail, to gather useful information. There’s likely a lot of recent research out there, so I’m eager to see what I can find! Hopefully, this will lead me to valuable insights.**Searching for studies on psychrophiles**

I’m considering looking for recent research published in 2025 in Nature Communications specifically about psychrophiles. I think it would be helpful to explore cross-species studies related to this topic. I want to ensure I gather comprehensive and relevant information that will provide insights into how these organisms are studied across different species. Let’s see what I can find to enrich my understanding of psychrophiles and their unique characteristics!**Searching for recent studies**

I’m looking for better studies from 2024 to 2026, possibly referencing Keyport et al. So, I think I might need to search on yeast divergence as this could help with H1/H3. I’ll also search for thermal stability evolution during this timeframe. I need to gather recent research to ensure I’m getting the most current information possible, focusing on the relevant areas, and see if there are any useful insights available.**Researching stability and evolutionary rates**

I'm focusing on finding specific papers about stability and evolutionary rates, particularly those from 2024 or 2025. I think utilizing both primary research and reviews could provide a broader perspective. It's essential to gather a good mix of sources, as reviews can highlight key findings that primary studies might delve into more deeply. I'm eager to see what insights I can uncover in this realm!**Searching for stability literature**

I’m looking for literature on the connection between thermal stability and evolutionary rate, not just Tm-dN/dS specifics. I need to explore prior work that blends these concepts, potentially citing theoretical and empirical studies, maybe by Leuenberger, Drummond, or Zeldovich. I should check for recent literature on thermal divergence, possibly using search terms like "protein stability evolutionary constraints across proteome" and "dN/dS." If recent papers aren't available, I might resort to classic studies.**Searching proteomics stats**

I'm planning to look into extreme value statistics in proteomics. This is an interesting topic, and there seems to be a lot of fascinating information available. I'll want to find reliable sources that discuss the applications and implications of these statistics in proteomics. Understanding this can lead to better insights and advancements in the field. Let's see what I can find that highlights key findings or methodologies used!**Searching EVT in omics**

I'm thinking about searching for EVT in the context of omics, especially focusing on the extreme rank sum in peptide identification. It sounds like I might find something specific there but, hmm, I need to check if there's a particular EVT framework applicable to proteomics or metabolomics. I think I should search more targetedly to get the best results for what I'm looking for. Let's refine that search a bit!**Considering EVT in proteomics**

I'm thinking about how EVT could be applied to proteomics, focusing more on peptide identification and statistical calibration instead of thermal biology. It seems like I might also want to explore its relevance in metabolomics. Specifically, I'll look into peptide-spectrum scoring and how it relates to omics biomarker selection. Perhaps I should dive deeper into metabolomics for a more direct understanding. Let’s see what I can find!**Searching temperature impacts**

I’m considering looking into the effects of process failures related to temperature, specifically in terms of human respiration and heat stress. It seems important to measure factors like translation loss and how OCR might decline under those conditions. I’ll need to gather some experimental data to understand this better. This search will help clarify how these elements interact in real-world scenarios.**Searching for thermal analysis**

I need to look for recent complex-level thermal analysis for the years 2024-2026. I want to focus on resources such as MAP-X and TPCA. These might provide valuable data and insights I’m looking for. I’ll need to ensure I’m gathering accurate information from reliable sources. Let’s see what I can find that matches this criteria!**Verifying species list**

I need to search for an official query to the current site’s species list. I already have some information, but I might mention there’s no evidence of any expansion beyond the original 13 cross-species published by Jarzab in 2020. However, I’ve found some related papers from 2025 that aren’t experimental. It seems like I might need to verify the cited papers to confirm this, using both the internet and common knowledge if necessary.**Evaluating information sources**

I'm considering using a screenshot of a figure or accessing relevant lines from a PDF that includes figure descriptions. It seems that a research portal could have an excerpt stating that species OGT is close to the cold side of its distribution, which could be useful. I wonder if I could cite a reputable RG PDF mirror of the paper, but I'm cautious about its reliability. For thermophilic archaea distribution, I might refer to figure snippets, although it’s not ideal. I may need to check other sources for more detailed info.**Searching for specific data**

I’m thinking it's not necessary to dive deeper, as I can state that there's insufficient data on signaling versus metabolic classes from available sources. Leuenberger focused on protein size, expression, and functional subsets rather than a clear dichotomy. However, since the question asks specifically about the thermal stability of signaling proteins versus metabolic enzymes, I may need to access the actual paper. I might try using a search to find “signaling” in a PDF, potentially needing multiple commands for this.**Considering statistical calculations**

I have one call left, but maybe it's not needed since we have enough calculations. I’ll be using Python to compute the GEV shape's standard error through simulation and Fisher information. I also want to assess the regression power, especially for a detectable correlation with n=13 species. We need to explore hypotheses about the ξ correlation with OGT and determine if the regression or t-test is necessary for these calculations. Let's compute everything carefully!**Analyzing lower tail characteristics**

I need to define Y as u-X for X<u, or consider exceedances over a low threshold in a transformed variable. The hypothesis wording seems a bit off, so I’ll calculate the 1% return level with a threshold of u=45°C, noting that 10% of complexes exceeding the threshold might mean they are below 45°C. I want to derive the standard formula and verify SE(ξ) using standard GEV methods while approximating Fisher information for numerical values, possibly needing to use SciPy for simulations.**Addressing arithmetic estimations**

I need to note a possible arithmetic inconsistency. I want to verify what the standard error (SE) would be if n=5000–7000 for independent GEV minima. The estimate of 0.029 corresponds to a constant of 2.05 at n=5000, which is calculated as 0.029 multiplied by the square root of 5000. That resulting value feels quite large, so I need to double-check these calculations to ensure everything aligns correctly!**Calculating variance numerically**

I need to score a numerical value by applying finite difference on the log probability density function with respect to parameters like [mu, log_sigma, xi]. I could compute this for many samples to find a solid answer. Afterward, I would invert the Fisher information divided by n to get the variance. For the parameter xi, I plan to look around values -0.2, 0, and 0.2 to analyze the effects.**Verifying numerical estimates**

I’m calculating the standard error for observations with values around 0.6 to 0.8. At n=5000, I see values between 0.0084 and 0.011, and at n=7000, it comes out to 0.007. It seems like 0.029 is an overestimate by about three times. I might want to verify this through simulations of MLE fits. Let's consider a quicker simulation approach, possibly running around 200 repetitions for different n values.**Inspecting fitting issues**

I think I've hit a snag with the fitting process, possibly related to bounds or maybe an issue with the custom optimizer I'm using. This could be tied to the gradient calculations I'm working with. I really need to take a closer look at the fitting procedure to see what's happening. Let’s inspect the fit closely to figure out what's going wrong, and then I can determine the best steps to address it!**Evaluating simulation approach**

I think I made a mistake with my parameters, specifically using xi=-0.2 and generating c=0.2, which isn't working out well. The fit to the xi parameter returns zero because the initial value is close to zero. Hmm, that suggests this simulation might not be functioning as expected. I might need to consider using the scipy fit instead to get a better result. Let's see if that can help!**Planning a simulation**

I’m considering using the SciPy library for fit simulation. The choice seems logical since SciPy has good tools for fitting data and performing scientific computing. It looks like a straightforward option, but I need to make sure I understand how to implement the fitting process properly. I'll take a moment to explore the details and see which fitting functions will work best. It's all about getting the right parameters, right? Let’s get to it!**Evaluating statistical measures**

Okay, so I've found that the standard error (SE) of 0.029 seems too high for a sample size of 5,000-7,000 but is closer to 0.034-0.041 when n=300. That's intriguing! It makes sense since the actual number of pathway blocks is around 300 per species, so the SE of 0.029 aligns better with n≈400. I should emphasize this point and consider computing the block minima across approximately 300 pathways to see if it holds up.**Determining rho for power thresholds**

I need to find the value of rho to analyze the power thresholds effectively. It's essential to have that information to ensure accurate calculations. I'm thinking through how different contexts might influence rho, like the specific application or field I'm working with. I want to make sure I'm considering everything related to this concept. Let's take a closer look at the factors that could affect rho and how best to approach this.**Evaluating statistical power**

I'm considering the power needed for a linear regression slope with 13 species and an expected ξ difference ranging from 0.3 to 0.5 between thermal and psychological data, depending on OGT range. I think I can approximate that if OGT spans 70°C and look at the residual standard error across species. To achieve statistical significance with 13 species, I need an r value of at least 0.55 for a nominal p-value less than 0.05.**Considering lower tail adaptation**

I need to focus on the lower tail adaptation, specifically with a threshold of u = 45°C. Since about 10% of the complexes might exceed this threshold, I assume that 10% are below it as well. I want to determine the 1% return level temperature, which is the temperature only 1% of complexes fall below. I'll define Y as u - X for values below the threshold and fit a generalized Pareto distribution to Y to derive the needed quantile.**Calculating correlation and sample size**

I'm considering whether I need specific sample sizes. It seems like I'm discussing the number of complexes and repeated measurements, especially with n=13. I computed r thresholds, and now I'm thinking about using multiple covariates. If I explore partial correlation with three covariates, the degrees of freedom drop to 8, which gives a critical r value of around 0.632. I should calculate the minimum partial R² and consider the critical t value of 2.306 too. I’m on it!**Considering temperature effects on cells**

I can mention that global translation decreases at 42°C in neurons and HEK293 cells, while human mitochondria can still respire near normally at 46°C. However, I haven't found high-quality papers detailing specific temperature failures for human cells on a small scale of 1–2°C. It's worth noting the data is insufficient. I should also be cautious about the reliability of the puromycin assay under stress from external sources, which could serve as a counter-evidence or experimental caveat.**Analyzing Meltome Atlas**

I’m checking the current state of the Meltome Atlas, which still has its original 13 species along with around 48,000 cross-species atlases plus human cell-line data. It seems there’s no clear peer-reviewed expansion of the atlas. 

For the next question about the most detectable signal, it looks like H2 is likely. Data availability is decent, with human complexes being abundant, but mapping return levels can be challenging, especially since H1 and H3 are limited by the same 13 species.**Considering species analysis**

I think it’s better to avoid making correlations at the species level. Instead, focusing on class-level or ortholog groups could be more effective. I’m considering modeling the melting temperature per protein against evolutionary constraint. However, I feel like I need to include more species in my analysis. Maybe I could use larger sequence-based datasets for melting temperature predictions, like DeepSTABp? But I'm wondering if the Meltome 13 species dataset is really enough for my hypothesis.**Evaluating correlation estimates**

I'm predicting temperature from DeepSTABp and ortholog data to assess correlation among 13 species in relation to OGT. I wonder about translating differences into correlation, where species are divided into three groups based on thermal preferences. Although I might mention a minimum detectable correlation, strong linear trends are the focus here. Since there's limited diversity among the species, any estimated slope might be unstable. I should check citations for established sources in EVT but might not need too many details.**Examining citations and correlations**

I could cite multiple sources from the web, but since we have no more web calls, it's fine. I need to cite them in my answer, particularly noting Mateus 2020, which is from Mol Syst Biol 16:e9232, not from Science. Also, Tan's abstract mentions over 350 human complexes with statistically observable signatures, though the correlation of r 0.75-0.83 isn't verified. I might clarify this from the accessible abstract. Regarding the "1% return level" mechanism, it may be weak since translation involves more than just the lowest-Tm bottleneck.**Reviewing translation impacts**

I’m looking into search results regarding heat-shocked neurons and HEK293 cells, which indicate that translation decreases at 42°C. However, this decline may not be solely due to ribosome denaturation. I should snag a citation from the relevant website to support this information. It's good to note these findings, as they could provide useful insights into the cellular response to heat shock and its effects on translation mechanisms.**Clarifying confidence levels**

I'm contemplating how to express "Original confidence." Should I say "not stated" or clarify that it's "not stated in the prompt"? That seems safer. If they want a specific number, I'm not sure if that’s necessary since they asked based on what's in the hypothesis. I think it might be good to mention that it wasn't explicitly stated. I want to ensure I get this right!**Preparing cross-cutting findings**

Since the user has posed general cross-cutting questions, I’ll label the section "Cross-cutting findings." Citations are necessary for every paragraph, ensuring all factual claims are supported. I’ll note that calculations performed in Python don’t need web citations, just labeled as "Python calculation." I’m considering including tables for clarity, as well as bullet lists to check citations. I’ll also compute H1 standard error and H3 power with a minimal sample size, starting with n=13 and r threshold, and k=4 covariates.**Calculating correlations**

I'm considering how to compute minimal detectable partial correlation and full simple correlation. It sounds like an interesting task! I need to think through the methods and formulas to use for each calculation. I'll check the necessary assumptions and data requirements for these correlation analyses to ensure I get accurate results. Let's see how this goes!**Calculating sample size**

I’m thinking about whether I need to compute confidence intervals, but it might not be necessary. I’m considering if the H1 standard error estimate of 0.029 corresponds to a sample size of around 400. So, let’s calculate that using the asymptotic constant around 0.6966. It seems to suggest a sample size of about 577. I’m also thinking about how a simulation might involve a constant closer to 0.665. Currently, with n=300, I see a standard error of 0.0384.**Analyzing observations for pathways**

I’m looking at 526 observations. It seems like 0.029 is more aligned with a few hundred observations than with 5,000 to 7,000. I need to check if having n=300 for pathway blocks might keep the standard error around 0.03-0.04. My hypothesis suggests blocking minima for 300 KEGG pathway blocks across 13 species. I should also consider return level formula details for the lower tail around the 10% threshold, possibly providing some simple arithmetic. I'm also thinking about the sample size related to complexes, focusing on pathway-specific ones.**Evaluating pathway distributions**

I’m realizing that applying a single pathway distribution for complex minima might be underpowered. That's crucial! Major pathways like translation might have just a few distinct complexes, which means there probably isn't enough data for reliable peaks over thresholds in a pathway-specific distribution. While using all 5,000 human CORUM complexes could offer sufficient data, specific distributions might only have tens, not thousands, of complexes. It could be wise to mention that “CORUM provides many annotated human complexes” without focusing on the exact number, unless necessary, as I haven't independently verified that count.**Checking citations and evidence**

I’m realizing the citation check might indicate that the current count hasn’t been independently verified, but that could be okay. I could label the H1 novelty verdict as "PARTIALLY EXPLORED." I need to verify supporting citations as Jarzab, Fisher/Tippett, Gnedenko, and Coles seem accurate with no discrepancies. For plausibility, I should mention there’s only one archaeal species in the original atlas, which means that claims about thermophilic archaea’s tail shapes can't be tested within that original dataset, and I might need a citation for that.**Analyzing stability and mutation**

I'm considering how stability might affect sequence constraints. It seems plausible, but the sigma of the lower tail acts as a species-level mixture parameter rather than simply indicating mutational tolerance. Then there's the dN/dS ratio, which appears to be influenced mainly by factors like expression levels, protein abundance, and the degree of interactions. In fact, both Drummond and Leuenberger link expression and stability in their work. There's a lot to unpack here!**Planning experimental structure**

I'm thinking about the experimental feasibility of each hypothesis. It seems like H1 could be at a medium level, H2 might be medium to high, and H3 would fall into the low category. Since the user wants each hypothesis sectioned in order, I should think about structuring it with bullet subsections and concise paragraphs for clarity. Also, I definitely need to ensure I include proper citations in the final answer's paragraphs.**Analyzing research on adaptation**

I’m looking at the 2025 psychrophile study, which shows that PA distribution peaks at around 315.6K and has a long tail reaching 351K. This contradicts the idea that "cold adaptation equals a left shift with a similar tail shape." Then there's the 2025 yeast divergence paper suggesting that selection influences the entire distribution, not just truncating the tail. I'm pondering how these findings challenge existing assumptions about cold adaptation.**Examining evolutionary factors**

I want to explore the counter-evidence surrounding evolutionary rates. It seems that expression is a major determinant, while size and disorder significantly affect stability. Also, I’m considering how within-species characteristics, especially vulnerable tail identities, might change over time. I’m curious about how these elements interact and contribute to evolutionary dynamics. There’s a lot to unpack here, and I want to ensure I’m considering all aspects thoroughly.**Considering detectable signals**

I'm thinking the most likely detectable signal is H2 since it can interact with many complexes within one species and assist in direct functional assays. H1 and H3 face challenges from having n=13 species, which complicates the phylogenetic and orthology aspects. I need to remember to include citations from the websites along with any calculations we’ve made. It’s important to clarify this part in my analysis for accuracy!**Considering citation strategies**

I’m pondering the best way to use authoritative sources like Cambridge for my citations. I could look at specific searches related to various references. But I’m wondering if using less authoritative sources will be a potential issue. It seems like I need more than half of my citations from recognized outlets like Nature, PubMed, PNAS, Oxford, and Science. I’m also contemplating whether I actually need citations for summary statements since they’re based on previous information. But, maybe including them after each paragraph would be awkward.**Evaluating citation placement**

I’m considering whether the block needs citations. It seems like I could leave it uncited since it's mostly my assessments and calculations. However, if I'm referencing something like "pathway failure may be regulatory," maybe that’s okay to summarize without citations. Still, it might be safer to include citations after the key counter-evidence line. I wonder if I need to avoid code blocks since they can't include citations and might not render properly. Instead, I could use a plain text list following user-requested labels, but they did specify a code block.**Drafting a summary approach**

I’m thinking about how to present information without needing citations, possibly by using indented text or bullet lists. I want to be cautious and avoid code fences to stay within guidelines. Maybe I should mention the calculation methodology, especially regarding the H1 SE and repeated SciPy GEV fits. I could say it’s a “Python simulation of standard 3-parameter GEV MLE.” There might also be some confusion about "block observations" that I need to clarify.

---

Below is an independent stress-test of the three hypotheses, using recent literature searches plus Python calculations.

## HYPOTHESIS 1 — GEV Shape Parameter as a Cross-Species Signature of Thermal Adaptation

### 1. Novelty Verdict — **PARTIALLY EXPLORED**

I did **not** find a paper that fits **GEV/GPD shape parameters** to proteome melting-temperature distributions and interprets the fitted **shape parameter ξ** as a cross-species thermal-adaptation signature. What **does** exist is a literature showing that proteome-wide Tm distributions differ across species and track thermal ecology, starting with the Meltome Atlas itself, plus newer work arguing that selection shapes proteome-wide thermostability distributions across species. In 2025, a yeast study explicitly described selection acting on the **distribution** of protein melting temperatures across species, and a 2025 psychrophile paper compared whole-proteome Tm distributions between a cold-adapted bacterium and *E. coli*. That means the **biological question** is already in play, but the specific **EVT parameterization by ξ** still appears novel. ([nature.com](https://www.nature.com/articles/s41592-020-0801-4))

My searches for EVT in proteomics turned up **other** uses of extreme-value ideas—especially peptide-spectrum match score calibration and null-distribution fitting in biomarker studies—but not EVT applied to **proteome thermal-stability tails**. So the math-to-biology bridge is novel, but EVT is not foreign to proteomics as a whole. ([noble.gs.washington.edu](https://noble.gs.washington.edu/papers/klammer2009statistical.pdf))

### 2. Citation Check

- **Jarzab et al. 2020, Nature Methods 17:495–503** — **Verified.** The paper exists, reports ~48,000 proteins across 13 species, a 30–90 °C measurement range, and states the data are in PRIDE **PXD011929**. ([nature.com](https://www.nature.com/articles/s41592-020-0801-4))  
- **Fisher & Tippett 1928** — **Verified as a real classic EVT reference** on limiting forms for sample extremes. ([ndltd.ncl.edu.tw](https://ndltd.ncl.edu.tw/handle/15224402977733726138?utm_source=openai))  
- **Gnedenko 1943, Annals of Mathematics 44:423–453** — **Verified** as the classic completion of the Fisher-Tippett theorem. ([cambridge.org](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/1A78F46EC1BC6F1D27B68AC6F8A68546/9781108473682ref_410-414.pdf/references.pdf?utm_source=openai))  
- **Coles 2001, Springer** — **Verified.** Standard EVT text exists as cited. ([link.springer.com](https://link.springer.com/book/10.1007/978-1-4471-3675-0?utm_source=openai))

Two practical discrepancies matter:
1. The original Meltome Atlas cross-species resource has **13 species total**, including **only one archaeon** in the published atlas, not multiple thermophilic archaea. That weakens any claim about “thermophilic archaea” as a class inside the original dataset. ([research-portal.uu.nl](https://research-portal.uu.nl/ws/portalfiles/portal/234736812/s41592-020-0801-4.pdf?utm_source=openai))  
2. The hypothesis text says “~300 KEGG pathway blocks per species” but then quotes an SE for **n = 5,000–7,000 block observations**. Those sample-size statements are not internally consistent.

### 3. Mechanism Plausibility

The biological intuition is plausible at a high level: thermophiles can adapt by eliminating especially labile proteins, whereas cold-adapted organisms may favor greater flexibility and lower average stability. The Meltome Atlas already showed that Tm distributions differ systematically across species, and the 2025 yeast paper argued that selection shapes these distributions across lineages. ([nature.com](https://www.nature.com/articles/s41592-020-0801-4))

But the jump from “distribution differs” to “**GEV shape ξ of pathway minima** is a species signature” is much shakier. A fitted ξ from block minima assumes something close to repeated draws from a common tail process. Pathway minima are not i.i.d.; they are driven by pathway composition, complex stoichiometry, membrane-protein burden, disorder content, organellar composition, and lysate-versus-cell context. Jarzab explicitly emphasized sequence, composition, size, disorder, and complex conservation as determinants of stability, which means ξ could easily become a proxy for proteome composition rather than temperature adaptation per se. ([nature.com](https://www.nature.com/articles/s41592-020-0801-4))

There is also a measurement issue: the atlas covers **30–90 °C**, so both tails are censored by assay design. Estimating a tail-shape parameter from minima is hardest exactly when the lower tail is truncated by the instrument window. That is especially problematic if the scientific claim is about the **hardness of the lower cutoff**. ([nature.com](https://www.nature.com/articles/s41592-020-0801-4))

### 4. Counter-Evidence

A strong challenge comes from the 2025 psychrophile study. Its predicted proteome Tm distribution for the psychrophile (*Pseudoalteromonas arctica*) had a maximum around **315.6 K** and a **long tail extending to 351 K**, whereas *E. coli* looked **more symmetric** with a maximum around **322.3 K**. That is not the simple “cold-adapted = left-shift with similar tail shape” story; the tail itself may change in complicated ways. ([nature.com](https://www.nature.com/articles/s41467-025-65270-5))

Another challenge is that recent comparative work has emphasized **proteome-wide shifts** rather than selective lower-tail truncation. In the 2025 yeast study, ~85% of proteins in *S. cerevisiae* were more stable than their *S. uvarum* orthologs, consistent with a broad shift in thermostability rather than an EVT-tail-only mechanism. ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC12227239/))

Finally, the published atlas is just a **13-species** panel with only **one archaeon** and limited thermal extremes. Even if ξ truly tracked OGT, the available design is heavily exposed to phylogeny and lineage composition. ([research-portal.uu.nl](https://research-portal.uu.nl/ws/portalfiles/portal/234736812/s41592-020-0801-4.pdf?utm_source=openai))

### 5. Experimental Design Review

The proposed SE claim does **not** survive arithmetic if the effective per-species sample size is really ~300 pathway blocks. I checked this in Python by simulating standard 3-parameter GEV MLE fits. For true ξ in the range −0.2 to +0.2, the empirical SE of \(\hat{\xi}\) is about **0.034–0.044 at n = 300**, but only about **0.007–0.010 at n = 5,000–7,000**. So the stated **SE ≈ 0.029** is far too large for 5,000–7,000 independent blocks and is much more consistent with **a few hundred** effective observations.

The regression is also underpowered at the species level. With **n = 13 species**, a two-sided Pearson correlation needs about **|r| = 0.553** just to clear **p < 0.05**, and about **|r| ≈ 0.68** for ~80% power. So only a **very strong** ξ–OGT trend is detectable. Once you account for phylogeny, the required effect is effectively larger.

Missing controls:
- phylogenetic GLS or mixed models rather than plain regression  
- sensitivity to block definition (KEGG, CORUM, GO, random blocks)  
- explicit handling of bimodality/multimodality  
- censoring-aware methods for proteins near assay limits  
- robustness checks against membrane/disordered/complex-rich proteome fractions

### 6. Final Assessment

Original confidence: not stated in prompt  
Updated confidence: **4/10**  
Change reason: biologically plausible, and ξ-as-summary-statistic is novel, but the available atlas is too small and too phylogenetically uneven; the SE claim is numerically inconsistent with the stated n, and recent data suggest tail behavior may not map cleanly onto “shift vs truncation.”  
Novelty status: **PARTIALLY EXPLORED**  
Key counter-evidence: psychrophile proteome distributions can have altered tail asymmetry/long tails, not just left-shifted versions of mesophile distributions.  
Experimental feasibility: **MEDIUM**  
Recommended next step: fit **censoring-aware** whole-distribution and lower-quantile models on the actual Meltome data first, then compare whether ξ adds predictive value over simpler summaries such as lower 5th percentile, skewness, or mixture-model parameters.

---

## HYPOTHESIS 2 — Return Levels of Complex-Minimum Melting Temperature Predict Pathway-Specific Thermal Failure

### 1. Novelty Verdict — **PARTIALLY EXPLORED**

This is **not** a blank-slate idea. Complex-level thermal behavior is already a real subfield: **TPCA** from Tan et al. 2018 showed coordinated complex melting across >350 human complexes, Sun et al. 2023 improved TPCA at scale, and recent 2025 papers extended complex-level thermal analysis, including MAP-X for complex dynamics and an integrated TPP+TPCA drug-target paper. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/29439025/))

What I did **not** find is the specific EVT move: fitting a **GPD to lower-tail complex bottlenecks** and using **return levels** to forecast a pathway’s functional failure temperature. So the “complex bottleneck” part is partly anticipated; the “hydrology-style return-level prediction of pathway failure” still looks novel. ([nature.com](https://www.nature.com/articles/s41467-023-43526-2))

### 2. Citation Check

- **Tan et al. 2018, Science 359:1170–1177, DOI 10.1126/science.aan0346** — **Verified.** PubMed confirms the paper and says TPCA signatures were “statistically observable in **more than 350 annotated human protein complexes**.” ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/29439025/))  
- **Correction of the wrong citation** — **Verified.** The hypothesis is right that “Mateus et al. 2020, Science 367:eaaz5268” is wrong for TPCA. The relevant Mateus 2020 paper is in **Molecular Systems Biology 16:e9232**, not Science. ([link.springer.com](https://link.springer.com/article/10.15252/msb.20199232?utm_source=openai))  
- **r = 0.75–0.83 intra-complex Tm correlation** — **Unverified from the accessible primary-source abstract.** Tan’s abstract supports coordinated complex behavior and >350 complexes, but I could not independently confirm that exact numeric range from the accessible abstract alone. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/29439025/))  
- **“Lim et al. 2023, Nature Communications”** — **Discrepancy.** The 2023 Nature Communications TPCA-improvement paper exists, but the first author is **Sun**, not Lim. Yan Ting Lim is a coauthor. ([nature.com](https://www.nature.com/articles/s41467-023-43526-2))  
- **Jarzab 2020** and **Coles 2001** — **Verified.** ([nature.com](https://www.nature.com/articles/s41592-020-0801-4))

### 3. Mechanism Plausibility

The minimum-Tm-subunit bottleneck idea is plausible for some complexes, especially if subunits coaggregate and if the lowest-stability subunit is essential for assembly or catalysis. Tan et al. support coordinated thermal behavior within complexes, which makes “complex-level thermal units” a reasonable starting point. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/29439025/))

But the proposed mechanism is too strong as written. Process failure in cells often happens **before** wholesale complex denaturation because of stress signaling, translational shutdown, ATP depletion, chaperone buffering, or failure of a small number of upstream regulators. In heat-shocked neuronal/HEK293 systems, global translation drops at **42 °C**; in isolated human mitochondria, the elongation factor **Tufm** becomes highly aggregation-prone under mild heat stress and mitochondrial translation/import become defective; yet Jarzab reported that human mitochondria maintained near-normal respiration at **46 °C**. That pattern argues against a universal one-step mapping from “lowest-Tm subunit” to “pathway failure temperature.” ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC12285177/?utm_source=openai))

A second problem is granularity. EVT needs enough tail observations. “All human complexes” may be large enough, but **pathway-specific** sets like translation or respiration may contain too few distinct complexes for stable POT fitting once you subset to one pathway and then further subset to the lower tail.

### 4. Counter-Evidence

The biggest biological counterpoint is that heat-induced process failure is often **regulatory** rather than purely **structural**. Translation suppression during heat shock is a classic stress response and can be observed around 42 °C, so a “ribosome bottleneck temperature” may not be the dominant driver of loss of protein synthesis in intact cells. ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC12285177/?utm_source=openai))

For mitochondria, the JBC 2018 study showed that a **specific translation factor** (Tufm) is exceptionally heat-sensitive and that mitochondrial translation/import fail under mild heat stress, even though the overall mitochondrial proteome remains largely soluble. That is exactly the kind of pathway failure by **special vulnerable regulator** that breaks the “minimum subunit of each annotated complex predicts pathway collapse” model. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/29895621/))

Methodologically, the proposed validation assay also has issues: puromycin-based readouts can be unreliable under energetic stress conditions, which matters if the experiment links heat, translation, and metabolism. ([nature.com](https://www.nature.com/articles/s41419-017-0056-x?utm_source=openai))

### 5. Experimental Design Review

The lower-tail EVT arithmetic is feasible, but the orientation must be handled correctly. For a **lower tail**, you should transform to exceedances \(Y=u-X\) for \(X<u\), not reuse the upper-tail formula naively.

Using the stated numbers:
- threshold \(u = 45^\circ\)C  
- exceedance fraction below threshold \(q = 0.10\)  
- GPD scale \(\sigma = 3^\circ\)C  
- shape \(\xi = -0.2\)  
- target lower-tail probability \(p = 0.01\)

the 1% lower-tail return level is:

\[
x_p = u - \frac{\sigma}{\xi}\left[\left(\frac{p}{q}\right)^{-\xi}-1\right]
\]

Python calculation gives **\(x_{0.01} \approx 39.46^\circ\)C**.

That arithmetic is fine. The biology is the hard part.

I did **not** find a literature basis for the claimed **±2 °C** agreement with experimentally measured pathway failure temperatures in human cells. What I found were coarser anchors: translation decreases around **42 °C** in heat-shocked cell systems, and human mitochondrial respiration can remain close to normal at **46 °C**. That is not enough to justify a ±2 °C forecast claim. ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC12285177/?utm_source=openai))

A better design would include:
- intact-cell TPP/TPCA in the same cell type used for functional assays  
- “essential subunit” definitions based on perturbation/fitness data, not just CORUM membership  
- threshold-diagnostic plots for POT choice  
- chaperone-modulation controls  
- at least **3–4 biological replicates** per temperature and **6–8 temperatures** spanning the expected failure zone  
- validation across **multiple pathways**, not just one cherry-picked success

### 6. Final Assessment

Original confidence: not stated in prompt  
Updated confidence: **5/10**  
Change reason: complex-level thermal coupling is real and the hypothesis is experimentally tractable, but the jump from complex bottleneck statistics to precise pathway failure temperatures is much less secure than the hypothesis assumes.  
Novelty status: **PARTIALLY EXPLORED**  
Key counter-evidence: pathway failure can be driven by stress signaling or a few hypersensitive regulators rather than by the minimum-Tm subunit of annotated complexes.  
Experimental feasibility: **MEDIUM**  
Recommended next step: test the idea first on one pathway with strong orthogonal functional readouts and enough complex members, and compare EVT return levels against simpler predictors such as the lowest essential-subunit Tm, median complex-minimum Tm, and robust lower quantiles.

---

## HYPOTHESIS 3 — GPD Scale Parameter Predicts Evolutionary Rate of Thermally Vulnerable Proteins

### 1. Novelty Verdict — **PARTIALLY EXPLORED**

The specific proposal—using the **GPD scale parameter σ of the low-Tm tail** as a predictor of evolutionary constraint—is, as far as I could find, **novel**. But the broader link between **protein stability** and **evolutionary constraint** is already well explored. Drummond et al. 2005 made expression a central predictor of slow evolution, and Leuenberger et al. 2017 explicitly tied higher thermostability to high expression and tolerance to translational errors. Reviews on protein evolutionary-rate determinants also already list **protein stability** among known contributors. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/16176987/?utm_source=openai))

So this is not a new biology claim; it is a new **summary statistic** for an old, partly contested biology problem. ([academic.oup.com](https://academic.oup.com/mbe/article/30/7/1500/972515?utm_source=openai))

### 2. Citation Check

- **Drummond et al. 2005** — **Verified correction.** The paper is **PNAS**, not Cell: *Proc Natl Acad Sci U S A.* 2005;102(40):14338–14343. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/16176987/?utm_source=openai))  
- **Yang 2007, PAML 4** — **Verified.** The paper exists in *Molecular Biology and Evolution* 24:1586–1591. ([ebi.ac.uk](https://www.ebi.ac.uk/research/goldman/software/SLR/?utm_source=openai))  
- **Leuenberger et al. 2017, Science 355:eaai7825** — **Verified.** PubMed confirms the paper and its thermostability conclusions. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/28232526/?utm_source=openai))  
- **Jarzab et al. 2020** — **Verified.** ([nature.com](https://www.nature.com/articles/s41592-020-0801-4))

One conceptual discrepancy: the hypothesis treats **dN/dS as an “evolutionary rate.”** That is not strictly correct. A 2021 review cautions that **dN/dS is a ratio of nonsynonymous to synonymous substitution rates and should not itself be interpreted as a raw rate of evolution**. It is usable as a constraint/selection metric, but the wording in the hypothesis is sloppy. ([academic.oup.com](https://academic.oup.com/bib/article/doi/10.1093/bib/bbaa431/6105943?utm_source=openai))

### 3. Mechanism Plausibility

There is a plausible core idea here: if proteins sit close to a functional stability threshold, destabilizing mutations should be less tolerated, increasing purifying selection. That logic is consistent with older stability-centered views of protein evolution and with Leuenberger’s finding that highly expressed proteins are especially thermostable. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/28232526/?utm_source=openai))

But the proposed **species-level σ** is a very indirect proxy for that mechanism. σ of the low-Tm tail is a **mixture property** of a species’ vulnerable proteins. It can widen or narrow because of changes in protein classes, subcellular composition, disorder, size, expression, or assay censoring—not necessarily because mutational tolerance changed. Leuenberger explicitly links expression and stability, which means σ could just be a disguised expression-composition variable. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/28232526/?utm_source=openai))

A second problem is identity mismatch. The “thermally vulnerable subproteome” in one species will not necessarily be the same ortholog set in another. If the tail is not made of the same genes, correlating one species-level σ with another species-level mean dN/dS over “tail orthologs” becomes conceptually unstable.

For the question about **signaling proteins vs metabolic enzymes in Leuenberger et al. 2017**: **INSUFFICIENT DATA.** In the primary-source abstract and accessible excerpts I verified, the paper emphasizes size, disorder, expression, key functional proteins, and conservation of domains, but I could not independently confirm a specific signaling-vs-metabolic-enzyme claim from the source text I accessed. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/28232526/?utm_source=openai))

### 4. Counter-Evidence

The strongest counter-evidence is that expression and abundance already explain a large share of evolutionary-rate variation. Drummond’s PNAS paper makes expression level the major determinant, and later summaries/reviews continue to place expression and abundance at the center. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/16176987/?utm_source=openai))

Leuenberger adds another confounder: highly expressed proteins are also more thermostable. So any σ–dN/dS correlation could simply reflect variation in expression structure across species rather than a new tail-width mechanism. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/28232526/?utm_source=openai))

Recent comparative work also suggests that thermostability divergence is shaped by both **structural changes and cellular environment**. That makes a single one-number tail parameter even less likely to isolate evolutionary constraint cleanly. ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC12227239/))

### 5. Experimental Design Review

This design is badly underpowered at **n = 13 species**.

Python calculations:
- For a simple Pearson correlation with **n = 13**, you need about **|r| = 0.553** just for **p < 0.05**, and about **|r| ≈ 0.68** for ~80% power.
- If you include **four predictors/covariates** (e.g., σ, expression, size, disorder), the required **partial correlation** rises to about **|r| = 0.632** for **p < 0.05** and **|r| ≈ 0.75** for ~80% power.

That is a huge effect-size requirement for a noisy comparative genomics question.

Other missing controls:
- phylogenetic non-independence  
- gene set stability across species (same tail genes or not?)  
- dN/dS estimation uncertainty for distant orthologs  
- assay censoring at the low-Tm end  
- threshold sensitivity of the GPD fit

A stronger redesign would move from **13 species** to **hundreds of genomes**, using predicted Tm values or homolog-pair resources as screening data and reserving measured meltomes for calibration.

### 6. Final Assessment

Original confidence: not stated in prompt  
Updated confidence: **2/10**  
Change reason: the stability–constraint link is real, but the proposed σ statistic is too indirect, the response variable is partly mischaracterized, and the n=13 comparative design is underpowered once major confounders are included.  
Novelty status: **PARTIALLY EXPLORED**  
Key counter-evidence: expression level and abundance already dominate much of the evolutionary-constraint signal and also correlate with stability.  
Experimental feasibility: **LOW**  
Recommended next step: abandon the 13-species species-level correlation and reframe this as a larger ortholog-group or within-species mixed-model analysis, using measured or predicted Tm at much larger scale.

---

# Cross-cutting findings

## 1. Has anyone applied EVT to proteomics or metabolomics at all?

**Yes, but not in the same way.** I found EVT/EVD use in proteomics for **mass-spectrometry score calibration**—for example, modeling the distribution of top peptide-spectrum match scores as an extreme-value distribution—and in a proteomic biomarker paper that fit a **GEV** to a bootstrap null distribution of multivariate AUC. I did **not** find a clear example of GEV/GPD/return-level modeling applied to **proteome thermal-stability distributions**. ([noble.gs.washington.edu](https://noble.gs.washington.edu/papers/klammer2009statistical.pdf))

## 2. 2024–2026 “dark meltome” papers?

**INSUFFICIENT DATA:** I searched for “dark meltome” and for 2024–2026 work on proteins outside the 30–90 °C TPP window, but I did not find a clear paper/preprint establishing that term or framework.

## 3. Current state of the Meltome Atlas

As of the currently accessible official site, the Meltome Atlas still presents itself as the interactive front end for the dataset **published by Jarzab et al. 2020**, with tabs for **cross-species** and **human cell line/cell type** exploration. The Nature Methods paper still describes the core cross-species atlas as **13 species / ~48,000 proteins**, plus a human chapter with additional cell-line/tissue/body-fluid data. I did **not** find a peer-reviewed broad cross-species expansion beyond that original published atlas. ([meltomeatlas.proteomics.wzw.tum.de](https://meltomeatlas.proteomics.wzw.tum.de/master_meltomeatlasapp/?utm_source=openai))

## 4. Which hypothesis is most likely to yield a detectable signal?

**Hypothesis 2** is the best bet. Complex-level thermal coupling is already measurable, and the needed data structure exists within a **single species**, avoiding the n=13 cross-species bottleneck that hurts Hypotheses 1 and 3. Its exact EVT framing may or may not be the right one, but it has the clearest path to an empirical win. Hypotheses 1 and 3 both run into severe comparative-power and confounding problems with the current Meltome Atlas scale. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/29439025/))

If you want, I can turn this into a **ranked decision memo** with:
1. best hypothesis to pursue now,  
2. minimum viable experiment, and  
3. kill criteria for each hypothesis.

---

## Citations

- [Meltome atlas—thermal proteome stability across the tree of life | Nature Methods](https://www.nature.com/articles/s41592-020-0801-4)
- [Source](https://noble.gs.washington.edu/papers/klammer2009statistical.pdf)
- [Meltome atlas—thermal proteome stability across the tree of life | Nature Methods](https://www.nature.com/articles/s41592-020-0801-4)
- [極值理論應用於風險值估計之研究__臺灣博碩士論文知識加值系統](https://ndltd.ncl.edu.tw/handle/15224402977733726138?utm_source=openai)
- [References - Probability](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/1A78F46EC1BC6F1D27B68AC6F8A68546/9781108473682ref_410-414.pdf/references.pdf?utm_source=openai)
- [An Introduction to Statistical Modeling of Extreme Values | Springer Nature Link](https://link.springer.com/book/10.1007/978-1-4471-3675-0?utm_source=openai)
- [Resource
https://doi.org/10.1038/s41592-020-0801-4](https://research-portal.uu.nl/ws/portalfiles/portal/234736812/s41592-020-0801-4.pdf?utm_source=openai)
- [Meltome atlas—thermal proteome stability across the tree of life | Nature Methods](https://www.nature.com/articles/s41592-020-0801-4)
- [Meltome atlas—thermal proteome stability across the tree of life | Nature Methods](https://www.nature.com/articles/s41592-020-0801-4)
- [Meltome atlas—thermal proteome stability across the tree of life | Nature Methods](https://www.nature.com/articles/s41592-020-0801-4)
- [Cytoplasmic fluidity and the cold life: proteome stability is decoupled from viability in psychrophiles | Nature Communications](https://www.nature.com/articles/s41467-025-65270-5)
- [
            Pervasive Divergence in Protein Thermostability is Mediated by Both Structural Changes and Cellular Environments - PMC
        ](https://pmc.ncbi.nlm.nih.gov/articles/PMC12227239/)
- [Resource
https://doi.org/10.1038/s41592-020-0801-4](https://research-portal.uu.nl/ws/portalfiles/portal/234736812/s41592-020-0801-4.pdf?utm_source=openai)
- [Thermal proximity coaggregation for system-wide profiling of protein complex dynamics in cells - PubMed](https://pubmed.ncbi.nlm.nih.gov/29439025/)
- [Improved in situ characterization of protein complex dynamics at scale with thermal proximity co-aggregation | Nature Communications](https://www.nature.com/articles/s41467-023-43526-2)
- [Thermal proximity coaggregation for system-wide profiling of protein complex dynamics in cells - PubMed](https://pubmed.ncbi.nlm.nih.gov/29439025/)
- [Thermal proteome profiling for interrogating protein interactions | Molecular Systems Biology | Springer Nature Link](https://link.springer.com/article/10.15252/msb.20199232?utm_source=openai)
- [Thermal proximity coaggregation for system-wide profiling of protein complex dynamics in cells - PubMed](https://pubmed.ncbi.nlm.nih.gov/29439025/)
- [Improved in situ characterization of protein complex dynamics at scale with thermal proximity co-aggregation | Nature Communications](https://www.nature.com/articles/s41467-023-43526-2)
- [Meltome atlas—thermal proteome stability across the tree of life | Nature Methods](https://www.nature.com/articles/s41592-020-0801-4)
- [Thermal proximity coaggregation for system-wide profiling of protein complex dynamics in cells - PubMed](https://pubmed.ncbi.nlm.nih.gov/29439025/)
- [Regulation of translation elongation and integrated stress response in heat-shocked neurons - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12285177/?utm_source=openai)
- [Regulation of translation elongation and integrated stress response in heat-shocked neurons - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12285177/?utm_source=openai)
- [Analysis of heat-induced protein aggregation in human mitochondria - PubMed](https://pubmed.ncbi.nlm.nih.gov/29895621/)
- [Puromycin labeling does not allow protein synthesis to be measured in energy-starved cells | Cell Death & Disease](https://www.nature.com/articles/s41419-017-0056-x?utm_source=openai)
- [Regulation of translation elongation and integrated stress response in heat-shocked neurons - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12285177/?utm_source=openai)
- [Why highly expressed proteins evolve slowly - PubMed](https://pubmed.ncbi.nlm.nih.gov/16176987/?utm_source=openai)
- [Protein Conformational Diversity Correlates with Evolutionary Rate | Molecular Biology and Evolution | Oxford Academic](https://academic.oup.com/mbe/article/30/7/1500/972515?utm_source=openai)
- [Why highly expressed proteins evolve slowly - PubMed](https://pubmed.ncbi.nlm.nih.gov/16176987/?utm_source=openai)
- [SLR – Goldman Group](https://www.ebi.ac.uk/research/goldman/software/SLR/?utm_source=openai)
- [Cell-wide analysis of protein thermal unfolding reveals determinants of thermostability - PubMed](https://pubmed.ncbi.nlm.nih.gov/28232526/?utm_source=openai)
- [Meltome atlas—thermal proteome stability across the tree of life | Nature Methods](https://www.nature.com/articles/s41592-020-0801-4)
- [Analysis of selection in protein-coding sequences accounting for common biases | Briefings in Bioinformatics | Oxford Academic](https://academic.oup.com/bib/article/doi/10.1093/bib/bbaa431/6105943?utm_source=openai)
- [Cell-wide analysis of protein thermal unfolding reveals determinants of thermostability - PubMed](https://pubmed.ncbi.nlm.nih.gov/28232526/?utm_source=openai)
- [Cell-wide analysis of protein thermal unfolding reveals determinants of thermostability - PubMed](https://pubmed.ncbi.nlm.nih.gov/28232526/?utm_source=openai)
- [Cell-wide analysis of protein thermal unfolding reveals determinants of thermostability - PubMed](https://pubmed.ncbi.nlm.nih.gov/28232526/?utm_source=openai)
- [Why highly expressed proteins evolve slowly - PubMed](https://pubmed.ncbi.nlm.nih.gov/16176987/?utm_source=openai)
- [Cell-wide analysis of protein thermal unfolding reveals determinants of thermostability - PubMed](https://pubmed.ncbi.nlm.nih.gov/28232526/?utm_source=openai)
- [
            Pervasive Divergence in Protein Thermostability is Mediated by Both Structural Changes and Cellular Environments - PMC
        ](https://pmc.ncbi.nlm.nih.gov/articles/PMC12227239/)
- [Source](https://noble.gs.washington.edu/papers/klammer2009statistical.pdf)
- [Meltome Atlas](https://meltomeatlas.proteomics.wzw.tum.de/master_meltomeatlasapp/?utm_source=openai)
- [Thermal proximity coaggregation for system-wide profiling of protein complex dynamics in cells - PubMed](https://pubmed.ncbi.nlm.nih.gov/29439025/)
