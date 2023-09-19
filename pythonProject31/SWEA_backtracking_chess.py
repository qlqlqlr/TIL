N = int(input())

arr = [i for i in range(1, N + 1)]
cnt = 0
path = [0] * N

def backtracking(idx):
    global cnt
    if idx == N:
        if len(set(path)) == N:
            cnt += 1
        return

    for num in arr:
        if num not in path[:idx]:
            path[idx] = num
            backtracking(idx + 1)

backtracking(0)
print(cnt)
