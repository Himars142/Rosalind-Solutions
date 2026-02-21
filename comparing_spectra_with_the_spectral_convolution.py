FILE_NAME = "rosalind_conv.txt"

with open(FILE_NAME, 'r') as file:
    s1_list = [float(num) for num in file.readline().strip().split()]
    s2_list = [float(num) for num in file.readline().strip().split()]

result = {}

for i in range(len(s1_list)):
    for j in range(len(s2_list)):
        current_num = round(s1_list[i] - s2_list[j], 5)
        if not result.get(current_num):
            result[current_num] = 1
        else:
            result[current_num] += 1

largest_multiplicity, absolute_value = 0, 0.0

for key, item in result.items():
    if largest_multiplicity < item:
        largest_multiplicity, absolute_value = item, key

print(largest_multiplicity, absolute_value, sep='\n')