# swea 4881 배열 최소 합

def f(i, N):
    if i == N:
        print(bit)
        return
    else:
        bit[i] = 1
        f(i+1, N)
        bit[i] = 0
        f(i+1, N)
        return

A = [1, 2, 3]
bit = [0] * 3
f(0, 3)