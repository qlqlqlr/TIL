# 크로스워드 만들기


A, B = input().split()

Aline = 0
Bline = 0
result = []
space = [['.']*len(A) for _ in range(len(B))]

def point(A, B):
    cnt = 0
    for i in range(len(A)):
        for j in range(len(B)):

            if A[i] == B[j] and cnt == 0:
                Aline = i
                Bline = j
                cnt += 1




    return Aline, Bline

def draw(A, B, Aline, Bline):
    for l in range(len(A)):
        space[Bline][l] = A[l]

    for zz in range(len(B)):
        space[zz][Aline] = B[zz]


Aline, Bline = point(A, B)
draw(A, B, Aline, Bline)

for row in space:
    print(*row, sep = '')