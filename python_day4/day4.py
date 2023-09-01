# num = int(input('숫자를 입력하세요 : '))

# # if statement
# # num이 홀수라면
# if num % 2 == 1:
#     print('홀수입니다.')
# # num이 홀수가 아니라면(짝수면)
# else:
#     print('짝수입니다.')




# # 0~9 요소를 가지는 리스트 만들기
# # 1. 일반적인 방법
# new_list = []
# for i in range(10):
#     if i % 2 == 1:
#         new_list.append(i)
# print(new_list)

# # 2. list comprehension
# new_list_2 = [i for i in range(10) if i % 2 == 1]
# print(new_list_2)





# # 리스트를 생성하는 3가지 방법 비교
# # 어떤게 제일 빨라요 ?? 

# numbers = ['1', '2', '3']         # 문자열을 정수로 바꾸어 가지는 리스트 만들기 

# # 1. for loop
# new_numbers = []
# for number in numbers:
#     new_numbers.append(int(number))
# print(new_numbers)    #[1, 2, 3]

# # 2. map
# new_numbers_2 = list(map(int, numbers))
# print(new_numbers_2)

# # 3. list comprehension
# new_numbers_3 = [int(number) for number in numbers]
# print(new_numbers_3)



# # enumerate
# result = ['a', 'b', 'c']

# print(enumerate(result))     # <enumerate object at 0x0000014096868D80>
# print(list(enumerate(result)))    # [(0, 'a'), (1, 'b'), (2, 'c')]

# for index, elem in enumerate(result):
#     print(index, elem)





# # 패킹은 여러 value를 하나의 시퀀스로 묶는 과정
# # 예시 1) 
# packing_values = 1, 2, 3, 4, 5
# print(packing_values)         # (1, 2, 3, 4, 5)  튜플로 묶인다. 

# numbers = [1, 2, 3, 4, 5]
# a, *b, c = numbers   #*(애스터리스크) : 패킹연산자로 활용
# print(a)      # 1 
# print(b)      # [2, 3, 4]
# print(c)      # 5

# print('hi', 'hello', 'goodbye', sep = '-')      # 프린트로 패킹
# print('hi', end = ' ')
# print('hello') 

# # *(애스터리스크)를 언패킹 연산자로 활용
# names = ['kai', 'jane', 'bpb']
# print(*names)

# # ** : 딕셔너리 언패킹 연산자
# def my_function(x, y, z):
#     print(x, y, z)
# dict_values = {'x' : 1, 'y' : 2, 'z' : 3}
# my_function(**dict_values)






# # 모듈과 라이브러리는 같은 말일까 ? (x)
# # 라이브러리는 모듈과 패키지의 집합이다. 

# # 모듈 : 한 파일로 묶인 변수와 함수의 모음. 특정하 ㄴ기능을 하는 코드가 작성된 .py 파일

# import math
# print(math.pi)         # 3.141592653589793
# print(math.sqrt(4))    # 2.0

# from math import pi, sqrt
# print(pi)
# print(sqrt(4))

# import random
# print(random.randint(1, 10))

# from random import *      # 모든 모듈을 다 가져오겠다
# print(randint(1, 10))



# # 사용자가 정의한 모듈 사용하기 (my_math.py)
# from my_math import add
# print(add(2, 6))


# from my_package.math import my_math
# from my_package.statistics import tools




# # 외부 패키지 설치 및 사용

# import requests

# url = 'https://random-data-api.com/api/v2/users'
# response = requests.get(url).json()

# print(response)

# # https://jsonviewer.stack.hu/ 사이트에서 복잡한 딕셔너리를 비주얼라이제이션 할수 있따. 
# # United States 를 출력해보자
# print(response.get('address').get('country'))
# print(response['address']['country'])






# 조건문(if문) - 조건식이 참이면 코드를 실행
'''
if 조건식:
    code ... 
elif 조건식:
    code ...
else:
    code ...

'''

