# 백준 14696. 딱지놀이 IM 대비


N = int(input())

for i in range(N):
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    A = [0] * 5
    B = [0] * 5
    result = 0
    for j in range(1, len(arr1)):
        A[arr1[j] - 1] += 1

    for k in range(1, len(arr2)):
        B[arr2[k] - 1] += 1


    for l in range(4, -1, -1):
        if A[l] == B[l]:
            continue

        elif A[l] < B[l]:
            print('B')
            result = 1
            break
        elif A[l] > B[l]:
            print('A')
            result = 1
            break

    if result == 0:
        print('D')
