base_numbers = []
with open("input.txt") as file:
    for line in file:
        base_numbers.append(line.strip())

def b_to_d(number):
    dec = 0;
    for i, bit in enumerate(number[::-1]):
        dec += int(bit) << i
    return dec
print(f"01010: {b_to_d('01010')}")

def ref_filter(numbers, popular, cur_index=0):
    if len(numbers) == 1:
        return b_to_d(numbers[0])

    sum = 0
    for number in numbers:
        sum += int(number[cur_index])

    keep = (sum >= len(numbers) / 2) ^ popular
    new_numbers = [];
    for number in numbers:
        if int(number[cur_index]) == keep:
            new_numbers.append(number)

    return ref_filter(new_numbers, popular, cur_index + 1)

o2 = ref_filter(base_numbers, True)
co2 = ref_filter(base_numbers, False)

print(f"o2 {o2} co2 {co2} mult {o2 * co2}")
