# 솔빙클럽 BFS 2

from collections import deque

def bfs(arr, k):
    d = deque()
    visited = [False] * len(arr)
    d.append(k)
    visited[k] = True

    while d:
        v = d.popleft()
        print(v)
        for i in range(len(arr)):
            if not visited[i] and arr[v][i]:
                d.append(i)
                visited[i] = True




arr = [[0, 0, 0, 0, 1, 0],
       [1, 0, 1, 0, 0, 1],
       [1, 0, 0, 1, 0, 0],
       [1, 1, 0, 0, 0, 0],
       [0, 1, 0, 1, 0, 1],
       [0, 0, 1, 1, 0, 0]]

k = int(input())
bfs(arr, k)