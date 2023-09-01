
def dfs(n, V, arr):
    stack = []
    visited = [0] * V
    visited[n] = 1
    path = []
    path.append(n)
    cnt = 1

    while True:
        for w in range(V):
            if arr[n][w] == 1 and visited[w] == 0:
                cnt += 1
                stack.append(n)
                n = w
                visited[n] = 1
                path.append(n)
                if cnt == 3:
                    print(*path)
                    path.pop()
                    path.pop()
                break
        else:
            if stack:
                n = stack.pop()
                if n == 0:
                    path.pop()
                    path.pop()
                path.append(n)
                cnt -= 1
            else:
                break







N = int(input())
arr = [list(map(int, input().split()))for _ in range(N)]

dfs(0, N, arr)