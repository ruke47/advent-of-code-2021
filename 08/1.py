import re

outputs = []
line_pattern = re.compile("(\\w+) (\\w+) (\\w+) (\\w+) (\\w+) (\\w+) (\\w+) (\\w+) (\\w+) (\\w+) \\| (\\w+) (\\w+) (\\w+) (\\w+)")

with open("input.txt") as file:
    for line in file:
        m = line_pattern.match(line.strip())
        if m:
            outputs.append((m.group(11), m.group(12), m.group(13), m.group(14)))

count = 0
for output in outputs:
    for disp in output:
        length = len(disp)
        if length in (2, 3, 4, 7):
            count += 1

print(f"{count}")