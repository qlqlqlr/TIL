
N, M = map(int, input().split())
K = int(input())
arr = [list(input()) for _ in range(N)]
directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == '@':
            for dy, dx in directions:
                for k in range(1, K + 1):
                    ny, nx = i + (k * dy), j + (k * dx)
                    if 0 <= ny < N and 0 <= nx < M:
                        if arr[ny][nx] == '_':
                            arr[ny][nx] = '%'
                        if arr[ny][nx] == '#':
                            break

            arr[i][j] = '%'

for row in arr:
    print(*row, sep = '')