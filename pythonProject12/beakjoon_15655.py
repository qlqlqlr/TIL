N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
path = []
used = [0] * N


def dfs(start, level):
    global path
    if level == M:
        print(*path)

        return

    for i in range(start, N):
        if used[i] == 1:
            continue
        path.append(lst[i])
        used[i] = 1
        dfs(i + 1, level + 1)
        used[i] = 0
        path.pop()


dfs(0, 0)