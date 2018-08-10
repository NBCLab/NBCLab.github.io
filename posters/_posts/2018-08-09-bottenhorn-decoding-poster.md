---
layout: poster
title: "Quantitative comparison of functional decoding approaches across meta-analytic frameworks"
nickname: 2018-08-09-bottenhorn-decoding-poster
authors: "Bottenhorn KL, Salo T, Sutherland MT, Laird AR"
year: "2018"
conference: "INCF Neuroinformatics"
image: /assets/images/posters/2018-08-09-bottenhorn-decoding-poster.png
projects: []
tags: []

# Content
pdf: https://f1000research.com/posters/7-1222

# Links
doi: "10.7490/f1000research.1115906.1"

# Data and code
github: ["https://github.com/62442katieb/ns-v-bm-decoding"]
neurovault:
openneuro:
osf:
f1000: "https://f1000research.com/posters/7-1222"
---
{% include JB/setup %}

# Abstract

Functional decoding is an analytic method that seeks to determine the most consistent brain structure-function relationships; this approach typically relies on a large database of neuroimaging results. Two frameworks, Neurosynth (NS) and BrainMap (BM), offer quantitative functional decoding free of researcher bias, but their implementations differ as NS annotates each study with a bag-of-words approach, while BM relies on a structured vocabulary. To assess these differences, we performed a quantitative comparison by decoding a set of 15 ROIs using both NS and BM. NS terms were coded as “functional” (functional or subject-related) or “non-functional” (non-content or anatomical) and compared to BM terms. We observed that 43% of NS’s terms were functional, with 80% of those not corresponding to a term in BM’s taxonomy. Conversely, of BM’s terms, 44% were not represented in NS’s lexicon. Further analysis revealed that characteristics of decoded ROIs (i.e., size, false positive activation rate) were unrelated to the proportion of noise in NS decoding results or the number of significant terms returned by BM. Average correlation of NS terms analogous to BM terms was 0.09, compared to an average correlation of 0.36 for the top 50 functional NS terms. Overall, we observed that NS’s functional terms provide high specificity, but require filtering through many non-informative terms. In contrast, BM provides broad descriptions that less accurately relate function to brain activations.
