# 진법 변경
# print(bin(12))     #0b1100
# print(oct(12))     #0o14
# print(hex(12))     #0xc

# print (2 / 3)   #0.66666666666 메모리 한계에 따른 근사값 표현

# print (5 / 3)   #1.66666666667

##부동소수점

# a = 3.2 - 3.1    #0.1000000000000009
# b = 1.2 - 1.1    #0.0999999999999987

# # 1. 임의의 작은 수 활용
# print(abs(a - b)) <= 1e-10  #True        두수의 차가 임의의 작은수 보다 작다면 같다고보는 것

# # 2. math 모듈 활용
# import math
# print(math.isclose(a, b))   #True        모듈을 활용해서 가까운 수를 같다고 보는 것

# # 314 * 0.01
# number = 314e-2

# #float
# print(type(number))

# #3.14
# print(number)

# #지수(제곱)하는 횟수 표현
# print(314e-2)  #3.14
# print(314e2)   #31400.0


## sequence Type

# # f-string
# bugs = 'roaches'
# counts = 100
# area = 'living room'
# print(f'Debugging {bugs} {counts} {area}')

# set1 = {1, 3, 2, 5, 4}    # 세트는 순서와 중복이 없다
# set2 = {1, 1, 2, 4, 4}
# print(set1)
# print(set2)
