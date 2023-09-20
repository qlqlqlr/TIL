# 솔빙 클럽 DFS의 탑 크리스마스 트리

N = int(input())
arr = [list(map(int, input().split()))for _ in range(N)]
path1 = []
path2 = []
path3 = []


def dfs1(node):
    pass

# 시작 노드를 1로 가정
dfs1(1)
print(*path1)

def dfs2(now):
    visited = [0] * (N + 1)
    visited[now] = 1
    path2.append(now)

    for to in range(1, 3):
        next = arr[now - 1][to]
        if visited[next] == 1:
            continue

        if next == -1:
            continue
        dfs2(next)

dfs2(1)
print(*path2)

def dfs3(now):
    visited = [0] * (N + 1)
    visited[now] = 1

    for to in range(1, 3):
        next = arr[now - 1][to]
        if visited[next] == 0 and next != -1:
            dfs3(next)
    else:
        path3.append(now)


dfs3(1)
print(*path3)