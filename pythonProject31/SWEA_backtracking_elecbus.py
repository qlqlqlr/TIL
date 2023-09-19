# SWEA 솔빙클럽 백트래킹 전기버스2

def min_battery_changes(N, battery_capacities):
    def backtrack(current_station, battery_charge, changes):
        nonlocal min_changes

        if current_station == N:  # 마지막 정류장에 도착한 경우
            min_changes = min(min_changes, changes)
            return

        if changes >= min_changes:  # 현재까지의 교환 횟수가 이미 최소 횟수를 초과한 경우
            return

        # 배터리를 더 사용하지 않고 다음 정류장으로 이동
        if battery_charge > 0:
            backtrack(current_station + 1, battery_charge - 1, changes)

        # 배터리를 교환하고 다음 정류장으로 이동
        for i in range(1, battery_capacities[current_station - 1] + 1):
            if current_station + i <= N:
                backtrack(current_station + i, battery_capacities[current_station - 1] - i, changes + 1)

    min_changes = float('inf')
    backtrack(1, battery_capacities[0], 0)  # 출발 정류장에서 충전하지 않고 시작

    return min_changes

T = int(input())
for tc in range(1, 1 + T):
    N, *battery_capacities = map(int, input().split())

    # 최소 배터리 교환 횟수 계산
    result = min_battery_changes(N, battery_capacities)
    print(f'#{tc} {result}')

