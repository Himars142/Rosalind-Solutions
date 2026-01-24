FILE_NAME = "rosalind_sseq.txt"

with open(FILE_NAME, 'r') as file:
    sequences = []
    content = file.read().strip()
    entries = content.split('>')
    for entry in entries:
        if not entry: continue
        lines = entry.splitlines()
        seq = "".join(lines[1:])
        sequences.append(seq)

dna, subsequence = sequences[0], sequences[1]

indices = []
j = 0

for i in range(len(dna)):
    if j < len(subsequence):
        if dna[i] == subsequence[j]:
            indices.append(i + 1)
            j += 1
    
print(*indices)