# 강사님 풀이

n, m = map(int, input().split())
arr = list(map(int, input().split()))


left, right = 0, 0
sum, cnt = 0, 0

while right <= n:
    # 중간합 sum 이 목표값 m보다 작을경우
    if sum < m:
        if right < n:   # 리스트 범위를 벗어나지 않게
            sum += arr[right]
        right += 1
        # 중간합이 목표값 보다 클 경우
    if sum > m:
        sum -= arr[left]
        left += 1
    # 중간합이 목표값과 같은경우
    if sum == m:
        cnt += 1
        if right < n:
            sum += arr[right]
        right += 1
print(cnt)