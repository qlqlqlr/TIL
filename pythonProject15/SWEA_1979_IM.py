# SWEA 1979. 어디에 단어가 들어갈 수 있을까

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def where():
    result = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                for k in range(4):
                    cnt = 1
                    for l in range(1, K + 1):
                        nx = i + l * dx[k]
                        ny = j + l * dy[k]
                        nx2 = i + (-1) * dx[k]
                        ny2 = j + (-1) * dy[k]

                        if 0 <= nx2 < N and 0 <= ny2 < N:
                            if arr[nx2][ny2] == 1:
                                break

                        if 0 <= nx < N and 0 <= ny < N:

                            if arr[nx][ny] == 1:
                                cnt += 1
                            elif cnt != K and arr[nx][ny] == 0:
                                break
                    if cnt == K:
                        result += 1

    return result // 2



T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]


    print(f'#{tc} {where()}')

