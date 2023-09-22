# 통행료
def dijkstra(start):
    dist[start] = 0 # 시작 노드 최단 거리 distance 0으로 설정
    for _ in range(N + 1):
        min_idx = -1 # 최소 거리 노드의 인덱스
        min_value = float('inf')

        # 아직 방문하지 않은 노드 중에서 최소거리 노드 찾기
        for i in range(N + 1):
            if not visited[i] and dist[i] < min_value:
                min_idx = i
                min_value = dist[i]

        visited[min_idx] = 1 # 최소 거리 노드 방문 처리

        # 최소거리 노드와 연결된 다른 노드들의 거리 갱신
        for i in range(N + 1):
            if arr[min_idx][i] and not visited[i]:
                dist[i] = min(dist[i], dist[min_idx] + arr[min_idx][i])



N, M, K = map(int, input().split())
A, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
p = list(int(input()) for _ in range(K))
