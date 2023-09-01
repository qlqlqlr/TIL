# 백준 13300 방배정 IM 대비

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

mcntarr = [0] * 7
wcntarr = [0] * 7
for i in range(N):
    if arr[i][0] == 1:
        mcntarr[arr[i][1]] += 1
    else:
        wcntarr[arr[i][1]] += 1

result = 0
for j in range(7):
    if mcntarr[j] != 0:
        if mcntarr[j] % K == 0:
            result += mcntarr[j] // K

        else:
            result += mcntarr[j] // K + 1

    if wcntarr[j] != 0:
        if wcntarr[j] % K == 0:
            result += wcntarr[j] // K

        else:
            result += wcntarr[j] // K + 1


print(result)