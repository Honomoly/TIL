class Payment:
    def __init__(self, order):
        self.__order = order
        self.__pay_price = order.get_order_price()