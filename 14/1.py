from collections import Counter

instructions = {}
with open("input.txt") as file:
    polymer = list(file.readline().strip())
    file.readline()
    for line in file:
        pair, child = line.strip().split(" -> ")
        instructions[(pair[0], pair[1])] = child

for step in range(10):
    new_polymer = []
    for i in range(len(polymer) - 1):
        first = polymer[i]
        second = polymer[i+1]
        child = instructions[(first, second)]
        new_polymer.append(first)
        new_polymer.append(child)
    new_polymer.append(polymer[-1])
    polymer = new_polymer
    print(f"Step: {step} Length: {len(new_polymer)}")

counts = Counter(polymer).most_common()
most = counts[0][1]
least = counts[-1][1]
print(f"Score: {most-least}")