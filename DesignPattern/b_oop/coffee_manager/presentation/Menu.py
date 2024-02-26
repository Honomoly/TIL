from service.Order import *
from service.Payment import *
from service.Purchase import *
from service.Sales import *

class Menu:
    def __init__(self, drinks, account):
        self.__drinks = drinks
        self.__account = account
        self.__present_menu()

    def __present_menu(self):
        print("=======메뉴 (주문번호)=======")
        for idx, drink in enumerate(self.__drinks):
            print(drink.get_name(), f" ({idx})")
        while True:
            ipt = int(input("주문번호 입력 : "))
            if ipt in list(range(len(self.__drinks))):
                pass
            elif ipt == -1:
                print("관리자화면")
            elif ipt == "quit":
                print("종료합니다")
                break