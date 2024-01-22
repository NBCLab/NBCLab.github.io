---
layout: paper
title: "Support vector machines-based identification of alternative splicing in Arabidopsis thaliana from whole-genome tiling arrays"
nickname: 2011-02-16-eichner-support-vector-machinesbased
authors: "Eichner J, Zeller G, Laubinger S, Ratsch G"
year: "2011"
journal: "BMC Bioinformatics"
volume: 12
issue: 
pages: 55
is_published: true
image: /assets/images/papers/bmc-bioinformatics.png
projects:
tags: []

# Text
fulltext:
pdf:
pdflink:
pmcid: PMC3051901
preprint:
supplement:

# Links
doi: "10.1186/1471-2105-12-55"
pmid: 21324185

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

BACKGROUND: Alternative splicing (AS) is a process which generates several distinct mRNA isoforms from the same gene by splicing different portions out of the precursor transcript. Due to the (patho-)physiological importance of AS, a complete inventory of AS is of great interest. While this is in reach for human and mammalian model organisms, our knowledge of AS in plants has remained more incomplete. Experimental approaches for monitoring AS are either based on transcript sequencing or rely on hybridization to DNA microarrays. Among the microarray platforms facilitating the discovery of AS events, tiling arrays are well-suited for identifying intron retention, the most prevalent type of AS in plants. However, analyzing tiling array data is challenging, because of high noise levels and limited probe coverage. RESULTS: In this work, we present a novel method to detect intron retentions (IR) and exon skips (ES) from tiling arrays. While statistical tests have typically been proposed for this purpose, our method instead utilizes support vector machines (SVMs) which are appreciated for their accuracy and robustness to noise. Existing EST and cDNA sequences served for supervised training and evaluation. Analyzing a large collection of publicly available microarray and sequence data for the model plant A. thaliana, we demonstrated that our method is more accurate than existing approaches. The method was applied in a genome-wide screen which resulted in the discovery of 1,355 IR events. A comparison of these IR events to the TAIR annotation and a large set of short-read RNA-seq data showed that 830 of the predicted IR events are novel and that 525 events (39%) overlap with either the TAIR annotation or the IR events inferred from the RNA-seq data. CONCLUSIONS: The method developed in this work expands the scarce repertoire of analysis tools for the identification of alternative mRNA splicing from whole-genome tiling arrays. Our predictions are highly enriched with known AS events and complement the A. thaliana genome annotation with respect to AS. Since all predicted AS events can be precisely attributed to experimental conditions, our work provides a basis for follow-up studies focused on the elucidation of the regulatory mechanisms underlying tissue-specific and stress-dependent AS in plants.
