T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    min_idx = 0
    max_idx = 0
    for i in range(1, N):
        if arr[min_idx] > arr[i]:
            min_idx = i

    for j in range(1, N):
        if arr[max_idx] <= arr[j]:
            max_idx = j


    ans = max_idx - min_idx
    if ans < 0:
        ans *= (-1)

    print(f'{tc} {ans}')