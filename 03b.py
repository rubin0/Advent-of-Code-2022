with open('input3.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

    score = 0
    rucksacks = []
    for line in lines:
        line = line.strip()

        if line:
            rucksacks.append(set(line))

            if len(rucksacks) == 3:
                intersection = set.intersection(*rucksacks).pop()

                if intersection.islower():
                    score += ord(intersection) - 96
                else:
                    score += ord(intersection) - 38
                rucksacks = []

        else:
            break

    print(score)
