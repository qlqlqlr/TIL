
# 4047. 영준이의 카드 카운팅 IM 대비

def ch():
    S = 13
    D = 13
    H = 13
    C = 13
    have = input()
    i = 0
    while True:
        num = ''
        if not have[i].isdigit():
            num += have[i + 1]
            num += have[i + 2]
            num = int(num)
            if have[i] == 'S':
                S -= 1
            elif have[i] == 'D':
                D -= 1
            elif have[i] == 'H':
                H -= 1
            elif have[i] == 'C':
                C -= 1

        if have[i: i + 3] in have[i + 3:]:
            print(f'#{tc} ERROR')
            break

        if i == len(have) - 3:
            print(f'#{tc} {S} {D} {H} {C}')
            break

        i += 3

T = int(input())
for tc in range(1, T + 1):

    ch()

