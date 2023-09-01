

T = 10

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for j in range(N):
        cnt = []
        for i in range(N):
            if arr[i][j] == 1 or arr[i][j] == 2:
                cnt.append(arr[i][j])


        if len(cnt) > 1:

            for k in range(len(cnt) - 1):
                if cnt[k] == 1 and cnt[k + 1] == 2:
                    result += 1

    print(f'#{tc} {result}')


