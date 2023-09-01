# 4864. [파이썬 S/W 문제해결 기본] 3일차 - 문자열 비교


T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    N, M = len(str1), len(str2)
    result = 0

    if str1 in str2:
        result = 1

    else:
        result = 0

    print(f'#{tc} {result}')
