

def check():
    maxi = 0
    mini = 8e10
    for i in range(N):
        cnt = 0
        result = 0
        for j in range(M):
            if arr[i][j] == cor[j]:
                result += 1 + cnt
                cnt += 1
            else:
                cnt = 0
        if maxi < result:
            maxi = result

        if mini > result:
            mini = result

    print(f'#{tc} {maxi - mini}')


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    cor = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]


    check()



