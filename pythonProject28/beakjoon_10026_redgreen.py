import copy
# 적록 색약

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N = int(input())
arr = [list(input()) for _ in range(N)]
arr2 = copy.deepcopy(arr)
for i in range(N):
    for j in range(N):
        if arr2[i][j] == 'G':
            arr2[i][j] = 'R'

spa1 = [[0] * N for _ in range(N)]
spa2 = [[0] * N for _ in range(N)]

def bfs(x, y, spa1):
    q1 = []
    q1.append((x, y))
    spa1[x][y] = 1
    while q1:
        cx, cy = q1.pop(0)
        for w in range(4):
            nx = cx + dx[w]
            ny = cy + dy[w]
            if 0 <= nx < N and 0 <= ny < N:
                if spa1[nx][ny] == 0 and arr[cx][cy] == arr[nx][ny]:
                    q1.append((nx, ny))
                    spa1[nx][ny] = 1

def bfs2(x, y, spa2):
    q2 = []
    q2.append((x, y))
    spa2[x][y] = 1
    while q2:
        cx, cy = q2.pop(0)
        for w in range(4):
            nx = cx + dx[w]
            ny = cy + dy[w]
            if 0 <= nx < N and 0 <= ny < N:
                if spa2[nx][ny] == 0 and arr2[cx][cy] == arr2[nx][ny]:
                    q2.append((nx, ny))
                    spa2[nx][ny] = 1

cnt1 = 0
cnt2 = 0
for i in range(N):
    for j in range(N):
        if spa1[i][j] == 0:
            bfs(i, j, spa1)
            cnt1 += 1
        if spa2[i][j] == 0:
            bfs2(i, j, spa2)
            cnt2 += 1

print(cnt1, cnt2)