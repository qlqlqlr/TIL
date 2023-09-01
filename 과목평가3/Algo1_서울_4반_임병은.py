

directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]            # 상하좌우 방향배열

T = int(input())

for tc in range(1, T +1):
    N = int(input())
    space = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            find_max = []                        # 상하좌우 인접지역의 높이를 임시적으로 담는 리스트
            im_max = 0                           # 현재위치에서 인접 지역값중 최대값을 임시로 저장
            for dx, dy in directions:
                nx = i + dx                      # 방향배열을 통해 인접지역을 탐색
                ny = j + dy
                if 0 <= nx < N and 0 <= ny < N:       #인접 지역의 좌표가 전체 space 안에 들어오는 좌표인지 확인
                    find_max.append(space[nx][ny])     # 존재하는 좌표라면 리스트에 값을 담는다
            for k in range(len(find_max)):             # 인접 지역값들 중 최대값을 구한다
                if find_max[k] > im_max:
                    im_max = find_max[k]
            if im_max < space[i][j]:
                result += 1                            # 현재위치의 값이 인 접 지역들 보다 크다면 봉우리 이므로 +1

    print(f'#{tc} {result}')
