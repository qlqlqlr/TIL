from collections import deque
# SWEA 5102. 노드의 거리

def bfs(n, G, arr):
    d = deque()
    visited = [0] * (V + 1)
    visited[n] = 1
    d.append([n, 0])

    while d:
        v, distance = d.popleft()
        for i in range(1, V + 1):
            if arr[v][i] and visited[i] == 0:
                if i == G:
                    return distance + 1
                d.append([i, distance + 1])
                visited[i] = 1
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[0] * (V + 1) for _ in range(V + 1)]
    for i in range(E):
        a, b = map(int, input().split())
        arr[a][b] = 1
        arr[b][a] = 1
    S, G = map(int, input().split())
    print(f'#{tc} {bfs(S, G, arr)}')
