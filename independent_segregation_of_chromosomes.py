from math import comb
from math import log10

FILE_NAME = "rosalind_indc.txt"

with open(FILE_NAME, 'r') as file:
    n = int(file.read().strip())

prob_list = []
result_list = []

for i in range(2 * n + 1):
    prob_list.append(comb(2 * n, i) * (0.5 ** (2 * n)))

for j in range(1, 2 * n + 1):
    result_list.append(log10(sum(prob_list[j:])))

print(*result_list)