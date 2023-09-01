# SWEA 5174. subtree

def preorder(n):
    if n:
        global cnt
        cnt += 1
        preorder(ch1[n])
        preorder(ch2[n])

    return cnt

T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    ch1 = [0] * (E + 2)
    ch2 = [0] * (E + 2)
    cnt = 0
    for i in range(E):
        p, c = arr[i * 2], arr[i * 2 + 1]
        if ch1[p] == 0:
            ch1[p] = c

        else:
            ch2[p] = c


    print(f'#{tc} {preorder(N)}')
