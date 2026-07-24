# Week 2 - Day 10 Protein Conservation Project

## Objective

Analyze conservation of GAPDH proteins from ten organisms using MAFFT and Biopython.

## Workflow

- Downloaded 10 GAPDH protein sequences from UniProt.
- Combined sequences into a single FASTA file.
- Performed Multiple Sequence Alignment using MAFFT.
- Calculated conservation scores for every alignment position.
- Plotted conservation profile with Matplotlib.
- Identified the top 10 most conserved positions.
- Compared conserved regions with UniProt functional annotations.

## Files

- input.fasta
- aligned.fasta
- day10_conservation.py
- conservation_profile.png

## Conclusion
Highly conserved regions are likely to represent functionally or structurally important residues that have been preserved throughout evolution.