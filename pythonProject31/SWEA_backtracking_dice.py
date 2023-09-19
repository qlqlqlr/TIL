def backtracking(N, M, path, last_choice):
    # 기저 조건
    if len(path) == N:
        if M == 1:
            print(*path)
        elif M == 2:
            if sorted(path) == path:
                print(*path)
        elif M == 3:
            if len(set(path)) == N and sorted(path) == path:
                print(*path)
        return

    for num in range(1, 7):
        if M == 2 and num < last_choice:
            continue
        # 주사위 던지기
        path.append(num)
        # 다음 재귀 함수 호출
        backtracking(N, M, path, num)
        # 백트래킹
        path.pop()

N, M = map(int, input().split())
path = []
backtracking(N, M, path, 0)
