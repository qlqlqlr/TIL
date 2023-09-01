# SWEA 1926 간단한 369 게임

N = int(input())
for i in range(1, N + 1):
    cnt = 0
    a = i // 100
    b = (i % 100) // 10
    c = i % 10
    if a == 3 or a == 6 or a == 9:
        cnt += 1

    if b == 3 or b == 6 or b == 9:
        cnt += 1

