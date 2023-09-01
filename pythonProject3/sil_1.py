
# map 배열을 하드코딩 해주세요
# 그리고 map에서 대각선 방향의 합이 가장 큰 값이 나오는 좌표(y, x)를 출력하세요
# 단, 대각선 방향의 합을 구하는 sum_1(y, x) 함수를 만들어서 사용해 주세요.
# sum(y,x)는 특정 좌표(y, x)에서 대각선 방향의 합을 반환하는 함수입니다.




map = [[3, 3, 5, 3, 1],
       [2, 2, 4, 2, 6],
       [4, 9, 2, 3, 4],
       [1, 1, 1, 1, 1],
       [3, 3, 5, 9, 2]]

dx = [1, 1, -1, -1]
dy = [1, -1, 1, -1]      #상 하 좌 우 를 구성하는 방향틀
max_v = 0
max_y = 0
max_x = 0

def sum_1(y, x):
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if ny >= 0 and nx >= 0:
            s += map[ny][nx]


    return s


for y in range(0, len(map)):
    for x in range(0, len(map[0])):
        sum_1(y, x)




# for i in range (len(map)):
#     print(map[i])