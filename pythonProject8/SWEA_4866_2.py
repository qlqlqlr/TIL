
T = int(input())
for tc in range(1, T + 1):
    text = input()
    stack = []
    for i in text:
        if i == '{' or i == '(':
            stack.append(i)

        # 여는 괄호가 있는 상태여야만 함으로 stack 이 참이여야함
        elif stack and i == '}' and stack[-1] == '{':
            stack.pop()

        elif stack and i == ')' and stack[-1] == '(':
            stack.pop()

        # 닫는 괄호인데 짝이 맞지 않음 -> 스택에 추가
        elif i == '}' or i ==')':
            stack.append(i)

    if stack:
        result = 0

    else:
        result = 1

    print(f'#{tc} {result}')