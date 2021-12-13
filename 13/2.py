import re
fold_pattern = re.compile("fold along (x|y)=(\\d+)")

grid = {}
instructions = []
with open("input.txt") as file:
    for line in file:
        if not line.strip():
            break
        if line.startswith("fold"):
            print("You've fucked up")
        x,y = line.strip().split(",")
        grid[(int(x), int(y))] = True
    for line in file:
        m = fold_pattern.match(line.strip())
        if not m:
            print(f"Pattern didn't match: {line}")
            exit(-1)
        instructions.append((m.group(1), int(m.group(2))))


def foldy(line_y):
    keys = list(grid.keys())
    for x, y in keys:
        if y > line_y:
            grid.pop((x,y))
            new_y = 2 * line_y - y
            grid[(x, new_y)] = True


def foldx(line_x):
    keys = list(grid.keys())
    for x, y in keys:
        if x > line_x:
            grid.pop((x, y))
            new_x = 2 * line_x - x
            grid[(new_x, y)] = True


for direction, along in instructions:
    if direction == 'x':
        foldx(along)
    elif direction == 'y':
        foldy(along)
    else:
        print(f"Invalid direction: {direction}")

max_x = max([x for x,y in grid.keys()])
max_y = max([y for x,y in grid.keys()])

for y in range(max_y + 1):
    for x in range (max_x + 1):
        if (x,y) in grid.keys():
            print("@", end='')
        else:
            print(' ', end='')
    print("")