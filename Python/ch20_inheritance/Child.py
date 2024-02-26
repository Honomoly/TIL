from Parent import *

class Child(Parent): # 부모에서 변수와 메소드 상속 받기
    def __init__(self):
        super().__init__() # 부모생성자(부모의 변수들) 호출
        self.__c = 20

    def show_child(self):
        self.show_parent() # 부모의 메소드 사용 가능
        print('자식 클래스의 숫자 : ', self.__c)
        print(self._Parent__p) # 부모의 인스턴스 사용 가능