# # queue 1
#
# def enQ(item):
#     global rear
#     if rear == Qsize - 1:
#         print('Q is Full')
#     else:
#         rear += 1
#         Q[rear] = item
#
# def deQ():
#     global front
#     if front == rear:
#         print('Q is empty')
#
#     else:
#         front += 1
#         return Q[front]
#
#
# Q = [0] * 3
# Qsize = len(Q)
# rear = -1
# front = -1
#
# enQ(1)
# enQ(2)
# enQ(3)
# enQ(4)
# print(Q)
# print(deQ())
# print(deQ())
# print(deQ())
# print(deQ())


# 스택 : 후입선출
# 데이터 추가 : push, 데이터 삭제 : pop
# DFS에서 활용
# append, pop 사용

# 큐 : 선입선출
# 데이터 추가 : enqueue, 데이터 삭제 : dequeue
# append, pop(0) 사용
#
# # 덱 deque
# from collections import deque
# # deque 양쪽  끝에서 삽입과 삭제가 이루어짐
# d = deque()
# d.append(1)
# d.extend([10, 15, 20])
#
# print(d.popleft())          # 왼쪽끝을 삭제하고 반환
#
# print(d.pop())             # 오른쪽 삭제 반환
# print(d)
#

# for item in d:
#     print(item, end = ' ')


#



