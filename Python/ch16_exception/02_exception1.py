# try - except - else - finally
try :
    # 코드 실행 시도
    print(10/0)
except : # 미지정시 모든 에러 처리
    # 에러시 실행되는 문장
    print('나누기 예외처리 됨')


# 여러개 적을 시 첫 에러만 처리됨
try :
    print('나이 : ' + 23 + '살') # 여기서 에러나면
    print(10/0) # 이 문장은 처리 안됨
except ZeroDivisionError :
    print('0으로 나눌 수 없습니다!')
except TypeError :
    print('타입이 일치하지 않습니다!')


# 함께 처리
try :
    print(10/0)
    print('나이 : ' + 23 + '살')
except (ZeroDivisionError, TypeError) as e : # 에러 원인을 e에 저장
    print('오류가 발생했습니다!', e)


# 오류를 모를 경우 최상위인 Exception으로 처리
try :
    print(10/0)
    print('나이 : ' + 23 + '살')
except Exception as e : # 에러 원인을 e에 저장
    print('오류가 발생했습니다!', e)