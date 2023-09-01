# 다섯 종류의 카드를 입력받습니다. (0~ 9)
# 각각의 카드들은 다량으로 쌓여있습니다
# 다섯 종류의 숫자 카드에서 4장을 뽑으려고 합니다
# 뽑을 때마다 전에 뽑았던 카드번호와 간격이 3이하로 차이나는
# 중복순열이 몇 가지인지 출력하세요
# 재귀호출을 이용해서 풀어주세요


card = list(input())
path = [0] * 4
cnt = 0

def card_cnt(level):         # level은 현재 받은 카드의 수
    global cnt
    #4장의 카드를 뽑았으면 경우의 수 증가
    if level == 4:
        cnt += 1
        return   # 재귀 호출 종료

    for i in range(5):          # 5개의 카드중 하나 선택
        path[level] = card[i]    # 현재 레벨 경로에 -> 선택한 카드를 저장
        # 연속한 카드 간의 차이가 4 이상이면 > 다음 카드를 선택> 백트래킹
        if int(path[level]) - int(path[level - 1]) >= 4:
            continue
        if int(path[level - 1]) - int(path[level]) >= 4:
            continue

        # 다음 레벨로 재귀 호출
        card_cnt(level + 1)

card_cnt(0)   # 시작 level은 0
print(cnt)
