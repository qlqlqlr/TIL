# ws_3_3.py
from book import decrease_book

def rental_book(name, num):
    decrease_book(num)
    print(f"{name}님이 {num}권의 책을 대여하였습니다.")

name = "홍길동"
rental_book(name, 3)

