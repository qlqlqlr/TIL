
# 배관공 카리오

n, L = map(int, input().split())
leaks = list(map(int, input().split()))
# 구멍의 위치 정렬
leaks.sort()
cnt = 1 # 첫 번쨰 구멍을 막기 위해 1로 초기화
cur = leaks[0]  # 첫 번째 구멍 위치 저장
for i in range(1, n):
    if leaks[i] - cur < L:    # 현재 테이프로 다음 구멍을 막을 수 있으면 PASS
        continue
    else:
        # 현재 구멍 위치를 갱신하고, 테이프 개수 1 증가
        cur = leaks[i]
        cnt += 1
print(cnt)