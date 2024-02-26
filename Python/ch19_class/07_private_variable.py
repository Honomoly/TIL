# __인스턴스변수 형태로 사용하여 외부에서의 직접 변경을 차단한다
class BankAccount:
    def __init__(self):
        self.__balance = 0
        self.name = '홍길동'

    def show_balance(self):
        print('현재 잔액 : ', self.__balance)
    
    def get_name(self):
        return self.name
    
    def deposit(self):
        self.__balance += int(input('예금액 입력 : '))
    
    def withdraw(self):
        withdraw = int(input('출금액 입력 : '))
        if self.__balance < withdraw:
            print('잔액이 부족합니다.')
        else:
            self.__balance -= withdraw

acc  = BankAccount()
acc.deposit()
acc.withdraw()
acc.show_balance()