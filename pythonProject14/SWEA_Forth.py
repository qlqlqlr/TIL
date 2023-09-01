
# SWEA Forth 다시 풀기

T = int(input())
for tc in range(1, T + 1):
    forth = list(input().split())
    stack = []
    error = False
    for k in range(len(forth) - 1):
        if forth[k].isdigit():
            stack.append(forth[k])
        else:
            try:
                b = int(stack.pop())
                a = int(stack.pop())
                if forth[k] == '+':
                    ans = a + b
                elif forth[k] == '-':
                    ans = a - b
                elif forth[k] == '*':
                    ans = a * b
                elif forth[k] == '/':
                    ans = a // b

                stack.append(ans)
            except:
                error = True

    if error == True or len(stack) != 1:
        print(f'#{tc} error')

    else:
        print(f'#{tc} {stack[0]}')