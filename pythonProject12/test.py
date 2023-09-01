def f(i, N, s, M, selected):
    if i == N:
        if sum(selected) == M and s == target_sum:
            for j in range(N):
                if selected[j]:
                    print(A[j], end=" ")
            print()
        return
    else:
        selected[i] = 1
        f(i+1, N, s * A[i], M, selected)
        selected[i] = 0
        f(i+1, N, s, M, selected)
        return

N, M = map(int, input().split())
A = list(map(int, input().split()))
target_sum = 1  # Initialize the target sum
for num in A:
    target_sum *= num

bit = [0] * N
selected = [0] * N
f(0, N, 1, M, selected)