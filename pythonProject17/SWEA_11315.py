# SWEA 11315. 오목 판정

dx = [0, 1, 0, -1, 1, 1, -1, -1]
dy = [1, 0, -1, 0, 1, -1, 1, -1]

def ch():
    Power = 5
    result = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for w in range(8):
                    cnt = 1
                    for p in range(1, Power):
                        nx = i + p * dx[w]
                        ny = j + p * dy[w]
                        if 0 <= nx < N and 0 <= ny < N:
                            if arr[nx][ny] == 'o':
                                cnt += 1

                            else:
                                cnt = 1
                    if cnt == 5:
                        result = 1

    if result == 0:
        print(f'#{tc} NO')

    elif result == 1:
        print(f'#{tc} YES')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [input() for _ in range(N)]
    ch()



