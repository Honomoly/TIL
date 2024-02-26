class Purchase:
    def __init__(self, coffee, purchase_cnt):
        self.__coffee = coffee
        self.__purchase_cnt = purchase_cnt
        self.__budget = coffee.get_cost() * purchase_cnt