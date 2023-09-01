class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'안녕, {self.name}'


class Mom(Person):
    gene = 'XX'


    def __init__(self, name):
        super().__init__(name)
    

    def swim(self):
        return '엄마가 수영'


class Dad(Person):
    gene = 'XY'


    def __init__(self, name):
        super().__init__(name)


    def walk(self):
        return '아빠가 걷기'
    

class FirstChild(Mom, Dad):
    def __init__(self, name):
        super().__init__(name)


    def swim(self):
        return '첫째가 수영'
    
    def cry(self):
        return '첫째가 응애'
    

baby1 = FirstChild('아가')
print(baby1.cry())       # 첫째가 응애
print(baby1.swim())      # 첫째가 수영
print(baby1.walk())      # 아빠가 걷기
print(baby1.gene)        # XX      다중 상속의 순서가 엄마가 먼저이므로 아빠 성별이 나온다