
T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    sample = list(map(int, input().split()))
    passcode = list(map(int, input().split()))
    answer = 0
    j = 0
    for i in range(K):
        for j in range(N):




    if answer == K:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
