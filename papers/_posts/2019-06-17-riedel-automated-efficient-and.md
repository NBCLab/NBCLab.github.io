---
layout: paper
title: "Automated, Efficient, and Accelerated Knowledge Modeling of the Cognitive Neuroimaging Literature Using the ATHENA Toolkit"
nickname: 2019-05-15-riedel-automated-efficient-and
authors: "Riedel MC, Salo T, Hays J, Turner MD, Sutherland MT, Turner JA, Laird AR"
year: "2019"
journal: "Front Neurosci"
volume: 13
issue:
pages: 494
is_published: true
image: /assets/images/papers/front-neurosci.png
projects: [athena]
tags: []

# Text
fulltext: https://www.frontiersin.org/articles/10.3389/fnins.2019.00494/full#h10
pdf:
pdflink:
pmcid: PMC6530419
preprint:
supplement: https://www.frontiersin.org/articles/10.3389/fnins.2019.00494/full#supplementary-material

# Links
doi: "10.3389/fnins.2019.00494"
pmid: 31156374

# Data and code
github: ["https://github.com/NBCLab/athena"]
neurovault:
openneuro:
figshare: ["https://figshare.com/articles/Classifier_and_vectorizer_pickle_files/7203305"]
figshare_names:
osf:
---
{% include JB/setup %}

# Abstract

Neuroimaging research is growing rapidly, providing expansive resources for synthesizing data. However, navigating these dense resources is complicated by the volume of research articles and variety of experimental designs implemented across studies. The advent of machine learning algorithms and text-mining techniques has advanced automated labeling of published articles in biomedical research to alleviate such obstacles. As of yet, a comprehensive examination of document features and classifier techniques for annotating neuroimaging articles has yet to be undertaken. Here, we evaluated which combination of corpus (abstract-only or full-article text), features (bag-of-words or Cognitive Atlas terms), and classifier (Bernoulli naïve Bayes, k-nearest neighbors, logistic regression, or support vector classifier) resulted in the highest predictive performance in annotating a selection of 2,633 manually annotated neuroimaging articles. We found that, when utilizing full article text, data-driven features derived from the text performed the best, whereas if article abstracts were used for annotation, features derived from the Cognitive Atlas performed better. Additionally, we observed that when features were derived from article text, anatomical terms appeared to be the most frequently utilized for classification purposes and that cognitive concepts can be identified based on similar representations of these anatomical terms. Optimizing parameters for the automated classification of neuroimaging articles may result in a larger proportion of the neuroimaging literature being annotated with labels supporting the meta-analysis of psychological constructs.
