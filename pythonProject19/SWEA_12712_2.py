# 파리퇴치3 강사님

def spray(y, x):
    # 상하좌우 4, 대각선 4
    dir = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
    s1 = s2 = arr[y][x]
    for i in range(4):   # 상하 좌우
        for j in range(1, M):
            dy = y + dir[1][0] * j
            dx = x + dir[1][1] * j
            if 0 <= dy < N and 0 <= dx < N:
                s1 += arr[dy][dx]
    for i in range(4, 8):   # 대각선
        for j in range(1, M):
            dy = y + dir[1][0] * j
            dx = x + dir[1][1] * j
            if 0 <= dy < N and 0 <= dx < N:
                s2 += arr[dy][dx]

    return max(s1,s2)

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_value = 0
    for i in range(N):
        for j in range(N):
            s = spray(i, j)
            if s > max_value:
                max_value = s

    print(f'#{tc} {max_value}')

