---
layout: poster
title: "Denoising physiological data collected during multi-band, multi-echo EPI sequences"
nickname: 2021-06-21-bottenhorn-physio-ohbm
authors: "Bottenhorn KL, Salo T, Riedel MC, Musser ED, Robinson JL, Sutherland MT, Laird AR"
year: "2021"
conference: "HBM"
image: /assets/images/posters/2021-06-21-bottenhorn-physio-ohbm.png
projects: ["diva"]
tags: []

# Content
fulltext: "https://ww4.aievolution.com/hbm2101/index.cfm?do=abs.viewAbs&src=ext&abs=1463"
pdf: "https://anyscreeninc.com/PF/OHBM/2021/OHBM-Educational-Courses/pdf_poster_files/Katherine_Bottenhorn60785c7f4c7de/Katherine_Bottenhorn.pdf"

# Links
doi:

# Data and code
github: ["https://github.com/62442katieb/mbme-physio-denoising"]
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

The utility of physiological data collected during functional magnetic resonance imaging (fMRI) is twofold, both in removing non-neural physiological noise from fMRI data and in studying psychophysiological phenomena. However, MR sequences impart significant artifacts on simultaneously-collected physiological data, obscuring phenomena of interest and necessitating effective data cleaning approaches. While single-echo (SE) MRI sequences that measure the blood-oxygenation level dependent (BOLD) signal are the norm in fMRI research, advances in MR technology and denoising are prompting researchers to turn to multi-echo (ME) sequences, offering better differentiation between BOLD signal and non-neural noise for improved estimates of brain activation.1-3 Despite their benefits, ME sequences limit temporal resolution, as adding echoes extends repetition times (TRs), and introduce added artifacts to concurrent physiological data. The former can be mitigated by using multi-band (MB) excitation, reducing the time required to acquire a single volume by acquiring several slices simultaneously. The latter complicates the use of physiological data in fMRI studies using ME sequences, which we address here by comparing strategies for MR-artifact removal in physiological data across SE and ME BOLD fMRI scans.

## Methods

Physiological data were collected at 2000Hz using MRI-compatible equipment from BIOPAC Systems. Data were acquired using a BIOPAC MP150 system with MRI-RFIF filters: electrocardiogram (ECG) data with a 3-lead bipolar configuration and an ECG100C-MRI amplifier; electrodermal activity (EDA) recordings, from the nondominant hand, with an EDA100C-MRI amplifier.
Physiological data were acquired in the bore of a 3-Tesla Siemens MAGNETOM Prisma during both a MBSE BOLD echo planar imaging (EPI) sequence and a MBME BOLD EPI sequence.
The MBSE sequence is by the Adolescent Brain Cognitive Development (ABCD) Study,4 which acquires 60 slices with TE=30ms, TR=800ms, and MB factor of 6.
The MBME sequence is from the distribution of MB GRE-EPI sequences developed by the Center for Magnetic Resonance Research at the University of Minnesota, and acquires 48 slices in 4 echoes (TE1=11.80ms, TE2=28.04ms, TE3=44.28ms, TE4=60.52ms), TR=1500ms, MB factor of 3.5
Code used to create and apply these filters is available on GitHub (github.com/62442katieb/mbme-physio-denoising).

## Results

Following Fourier transforms of ECG and EDA data before and during both sequences, we identified MR-related noise in frequencies corresponding to the TR and slice acquisition. The effects of this noise were greater during ME than SE sequences, which is visually apparent in (1) the difference between recordings collected before and during the two BOLD EPI sequences and (2) their frequency spectra (MBSE-ECG in Fig. 1A-B vs. 1C-D; MBME-ECG in Fig. 1I-J vs. 1K-L and MBSE-ECG in Fig. 2A-B vs. 2C-D; MBME-ECG in Fig. 2I-J vs. 2K-L). By adapting recommendations from industry leaders and prior research, we developed and applied digital infinite impulse-response (IIR) notch filters, greatly reducing the impact of this noise on physiological data.

## Conclusions

MB and ME pulse sequences introduce more complicated artifacts concurrent physiological data than can be addressed with current industry recommendations. Our research finds that these artifacts are predictable and their effects can be greatly mitigated with notch filters centered at their fundamental frequencies and harmonics. By targeting the slice acquisition frequency, adjusted for MB factor, and TR frequency, especially with ME sequences, researchers should be able to remove significant MR-related artifacts from ECG and EDA data collected during fMRI scans using straightforward digital filters. Such recommendations allow researchers to capitalize on the improved SNR afforded by MBSE and MBME BOLD sequences, while including rich physiological data for both cleaning fMRI data and investigating psychophysiological phenomena.
