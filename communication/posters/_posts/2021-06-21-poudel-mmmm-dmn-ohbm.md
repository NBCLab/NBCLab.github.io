---
layout: poster
title: "Working memory is linked with default mode network deactivation and real-world money saving behavior"
nickname: 2021-06-21-poudel-mmmm-dmn-ohbm
authors: "Poudel R, Tobia MJ, Riedel MC, Salo T, Flannery JS, Hill-Bowen LD, Laird AR, Dick AS, Parra CM, Sutherland MT"
year: "2021"
conference: "HBM"
image: /assets/images/posters/2021-06-21-poudel-mmmm-dmn-ohbm.png
projects: ["abcd"]
tags: []

# Content
fulltext: "https://ww4.aievolution.com/hbm2101/index.cfm?do=abs.viewAbs&src=ext&abs=1588"
pdf: "https://anyscreeninc.com/PF/OHBM/2021/OHBM-Educational-Courses/pdf_poster_files/Ranjita_Poudel60785c7f8a11b/Ranjita_Poudel.pdf"

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

The COVID-19 pandemic highlights the importance of emergency savings during uncertain times particularly among populations impacted by adverse social determinants of health (SDoH)[1]. SDoH, such as low socioeconomic status (low-SES), have been linked with a range of cognitive operations including working memory (WM), and have shown to impact health and education outcomes, rendering individuals vulnerable to disparities[2,3]. Despite evidence suggesting that financial stability may minimize SDoH related disparities[4,5], neurocognitive mechanisms associated with money-saving behavior among individuals impacted by adverse SDoH remains to be understood. To this end, we interrogated brain activity supporting WM performance, a cognitive construct widely impacted by low-SES related stress, to identify potential neurocognitive markers associated with saving behavior.

## Methods

We employed a widely utilized WM paradigm (N-back task) and collected fMRI data from individuals (n=24, 14 females; age: 24-60 years) with low-SES (income<$20,000/yr). Participants also completed a self-report measure of cognitive failures and a financial program where their money saving behavior was tracked over a 6-month period. Following preprocessing utilizing fMRIprep[6], fMRI task regressors along with nuisance regressors were entered in a subject-level general linear model to obtain task-evoked activation maps associated with three different WM loads (i.e., 1-back, 2-back, and 3-back versus vigilant 0-back)[7]. Significant brain activity related to each WM load was identified utilizing a whole brain, one-sample t-test (3dTtest++: two-tailed, pvoxel-wise=0.001, cluster extent: 26 voxels). To assess brain-behavior relationships, we assessed Pearson's correlations between beta-coefficients extracted from identified clusters and measures of WM task performance (d-prime), self-reported cognitive failures, and real-world saving behavior. We further conducted a mediation analysis to probe if task performance (M) mediated the effect of WM-related brain activity (X) on money savings (Y)[8].

## Results

Regarding task-effects, we observed WM-load related deactivations in brain regions associated with the default mode network (DMN) (i.e., precuneus and medial frontal gyrus [MFG]). Further, we observed that DMN deactivation was negatively correlated with task performance such that increased WM-related deactivations were linked with improved task performance [precuneus: r(24)=-0.43, p=0.03, MFG: r(24)=-0.43, p=0.02] [Fig.1]. As WM task performance correlated with both task-based regional deactivations and saving behavior [savings-task performance: r(24)=0.56, p=0.005], we subsequently conducted a mediation analysis to test if the influence of DMN deactivation (X) on savings behavior (Y) was mediated by task performance (M). We found that task performance fully mediated the influence of DMN deactivation on savings behavior. Specifically, when including WM task performance as a mediator, DMN's direct effect on savings failed to reach significance, whereas the indirect effect was significant (Precuneus; ab path: β = -103.96: 96% CI= -221.22, -23.06, MFG; ab path: β = -145.61: 95% CI = -420.35, -2.16) [Fig.2]. These results indicate that increased WM-related DMN deactivation predicted improved task performance and, improved task performance, in turn, predicted better saving behavior.

## Conclusions

Overall, these findings indicate that individual differences in WM performance and/or WM-related DMN deactivation may be relevant aspects associated with successful money saving behavior. Understanding underlying brain-behavior relationships associated with savings behavior among low-SES individuals may provide principled first steps toward the development of tailored interventions aiming to increase financial stability and facilitate adaptive behavioral change for financial success aimed towards minimizing SDoH related disparity.
