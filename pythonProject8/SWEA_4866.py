
T = int(input())
arr = []
result = 1

def push(a, arr):
    arr.append(a)


for tc in range(1, T+1):
    str1 = input()

    for i in range(len(str1)):
        if str1[i] == '(':
            push(str1[i], arr)

        elif str1[i] == '{':
            push(str1[i], arr)


        elif str1[i] == ')':
            if arr.pop() != '(':
                result = 0
            else:
                continue


        elif str1[i] == '}':
            if arr.pop() != '{':
                result = 0
            else:
                continue

    print(f'#{tc} {result}')



