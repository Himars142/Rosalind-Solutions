FILE_NAME = "rosalind_revp.txt"

DNA_COMPLEMENT_TABLE = str.maketrans("ATCG", "TAGC")

with open(FILE_NAME, 'r') as file:
    entries = file.read().strip().split('>')
    for entry in entries:
        if not entry: continue
        lines = entry.splitlines()
        sequence = "".join(lines[1:])

for i in range(len(sequence)):
    for length in range(4, 13):
        sub = sequence[i : i + length]
        if len(sub) == length:
            if sub == sub.translate(DNA_COMPLEMENT_TABLE)[::-1]:
                print(i + 1, length)
        