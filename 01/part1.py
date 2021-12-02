with open("input.txt") as file:
    prior_line = None 
    increments = 0
    for line in file:
        if prior_line != None and int(line) > prior_line:
            increments += 1
        prior_line = int(line)
    print(f"Got {increments} increments.")
