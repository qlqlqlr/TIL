from collections import deque

directions = [[-1, 2],
              [-2, 1],
              [-2, -1],
              [-1, -2],
              [1, -2],
              [2, -1],
              [1, 2],
              [2, 1]
              ]

def bfs(x, y, arr):
    d = deque()
    arr[x][y] = 1
    d.append([x, y, 0])
    while d:
        cy, cx, distance = d.popleft()
        for dx, dy in directions:
            nx = cx + dx
            ny = cy + dy
            if 0 <= ny < l and 0 <= nx < l:
                if arr[nx][ny] != 1:
                    if arr[nx][ny] == 2:
                        return distance + 1
                    d.append([nx, ny, distance + 1])
                    arr[nx][ny] = 1

    return 0

T = int(input())
for tc in range(T):
    l = int(input())
    arr = [[0] * l for _ in range(l)]
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    arr[x2][y2] = 2
    print(bfs(x1, y1, arr))


