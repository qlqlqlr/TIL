
N, M, L = map(int, input().split())

def ch():
    arr = [0] * (N + 1)

    now = 1
    cnt = -1
    while True:
        arr[now] += 1
        cnt += 1

        if arr[now] == M:
            print(cnt)
            break


        if arr[now] % 2 == 1:
            now += L
            if now > N:
                now = now - N


        else:
            now -= L
            if now < 1:
                now = N + now


ch()