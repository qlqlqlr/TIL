
# 베이비진 게임

def bab(a, b):
    for i in range(12):
        if i == 0:
            a.append(arr[i])
        elif i % 2 == 0:
            a.append(arr[i])
            if i > 4:
                for j in range(10):
                    if a.count(j) == 3:
                        return 1
                    if a.count(j) >= 1:
                        if a.count(j + 1) >= 1 and a.count(j + 2) >= 1:
                            return 1

        else:
            b.append(arr[i])
            if i > 5:
                for j in range(10):
                    if b.count(j) == 3:
                        return 2
                    if b.count(j) >= 1:
                        if b.count(j + 1) >= 1 and b.count(j + 2) >= 1:
                            return 2
    return 0

T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    a = []
    b = []
    print(f'#{tc} {bab(a, b)}')


