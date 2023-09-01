
# 쉬운 최단거리

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    res = [[0] * m for _ in range(n)]
    q = []
    q.append((x, y))
    arr[x][y] = 0
    while q:
        cx, cy = q.pop(0)
        for w in range(4):
            nx = cx + dx[w]
            ny = cy + dy[w]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1:
                    q.append((nx, ny))
                    res[nx][ny] = res[cx][cy] + 1
                    arr[nx][ny] = 0

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                res[i][j] = -1


    for i in range(len(res)):
        print(*res[i])
    return

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]



for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            bfs(i, j)
