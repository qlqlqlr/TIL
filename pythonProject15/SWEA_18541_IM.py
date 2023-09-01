
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    sample = list(map(int, input().split()))
    passcode = list(map(int, input().split()))
    i = 0
    result = 0
    while i < K:
        for j in range(N):
            if passcode[i] == sample[j]:
                i += 1
                continue

            if i == K - 1:
                result = 1
                break

        break

    print(f'#{tc} {result}')
