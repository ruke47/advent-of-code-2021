with open("input.txt") as file:
    points = [int(x) for x in file.readline().strip().split(",")]

cost_map = {0: 0, 1: 1}
def get_cost(distance):
    if distance in cost_map:
        return cost_map[distance]
    else:
        for n in range(max(cost_map.keys()), distance):
            cost_map[n+1] = cost_map[n] + n + 1
        return cost_map[distance]

total_costs = {}
for target in range(min(points), max(points)):
    cost = 0
    for point in points:
        cost += get_cost(abs(point - target))
    total_costs[target] = cost

smallest = sorted(total_costs.items(), key=lambda x: x[1])[0]
print(smallest)