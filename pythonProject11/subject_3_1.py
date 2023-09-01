
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]
    cnt = 0
    for y in range(N):
        for x in range(N):
            high_fd = False
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < N and 0 <= nx < N:
                    if arr[y][x] <= arr[ny][nx]
                        high_fd = True
                        break

            if not high_fd:
                cnt += 1

    print(f'#{tc} {cnt}')