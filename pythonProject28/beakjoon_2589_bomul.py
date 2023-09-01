from collections import deque
import copy
# 보물섬

X, Y = map(int, input().split())
arr = [list(input()) for _ in range(X)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
maxi = 0
def bfs(x, y):
    global maxi
    arr2 = copy.deepcopy(arr)
    q = deque()
    q.append((x, y))
    arr2[x][y] = '0'
    while q:
        cx, cy = q.popleft()
        for w in range(4):
            nx = cx + dx[w]
            ny = cy + dy[w]
            if 0 <= nx < X and 0 <= ny < Y and arr2[nx][ny] == 'L':
                q.append((nx, ny))
                arr2[nx][ny] = str(int(arr2[cx][cy]) + 1)


    for i in range(X):
        for j in range(Y):
            if arr2[i][j].isdigit():
                if int(arr2[i][j]) > maxi:
                    maxi = int(arr2[i][j])



for i in range(X):
    for j in range(Y):
        if arr[i][j] == 'L':
            bfs(i, j)

print(maxi)