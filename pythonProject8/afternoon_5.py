# 다섯 종류의 카드를 입력받습니다. (0~ 9)
# 각각의 카드들은 다량으로 쌓여있습니다
# 다섯 종류의 숫자 카드에서 4장을 뽑으려고 합니다
# 뽑을 때마다 전에 뽑았던 카드번호와 간격이 3이하로 차이나는
# 중복순열이 몇 가지인지 출력하세요
# 재귀호출을 이용해서 풀어주세요


N = input()
cards = []
for i in range(5):
    cards.append(int(N[i]))

def path(p):






