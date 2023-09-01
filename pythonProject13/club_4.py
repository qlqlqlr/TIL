from collections import deque

q = deque()
q.append(12)
q.append(9)
q.append(3)
q.append(6)

k = int(input())

Kay = (k // 90) % 4
a, b, c = 0, 0, 0

if Kay == 0:
    print(*q)
else:
    for i in range(Kay):
        a = q.popleft()       # 12
        b = q.pop()           # 6
        c = q.pop()           # 3
        q.append(b)
        q.append(a)
        q.append(c)
    print(*q)


