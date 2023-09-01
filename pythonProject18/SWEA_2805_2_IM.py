
T = int (input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    start, end = N // 2, N // 2
    result = 0
    for i in range(N):    # 각 행 순회
        for j in range(start, end + 1):   # 열순회
            result += arr[i][j]
        if i < N // 2:   # 농장의 상단부분
            start -= 1
            end += 1

        else:            # 농장의 하단 부분
            start += 1
            end -= 1

    print(f'#{tc} {result}')