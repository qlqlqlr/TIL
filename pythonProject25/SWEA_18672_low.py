
N, M = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
sum = 0
high = 0
low = 0

while True:
    if sum >= M or high == N:
        sum -= arr[low]
        low += 1

    elif sum < M:
        sum += arr[high]
        high += 1

    if sum == M:
        cnt += 1


    if low == N:
        break
print(cnt)
