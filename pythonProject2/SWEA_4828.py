T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_v = 0
    min_v = 0
    max_v = max(arr)
    min_v = min(arr)

    ans = max_v - min_v

    print(f'#{tc} {ans}')