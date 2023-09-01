# 8/3 알고리즘 4일차 라이브 강의
# bit로 부분집합을 생성하는 방법

#
# def print_subset(bit, arr, n):
#     total = 0    # 부분집합의 합
#     for i in range(n):
#         if bit[i]:
#             print(arr[i], end = ' ')        # 부분 집합의 원소들을 출력
#             total += arr[i]
#     print(bit, total)                     # 부분집합 생성 비트와 원소들의 합을 출력
#
#
# arr = [1, 2, 3, 4]
# bit = [0, 0, 0, 0]
#
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] =k
#             for l in range(2):
#                 bit[3] = l
#                 print_subset(bit, arr, 4)     # 생성된 부분집합 출력

#
# # arr = [3, 6, 7, 1, 5, 4]
# arr = [1, 2, 3]
#
# n = len(arr)        # n : 원소의 개수
#
# for i in range(1 << n) :        # 1<<n : 부분집합의 개수     2^n
#     for j in range(n):        # 원소의 수만큼 비트를 비교함
#         if i & (1 << j):         # i의 j번 비트가 1인경우
#             print(arr[j], end = ', ')        # j 번 원소 출력
#     print()
# print()

#
#
# # 이진 탐색
# def binarySearch(a, N, key)
#     start = 0
#     end = N -1
#     while start <= end:
#         middle = (start + end) // 2
#         if a[middle] == key:  # 검색 성공
#             return True
#         elif a[middle] > key:
#             end = middle - 1
#         else:
#             start = middle + 1
#
#     return False                 # 검색 실패


