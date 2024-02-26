def order(price, qty):
    amount = price*qty
    discount = get_discount(amount)
    total = get_total(amount, discount)
    return amount, discount, total

def get_discount(amount):
    if amount >= 1e5:
        discount = amount*0.1
    elif amount >= 5e4:
        discount = amount*0.05
    else:
        discount = 0
    return int(discount)
 
def get_total(amount, discount):
    return amount - discount

input_price = int(input('상품 가격 입력 : '))
input_qty = int(input('주문 수량 입력 : '))
print('----------------')
amount, discount, total = order(input_price, input_qty)
print('주문액 : %d원'%amount)
print('할인액 : %d원'%discount)
print('지불액 : %d원'%total)