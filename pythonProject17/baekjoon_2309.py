# 백준 2309. 일곱난쟁이 IM 대비


arr = []
for i in range(9):
    num = int(input())
    arr.append(num)

n = len(arr)        # n : 원소의 개수


for i in range(1 << n) :        # 1<<n : 부분집합의 개수     2^n
    total = 0
    result = []
    for j in range(n):        # 원소의 수만큼 비트를 비교함
        if i & (1 << j):         # i의 j번 비트가 1인경우
            total += arr[j]        # j 번 원소 더함
            result.append(arr[j])

    if total == 100 and len(result) == 7:
        result.sort()
        for k in range(len(result)):
            print(result[k])
        break