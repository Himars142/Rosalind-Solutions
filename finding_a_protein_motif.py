import urllib.request
import re

FILE_NAME = "rosalind_mprt.txt"

proteins = {}
ids = []

with open(FILE_NAME, 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        ids.append(line)

for identifier in ids:
    accession = identifier.split('_')[0]
    ENDPOINT_URL = f"https://rest.uniprot.org/uniprotkb/{accession}.fasta"
    with urllib.request.urlopen(ENDPOINT_URL) as response:
        data = response.read().decode("utf-8")
        proteins[identifier] = ''.join(data.splitlines()[1:])

for identifier, protein in proteins.items():
    matches = re.finditer(r'(?=(N[^P][ST][^P]))', protein)
    locations = [m.start() + 1 for m in matches]
    if locations:
        print(identifier)
        print(*locations)