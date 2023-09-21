# 유니온파인드 순환회로 검사

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

parents = [i for i in range(N)]

def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return 'WARNING'

    if x < y:
        parents[y] = x
    else:
        parents[x] = y

    return 'STABLE'

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            if find_set(i) != find_set(j):
                union(i, j)

            else:
                print(union(i, j))
                exit()
print('STABLE')
