

arr = []

for i in range(4):
    a = []
    for j in range(5):
        a.append('_')
    arr.append(a)

def explode(y, x):
    direct = [(1, 0), (-1, 0), (0, 1), (0, -1),
              (1, 1), (-1, -1), (-1, 1), (1, -1)]

    for i, j in direct:
        dir_y = y + i
        dir_x = x + j

        if 0 <= dir_y < len(arr) and 0 <= dir_x < len(arr[0]):
            arr[dir_y][dir_x] = '#'


for i in range(2):
    y, x = (map(int, input().split()))
    explode(y, x)
for a in arr:
    print(*a)





