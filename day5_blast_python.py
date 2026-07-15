#importing biopython modules

#%%
from Bio.Blast import NCBIWWW, NCBIXML

print("Submitting BLAST search...")


result = NCBIWWW.qblast("blastp", "nr", "MTEYKLVVVGAGGVGKS")

print("BLAST completed!")

records = NCBIXML.parse(result)
record = next(records)

print("\nTop 5 Hits\n")

for hit in record.alignments[:5]:
    hsp = hit.hsps[0]
    print(hit.title[:60])
    print("E-value:", hsp.expect)
    print("-" * 40)