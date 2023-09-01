# 솔빙클럽 bfs 트레이닝  최소 환승

from collections import deque
def bfs(S, G, arr):
    result = 0
    visited = [0] * (N +1)
    d = deque()
    d.append([S, 0])
    visited[S] = 1
    result = 100
    while d:
        v, dis = d.popleft()

        for i in range(1, N + 1):
            if visited[i] == 0 and arr[v][i] == 1:
                d.append([i, dis + 1])
                visited[i] = 1
                if visited[i] == 1 and i == G:
                    result = dis + 1


                    return result


    return -1





N, M = map(int, input().split())

arr = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

T = int(input())
for i in range(1, N+1):
    arr[i][T] = 0
    arr[T][i] = 0

print(bfs(1, N, arr))
