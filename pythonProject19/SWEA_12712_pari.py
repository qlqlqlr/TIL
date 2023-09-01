

dx1 = [0, 1, 0, -1]
dy1 = [1, 0, -1, 0]

dx2 = [1, 1, -1, -1]
dy2 = [-1, 1, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    maxi = 0
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            cnt1 = arr[i][j]
            cnt2 = arr[i][j]
            for w in range(4):
                for pp in range(1, M):
                    nx = i + pp * dx1[w]
                    ny = j + pp * dy1[w]
                    nx2 = i + pp * dx2[w]
                    ny2 = j + pp * dy2[w]
                    if 0 <= nx < N and 0 <= ny < N:
                        cnt1 += arr[nx][ny]

                    if 0 <= nx2 < N and 0 <= ny2 < N:
                        cnt2 += arr[nx2][ny2]

            if cnt1 > maxi:
                maxi = cnt1
            if cnt2 > maxi:
                maxi = cnt2

    print(f'#{tc} {maxi}')