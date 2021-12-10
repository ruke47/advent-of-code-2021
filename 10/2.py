import math

lines = []
with open("input.txt") as file:
    for line in file:
        lines.append(line.strip())


parens = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

openers = parens.keys()
closers = parens.values()

scorekey = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

scores = []
for line in lines:
    expected_closers = []
    illegal = False
    for character in line:
        if character in openers:
            expected_closers.append(parens[character])
        elif character in closers:
            if expected_closers[-1] == character:
                expected_closers.pop()
            else:
                illegal = True
                break
        else:
            print(f"Unexpected char: {character}")

    if illegal:
        continue
    linescore = 0
    for character in expected_closers[::-1]:
        linescore *= 5
        linescore += scorekey[character]
    scores.append(linescore)

scores.sort()
print(f"Scores: {scores} len: {len(scores)}")
middle = math.ceil(len(scores)/2) - 1
print(f' Middle: {scores[middle]}')
