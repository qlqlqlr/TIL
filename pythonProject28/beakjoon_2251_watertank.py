from collections import deque
# 입력
A, B, C = map(int, input().split())

# BFS
q = deque()

# 초기값
q.append((0, 0, C))
visited = {q[0]}

# 결과를 담을 세트
result = set()

# BFS 시작
while q:
    # a, b, c = 현재 물통에 담긴 물의 양
    a, b, c = q.popleft()

    # a 가 비었을 때 c 의 양을 결과에 저장
    if a == 0:
        result.add(c)

    # 다음 큐에 넣을 값을 저장할 공간
    nxt = []

    # 모든 조건을 검색
    if a > 0:       # 1. a에 물이 들어 있을 때,
        if b < B:   # b의 공간이 남을 때, 남는 공간 = (B - b)
            if a > B - b:       # b의 남는 용량이 a에 남은 물보다 적을 때
                nxt.append((a - (B - b), B, c))     # B의 최대 = B
            elif a <= B - b:    # b의 남는 용량이 a에 남은 물보다 많을 때
                nxt.append((0, b + a, c))
        if c < C:
            if a > C - c:
                nxt.append((a - (C - c), b, C))
            elif a <= C - c:
                nxt.append((0, b, c + a))
    if b > 0:
        if a < A:
            if b > A - a:
                nxt.append((A, b - (A - a), c))
            elif b <= A - a:
                nxt.append((a + b, 0, c))
        if c < C:
            if b > C - c:
                nxt.append((a, B - (C - c), C))
            elif b <= C - c:
                nxt.append((a, 0, c + b))
    if c > 0:
        if a < A:
            if c > A - a:
                nxt.append((A, b, c - (A - a)))
            elif c <= A - a:
                nxt.append((a + c, b, 0))
        if b < B:
            if c > B - b:
                nxt.append((a, B, c - (B - b)))
            elif c <= B - b:
                nxt.append((a, b + c, 0))

    # 큐에 추가하는 단계
    for i in nxt:               # 경우의 수들 중에서
        if i not in visited:    # 물의 용량이 이전에 체크된 적없는 경우만
            visited.add(i)      # 방문기록과 큐에 추가
            q.append(i)

# 결과값을 List로 바꾼 후 정렬, 출력
ans = list(result)
ans.sort()
print(*ans)