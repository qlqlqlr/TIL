T = int(input())

for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    curr, cnt = 0, 0

    while curr != N:
        if N <= curr + K:
            curr = N
            break

        for i in range(len(arr)-1, -1, -1):
            #리스트에서 arr의 값이 curr + K 이내에 있다면
            if arr[i] <= curr + K:
                cnt += 1        # 충전 횟수 증가
                curr = arr[i]    # 현재위치 충전소로 이동
                arr = arr[i+1:]   # 현재 충전호 이후 정류장만 남기기
                break
            if i == 0:
                cnt = 0
                curr = N    # 현재위치를 종점으로 하여 while 탈출
    print(f'#{tc} {cnt}')