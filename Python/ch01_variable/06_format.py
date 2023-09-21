
weight = 70
height = 1.72
bmi = 22.8571

# format() 사용
print('몸무게 : {}, 키 : {}, bmi : {}'.format(weight, height, bmi))
print('키 : {1}, 몸무게 : {0}, bmi : {2}'.format(weight, height, bmi))
print('몸무게 : {0}, 키 : {1:.3f}, bmi : {2:.2f}'.format(weight, height, bmi))

# 천단위 구분
x = 1000
y = 2142
print(format(x, ','), format(y, ','))

# 변수 2개 이상
total = 250
avg = 83.3333
print('%d, %.2f'%(total, avg))