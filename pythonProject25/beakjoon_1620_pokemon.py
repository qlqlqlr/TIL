# 포켓몬 문제
# 리스트를 사용하면 2중 포문 을 사용해야한다. 딕셔너리를 사용하면 반복 횟수를 줄일 수 있다.

N, M = map(int, input().split())
dic = {}
dic2 = {}
for i in range(1, N + 1):
    pokemon = input()
    dic[i] = pokemon
    dic2[pokemon] = i
for _ in range(M):
    x = input()
    if x.isdigit():
        print(dic[int(x)])
    else:
        print(dic2[x])




