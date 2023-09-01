# 2023 im 기출문제

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


T = int(input())
#N 칸수, 파워
for tc in range(1, T+1):
    N, P = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for zz in range(N):
        print(arr[zz])
    max_v = 0
    for i in range(N):
        for j in range(N):
            cnt = arr[i][j]
            print(cnt)
            for k in range(4):
                for p in range(1, P+1):
                    ni = i + di[k] * p
                    nj = j + dj[k] * P
                    if 0 <= ni < N and 0 <= nj < N:
                        cnt += arr[ni][nj]
                        print(cnt)

            if max_v < cnt:
                max_v = cnt

    print(f'#{tc} {max_v}')
# 행렬


#각 테스트 케이스에서 최대갑 출력