FILE_NAME = "rosalind_tree.txt"

with open(FILE_NAME, 'r') as file:
    content = file.read().strip().splitlines()
    nodes_count = int(content[0])
    edges_count = len([line for line in content[1:] if line.strip()])
    print(nodes_count - 1 - edges_count)