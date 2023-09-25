T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 16진수 자리수 N
    P = list(input())  # 암호화된 16진수 P 리스트
    key = int(input(), 16)  # 한 자리 16진수 key 입력받아 정수로 변환

    H = [0] * N
    for i in range(N):
        # XOR 연산(^) : 두 비트 값이 다를때는 1반환, 같을 때는 0 반환
        H[i] = int(P[i], 16) ^ key  # P의 i번째 자리 16진수를 정수로 변환후 key와 xor 연산

    print(f'#{tc}', end=' ')
    for x in H:
        print(f'{x:X}', end='')
    print()