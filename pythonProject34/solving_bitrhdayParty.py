from collections import deque
T = int(input())

def bfs(s, g):
    q = deque
    visited = [0] * N + 1
    q.append()


for tc in range(1, T + 1):
    N, M, X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]

