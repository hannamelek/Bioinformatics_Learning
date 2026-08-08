from Bio import Entrez, SeqIO
import time

Entrez.email = "hannamelek826@gmail.com"

# Search NCBI Protein for human BRCA1
handle = Entrez.esearch(
    db="protein",
    term="BRCA1[gene] AND Homo sapiens[organism]"
)

results = Entrez.read(handle)
handle.close()

ids = results["IdList"]

print("Number of NCBI protein records:", len(ids))

records = []

# Download all records
for pid in ids:

    handle = Entrez.efetch(
        db="protein",
        id=pid,
        rettype="fasta",
        retmode="text"
    )

    record = SeqIO.read(handle, "fasta")
    handle.close()

    records.append(record)

    print(record.id, len(record.seq))

    time.sleep(0.5)


SeqIO.write(records, "BRCA1_proteins.fasta", "fasta")

print("Saved", len(records), "protein sequences.")

awk '$3 == "exon"' BRCA1.gff3 | wc -l