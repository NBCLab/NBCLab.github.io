---
layout: paper
title: "PyHMMER: a Python library binding to HMMER for efficient sequence analysis"
nickname: 2023-05-04-larralde-pyhmmer-a-python
authors: "Larralde M, Zeller G"
year: "2023"
journal: "Bioinformatics"
volume: 39
issue: 5
pages: 
is_published: true
image: /assets/images/papers/bioinformatics.png
projects:
tags: []

# Text
fulltext:
pdf:
pdflink:
pmcid: PMC10159651
preprint:
supplement:

# Links
doi: "10.1093/bioinformatics/btad214"
pmid: 37074928

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

SUMMARY: PyHMMER provides Python integration of the popular profile Hidden Markov Model software HMMER via Cython bindings. This allows the annotation of protein sequences with profile HMMs and building new ones directly with Python. PyHMMER increases flexibility of use, allowing creating queries directly from Python code, launching searches, and obtaining results without I/O, or accessing previously unavailable statistics like uncorrected P-values. A new parallelization model greatly improves performance when running multithreaded searches, while producing the exact same results as HMMER. AVAILABILITY AND IMPLEMENTATION: PyHMMER supports all modern Python versions (Python 3.6+) and similar platforms as HMMER (x86 or PowerPC UNIX systems). Pre-compiled packages are released via PyPI (https://pypi.org/project/pyhmmer/) and Bioconda (https://anaconda.org/bioconda/pyhmmer). The PyHMMER source code is available under the terms of the open-source MIT licence and hosted on GitHub (https://github.com/althonos/pyhmmer); its documentation is available on ReadTheDocs (https://pyhmmer.readthedocs.io).
