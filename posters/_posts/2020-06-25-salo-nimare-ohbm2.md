---
layout: poster
title: "NiMARE: A Neuroimaging Meta-Analysis Research Environment"
nickname: 2020-06-25-salo-nimare-ohbm2
authors: "Salo T, Yarkoni T, Nichols TE, Bottenhorn KL, Gorgolewski KJ, Riedel MC, Kent JD, Glerean E, Bilgel M, Wright J, Reeders P, Nielson DN, Yanes JA, Perez A, Sutherland MT, Laird AR"
year: "2020"
conference: "HBM"
image: /assets/images/posters/2020-06-25-salo-nimare-ohbm2.png
projects: [nimare]
tags: []

# Content
fulltext:
pdf: "https://cdn-akamai.6connex.com/645/1827//OHBM2020_poster_15922300559215893.pdf"

# Links
doi:

# Data and code
github: ["https://github.com/neurostuff/NiMARE"]
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

Meta-analytic databases like BrainMap, Neurosynth, and NeuroVault have become extremely popular tools for a range of analyses, including coordinate- and image-based meta-analysis, region-of-interest definition, meta-analytic coactivation modeling, meta-analytic parcellation, semantic model development, and quantitative functional decoding. Each of these analyses has been approached in a number of ways across the literature, often accompanied with closed-source code, or even no code at all.

NiMARE (Neuroimaging Meta-Analysis Research Environment) is a Python library that implements a range of meta-analytic tools for neuroimaging data. NiMARE is open source, collaboratively developed, and includes citations for all methods so that the original creators will receive credit in any publications using their method. NiMARE is currently in alpha development, although in the past year the package has developed considerably. Here we describe the latest improvements to NiMARE, including documentation, implemented methods, software improvements, and future directions.

## Methods

NiMARE’s principal purpose is to consolidate meta-analytic algorithms designed for neuroimaging data into a single, open source package with a common interface across methods, much like scikit-learn has done for classification algorithms. NiMARE relies on a highly modularized coding style, in which each kind of algorithm is grouped with similar algorithms, regardless of source. This style is enhanced with an object-oriented approach, in which modules share parent classes so that each algorithm shares the same inputs, methods, and outputs with others of the same type.

## Results

Currently, NiMARE implements a number of meta-analytic algorithms and associated analytic tools. Meta-analytic algorithms are split into image- and coordinate-based methods. NiMARE includes a range of coordinate-based meta-analysis algorithms, including activation likelihood estimation, specific coactivation likelihood estimation, multilevel kernel density analysis, and kernel density analysis. For image-based meta-analyses, NiMARE implements a number of common fixed-, random-, and mixed-effects methods, and has recently added Bayesian mixed-effects methods with the Stan package. The general nature of many of these image-based methods has led the NiMARE developers to create a separate, domain-agnostic meta-analysis library, PyMARE (https://github.com/neurostuff/PyMARE), from which NiMARE can import methods and vectorize them across voxels in order to apply them to fMRI data.

In addition to meta-analyses, NiMARE has added methods for automated annotation, functional decoding, and dataset extraction. In the past year, NiMARE has added support for generalized correspondence latent Dirichlet allocation and standard latent Dirichlet allocation, as well as annotation methods using the Cognitive Atlas ontology. Associated functional decoding and encoding methods are supported as well. NiMARE has also added a number of dataset extraction methods to allow users to easily access a number of resources that can be used in conjunction with the algorithms implemented in the package.

## Conclusions

NiMARE aims to centralize neuroimaging meta-analysis methods, with contributions from both developers and users. In the past year, we have hosted a hackathon with over a dozen attendees, added support for new annotation, decoding, and extraction methods, and expanded testing and documentation. Additionally, NiMARE has been used in a number of posters, as well as the recent preprint for the NARPS project [Botvinik-Nezer et al. 2019].
