
# 스타트 링크 BFS

F, S, G, U, D = map(int, input().split())

dir = [U, -1 *D]

def bfs(n):
    q = []
    visited = [0] * (F + 1)
    visited[0] = 1
    visited[n] = 1
    q.append(n)
    while q:
        v = q.pop(0)
        if v == G:
            return visited[v] - 1
        for w in range(2):
            nv = v + dir[w]
            if 0 < nv < F + 1:
                if visited[nv] == 0:
                    q.append(nv)
                    visited[nv] = visited[v] + 1

    return 'use the stairs'


print(bfs(S))