class Worker:
    def __init__(self, no, name):
        self.__no = no
        self.__name = name
    
    def show_worker_info(self):
        print('사번 : ', self.__no)
        print('성명 : ', self.__name)