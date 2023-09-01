# 강사님 풀이

def DFS(idx, now_sum):
    global min_sum
    if now_sum >= min_sum:    # 현재 합이 최소합보다 크거나 같으면 탐색 x
        return
    if idx == N:    # 모든 행을 선택
        if min_sum > now_sum:
            min_sum = now_sum     # 모든 행을 선택했으면 , 현재합이 최소합보다 작을때 없데이트
            return

    for i in range(N):
        if not used[i]:
            used[i] = 1
            DFS(idx + 1, now_sum + arr[idx][i])   # 행을 다음 행으로 넘어가면서 재귀 호출
            used[i] = 0   # 복구 (백트래킹)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    min_sum = 21e8
    DFS(0, 0)
    print(f'#{tc} {min_sum}')