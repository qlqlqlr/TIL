
def check():
    maxi1 = 0
    maxi2 = 0
    for i in range(4):
        if arr[i][0] > maxi1:
            maxi1 = arr[i][0]

        if arr[i][2] > maxi1:
            maxi1 = arr[i][2]

        if arr[i][1] > maxi2:
            maxi2 = arr[i][1]

        if arr[i][3] > maxi2:
            maxi2 = arr[i][3]

    return maxi1, maxi2




arr = [list(map(int, input().split())) for _ in range(4)]

maxi1, maxi2 = check()

space = [[0] * maxi1 for _ in range(maxi2)]

for i in range(4):
    for x in range(arr[i][0], arr[i][2]):
        for y in range(arr[i][1], arr[i][3]):
            space[y][x] += 1

result = 0
for i in range(maxi2):
    for j in range(maxi1):
        if space[i][j] != 0:
            result += 1


print(result)
