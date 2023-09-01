from collections import deque
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y, arr):
    d = deque()
    d.append([x, y, 0])  # Also keep track of the distance

    while d:
        x, y, distance = d.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] == '0':
                    d.append([nx, ny, distance + 1])
                    arr[nx][ny] += '1'
                elif arr[nx][ny] == '3':
                    return distance  # Return the distance when destination is found

    return 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    cnt = 0
    x, y = 0, 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                x, y = i, j
                cnt += 1
                break

        if cnt == 1:
            break

    result = bfs(x, y, arr)
    print(f'#{tc} {result}')