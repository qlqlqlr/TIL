
T = int(input())

for tc in range(1, T+1):
    sik = list(input())
    N = len(sik)

    def check(sik, N):
        stack = []  # 괄호들을 저장할 스택
        num_stack = []
        result = 0
        poped = ''
        i = 0
        while i < N:

            if sik[i] == '(' or sik[i] == '{':
                stack.append(sik[i])
                i += 1
                while 1 < N:
                    if sik[i] != '(' and sik[i] != '{' and sik[i] != ')' and sik[i] != '}':
                        num_stack.append(int(sik[i]))
                        i += 1
                    else:
                        if sik[i] == ')':
                            poped = stack.pop()
                            if poped == '(':
                                result = 2
                                i += 1
                            else:
                                result = -1
                                break
                        elif sik[i] == '}':
                            poped = stack.pop()
                            if poped == '{':
                                result = 2
                                i += 1
                            else:
                                result = -1
                                break
                        else:
                            result = -1
                            break
                break
            else:
                result = -1
                break
        if stack:
            result = -1
        print(result)