T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = input()
    # 숫자의 등장 횟수를 저장할 딕셔너리 생성
    counts = {str(n) : 0 for n in range(10)}
    # 각 숫자 등장 횟수를 세기
    for card in cards:
        counts[card] += 1
    # 벨류 값들(개수) 중 가장 큰 값을 가져옴
    max_count = max(counts.values())
    # max_count와 같은 횟수를 가진 숫자들 중 가장 큰 숫자를 찾는다 -> 키를 num에 벨류는 count 에 저장
    max_number = max([int(num) for num, count in counts.items() if count == max_count])
    print(f'#{tc} {max_number} {max_count}')

