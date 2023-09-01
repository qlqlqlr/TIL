# def f(i, N):
#     if i == N:
#         return
#     else:
#         B[i] = A[i]
#         f(i+1, N)
#         return
#
# N = 3
# A = [1, 2, 3]
# B = [0] * N
#
# f(0, N)
# print(B)

#
# def f(i, N):
#     if i == N:
#         print(bit)
#         return
#     else:
#         bit[i] = 1
#         f(i+1, N)
#         bit[i] = 0
#         f(i+1, N)
#         return
#
# A = [1, 2, 3]
# bit = [0] * 3
# f(0, 3)



#
# def f(i, N, s):                # i-1 원소까지 부분집합의 합
#     if i == N:
#         print(bit, end = ' ')
#         print(f' : {s}')
#         return
#     else:
#         bit[i] = 1               # 부분집합에 A[i] 포함
#         f(i+1, N, s+A[i])
#         bit[i] = 0               # 부분집합에 A[i] 빠짐
#         f(i+1, N, s)
#         return
#
# A = [1, 2, 3]
# bit = [0] * 3
# f(0, 3, 0)



#
# def f(i, N, s):                # i-1 원소까지 부분집합의 합
#     if i == N:
#         if s == 10:
#             print(bit)
#         return
#     else:
#         bit[i] = 1               # 부분집합에 A[i] 포함
#         f(i+1, N, s+A[i])
#         bit[i] = 0               # 부분집합에 A[i] 빠짐
#         f(i+1, N, s)
#         return
#
#
# # 1 부터 10 까지 원소인 집합, 부분집합의 합이 10인 경우는?
# N = 10
# A = [i for i in range(1, N + 1)]
# bit = [0] * N
# f(0, N, 0)



#
#
#

def f(i, N, s, t):                # i-1 원소까지 부분집합의 합
    global cnt
    cnt += 1
    if s == t:
        if s == 10:
            print(bit)
        return
    elif i == N:                       # 남은 원소가 없는경우
        return

    else:
        bit[i] = 1               # 부분집합에 A[i] 포함
        f(i+1, N, s+A[i], t)
        bit[i] = 0               # 부분집합에 A[i] 빠짐
        f(i+1, N, s, t)
        return


# 1 부터 10 까지 원소인 집합, 부분집합의 합이 10인 경우는?
cnt = 0
N = 10
A = [i for i in range(1, N + 1)]
bit = [0] * N
f(0, N, 0, 10)
print(cnt)




#
# def f(i, N):
#     if i == N:
#         print(A)
#     else:
#         for j in range(i, N):    # 자신부터 오른쪽끝까지
#             A[i], A[j] = A[j], A[i]
#             f(i+1, N)
#             A[i], A[j] = A[j], A[i]
#
#
# A = [1, 2, 3]
# f(0, 3)




# # 거듭제곱
#
# def f1(b, e):
#     if b == 0:
#         return 1
#     r = 1
#     for i in range(e):              # 연산량 e번 반복
#         r *= b
#
#     return r
#
# def f2(b, e):                       # 재귀 호출량 4
#     if b == 0 or e == 0:
#         return 1
#     if e % 2 == 1:
#         r = f2(b, (e - 1) // 2)
#         return r * r * b
#     else:
#         r= f2(b, e // 2)
#         return r * r
#
#
# print(f1(2, 10))
# print(f2(2, 10))                       # 값은 같지만 연산량 or 호출횟수가 다르다


