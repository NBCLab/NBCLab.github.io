---
layout: paper
title: "A realistic benchmark for the identification of differentially abundant taxa in (confounded) human microbiome studies"
nickname: 2024-01-04-wirbel-a-realistic-benchmark
authors: "Romano S, Wirbel J, Ansorge R, Schudoma C, Ducarmon QR, Narbad A, Zeller G"
year: "2024"
journal: "bioRxiv"
volume: 
issue: 
pages: 
is_published: false
image: /assets/images/papers/biorxiv.png
projects:
tags: ["preprint"]

# Text
fulltext:
pdf:
pdflink:
pmcid: 
preprint: https://doi.org/10.1101/2022.05.09.491139 
supplement: https://www.biorxiv.org/content/10.1101/2022.05.09.491139v2.supplementary-material

# Links
doi: "10.1101/2022.05.09.491139"
pmid: 

# Data and code
github:
neurovault:
openneuro:
figshare:
figshare_names:
osf:
---
{% include JB/setup %}

# Abstract
Background In microbiome disease association studies, it is a fundamental task to test which microbes differ in their abundance between groups. Yet, consensus on suitable or optimal statistical methods for differential abundance (DA) testing is lacking, and it remains unexplored how these cope with confounding. Previous DA benchmarks relying on simulated datasets did not quantitatively evaluate the similarity to real data, which undermines their recommendations.

Results Here we develop a simulation framework which implants calibrated signals into real taxonomic profiles, including signals mimicking confounders. Using several whole-metagenome and 16S rRNA gene amplicon datasets, we validate that our simulated data resembles real data from disease association studies to a much greater extent than in previous benchmarks. With extensively parametrized simulations we benchmark the performance of eighteen DA methods and further evaluate the best ones on confounded simulations. Only linear models, limma, fastANCOM, and the Wilcoxon test properly control false discoveries at relatively high sensitivity. When additionally considering confounders, these issues are exacerbated, but we find that post hoc adjustment can effectively mitigate them. In a large cardiometabolic disease dataset, we showcase that failure to account for covariates such as medication causes spurious association in real-world applications.

Conclusions For microbiome association studies tight error control is critical. The unsatisfactory performance of many DA methods and the persistent danger of unchecked confounding suggest these contribute to a lack of reproducibility among such studies. We have open-sourced our simulation and benchmarking software to foster a much-needed consolidation of statistical methodology for microbiome research.
