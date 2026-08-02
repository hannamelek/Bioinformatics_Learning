# Week 3 - Ensembl Notes

## What is Ensembl?

Ensembl is a genome database that provides annotated genomes for vertebrates and other species. It includes genes, transcripts, proteins, variants, and regulatory information.

---

## BRCA1

Gene Name:
BRCA1

Ensembl Gene ID:
ENSG00000012048

Species:
Homo sapiens

Chromosome:
17

---

## Gene Page

Contains:

- Gene summary
- Chromosome location
- Strand
- Gene length
- External references

---

## Transcripts

Transcript IDs begin with:

ENST

Different transcripts arise due to alternative splicing.

---

## Proteins

Protein IDs begin with:

ENSP

---

## Exons

Genes are divided into exons and introns.

The exon table provides:

- Exon number
- Coordinates
- Length

---

## Variants

Variant information includes:

- SNPs
- Insertions
- Deletions
- Clinical significance

---

## Regulation

Regulatory tracks include:

- Promoters
- Enhancers
- Histone modifications
- Open chromatin
- Transcription factor binding sites

---

## GFF3

General Feature Format version 3.

Contains annotations for:

- Genes
- Transcripts
- Exons
- CDS
- UTRs

---

## Ensembl REST API

Example:

```python
import requests

url = "https://rest.ensembl.org/lookup/symbol/homo_sapiens/BRCA1"

response = requests.get(
    url,
    headers={"Content-Type":"application/json"}
)

print(response.json())
```

---

## Key Points

- Ensembl is a genome annotation database.
- ENSG = Gene.
- ENST = Transcript.
- ENSP = Protein.
- GFF3 files contain genome annotations.
- Use Ensembl stable IDs instead of gene names in bioinformatics scripts.