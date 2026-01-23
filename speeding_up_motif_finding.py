FILE_NAME = "rosalind_kmp.txt"

with open(FILE_NAME, 'r') as file:
    lines = file.read().splitlines()
    dna_sequence = ''.join([line.strip() for line in lines[1:]])

dna_lenght = len(dna_sequence)
failure_array = [0] * dna_lenght
j, i = 0, 1

while i < dna_lenght:
    if dna_sequence[j] != dna_sequence[i]:
        if j > 0:
            j = failure_array[j-1]
        else:           
            i += 1
    else:               
        failure_array[i] = j + 1
        i += 1
        j += 1

with open(FILE_NAME, 'w') as file:
    print(*failure_array, file=file)