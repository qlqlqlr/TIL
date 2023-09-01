# BFS 트레이닝    출근하기 편한 지역
from collections import deque
def bfs(S, G, arr):
    result = 0
    visited = [0] * (N +1)
    d = deque()
    d.append([S, 0])
    visited[S] = 1
    result += 1

    while d:
        v, dis = d.popleft()

        for i in range(1, N + 1):
            if visited[i] == 0 and arr[v][i] == 1 and dis < G:
                d.append([i, dis + 1])
                visited[i] = 1
                result += 1

    print(result)
    return





N, M = map(int, input().split())

arr = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

S, G = map(int, input().split())
bfs(S, G, arr)
