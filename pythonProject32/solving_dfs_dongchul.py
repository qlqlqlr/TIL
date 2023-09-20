# 솔빙 클럽 동철이의 일분배 dfs

# 현재 직원(n), 일 할당 받은 직원 리스트(items), 현재까지 성공확률(total)
def dfs(n, items, total):
    global ans
    # 현재의 확률이 이미 알려진 최대 확률보다 낮으면 탐색 x
    if total <= ans:
        return
    # 모든 직원에게 일이 할당되면 최대확률 갱신
    if n == N:
        ans = max(ans, total)
        return
    for i in range(N):
        if i not in items: # 해당 직원이 아직 일을 할당받지 않았다면
            items.append(i) # 일 할당하고
            dfs(n + 1, items, total * (arr[n][i] / 100))
            items.pop() # 백 트래킹: 일을 할당 해제

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    dfs(0, [], 1)  # 첫 번째 직원부터 시작하여 dfs 호출
    result = round(ans * 100, 6)
    print(f'#{tc} {result:.6f}')  # 소수 6번째 까지 출력