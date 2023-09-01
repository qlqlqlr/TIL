

T = int(input())

for tc in range(1, T+1):
    sik = list(input())
    N = len(sik)

    def check(N, sik):
        stack = []  # 괄호들을 저장할 스택
        result = 0
        poped = ''
        for i in range(N):
            if sik[i] == '(' or sik[i] == '{':
                stack.append(sik[i])

            elif sik[i] == ')':
                poped = stack.pop()
                if poped == '(':
                    num_stack = []
                    j = i - 1
                    while True:

                        if sik[j] == '(':
                            while num_stack:
                                result += num_stack.pop()

                            break
                        else:
                            num_stack.append(int(sik[j]))
                            j -= 1
                else:
                    return -1

            elif sik[i] == '}':
                poped = stack.pop()
                if poped == '{':
                    num_stack = []
                    j = i - 1
                    while True:

                        if sik[j] == '(':
                            while num_stack:
                                result *= num_stack.pop()

                            break
                        else:
                            num_stack.append(int(sik[j]))
                            j -= 1
                else:
                    return -1


        if stack:
            return -1
        else:
            return result

    ans = check(N,sik)
    print(ans)