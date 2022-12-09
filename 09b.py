import math


def serialize(list):
    return str(list[0])+","+str(list[1])


with open('input9.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

    knots_number = 2
    knots = []
    for i in range(knots_number):
        starting_point = [0, 0]
        knots.append(starting_point)

    last_knot_position = [serialize(knots[-1])]

    for line in lines:
        line = line.strip()

        dir, n = line.split()
        n = int(n)

        for i in range(n):
            match dir:
                case "L":
                    knots[0][0] += -1
                case "R":
                    knots[0][0] += 1
                case "U":
                    knots[0][1] += -1
                case "D":
                    knots[0][1] += 1

            for j in range(1, knots_number):
                distance = math.dist(knots[j-1], knots[j])

                if distance > math.sqrt(2):
                    diff = [knots[j-1][0] - knots[j][0],
                            knots[j-1][1] - knots[j][1]]

                    if diff[0] != 0:
                        diff[0] /= abs(diff[0])

                    if diff[1] != 0:
                        diff[1] /= abs(diff[1])

                    knots[j][0] += int(diff[0])
                    knots[j][1] += int(diff[1])

                    if j == knots_number - 1:
                        last_knot_position.append(serialize(knots[j]))

    print(len(set(last_knot_position)))
