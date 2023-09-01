
# 동전교환 LOW

coin = [500, 100, 50, 10]

N = int(input())

def ch(N):
    cnt = 0
    for i in range(4):
        if N >= coin[i]:
            cnt += N // coin[i]
            N = N % coin[i]


    print(cnt)

ch(N)