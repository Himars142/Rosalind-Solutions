from functools import lru_cache

FILE_NAME = "rosalind_cat.txt"

ALLOWED_PAIRS = {'AU', 'UA', 'CG', 'GC'}

with open(FILE_NAME, 'r') as file:
    for entry in file.read().strip().split('>'):
        if not entry: continue
        lines = entry.splitlines()
        sequence = "".join(lines[1:])

@lru_cache(None)
def count_structures(s):
    if not s:
        return 1
    total = 0
    for j in range(1, len(s), 2):
        if s[0] + s[j] in ALLOWED_PAIRS:
            rec_inside = count_structures(s[1:j])
            rec_outside = count_structures(s[j + 1:])
            total += rec_inside * rec_outside
    return total % 1000000
    
print(count_structures(sequence))