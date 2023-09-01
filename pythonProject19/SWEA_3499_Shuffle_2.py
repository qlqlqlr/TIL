# 3499 퍼펙트 셔틀 강사님

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    card = input().split()
    result = [0] * len(card)
    if N % 2:
        for i in range(N //2 + 1):
            result[2 * i] = card[i]   #짝수 인덱스에 카드 배치
        for i in range(N // 2): # 절반
            result[2 * i + 1] = card[i + N // 2 + 1]  # 홀수 인덱스에 카드 배치

    # 짝수장의 카드
    else:
        for i in range(N // 2):
            result[2 * i] = card[i]
            result[2 * i + 1] = card[i + N // 2]

    print(f'#{tc}', *result)