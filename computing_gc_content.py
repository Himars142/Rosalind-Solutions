FILE_NAME = "rosalind_gc.txt"

sequences = {}
current_id = None

with open(FILE_NAME, 'r') as f:
    for line in f:
        line = line.strip()

        if not line:
            continue

        if line.startswith(">"):
            current_id = line[1:]
            sequences[current_id] = ""
        else:
            sequences[current_id] += line

biggest_cg_content = 0
biggest_cg_content_id = None

for sequence in sequences:
    dna = sequences[sequence]
    cg_count = dna.count("C") + dna.count("G")
    current_cg_content = 100/len(dna) * cg_count
    if(biggest_cg_content < current_cg_content):
        biggest_cg_content = current_cg_content
        biggest_cg_content_id = sequence

print(biggest_cg_content_id)
print(biggest_cg_content)