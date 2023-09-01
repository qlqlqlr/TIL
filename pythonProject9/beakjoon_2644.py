
def dfs(n, N, adj_m, G):
    stack = []
    visited = [0] * (N + 1)
    visited[n] = 1
    cnt = 0
    while True:
        for w in range(1, N+1):
            if adj_m[n][w] == 1 and visited[w] == 0:
                stack.append(n)
                n = w
                cnt += 1
                visited[n] = 1
                if n == G:
                    return cnt
                break
        else:
            if stack:
                n = stack.pop()
                cnt -= 1
            else:
                return -1

    return cnt


N = int(input())     # 전체 사람의 수
S, G = map(int, input().split())    # 촌수를 계산해야하는 두사람의 번호
m = int(input())      # 관계 개수
arr = [list(map(int, input().split())) for _ in range(m)]      # 관계도 m 개
adj_m = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(m):
    v1, v2 = arr[i][0], arr[i][1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1

print(dfs(S, N, adj_m, G))


