

a, b = map(int, input().split())

arr = [[1] * a for _ in range(b)]

N = int(input())
cut = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
max = 0
for i in range(N):
    if cut[i][0] == 0:
        for j in range(a):

            arr[cut[i][1]][j] = 3

    if cut[i][0] == 1:
        for k in range(b):
            arr[k][arr[i][1]] = 2

t = 0
for y in range(b):
    if arr[y][t] == 3:
        if cnt > max:
            max = cnt
            cnt = 0
        for z in range(a):
            cnt += 1
            if arr[y][z] == 2:
                break

    for x in range(a):
       if arr[y][x] == 2:
           cnt += 1
           break
