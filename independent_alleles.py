FILE_NAME = "rosalind_lia.txt"

with open(FILE_NAME, 'r') as file:
    data = file.readline().strip().split(' ')

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)

k, N = int(data[0]), int(data[1])

total_pop = 2 ** k
total_pop_factorial = factorial(total_pop)
total_probabilty = 0


for i in range(N, total_pop + 1):
    total_pop_minus_i = total_pop - i
    total_probabilty += (total_pop_factorial/ (factorial(i) * factorial(total_pop_minus_i)) * (0.25 ** i) * (0.75 ** (total_pop_minus_i)))

print(total_probabilty)