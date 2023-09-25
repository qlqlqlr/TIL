
T = int(input())

def shoot(level, cnt):
    # print(cnt, end = ' ')
    if level == N:
        result.append(cnt)
        return

    for i in range(N):
        if visited[i] == 1:
            continue
        cnt += arr[level][i]
        visited[i] = 1
        shoot(level + 1, cnt)
        visited[i] = 0
        cnt -= arr[level][i]


for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = []
    visited = [0] * N
    level, cnt = 0, 0
    shoot(level, cnt)
    print(f'#{tc} {max(result)}')