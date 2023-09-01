# 콜라츠 추측

def colatz(N):
    if N == 1:
        return 0
    elif N % 2 == 0:
        return 1 + colatz(N // 2)
    elif N % 2 != 0:
        return 1 + colatz(N * 3 + 1)


N = int(input())
print(colatz(N))
