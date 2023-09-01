
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

arr2 = []

def bubun(arr):
    n = len(arr)  # n : 원소의 개수
    cnt = 0

    for i in range(1 << n) :        # 1<<n : 부분집합의 개수     2^n
        arr1 = []
        for j in range(n):        # 원소의 수만큼 비트를 비교함
            if i & (1 << j):         # i의 j번 비트가 1인경우
                arr1.append(arr[j])        # j 번 원소 출력

        arr2.append(arr1)
        total = 0
        if len(arr2[i]) == N:
            for k in range(N):
                total += arr2[i][k]
                if total == K:
                    cnt += 1

    return cnt

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    result = bubun(A)

    print(f'#{tc} {result}')










