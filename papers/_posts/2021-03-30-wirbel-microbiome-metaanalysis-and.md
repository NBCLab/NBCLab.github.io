---
layout: paper
title: "Microbiome meta-analysis and cross-disease comparison enabled by the SIAMCAT machine learning toolbox"
nickname: 2021-03-30-wirbel-microbiome-metaanalysis-and
authors: "Wirbel J, Zych K, Essex M, Karcher N, Kartal E, Salazar G, Bork P, Sunagawa S, Zeller G"
year: "2021"
journal: "Genome Biol"
volume: 22
issue: 1
pages: 93
is_published: true
image: /assets/images/papers/genome-biol.png
projects:
tags: []

# Text
fulltext:
pdf:
pdflink:
pmcid: PMC8008609
preprint:
supplement:

# Links
doi: "10.1186/s13059-021-02306-1"
pmid: 33785070

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

The human microbiome is increasingly mined for diagnostic and therapeutic biomarkers using machine learning (ML). However, metagenomics-specific software is scarce, and overoptimistic evaluation and limited cross-study generalization are prevailing issues. To address these, we developed SIAMCAT, a versatile R toolbox for ML-based comparative metagenomics. We demonstrate its capabilities in a meta-analysis of fecal metagenomic studies (10,803 samples). When naively transferred across studies, ML models lost accuracy and disease specificity, which could however be resolved by a novel training set augmentation strategy. This reveals some biomarkers to be disease-specific, with others shared across multiple conditions. SIAMCAT is freely available from siamcat.embl.de .
