FILE_NAME = "rosalind_pdst.txt"

sequences = []
result = []

with open(FILE_NAME, 'r') as file:
    for entry in file.read().strip().split('>'):
        if not entry: continue
        lines = entry.splitlines()
        sequences.append("".join(lines[1:]))

for i in range(0, len(sequences)):
    for seq in sequences:
        count = 0
        for j in range(0, len(seq)):
            if not seq[j] == sequences[i][j]:
                count += 1
        result.append(count / len(seq))
        
for k in range(0, len(result)):
    if (k + 1) % len(sequences) == 0:
        print(result[k], end='\n')
    else:
        print(result[k], end=' ')