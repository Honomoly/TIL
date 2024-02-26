dep = int(input('예금액 입력 : '))
rate = float(input('이자율 입력(%) : '))
interest = dep*rate/100
total = dep+interest
print('------------------')
print('예금액 : %d원' %dep)
print('이자율 : %.1f%%'%rate)
print('예금이자 : %d원'%interest)
print('잔액 : %d원'%total)
print('------------------')
print('예금액 : '+format(dep,',')+'원')
print('이자율 : {:.1f}%'.format(rate))
print('예금이자 : '+format(int(interest),',')+'원')
print('잔액 : '+format(int(total), ',')+'원')