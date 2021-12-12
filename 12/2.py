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


def can_visit(path_so_far, target):
    if target == 'start':
        # You can never return home...
        return False
    if target.isupper():
        return True
    visited_smalls = [p for p in path_so_far if p.islower()]
    if target not in path_so_far:
        return True
    elif len(visited_smalls) == len(set(visited_smalls)):
        # no small has been visited twice
        return True
    else:
        return False


def find_paths(path):
    current_node = path[-1]
    if current_node == "end":
        return [path]

    new_paths = []
    for neighbor in neighborships[current_node]:
        if can_visit(path, neighbor):
            new_path = path.copy()
            new_path.append(neighbor)
            new_paths.extend(find_paths(new_path))

    return new_paths


all_paths = find_paths(['start'])
#print("All Paths:")
#for path in all_paths:
#    print(f"\t{path}")
print(f"Count: {len(all_paths)}")