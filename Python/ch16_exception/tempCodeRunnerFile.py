try :
    num = int(input('숫자 입력 : '))
except ValueError :
    print('숫자가 아닙니다')
else :
    print(num)
finally :
    print('종료') # 오류 발생 여부와 상관없이 실행