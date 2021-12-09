grid = []
with open("input.txt") as file:
    for line in file:
        grid.append([int(x) for x in line.strip()])

width = len(grid[0])
height = len(grid)

print(f"width/height: {(width, height)}")


def is_low_point(x, y):
    val = grid[y][x]
    for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        tx = x + dx
        if tx < 0 or tx >= width:
            continue
        ty = y + dy
        if ty < 0 or ty >= height:
            continue
        if grid[ty][tx] <= val:
            return False
    return True


dangersum = 0
for y, row in enumerate(grid):
    for x, value in enumerate(row):
        if is_low_point(x, y):
            dangersum += 1 + value
            print(f"[{value}]", end='')
        else:
            print(f" {value} ", end='')
    print("")

print(f"Danger! {dangersum}")
