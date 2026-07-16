# Week 2 – Day 6: Multiple Sequence Alignment (MSA)

## What is Multiple Sequence Alignment?

Multiple Sequence Alignment (MSA) is the process of aligning three or more DNA, RNA, or protein sequences to identify similarities and differences. Similar positions are arranged in the same columns, making it easier to study sequence conservation, mutations, and evolutionary relationships.

### Applications
- Identify conserved regions
- Detect mutations and sequence variation
- Study evolutionary relationships
- Identify functional protein domains
- Compare members of a gene or protein family

---

## Gap Penalties

During sequence alignment, gaps are introduced to represent evolutionary insertion or deletion events (indels).

Gap penalties prevent the algorithm from inserting unnecessary gaps and help produce biologically meaningful alignments.

### Types of Gap Penalties

**Gap Opening Penalty**
- Cost of creating a new gap.
- Usually assigned a larger penalty.

**Gap Extension Penalty**
- Cost of extending an existing gap.
- Usually smaller than the opening penalty because one long indel is more likely than many short ones.

---

## Global vs Local Alignment

| Feature | Global Alignment | Local Alignment |
|---------|-----------------|----------------|
| Algorithm | Needleman–Wunsch | Smith–Waterman |
| Aligns | Entire sequence | Best matching region only |
| Best for | Closely related sequences | Conserved domains or distant homologs |
| Uses full sequence | Yes | No |

### Needleman–Wunsch
- Performs end-to-end alignment.
- Suitable for sequences with similar lengths and high similarity.

### Smith–Waterman
- Finds the highest-scoring local region.
- Useful when sequences only share a conserved segment.

---

## Clustal Omega (EMBL-EBI)

Website:
https://www.ebi.ac.uk/Tools/msa/clustalo/

Clustal Omega is an online Multiple Sequence Alignment tool used to align multiple DNA, RNA, or protein sequences.

### Alignment Symbols

| Symbol | Meaning |
|---------|---------|
| `*` | Fully conserved column |
| `:` | Strongly similar residues |
| `.` | Weakly similar residues |
| Space | No significant similarity |

---

## Conserved vs Variable Regions

### Conserved Regions
- Similar or identical across sequences
- Often indicate functionally important residues
- Preserved through evolution

### Variable Regions
- Differ between sequences
- May represent mutations or evolutionary divergence
- Can contribute to species-specific adaptations

---

## Key Takeaways

- MSA aligns three or more sequences simultaneously.
- Gaps represent insertion/deletion (indel) events during evolution.
- Gap penalties produce biologically meaningful alignments.
- Needleman–Wunsch performs global alignment.
- Smith–Waterman performs local alignment.
- Conserved regions often indicate important biological functions.
- Clustal Omega is a widely used tool for Multiple Sequence Alignment.