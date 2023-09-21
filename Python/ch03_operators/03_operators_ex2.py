money = int(input("교환할 돈은 얼마입니까? "))

five_h = money//500
money -= five_h*500
one_h = money//100
money -= one_h*100
five_t = money//50
money -= five_t*50
one_t = money//10
money -= one_t*10

print('오백원 : %d개'%five_h)
print('백원 : %d개'%one_h)
print('오십원 : %d개'%five_t)
print('십원 : %d개'%one_t)
print('나머지 : %d원'%money)