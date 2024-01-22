---
layout: paper
title: "mGene.web: a web service for accurate computational gene finding"
nickname: 2009-07-22-schweikert-mgeneweb-a-web
authors: "Schweikert G, Behr J, Zien A, Zeller G, Ong CS, Sonnenburg S, Ratsch G"
year: "2009"
journal: "Nucleic Acids Res"
volume: 37
issue: Web Server issue
pages: W312-6
is_published: true
image: /assets/images/papers/nucleic-acids-res.png
projects:
tags: []

# Text
fulltext:
pdf:
pdflink:
pmcid: PMC2703990
preprint:
supplement:

# Links
doi: "10.1093/nar/gkp479"
pmid: 19494180

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

We describe mGene.web, a web service for the genome-wide prediction of protein coding genes from eukaryotic DNA sequences. It offers pre-trained models for the recognition of gene structures including untranslated regions in an increasing number of organisms. With mGene.web, users have the additional possibility to train the system with their own data for other organisms on the push of a button, a functionality that will greatly accelerate the annotation of newly sequenced genomes. The system is built in a highly modular way, such that individual components of the framework, like the promoter prediction tool or the splice site predictor, can be used autonomously. The underlying gene finding system mGene is based on discriminative machine learning techniques and its high accuracy has been demonstrated in an international competition on nematode genomes. mGene.web is available at http://www.mgene.org/web, it is free of charge and can be used for eukaryotic genomes of small to moderate size (several hundred Mbp).
