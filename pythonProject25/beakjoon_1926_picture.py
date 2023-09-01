direction = [[0, 1],
             [1, 0],
             [-1, 0],
             [0, -1]
             ]
n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
ea = 0
maxi = 0

# 그림   DFS, BFS
def bfs(y, x):
    global ea
    global maxi
    q = []
    q.append((y, x))
    arr[y][x] = 0
    cnt = 1
    while q:
        cy, cx = q.pop(0)
        for dy, dx in direction:
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < n and 0 <= nx < m:
                if arr[ny][nx] == 1:
                    q.append((ny, nx))
                    arr[ny][nx] = 0
                    cnt += 1
    if cnt != 0:
        ea += 1
    if cnt > maxi:
        maxi = cnt


for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            bfs(i, j)

print(ea)
print(maxi)

