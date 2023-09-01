# #python 5일차 실시간 강의

# print(help(list))

# #메서드는 어딘가(클래스)에 속해있는 함수이며, 각 데이터 타입별로 다양한 기능을 가진 메서드가 존재

# numbers = [1, 2, 3]
# numbers2 = [4, 5, 6]
# numbers.append(numbers2)
# print(numbers)       # [1, 2, 3, [4, 5, 6]]
 
# numbers.extend(numbers2)
# print(numbers)          # [1, 2, 3, 4, 5, 6]


numbers = [1, 2, 3]
# sort 함수
print(numbers.sort())    # None

# sorted 함수
print(sorted(numbers))