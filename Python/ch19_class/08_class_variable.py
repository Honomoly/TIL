# 클래스 변수 : 모든 클래스 객체들이 공용으로 사용하는 변수

class Calculation:
    total = 0 # 클래스 변수

    def __init__(self, num):
        self.__num = num
        self.add_to_total() # 만들어지자마자 total에 더함

    def add_to_total(self):
        Calculation.total += self.__num
    
    def show(self):
        print('-------------')
        print('num : ', self.__num)
        print('total : ', Calculation.total)

c1 = Calculation(10)
c1.show()

c2 = Calculation(20)
c2.show()
