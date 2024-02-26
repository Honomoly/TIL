def get_interest(deposit, int_rate):
    return int(deposit*int_rate/100)

deposit = int(input('예금액 입력 : '))
int_rate = float(input('이자율 입력(%) : '))
print('이자액 : ',format(get_interest(deposit, int_rate),','),'원')