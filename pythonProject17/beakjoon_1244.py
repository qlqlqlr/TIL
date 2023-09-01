
N = int(input())

arr = list(map(int, input().split()))

st = int(input())

stu_arr = [list(map(int, input().split())) for _ in range(st)]



def ch():
    asdf = arr
    for i in range(st):
        if stu_arr[i][0] == 1:
            num = stu_arr[i][1]

            for j in range(1, N + 1):
                if j % num == 0:
                    if arr[j - 1] == 0:
                        arr[j - 1] = 1
                    else:
                        arr[j - 1] = 0


        if stu_arr[i][0] == 2:
            num = stu_arr[i][1]

            if arr[num -1 ] == 0:
                arr[num - 1] = 1
            else:
                arr[num - 1] = 0

            for j in range(1, N//2):
                if 0 <= num - j - 1 and num + j - 1 < N:
                    if arr[num - j - 1] == arr[num + j - 1]:
                        if arr[num - j - 1] == 0:
                            arr[num - j - 1] = 1
                            arr[num + j - 1] = 1
                        elif arr[num - j - 1] == 1:
                            arr[num - j - 1] = 0
                            arr[num + j - 1] = 0
    cnt = 0

    if N // 20 != 0:
        while cnt < N // 20 + 1:
            i = 0
            while i < 20:
                print(arr[i + cnt * 20], end = ' ')
                i += 1
                if i + cnt * 20 == len(arr):
                    break
            print()
            cnt += 1
    else:
        print(*arr)

ch()



