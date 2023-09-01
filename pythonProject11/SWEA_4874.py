# SWEA 4874. Forth

T = int(input())
for tc in range(1, T+1):
    arr = list(input().split())
    stack = []
    result = 0

    for i in range(len(arr)):
        if arr[i] not in '+-/*.':
            stack.append(int(arr[i]))

        else:
            if arr[i] == '.':
                result = stack[0]
                break

            if len(stack) > 1:
                op2 = stack.pop()
                op1 = stack.pop()

                if arr[i] == '+':
                    tmp = op1 + op2
                    stack.append(tmp)

                elif arr[i] == '-':
                    tmp = op1 - op2
                    stack.append(tmp)

                elif arr[i] == '/':
                    tmp = op1 / op2
                    stack.append(tmp)

                elif arr[i] == '*':
                    tmp = op1 * op2
                    stack.append(tmp)

            else:
                result = -1
                break


    if result == -1:
        print(f'#{tc} error')
    else:
        print(f'#{tc} {result}')


