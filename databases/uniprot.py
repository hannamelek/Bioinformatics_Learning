import requests

url = "https://rest.uniprot.org/uniprotkb/P04637.fasta"

response = requests.get(url)

print(response.text)