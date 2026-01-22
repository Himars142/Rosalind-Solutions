FILE_NAME = "rosalind_pmch.txt"

with open(FILE_NAME, 'r') as file:
    content = file.read().strip()
    entries = content.split('>')
    for entry in entries:
        if not entry: continue
        lines = entry.splitlines()
        rna_sequence = "".join(lines[1:])

A_count, C_count = rna_sequence.count('A'), rna_sequence.count('C')

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(A_count) * factorial(C_count))

