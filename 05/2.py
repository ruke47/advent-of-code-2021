import re

span_pattern = re.compile("(\d+),(\d+) -> (\d+),(\d+)\\n")
spans = []
with open("input.txt") as file:
    for line in file:
        m = span_pattern.match(line)
        if m:
            spans.append(((int(m.group(1)), int(m.group(2))), (int(m.group(3)), int(m.group(4)))))
        else:
            print(f"non-matching line: {line}")

points = {}


def add_to_points(point):
    if point not in points:
        points[point] = 0
    points[point] += 1


for ((sx, sy), (ex, ey)) in spans:
    if sx == ex:
        x = sx
        big = max(sy, ey)
        small = min(sy, ey)
        for y in range(small, big + 1):
            add_to_points((x,y))
    elif sy == ey:
        y = sy
        big = max(sx, ex)
        small = min(sx, ex)
        for x in range(small, big + 1):
            add_to_points((x,y))
    else:
        dx = 1 if sx < ex else -1
        dy = 1 if sy < ey else -1
        x = sx
        y = sy
        while x != ex:
            add_to_points((x, y))
            x += dx
            y += dy
        add_to_points((x, y))
        if y != ey:
            print(f"You goofed! {((sx, sy), (ex, ey), (x, y))}")

two_or_more = sum(v >= 2 for v in points.values())
print(f"Two or more: {two_or_more}")
