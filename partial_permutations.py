FILE_NAME = "rosalind_pper.txt"

with open(FILE_NAME, 'r') as file:
    data = file.readline().strip().split(' ')
    n = int(data[0])
    k = int(data[1])

def find_partial_permutations(n, k):
    total_partial_permutations = n
    for i in range(1, k):
        total_partial_permutations *= n - i
    return total_partial_permutations % 1000000
        

print(find_partial_permutations(n, k))