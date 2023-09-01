# 백준 2578. 빙고 IM 대비

arr = [list(map(int, input().split())) for _ in range(5)]

mc = [list(map(int, input().split())) for _ in range(5)]




def ch():
    cnt = [0] * 12
    mcnt = 0

    for m in mc:
        for c in m:
            mcnt += 1
            for i in range(5):
                for j in range(5):
                    if arr[i][j] == c:

                        cnt[j] += 1
                        cnt[i + 5] += 1
                        if i == j:
                            cnt[10] += 1

                        if i + j == 4:
                            cnt[11] += 1
                        break
            result = 0
            for k in range(12):
                if cnt[k] == 5:
                    result += 1
                    if result >= 3:
                        return mcnt
    return mcnt

print(ch())