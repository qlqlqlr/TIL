#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     cnt = [0] * 5001 # 1-5000번 각 정류장을 지나는 노선수
#     for _ in range(N):  # N개의 노선에 대해
#         A, B = map(int, input().split())
#         for i in range(A, B+1):
#             cnt[i] += 1           #현재 노선이 i번 정류장 정착
#
#     P = int(input())
#     bus_stop = [int(input()) for _ in range(P)]
#     print(f'#{tc}', end = ' ')
#     for x in bus_stop:
#         print(cnt[x], end = ' ')
#     print()



# # 1979. 어디에 단어가 들어갈 수 있을까
#
# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     ans = 0         # 조건에 부합하는 자리 수
#     for i in range(N):         # 행 우선 순회
#         cnt = 0
#         for j in range(N):
#             if arr[i][j]:
#                 cnt += 1
#
#             if j == N - 1 or arr[i][j] == 0:
#                 if cnt == K:
#                     ans += 1
#                 cnt = 0
#     print(ans)
#
#     # 세로도 고려해야하니까 열 우선 순회 작성해보자

#
# # 16268. 풍선팡2
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     max_v = 0
#     for i in range(N):
#         for j in range(M):
#             cnt = arr[i][j]   # 터트린 풍선의 꽃가루 수
#             for k in range(4): # i, j 인접(상하좌우)에 대해
#                 ni, nj = i+di[k], j+dj[k]
#                 if 0 <= ni < N and 0 <= nj < M:
#                     cnt += arr[ni][nj]
#
#             if max_v < cnt:
#                 max_v = cnt
#     print(f'#{tc} {max_v}')



# 9490. 풍선팡
#
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     max_v = 0
#     for i in range(N):
#         for j in range(M):
#             cnt = arr[i][j]   # 터트린 풍선의 꽃가루 수
#             for k in range(4): # i, j 인접(상하좌우)에 대해
#                 for p in range(1, arr[i][j]+1):
#                     ni, nj = i+di[k] * p, j+dj[k] * p
#                     if 0 <= ni < N and 0 <= nj < M:
#                         cnt += arr[ni][nj]
#
#             if max_v < cnt:
#                 max_v = cnt
#     print(f'#{tc} {max_v}')
