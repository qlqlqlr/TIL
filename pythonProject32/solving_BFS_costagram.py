from collections import deque
# 솔빙클럽 BFS 코스타그램

N = int(input())
M = int(input())
arr = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    arr[x][y] = 1
    arr[y][x] = 1

coco = int(input())

cnt = -1
def bfs(now):
    global cnt
    q = deque()
    visited = [0] * (N + 1)
    q.append(now)
    visited[now] = 1
    while q:
        cn = q.popleft()
        cnt += 1
        for i in range(N + 1):
            if arr[cn][i] == 1 and visited[i] == 0:
                nn = i
                q.append(nn)
                visited[nn] = 1

bfs(coco)
print(cnt)

