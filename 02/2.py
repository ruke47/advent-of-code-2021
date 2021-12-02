cmds = []
with open("input.txt") as file:
    for line in file:
        parts = line.strip().split()
        cmds.append((parts[0], int(parts[1])))

hpos = 0
depth = 0
aim = 0
for cmd in cmds:
    if cmd[0] == 'forward':
        hpos += cmd[1]
        depth += aim * cmd[1]
    elif cmd[0] == 'down':
        aim += cmd[1]
    elif cmd[0] == 'up':
        aim -= cmd[1]
    else:
        print(f"unrecognized command: {cmd[0]}")

print(f"hpos: {hpos}\ndepth: {depth}\nmul: {hpos * depth}")
