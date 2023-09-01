#
# N = 2 # 행의크기
# M = 4 # 열의크기
# arr = [[0, 1, 2, 3], [4, 5, 6, 7]]
#
# for i in range(N):
#     for j in range(M):
#         print(arr[i][j + (M-1-2*j) * (i % 2)])

#
# # 2차원 배열 만들기
# N = 2
# M = 4
# arr = [[0]*M for _ in range(N)]    # 0000 을  n 번 반복
# print(arr)





N = 3
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]      #상 하 좌 우 를 구성하는 방향틀


max_v = 0    # 모든 원소가 0 이상이라면..
for i in range(N):
    for j in range(N):
        # arr[i][j] 중심으로
        s = arr[i][j]
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                s += arr[ni][nj]
        # 주변 원소를 포함한 합을 구한다
        if max_v < s:
            max_v = s
        # 그 중 최대값 가져오기


print(max_v)