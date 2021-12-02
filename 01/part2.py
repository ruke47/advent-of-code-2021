measurements = []
with open("input.txt") as file:
    for line in file:
        measurements.append(int(line))

old_sum = measurements[0] + measurements[1] + measurements[2]
incrs = 0
for i in range(3, len(measurements)):
    new_sum = old_sum - measurements[i-3] + measurements[i]
    if (new_sum > old_sum):
        incrs += 1
print(f"Increments: {incrs}") 

