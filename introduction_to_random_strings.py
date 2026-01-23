from math import log10

FILE_NAME = "rosalind_prob.txt"

with open(FILE_NAME, 'r') as file:
    dna_sequence = file.readline().strip()
    cg_content_list = [float(item) for item in file.readline().strip().split(' ')]

for cg_total_percentage in cg_content_list:
    probability = 0
    cg_prob = cg_total_percentage / 2
    at_prob = (1 - cg_total_percentage) / 2
    for base in dna_sequence:
        if base == 'A' or base == 'T':
            probability += log10(at_prob)
        else:
            probability += log10(cg_prob)
    print(probability, end=" ")

