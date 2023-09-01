# 베이비진 게임

def check_win(cards):
    cnt = [0] * 10
    for num in cards:
        cnt[num] += 1   # 카드의 숫자 세기
    # 트리플릿 확인
    if 3 in cnt:
        return True
    # 런 확인
    for i in range(8):
        if 0 not in cnt[i : i + 3]:
            return True
    return False

T = int(input())
for tc in range(1, T +1):
    all_cards = list(map(int, input().split()))
    p1 = []
    p2 = []
    winner = 0   # 초기 값은 무승부
    for i in range(6):
        p1. append(all_cards[i * 2])
        if len(p1) > 2 and check_win(p1): # 3장 이상일 때만 확인
            winner = 1
            break
        p2.append(all_cards[i * 2 + 1])
        if len(p2) > 2 and check_win(p2):
            winner = 2
            break
    print(f'#{tc} {winner}')



    