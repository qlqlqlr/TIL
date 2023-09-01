
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * 3          # 현재 경로에서 방문한 노드를 저장할 리스트

def dfs(now, level):
    global visited
    visited[level] = str(now) # 현재 방문한 노드를 저장
    if level == 2:
        print(' '.join(visited))

    for i in range(N):
        if arr[now][i] == 1:
            dfs(i, level + 1)

dfs(0, 0)