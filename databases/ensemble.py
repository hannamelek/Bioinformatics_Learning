import requests
import json

url = "https://rest.ensembl.org/lookup/symbol/homo_sapiens/BRCA1"

response = requests.get(
    url,
    headers={"Content-Type": "application/json"}
)

print(json.dumps(response.json(), indent=2))