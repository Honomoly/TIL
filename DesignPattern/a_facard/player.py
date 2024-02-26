class IllegalArgError(RuntimeError):
    pass

class Player:
    def __init__(self, name):
        self.__name = name
        
    def prepare(self):
        print(f'{self.__name} 가 연주할 준비 중입니다.')
    
    def ing(self):
        print(f'{self.__name} 가 연주 중입니다.')
        
    def end(self):
        print(f'{self.__name} 가 연주를 마칩니다.')
    
    def curtain_call(self):
        print(f'{self.__name} 가 커튼콜을 진행합니다.')
        
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        if name is None:
            raise IllegalArgError
        
        self.__name = name