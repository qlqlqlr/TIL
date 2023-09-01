
# 백준 2563. 색종이 IM 대비

N = int(input())

arr = [[0] * 101 for _ in range(101)]

result = 0
for i in range(N):
    a, b = map(int, input().split())
    for j in range(a, a + 10):
        for k in range(b, b + 10):
            if arr[k][j] == 0:
                arr[k][j] = 1
                result += 1

            else:
                continue

print(result)