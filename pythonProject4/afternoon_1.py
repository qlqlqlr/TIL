

N, M = map(int, input().split())
K = int(input())
space = [list(map(str, input())) for _ in range(N)]


def explode(y, x):
    direct2 = []
    for k in range(1, K+1):
        direct = [(k, 0), (-k, 0), (0, k), (0, -k)]
        direct2.append(direct)
    for t in range(len(direct2)):
        for i, j in direct2[t]:
            dir_y = y + i
            dir_x = x + j

            if 0 <= dir_y < len(space) and 0 <= dir_x < len(space[0]):
                if space[dir_y][dir_x] != '#':
                    space[dir_y][dir_x] = '%'
                else:
                    break

for a in range(N):
    for b in range(M):
        if space[a][b] == '@':
            space[a][b] = '%'
            explode(a, b)

for z in range(len(space)):
    result = ''.join(space[z])
    print(result)
