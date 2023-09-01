# im 대비 기출형 문제
di = [1, 1, -1, -1]
dj = [1, -1, 1, -1]


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
K = int(input())

max_v = 0
for i in range(N):
    for j in range(N):
        cnt = 0           # 시전위치는 카운트 x
        for k in range(4):
            for p in range(1, K+1):
                ni, nj = i + di[k] * p, j + dj[k] * p
                if 0 <= ni < N and 0 <= nj < N:
                    cnt += arr[ni][nj]


        if max_v < cnt:
            max_v = cnt

print(max_v)