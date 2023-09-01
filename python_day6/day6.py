# 파이썬 6일차

# my_set = {1, 2, 3}
# # my_set.discard(2)
# # print(my_set)         # {1, 3}

# # my_set.remove(10)    # key error 10

# # my_set.discard(10)    # 없는 요소를 지우려고해도 에러가 발생하지는 않음

# element = my_set.pop()
# print(element)      #  1          
# print(my_set)       # {2, 3}    


# my_dict = {
#     'name' : 'Alice'
# }

# print(my_dict['name'])
# print(my_dict.get('name'))

# # 찾고자 하는 키가 없을 때 
# # print(my_dict['age'])   # KeyError
# print(my_dict.get('age')) # None
# print(my_dict.get('age', 'Unknown'))   # Unknown



# person = {
#     'name' : 'Alice',
#     'age' : 25
# }
# print(person.keys())

# for k in person.keys():
#     print(k)

# print(person.values())

# for v in person.values():
#     print(v)

# print(person.items())
# for key, value in person.items():
#     print(key,value)


# print(person.pop('age'))
# # print(person.pop('country'))     # Key Error
# print(person.pop('country', 'country 키는 없어요'))    
# # 없는걸 팝하면 우측 메세지 출력





# .setdefault(key[,default]) : 키와 연결된 값을 반환, 
# 키가 없다면 default와 연결한 키를 딕셔너리에 추가하고 default를 반환

# person = {
#     'name' : 'Alice',
#     'age' : 25
# }

# print(person.setdefault('country', 'KOREA'))    #KOREA
# print(person)         # {'name': 'Alice', 'age': 25, 'country': 'KOREA'}
# print(person.setdefault('age', 50))    # 이미 있는 키 이므로 조회만 함 





# 키를 통해서 값을 조회하는 3가지 방법을 배움
# 키값이 존재하고 문제가 없다면 셋 다 똑같이 동작함

# 혈액형 인원수 세기 문제실습
# 결과 => {'A': 3, 'B': 3, 'O': 3, 'AB': 3}
blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']

# 1) []

# new_dict = {}      # 결과는 딕셔너리 이므로 딕셔너리 생성
# # 순회하면서 찾아야 한다
# for blood_type in blood_types:
#     # 처음 등장한 혈액형과 이미 기존에 존재하는 혈액형의 경우 두가지를 고려해야함
#     # if 기존에 키가 이미 존재
#     if blood_type in new_dict:
#         #기존의 키의 값을 +1
#         new_dict[blood_type] += 1 

#     # if 키가 존재하지 않는다면 (처음 설정되는 키 1)
#     else:
#         new_dict[blood_type] = 1
# print(new_dict)



# # 2) .get()

# new_dict = {}      # 결과는 딕셔너리 이므로 딕셔너리 생성
# # 순회하면서 찾아야 한다
# for blood_type in blood_types:

#     new_dict[blood_type] = new_dict.get(blood_type, 0) + 1  # get으로 조회해서 없는 키이면 0값을 넣어 만듬
# print(new_dict)




# # 3) .setdefualt()

# for blood_type in blood_types:
#     new_dict.setdefault(blood_type, 0)  # 없으면 바로 넣어주기 떄문에 할당 필요없음
#     new_dict[blood_type] += 1
# print(new_dict)









# # 얕은 복사의 한계

# a = [1, 2, [1, 2]]
# b = a[:]
# b[2][0] =999
# print(a, b)        # a 도 똑같이 바뀜 

# c = a.copy()
# c[2][0] = 222
# print(a, c)         # 여기도 a가 같이 바뀜



# # 깊은 복사를 하면 해결 가능
# import copy

# original_list = [1, 2, [1, 2]]

# deep_copied_list = copy.deepcopy(original_list)

# deep_copied_list[2][0] = 999

# print(original_list, deep_copied_list)         # 오리지널에는 아무런 변화가 없다


