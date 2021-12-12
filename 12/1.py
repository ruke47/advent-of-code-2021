connections = []
with open("input.txt") as file:
    for line in file:
        connections.append(line.strip().split('-'))

distinct_nodes = set([node for nodes in connections for node in nodes])
neighborships = {}
for node in distinct_nodes:
    neighbors = []
    for path in connections:
        if path[0] == node:
            neighbors.append(path[1])
        if path[1] == node:
            neighbors.append(path[0])
    neighborships[node] = neighbors

def find_paths(path):
    current_node = path[-1]
    if current_node == "end":
        return [path]

    new_paths = []
    for neighbor in neighborships[current_node]:
        if neighbor.isupper() or neighbor not in path:
            new_path = path.copy()
            new_path.append(neighbor)
            new_paths.extend(find_paths(new_path))

    return new_paths


all_paths = find_paths(['start'])
print("All Paths:")
for path in all_paths:
    print(f"\t{path}")
print(f"Count: {len(all_paths)}")