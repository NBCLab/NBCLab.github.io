---
layout: paper
title: "Pyrodigal: Python bindings and interface to Prodigal, an efficient method for gene prediction in prokaryotes"
nickname: "2022-04-25-larralde-pyrodigal-python-bindings"
authors: "Larralde M"
year: "2022"
journal: "Journal of Open Source Software"
volume:
issue:
pages:
is_published: true
image: /assets/images/papers/joss.png
projects:
tags: []

# Text
fulltext: "https://joss.theoj.org/papers/10.21105/joss.04296"
pdf:
pdflink: "https://www.theoj.org/joss-papers/joss.04296/10.21105.joss.04296.pdf"
pmcid:
preprint:
supplement:

# Links
doi: "10.21105/joss.04296"
pmid:

# Data and code
github: [https://github.com/althonos/pyrodigal]
neurovault:
openneuro:
osf:
figshare:
---
{% include JB/setup %}

# Abstract

Improvements in sequencing technologies have seen the amount of available genomic data
expand considerably over the last twenty years. One of the key steps for analysing is the
prediction of protein-coding regions in genomic sequences, known as Open Reading Frames
(ORFs), which span between a start and a stop codon. A recent comparison of several ORF
prediction methods (Korandla et al., 2019) has shown that Prodigal (Hyatt et al., 2010), a
prokaryotic gene finder that uses dynamic programming, is one of the highest performing ab
initio ORF finders. Pyrodigal is a Python package that provides bindings and an interface to
Prodigal to make it easier to use in Python applications.