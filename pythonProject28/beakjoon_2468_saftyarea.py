import copy
# 안전 영역

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y, arr2):
    q = []
    q.append((x, y))
    arr2[x][y] = 0
    while q:
        cx, cy = q.pop(0)
        for w in range(4):
            nx = cx + dx[w]
            ny = cy + dy[w]
            if 0 <= nx < N and 0 <= ny < N:
                if arr2[nx][ny] != 0:
                    q.append((nx, ny))
                    arr2[nx][ny] = 0
def ch():
    global rai
    maxi = 0
    arr2 = copy.deepcopy(arr)
    rai = 0
    while True:
        cnt = 0
        arr2 = copy.deepcopy(arr)
        rai_cnt = 0
        for i in range(N):
            for j in range(N):
                if arr2[i][j] <= rai:
                    arr2[i][j] = 0
                    rai_cnt += 1
        if rai_cnt >= (N * N - 1):
            break

        for k in range(N):
            for l in range(N):
                if arr2[k][l] != 0:
                    bfs(k, l, arr2)
                    cnt += 1

        if cnt > maxi:
            maxi = cnt
        rai += 1
    print(maxi)

ch()