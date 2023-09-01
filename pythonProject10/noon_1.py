
def dfs(n, V, adj_m):
    stack = []
    visited = [0] * V
    visited[n] = 1
    print(n, end = ' ')

    while True:
        for w in range(V):
            if adj_m[n][w] == 1 and visited[w] == 0:
                stack.append(n)
                n = w
                visited[n] = 1
                print(n, end = ' ')
                break
        else:
            if stack:
                n = stack.pop()
            else:
                break
    return

n = int(input())
arr = [list(map(int, input().split()))for _ in range(n)]

dfs(0, n, arr)
