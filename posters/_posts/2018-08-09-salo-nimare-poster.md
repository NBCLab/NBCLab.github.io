---
layout: poster
title: "NiMARE: A Neuroimaging Meta-Analysis Research Environment"
nickname: 2018-08-09-salo-nimare-poster
authors: "Salo T, Bottenhorn KL, Nichols TE, Riedel MC, Sutherland MT, Yarkoni T, Laird AR"
year: "2018"
conference: "INCF Neuroinformatics"
image: /assets/images/posters/2018-08-09-salo-nimare-poster.png
projects: [nimare]
tags: []

# Content
pdf: "https://f1000research.com/posters/7-1221"

# Links
doi: "10.7490/f1000research.1115905.1"

# Data and code
github: ["https://github.com/neurostuff/NiMARE", "https://github.com/NBCLab/nimare-incf-2018"]
neurovault:
openneuro:
osf:
f1000: "https://f1000research.com/posters/7-1221"
---
{% include JB/setup %}

# Abstract

We present NiMARE, a Python package for performing meta-analyses of the neuroimaging literature. While meta-analytic packages exist which implement one or two algorithms each, NiMARE provides a standard syntax for performing a wide range of analyses and for interacting with databases of coordinates and images from fMRI studies (e.g., brainspell, Neurosynth, and Neurovault). NiMARE joins a growing Python ecosystem for neuroimaging research, which includes such tools as nipype, nistats, and nilearn. As with these other tools, NiMARE is open source, collaboratively developed, and built with ease of use in mind.

As a demonstration of NiMARE’s capabilities, we have performed a series of image- and coordinate-based meta-analyses of a set of 21 fMRI studies of pain taken from Neurovault. NiMARE contains implementations of the nine image-based meta-analytic methods described in Maumet and Nichols (2016; MFX GLM, RFX GLM, FFX GLM, Contrast Permutation, Fisher’s, Stouffer’s, Weighted Stouffer’s, Z MFX, and Z Permutation), as well as five coordinate-based methods (ALE, SCALE, MKDA density analysis, MKDA chi-square analysis, and KDA density analysis). Results from each of these meta-analyses are shown in Figure 1. As would be expected, the image-based fixed effect procedures are much more sensitive than mixed and random effects, and the coordinate-based methods find less expansive regions of activation but generally pick up most of the pain network.
