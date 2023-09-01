# 런타임 에러 고친 버전

N = int(input())
arr = list(map(int, input().split()))
st = int(input())
stu_arr = [list(map(int, input().split())) for _ in range(st)]

def ch():
    for i in range(st):
        if stu_arr[i][0] == 1:
            num = stu_arr[i][1]
            for j in range(num - 1, N, num):  # 해당 위치를 변경해야 합니다.
                arr[j] = 1 - arr[j]

        if stu_arr[i][0] == 2:
            num = stu_arr[i][1]
            arr[num - 1] = 1 - arr[num - 1]
            left = num - 2
            right = num
            while left >= 0 and right < N and arr[left] == arr[right]:
                arr[left] = 1 - arr[left]
                arr[right] = 1 - arr[right]
                left -= 1
                right += 1

    cnt = 0
    for val in arr:
        print(val, end=' ')
        cnt += 1
        if cnt % 20 == 0:
            print()

ch()