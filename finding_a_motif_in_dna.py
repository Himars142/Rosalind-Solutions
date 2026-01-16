data = input()
substring = input()

def find_motif(data, substring):
    locations = []
    for i in range(len(data) - len(substring) + 1):
        if data[i:i + len(substring)] == substring:
            locations.append(i + 1)
    return " ".join(map(str, locations))

print(find_motif(data, substring))