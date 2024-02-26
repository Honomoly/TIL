import datetime

class Order:
    def __init__(self, coffee, order_cnt):
        self.__coffee = coffee
        self.__order__cnt = order_cnt
        self.__order_time = datetime.now()
        self.__order_price = coffee.get_price()
        self.__order_title = f"{coffee.get_name()} [{order_cnt}잔]"