# 솔빙클럽 히프 정중앙 대학교

import heapq

max_heap = []
min_heap = []
mid = 500

def push(v):
    if mid > v:
        heapq.heappush(max_heap, -v)
    else:
        heapq.heappush(min_heap, v)

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    push(a)
    push(b)

    if len(max_heap) > len(min_heap):
        heapq.heappush(min_heap, mid)
        mid = -heapq.heappop(max_heap)  # 맥스 힙에서 값을 꺼낼때 -1 을 곱해준다
    elif len(max_heap) < len(min_heap):
        heapq.heappush(max_heap, -mid)
        mid = heapq.heappop(min_heap)
    print(mid)