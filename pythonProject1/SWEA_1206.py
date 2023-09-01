T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = []
    answer = 0
    for i in range (2, N-3):
        dif = []
        for j in range(-2, 3):
            if arr[i] >= arr[i + j]:
                dif.append(arr[i] - arr[i + j])
                if arr[i] == arr[i + j] and j != 0:
                    print(i)
            else:
                break
            if len(dif) == 5:
                dif.pop()

                ans.append(min(dif))

    answer = sum(ans)
    print(f'#{tc} {answer}')