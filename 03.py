with open('input3.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

    score = 0
    for line in lines:
        line = line.strip()

        if line:
            lenght = len(line)
            first_comp = sorted(line[0:int(lenght/2)])
            second_comp = sorted(line[int(lenght/2):lenght])

            intersection = list(set(first_comp) & set(second_comp))[0]

            if intersection.islower():
                score += ord(intersection)-96
            else:
                score += ord(intersection)-38
        else:
            break

    print(score)
