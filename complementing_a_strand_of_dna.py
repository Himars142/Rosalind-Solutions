data= input();
output = ""

for char in data:
    if char == 'A':
        output += 'T'
    elif char == 'T':
        output += 'A'
    elif char == 'C':
        output += 'G'
    elif char == 'G':
        output += 'C'

print(output [::-1])