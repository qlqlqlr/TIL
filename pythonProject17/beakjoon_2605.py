# 백준 2605. 줄 세우기 IM 대비


S = int(input())
arr = list(map(int, input().split()))

def line():
    result = []
    tmp = []
    cnt = 0
    for i in range(S):
        if cnt == arr[i]:
            tmp.append(cnt + 1)
            if result:
                for j in range(len(result)):
                    tmp.append(result[j])

            result = tmp
            tmp = []
            cnt += 1
            continue

        elif arr[i] == 0:
            result.append(cnt + 1)
            cnt += 1
            continue

        else:
            cord = len(result)
            for k in range(len(result)):
                if cord == arr[i]:
                    tmp.append(cnt + 1)


                cord -= 1
                tmp.append(result[k])

            result = tmp
            tmp = []
            cnt += 1

    print(*result)
    # for l in range(len(result)):
    #     print(result[l], end  = ' ')

line()




