sums = {}
count = 0
with open("input.txt") as file:
    for line in file:
        for i, bit in enumerate(line.strip()):
            if i not in sums:
                sums[i] = 0
            sums[i] += int(bit)
        count += 1
print(f"sums: {sums} count: {count}")


gamma = 0
mask = 0
for i, sum in sums.items():
    if (sum > count / 2):
        gamma += 1 << (len(sums) - i - 1)
    mask += 1 << i

epsilon = gamma ^ mask

print(f"gamma {gamma} epsilon {epsilon} product {gamma * epsilon}")

