FILE_NAME = "rosalind_fibd.txt"

with open(FILE_NAME, 'r') as file:
    data = file.readline().strip().split(' ')

mounth = int(data[0])
live_mounth = int(data[1])

generations = [0] * live_mounth
generations[0] = 1

for month in range(mounth - 1):
    newborns = sum(generations[1:])
    
    for i in range(live_mounth - 1, 0, -1):
        generations[i] = generations[i-1]

    generations[0] = newborns

print(sum(generations))