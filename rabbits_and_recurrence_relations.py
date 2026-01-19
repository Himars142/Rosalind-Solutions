FILE_NAME = "rosalind.fib.txt"

with open(FILE_NAME, 'r') as file:
    data = file.readline().strip().split(' ')

mounth = int(data[0])
new_pairs = int(data[1])

def fibonachi(mounth, new_pairs):
    previous, rab_sum = 1, 1
    for i in range(2, mounth):
        temp = rab_sum
        rab_sum += new_pairs * previous
        previous = temp;
    return rab_sum

print(fibonachi(mounth, new_pairs))