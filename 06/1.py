import numpy as np

class Fish:
    def __init__(self, days_left=8, multiplier=1):
        self.days_left = days_left
        self.multiplier = multiplier

    def tick(self):
        self.days_left -= 1
        if self.days_left < 0:
            self.days_left = 6
            return True
        else:
            return False

    def print(self):
        return f"{self.days_left} x {self.multiplier}"

pool = []
with open("input.txt") as file:
    all_numbers = [int(n) for n in file.readline().strip().split(",")]
    numbers, counts = np.unique(all_numbers, return_counts=True)
    for number, count in zip(numbers, counts):
        pool.append(Fish(days_left=number, multiplier=count))


for day in range(256):
    print(f"Day {day}: {[fish.print() for fish in pool]}")
    new_fish = 0
    for fish in pool:
        if fish.tick():
            new_fish += fish.multiplier
    pool.append(Fish(multiplier=new_fish))

print(f"All done! {[fish.print() for fish in pool]}")
print(f"Sums to: {sum(fish.multiplier for fish in pool)}")
