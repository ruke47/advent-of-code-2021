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
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

score = 0
for line in lines:
    expected_closers = []
    for character in line:
        if character in openers:
            expected_closers.append(parens[character])
        elif character in closers:
            if expected_closers[-1] == character:
                expected_closers.pop()
            else:
                # illegal closer!
                score += scorekey[character]
                break
        else:
            print(f"Unexpected char: {character}")

print(f"Score: {score}")