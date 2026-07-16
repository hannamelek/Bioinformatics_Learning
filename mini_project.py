#%%

from Bio.Blast import NCBIWWW, NCBIXML
import pandas as pd 

sequences = [
    "MTEYKLVVVGAGGVGKS",
    "MVHLTPEEKSAVTALWGKV",
    "MKWVTFISLLFLFSSAYS"
]

results = []

for i, seq in enumerate(sequences, start=1):

    print(f"\nRunning BLAST for Sequence {i}...")


    result_handle = NCBIWWW.qblast("blastp", "nr", seq)

    blast_record = NCBIXML.read(result_handle)

    if blast_record.alignments:

        hit = blast_record.alignments[0]
        hsp = hit.hsps[0]

        identity = (hsp.identities / hsp.align_length) * 100

        results.append({
            "Sequence": i,
            "Accession": hit.accession,
            "Protein": hit.title[:60],
            "E-value": hsp.expect,
            "% Identity": round(identity, 2)
        })

    else:

        results.append({
            "Sequence": i,
            "Accession": "No hit",
            "Protein": "No hit",
            "E-value": None,
            "% Identity": None
        })

df = pd.DataFrame(results)

print("\nSummary Table")
print(df)

df.to_csv("blast_summary.csv", index=False)

print("\nResults saved as blast_summary.csv")
# %%
