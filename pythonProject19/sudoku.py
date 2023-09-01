# SWEA 스도쿠 검증 IM 대비

def sudoku():
    for i in range(9):
        st1 = arr[i]
        st1 = set(st1)
        if len(st1) < 9:
            return 0

        st2 = []
        for j in range(9):
            st2.append(arr[j][i])
        st2 = set(st2)
        if len(st2) < 9:
            return 0
    x = 0
    y = 0
    while True:
        st3 = []
        for k in range(x, x + 3):
            for l in range(y, y + 3):
                st3.append(arr[k][l])
        st3 = set(st3)
        if len(st3) < 9:
            return 0

        if x < 6:
            x += 3
            y += 3
        else:
            break

    return 1


T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = sudoku()
    print(f'#{tc} {result}')

