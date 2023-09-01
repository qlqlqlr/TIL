

# 종강파티

n, m = map(int, input().split())
six_min = float('inf')
one_min = float('inf')
for _ in range(m):
    six_cost, one_cost = map(int, input().split())
    # 현재 까지 가장 저렴한 6병 세트와 낱개 가격 업데이트
    six_min = min(six_min, six_cost)
    one_min = min(one_min, one_cost)
if one_min * 6 < six_min:   # 낱개로 사는 것 보다 저렴하면 낱개로 모두 구매
    print(one_min * n)
else:
    buy = n // 6
    n %= 6     # 6으로 나눈 나머지가 남은 병수
    if n * one_min > six_min:    # 낱개로 사는 것이 세트로 사는 것보다 비싸다면
        buy += 1
        print(buy * six_min)
    else:   # 적절히 섞어 최소비용으로 구매
        print(buy * six_min + one_min * n)