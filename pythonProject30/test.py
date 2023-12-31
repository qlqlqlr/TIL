# 분할함수(재귀) + 병합함수

# 분할함수

def divide(arr):
    if len(arr) <= 1: #리스트의 길이가 1 이하면 그대로 반환
        return arr

    middle = len(arr) // 2
    left = divide(arr[:middle])   #왼쪽 부분
    right = divide(arr[middle:])  # 오른쪽 부분
    return merge(left, right)


# 병합함수
def merge(left, right):
    global ans
    # 왼쪽 리스트의 마지막 원소가 오른쪽 리스트의 마지막 원소보다 큰경우 answer 1 증가
    if right[-1] < left[-1]:
        ans += 1
    result = [] # 병합결과
    len_l = len(left)
    len_r = len(right)
    l = r = 0
    while l < len_l or r < len_r:
        # 1. 왼쪽과 오른쪽 리스트 모두 남아 있는경우
        if l < len_l and r < len_r:
            if left[l] <= right[r]:
                result.append(left[l]) # 왼쪽의 원소를 result에 추가
                l += 1

            else:
                result.append(right[r]) # 오른쪽의 원소를 result에 추가
                r += 1

        # 2. 왼쪽 리스트만 남아있는 경우
        elif l < len_l:
            result.append(left[l])
            l += 1

        # 3. 오른쪽 리스트만 남아있는 경우
        elif r < len_r:
            result.append(right[r])
            r += 1

    return result

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    result = divide(arr) # 병합 정렬 실행
    print(f'#{tc} {result[N//2]} {ans}')