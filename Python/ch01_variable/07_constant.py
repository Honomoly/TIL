# 상수 : 그런거 없다
# 변수와 구분하기 위해 대문자로 쓸 뿐

PI = 3.141592653589793238

INT_RATE = 0.03
deposit = 10000000

interest = deposit*INT_RATE
balance = deposit+interest
print(balance)
print(format(balance, ','))
print(int(balance))
