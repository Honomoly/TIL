print('**********상품 정보**********')
print('1 노트북 : 1,200,000원')
print('2 노트북 : 400,000원')
print('***************************')

nb = 1200000
dc = 400000
no = input('상품번호 입력 : ')
if no == '1' or no == '2':
    num = int(input('주문 수량 입력 : '))
    if no == '1':
        name = '노트북'
        price = nb
        total = nb*num
    else:
        name = '디지털카메라'
        price = dc
        total = dc*num
    if total >= 1e6:
        discount = int(total*0.1)
    elif total >= 5e5:
        discount = int(total*0.05)
    else:
        discount = 0

    print('**********주문 내용**********')
    print('상품명 :\t%s'%name)
    print('가격 :\t\t', format(price, ','),'원')
    print('주문 수량 :\t',num)
    print('주문액 :\t', format(total, ','),'원')
    print('할인액 :\t', format(discount, ','),'원')
    print('총지불액 :\t', format(total-discount, ','),'원')
    # format()뒤에 .rjust(n)을 붙여서 오른쪽 정렬 가능
else:
    print('잘못 입력하였습니다. 종료합니다')