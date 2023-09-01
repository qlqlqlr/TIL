# SWEA 4873. 반복문자 지우기

T = int(input())
for tc in range(1, T + 1):
    arr = list(input())
    i = 0
    stk = []
    result = 0
    while i < len(arr):
        if stk == []:
            stk.append(arr[i])
            i += 1

        else:
            if arr[i] == stk[-1]:
                stk.pop()
                i += 1
            else:
                stk.append(arr[i])
                i += 1

    print(f'#{tc} {len(stk)}')







