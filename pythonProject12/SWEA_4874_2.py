# swea 4874. forth 강사님 풀이

# error 처리를 위해 try, except 를 사용한다.

T = int(input())
for tc in range(1, T+1):
    forth = list(input().split())
    stack = []
    error = False
    for i in range(len(forth) - 1):      # 마지막 온점 제외
        if forth[i].isdigit():          # 숫자일 경우
            stack.append(forth[i])
        else:                            # 연산자일 경우
            try:
                b = int(stack.pop())
                a = int(stack.pop())
                if forth[i] == '+':
                    ans = a + b
                elif forth[i] == '-':
                    ans = a - b
                elif forth[i] == '*':
                    ans = a * b
                elif forth[i] == '/':
                    ans = a // b

                stack.append(ans)

            except:  # 두개의 숫자를 꺼낼 수 없는경우
                error = True

    if error == True or len(stack) != 1:       # 에러가 트루 = 기호가 더 많거나, 숫자가 더 많은 경우
        print(f'#{tc} error')
    else:
        print(f'#{tc} {stack.pop()}')