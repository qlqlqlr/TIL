
A, B, V = map(int, input().split())

cnt = 0
up = 0

ini = V // A

if A * (ini - 1) - (B * (ini - 1)) < V:
    up = A * (ini - 1) - (B * (ini - 1))
    cnt = ini - 1

elif if A * (ini - 1) - (B * (ini - 1)) == V:
    up = A * (ini - 1) - (B * (ini - 1))
    cnt = ini - 1

else:
    up = A * (ini - A - B) - (B * (ini - A - B))
    cnt = ini - A - B

while up < V:

    if up + A >= V:
        up += A
        cnt += 1

    else:
        up += A
        up -= B
        cnt += 1



print(cnt)

