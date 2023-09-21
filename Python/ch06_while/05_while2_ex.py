money = 10000
i = 0
while True:
    i += 1
    money -= 2000
    print('노래를 %d곡 불렀습니다.'%i)
    if money <= 0:
        print('잔액이 없습니다. 종료합니다.')
        break
    print('현재 %d원 남았습니다.'%money)
