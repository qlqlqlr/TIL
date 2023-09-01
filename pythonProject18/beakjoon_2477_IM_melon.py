# Im 대비 백준 참외밭

K = int(input())

arr = [list(map(int, input().split())) for _ in range(6)]
def ch():
    a = 0
    b = 0
    maxx = 0
    maxy = 0
    for i in range(len(arr)):
        if arr[i][0] == 1 or arr[i][0] == 2:
            if a < arr[i][1]:
                maxx = i
                a = arr[i][1]

        else:
            if b < arr[i][1]:
                maxy = i
                b = arr[i][1]

    if maxx < len(arr) - 1:
        x = arr[maxx - 1][1] - arr[maxx + 1][1]


    else:
        x = arr[maxx - 1][1] - arr[0][1]


    if maxy < len(arr) - 1:
        y = arr[maxy - 1][1] - arr[maxy + 1][1]

    else:
        y = arr[maxy - 1][1] - arr[0][1]

    if x * y < 0:
        x *= -1

    result = (a * b) - (x * y)
    print(result * K)

ch()