FILE_NAME = "rosalind_sset.txt"

with open(FILE_NAME, 'r') as file:
    n = int(file.readline())

print((2 ** n) % 1000000)