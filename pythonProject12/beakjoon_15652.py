N, M = map(int, input().split())
lst = [i for i in range(1, N + 1)]
path = []
used = [0] * N


def dfs(start, level):
    global path
    if level == M:
        print(*path)

        return

    for i in range(start, N):
        path.append(lst[i])
        dfs(i , level + 1)
        path.pop()


dfs(0, 0)