type = input('번호 입력(1. 현금, 2. 카드) : ')
if type != '1' and type != '2':
    print('잘못 입력하였습니다. 종료합니다.')
else:
    pay = int(input('지불액 입력 : '))
    if type == '1':
        print('할인율 10%')
        print('할인액 : %d원'%(pay*0.1))
    else:
        print('할인율 5%')
        print('할인액 : %d원'%(pay*0.05))
