T = int(input())


for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    space = [[0]*10 for _ in range(10)]
    count = 0

    for i in range (N):
        r1, c1 = arr[i][0], arr[i][1]
        r2, c2 = arr[i][2], arr[i][3]
        color = arr[i][4]

        for j in range(r1, r2+1):
            for k in range(c1, c2+1):
                if color == 1:
                    if space[j][k] == 0:
                        space[j][k] = 1
                    elif space[j][k] == 1:
                        space[j][k] = 1
                    elif space[j][k] == 2:
                        space[j][k] = 3
                        count += 1
                    else:
                        space[j][k] = 3
                else:
                    if space[j][k] == 0:
                        space[j][k] = 2
                    elif space[j][k] == 1:
                        space[j][k] = 3
                        count += 1
                    elif space[j][k] == 2:
                        space[j][k] = 2
                    else:
                        space[j][k] = 3

    print(f'#{tc} {count}')

    # for z in range(10):
    #     print(space[z])


