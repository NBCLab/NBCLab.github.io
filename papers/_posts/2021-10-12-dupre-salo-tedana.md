---
layout: paper
title: "TE-dependent analysis of multi-echo fMRI with tedana"
nickname: 2021-10-12-dupre-salo-tedana
authors: "DuPre EM, Salo T, Ahmed Z, Bandettini PA, Bottenhorn KL, Caballero-Gaudes C, Dowdle LT, Gonzalez-Castillo J, Heunis H, Kundu P, Laird AR, Markello R, Markiewicz CJ, Moia S, Staden I, Teves JB, Uruñuela E, Vaziri-Pashkam M, Whitaker K, Handwerker DA"
year: "2021"
journal: "Journal of Open Source Software"
volume:
issue:
pages:
is_published: true
image: /assets/images/papers/joss.png
projects:
tags: []

# Text
fulltext:
pdf:
pdflink:
pmcid:
preprint:
supplement:

# Links
doi: "10.21105/joss.03669"
pmid:

# Data and code
github: ["https://github.com/ME-ICA/tedana"]
neurovault:
openneuro:
figshare:
figshare_names:
osf:
---
{% include JB/setup %}

# Summary

Functional magnetic resonance imaging (fMRI) is a popular method for in vivo neuroimaging.
Modern fMRI sequences are often weighted towards the blood oxygen level dependent (BOLD) signal, which is closely linked to neuronal activity [@Logothetis2002-af].
This weighting is achieved by tuning several parameters to increase the BOLD-weighted signal contrast.
One such parameter is “TE,” or echo time.
TE is the amount of time elapsed between when protons are excited (the MRI signal source) and measured.
Although the total measured signal magnitude decays with echo time, BOLD sensitivity increases [@Silvennoinen2003-kg].
The optimal TE maximizes the BOLD signal weighting based on a number of factors, including  several MRI scanner parameters (e.g., field strength), imaged tissue composition (e.g., grey vs. white matter), and proximity to air-tissue boundaries.

Even as optimal TE values vary by brain region, most whole-brain fMRI scans are "single-echo," where signal is collected at a fixed TE everywhere in the brain.
This TE value is often based on either a value that is best on average across all brain regions or an optimised value for a specific region of interest [@Stocker2006-ae; @Peters2007-lc].
Generally, these choices reflect a tradeoff between BOLD weighting, overall signal-to-noise ratio (SNR), and signal loss due to magnetic susceptibility artifacts.
Further, for any TE with BOLD signal there is also susceptibility to contamination from noise sources including head motion, respiration, and cardiac pulsation [@Chang2009-bj; @Power2018-ca; @Murphy2013-vo; @Caballero-Gaudes2017-ix].

Rather than collect data at a single TE, an alternative approach is to collect multiple TEs (that is, multiple echos) for each time point.
This approach, also known as multi-echo fMRI, has several benefits, including allowing researchers to estimate each voxel's T~2~^\*^ value, combining echos [@Posse1999-lt], recovering signal in regions typically not sampled at longer echo times [@Kundu2013-xm], and improving activation and connectivity mapping [@Gonzalez-Castillo2016-tj; @Caballero-Gaudes2019-lv; @Lynch2020-tz] even in real time fMRI [@Heunis2020-bd].
In addition, artifactual non-T~2~^\*^ changes (known as S~0~ in this context) may be identified and removed by leveraging the relationship between BOLD contrast and T~2~^\*^ obtained with multi-echo fMRI [@Kundu2012-bq].
Strategies to perform this efficiently and robustly are in active development.

Continuing these efforts, we present *tedana* (TE-Dependent ANAlysis) as an open-source Python package for processing and denoising multi-echo fMRI data.
*tedana* implements two approaches to multi-echo preprocessing: (1) estimating a T~2~^\*^ map and using these values to generate a weighted sum of individual echos, and  (2) using echo-time dependent information in analysis and denoising [@Kundu2012-bq].
