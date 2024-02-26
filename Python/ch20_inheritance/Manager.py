from Employee import *

class Manager(Employee):
    def __init__(self, emp_no, emp_name, emp_dpt, position):
        super().__init__(emp_no, emp_name, emp_dpt) # 부모상속자에 매개변수 전달
        self.__position = position
    
    def show_manager_info(self):
        self.show_emp_info()
        print('직위 : ', self.__position)