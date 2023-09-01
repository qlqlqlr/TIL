
N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
path = []
used = [0] * N
use_com = []

def dfs(level):
    global path
    if level == M:
        for i in range(len(use_com)):
            if use_com[i] == path:
                continue
        else:
            print(*path)
            use_com.append(path)

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