from abc import *

class DrawingObject(metaclass=ABCMeta): # 추상 클래스 정의
    def __init__(self):
        self.__pen_color = ''

    # 추상 메소드
    @abstractmethod
    def draw(self):
        pass # 비어있는 상태 / 상속받은 클래스들이 무조건 재정의 해야 쓸 수 있음