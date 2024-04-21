#!/usr/bin/env python
# coding: utf-8
"""Download new lab publication information from PubMed.

We use this script to periodically search for, and download information about,
new papers by either Dr. Laird or Dr. Sutherland.
This script uses BioPython's PubMed search tool to grab information from PubMed based on search
criteria.
Then, we build a publication-specific MarkDown file for each new paper.
A lot of the elements of the file are automatically set up.
The only thing you generally have to check is that the journal cover that the MarkDown file
automatically points to exists.
If the image doesn't exist, search online for a good one, export to PNG, and reduce the size to
~150px by 300px.

You might also want to check new papers for relevant info, like a link to a GitHub repository or
OpenNeuro collection, that might be found in the text.

Unfortunately, this notebook cannot find new preprints, so the associated website files must be
created manually.
We also have to merge those files with the version grabbed from PubMed once the preprint is
published by hand.

Steps
-----
1.  Run this notebook.
2.  If any new papers were grabbed, check the following:
    a.  The journal image exists.
    b.  The paper has either of the lab PIs as an author.
        Ensure that it isn't by *another* AR Laird or MT Sutherland.
    c.  The paper is not a duplicate of a preprint or another version of the paper.
        If so, merge the two versions.
3.  Save the changes to the notebook.
4.  Push changes to the notebook and affected files to GitHub.
5.  Open a pull request to NBCLab/NBCLab.github.io.
"""
import re
from glob import glob

import pandas as pd
from Bio import Entrez, Medline
from dateutil import parser

# Only grab papers from after the lab PIs came to FIU.
searches = [
    '"Laird AR"[AUTH] AND ("2012/01/01"[PDAT] : "3000/12/31"[PDAT])',
    '"Sutherland MT"[AUTH] AND ("2012/01/01"[PDAT] : "3000/12/31"[PDAT])',
]

# Papers indexed on PubMed, but not captured by the searches.
other_pmids = [
    "33749724",
    "33932337",
]
pmid_search = "[PMID] OR ".join(other_pmids) + "[PMID]"
searches.append(pmid_search)

# Extract all publications matching term.
Entrez.email = "tsalo006@fiu.edu"

rows = []

for TERM in searches:
    h = Entrez.esearch(db="pubmed", retmax="2", term=TERM)
    result = Entrez.read(h)
    print(f"Total number of publications containing {TERM}: {result['Count']}")
    h_all = Entrez.esearch(db="pubmed", term=TERM, retmax=result["Count"])
    result_all = Entrez.read(h_all)
    ids_all = result_all["IdList"]
    h = Entrez.efetch(db="pubmed", id=ids_all, rettype="medline", retmode="text")
    records = Medline.parse(h)

    acceptable_formats = [
        "journal article",
        "comparative study",
        "editorial",
        "introductory journal article",
    ]
    for record in records:
        if any([type_.lower() in acceptable_formats for type_ in record.get("PT")]):
            pmid = record.get("PMID")
            pmcid = record.get("PMC", "")

            doi = [aid for aid in record.get("AID", []) if aid.endswith(" [doi]")]
            if doi:
                doi = doi[0].replace(" [doi]", "")
            else:
                doi = ""

            title = record.get("TI").rstrip(".")
            authors = record.get("AU")

            pub_date = parser.parse(record.get("DP"))
            year = pub_date.year
            month = pub_date.month
            day = pub_date.day

            journal = record.get("TA")
            volume = record.get("VI", "")
            issue = record.get("IP", "")
            pages = record.get("PG", "")

            abstract = record.get("AB", "")

            row = [
                pmid,
                pmcid,
                doi,
                title,
                authors,
                year,
                month,
                day,
                journal,
                volume,
                issue,
                pages,
                abstract,
            ]
            rows += [row]

# Save all relevant info from articles to a csv.
df = pd.DataFrame(
    columns=[
        "pmid",
        "pmcid",
        "doi",
        "title",
        "authors",
        "year",
        "month",
        "day",
        "journal",
        "volume",
        "issue",
        "pages",
        "abstract",
    ],
    data=rows,
)
df = df.sort_values(by=["pmid"])
df.to_csv("articles.tsv", sep="\t", lineterminator="\n", index=False)
df = df.fillna("")

# Grab our markdown file template
with open("papers/_posts/template_with_stuff.md", "r") as fo:
    template = fo.read()

old_papers = sorted(glob("papers/_posts/20*.md"))

# One paper is by another MT Sutherland.
# Something to do with mouse teeth.
skip_pmids = ["28650075"]

# Add papers we already have pages for.
old_pmids = skip_pmids
for pap in old_papers:
    # Grab each existing article's PMID
    with open(pap, "r") as fo:
        dat = fo.readlines()

    line = [lin for lin in dat if lin.startswith("pmid:")][0]
    pmid = line.replace("pmid:", "").strip()
    old_pmids.append(pmid)
    old_pmids = [pmid for pmid in old_pmids if pmid]

print(f"{len(old_papers)} existing articles found.")
print(f"{len(old_pmids)} existing articles with PubMed IDs found.")

# Just a small check. Unnecessary for the notebook.
# journals = df["journal"].str.lower().unique()
# print(journals)

# Create files for new articles
for _, row in df.iterrows():
    pmid = row["pmid"]
    if str(pmid) not in old_pmids:
        # This appears broken. 'authors' is now a list of strings.
        # authors = ast.literal_eval(row['authors'])
        authors = row["authors"]
        nick = [re.sub(r"\W+", "", w) for w in row["title"].lower().split(" ")[:3]]
        nickname = (
            f"{row['year']}-{int(row['month']):02d}-{int(row['day']):02d}-"
            f"{authors[0].split(' ')[0].lower()}-{'-'.join(nick)}"
        )
        nickname = nickname.replace(":", "")
        journal = row["journal"]
        image = f"/assets/images/papers/{'-'.join(journal.lower().split(' '))}.png"
        title = row["title"].replace('"', "'")
        completed = template.format(
            title=title,
            nickname=nickname,
            authors=", ".join(authors),
            year=int(row["year"]),
            journal=journal,
            volume=row["volume"],
            image=image,
            issue=row["issue"],
            pages=row["pages"],
            pmcid=row["pmcid"],
            doi=row["doi"],
            pmid=row["pmid"],
            abstract=row["abstract"],
        )
        with open(f"papers/_posts/{nickname}.md", "w") as fo:
            fo.write(completed)

        print(f"New file created for {pmid}")
