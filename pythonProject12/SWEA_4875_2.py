# swea 4875. 미로  강사님 풀이

def maze():
    while stack:
        y, x = stack.pop()   # 현재위치를 스택에서 꺼냄
        arr[y][x] = -1   # 지나간길 표시
        for i in range(4):   # 4방향 탐색
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if arr[ny][nx] == 3:   # 도착점을 찾은 경우 1반환
                    return 1
                elif arr[ny][nx] == 0:       #갈수 있는곳을 모두 스택에 추가
                    stack.append((ny, nx))  # 튜플

    return 0       # 도착점을 못찾으면 0반환

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    dy = [0, 1, 0, -1]    #세로 방향
    dx = [1, 0, -1, 0]    #가로 방향
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 2:   # 시작점 찾기
                stack = [(y, x)]     # 시작점을 스택에 추가
                break

    print(f'#{tc} {maze()}')