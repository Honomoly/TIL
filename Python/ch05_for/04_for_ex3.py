num1 = int(input('숫자1 입력 : '))
num2 = int(input('숫자2 입력 : '))

if num1 > num2 :
    num1, num2 = num2, num1

sum = 0
for i in range(num1, num2+1):
    sum += i

print('%d부터 %d까지의 합 : %d'%(num1, num2, sum))