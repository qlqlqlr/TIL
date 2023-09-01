

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    c = [int(input()) for _ in range(P)]

    cnt = [0] * P

    for i in range(N):
        s = arr[i][0] - 1
        g = arr[i][1] - 1
        for j in range(s, g + 1):
            cnt[j] += 1

    print('#', end = '')
    print(tc, end = ' ')
    for k in range(P):
        print(cnt[k], end = ' ')