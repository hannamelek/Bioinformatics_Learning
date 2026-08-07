# Week 4 — HMM Concepts

## What is an HMM?

A Hidden Markov Model (HMM) is a probabilistic model used to represent patterns in a family of related biological sequences.

A profile HMM is generally built from a multiple sequence alignment (MSA).

## HMM vs BLAST

BLAST mainly compares a query sequence with individual sequences.

HMMER compares a query sequence against a profile HMM representing an entire sequence family.

Because profile HMMs capture position-specific conservation and variation, HMMER can detect distant homologs that BLAST may miss.

## Pfam

Pfam is a database of protein families represented using profile HMMs.

I explored a kinase-related protein family/domain and examined its HMM/sequence logo.

## HMM Logo

- Tall columns = highly conserved positions
- Short columns = variable positions
- Large amino-acid letters = residues strongly preferred at that position
- Column height represents information content/conservation

## E-values

### Sequence E-value
Represents the significance of the overall sequence/profile match.

### Domain E-value
Represents the significance of a particular domain match within a sequence.

A smaller E-value indicates a more statistically significant match.

## Key Concept

MSA → Profile HMM → HMMER → Detection of distant homologs