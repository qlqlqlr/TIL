# 강사님 풀이

T = int(input())

for tc in range(1, T+1):
    N = int(input())    # 방의 가로길이
    arr = list(map(int, input().split()))
    max = 0

    # 방의 가로길이 만큼 반복
    for i in range(N):
        cnt = 0
        # 현재 위치의 상자가 오른쪾에 있는 모든 상자를 확인
        for j in range(i + 1, N):
            # 현재 위치의 상자가 오른쪽의 상자보다 높이가 크면
            if arr[i] > arr[j]:
                cnt += 1

        # 최대값
        if max <= cnt:
            max = cnt

    print(f'#{tc} {max}')