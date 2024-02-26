class Calculator:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
    
    def input(self):
        self.num1 = int(input('숫자1 입력 : '))
        self.num2 = int(input('숫자2 입력 : '))

    def add(self):
        print('덧셈 : ', self.num1 + self.num2)

    def multiply(self):
        print('곱셈 : ', self.num1 * self.num2)

cal = Calculator()

cal.input()

cal.add()
cal.multiply()