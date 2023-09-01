
# 자석 문제

T = 10
for tc in range(1, T +1):
    N = int(input())
    mag = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for j in range(N):
        y, x = 0, j
        stack = []
        while y < N:
            if not stack and mag[y][x] == 1:   # 스택이 비어있고, 현재 N극의 성질
                stack.append(1)
            elif stack and mag[y][x] == 2:     #스택에  N극에 성질이 있고, 현재 S극의 성질
                cnt += stack.pop()

            y += 1  # 다음행으로 이동

    print(f'#{tc} {cnt}')