# # 조건식에는 비교연산, 논리연산, 멤버연산 등이 들어갈 수 있다. 
# # if의 부정이 elif, elif의 부정이 else 이다. 

# dust = int(input('미세먼지 양을 입력하세요 : '))

# if dust > 150:
#     print('매우 나쁨')
# elif dust > 80:
#     print('나쁨')
# elif dust > 30:
#     print('보통')
# else:
#     print('좋음')

# # 2번째 elif 의 법위는 ?   80 < dust <= 150


# # 실습1. 정수를 입력받아 짝수면 'EVEN' 출력, 홀수면 'ODD'출력
# num = int(input('정수를 입력하시오 : '))

# if num % 2 == 0:
#     print('EVEN')
# else:
#     print('ODD')


# # 실습2. 윤년 판별하기, 윤년이면 'leap year', 그렇지 않으면 'common year'출력
# # 윤년의 조건 1. 연도가 4로 나누어 떨어지지만 100으로는 나누어 떨어지면 안된다
# # 윤년의 조건 2. 연도가 400으로 나누어 떨어진다

# year = int(input('년도를 입력하시오 : '))

# if year % 4 == 0 and year % 100 != 0:
#     print('해당연도는 윤년입니다')
# elif year % 400 == 0:
#     print('해당연도는 윤년입니다')
# else:
#     print('해당연도는 윤년이 아닙니다')


# # 중첩 for 문 실습1. 구구단 출력
# for i in range(1, 9):
#     print(f'< {i}단 >')
#     for j in range(1, 9):
#         print(f'{i} * {j} = {i*j}')


# #실습2. 정수 n을 입력받아 n단의 왼쪽 직각 이등변 삼각형을 그리는 프로그램 작성
# n = int(input())

# for i in range(1, n+1):
#     print('*'*i)


# # 중첩 반복문
# outers = ['A', 'B']
# inners = ['c', 'd']

# for outer in outers:
#     for inner in inners:
#         print(outer, inner)



'''
 # while 문 # 

 초기식
 while 조건식:
    code ...
    증감식

'''

# while 조건식이 참인동안 반복하는 반복문 -> 거짓일 때 까지 반복한다
# 프로그램 종료 조건 만들어야한다

# # 실습1. continue를 이용하여 1부터 10까지 정수중 홀수만 출력하기
# n = 1
# while n <= 10 :
#     if n % 2 == 1:
#         print(n)
#         n += 1
#     else:
#         n += 1
#         continue



# # 실습2. break를 이용하여 'Shall we close? (y/n)' 문구에 y를 입력해야 
# #           반복문을 탈출하고 'The end'를 출력하는 프로그램 작성해 보자

# while True:
#     ans = input('Shall we close? (y/n)')
#     if ans == 'y':
#         print('The end')
#         break


# # 실습 3. 정수를 입력받아 그 정수가 몇 자리수 숫자인지 알아내는 프로그램 작성
# n = int(input('정수를 입력하시오'))
# count = 0

# while n > 0:
#     count += 1
#     n //= 10

# print(count)


# # 실습 1. 271, 272, 273 라인을  list comprehension 으로 수정
# import math
# numbers = [1, 4, 9, 16, 25]

# sqrt_numbers = []
# for numbers in numbers:
#     sqrt_numbers.append(math.sqrt(number))

# print(sqrt_numbers)

# #----------------------------------------------------------

# import math
# numbers = [1, 4, 9, 16, 25]

# sqrt_numbers = [math.sqrt(number) for number in numbers]

# print(sqrt_numbers)




# # 실습 2. if 추가해서 짝수만 추가해보시오
# import math
# numbers = [1, 4, 9, 16, 25]

# sqrt_numbers = [math.sqrt(number) for number in numbers if number % 2 == 0]

# print(sqrt_numbers)



# #enumerate : 인덱스와 함꼐 각 요소를 반환 
# names = ['Kai', 'jane', 'bob']

# for index, name in enumerate(names):
#     print(f'인덱스 : {index} : {name}')

