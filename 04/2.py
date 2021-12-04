class Board:
    def __init__(self, lookups: dict):
        self.lookups = lookups
        self.cells = []
        self.has_won = False
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

        if rowmatch or colmatch:
            self.has_won = True

        return self.has_won

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

winner_count = 0
for call in calls:
    print(f"Call {call}")
    for i, board in enumerate(boards):
        if board.has_won:
            continue
        winner = board.mark(call)
        if winner:
            print(f"Winner #{i}")
            winner_count += 1
        if winner_count == len(boards):
            print(board.lookups)
            board.print()
            print(f"Loser! Score: {board.get_score(call)}")
            exit(0)