
T = int(input())

for tc in range(1, T + 1):
    N, W = map(int, input().split())
    arr = list(map(int, input().split()))
    sum = 0
    for i in range(W):
        sum += arr[i]
        maxi = sum
        x, y = 0, i

    for i in range(N - W):
        sum += arr[i + W]
        sum -= arr[i]
        if sum > maxi:
            maxi = sum
            x, y = i + 1, i + W

    print(f'#{tc} {x} {y} {maxi}')