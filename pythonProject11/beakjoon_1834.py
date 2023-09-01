
N = int(input())

arr = []
result = 0
for i in range(1, N):

    arr.append(i * N + i)

result = sum(arr)

print(result)
