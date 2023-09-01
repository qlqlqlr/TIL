# 솔빙클럽 트리인접행렬 BFS
# 트리 자료구조에서 너비 우선 탐색법으로 각 노드를 탐색해주세요.
#
# 시작 지점 부터, 노드에 방문할 때마다 값을 출력 해주세요.
#
# 출발지점은 입력으로 주어 집니다.
#
# 한번 방문 했던 노드는 방문할 수 없습니다.
#
# 트리 자료구조는 인접행렬로 하드코딩 해주세요.
from collections import deque

def bfs(arr, k):
    d = deque()
    visited = [False] * len(arr)
    d.append(k)
    visited[k] = True

    while d:
        v = d.popleft()
        print(v, end = ' ')
        for i in range(len(arr)):
            if not visited[i] and arr[v][i]:
                d.append(i)
                visited[i] = True




arr = [[0, 1, 0, 0, 1, 0],
       [0, 0, 1, 0, 0, 1],
       [0, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0]
       ]

k = int(input())
bfs(arr, k)