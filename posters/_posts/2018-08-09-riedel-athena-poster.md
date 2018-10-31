---
layout: poster
title: "Automating annotations of the cognitive neuroimaging literature using ATHENA"
nickname: 2018-08-09-riedel-athena-poster
authors: "Riedel MC, Salo T, Hays J, Turner MD, Sutherland MT, Turner JA, Laird AR"
year: "2018"
conference: "INCF Neuroinformatics"
image: /assets/images/posters/2018-08-09-riedel-athena-poster.png
projects: [athena]
tags: []

# Content
fulltext: "https://f1000research.com/posters/7-1229"
pdf:

# Links
doi: "10.7490/f1000research.1115916.1"

# Data and code
github:
neurovault:
openneuro:
figshare:
figshare_names:
osf:
f1000: "https://f1000research.com/posters/7-1229"
---
{% include JB/setup %}

# Abstract
We sought to develop classifiers for automatically annotating neuroimaging research articles with labels from the Cognitive Paradigm Ontology. We examined classifier performance when varying corpus (abstract-only vs full-text), feature space (bag-of-words vs Cognitive Atlas), classifiers (BnB, knn, lr, svm). The most optimal classification performance across labels utilized full-text with bag-of-words and the logistic regression algorithm. When only considering abstract-text, the Cognitive Atlas features outperformed the bag-of-words features. We also found that anatomical terms dominated the features used for classification/
