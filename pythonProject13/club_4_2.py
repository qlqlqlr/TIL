from collections import deque

clock = deque([12, 3, 6, 9])
turn = int(input()) // 90
clock.rotate(turn)
print(clock[0],clock[3], clock[1], clock[2])