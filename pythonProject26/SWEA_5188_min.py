
# 5188. 최소합
def dfs(x, y):
    cnt = 0
    mini = 1000
    stack = []
    visited = [([0] * N) for _ in range(N)]
    visited[x][y] = 1
    visited[N-1][N-1] = 2
    cnt = arr[x][y]
    stack.append((x, y))
    while True:
        if x == N -1 and y == N - 1:
            if cnt < mini:
                mini = cnt

        for w in range(2):
            nx = x + dx[w]
            ny = y + dy[w]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] != 1 :
                    if nx == N -1 and ny == N -1:
                        x, y = nx, ny
                        cnt += arr[x][y]
                        visited[x][y] = 2
                        break
                    stack.append((nx, ny))
                    x, y = nx, ny
                    cnt += arr[x][y]
                    visited[x][y] = 1
                    break

        else:
            cnt -= arr[x][y]
            if stack:
                x, y = stack.pop()

            else:
                break
    return mini


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 1]
    dy = [1, 0]
    x, y = 0, 0

    print(f'#{tc} {dfs(x, y)}')





