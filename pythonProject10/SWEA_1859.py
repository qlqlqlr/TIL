# swea 5432. 쇠막대기 자르기


T = int(input())
for tc in range(1, T+1):
    str1 = input()
    cnt = 0
    ans = 0
    for i in range(len(str1)):
        if str1[i] == '(':
            cnt += 1
        elif str1[i] == ')':
            if str1[i -1] == '(':
                cnt -= 1
                ans += cnt
            else:
                cnt -= 1
                ans += 1

    print(f'#{tc} {ans}')