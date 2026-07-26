# 🧬 Week 3 - NCBI Entrez Notes

## NCBI Databases

### 1. Nucleotide
- Contains DNA and RNA sequences.
- Includes genomic DNA, mRNA, cDNA, and other nucleotide records.

### 2. Protein
- Contains protein sequences translated from genes.
- Includes RefSeq, GenPept, UniProt cross-references, and submitted protein sequences.

### 3. Gene
- Provides detailed information about a gene.
- Includes gene function, aliases, chromosome location, expression, pathways, and links to protein and nucleotide records.

### 4. PubMed
- Database of biomedical research articles and scientific publications.

---

# TP53 Protein Search

Database used:
- Protein

Search term:
```
TP53 Homo sapiens
```

Selected record:
```
NP_000537.3
```

Protein:
- Tumor protein p53 isoform 1

Organism:
- Homo sapiens

---

# RefSeq Record Sections

## LOCUS
Contains basic information about the sequence including length, molecule type, and update date.

## DEFINITION
Describes what the sequence represents.

Example:
```
Tumor protein p53 isoform 1
```

## ACCESSION
Unique identifier assigned to the record.

Example:
```
NP_000537
```

## VERSION
Accession number with version.

Example:
```
NP_000537.3
```

The ".3" indicates the third version of the record.

## DBSOURCE
Shows which nucleotide (mRNA) record was used to derive the protein.

Usually linked to an NM_ accession.

## SOURCE
Scientific name of the organism.

Example:
```
Homo sapiens
```

## REFERENCE
Lists scientific publications supporting the annotation.

Contains:
- Authors
- Journal
- PubMed ID (PMID)

## COMMENT
Contains additional annotation such as:
- Biological function
- Protein information
- Curation notes

## FEATURES
Lists annotated regions of the protein.

Examples include:
- Protein
- Region
- Site
- Domain
- Chain

These identify important functional parts of the protein.

## ORIGIN
Contains the complete amino acid sequence.

---

# FASTA Format

Contains only:
- Header
- Amino acid sequence

Example:

>NP_000537.3 tumor protein p53 isoform 1

MEEPQSDPSVEPPLSQETFSDLWK...

Advantages:
- Simple
- Small file size
- Used for BLAST, alignments, and sequence analysis

---

# GenPept Format

The Protein database provides **GenPept**, not GenBank.

GenPept contains:
- LOCUS
- DEFINITION
- ACCESSION
- VERSION
- REFERENCE
- FEATURES
- COMMENT
- ORIGIN

It is the protein equivalent of the GenBank flat-file format.

---

# RefSeq vs GenBank

| RefSeq | GenBank |
|--------|----------|
| Curated by NCBI | Submitted by researchers |
| High quality | Quality varies |
| Stable accession numbers | Multiple submissions may exist |
| Prefixes: NP_, NM_, NC_ | Prefixes such as AAA..., AAB..., AK... |
| Recommended for analysis | Useful as original submissions |

---

# Biopython Entrez

Import:

```python
from Bio import Entrez, SeqIO
import time
```

Always set your email:

```python
Entrez.email = "your_email@example.com"
```

Search protein database:

```python
handle = Entrez.esearch(
    db="protein",
    term="TP53[gene] AND Homo sapiens[organism]"
)
```

Download FASTA:

```python
handle = Entrez.efetch(
    db="protein",
    id="NP_000537.3",
    rettype="fasta",
    retmode="text"
)
```

Download GenPept (GenBank format):

```python
handle = Entrez.efetch(
    db="protein",
    id="NP_000537.3",
    rettype="gb",
    retmode="text"
)
```

Read using SeqIO:

```python
record = SeqIO.read(handle, "genbank")
```

---

# NCBI Rate Limits

Without API key:
- Maximum 3 requests per second.

With API key:
- Maximum 10 requests per second.

To avoid exceeding the limit:

```python
time.sleep(0.5)
```

Always include your email address when using Entrez.

---

# Key Takeaways

- NCBI provides several databases including Nucleotide, Protein, Gene, and PubMed.
- RefSeq records (NP_, NM_, NC_) are curated and preferred for analysis.
- Protein records are downloaded in GenPept format on the website.
- Biopython retrieves GenPept records using `rettype="gb"` and parses them with `SeqIO` using the `"genbank"` format.
- FASTA contains only sequence data, while GenPept contains detailed annotations.
- Respect NCBI rate limits by setting `Entrez.email` and adding delays between requests.