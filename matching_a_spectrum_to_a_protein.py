import collections

FILE_NAME = "rosalind_prsm.txt"

MASS_TABLE = {
    'A': 71.03711, 'C': 103.00919, 'D': 115.02694, 'E': 129.04259,
    'F': 147.06841, 'G': 57.02146, 'H': 137.05891, 'I': 113.08406,
    'K': 128.09496, 'L': 113.08406, 'M': 131.04049, 'N': 114.04293,
    'P': 97.05276, 'Q': 128.05858, 'R': 156.10111, 'S': 87.03203,
    'T': 101.04768, 'V': 99.06841, 'W': 186.07931, 'Y': 163.06333
}

protein_strings, amino_acids_mass, result = [], [], {}

with open(FILE_NAME, 'r') as file:
    n = int(file.readline().strip())
    for _ in range(n):
        protein_strings.append(file.readline().strip())
    for line in file:
        line = line.strip()
        if line:
            amino_acids_mass.append(float(line))

def get_theoretical_spectrum(protein):
    spectrum = []
    n = len(protein)
    current = 0
    for i in range(n):
        current += MASS_TABLE[protein[i]]
        spectrum.append(round(current, 5))
    current = 0
    for i in range(n - 1, 0, -1): 
        current += MASS_TABLE[protein[i]]
        spectrum.append(round(current, 5))
    return spectrum

best_protein, max_multiplicity = "", -1
        
for protein in protein_strings:
    s1_list = get_theoretical_spectrum(protein)

    diffs = []
    for r_val in s1_list:
        for s_val in amino_acids_mass:
            diffs.append(round(r_val - s_val, 4))

    if diffs:
        current_max = collections.Counter(diffs).most_common(1)[0][1]
        if current_max > max_multiplicity:
            max_multiplicity = current_max
            best_protein = protein

print(max_multiplicity)
print(best_protein)