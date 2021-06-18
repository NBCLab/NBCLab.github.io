---
layout: poster
title: "IDConn: A Python pipeline for investigating individual differences in functional brain connectivity"
nickname: 2021-06-21-bottenhorn-idconn-ohbm
authors: "Bottenhorn KL, Salo T, Bartley JE, Flannery JS, Sutherland MT, Laird AR"
year: "2021"
conference: "HBM"
image: /assets/images/posters/2021-06-21-bottenhorn-idconn-ohbm.png
projects:
tags: []

# Content
fulltext: "https://ww4.aievolution.com/hbm2101/index.cfm?do=abs.viewAbs&src=ext&abs=1565"
pdf: "https://anyscreeninc.com/PF/OHBM/2021/OHBM-Educational-Courses/pdf_poster_files/Katherine_Bottenhorn60785c7f7e1ed/Katherine_Bottenhorn.pdf"

# Links
doi:

# Data and code
github: ["https://github.com/NBCLab/IDConn"]
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

Recent research has shown variability in brain network organization within individuals is nearly as great as variability within a group. [1] This has implications for human neuroimaging research and illustrates the need for a greater understanding of sources of individual variability in brain network organization and how it relates to behavior. Here, we present an open-source pipeline for assessing Individual Differences in the brain's functional Connectivity (IDConn). IDConn is a data analysis workflow that combines methods for assessing individual differences from functional magnetic resonance imaging (fMRI) data with connectomics, network science, and robust statistical methods, adjusted to address the unique challenges of fMRI data.

## Methods

IDConn (github.com/NBCLab/IDConn) brings together existing tools to create a configurable pipeline that is accessible to researchers, regardless of their technical background. It integrates functions from Nilearn [2], Nipype [3], scikit-learn [4], SciPy [5], Numpy[6], NiBabel, Pandas, Seaborn, statsmodels, NetworkX, and the Brain Connectivity Toolbox [7] in Python to provide the following workflow (Fig. 1).
1. Computation of brain connectivity graphs (including input/output support)
2. Computation of topological and graph theoretic measures from these graphs
3. Data organization, harmonization, and treatment of missing data
4. Statistical analysis, including multivariate regressions and robust corrections for multiple comparisons
5. Generation of publication-quality figures based on these analyses

## Results

IDConn was designed for applications in human neuroimaging research, providing a flexible, open data analysis stream that takes in preprocessed fMRI data and provides computed graphs, derived graph measures, statistical models and the results thereof, and, optionally, figures presenting these results, all in an organized, sharing-friendly format for optimal reproducibility and transparency. It has already been used in two scientific publications. Gonzalez and Bottenhorn et al. [8] used an early iteration of IDConn to assess how differences in resting state functional connectivity between canonical brain networks are related to generalized anxiety and anxiety around Science, Technology, Engineering, and Math (i.e., STEM anxiety) and how these relations may differ between male and female university students before and after their first physics class (Fig. 2, top). Bottenhorn et al. [9] used IDConn to assess how task-based functional network organization supports relations between intelligence and academic achievement during physics-related cognition (Fig. 2, bottom). Bringing together robust tools for fMRI data processing and statistical inference, IDConn enables statistically-robust assessments of individual differences in functional brain connectivity and organization by neuroimaging researchers, Python-naïve to seasoned Pythonistas.

## Conclusions

IDConn is a configurable data analysis pipeline for assessing individual differences in functional connectivity and derived network measures. It amalgamates existing tools for neuroimaging data analysis, data science, machine learning, graph theoretic network analysis, statistics, and scientific computing into a unified, streamlined workflow for sophisticated, rigorous computation and extraction of connectivity and graph theoretic measures, for analyses with behavioral, demographic, psychophysiological, or other continuous variables. Furthermore, it conforms with the Brain Imaging Data Structure [10] for optimal redistribution and sharing of pipeline outputs. While there are a host of extant open-source software tools for analyzing fMRI data, many assume a level of code literacy and related skills that are not as common among researchers from the psychological sciences. IDConn fills this gap and provides an open, reproducible option for data analysis that incorporates high-quality software tools and up-to-date "best practices'' for analyzing fMRI data.
