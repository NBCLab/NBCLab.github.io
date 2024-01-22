---
layout: paper
title: "Detecting polymorphic regions in Arabidopsis thaliana with resequencing microarrays"
nickname: 2008-06-22-zeller-detecting-polymorphic-regions
authors: "Zeller G, Clark RM, Schneeberger K, Bohlen A, Weigel D, Ratsch G"
year: "2008"
journal: "Genome Res"
volume: 18
issue: 6
pages: 918-29
is_published: true
image: /assets/images/papers/genome-res.png
projects:
tags: []

# Text
fulltext:
pdf:
pdflink:
pmcid: PMC2413159
preprint:
supplement:

# Links
doi: "10.1101/gr.070169.107"
pmid: 18323538

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

Whole-genome oligonucleotide resequencing arrays have allowed the comprehensive discovery of single nucleotide polymorphisms (SNPs) in eukaryotic genomes of moderate to large size. With this technology, the detection rate for isolated SNPs is typically high. However, it is greatly reduced when other polymorphisms are located near a SNP as multiple mismatches inhibit hybridization to arrayed oligonucleotides. Contiguous tracts of suppressed hybridization therefore typify polymorphic regions (PRs) such as clusters of SNPs or deletions. We developed a machine learning method, designated margin-based prediction of polymorphic regions (mPPR), to predict PRs from resequencing array data. Conceptually similar to hidden Markov models, the method is trained with discriminative learning techniques related to support vector machines, and accurately identifies even very short polymorphic tracts (<10 bp). We applied this method to resequencing array data previously generated for the euchromatic genomes of 20 strains (accessions) of the best-characterized plant, Arabidopsis thaliana. Nonredundantly, 27% of the genome was included within the boundaries of PRs predicted at high specificity ( approximately 97%). The resulting data set provides a fine-scale view of polymorphic sequences in A. thaliana; patterns of polymorphism not apparent in SNP data were readily detected, especially for noncoding regions. Our predictions provide a valuable resource for evolutionary genetic and functional studies in A. thaliana, and our method is applicable to similar data sets in other species. More broadly, our computational approach can be applied to other segmentation tasks related to the analysis of genomic variation.
