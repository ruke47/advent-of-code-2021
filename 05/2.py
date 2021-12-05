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


def calc_delta(start, end):
    if start < end:
        return 1
    elif start > end:
        return -1
    else:
        return 0


for ((sx, sy), (ex, ey)) in spans:
    dx = calc_delta(sx, ex)
    dy = calc_delta(sy, ey)
    x = sx
    y = sy
    while x != ex or y != ey:
        add_to_points((x, y))
        x += dx
        y += dy
    add_to_points((x, y))

two_or_more = sum(v >= 2 for v in points.values())
print(f"Two or more: {two_or_more}")
