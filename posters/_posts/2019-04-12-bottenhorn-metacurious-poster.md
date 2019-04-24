---
layout: poster
title: "metaCurious: A neuroimaging web-application for meta-analytic curation and annotation"
nickname: 2019-04-12-bottenhorn-metacurious-poster
authors: "Bottenhorn KL, Keshavan A, Somani N, Ramesh S, Poline JB, Laird AR"
year: "2019"
conference: "BRAIN Initiative Investigators Meeting"
image: /assets/images/posters/2019-04-12-bottenhorn-metacurious-poster.png
projects: [metacurious]
tags: []

# Content
fulltext:
pdf:

# Links
doi:

# Data and code
github: ["https://github.com/akeshavan/brainspell-neo-frontend"]
neurovault:
openneuro:
figshare:
figshare_names:
osf:
f1000:
---
{% include JB/setup %}

# Abstract

Neuroimaging meta-analysis allows researchers to statistically assess consensus across published results, washing out error or bias in any one published study. Databases such as BrainMap and Neurosynth facilitate meta-analysis by indexing results and meta-data from published neuroimaging papers. The two are populated by contrasting approaches: BrainMap relies on manual, human annotation, while Neurosynth takes an automated approach. BrainMap’s method yields more detailed, precise information, but is resource intensive and unable to keep up with accelerating publication of neuroimaging papers. Neurosynth keeps up with publication volume, but does not include finer details of papers’ results, which are useful for meta-analysis. The Brainspell database integrates the merits of each and addresses their drawbacks. Building on Neurosynth’s volume of automatically curated results, it allows researchers to manually annotate and correct results a la BrainMap. Here, we present metaCurious, a web application for user interaction with Brainspell’s database. metaCurious facilitates user annotation of the automatically gathered results from Neurosynth, allowing researchers to add details, such as number of subjects and stereotaxic space, and correct errors in the automatically collected neuroimaging results. In addition to adding the human element to automated database population, metaCurious integrates with GitHub to facilitate researcher collaboration in curating “Collections” of neuroimaging experiments for eventual meta-analysis. metaCurious will minimize the burden of with finding, annotating, and extracting data from neuroimaging papers for meta-analysis. To advance the curation of published research, metaCurious is being developed in conjunction with the ATHENA project, to use the classification algorithm for further annotation of the literature. ATHENA presents a middle-point between Neurosynth’s approach to annotate papers with only their most frequently used terms, without incurring the costs of manual annotation. Facilitating ATHENA’s annotation will allow metaCurious to provide more information to users, increasing the ease of meta-analysis.
