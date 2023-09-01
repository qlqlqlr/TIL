
# 액체괴물 놀이

N = int(input())
arr = list(map(int, input().split()))
def ch():
    cnt = 0
    for i in range(N -1):
        x = arr.pop(arr.index(min(arr)))
        y = arr.pop(arr.index(min(arr)))
        tmp = x + y
        cnt += tmp
        arr.append(tmp)

    print(cnt)

ch()