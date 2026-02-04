from math import sqrt

FILE_NAME = "rosalind_afrq.txt"

with open(FILE_NAME, 'r') as file:
    proportion_list = [float(num) for num in file.read().strip().split(' ')]

for proportion in proportion_list:
    print(1 - ((1 - sqrt(proportion)) ** 2), end=' ')