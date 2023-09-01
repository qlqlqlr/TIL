# swea 4880. 토너먼트 카드게임

def card(i, j, arr):

    if j - i = 1:

        if arr[i] == arr[j]:
            return i

        else:
            if arr[i] == 1:
                if arr[j] == 2:
                    return j
                elif arr[j] == 3:
                    return i

            elif arr[i] == 2:
                if arr[j] == 3:
                    return j
                elif arr[j] == 1:
                    return i

            elif arr[i] == 3:
                if arr[j] == 1:
                    return j
                elif arr[j] == 2:
                    return i
    else:
        return



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    i = 0
    j = N - 1

    print(f'#{tc} {card(N, arr)}')