from collections import deque
# 토마토
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
sta = deque()
ban = 0

def bfs(sta):
    while sta:
        cx, cy = sta.popleft()
        for w in range(4):
            nx = cx + dx[w]
            ny = cy + dy[w]
            if 0 <= nx < M and 0 <= ny < N and arr[nx][ny] == 0:
                arr[nx][ny] = arr[cx][cy] + 1
                sta.append((nx, ny))

maxi = 0
result = 0

for i in range(M):
    for j in range(N):
        if arr[i][j] == 1:
            sta.append((i, j))

bfs(sta)

for k in range(M):
    for l in range(N):
        if arr[k][l] == 0:
            result = -1
            print(result)
            exit(0)

for k in range(M):
    for l in range(N):
        if arr[k][l] > maxi:
            maxi = arr[k][l]
print(maxi - 1)
