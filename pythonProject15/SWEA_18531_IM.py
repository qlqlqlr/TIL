import math


def Radian():
    R = 0
    result = 0
    for i in range(N + 1):
        for j in range(N + 1):
            D = 0
            if arr[i][j] == 1:
                D = (i - x) ** 2 + (j - y) ** 2
                if D > R:
                    R = D
    result = math.sqrt(R)

    if result - int(result) > 0:
        result = int(result) + 1

    return int(result)

def point():
    for i in range(N + 1):
        for j in range(N + 1):
            if arr[i][j] == 2:
                return i, j


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N + 1)]

    x, y = point()

    print(f'#{tc} {Radian()}')

