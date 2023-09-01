

ydir = [-1, 1, 0, 0]
xdir = [0, 0, -1, 1]
T = int(input())
for tc in range(1, T+1):
    N, P = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            # 일단 현재위치 누적
            cnt = MAP[i][j]
            # 4방향
            for d in range(4):
                # k칸 만큼 p까지 터져나감
                for k in range(1, P + 1):
                    ny = i + ydir[d] * k
                    nx = j + xdir[d] * k
                    # 범위체크
                    if ny < 0 or nx < 0 or ny >= N or nx >= N:
                        continue
                    else:
                        cnt += MAP[ny][nx]
            ans = max(ans, cnt)
    print(f'#{tc} {ans}')