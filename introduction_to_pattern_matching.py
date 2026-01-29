FILE_NAME = "rosalind_trie.txt"
FILE_OUTPUT = "rosalind_trie_output.txt"

with open(FILE_NAME, 'r') as file:
    sequences = file.read().splitlines()

trie = {}
result = []
node_map = {id(trie): 1}
node_counter = 1

for seq in sequences:
    node = trie
    for base in seq:
        parent_id = id(node)
        if base not in node:
            node[base] = {}
            node_counter += 1
            node_map[id(node[base])] = node_counter
            result.append(f"{node_map[parent_id]} {node_map[id(node[base])]} {base}\n")
        node = node[base]

with open(FILE_OUTPUT, 'w') as file:
    print(*result, file=file)