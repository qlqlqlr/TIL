
def ccc():
    result = 0
    answer = 0
    cnt = 0
    for i in range(N):
        for j in range(N):

            for l in range(i, N):
                for k in range(j, N):
                    if arr[i][j] == arr[l][k]:
                        if k - j == 0 and l - i == 0:
                            cnt = 1
                        elif k - j == 0 and l - i != 0:
                            cnt = (l - i + 1)
                        elif k - j != 0 and l - i == 0:
                            cnt = (k - j + 1)
                        else:
                            cnt = (k - j + 1) * (l - i + 1)

                        if cnt > result:

                            result = cnt
                            answer = 1

                        elif cnt == result:
                            answer += 1



    return answer

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]






    print(f'#{tc} {ccc()}')
