number_of_people = 0
from book import decrease_book

def increase_user():
    global number_of_people
    number_of_people += 1

def create_user(name, age, address):
    increase_user()
    print(f'{name}님 환영합니다!')
    return {'name': name, 'age': age, 'address': address}

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

many_user = list(map(lambda n, a, ad: create_user(n, a, ad), name, age, address))


def rental_book(info):
    num_of_books = info['age'] // 10
    decrease_book(num_of_books)
    print(f'{info["name"]}님이 {num_of_books}권의 책을 대여하였습니다.')

list(map(lambda u: rental_book(u), many_user))

