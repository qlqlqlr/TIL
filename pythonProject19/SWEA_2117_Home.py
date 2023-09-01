# SWEA 모의 SW 역량테스트 홈 방범 서비스

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # M 집 당 비용 지불 액수
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(1, N):
        k = i * i + (i - 1) * (i - 1)
        p = i + (i - 1)

        for x in range(N):
            for y in range(N):
                if i == 1:
                    if arr[x][y] == 1:
                        cnt = 1
                else:
                    cnt = 0
                    for z in range(1, i):
                        nx = x + z
                        nx2 = x - z

                        start = y - i + 1
                        end = y + i - 1
                        for w in range(start, end + 1):
                            if arr[n][w] == 1:
                                cnt +=1
