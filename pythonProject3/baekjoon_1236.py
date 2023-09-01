
N, M = map(int, input().split())
arr = [list(map(str, input())) for _ in range(N)]
answer = 0

def castle():
    result = 0
    cnt3 = 0
    for i in range(N):
        im = 0
        cnt = 0
        cnt2 = 0
        for j in range(M):
            if arr[i][j] == 'X':
                cnt += 1




        if cnt == 0:
            for k in range(M):
                cnt2 = 0
                for z in range(N):
                    if arr[z][k] == 'X':
                        cnt2 += 1

                if cnt2 == 0:
                    arr[i][k] = 'X'
                    result += 1
                    break
            else:
                arr[i][i] = 'X'
                result += 1
                continue


    for z in range(M):
        cnt3 = 0
        for zz in range(N):
            if arr[zz][z] == 'X':
                cnt3 += 1
        if cnt3 == 0:
            arr[im][z] = 'X'
            result += 1
            im += 1
            # print(arr)




    return result


answer = castle()
# print(arr)
print(answer)






