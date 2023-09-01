# 강사님 풀이
# 같은색인 영역은 겹치지 않는다. 라는 조건을 참고하여 같은색은 겹칠 일이 없다는 전제하에 코드작성.

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    space = [[0]*10 for _ in range(10)]
    count = 0

    for i in range(N):
        row1, col1, row2, col2, color = map(int, input().split())

        for j in range(row1, row2 + 1):
            for k in range(col1, col2 + 1):
                arr[j][k] += color
                # 격자 값이 3이면 카운팅
                if arr[i][j] == 3:
                    count += 1

    print(f'#{tc} {count}')
