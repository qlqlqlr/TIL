# def ncr(n, r):
#     if r == 0:
#         print(tr)
#
#     elif n < r:   # 남은 원소보다 많은 원소를 선택해야 하는경우
#         return    # 불가
#
#     else:
#         tr[r - 1] = a[n - 1]   # a[n - 1] 조합에 포함시키는 경우
#         ncr(n - 1, r - 1)
#         ncr(n - 1, r)          # a[n - 1]을 포함시키지 않는 경우
#
#
# n = 5
# r = 3
# a = [1, 2, 3, 4, 5]
# tr = [0] * r
# ncr(n, r)
#


# # 10 개의 원소 중 3 개를 고르는 조합
#
# for i in range(0, 8):
#     for j in range(i + 1, 9):
#         for k in range(j + 1, 10):
#             print(i, j, k)


# def nCr(n, r, s):
#     if r == 0:
#         print(*comb)
#     else:
#         for i in range(s, n - r + 1):
#             comb[r - 1] = A[i]
#             nCr(n, r - 1, i + 1)
#
#
#
# A = [1, 2, 3, 4, 5, 6]
# N = len(A)
# R = 2
# comb = [0] * R
#
# nCr(N, R, 0)


#
#
# def subset(i, N):
#     if i == N:
#         s  = 0
#         for j in range(N):
#             if bit[j]:
#                 s += arr[j]
#         if s == 0:
#             for j in range(N):
#                 if bit[j]:
#                     print(arr[j], end = ' ')
#             print()
#     else:
#         bit[i] = 1
#         subset(i + 1, N)      # 다음자리 결정하러
#         bit[i] = 0
#         subset(i + 1, N)      # 0으로 결정하고 다음자리 결정하러
#     return
#
#
#
# arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
# N = len(arr)
# bit = [0] * N
# subset(0, N)






N =10
a = [1, 4, 1, 6, 6, 10, 5, 7, 3, 8, 5, 9, 3, 5, 8, 11, 2, 13, 12, 14]

meet = []
for i in range(N):
    meet.append([a[i*2], a[i*2+1]])
meet.sort(key=lambda x:x[1])
meet = [[0, 0]] + meet

s = []
j = 0
for i in range(1, N + 1):
    if meet[i][0] >= meet[j][1]:           # si >= fj
        s.append(i)
        j = i

print(s)