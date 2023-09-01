from collections import deque
N, M, V = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
adj = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(M):
    x, y = arr[i][0], arr[i][1]
    adj[x][y] = 1
    adj[y][x] = 1


def dfs(n, N, adj):
    stack = []
    visited = [0] * (N + 1)
    visited[n] = 1
    print(n, end = ' ')
    while True:
        for w in range(1, N + 1):
            if adj[n][w] == 1 and visited[w] == 0:
                stack.append(n)
                n = w
                print(n, end = ' ')
                visited[n] = 1
                break
        else:
            if stack:
                n = stack.pop()
            else:
                break
    print()
    return

def bfs(adj, n, N):
    d = deque()
    visited = [False] * (N + 1)
    d.append(n)
    visited[n] = True

    while d:
        v = d.popleft()
        print(v, end = ' ')
        for i in range(1, N + 1):
            if not visited[i] and adj[v][i]:
                d.append(i)
                visited[i] = True



dfs(V, N, adj)
bfs(adj, V, N)

