N = int(input())
arr = []
a = 0
for i in range(N):
    a = list(map(int, input().split()))
    arr.append(a)
K = int(input())

def magic(y, x):
    dy = [-1, 1, -1, 1]
    dx = [1, 1, -1, -1]
    result = 0
    #마법의 ㅓㅂㅁ위가 4방향
    for l in range(4):
        for k in range(1, K + 1):
            ny = y + dy[l] * k
            nx = x + dx[l] * k
            if 0 <= ny < N and 0 <= nx < N:
                result += arr[ny][nx]

    return result
result_list = []
for i in range(N):
    for j in range(N):
        result_list.append(magic(i, j))
print(max(result_list))