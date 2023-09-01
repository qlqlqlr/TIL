

arr = ['3', '5', '1', '9', '7']
T = [(input()) for _ in range(4)]

def Right(lst):

    for i in range(4):
        lst.append(lst[i])

    # 리스트 앞쪽의 4개원소 제거
    for _ in range(4):
        lst.pop(0)


def Left(lst):
    lst.append(lst[0])    # 맨 앞의 원소를 맨 뒤에 추가
    lst.pop(0)           # 맨앞의 원소를 제거

for i in range(4):
    if T[i] == 'R':
        Right(arr)

    if T[i] == 'L':
        Left(arr)

print(*arr)