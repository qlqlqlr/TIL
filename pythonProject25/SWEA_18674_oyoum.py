
N = int(input())
arr = list(map(int, input().split()))
min = 10e16
x, y = 0, 0
for i in range(N):
    if arr[i] >= 0:
        continue
    else:
        for j in range(N):
            sum = 0
            if arr[j] < 0:
                continue
            else:
                sum = abs(arr[i] + arr[j])
                if sum < min:
                    min = sum

                    x, y = arr[i], arr[j]
                if sum == 0:
                    if abs(x) + abs(y) < abs(arr[i]) + abs(arr[j]):

                        x, y = arr[i], arr[j]

if x < y:
    print(x, y)
else:
    print(y, x)