from Bio import AlignIO
import matplotlib.pyplot as plt
from collections import Counter

# Read alignment
align = AlignIO.read("aligned.fasta", "fasta")

print(f"Number of sequences: {len(align)}")
print(f"Alignment length: {align.get_alignment_length()}")

print("\nFully Conserved Positions:\n")

for i in range(align.get_alignment_length()):

    column = align[:, i]

    if len(set(column)) == 1:

        print(f"Position {i+1}: {column[0]}")

conservation = []

for i in range(align.get_alignment_length()):

    column = align[:, i]

    counts = Counter(column)

    most_common = counts.most_common(1)[0][1]

    percent = (most_common / len(column))*100

    conservation.append(percent)

print("\nConservation per Position:\n")

for i, value in enumerate(conservation):

    print(f"Position {i+1}: {value:.1f}%")

plt.figure(figsize=(12,5))

plt.bar(range(1, len(conservation)+1), conservation)

plt.xlabel("Alignment Position")

plt.ylabel("Conservation (%)")

plt.title("Conservation Across Alignment")

plt.ylim(0,100)

plt.tight_layout()

plt.show()