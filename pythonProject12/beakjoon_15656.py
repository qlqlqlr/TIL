
N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
path = []
used = [0] * N


def dfs(level):
    global path
    if level == M:
        print(*path)

        return

    for i in range(N):

        path.append(lst[i])
        used[i] = 1
        dfs(level + 1)
        used[i] = 0
        path.pop()


dfs(0)