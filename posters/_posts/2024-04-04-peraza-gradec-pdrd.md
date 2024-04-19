---
layout: poster
title: "Gradec: Meta-analytic decoder of connectivity gradients"
nickname: 2024-04-04-peraza-gradec-pdrd
authors: "Peraza JA, Salo T, Kent JD, de la Vega A, Laird AR"
year: "2024"
conference: "PDRD"
image: /assets/images/posters/2024-04-04-peraza-gradec-pdrd.png
projects: ["mmmm"]
tags: []

# Content
fulltext:
pdf: https://osf.io/bkmca

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

Macroscale gradients of brain connectivity have emerged as a central principle for understanding functional brain organization. Previous studies have demonstrated that the principal gradient of functional connectivity in the human brain exists, with unimodal primary sensorimotor regions situated at one end and transmodal regions associated with the default mode network at the other. The functional significance and interpretation of gradients remain a central topic of discussion in the neuroimaging community, with some studies demonstrating that they may be described using meta-analytic functional decoding techniques. However, additional methodological development and tools are necessary to fully leverage available meta-analytic methods to describe connectivity gradients. To this end, we developed Gradec, an open-source Python package for surface-based functional decoding of connectivity gradients. Gradec implements a range of methods for clustering highly connected regions within the principal gradients and meta-analytic decoding on surface space. In addition, it presents a set of visualization functions to facilitate the interpretation of the functional decoding results. Notably, Gradec supports clustering and decoding on a multidimensional space, which helps describe additional components of the gradient decomposition. The current tool aims to provide recommendations on best practices and flexible tools and methods for gradient-based functional decoding of connectivity data.
