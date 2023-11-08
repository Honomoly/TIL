class Coffee:
    def __init__(self, name, price, cost, stock, safety_stock, sales_cnt):
        self.__name = name
        self.__price = price
        self.__cost = cost
        self.__stock = stock
        self.__safety_stock = safety_stock
        self.__sales_cnt = sales_cnt
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
    def get_price(self):
        return self.__price
    
    def set_price(self, price):
        self.__price = price
    
    def get_cost(self):
        return self.__cost
    
    def set_cost(self, cost):
        self.__cost = cost
    
    def get_stock(self):
        return self.__stock
    
    def set_stock(self, stock):
        self.__stock = stock
    
    def get_safety_stock(self):
        return self.__safety_stock
    
    def set_safety_stock(self, safety_stock):
        self.__safety_stock = safety_stock
    
    def get_sales_cnt(self):
        return self.__sales_cnt
    
    def set_sales_cnt(self, sales_cnt):
        self.__sales_cnt = sales_cnt