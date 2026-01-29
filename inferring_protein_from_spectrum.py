FILE_NAME = "rosalind_spec.txt"

AMINO_ACIDS_MASS = {
    "A": 71.03711,
    "C": 103.00919,
    "D": 115.02694,
    "E": 129.04259,
    "F": 147.06841,
    "G": 57.02146,
    "H": 137.05891,
    "I": 113.08406,
    "K": 128.09496,
    "L": 113.08406,
    "M": 131.04049,
    "N": 114.04293,
    "P": 97.05276,
    "Q": 128.05858,
    "R": 156.10111,
    "S": 87.03203,
    "T": 101.04768,
    "V": 99.06841,
    "W": 186.07931,
    "Y": 163.06333
}

with open(FILE_NAME, 'r') as file:
    mass_list = [float(mass.strip()) for mass in file.read().splitlines()]

protein_string = ""

for i in range(len(mass_list) - 1):
    portein_mass = abs(mass_list[i] - mass_list[i + 1])
    closest_mass_potein = ''
    for protein, mass in AMINO_ACIDS_MASS.items():
        if abs(portein_mass - mass) < 0.0001:
            closest_mass_potein = protein
    protein_string += closest_mass_potein

print(protein_string)