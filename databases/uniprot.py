import requests
from Bio import SeqIO

url = "https://rest.uniprot.org/uniprotkb/P04637.fasta"

response = requests.get(url)

if response.status_code == 200:

    with open("tp53_uniprot.fasta", "w") as file:
        file.write(response.text)

    print("Downloaded successfully!")

    record = SeqIO.read("tp53_uniprot.fasta", "fasta")

    print("ID:", record.id)
    print("Description:", record.description)
    print("Length:", len(record.seq))

else:
    print("Download failed.")