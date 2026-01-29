FILE_NAME = "rosalind_tran.txt"

PURINES = "AG"
PYRIMIDINES = "CT"

sequences = []

with open(FILE_NAME, 'r') as file:
    entries = file.read().strip().split('>')
    for entry in entries:
        if not entry: continue
        lines = entry.splitlines()
        sequences.append("".join(lines[1:]))

first_dna_seq, second_dna_seq = sequences[0], sequences[1]
transitions, transversions = 0, 0

for i in range(0, len(first_dna_seq)):
    if not first_dna_seq[i] == second_dna_seq[i]:
        if (first_dna_seq[i] in PURINES and second_dna_seq[i] in PYRIMIDINES) or \
            (first_dna_seq[i] in PYRIMIDINES and second_dna_seq[i] in PURINES):
                transversions += 1
        if (first_dna_seq[i] in PURINES and second_dna_seq[i] in PURINES) or \
            (first_dna_seq[i] in PYRIMIDINES and second_dna_seq[i] in PYRIMIDINES):
                transitions += 1  

print(transitions / transversions)