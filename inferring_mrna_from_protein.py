FILE_NAME = "rosalind_mrna.txt"

CODON_TABLE = {
    # U 
    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
    "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",

    # C 
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAC": "H", "CAA": "Q", "CAG": "Q", "CGU": "R", 
    "CGC": "R", "CGA": "R", "CGG": "R", "CAU": "H",

    # A
    "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",

    # G 
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}

with open(FILE_NAME, 'r') as file:
    protein = "".join(line.strip() for line in file.readlines()) 

mod = 0
total_count = 3

for amino_acid in protein:
    count = list(CODON_TABLE.values()).count(amino_acid)
    total_count *= count
    mod = total_count % 1000000

print(mod)
