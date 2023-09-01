#
# def f (i, N):       # i 현재 상태, N 목표
#     if i == N:
#         print(B)
#         return
#     else:
#         B[i] = A[i]
#         f(i + 1, N)
#
# N = 5
# A = [1, 2, 3, 4, 5]
# B = [0] * N
# f(0, N)

# # key가 있으면 1, 없으면 0을 리턴하는 함수
# def f(i, N, key, arr):
#     if i == N:
#         return 0          # key가 없는 경우
#     elif arr[i] == key:
#         return 1
#     else:
#         f(i + 1, N, key, arr)
#
# N = 5
# A = [1, 2, 3, 4, 5]
# key = 3
# f(0, N, key, arr)


# 선택 정렬 함수를 재귀적 알고리즘으로 작성해보자




#
# def f(i, N):
#     if i == N:    # 순열 완성
#         print(p)
#         return
#     else:      # p[i] 에 들어갈 숫자를 결정
#         for j in range(N):
#             if used[j] == 0:    # 아직 사용되기 전이면
#                 p[i] = card[j]
#                 used[j] = 1
#                 f(i + 1, N)
#                 used[j] = 0
#
# card = list(map(int, input()))
# used = [0] * 6    # 이미 사용한 카드인지 표시
# p = [0] * 6
# f(0, 6)
#
#
# def f(i, N):
#     if i == N:    # 순열 완성
#         print(p)
#         return
#     else:      # p[i] 에 들어갈 숫자를 결정
#         for j in range(N):
#             if used[j] == 0:    # 아직 사용되기 전이면
#                 p[i] = card[j]
#                 used[j] = 1
#                 f(i + 1, N)
#                 used[j] = 0
#
# card = [1, 2, 3]
# used = [0] * 3    # 이미 사용한 카드인지 표시
# p = [0] * 3
# f(0, 3)



# 그룹 나누기...

a = [1, 2, 3, 4]
N = 4

# for i in range(1, (1 << N) - 1):
for i in range(1, 1 << (N - 1)):     # 1 << (N - 1) == (i << N) // 2
    subset1 = []
    subset2 = []
    total1 = 0
    total2 = 0
    for j in range(N):
        if i & (1 << j):    # j번 비트가 0이 아니면
            subset1.append(a[j])
            total1 += a[j]
        else:
            subset2.append(a[j])
            total2 += a[j]

    print(subset1, subset2)