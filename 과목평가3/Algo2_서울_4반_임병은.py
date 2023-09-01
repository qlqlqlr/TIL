

T = int(input())


def check(N, sik):  # 괄호검사 함수
    stack = []  # 괄호들을 저장할 스택
    ans = 0  # 괄호가 정상적으로 있을 때 리턴해줄 값
    poped = ''
    for i in range(N):

        if sik[i] == '(' or sik[i] == '{':  # 여는 괄호이면 스택에 넣어둔다
            stack.append(sik[i])

        elif sik[i] == ')':  # 닫는 괄호일 때 스택에서 팝한것과 짝이 맞는지 확인
            poped = stack.pop()
            if poped == '(':
                ans += 1
            else:
                return -1

        elif sik[i] == '}':  # 닫는 괄호일 때 스택에서 팝한것과 짝이 맞는지 확인
            poped = stack.pop()
            if poped == '{':
                ans += 1
            else:
                return -1
        elif i == 0:  # 수식의 처음과 끝은 괄호로 시작해야한다
            if sik[i] != '(' and sik[i] != '{':  # 그렇지 않으면 수식이 계산되지 않으니까
                return -1
        elif i == N - 1:
            if sik[i] != ')' and sik[i] != '}':
                return -1
    if stack:  # 반복문을 나왔을 때 스택에 괄호가 남아있다면
        return -1  # 짝이 맞지 않는 것이므로 -1
    else:
        return ans




for tc in range(1, T+1):
    sik = list(input())
    N = len(sik)
    result = 0


    result = check(N, sik)
    print(f'#{tc} {result}')
