# 2007 패턴 마디의 길이 강사님 풀이

T = int(input())
for tc in range(1, T + 1):
    text = input()
    # 최대길이는 10
    for i in range(1, 11):
        # 0부터 i - 1 == (i 부터 2 * i - 1까지)
        if text[:i] == text[i:i*2]:
            print(f'#{tc} {i}')
            break
