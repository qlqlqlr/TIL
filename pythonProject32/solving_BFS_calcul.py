from collections import deque
# 솔빙클럽 swea 연산 BFS

def bfs(s, g):
    q = deque()
    visited = [0] * 1000001
    q.append(s)
    visited[s] = 1

    while q:
        cn = q.popleft()
        cl1 = cn + 1
        cl2 = cn - 1
        cl3 = cn * 2
        cl4 = cn - 10
        if cl1 == g or cl2 == g or cl3 == g or cl4 == g:
            return visited[cn]
        if 0 < cl1 < 1000001:
            if visited[cl1] == 0:
                q.append(cl1)
                visited[cl1] = visited[cn] + 1
        if 0 < cl2 < 1000001:
            if visited[cl2] == 0:
                q.append(cl2)
                visited[cl2] = visited[cn] + 1
        if 0 < cl3 < 1000001:
            if visited[cl3] == 0:
                q.append(cl3)
                visited[cl3] = visited[cn] + 1
        if 0 < cl4 < 1000001:
            if visited[cl4] == 0:
                q.append(cl4)
                visited[cl4] = visited[cn] + 1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    print(f'#{tc} {bfs(N, M)}')


