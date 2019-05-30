---
layout: poster
title: "NiMARE: A Neuroimaging Meta-Analysis Research Environment"
nickname: 2019-06-09-salo-nimare-ohbm
authors: "Salo T, Yarkoni T, Kent JD, Gorgolewski KJ, Glerean E, Bottenhorn KL, Bilgel M, Wright J, Reeders P, Nielson DN, Nichols TE, Riedel MC, Sutherland MT, Laird AR"
year: "2019"
conference: "HBM"
image: /assets/images/posters/2019-06-09-salo-nimare-ohbm.png
projects: [nimare]
tags: []

# Content
fulltext: "https://ww5.aievolution.com/hbm1901/index.cfm?do=abs.viewAbs&abs=4138"
pdf:

# Links
doi:

# Data and code
github: ["https://github.com/neurostuff/NiMARE", "https://github.com/NBCLab/nimare-ohbm-2019"]
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

We present NiMARE, a Python package for performing meta-analyses of the neuroimaging literature. While extant meta-analytic packages implement one or two algorithms each, NiMARE provides a standard syntax for performing a wide range of analyses and for interacting with databases of coordinates and images from fMRI studies (e.g., brainspell, Neurosynth, and Neurovault). NiMARE joins a growing Python ecosystem for neuroimaging research, which includes tools like nipype, nistats, and nilearn. As with these other tools, NiMARE is open source, collaboratively developed, and built with ease of use in mind.

As a demonstration of NiMARE's capabilities, we have performed a series of meta-analyses of a set of 21 fMRI studies of pain taken from Neurovault. NiMARE contains implementations of the nine image-based meta-analytic (IBMA) methods described in Maumet and Nichols (2016; MFX GLM, RFX GLM, FFX GLM, Contrast Permutation, Fisher's, Stouffer's, Weighted Stouffer's, Z MFX, and Z Permutation), as well as five coordinate-based meta-analytic (CBMA) methods (ALE, SCALE, MKDA density, MKDA chi-square, and KDA density).

## Methods

Statistical images for 21 fMRI studies of pain were downloaded from Neurovault (collection 1425). This dataset has been used in previous validations of existing meta-analytic tools (Maumet & Nichols, 2016).

Of the 21 studies, 11 included Z maps for the relevant contrast, while the rest included T maps. T maps were converted to Z maps for IBMAs using z-statistics (i.e., Fisher's, Stouffer's, weighted Stouffer's, Z MFX, and Z permutation). Each study contained contrast maps, which were used for RFX GLM, and contrast permutation IBMAs. Additionally, each study included standard error maps, which were used with the contrast maps for the FFX and MFX GLM IBMAs.

For the RFX GLM, Fisher's, Stouffer's, weighted Stouffer's, and Z MFX IBMAs, Bonferroni correction was used. For the Z-permutation and contrast permutation IBMAs, 10000 iterations were used to build null distributions, and Benjamini-Hochberg FDR correction was employed for multiple comparisons correction. FDR correction was used instead of a more stringent Bonferroni correction because the resolution of the p-values for the permutation methods are dependent on the number of iterations performed. Finally, for the IBMAs performed through FSL (FFX GLM and MFX GLM), thresholding was applied with the FSL command cluster.

For the CBMAs, peaks and subpeaks were extracted from the thresholded maps in the Results packs. For all of the CBMAs except MKDA Chi2 with FDR, FWE correction was employed with 10000 iterations. For the MKDA meta-analyses, a kernel radius of 10mm was used.

## Results

Thresholded results from each of these meta-analyses are shown in Figure 1. Each meta-analysis, both coordinate- and image-based, identifies right anterior insula, and most also include significant clusters in left anterior insula and middle cingulate cortex.

As would be expected due to their failure to model important sources of variance, the image-based fixed effect procedures (i.e., FFX GLM, Fisher's, Stouffer's, and Weighted Stouffer's) spuriously produce numerically stronger results, and the coordinate-based methods find less expansive regions of activation but generally detect most of the pain network.

## Conclusions

NiMARE implements a range of meta-analytic algorithms with a standardized interface, and will soon be expanded to include tools for derivative analyses like meta-analytic connectivity modeling, meta-analytic parcellation, automated annotation, and functional decoding. This allows users to select the most appropriate meta-analytic tool for a given analysis, without having to learn or use novel packages which may be implemented very differently from one another. For example, the code needed to run an MFX GLM using both contrast maps and error maps, a Z permutation analysis using Z-maps, and an ALE meta-analysis using coordinates and sample sizes are all similar and can be run in the same framework.
