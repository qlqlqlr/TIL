
T = int(input())
for tc in range(1, T +1):
    N, M = map(int, input().split())
    Q = list(map(int, input().split()))

    result = 0
    n = M % N


    for i in range(N):
        if i == n:
            result = Q[i]


    print(f'#{tc} {result}')
