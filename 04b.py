with open('input4.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

    score = 0
    for line in lines:
        line = line.strip()

        if line:
            values = line.split(",")

            left_values = [int(i) for i in values[0].split("-")]
            right_values = [int(i) for i in values[1].split("-")]

            left_set = set(range(left_values[0], (left_values[1]+1)))
            right_set = set(range(right_values[0], (right_values[1]+1)))

            intersection = set.intersection(left_set, right_set)

            if intersection:
                score += 1

        else:
            break

    print(score)
