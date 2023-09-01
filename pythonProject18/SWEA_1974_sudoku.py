
# SWEA 1974 스도쿠 검증

def sudoku():
    result = 0
    # for i in range(9):
    #     ch = []
    #     ch = set(arr[i])
    #     if len(ch) == 9:
    #         result += 1
    #
    #     else:
    #         result = 0
    #         print(f'#{tc} {result}')
    #         return
    #
    #     stack = []
    #     for j in range(9):
    #         stack.append(arr[j][i])
    #     stack = set(stack)
    #     if len(stack) == 9:
    #         result += 1
    #
    #     else:
    #         result = 0
    #         print(f'#{tc} {result}')
    #         return

    a, b = 0, 0

    while True:
        check = []
        for k in range(a, a + 3):
            for l in range(b, b + 3):
                check.append(arr[k][l])

        check = set(check)
        if len(check) == 9:
            result += 1
            if a < 6:
                a += 3
            elif a == 6 and b < 6:
                b += 3

            elif a == 6 and b == 6:
                break

            continue
        else:
            result = 0
            print(f'#{tc} {result}')
            return
    if result != 0:
        result = 1
        print(f'#{tc} {result}')

T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    sudoku ()