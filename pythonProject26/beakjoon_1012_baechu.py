# 유기농 배추
def bfs(x, y, arr):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = []
    cnt = 0
    q.append((x, y))
    arr[x][y] = 0
    while q:
        cx, cy = q.pop(0)
        for w in range(4):
            nx = cx + dx[w]
            ny = cy + dy[w]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 1:
                    q.append((nx, ny))
                    arr[nx][ny] = 0
    cnt += 1
    return cnt

T = int(input())
for tc in range(1, T + 1):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    for i in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1


    result = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                bfs(i, j, arr)
                result += 1

    print(result)
