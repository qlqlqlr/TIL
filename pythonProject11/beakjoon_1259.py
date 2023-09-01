def pelin(arr):
    N = len(arr)
    stack = []
    if N % 2 == 0:

        for i in range(N):
            if stack:
                if arr[i] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(arr[i])
            else:
                stack.append(arr[i])

        if stack:
            print('no')

        else:
            print('yes')

    else:
        for i in range(N):
            if i == (N // 2 ):
                continue
            elif stack:
                if arr[i] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(arr[i])
            else:
                stack.append(arr[i])

        if stack:
            print('no')

        else:
            print('yes')


arr = []
while True:
    str1 = input()
    arr.append(str1)

    if arr[-1] == '0':
        arr.pop()

        break

for k in range(len(arr)):
    pelin(arr[k])
