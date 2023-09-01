
T = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


for tc in range(1, T + 1):
    N, P = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxi = 0
    for i in range(N):
        for j in range(N):

            s = arr[i][j]
            for k in range(4):
                for p in range(1, P + 1):
                    nx = i + p * dx[k]
                    ny = j + p * dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        s += arr[nx][ny]

            if maxi < s:
                maxi = s

    print(f'#{tc} {maxi}')