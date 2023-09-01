
T = int(input())

direction = [[0, 1],
             [1, 0],
             [-1, 0],
             [0, -1]
             ]
def bfs(arr, y, x):
    global cnt
    queue = []
    queue.append((y, x))
    arr[y][x] = 0
    while queue:
        cy, cx = queue.pop(0)
        for dy, dx in direction:
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < N and 0 <= nx < M:
                if arr[ny][nx] == 1:
                    queue.append((ny, nx))
                    arr[ny][nx] = 0

    cnt += 1



for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    for k in range(K):
        y, x = map(int, input().split())
        arr[x][y] = 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                bfs(arr, i, j)

    print(cnt)