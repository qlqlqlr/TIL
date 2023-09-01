
N = int(input())

arr = []
def binary(N):

    if N == 0:
        arr.append(0)
    elif N == 1:
        arr.append(1)
    else:
        arr.append(N % 2)
        binary(N // 2)

    return arr

binary(N)
arr.reverse()
print(*arr, sep = '')
