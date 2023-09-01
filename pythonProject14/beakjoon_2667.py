
direction = [[0, 1],
             [1, 0],
             [-1, 0],
             [0, -1]
             ]
def bfs(arr, y, x, apt):
    global cnt
    queue = []
    queue.append((y, x))
    arr[y][x] = 0
    dan = 1
    while queue:
        cy, cx = queue.pop(0)
        for dy, dx in direction:
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < N and 0 <= nx < N:
                if arr[ny][nx] == 1:
                    queue.append((ny, nx))
                    arr[ny][nx] = 0
                    dan += 1
    apt.append(dan)
    cnt += 1


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

cnt = 0
apt = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            bfs(arr, i, j, apt)

print(cnt)
apt.sort()
for i in range(len(apt)):
    print(apt[i])