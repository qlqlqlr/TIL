from collections import deque
direction = [[0, 1],
             [1, 0],
             [-1, 0],
             [0, -1]
             ]
T = int(input())

def start():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                return i, j


def bfs(y, x):
    d = deque()
    d.append([y, x])
    visited[y][x] = 1
    while d:
        v1, v2 = d.popleft()
        if arr[v1][v2] == '3':
            return visited[v1][v2] - 2
        for dy, dx in direction:
            ny = v1 + dy
            nx = v2 + dx
            if 0 <= ny < N and 0 <= nx < N:
                if arr[ny][nx] != '1' and visited[ny][nx] == 0:
                    visited[ny][nx] = visited[v1][v2] + 1
                    d.append([ny, nx])

    return 0




for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    a, b = start()
    print(f'#{tc} {bfs(a, b)}')
