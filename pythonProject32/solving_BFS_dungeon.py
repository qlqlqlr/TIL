from collections import deque
# 솔빙클럽 코딩 던전 BFS

N, M, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(M)]
result = []
def bfs(now):
    q = deque()
    visited = [0] * N
    q.append(now)

    while q:
        cn = q.popleft()
        result.append(cn)
        for i in range(M):
            if arr[i][0] == cn and visited[arr[i][1]] == 0:
                visited[arr[i][1]] = arr[i][2] + visited[cn]
                if visited[arr[i][1]] <= K:
                    q.append(arr[i][1])

    result.pop(0)
    print(*result)

bfs(0)