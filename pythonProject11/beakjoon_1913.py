
N = int(input())
G = int(input())
arr = [[0] * N for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dal(N):
    nx, ny = N // 2, N // 2
    arr[nx][ny] = 1
    z = 1
    cnt = 1
    i = 2
    for k in range(N+1):
        for j in range(2):

            while i < (N ** 2 + 1):
                if cnt % 2 == 1:
                    for p in range(2):
                        nx, ny = nx + z * (dy[p]), ny + z * (dx[p])
                        arr[nx][ny] = i
                        i += 1
                    z += 1
                    cnt += 1
                else:
                    for p in range(2, 4):
                        nx, ny = nx + z * (dy[p]), ny + z * (dx[p])
                        arr[nx][ny] = i
                        i += 1
                    z += 1
                    cnt += 1







