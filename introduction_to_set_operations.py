FILE_NAME = "rosalind_seto.txt"
OUTPUT_FILE = "rosalind_seto_output.txt"

TABLE = str.maketrans("", "", "{},")

with open(FILE_NAME, 'r') as file:
    n = int(file.readline().strip())
    first_set = {int(num) for num in file.readline().strip().translate(TABLE).split(' ')}
    second_set = {int(num) for num in file.readline().strip().translate(TABLE).split(' ')}
    third_set = {x for x in range(1, n + 1)}

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    file.write(str(first_set | second_set) + '\n')
    file.write(str(first_set & second_set) + '\n')
    file.write(str(first_set - second_set) + '\n')
    file.write(str(second_set - first_set) + '\n')
    file.write(str(third_set - first_set) + '\n')
    file.write(str(third_set - second_set) + '\n')