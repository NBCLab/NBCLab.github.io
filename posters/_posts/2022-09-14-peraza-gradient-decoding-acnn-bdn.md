---
layout: poster
title: "Meta-analytic decoding of macroscale gradients: Segmentation of connectivity gradients"
nickname: 2022-09-14-peraza-gradient-decoding-acnn-bdn
authors: "Peraza JA, Salo T, Riedel MC, Bottenhorn KL, Poline J-B, Dockès J, Kent JD, de la Vega A, Laird AR"
year: "2022"
conference: "ACNN-BDN"
image: /assets/images/posters/2022-09-14-peraza-gradient-decoding-acnn-bdn.png
projects: ["mmmm"]
tags: []

# Content
fulltext:
pdf: https://osf.io/download/4uzpk/

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

## Introduction

Macroscale gradients have emerged as a central principle for understanding functional brain organization. Margulies et al. demonstrated that a principal gradient of connectivity exists, with unimodal, primary sensorimotor regions situated at one end and transmodal regions associated with the default mode network and representative of abstract functioning at the other. The functional interpretation of macroscale gradients remains a central topic of discussion, with some studies demonstrating that gradients may be described using meta-analytic functional decoding. Using the Neurosynth database, meta-analytic decoding of a connectivity gradient has previously been performed by first segmenting the gradient spectrum (i.e., from high- to low-intensity voxels) into five-percentile increments, binarizing the 20 resultant maps, and decoding each map. This segmented approach has been used in prior studies and allows characterization of the full gradient spectrum; however, existing segmentation procedures are arbitrarily determined with equidistant intervals (i.e., five-percentile increments) and should be based on a more data-driven approach. We investigated the performance of various methods to establish a principled approach for gradient segmentation and functional decoding.

## Methods

To this end, we utilized the resting-state fMRI (rs-fMRI) group-average dense connectome from the Human Connectome Project (HCP) S1200 data release to identify the principal gradient of functional connectivity. Following Margulies et al., an inverse Fisher transform was applied to the z-transformed correlation from the dense connectome to scale the values between -1 and 1; connections that included vertex in the medial wall were zeroed. Diffusion embedding was applied to the cosine similarity affinity matrix using the mapalign repository. We utilized the gradient (i.e., eigenvector) with the highest variance explained (i.e., eigenvalue), also called the principal gradient, for further analysis. We evaluated three segmentation approaches: (i) percentile-based, equidistant segmentation, (ii) segmentation based on a 1D k-means clustering approach, and (iii) segmentation based on the Kernel Density Estimation (KDE) curve of the gradient axis (Figure 1). n=30 different segmentations of the principal gradient for each segmentation approach were generated, corresponding to numbers of segments ranging from k=3-32 . Mean silhouette scores were computed to determine relative performance across percentile-based, k-means-based, and KDE-based segmentations, with the highest mean silhouette score representing the “best” relative performance.

## Results

We observed that a data-driven segmentation approach (e.g., KMeans-based) is preferable to an equidistant segmentation (Figure 2). In particular, the k-means clustering approach showed the “best” relative performance across segment sizes.

## Conclusions

Continued work on this project will include assessment of six decoding strategies using two meta-analytic databases and three sets of meta-analytic maps. An optimization test will be performed to identify the segmentation that yielded a maximum association between meta-analytic maps and gradient maps for each of the six decoding strategies. Data are available on G-Node GIN and version controlled with DataLad; all code required to reproduce the analyses and figures in this paper is made available on GitHub. The decoding workflow is being made available for future re-use and be linked to NiMARE as a Python module for gradient meta-analytic decoding. Taken together, the current work aims to provide recommendations on best practices, along with open-source tools and flexible methods, for gradient-based functional decoding of fMRI data.
