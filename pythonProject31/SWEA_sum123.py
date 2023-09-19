def count_ways_to_sum(n):
    # 결과를 저장할 변수
    count = 0

    # 백트래킹 함수 정의
    def backtrack(current_sum, path):
        nonlocal count
        if current_sum == n:
            # 현재 합이 목표 값과 같다면 경우의 수를 하나 증가
            count += 1
        elif current_sum < n:
            # 현재 합이 목표 값보다 작다면 1, 2, 3을 선택하여 재귀 호출
            for num in [1, 2, 3]:
                path.append(num)
                backtrack(current_sum + num, path)
                path.pop()  # 백트래킹

    backtrack(0, [])  # 백트래킹 함수 호출

    return count


# 예제 테스트
n = int(input())
result = count_ways_to_sum(n)
print(result)
