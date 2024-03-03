from collections import defaultdict
import re


def manhattan(sx, sy, bx, by):
    return abs(sx - bx) + abs(sy - by)


with open("input15b.txt") as f:
    coord = [re.findall(r'[-]?[0-9]+', x)
             for x in f.read().strip().split("\n")]

flattened = [int(val) for sublist in coord for val in sublist]

minimum = min(flattened)
maximum = max(flattened)

m = defaultdict(lambda: defaultdict(lambda: False))

for c in coord:
    sx, sy, bx, by = map(int, c)

    m[sx][sy] = True

    d = manhattan(sx, sy, bx, by)

    for i in range(d+1):
        for j in range(d-i+1):
            m[sx + i][sy + j] = True
            m[sx - i][sy + j] = True
            m[sx + i][sy - j] = True
            m[sx - i][sy - j] = True

    print("")
    for j in range(minimum-10, maximum+10):
        print(str(j).ljust(3), end="")
        for i in range(minimum-10, maximum+10):
            char = "."
            if m[i][j]:
                char = "#"
            if sx == i and sy == j:
                char = "S"
            if bx == i and by == j:
                char = "B"
            print(char, end="")
        print("")

    print()
