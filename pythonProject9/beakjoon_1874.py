

N = int(input())
arr = list(int(input())for _ in range(N))
result = ''
stack = []
j = 0
for i in range(1, N + 1):
    if i != arr[j]:
        stack.append(i)
        result += '+'

    elif i == arr[j]:
        result += '+'
        result += '-'
        j += 1
        while len(stack) != 0:

            if stack[-1] == arr[j]:
                stack.pop()
                result += '-'
                j += 1
            else:
                break
if j < N:
    print('NO')
else:
    for l in range(len(result)):
        print(result[l])

