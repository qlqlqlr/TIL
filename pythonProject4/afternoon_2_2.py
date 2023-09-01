

#빙고판 입력받기
board = [int(num) for _ in range(5) for num in input().split()]
# 사회자 숫자 부르기
call = [int(num) for _ in range(5) for num in input().split()]
cnt = 0
# 가로, 세로, 대각선 빙고를 체크하기 위한 리스트
x_lst = [0] * 10
y_lst = [0] * 10
di_lst1 = [0] * 10
di_lst2 = [0] * 10

for n in call:
    #부른 숫자의 인덱스 받기
    a = board.index(n)
    # 인덱스를 ㅎ이용해 해당 숫자의 위치 x, y 계싼
    x, y = a // 5, a % 5
    # 가로, 세로, 대각선 빙고 개수 카운트 증가
    x_lst[x] += 1
    y_lst[y] += 1
    di_lst1[x + y] += 1
    di_lst2[y - x + 4] += 1
    # 빙고 개수를 확인하여 cnt 증가
    if x_lst[x] == 5:
        cnt += 1
    if y_lst[y] == 5:
        cnt += 1
    if di_lst1[x + y] == 0 and di_lst2[y - x + 4] == 5:
        cnt += 1

    # cnt 가 3이되면, 3선빙고 완성 n 출력하고 반복문 종료
    if cnt == 3:
        print(n)
        break