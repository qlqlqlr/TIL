# 3499 퍼펙트 셔플

def shuffle(arr, N):
    n = N // 2
    if n == 0:
        print(f'#{tc}', *arr)

    if N % 2 == 0:
        dek1 = arr[: n]
        dek2 = arr[n:]
        result = []
        for i in range(n):
            result.append(dek1[i])
            result.append(dek2[i])

        print(f'#{tc}', *result)

    elif N % 2 == 1:
        dek1 = arr[: n+1]
        dek2 = arr[n+1:]
        result = []
        for i in range(n):
            result.append(dek1[i])
            result.append(dek2[i])

        result.append(dek1[n])

        print(f'#{tc}', *result)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(input().split())

    shuffle(arr, N)