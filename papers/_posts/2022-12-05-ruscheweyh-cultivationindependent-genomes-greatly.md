---
layout: paper
title: "Cultivation-independent genomes greatly expand taxonomic-profiling capabilities of mOTUs across various environments"
nickname: 2022-12-05-ruscheweyh-cultivationindependent-genomes-greatly
authors: "Ruscheweyh HJ, Milanese A, Paoli L, Karcher N, Clayssen Q, Keller MI, Wirbel J, Bork P, Mende DR, Zeller G, Sunagawa S"
year: "2022"
journal: "Microbiome"
volume: 10
issue: 1
pages: 212
is_published: true
image: /assets/images/papers/microbiome.png
projects:
tags: []

# Text
fulltext:
pdf:
pdflink:
pmcid: PMC9721005
preprint:
supplement:

# Links
doi: "10.1186/s40168-022-01410-z"
pmid: 36464731

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

BACKGROUND: Taxonomic profiling is a fundamental task in microbiome research that aims to detect and quantify the relative abundance of microorganisms in biological samples. Available methods using shotgun metagenomic data generally depend on the deposition of sequenced and taxonomically annotated genomes, usually from cultures of isolated strains, in reference databases (reference genomes). However, the majority of microorganisms have not been cultured yet. Thus, a substantial fraction of microbial community members remains unaccounted for during taxonomic profiling, particularly in samples from underexplored environments. To address this issue, we developed the mOTU profiler, a tool that enables reference genome-independent species-level profiling of metagenomes. As such, it supports the identification and quantification of both "known" and "unknown" species based on a set of select marker genes. RESULTS: We present mOTUs3, a command line tool that enables the profiling of metagenomes for >33,000 species-level operational taxonomic units. To achieve this, we leveraged the reconstruction of >600,000 draft genomes, most of which are metagenome-assembled genomes (MAGs), from diverse microbiomes, including soil, freshwater systems, and the gastrointestinal tract of ruminants and other animals, which we found to be underrepresented by reference genomes. Overall, two thirds of all species-level taxa lacked a reference genome. The cumulative relative abundance of these newly included taxa was low in well-studied microbiomes, such as the human body sites (6-11%). By contrast, they accounted for substantial proportions (ocean, freshwater, soil: 43-63%) or even the majority (pig, fish, cattle: 60-80%) of the relative abundance across diverse non-human-associated microbiomes. Using community-developed benchmarks and datasets, we found mOTUs3 to be more accurate than other methods and to be more congruent with 16S rRNA gene-based methods for taxonomic profiling. Furthermore, we demonstrate that mOTUs3 increases the resolution of well-known microbial groups into species-level taxa and helps identify new differentially abundant taxa in comparative metagenomic studies. CONCLUSIONS: We developed mOTUs3 to enable accurate species-level profiling of metagenomes. Compared to other methods, it provides a more comprehensive view of prokaryotic community diversity, in particular for currently underexplored microbiomes. To facilitate comparative analyses by the research community, it is released with >11,000 precomputed profiles for publicly available metagenomes and is freely available at: https://github.com/motu-tool/mOTUs . Video Abstract.
