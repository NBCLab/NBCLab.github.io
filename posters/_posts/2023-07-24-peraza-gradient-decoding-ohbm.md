---
layout: poster
title: "Meta-analytic decoding of the cortical gradient of functional connectivity"
nickname: 2023-07-24-peraza-gradient-decoding-ohbm
authors: "Peraza JA, Salo T, Riedel MC, Bottenhorn KL, Poline J-B, Dockès J, Kent JD, Bartley JE, Flannery JS, Hill-Bowen LD, Lobo RP, Poudel R, Ray KL, Robinson JL, Laird RW, Sutherland MT, de la Vega A, Laird AR"
year: "2023"
conference: "OHBM"
image: /assets/images/posters/2023-07-24-peraza-gradient-decoding-ohbm.png
projects: ["mmmm"]
tags: []

# Content
fulltext:
pdf: https://osf.io/download/hy32g/

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

Macroscale gradients have emerged as a central principle for understanding functional brain organization. Margulies et al. demonstrated that a principal gradient of connectivity exists, with unimodal, primary sensorimotor regions situated at one end and transmodal regions associated with the default mode network and representative of abstract functioning at the other. The functional interpretation of macroscale gradients remains a central topic of discussion, with some studies demonstrating that gradients may be described using meta-analytic functional decoding. Using the Neurosynth database, meta-analytic decoding of a connectivity gradient has previously been performed by first segmenting the gradient spectrum (i.e., from high- to low-intensity voxels) into five-percentile increments, binarizing the 20 resultant maps, and decoding each map. This segmented approach has been used in prior studies and allows characterization of the full gradient spectrum. However, existing segmentation procedures are arbitrarily determined with equidistant intervals (i.e., five-percentile increments) and could be based on a more data-driven approach. We investigated the performance of various methods to establish a principled approach for gradient segmentation and functional decoding.

## Methods

HCP S1200 resting-state fMRI data were used to generate functional connectivity and compute the affinity matrix. Diffusion map embedding was applied to identify the principal gradient of functional connectivity. Whole-brain gradient maps were segmented to divide the gradient spectrum into a finite number of brain maps. Three different segmentation approaches were evaluated: percentile-based (PCT), k-means (KMeans), and KDE. Individual segments were transformed into “activation” brain maps for decoding. The three segmentation approaches were evaluated using the silhouette score. Six different meta-analytic decoding strategies were implemented on surface space, derived from three sets of meta-analytic maps (i.e., term-based (Term), LDA, and GCLDA) and two databases (i.e., NS: Neurosynth and NQ: NeuroQuery). The resultant 18 different decoding strategies were evaluated using four performance metrics, assessed by comparing correlation profiles, semantic similarity metrics (i.e., information content and TFIDF), and signal-to-noise ratio (SNR). Finally, we select the strategy with better performance across metrics for visualization, where the non-functional terms were removed from the model.

## Results

The KMeans algorithm shows the most consistent result across segment solutions, with a distribution having the highest median value and the lowest number of vertices with negative silhouette coefficients. The KMeans approach consistently resulted in better segment assignment across the cortical surface.Data-driven segmentation determined by a KMeans algorithm produced the most balanced distributions of boundaries with the highest vertex-wise and mean silhouette coefficient across segment solutions. A small number of segments is preferred if we want to produce gradient maps with high silhouette scores, and to find the highest association between the subsegment maps and meta-analytic maps. KMeans provided the best and most consistent segment assignments for the 30 segmentation solutions, with the highest values observed between 3-8 segments. With regard to segmentation approaches, PCT showed the best performance, while KMeans performed better than KDE. LDA-based decoder, in addition to showing a high average of top correlation scores, yielded the highest information content, TFIDF, and SNR, We observed little differences in correlation profile between NS and NQ combinations; in some cases, NS performed slightly better (e.g., Term-PCT), and in others, NQ showed higher correlation values to some degree (e.g., LDA-PCT). The NeuroQuery database showed a higher information content, provided by the richness of its vocabulary as compared to Neurosynth. We propose a figure that delineates the results in a way that most effectively facilitates the interpretation of the functional gradients. The figure captures the continuous transition between different functional systems, from unimodal primary sensorimotor regions associated with “motor” and “movement”, to transmodal regions associated with the default mode network and representative of abstract functioning.

## Discussion and Conclusions

For small numbers of segments, a KMeans algorithm yields the most confident distribution of boundaries as shown by the vertex-wise and mean silhouette coefficients. We determined that a large number of segments was detrimental to the performance of correlation decoders, as the average of the top correlation values decreases exponentially with the increase of the segment solution. LDA-based produced meta-analytic maps that yielded both a relatively high correlation value and a collection of terms that naturally improved the information content, TFIDF, and SNR. NS and NQ performed similarly in terms of their correlation profile, given the similarity between their corpora. The size of the vocabulary may help improve the information content of a decoder, as well as the production of more functional terms. As such we recommend using a large database with a large and rich vocabulary like NeuroQuery. In conclusion, we provide recommendations on best practices for gradient-based functional decoding of fMRI data. We found that a K-means segmentation approach and an LDA-based meta-analysis combined with the NeuroQuery database was the optimal combination of methods for decoding functional connectivity gradients.
