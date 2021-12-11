class Octopus:
    def __init__(self, energy):
        self.energy = energy
        self.flashed_this_turn = False

    def tick(self):
        self.energy += 1
        if self.energy > 9:
            self.flashed_this_turn = True
        return self.flashed_this_turn

    def receive_energy(self):
        self.energy += 1
        if self.energy > 9 and not self.flashed_this_turn:
            self.flashed_this_turn = True
            return True
        else:
            return False

    def simmer_down(self):
        if self.flashed_this_turn:
            self.energy = 0
            self.flashed_this_turn = False

grid = []
with open("input.txt") as file:
    for line in file:
        grid.append([Octopus(int(x)) for x in line.strip()])

total_flashers = 0
for turn in range(100):
    has_flashed = set()
    to_flash = set()
    for x, row in enumerate(grid):
        for y, octopus in enumerate(row):
            if octopus.tick():
                to_flash.add((x,y))

    while len(to_flash) > 0:
        x,y = to_flash.pop()
        has_flashed.add((x,y))
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                tx = x + dx
                ty = y + dy
                if tx < 0 or ty < 0 or tx > 9 or ty > 9:
                    continue
                if grid[tx][ty].receive_energy():
                    if (tx, ty) not in has_flashed:
                        to_flash.add((tx, ty))

    print(f"Turn {turn}: {len(has_flashed)}")
    total_flashers += len(has_flashed)
    for row in grid:
        for octopus in row:
            octopus.simmer_down()

print(f"Total flashes: {total_flashers}")