FILE_NAME = "rosalind_cons.txt"

sequences = []
consensus = ''

with open(FILE_NAME, 'r') as file:
    entries = file.read().strip().split('>')
    for entry in entries:
        if not entry: continue            
        lines = entry.splitlines()
        sequences.append("".join(lines[1:]))

SEQUENCES_LENGTH = len(sequences[0])
BASES = "ACGT"

matrix = {
    'A': [0] * SEQUENCES_LENGTH,
    'C': [0] * SEQUENCES_LENGTH,
    'G': [0] * SEQUENCES_LENGTH,
    'T': [0] * SEQUENCES_LENGTH
}

for sequence in sequences:
    for i in range(0, SEQUENCES_LENGTH):
        matrix.get(sequence[i])[i] = matrix.get(sequence[i])[i] + 1
 

for i in range(0, SEQUENCES_LENGTH):
    biggest_value = 0
    current_key = 'A'
    for base in BASES:
        if matrix[base][i] > biggest_value:
            biggest_value = matrix[base][i]
            current_key = base
    consensus += current_key

print(consensus)

for key, value in matrix.items():
    print(key + ":", *value)