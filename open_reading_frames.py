FILE_NAME = "rosalind_orf.txt"

DNA_COMPLEMENT_TABLE = str.maketrans("ATCG", "TAGC")

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
    lines = file.readlines()
    dna_sequence = "".join(line.strip() for line in lines[1:])

dna_complement = dna_sequence.translate(DNA_COMPLEMENT_TABLE)[::-1]


def find_every_disctint_protein_candidate(*args) -> list[str]:
    proteins = set()

    for sequence in args:
        for i in range(len(sequence)):
            codon = sequence[i:i+3]
            if codon == "AUG":
                current_protein = []
                for j in range(i, len(sequence), 3):
                    codon = sequence[j:j+3]
                    amino_acid = CODON_TABLE.get(codon, '?')
                    if amino_acid == '*':
                        proteins.add("".join(current_protein))
                        break
                    else:
                        current_protein.append(amino_acid) 
        
    return list(proteins)

rna_sequence_one = dna_sequence.replace('T', 'U')
rna_sequence_two = dna_complement.replace('T', 'U')

for protein in find_every_disctint_protein_candidate(rna_sequence_one, rna_sequence_two):
    print(protein)

