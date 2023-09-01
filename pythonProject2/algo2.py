# # 버블정렬
#
# numbers = [63, 31 , 27, 11, 25]
# def bubble(arr):
#
#     for i in range(len(arr)):
#         for j in range(len(arr) - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
#
# bubble(numbers)
# print(numbers)

#
# # 카운팅 정렬 : 정수를 정렬하는 알고리즘, 각 숫자의 개수를 세어서 정렬
#
# def counting(arr):
#     max_value = max(arr)
#     # 카운트를 저장할 리스트를 만들기위해 최대값을 찾는다
#     count_arr = [0] * (max_value + 1)
#
#     for num in arr:
#         count_arr[num] += 1
#         # 카운트 리스트에 카운트하여 저장.
#
#     sorted_arr = []
#     for i, count in enumerate(count_arr):   # 인덱스와 값을 쌍으로 반환 enumerate
#         sorted_arr.extend([i] * count)   # 이터러블을 추가하므로 extend 사용
#
#     return sorted_arr
#
# list1 = [1, 4, 1, 2, 7, 5, 2]
# sorted_list = counting(list1)
# print(sorted_list)


# # 순열 : 주어진 항목들로 만들수 있는 모든 가능한 순서 (튜플)
# import itertools
#
# arr = [1, 2, 3]
# result = list(itertools.permutations(arr))
# print(result)


# 탐욕 알고리즘 : 각 단계에서 가장 최선의 선택을 하는 방법
# 대표적인 예 : 거스름돈을 줄 떄 가장 적은 수의 동전을 사용하여 거스름돈을 주는 문제
# 최선의 선택 : 가장 큰 단위의 동전부터 사용하는게 최선의 선택이다.
# 실습 1. 동전 종류가 100, 50, 10 원 거스름돈이 380원 이라면? 가장 적은수의 동전 구하기

def greedy(money, coins):
    coins.sort(reverse = True)
    # 거스름 돈의 개수를 저장할 딕셔너리
    change = {coin : 0 for coin in coins}
    for coin in coins:
        while money >= coin:
            money -= coin
            # 해당 코인의 개수를 1 씩 증가
            change[coin] += 1
    return change

result = greedy(380, [100, 50, 10])
print(result)