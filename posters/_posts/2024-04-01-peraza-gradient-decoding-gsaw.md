---
layout: poster
title: "Methods for decoding cortical gradients of functional connectivity"
nickname: 2024-04-01-peraza-gradient-decoding-gsaw
authors: "Peraza JA, Salo T, Riedel MC, Bottenhorn KL, Poline J-B, Dockès J, Kent JD, Bartley JE, Flannery JS, Hill-Bowen LD, Lobo RP, Poudel R, Ray KL, Robinson JL, Laird RW, Sutherland MT, de la Vega A, Laird AR"
year: "2024"
conference: "GSAW"
image: /assets/images/posters/2024-04-01-peraza-gradient-decoding-gsaw.png
projects: ["mmmm"]
tags: []

# Content
fulltext:
pdf: https://osf.io/6grs3

# Links
doi:

# Data and code
github:
neurovault:
openneuro:
figshare:
figshare_names:
osf:
f1000:
---

{% include JB/setup %}

# Abstract

## Background

- Macroscale gradients of brain connectivity have emerged as a central principle for understanding functional brain organization.
- The functional significance and interpretation of gradients remain a central topic of discussion in the neuroimaging community.
- Previous studies have demonstrated that the gradients may be described using meta-analytic functional decoding techniques.
- However, additional methodological development is necessary to fully leverage available meta-analytic methods and resources and quantitatively evaluate their relative performance.

## Goals

**Overall Objective:** investigate and improve the framework of data-driven methods for decoding the principal gradient of functional connectivity.

- Examine and evaluate different methods for decoding brain maps on surface space.
- Establish a principled approach for gradient segmentation and meta-analytic decoding.
- Provide recommendations on best practices and develop flexible methods for gradient-based functional decoding.

## Methods

We used the resting-state fMRI (rs-fMRI) group-average dense connectome from the Human Connectome Project (HCP) S1200 data release to identify the principal gradient of functional connectivity. We evaluated three segmentation approaches: (i) percentile-based, (ii) segmentation based on a 1D k-means clustering approach, and (iii) segmentation based on the Kernel Density Estimation curve of the gradient axis. We assessed six different decoding strategies that used two meta-analytic databases (i.e., Neurosynth and NeuroQuery) and three methods to produce meta-analytic maps (i.e., term-based, LDA-based, and GC-LDA-based decoding). In addition, we proposed a method for decoding lower-order gradient maps combined with the principal gradient in a high-dimensional space.

## Results

- For small numbers of segments, a k-means algorithm yields the most confident distribution of boundaries, as shown by the silhouette coefficients, variance ratio, and cluster separation.
- LDA-based produced meta-analytic maps that yielded a relatively high correlation value and a collection of terms that naturally improved the information content, TFIDF, and SNR.
- NS and NQ performed similarly regarding their correlation profile.
- We reproduced the results from Margulies et al., showing the continuous transition from primary sensorimotor to transmodal regions.
- We proposed methods for decoding lower-order gradient maps.

## Conclusions

- We found that a two-segment solution determined by a k-means segmentation approach and an LDA-based meta-analysis combined with the NeuroQuery database was the optimal combination of methods for decoding the principal gradient of functional connectivity.
- This combination of approaches and our recommended visualization method for reporting meta-analytic decoding findings will enhance the overall interpretability of macroscale gradients in the fMRI community.
