# 14889 스타트와 링크

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
M = N // 2
lst = [i for i in range(1, N + 1)]
path = []
tmp = []
cnt = 0
min = 1000

def combinations(start, level):
    if level == M:
        tmp.append([*path])
        return

    for i in range(start, N):
        path.append(lst[i])
        combinations(i + 1, level + 1)
        path.pop()

combinations(0, 0)
print(tmp)

# for i in range(N):
#     for j in range(N):



