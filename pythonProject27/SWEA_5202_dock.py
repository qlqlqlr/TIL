
# 화물 도크

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    arr.sort(key=lambda x: x[1])

    arr = [[0, 0]] + arr

    cnt = 0

    j = 0
    for i in range(1, N + 1):
        if arr[i][0] >= arr[j][1]:

            j = i
            cnt += 1
    print(f'#{tc} {cnt}')