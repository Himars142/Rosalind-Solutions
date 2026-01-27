FILE_NAME= "rosalind_rstr.txt"

with open(FILE_NAME, 'r') as file:
    data = [float(num) for num in file.readline().strip().split(' ')]
    dna_sequence = file.readline().strip()

random_dna_seq_count, cg_prob, at_prob = data[0], data[1] / 2, (1 - data[1]) / 2

dna_seq_prob = 1 - (at_prob ** (dna_sequence.count('A') + dna_sequence.count('T')) * \
    (cg_prob ** (dna_sequence.count('C') + dna_sequence.count('G'))))
probability = 1 - (dna_seq_prob ** random_dna_seq_count)

print(probability)