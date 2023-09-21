quality = input('사과 상태 입력(신선/나쁨) : ')

if quality == '신선':
    price = int(input('사과 가격 입력 : '))
    if price<1000:
        print('10개 구매')
    else:
        print('5개 구매')
else:
    print('구매하지 않는다')