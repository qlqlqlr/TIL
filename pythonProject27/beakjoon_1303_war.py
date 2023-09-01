
# 전쟁 - 전투

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y, c):
    cnt = 0
    q = []
    q.append((x, y))
    adj[x][y] = 0
    while q:
        cx, cy = q.pop(0)
        cnt += 1
        for w in range(4):
            nx = cx + dx[w]
            ny = cy + dy[w]
            if 0 <= nx < M and 0 <= ny < N:
                if adj[nx][ny] == c:
                    q.append((nx, ny))
                    adj[nx][ny] = 0

    return (cnt * cnt)

N, M = map(int, input().split())
arr = [input() for _ in range(M)]
adj = [[0] * N for _ in range(M)]

white = 0
blue = 0
for i in range(M):
    for j in range(N):
        if arr[i][j] == 'W':
            adj[i][j] = 1
        else:
            adj[i][j] = 2


for i in range(M):
    for j in range(N):
        if adj[i][j] == 1:
            white += bfs(i, j, 1)

        elif adj[i][j] == 2:
            blue += bfs(i, j, 2)

print(white, blue)