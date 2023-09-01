
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    maxarea = 0
    cnt = 0

    for y in range(N):
        for x in range(N):
            cur = MAP[y][x]    # 온쪽 위의 좌표값
            #현재위치에서 오른쪽 아래로 탐색
            for ny in range(y, N):
                for nx in range(x, N):
                    if MAP[ny][nx] == cur:
                        area = (ny - y + 1) * (nx - x + 1)

                        if area > maxarea:
                            maxarea = area
                            cnt = 1
                        elif area == maxarea:
                            cnt += 1

    print(f'#{tc} {cnt}')