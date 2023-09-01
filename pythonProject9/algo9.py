# # 피보나치 수열 재귀함수

# cnt = 0
#
# def fibo(n):
#     global cnt
#     cnt += 1
#     if n < 2:
#         return n
#     else:
#         return fibo(n-1) + fibo(n-2)
#
#
# print(fibo(30), cnt)           # cnt 26xxxxx


# # 동적할당  DP
#
# def fibo(n):
#     global cnt
#     cnt += 1
#     if n < 2:
#         return memo[n]
#     else:
#         if memo[n] == 0:
#             memo[n] = fibo(n-1) + fibo(n-2)
#         return memo[n]
#
# cnt = 0
# N = 30
# memo = [0] * (N + 1)
# memo[0] = 0
# memo[1] = 1
# print(fibo(N), cnt)             # cnt 59


#
# # 동적할당 2
#
# def fibo(n):
#     dp = [0] * (n+1)
#     dp[0] = 0
#     dp[1] = 1
#     for i in range(2, n + 1):
#         dp[i] = dp[i-1] + dp[i-2]
#
#     return dp[n]
#
#
# print(fibo(30))


'''
V E
v1 w1 v2 w2 ...
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def dfs(n, V, adj_m):
    stack = []         # stack 생성
    visited = [0] * (V + 1)      # visited 생성
    visited[n] = 1               # 시작점 방문 표시
    print(n)                     # do[n]     ( 각 정점에서 한 일 )
    while True:
        for w in range(1, V+1):         # 현재 정점 n에 인접하고 미방문 w 찾기
            if adj_m[n][w] == 1 and visited[w] == 0:
                stack.append(n)
                n = w                   # push(v), v = w
                print(n)                # do(w)
                visited[n] = 1          # w 방문 표시
                break
        else:                       # 현재위치에서 방문할 곳이 남아있지 않음
            if stack:          # 스택에 지나온 정점이 남아 있으면
                n = stack.pop()    # pop() 해서 최근 정점으로 돌아감
            else:                   # 스택이 비어있으면
                break               # while 문 탐색 종료


    return

V, E = map(int, input().split())   # 1번부터 V번 정점, E개의 간선
arr = list(map(int, input().split()))
adj_m = [[0] * (V + 1) for _ in range(V + 1)]
for i in range(E):
    v1, v2 = arr[i * 2], arr[i*2 + 1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1

dfs(1, V, adj_m)