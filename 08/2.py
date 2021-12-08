import re

line_pattern = re.compile("(\\w+) (\\w+) (\\w+) (\\w+) (\\w+) (\\w+) (\\w+) (\\w+) (\\w+) (\\w+) \\| (\\w+) (\\w+) (\\w+) (\\w+)")

def sortword(word):
    l = list(word)
    l.sort()
    return  ''.join(l)

puzzles = []
with open("input.txt") as file:
    for line in file:
        m = line_pattern.match(line.strip())
        if m:
            inputs = []
            for i in range(0, 10):
                inputs.append(sortword(m.group(i+1)))
            outputs = []
            for i in range(10, 14):
                outputs.append(sortword(m.group(i+1)))
            puzzles.append((inputs, outputs))
        else:
            print("Didn't pattern match!")

puzzlesum = 0
for (inputs, outputs) in puzzles:
    print(f"Inputs: {inputs}")
    one = [input for input in inputs if len(input) == 2][0]
    twos = [input for input in inputs if len(input) == 5]
    threes = twos.copy()
    four = [input for input in inputs if len(input) == 4][0]
    fives = twos.copy()
    sixes = [input for input in inputs if len(input) == 6]
    seven = [input for input in inputs if len(input) == 3][0]
    eight = [input for input in inputs if len(input) == 7][0]
    nines = sixes.copy()
    zeroes = sixes.copy()

    # a nine has all of the same segments as a four, and neither six nor zero do
    nine = [input for input in nines if set(four).issubset(set(input))][0]
    sixes.remove(nine)
    zeroes.remove(nine)

    # a zero has all of the same segments as a seven, but a six does not
    zero = [input for input in zeroes if set(seven).issubset(set(input))][0]
    sixes.remove(zero)

    # should only be one choice left for six
    six = sixes[0]

    # a three has all of the same segments as a one, and neither two nor five do
    three = [input for input in threes if set(one).issubset(set(input))][0]
    twos.remove(three)
    fives.remove(three)

    # a five is a six with an extra segment, but a two has a segment that a six does not
    five = [input for input in fives if set(input).issubset(set(six))][0]
    twos.remove(five)

    # should only be one choice left for two
    two = twos[0]

    mapping = {
        zero: 0,
        one: 1,
        two: 2,
        three: 3,
        four: 4,
        five: 5,
        six: 6,
        seven: 7,
        eight: 8,
        nine: 9
    }

    print(f"Mapping: {mapping}")
    print(f"Outputs: {outputs}\n")

    output_sum = 1000 * mapping[outputs[0]] + 100 * mapping[outputs[1]] + 10 * mapping[outputs[2]] + mapping[outputs[3]]

    puzzlesum += output_sum

print(f"Puzzlesum: {puzzlesum}")