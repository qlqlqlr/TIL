
N, M = map(int, input().split())
lst = [i for i in range(1, N + 1)]
path = []
used = [0] * N


def dfs(level):
    global path
    if level == M:
        print(*path)

        return

    for i in range(N):
        if used[i] == 1:
            continue
        path.append(lst[i])
        used[i] = 1
        dfs(level + 1)
        used[i] = 0
        path.pop()

dfs(0)

