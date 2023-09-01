
def check():
    maxi1 = 0
    maxi2 = 0
    tmp1 = 0
    tmp2 = 0
    for i in range(N):
        tmp1 = arr[i][0] + arr[i][2]
        tmp2 = arr[i][1] + arr[i][3]

        if maxi1 < tmp1:
            maxi1 = tmp1

        if maxi2 < tmp2:
            maxi2 = tmp2

    return maxi1, maxi2

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

x, y = check()
space = [[0] * (x + 1) for _ in range(y + 1)]
result = [0] * N
for i in range(N):
    cnt = 0
    minus = 0
    for x in range(arr[i][0], arr[i][0] + arr[i][2]):
        for y in range(arr[i][1], arr[i][1] + arr[i][3]):
            if space[y][x] == 0:
                space[y][x] = i + 1
                cnt += 1

            else:
                for k in range(1, i + 1):
                    if space[y][x] == k:
                        result[k - 1] -= 1


                space[y][x] = i + 1
                cnt += 1



    result[i] = cnt

for z in range(N):
    print(result[z])

