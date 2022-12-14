from collections import defaultdict

with open("input14.txt") as f:
    s = f.read().strip().split("\n")

walls = [s.split(" -> ") for s in s]
obstacles = defaultdict(lambda: defaultdict(lambda: False))
sand = defaultdict(lambda: defaultdict(lambda: False))

lowest_y = 0
highest_y = 1000000
lowest_x = 10000
highest_x = 0
for wall in walls:
    wall = [(int(w.split(",")[0]), int(w.split(",")[1])) for w in wall]

    for i in range(len(wall)-1):
        (x, y) = wall[i]
        (w, z) = wall[i+1]

        obstacles[x][y] = True
        obstacles[w][z] = True

        diff = x-w

        if y > lowest_y:
            lowest_y = y

        if y < highest_y:
            highest_y = y

        if x > highest_x:
            highest_x = x

        if x < lowest_x:
            lowest_x = x

        value = 1
        if diff > 0:
            value = -1

        for i in range(abs(diff)):
            obstacles[x+(value * i)][y] = True

        diff = y-z

        value = 1
        if diff > 0:
            value = -1

        for i in range(abs(diff)):
            obstacles[x][y+(value * i)] = True

starting_point = (500, 0)
dir = [(0, 1), (-1, 1), (1, 1)]

position = [starting_point[0], starting_point[1]]

abyss = True
count = 0
while (abyss):
    position = [starting_point[0], starting_point[1]]
    dir_index = 0
    while (True):
        next = (position[0] + dir[dir_index][0],
                position[1] + dir[dir_index][1])

        if sand[starting_point[0]][starting_point[1]]:  
            abyss = False
            break

        if obstacles[next[0]][next[1]] or sand[next[0]][next[1]] or next[1] == lowest_y+2:
            dir_index += 1
            if dir_index >= len(dir):
                dir_index = 0
                break
            else:
                continue
        else:
            dir_index = 0

        if sand[starting_point[0]][starting_point[1]]:
            abyss = False
            break

        position = next

    if abyss:
        count += 1
        sand[position[0]][position[1]] = True


print(count)
print("")
for j in range(0, lowest_y+1+5):
    print(str(j).ljust(3), end="")
    for i in range(lowest_x-30, highest_x+1+30):
        char = "."
        if obstacles[i][j] or j == lowest_y+2:
            char = "#"
        if sand[i][j]:
            char = "O"
        if j == 0 and i == 500:
            char = "X"
        print(char, end="")
    print("")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
