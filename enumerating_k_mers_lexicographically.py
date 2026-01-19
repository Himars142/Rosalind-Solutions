FILE_NAME = "rosalind_lexf.txt"

with open(FILE_NAME, 'r') as file:
    letters = file.readline().strip().split(' ')
    length = int(file.readline().strip())

def print_combinations(current_combination, length, letters):
    if len(current_combination) == length:
        print(*current_combination, sep='')
        return
    for letter in letters:
        new_combination = current_combination + [letter]
        print_combinations(new_combination, length, letters)

print_combinations([], length, letters)
