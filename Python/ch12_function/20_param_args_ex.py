def order_coffee(coffee, *options):
    print(coffee,', 옵션 :',end=' ')
    for option in options:
        print(option, end=' ')
    print()

order_coffee('아메리카노', 'Tall', 'HOT', '시럽추가', 'stay')
order_coffee('카페라떼', 'Grande', 'ICE', 'go')