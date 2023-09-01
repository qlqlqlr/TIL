from collections import deque

T = int(input())
for tc in range(1, 1 + T):
    N, M = map(int, input().split())    # 화덕 크기 N ,  피자 개수 M
    pizza = list(map(int, input().split()))
    arr = deque()
    for i in range(M):
        arr.append([i+1, pizza[i]])
    cnt = 0
    while True:
        arr.rotate(1)
        cnt += 1
        if cnt % N == 0:
            for j in range(N):
                arr[j][1] //= 2

