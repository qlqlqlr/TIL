'''
6528-*2/+
'''
#
# stack = [0] * 100
# top = -1
# susik = '6528-*2/+'
# for x in s:
#     if x not in '+-/*': # 피연산자면
#         top += 1            # push(x)
#         stack[top] = int(X)
#     else:
#         op2 = stack[top]
#         top -= 1
#         op1 = stack[top]
#         top -= 1
#         if x == '+':    # op1 + op2
#
#             top += 1
#             stack[top] = op1 + op2
#         elif x == '-':
#
#             top += 1
#             stack[top] = op1 - op2
#         elif x == '/':
#
#             top += 1
#             stack[top] = op1 / op2
#         elif x == '*':
#             top += 1
#             stack[top] = op1 * op2


stack = [0]* 100
top = -1
icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}


fx = '(6+5*(2-8)/2)'

susik = ''
for x in fx:
    if x not in '(+-*/)':
        susik += x
    elif x == ')':
        while stack[top] != '(':
            susik += stack[top]
            top -= 1
        top -= 1

    else:
        if top == -1 or isp[stack[top]] < icp[x]:
            top += 1
            stack[top] = x
        elif isp[stack[top]] >= icp[x]:
            while top > -1 and isp[stack[top]] >= icp[x]:
                susik += stack[top]
                top -= 1
            top += 1
            stack[top] = x

print(susik)