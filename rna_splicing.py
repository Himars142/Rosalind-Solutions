FILE_NAME = 'rosalind_splc.txt'

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

def parse_fasta(file_name):
    sequences = []
    with open(file_name) as file:
        content = file.read().strip()
        entries = content.split('>')
    for entry in entries:
        if not entry: continue
        lines = entry.splitlines()
        seq = "".join(lines[1:])
        sequences.append(seq)
    return sequences

data = parse_fasta(FILE_NAME)

dna_sequence = data[0]

data.pop(0)

for intron in data:
    dna_sequence = dna_sequence.replace(intron, "")

rna_sequence = dna_sequence.replace('T', 'U')

protein = []

for i in range(0, len(rna_sequence), 3):
    codon = rna_sequence[i:i+3]
    amino_acid = CODON_TABLE.get(codon)
    if amino_acid == "*":
        break
    protein.append(amino_acid)
    
print("".join(protein))