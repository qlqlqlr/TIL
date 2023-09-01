

space = [list(map(int, input().split())) for _ in range(5)]
mc = [list(map(int, input().split())) for _ in range(5)]
directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
cntlist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    # 가로 12345 세로12345 대각 좌 우

# for i in range(5):
#     for j in range(5):
#         cnt = 0
#         for k in range(5):
#             for l in range(5):
#                 if space[k][l] == mc[i][j]:
#                     space[k][l] = 0
#                     cntlist[k] += 1
#                     cntlist[l] += 1
#                     if k == l:
#                         cntlist[10] += 1
#
#
#         for


for i in range(5):
    for j in range(5):
        cnt = 0
        for k in range(5):
            for l in range(5):
                if space[k][l] == mc[i][j]:
                    for dy, dx in directions:
                        for ck in range(1, 5):
                            ny, nx = i + (ck * dy), j + (ck * dx)
                            if 0 <= ny < 5 and 0 <= nx < 5:
                                if space[ny][nx] == '_':
                                    space[ny][nx] = '%'
                                if space[ny][nx] == '#':
                                    break
