# swea 솔빙클럽 18417. 다빈치 코드

def f(i, N, s, M):
    global arr
    global cnt
    global minsub
    if i == N:
        if cnt == M:
            if s < minsub:
                minsub = s
                for k in range(N):
                    if bit[k] == 1:
                        arr.append(A[k])
            return
    else:
        bit[i] = 1
        cnt += 1
        f(i+1, N, s*A[i], M)
        bit[i] = 0
        cnt -= 1
        f(i+1, N, s, M)
        return

arr = []
cnt = 0
minsub = 0
N, M = map(int, input().split())
A = list(map(int, input().split()))
bit = [0] * N
f(0, N, 1, M)
p = len(arr)
for z in range(p-3, p):
    print(arr[z], end = ' ')