# 문자메시지

keys = [[' '],
        ['A', 'B', 'C'],
        ['D', 'E', 'F'],
        ['G', 'H', 'I'],
        ['J', 'K', 'L'],
        ['M', 'N', 'O'],
        ['P', 'Q', 'R', 'S'],
        ['T', 'U', 'V'],
        ['W', 'X', 'Y', 'Z']
        ]

p, w = map(int, input().split())
# p 버튼을 한번 누르는데 걸리는 시간 , w 같은 버튼을 연속으로 찍기 위해 기다리는 시간
mas = str(input())
result = 0

def cal(mas, keys):
    cnt = 0
    for k in range(len(mas)):
        for i in range(len(keys)):
            for j in range(len(keys[i])):
                if keys[i][j] == mas[k]:
                    cnt += p * (j + 1)

                    if k < (len(mas)-1):
                        if mas[k + 1] in keys[i] and i != 0:
                            cnt += w
                    break


    return cnt

result = cal(mas, keys)
print(result)




