# 농작물 수확하기

dx = [0,0]
dy = [-1, 1]


def ch():
    x, y = 0, N // 2
    P = N // 2  # 3
    cnt = 0
    for i in range(N // 2 + 1):
        cnt += int(arr[i][y])
        if i != 0:
            for w in range(2):
                for pw in range(1, i + 1):
                    ny = y + pw * dy[w]
                    if 0 <= ny < N:
                        cnt += int(arr[i][ny])

    for i in range(N // 2 + 1, N):
        cnt += int(arr[i][y])
        if i != N - 1:
            for w in range(2):
                for pw in range(N - i - 1 , 0, -1):
                    ny = y + pw * dy[w]
                    if 0 <= ny < N:
                        cnt += int(arr[i][ny])

    return cnt

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]





    print(f'#{tc} {ch()}')
