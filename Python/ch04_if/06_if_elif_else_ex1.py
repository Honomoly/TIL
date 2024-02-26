num1 = int(input('정수1 입력 : '))
num2 = int(input('정수2 입력 : '))
num3 = int(input('정수3 입력 : '))

if num1>num2 and num1>num3:
    print('제일 큰 수 : ', num1)
elif num2>num3:
    print('제일 큰 수 : ', num2)
else:
    print('제일 큰 수 : ', num3)