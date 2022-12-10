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

    offset = 0
    for x in range(240):
        pixel = strength_cycles[x + 1]
        drawing_range = [pixel-1, pixel, pixel+1]
        char = '.'
        if x - offset in drawing_range:
            char = '#'

        print(char, end="")
        if x in range(39, 241, 40):
            offset = x + 1
            print()
