# import requests

# url = 'https://fakestoreapi.com/carts'
# response = requests.get(url)




# print(response)            # <Response [200]>


# import json    # 내장 모듈

# # json 데이터
# json_data = '''
# {
#     "name": "김싸피",
#     "age": 28,
#     "hobbies": [
#         "공부하기",
#         "복습하기"
#     ]
# }
# '''

# print(json_data)     # 문자열이기 떄문에 항목에 접근하기가 어렵다. 슬라이싱 으로 일일히 숫자세서 접근해야함 


# data = json.loads(json_data)   # loads : 딕셔너리로 변환해준다 
# print(data)         # {'name': '김싸피', 'age': 28, 'hobbies': ['공부하기', '복습하기']}


# # json에서 원하는 데이터만 가져오기
# name = data.get('name')
# print(name)            # 김싸피



