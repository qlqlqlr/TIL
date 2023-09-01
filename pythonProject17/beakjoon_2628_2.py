

a, b = map(int, input().split())

arr = [[1] * a for _ in range(b)]

N = int(input())
cut = [list(map(int, input().split())) for _ in range(N)]

xs = []
ys = []

for i in range(N):
    if cut[i][0] == 0:
        xs.append(cut[i][1])

    elif cut[i][0] == 1:
        ys.append(cut[i][1])

xs.append(b)
ys.append(a)

xs.sort()
ys.sort()

def ch():
    cnt = 0
    maxi = 0

    e = xs
    r = ys

    for k in range(len(xs)):
        for l in range(len(ys)):
            if k == 0:
                if l == 0:
                    cnt = (ys[l] - 0) * (xs[k] - 0)
                    if maxi < cnt:
                        maxi = cnt
                else:
                    cnt = (ys[l] - ys[l - 1]) * (xs[k] - 0)
                    if maxi < cnt:
                        maxi = cnt
            else:
                if l == 0:
                    cnt = (ys[l] - 0) * (xs[k] - xs[k - 1])
                    if maxi < cnt:
                        maxi = cnt
                else:
                    cnt = (ys[l] - ys[l - 1]) * (xs[k] - xs[k - 1])
                    if maxi < cnt:
                        maxi = cnt

    print(maxi)

ch()