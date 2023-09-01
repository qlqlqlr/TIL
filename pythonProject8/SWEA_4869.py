
T = int(input())

# f1 = 1, f2 = 3, f3 = 5, f4 = 11 규칙성을 찾아아한다.
# 규칙 : 피보나치와 비슷한데 앞앞 숫자를 두배해서 앞 숫자와 더하면 지금 숫자가 된다
#       fn = fn-2 * 2 + fn-1

def func(n):
    if n % 10 == 0:
        if n == 10:
            return 1
        elif n == 20:
            return 3
        else:
            return func(n-10) + (2 * func(n-20))


for tc in range(1, T +1):
    N = int(input())
    result = func(N)

    print(f'#{tc} {result}')
