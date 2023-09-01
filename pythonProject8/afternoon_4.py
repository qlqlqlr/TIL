# 양의 정수 N이 주어지면 N의 모든 자릿수를 합한 값을 출력하는 프로그램을 재귀함수로 작서앻보자


N = int(input())

def Hab(N):
    if (N//10) == 0:
        return N % 10

    else:
        return (N % 10) + Hab(N // 10)


print(Hab(N))