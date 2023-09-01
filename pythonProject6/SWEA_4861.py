# 4861. [파이썬 S/W 문제해결 기본] 3일차 - 회문

def is_palindrome(s):
    return s == s[::-1]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]

    result = ""

    # 가로 방향에서 회문 찾기
    for row in board:
        for i in range(N - M + 1):
            if is_palindrome(row[i:i+M]):
                result = row[i:i+M]
                break

    # 세로 방향에서 회문 찾기
    for i in range(N):
        col = "".join(row[i] for row in board)
        for j in range(N - M + 1):
            if is_palindrome(col[j:j+M]):
                result = col[j:j+M]
                break

    print(f'#{tc} {result}')

