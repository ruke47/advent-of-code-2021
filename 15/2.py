import math

class Node:
    def __init__(self, x, y, ownscore):
        self.x = x
        self.y = y
        self.own_score = ownscore
        self.best_score = math.inf

    def set_best_score(self, neighbor_score):
        self.best_score = min(self.own_score + neighbor_score, self.best_score)

    def find_neighbors(self, grid):
        neighbors = []
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            n = (self.x + dx, self.y + dy)
            if n in grid.keys():
                neighbors.append(grid[n])
        return neighbors

    def to_str(self):
        return f'[{self.x, self.y}: {self.own_score, self.best_score}]'


grid: dict[(int, int), Node] = {}
size = 100

with open("input.txt") as file:
    for y, line in enumerate(file):
        for ym in range(5):
            for x, val in enumerate(line.strip()):
                for xm in range(5):
                    ival = int(val)
                    tx = xm * size + x
                    ty = ym * size + y
                    tv = ival + xm + ym
                    if tv > 9:
                        tv -= 9
                    grid[(tx , ty)] = Node(tx, ty, tv)

start = grid[(0,0)]
start.best_score = 0
to_consider = {start}
visited = set()

while True:
    best = min(to_consider, key=lambda node: node.best_score)
    to_consider.remove(best)
    visited.add(best)

    if best.x == best.y == size * 5 - 1:
        print(f'Best Path Score: {best.best_score}')
        break

    for neighbor in best.find_neighbors(grid):
        neighbor.set_best_score(best.best_score)
        if neighbor not in visited:
            to_consider.add(neighbor)
