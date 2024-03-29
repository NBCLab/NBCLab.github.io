---
layout: paper
title: "Methods for decoding cortical gradients of functional connectivity"
nickname: 2022-08-12-sutherland-the-association-of
authors: "Peraza JA, Salo T, Riedel MC, Bottenhorn KL, Poline J-B, Dockès J, Kent JD, Bartley JE, Flannery JS, Hill-Bowen LD, Lobo RP, Poudel R, Ray KL, Robinson JL, Laird RW, Sutherland MT, de la Vega A, Laird AR"
year: "2024"
journal: "Imaging Neuroscience"
volume: 2
issue:
pages: 1-32
is_published: true
image: /assets/images/papers/imaging-neuroscience.png
projects:
tags: []

# Text
fulltext:
pdf:
pdflink:
pmcid: "PMC10418206"
preprint: "https://www.biorxiv.org/content/10.1101/2023.08.01.551505v2"
supplement:

# Links
doi: "doi.org/10.1162/imag_a_00081"
pmid: 37577598

# Data and code
github:
  [
    "https://github.com/NBCLab/gradient-decoding",
    "https://github.com/JulioAPeraza/gradec",
  ]
neurovault:
openneuro:
figshare:
  [
    "https://figshare.com/projects/Meta-analytic_decoding_of_the_cortical_gradient_of_functional_connectivity/172347",
  ]
figshare_names:
osf: "https://osf.io/xzfrt/"
---

{% include JB/setup %}

# Abstract

Macroscale gradients have emerged as a central principle for understanding functional brain organization. Previous studies have demonstrated that a principal gradient of connectivity in the human brain exists, with unimodal primary sensorimotor regions situated at one end and transmodal regions associated with the default mode network and representative of abstract functioning at the other. The functional significance and interpretation of macroscale gradients remains a central topic of discussion in the neuroimaging community, with some studies demonstrating that gradients may be described using meta-analytic functional decoding techniques. However, additional methodological development is necessary to fully leverage available meta-analytic methods and resources and quantitatively evaluate their relative performance. Here, we conducted a comprehensive series of analyses to investigate and improve the framework of data-driven, meta-analytic methods, thereby establishing a principled approach for gradient segmentation and functional decoding. We found that a two-segment solution determined by a k-means segmentation approach and an LDA-based meta-analysis combined with the NeuroQuery database was the optimal combination of methods for decoding functional connectivity gradients. Finally, we proposed a method for decoding additional components of the gradient decomposition. The current work aims to provide recommendations on best practices and flexible methods for gradient-based functional decoding of fMRI data.
