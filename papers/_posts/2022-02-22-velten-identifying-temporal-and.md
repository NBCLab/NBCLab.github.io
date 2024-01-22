---
layout: paper
title: "Identifying temporal and spatial patterns of variation from multimodal data using MEFISTO"
nickname: 2022-02-22-velten-identifying-temporal-and
authors: "Velten B, Braunger JM, Argelaguet R, Arnol D, Wirbel J, Bredikhin D, Zeller G, Stegle O"
year: "2022"
journal: "Nat Methods"
volume: 19
issue: 2
pages: 179-186
is_published: true
image: /assets/images/papers/nat-methods.png
projects:
tags: []

# Text
fulltext:
pdf:
pdflink:
pmcid: PMC8828471
preprint:
supplement:

# Links
doi: "10.1038/s41592-021-01343-9"
pmid: 35027765

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

Factor analysis is a widely used method for dimensionality reduction in genome biology, with applications from personalized health to single-cell biology. Existing factor analysis models assume independence of the observed samples, an assumption that fails in spatio-temporal profiling studies. Here we present MEFISTO, a flexible and versatile toolbox for modeling high-dimensional data when spatial or temporal dependencies between the samples are known. MEFISTO maintains the established benefits of factor analysis for multimodal data, but enables the performance of spatio-temporally informed dimensionality reduction, interpolation, and separation of smooth from non-smooth patterns of variation. Moreover, MEFISTO can integrate multiple related datasets by simultaneously identifying and aligning the underlying patterns of variation in a data-driven manner. To illustrate MEFISTO, we apply the model to different datasets with spatial or temporal resolution, including an evolutionary atlas of organ development, a longitudinal microbiome study, a single-cell multi-omics atlas of mouse gastrulation and spatially resolved transcriptomics.
