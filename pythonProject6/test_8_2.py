T= int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = 0

    for i in range(N):
        for j in range(0, N, i + 1):
            result += numbers[j]

        # result가 0잏이면 0으로 작성
        result = result if result > 0 else 0
        print(f'#{tc} {result}')