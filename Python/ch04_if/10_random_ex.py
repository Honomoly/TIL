you = input('YOU 입력 : ')
from random import *
cpu_n = randrange(3)

if you == '가위':
    you_n = 0
elif you == '바위':
    you_n = 1
else:
    you_n = 2

if cpu_n == 0:
    cpu = '가위'
elif cpu_n == 1:
    cpu = '바위'
else:
    cpu = '보'

if you_n-cpu_n == 1 or you_n-cpu_n == -2:
    print('당신이 이겼습니다.')
elif you_n == cpu_n:
    print('비겼습니다.')
else:
    print('컴퓨터가 이겼습니다.')
print('컴퓨터는 %s 입니다.'%cpu)