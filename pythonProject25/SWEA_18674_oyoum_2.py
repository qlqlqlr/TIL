# 강사님 풀이 오염수 정화

# 투 포인터로 풀기

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
# 투 포인터 초기화
left = 0
right = n - 1
# 변수 초기화
minimum = 2e9 + 1
ansleft = 0
ansright = 0
while left < right:
    sum = arr[left] + arr[right] # 합구하기
    # 합이 0이면 두수를 출력하고 프로그램 종료
    if sum == 0:
        print(arr[left], arr[right])
        exit()    # break 와 exit() 의 차이는 exit는 프로그램 자체를 완전히 종료한다.
    # 절대값을 이용해서 최소 차이를 찾기
    if minimum > abs(sum):
        minimum = abs(sum)
        ansleft = left
        ansright = right
    #합이 0보다 크면 right를 줄이고, 합이 0보다 작으면 left를 늘린다.
    if sum > 0: right -= 1
    else: left += 1

print(arr[ansleft], arr[ansright])

