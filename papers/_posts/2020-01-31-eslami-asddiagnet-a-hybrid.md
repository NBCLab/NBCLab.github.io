---
layout: paper
title: "ASD-DiagNet: A Hybrid Learning Approach for Detection of Autism Spectrum Disorder Using fMRI Data"
nickname: 2020-01-31-eslami-asddiagnet-a-hybrid
authors: "Eslami T, Mirjalili V, Fong A, Laird AR, Saeed F"
year: "2020"
journal: "Front Neuroinform"
volume: 13
issue:
pages: 70
is_published: true
image: /assets/images/papers/front-neuroinform.png
projects:
tags: []

# Text
fulltext:
pdf:
pdflink:
pmcid: PMC6890833
preprint:
supplement:

# Links
doi: "10.3389/fninf.2019.00070"
pmid: 31827430

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

Heterogeneous mental disorders such as Autism Spectrum Disorder (ASD) are notoriously difficult to diagnose, especially in children. The current psychiatric diagnostic process is based purely on the behavioral observation of symptomology (DSM-5/ICD-10) and may be prone to misdiagnosis. In order to move the field toward more quantitative diagnosis, we need advanced and scalable machine learning infrastructure that will allow us to identify reliable biomarkers of mental health disorders. In this paper, we propose a framework called ASD-DiagNet for classifying subjects with ASD from healthy subjects by using only fMRI data. We designed and implemented a joint learning procedure using an autoencoder and a single layer perceptron (SLP) which results in improved quality of extracted features and optimized parameters for the model. Further, we designed and implemented a data augmentation strategy, based on linear interpolation on available feature vectors, that allows us to produce synthetic datasets needed for training of machine learning models. The proposed approach is evaluated on a public dataset provided by Autism Brain Imaging Data Exchange including 1, 035 subjects coming from 17 different brain imaging centers. Our machine learning model outperforms other state of the art methods from 10 imaging centers with increase in classification accuracy up to 28% with maximum accuracy of 82%. The machine learning technique presented in this paper, in addition to yielding better quality, gives enormous advantages in terms of execution time (40 min vs. 7 h on other methods). The implemented code is available as GPL license on GitHub portal of our lab (https://github.com/pcdslab/ASD-DiagNet).
