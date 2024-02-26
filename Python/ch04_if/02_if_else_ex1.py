id = 'flower'
password = '1234'

input_id = input('아이디 입력 : ')
input_password = input('비밀번호 입력 : ')

if input_id != id or input_password != password:
    print('로그인 실패!')
else:
    print('로그인 성공!')