FILE_NAME = "rosalind_eval.txt"

with open(FILE_NAME, 'r') as file:
    dna_string_lenght = int(file.readline().strip())
    dna_motif = file.readline().strip()
    cg_content_list = [float(x) for x in file.readline().strip().split(' ')]

for cg_content in cg_content_list:
    at_content = 1 - cg_content
    motif_prob = (at_content/2) ** (dna_motif.count('A') + dna_motif.count('T')) * \
        ((cg_content/2) ** (dna_motif.count('C') + dna_motif.count('G')))
    print(motif_prob * (dna_string_lenght - len(dna_motif) + 1), end=' ')