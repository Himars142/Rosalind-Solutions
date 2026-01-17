data = input()

CODON_TABLE = {
    # U 
    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
    "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",

    # C 
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAC": "H", "CAU": "H", "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", 

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

def translate_rna_to_protein(data, CODON_TABLE):
    protein = []
    pairs = len(data) // 3
    for i in range(pairs):
        codon = data[i*3 : i*3 + 3]
        amino_acid = CODON_TABLE.get(codon, "?")
        if amino_acid == "?":
            print("Invalid codon: ", codon)
            continue
        if amino_acid == "*":
            break
        protein.append(amino_acid)
    return "".join(protein)

print(translate_rna_to_protein(data, CODON_TABLE))
