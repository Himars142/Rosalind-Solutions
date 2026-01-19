FILE_NAME = "rosalind_perm.txt"

with open(FILE_NAME, 'r') as file:
    length = int(file.readline().strip())

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)

digits = []

for i in range(0, length):
    digits.append(i + 1)

def print_combinations(current_combination, digits):
    if not digits:
        print(*current_combination)
        return
    for digit in digits:
        new_combination = current_combination + [digit]
        remaining_digits = [d for d in digits if d != digit]
        print_combinations(new_combination, remaining_digits)
           
print(factorial(length))

print_combinations([], digits)