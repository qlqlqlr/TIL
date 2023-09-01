# 삼성시의 버스노선 IM 대비

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    stop = [0] * 5001   # 1번부터 5000번까지 정류장
    for i in range(N):
        ai, bi = map(int, input().split())
        # 해당 정류장에 지나는 버스 대수 누적
        for j in range(ai, bi + 1):
            stop[j] += 1

    P = int(input())
    result = []
    for j in range(P):
        cj = int(input())
        result.append(stop[cj])   # 각 정류장에 지나는 버스 노선 수

    print(f'#{tc}', *result)