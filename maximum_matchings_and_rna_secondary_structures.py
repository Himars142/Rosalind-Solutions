FILE_NAME = "rosalind_mmch.txt"

with open(FILE_NAME, 'r') as file:
    content = file.read().strip()
    entries = content.split('>')
    for entry in entries:
        if not entry: continue
        lines = entry.splitlines()
        rna_sequence = "".join(lines[1:])
    
A_count, U_count, C_count, G_count = rna_sequence.count('A'), rna_sequence.count('U'), rna_sequence.count('C'), rna_sequence.count('G')

AU_pairs = 1
CG_pairs = 1

for i in range(0, min(A_count, U_count)):
    AU_pairs *= max(A_count, U_count) - i

for i in range(0, min(C_count, G_count)):
    CG_pairs *= max(C_count, G_count) - i

print(AU_pairs * CG_pairs)