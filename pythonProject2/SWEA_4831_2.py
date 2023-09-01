T = int(input())

for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    # 정류장 만들기
    ch = [0] * (N + 1)
    # 충전소 넣기
    for i in arr:
        ch[i] += 1
    current = 0   # 현재 위치
    count = 0     # 충전 횟수
    while current < N:
        # 갈 수 있는 최대 거리 계산
        if ch[current + K]:
            current += K
            count += 1

        #충전소 찾기
        else:
            for j in range(1, K):
                # 충전소를 찾으면 충전, count 증가
                if ch[current + K - j]:
                    current += K - j
                    count += 1
                    break
                # 충전소가 없으면, count = 0, 반복 종료
            else:
                count = 0
                break

        # 최대거리가 도착점 보다 멀거나 같으면 , 반복종료
        if current + K >= N:
            current = N

    print(f'#{tc} {count}')
