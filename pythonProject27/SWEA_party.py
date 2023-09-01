
# 종강 파티

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

one = 10000000
six = 100000000

for i in range(M):
    one = min(one, arr[i][1])
    six = min(six, arr[i][0])

if one * 6 < six:
    print(min * N)
else:
    buy = N // 6
    N %= 6
    if N * one > six:
        buy += 1
        print(buy * six)
    else:
        print(buy * six + one * N)
