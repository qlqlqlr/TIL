# 솔클 힙 금나와라 황금보자기

import heapq
N = int(input())
arr = list(map(int, input().split()))
que = []  # 황금과 짱돌을 저장할 최소 힙
cnt = 0 # 황금의 개수
for i in range(N):  # 입력받은 황금의 무게들을 최소 힙에 추가
    heapq.heappush(que, [arr[i], -1])  # 각 황금의 무게와 -1(황금을 의미)을 저장
while que:  # 힙에  요소가 있을때 까지 반복
    x, tp = heapq.heappop(que)  # 1.힙에서 가장 가까운 돌을 꺼낸다
    if tp == 0:   # 꺼낸 돌이 짱돌이면
        break
    cnt += 1  # 황금 꺼냈으므로 카운트 증가

    y, tp = heapq.heappop(que)  # 2. 다음 가장 가까운 돌을 꺼냈다.
    if tp == 0:
        break
    else: # 꺼낸 돌이 황금이면
        heapq.heappush(que, [y*2, 0])  # 황금의 2배의 무게의 짱돌을 힙에 추가
    cnt += 1  # 황금을 꺼냈으므로 카운트 증가

print(cnt)