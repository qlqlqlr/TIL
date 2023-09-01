
# 바이러스  (BFS)

def bfs(n):
    cnt = 0
    q = []
    visited = [0] * (N + 1)
    visited[n] = 1
    q.append(n)

    while q:
        now = q.pop(0)
        cnt += 1
        for w in range(K):
            if arr[w][0] == now and visited[arr[w][1]] == 0:
                q.append(arr[w][1])
                visited[arr[w][1]] = 1
            elif arr[w][1] == now and visited[arr[w][0]] == 0:
                q.append(arr[w][0])
                visited[arr[w][0]] = 1
    return cnt - 1

N = int(input())
K = int(input())
arr = [list(map(int, input().split())) for _ in range(K)]

print(bfs(1))