# 영준이의 카드 카운팅 (딕셔너리로 풀이) 강사님

# 리스트, 스택, 딕셔너리, 세트 등 다양한 방법이 있음

T = int(input())
for tc in range(1, T + 1):
    card = input()
    check = []
    card_dict = {'S' : 13, 'D' : 13, 'H' : 13, 'C' : 13}  #무늬 별로 남은 카드수를 딕셔너리로 관리
    # 카드정보는 3글자씩 나누어 check 리스트에 넣는다
    for i in range(0, len(card), 3):
        check.append(card[i : i + 3])

    #중복 카드 체크 -> set이용 -> error 출력
    if len(check) != len(set(check)):
        print(f'#{tc} ERROR')
    else:
        #마지막 카드 정보의 첫글자 인덱스는 len(card) - 3
        for i in range(0, len(card) - 2, 3):
            num = card_dict[card[i]] - 1   #해당 무늬 카드수 1개 차감
            card_dict[card[i]] = num        # 딕셔너리에 남은 카드수 업데이트
        print(f'#{tc}', end = ' ')
        print(*card_dict.values())   # 딕셔너리의 value 출력 -> 남은 카드의 수
