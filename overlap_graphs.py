FILE_NAME = "rosalind_grph.txt"

def parse_fasta(file_name):
    sequences = {}
    with open(file_name) as file:
        content = file.read().strip()
        entries = content.split('>')
    for entry in entries:
        if not entry: continue
        lines = entry.splitlines()
        sequences[lines[0]] = "".join(lines[1:])
    return sequences

data = parse_fasta(FILE_NAME)
prefixes = {}
adj = {}

for header, sequence in data.items():
    prefixes.setdefault(sequence[:3], []).append(header)

for header, sequence in data.items():
    neighbors = []
    candidates = prefixes.get(sequence[-3:], [])
    for i in candidates:
        if i != header:
            neighbors.append(i)
    if neighbors:
        adj[header] = neighbors

for node, paths in adj.items():
    for path in paths:
        print(node, path)
