
# 2178. 미로 탐색

N, M = map(int, input().split())

arr = [input() for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(x, y):
    q = []
    visited = [[0] * M for _ in range(N)]
    q.append((x, y))
    visited[x][y] = 1
    while q:
        cx, cy = q.pop(0)
        for w in range(4):
            nx = cx + dx[w]
            ny = cy + dy[w]
            if nx == 0 and ny == 0:
                continue
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == '1' and visited[nx][ny] == 0:

                    visited[nx][ny] = visited[cx][cy] + 1
                    q.append((nx, ny))


    print(visited[N - 1][M - 1])

bfs(0, 0)