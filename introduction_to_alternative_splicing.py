FILE_NAME = "rosalind_aspc.txt"

with open(FILE_NAME, 'r') as file:
    data = [int(num) for num in file.read().strip().split(' ')]

n, m, result = data[0], data[1], 0

def factorial(n):    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

for k in range(m, n + 1):
    result += factorial(n) // (factorial(k) * factorial(n - k))
    
print(result % 1000000)