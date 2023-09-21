def order() :
    input_price = int(input('상품가격 입력 : '))
    input_quantity = int(input('주문수량 입력 : '))
    return input_price, input_quantity, input_quantity*input_price

a1, a2, a3 = order()
print('-------------------')
print('상품가격 : ', a1)
print('주문수량 : ', a2)
print('주문액 : ', a3)