from Worker import *

class PartTime(Worker):
    def __init__(self, no, name, pay, time):
        super().__init__(no, name)
        self.__pay = pay
        self.__time = time

    def calculate_salary(self):
        return self.__pay*self.__time
    
    def show_pt_info(self):
        print('시급 : %d원'%self.__pay)
        print('근무시간 : %d시간'%self.__time)
        print('급여 : %d원'%self.calculate_salary())