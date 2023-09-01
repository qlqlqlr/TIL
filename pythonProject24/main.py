N, M = map(int, input().split())
lst = [i for i in range(1, N + 1)]
path = []

def combinations(start, level):
    if level == M:
        print(*path)
        return

    for i in range(start, N):
        path.append(lst[i])
        combinations(i + 1, level + 1)
        path.pop()

combinations(0, 0)