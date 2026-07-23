from Bio import AlignIO
from collections import Counter
import matplotlib.pyplot as plt

align = AlignIO.read("aligned.fasta", "fasta")

print(f"Number of sequences: {len(align)}")
print(f"Alignment length: {align.get_alignment_length()}")

conservation = []

for i in range(align.get_alignment_length()):

    column = align[:, i]

    counts = Counter(column)

    most_common = counts.most_common(1)[0][1]

    percent = (most_common / len(column)) * 100

    conservation.append(percent)

# Top conserved positions
sorted_positions = sorted(
    enumerate(conservation, start=1),
    key=lambda x: x[1],
    reverse=True
)

print("\nTop 10 Conserved Positions\n")

for pos, score in sorted_positions[:10]:

    print(f"Position {pos}: {score:.1f}%")

# Plot
plt.figure(figsize=(12,5))

plt.plot(range(1, len(conservation)+1), conservation)

plt.xlabel("Alignment Position")

plt.ylabel("Conservation (%)")

plt.title("Protein Conservation Profile")

plt.ylim(0,100)

plt.grid(True)

plt.tight_layout()

plt.savefig("conservation_profile.png")

plt.show()