




T = int(input())
result = 0
for t in range(T):
    ans = 0
    stack = []
    str1 = input()
    for i in range(len(str1)):
        if len(stack) > 1:
            for j in range(len(stack)):
                if stack[j] == str1[i] and j != len(stack) - 1:
                    ans = -1
                else:
                    stack.append(str1[i])
        else:
            stack.append(str1[i])

    if ans == 0:
        result += 1

print(result)



