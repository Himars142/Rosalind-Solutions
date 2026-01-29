FILE_NAME = "rosalind_kmer.txt"

with open(FILE_NAME, 'r') as file:
    sequence = "".join(file.read().splitlines()[1:])

k_mers = {}

for i in range(len(sequence)):
    if i + 4 > len(sequence): break
    k_mer = sequence[i:i + 4]
    if not k_mers.get(k_mer):
        k_mers[k_mer] = 1
    else:
        k_mers[k_mer] += 1

for kmer in sorted(k_mers.keys()):
    print(k_mers[kmer], end=' ')