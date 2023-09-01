# SWEA 5356. 의석이의 세로로 말해요


T = int(input())
for tc in range(1, T + 1):
    arr = [list(input()) for _ in range(5)]
    N = 0
    result = []
    for i in range(5):
        N += len(arr[i])
    while True:
        for i in range(5):
            try :
                result.append(arr[i].pop(0))


            except:
                continue

        if len(result) == N:
            break

    print(f'#{tc}', end = ' ')
    print(*result, sep = '')