FILE_NAME = "rosalind_inod.txt"

with open(FILE_NAME, 'r') as file:
    n = int(file.read().strip())

print(n - 2)