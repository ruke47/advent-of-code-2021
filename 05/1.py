import re
span_pattern = re.compile("(\d+),(\d+) -> (\d+),(\d+)\\n")
spans = []
with open("input.txt") as file:
    for line in file:
        m = span_pattern.match(line)
        if m:
            spans.append( ((int(m.group(1)), int(m.group(2))), (int(m.group(3)), int(m.group(4)))) )
        else:
            print(f"non-matching line: {line}")

points = {}
for ((sx, sy), (ex, ey)) in spans:
    if sx == ex:
        print(f"Horizontal: {(sx, sy)} -> {(ex, ey)}")
        x = sx
        big = max(sy, ey)
        small = min(sy, ey)
        for y in range(small, big + 1):
            if (x,y) not in points:
                points[(x,y)] = 0
            points[(x,y)] += 1
    if sy == ey:
        print(f"Vertical: {(sx, sy)} -> {(ex, ey)}")
        y = sy
        big = max(sx, ex)
        small = min(sx, ex)
        for x in range(small, big + 1):
            if (x,y) not in points:
                points[(x,y)] = 0
            points[(x,y)] += 1

two_or_more = sum(v >= 2 for v in points.values())
print(f"Two or more: {two_or_more}")




