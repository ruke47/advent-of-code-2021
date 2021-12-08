# ended up not really using this, and instead staring at the 7-seg to see which numbers looked kind of like other numbers

used = {
    0: 'ABCEFG',
    1: 'CF',
    2: 'ACDEG',
    3: 'ACDFG',
    4: 'BCDF',
    5: 'ABDFG',
    6: 'ACDEFG',
    7: 'ACF',
    8: 'ABCDEFG',
    9: 'ABCDFG'
}

## ended up not using this at all :(
uses = {
    'A': [],
    'B': [],
    'C': [],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}
for digit, segments in used.items():
    for segment in segments:
        uses[segment].append(digit)

print(uses)
for segment, digits in uses.items():
    print(f"{segment}: {len(digits)}")
