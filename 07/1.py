with open("input.txt") as file:
    points = [int(x) for x in file.readline().strip().split(",")]

total_costs = {}
for target in range(min(points), max(points)):
    cost = 0
    for point in points:
        cost += abs(point - target)
    total_costs[target] = cost

smallest = sorted(total_costs.items(), key=lambda x: x[1])[0]
print(smallest)