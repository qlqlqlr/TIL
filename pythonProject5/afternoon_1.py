T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    ans = 0
    bigg = 0
    bigg_list = []
    imp = 0
    can_list = []
    for i in range(N):
        for j in range(N):
            imp = 0
            for k in range(N):
                for l in range(N):
                    if arr[i][j] == arr[k][l]:
                        if k == i and l == j:
                            continue
                        else:
                            if k >= i and l >= j:
                                cnt += 1
                                can = (k - i + 1) * (l - j + 1)
                                can_list.append(can)
            print(can_list)

            if len(can_list) != 0:
                bigg = max(can_list)
                bigg_list.append(bigg)
                print(bigg_list)
                for zz in range(len(can_list)):
                    if can_list[zz] == max(can_list):
                        imp += 1
                if imp > 1:
                    ans += (imp - 1)


    if cnt == 0:
        ans = 9

    for z in range(len(bigg_list)):
        if bigg_list[z] == max(bigg_list):
            ans += 1
            print(ans)
    print(f'#{tc} {ans}')

