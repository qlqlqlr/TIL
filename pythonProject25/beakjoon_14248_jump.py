# 점프점프 DFS, BFS, graph

def bfs(now):
    cnt = 0
    q = []
    visited = [0] * (n + 1)
    visited[now] = 1
    q.append(now)
    while q:
        v = q.pop(0)
        cnt += 1
        left = v - arr[v - 1]
        right = v + arr[v - 1]

        if 1 <= left < n + 1 and visited[left] == 0:
            q.append(left)
            visited[left] = 1
        if 1 <= right < n + 1 and visited[right] == 0:
            q.append(right)
            visited[right] = 1

    return cnt

n = int(input())
arr = list(map(int, input().split()))
s = int(input())

print(bfs(s))