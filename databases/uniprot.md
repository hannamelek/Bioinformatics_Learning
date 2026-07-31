# Week 3 - UniProt Notes

## What is UniProt?

UniProt is a comprehensive protein database that provides protein sequences, functions, structures, disease associations, and biological annotations.

---

## Swiss-Prot

- Reviewed by expert curators.
- High-quality annotations.
- Experimentally validated where possible.
- Preferred for research.

---

## TrEMBL

- Automatically annotated.
- Not manually reviewed.
- Larger database.
- Useful when no Swiss-Prot entry exists.

---
## TP53 (Human)

UniProt Accession:
P04637

Protein:
Cellular tumor antigen p53

Gene:
TP53

Organism:
Homo sapiens

---

## Function

- Tumor suppressor protein.
- Regulates cell cycle.
- Repairs DNA damage.
- Induces apoptosis.

---

## Subcellular Location

- Nucleus
- Cytoplasm

---

## PTMs

Common modifications include:
- Phosphorylation
- Acetylation
- Ubiquitination
- Methylation

---

## Disease

Mutations in TP53 are associated with:
- Li-Fraumeni syndrome
- Multiple human cancers

---

## PDB

UniProt provides links to experimentally determined protein structures in the Protein Data Bank (PDB).

---

## REST API

Download FASTA:

https://rest.uniprot.org/uniprotkb/P04637.fasta

Python:

```python
import requests

url = "https://rest.uniprot.org/uniprotkb/P04637.fasta"
response = requests.get(url)
print(response.text)
```

---

## Key Points

- UniProt is the primary protein annotation database.
- Swiss-Prot entries are reviewed and preferred.
- TrEMBL entries are automatically annotated.
- REST APIs allow programmatic access to protein sequences.
- P04637 is the UniProt accession for human TP53.