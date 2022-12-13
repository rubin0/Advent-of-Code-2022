from collections import deque
from collections import defaultdict

with open("input12.txt") as f:
    s = f.read().strip()

dirs = [(0,1),(1,0),(0,-1),(-1,0)]

matrix = [list(x) for x in s.split("\n")]
columns = len(matrix)
rows = len(matrix[0])

start_x, start_y = [ (i,j) for i in range(columns) for j in range(rows) if matrix[i][j] == "S"][0]
destination_x, destination_y = [ (i,j) for i in range(columns) for j in range(rows) if matrix[i][j] == "E"][0]

matrix[start_x][start_y] = "a"
matrix[destination_x][destination_y] = "z"

matrix = [[ord(columns) - ord("a") for columns in rows] for rows in matrix]
print(matrix)

frontier = deque([(i, j) for i in range(columns) for j in range(rows) if matrix[i][j] == 0])
dst = defaultdict(lambda : 1000000)

for x,y in frontier:
    dst[x, y] = 0

ans = 100000
while len(frontier) > 0:
    cx, cy = frontier.popleft()

    if(cx, cy) == (destination_x, destination_y):
        ans = dst[destination_x, destination_y]
        print(ans)
        break

    for dx, dy in dirs:
        nx, ny = cx + dx, cy + dy
        if nx in range(columns) and ny in range(rows):
            if matrix[cx][cy] >= matrix[nx][ny] -1:
                ndst = dst[cx,cy] + 1
                if ndst < dst[nx,ny]:
                    frontier.append((nx,ny))
                    dst[nx,ny] = ndst
