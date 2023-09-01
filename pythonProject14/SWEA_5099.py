# SWEA 5099. 피자굽기   강사님 풀이

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int,input().split())
    cheeses = list(map(int, input().split()))   #각 피자의 초기 치즈 양
    # 피자 인덱스(피자 번호), 치즈의 양
    pizzas = [[i + 1, p] for i, p in enumerate(cheeses)]   # 번호하고 치즈의 양이 튜플형태로 저장됌
    oven = pizzas[:N]            # 화덕에 넣는 피자들
    remain = pizzas[N:]              # 화덕에 넣지 않은 남아있는 피자

    while len(oven) > 1:    # 화덕에 남은피자가 1개 남을 때 까지 반복
        now = oven.pop(0)   # 화덕에서 피자를 꺼냄
        #now[0] : 현재 피자의 인덱스 번호 , now[1] : 현재 피자의 치즈 양
        now[1] //= 2                              # 치즈의 양을 반으로 줄이기
        if now[1] == 0:                             # 치즈가 모두 녹았다면
            if remain:                               # 아직 피자가 남아있다면 화덕에 넣는다
                oven.append(remain.pop(0))
        else:                                        # 치즈가 아직 안녹았으면
            oven.append(now)                        # 다시 화덕에 넣음

    # 화덕에 마지막 남은 피자의 인덱스 번호
    print(f'#{tc} {oven[0][0]}')