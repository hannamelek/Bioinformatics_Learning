from Bio import Entrez, SeqIO
import time

Entrez.email = "hannamelek826@gmail.com"

handle = Entrez.esearch(
    db="protein",
    term="TP53[gene] AND Homo sapiens[organism]"
)

search_results = Entrez.read(handle)
handle.close()

ids = search_results["IdList"]

print(ids)

protein_id = ids[0]

handle = Entrez.efetch(
    db="protein",
    id=protein_id,
    rettype="fasta",
    retmode="text"
)

record = SeqIO.read(handle, "fasta")
handle.close()

print(record.id)
print(record.description)
print(record.seq)

records = []

for pid in ids[:5]:

    handle = Entrez.efetch(
        db="protein",
        id=pid,
        rettype="fasta",
        retmode="text"
    )

    record = SeqIO.read(handle, "fasta")
    handle.close()

    records.append(record)

    print(record.description)

    time.sleep(0.5)

    SeqIO.write(records, "tp53_sequences.fasta", "fasta")

print("Saved", len(records), "sequences.")

handle = Entrez.efetch(
    db="protein",
    id=ids[0],
    rettype="gb",
    retmode="text"
)

record = SeqIO.read(handle, "genpept")
handle.close()

