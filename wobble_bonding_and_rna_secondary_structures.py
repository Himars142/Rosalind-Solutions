from functools import lru_cache

FILE_NAME = "rosalind_rnas.txt"

ALLOWED_PAIRS = {'AU', 'UA', 'CG', 'GC', 'GU', 'UG'}

with open(FILE_NAME, 'r') as file:
    sequence = file.read().strip()
    
@lru_cache(None)
def count_structures(s):
    if len(s) <= 4:
        return 1
    total = count_structures(s[1:])
    for j in range(4, len(s)):
        if s[0] + s[j] in ALLOWED_PAIRS:
            rec_inside = count_structures(s[1:j])
            rec_outside = count_structures(s[j + 1:])
            total += rec_inside * rec_outside
    return total
    
print(count_structures(sequence))