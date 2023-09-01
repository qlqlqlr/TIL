# SWEA 1289. IM 보충 대비

T = int(input())

def mem():
    i = 0
    result = 0
    cnt = 0
    while i < len(str1):
        if str1[i] == init[i]:
            i += 1
            continue

        elif str1[i] == '1' and init[i] == '0':
            for j in range(i, len(init)):
                init[j] = '1'
            i += 1
            result += 1

        elif str1[i] == '0' and init[i] == '1':
            for k in range(i, len(init)):
                init[k] = '0'
            i += 1
            result += 1

        for l in range(len(str1)):
            if str1[l] == init[l]:
                cnt += 1

        if cnt == len(str1):
            break


    return result


for tc in range(1, T + 1):
    str1 = list(input())
    init = ['0'] * len(str1)
    result = mem()
    print(f'#{tc} {result}')

