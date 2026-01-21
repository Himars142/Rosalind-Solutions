FILE_NAME = "rosalind_iev.txt"

with open(FILE_NAME, 'r') as file:
    data = file.readline().strip().split(' ')

AAAA, AAAa, AAaa, AaAa, Aaaa = int(data[0]), int(data[1]), int(data[2]), int(data[3]), int(data[4])

print(2 * AAAA + 2 * AAAa + 2 * AAaa + (2 * AaAa/100) * 75 + (2 * Aaaa/100) * 50)