
def dfs(n, N, adj_m):
    global result
    stack = []
    visited = [0] * (N + 1)
    visited[n] = 1
    result.append(n)

    while True:
        for w in range(N, 0, -1):
            if adj_m[n][w] == 1 and visited[w] == 0:
                stack.append(n)
                n = w
                result.append(n)
                visited[n] = 1
                break
        else:
            if stack:
                n = stack.pop()
            else:
                break
    return result



N, M, R = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(M)]
adj_m = [[0] * (N + 1) for _ in range(N + 1)]
result = []

for i in range(M):
    v1, v2 = arr[i][0], arr[i][1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1





result = dfs(R, N, adj_m)
for k in range(1, N+1):
    if k not in result:
        print(0)
    else:
        cnt = 1
        cnt += result.index(k)
        print(cnt)


