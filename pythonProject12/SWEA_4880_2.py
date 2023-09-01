# 4880. 강사님 풀이

def win(x, y):
    if arr[x] == arr[y]: # 비긴 경우
        return x

    elif arr[x] - arr[y] == 1 or arr[x] - arr[y] == -2:
        return x

    else:
        return y

def group(start, end):
    if start == end:
        return start

    left = group(start, (start+end) // 2)     # 시작 부터 중간까지
    right = group((start+end) // 2 + 1, end)

    return win(left, right)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = group(0, N - 1) + 1