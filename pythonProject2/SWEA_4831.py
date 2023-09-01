T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    stop = []
    stop += [0] * (N + 1)

    for i in arr:
        stop[i] = 1

    imp = N
    count = 0
    ans = 1
    while imp > 0:
        count += 1
        ercount = 0
        for c in range(1, K+1):
            if stop[imp - c] == 1:
                imp2 = imp - c
            else:
                ercount += 1

            if imp - c < 0:
                imp = 0
        imp = imp2


        if ercount == K:
            ans = 0
            break
        print(imp)
        print(count)
    if ans == 0:
        ans = 0
    else:
        ans = count - 1
    print(f'#{tc} {ans}')


