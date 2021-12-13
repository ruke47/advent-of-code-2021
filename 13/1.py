grid = {}
with open("input.txt") as file:
    for line in file:
        if not line.strip():
            break
        x,y = line.strip().split(",")
        grid[(int(x), int(y))] = True

def foldx(line_x):
    keys = list(grid.keys())
    for x, y in keys:
        if x >  line_x:
            grid.pop((x, y))
            new_x = 2 * line_x - x
            grid[(new_x, y)] = True


foldx(655)
print(f"Visible: {len(grid)}")