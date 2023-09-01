# 슬라이딩 윈도우(sliding window)
# 1. 주로 리스트와 같은 시퀀스 타입에서 일 정 크기의 '윈도우'를 정한다
# 2. 그 휜도우를 데이터의 처음부터 끝까지 움직이면서 해결한다
'''
n개의 정수를 입력받고, 연속된 m개의 정수들의 합을 구할때 최대값 구하기
합이 가장 큰 구간의 값은 무엇일까요? (2 <= m, n <= 100,000)

input
10 2
3 -2 -4 -9 8 3 7 13 8 -3

output
21

'''

# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
#
# maxi = 0
# for i in range(0, n):
#     if maxi < sum(arr[i:i+m]):
#         maxi = sum(arr[i:i + m])
#
# print(maxi)

'''
# 강사님 풀이
n, m = map(int, input().split())
arr = list(map(int, input().split()))
sum = 0
for i in range(m): # 처음 첫 m개의 구간의 합 구하기
    sum += arr[i]
    MAX = sum
for i in range(n-m):
    sum += arr[i + m]
    sum -= arr[i]
    if sum > MAX:
        MAX = sum
print(MAX)
'''

# 투 포인터(two pointer)
'''
1부터 10000 사이의 n개의 자연수 중에서 연속된 숫자를 더했을때 합이 m이 되는 경우는 몇가지 인가요?
(투포인터 -> 구간의 크기가 정해지지 x )

input
10 5
1 2 3 4 2 5 3 1 1 2

output
3
'''
# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# cnt = 0
#
# for i in range(n):
#     ch = 0
#     ch = arr[i]
#     if ch == m:
#         cnt += 1
#         continue
#     for j in range(i + 1, n):
#             ch += arr[j]
#             if ch == m:
#                 cnt += 1
#                 break
#
# print(cnt)
'''
# 강사님 풀이
n, target = map(int, input().split())
arr = list(map(int, input().split()))
cnt, sum = 0, 0
# 투 포인터 high, low
high, low = 0, 0
while True:
    if sum >= target or high == n:     #합이 타겟보다 크거나 같다면(범위 좁히기)
        sum -= arr[low]
        low += 1
    elif sum < target:    # 합이 타겟보다 작다면 범위 넓히시
        sum += arr[high]
        high += 1
    if sum == target:
        cnt += 1
    if low == n:
        break
print(cnt)
'''