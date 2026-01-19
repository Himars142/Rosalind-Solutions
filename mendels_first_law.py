FILE_NAME = "rosalind_iprb.txt"

with open(FILE_NAME, 'r') as file:
    data = file.readline().strip().split(' ')

homozygous_dominant = int(data[0])
heterozygous = int(data[1])
homozygous_recessive = int(data[2])
total_organisms = homozygous_dominant + heterozygous + homozygous_recessive

print(1 - ((homozygous_recessive * homozygous_recessive - homozygous_recessive) + (heterozygous * homozygous_recessive) + (0.25 * heterozygous * heterozygous - 0.25 * heterozygous)) / (total_organisms * total_organisms  - total_organisms))