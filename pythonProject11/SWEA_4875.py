# SWEA 4875. 미로

def maze(arr, x, y, N):
    stack = []
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    arr[x][y] = 1
    stack.append([x, y])
    for k in range(4):
        nx, ny = x + dx[k], y + dx[k]
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
            x = nx
            y = ny
            arr[x][y] = 1
            stack.append([x, y])
    else:
        pp =



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    x, y = 0, 0
    result = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
               x, y = i, j

    result = maze(arr, x, y, N)
    print(f'#{tc} {result}')