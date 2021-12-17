min_y = -108
max_y = -68
min_x = 169
max_x = 206

class Probe:
    def __init__(self, vx, vy):
        self.x = 0
        self.y = 0
        self.vxi = vx
        self.vyi = vy
        self.vx = vx
        self.vy = vy
        self.max_y = 0
        self.turn = 0

    def tick(self):
        self.turn += 1
        self.x += self.vx
        self.y += self.vy
        if self.vx > 0:
            self.vx -= 1
        self.vy -= 1
        self.max_y = max(self.y, self.max_y)

    def within_area(self) -> bool:
        return min_x <= self.x <= max_x and min_y <= self.y <= max_y

    def overshot(self) -> bool:
        return self.y < min_y or self.x > max_x

    def undershot(self) -> bool:
        return self.vx == 0 and self.x < min_x

    def falls_within(self) -> bool:
        while True:
            self.tick()
            if self.within_area():
                return True
            if self.overshot():
                print(f"Overshot: {self.vxi, self.vyi} x {self.turn} -> {self.x, self.y}")
                return False
            if self.undershot():
                print(f"Undershot: {self.vxi, self.vyi} x {self.turn} -> {self.x, self.y}")
                return False


valid = []
for vy in range(1000, min_y - 1, -1):
    # all vx slower than 18 stall out before reaching the min_y value
    for vx in range(18, max_x + 1):
        p = Probe(vx, vy)
        if p.falls_within():
            valid.append((vx, vy))
print(f"Valid [{len(valid)}]: {valid}")
print(f"Count: {len(valid)}")