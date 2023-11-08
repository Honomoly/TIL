class Account: # 중복 생성되면 안되는 클래스
    __instance = None 
    __init = False
    
    def __new__(cls): # 실제로 처음 클래스 인스턴스를 생성하는 기능은 여기서 일어난다
        if cls.__instance is None:
            cls.__instance = super().__new__(cls) # super(), 다시말해 object class를 이용하여 인스턴스를 생성한다
        return cls.__instance # 이 값이 밑의 __init__()으로 들어가게 된다

    def __init__(self): # 클래스를 초기화 하는 기능 / 새로 클래스를 호출하면 해당 클래스 인스턴스는 모두 초기화 된다
        cls = type(self) # 클래스 자체(Account)를 가져온다
        if not cls.__init:
            self.__balance = 100000
            self.__sales_volumn = 0
            self.__expenses = 0
            cls.__init = True

    def get_instance(cls):
        if cls.__instance is None:
            return cls()
        return cls.__instance

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    def get_sales_volumn(self):
        return self.__sales_volumn

    def set_sales_volumn(self, sales_volumn):
        self.__sales_volumn = sales_volumn

    def get_expenses(self):
        return self.__expenses

    def set_expenses(self, expenses):
        self.__expenses = expenses