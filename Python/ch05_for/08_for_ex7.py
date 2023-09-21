list = ['홍길동', '이몽룡', '성춘향', '변학도']

name = input('이름 입력 : ')

att = False
for member in list:
    if member == name:
        att = True
        break

if att:
    print('명단에 있습니다.')
else:
    print('명단에 없습니다.')