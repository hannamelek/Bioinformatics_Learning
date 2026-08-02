import requests
import json

url = "https://rest.ensembl.org/lookup/symbol/homo_sapiens/BRCA1"

response = requests.get(
    url,
    headers={"Content-Type":"application/json"}
)

if response.status_code == 200:

    gene = response.json()

    print(json.dumps(gene, indent=2))

    print("\nGene Information")
    print("----------------")
    print("Gene:", gene["display_name"])
    print("Gene ID:", gene["id"])
    print("Species:", gene["species"])
    print("Chromosome:", gene["seq_region_name"])
    print("Start:", gene["start"])
    print("End:", gene["end"])
    print("Biotype:", gene["biotype"])

else:

    print("Request failed.")