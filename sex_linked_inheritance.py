FILE_NAME = "rosalind_sexl.txt"

with open(FILE_NAME, 'r') as file:
    proportion_list = [float(num) for num in file.read().strip().split(' ')]

for proportion in proportion_list:
    print(2 * (proportion - (proportion ** 2)), end=' ')