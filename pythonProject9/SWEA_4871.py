# SWEA 4871. 그래프 경로

def dfs(n, V, adj_m, G):
    stack = []
    visited = [0] * (V + 1)
    visited[n] = 1
    while True:
        for w in range(1, V + 1):
            if adj_m[n][w] == 1 and visited[w] == 0:
                stack.append(n)
                n = w
                visited[n] = 1
                if n == G:
                    return 1
                break
        else:
            if stack:
                n = stack.pop()
            else:
                break
    return 0


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    adj_m = [[0] * (V + 1) for _ in range(V + 1)]
    for i in range(E):
        v1, v2 = arr[i][0], arr[i][1]
        adj_m[v1][v2] = 1


    result = dfs(S, V, adj_m, G)
    print(f'#{tc} {result}')

