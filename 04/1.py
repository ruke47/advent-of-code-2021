class Board:
    def __init__(self, lookups: dict):
        self.lookups = lookups
        self.cells = []
        for i in range(5):
            self.cells.append([False] * 5)

    def print(self):
        for row in self.cells:
            print(row)

    def has_match(self, row, col) -> bool:
        rowmatch = True
        colmatch = True
        for i in range(5):
            rowmatch &= self.cells[row][i]
            colmatch &= self.cells[i][col]

        return rowmatch or colmatch

    def mark(self, call):
        if call in self.lookups:
            row, col = self.lookups[call]
            self.cells[row][col] = True
            return self.has_match(row, col)
        else:
            return False

    def get_score(self, call):
        sum  = 0
        for i, (r, c) in self.lookups.items():
            if not self.cells[r][c]:
                sum += int(i)
        return sum * int(call)

calls = []
boards = []
with open("input.txt") as file:
    calls = file.readline().strip().split(",")
    while file.readline():
        lookup = {}
        for row in range(5):
            for col, value in enumerate(file.readline().strip().split()):
                lookup[value] = (row, col)
        boards.append(Board(lookup))

for call in calls:
    for board in boards:
        winner = board.mark(call)
        if winner:
            board.print()
            print(board.lookups)
            print(f"Winner! Score: {board.get_score(call)}")
            exit(0)

print("Didn't find a winner")