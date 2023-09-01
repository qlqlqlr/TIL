
M, N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(K)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

space = [[0] * N for _ in range(M)]
cnt = 0
area = []
def bfs(x, y):
    q= []
    q.append((x, y))
    space[x][y] = 2
    are = 0
    while q:
        cx, cy = q.pop(0)
        are += 1
        for w in range(4):
            nx = cx + dx[w]
            ny = cy + dy[w]
            if 0 <= nx < M and 0 <= ny < N:
                if space[nx][ny] == 0:
                    q.append((nx, ny))
                    space[nx][ny] = 2


    return are

for i in range(K):
    for j in range(arr[i][0], arr[i][2]):
        for k in range(arr[i][1], arr[i][3]):
            space[M - k - 1][j] = 1

for i in range(M):
    for j in range(N):
        if space[i][j] == 0:
            area.append(bfs(i, j))
            cnt += 1

print(cnt)
area.sort()
print(*area)