grid = []
with open("input.txt") as file:
    for line in file:
        grid.append([int(x) for x in line.strip()])

width = len(grid[0])
height = len(grid)

print(f"width/height: {(width, height)}")

cardinals = ((-1, 0), (1, 0), (0, -1), (0, 1))

def is_low_point(x, y):
    val = grid[x][y]
    for (dx, dy) in cardinals:
        tx = x + dx
        if tx < 0 or tx >= width:
            continue
        ty = y + dy
        if ty < 0 or ty >= height:
            continue
        if grid[tx][ty] <= val:
            return False
    return True


low_points = []
for x, row in enumerate(grid):
    for y, value in enumerate(row):
        if is_low_point(x, y):
            low_points.append((x,y))

def neighbors(x, y):
    return [(x + dx, y + dy) for (dx, dy) in cardinals]

basins = {}

print(f"low_points: {low_points}")

for (x, y) in low_points:
    explored_points = set()
    to_explore_points = {(x, y)}
    while len(to_explore_points) > 0:
        tx,ty = to_explore_points.pop()
        explored_points.add((tx, ty))

        tv = grid[tx][ty]
        for nx, ny in neighbors(tx, ty):
            if nx < 0 or ny < 0 or nx > 99 or ny > 99:
                continue
            nv = grid[nx][ny]
            if nv >= tv and nv < 9:
                if (nx, ny) not in explored_points:
                    to_explore_points.add((nx, ny))
    basins[(x,y)] = len(explored_points)

basin_values = list(basins.values())
basin_values.sort(reverse=True)

print(f"bigguns: {basin_values[0:3]} {basin_values[0] * basin_values[1] * basin_values[2]}")
