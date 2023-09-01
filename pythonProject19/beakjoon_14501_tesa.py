# 백준 퇴사

N = int(input())
arr = [list(map(int, input().split()))for _ in range(N)]

def dfs(n):
    hab = 0
    stack = []
    visited = [0] * N
    visited[n] = 1
    for j in range(n, n + arr[n][0]):
        visited[j] = 1
    while True:
        for w in range(1, N):
            if visited[w] == 0:

    return hab

for i in range(N):

    result = dfs(i)
    if result > maxi:
        maxi = result

    print(result)

