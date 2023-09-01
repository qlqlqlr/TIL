'''
a1 = 1     
a2 = 2.3
a3 = 2+3j
a4 = "Hello world"
a5 = True
a6 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a7 = (1, 2, 3, 4)
a8 = range(10)
a9 = {1, 2, 3, 4}
a10 = {"apple" : 2, "banana" : 3}
a11 = None
a12 = lambda x, y : x + y
a13 = {"a1" : [1, 2, 3], "a2" : [4, 5, 6]}           # 딕셔너리 안에 리스트가 들어갔지만 첫 형태가 딕셔너리이므로 

for i in range(1, 14):          # a1~ a12 까지 데이터 타입을 출력
    var = f'a{i}'
    var = eval(var)
    print(type(var))
'''
#print("7 / 3 : ", 7 / 3, "\n7 // 3 : ", 7 // 3, "\n7 % 3 : ", 7 % 3)       #연산자 실습 - 나눗셈 몫 나머지

# print(-2 ** 4)         # 연산자의 우선순위를 고려
# print(-(2 ** 4))
# print((-2) ** 4)

# degrees = 36.5
# print(id(degrees))      # 메모리 주소를 출력하는 문장

# degrees = 37.5
# print(id(degrees))

# number = 10 
# double = 2 * number
# print(double)

# number = 5
# print(double)

# Style Guide #
# name = "min"
# age = 33
# height = 175.4
# weight = 75.5
# is_student = True
# SECOND = 10
# MAX_VALLUE = 100
# PI = 3.14159

# person_name = "Alice"

# def calculate_sum(x, y) :                 # 함수와 함수 사이는 두줄 띄우자
#     return x + y


# def calculate_sub(x, y) :
#     return x - y 


