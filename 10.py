with open('input10.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

    strength_cycles = [1, 1]
    register = 1
    cycle = 1

    for line in lines:
        line = line.strip()

        splitted = line.split(" ")
        command = splitted[0]

        if command == "addx":
            value = int(splitted[1])
            register = strength_cycles[cycle]
            strength_cycles.insert(cycle, register)
            strength_cycles.insert(cycle+1, register)
            strength_cycles.insert(cycle+2, register + value)
            cycle += 2
        else:
            register = strength_cycles[cycle]
            strength_cycles.insert(cycle, register)
            cycle += 1

print(sum(strength_cycles[x]*x for x in range(20, 221, 40)))
