first_string = input()
second_string = input()

mutations = 0

for s1, s2 in zip(first_string, second_string):
    if s1 != s2:
        mutations += 1

print(mutations)