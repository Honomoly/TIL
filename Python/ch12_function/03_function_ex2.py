
def login() :
    input_id = input('ID 입력 : ')
    input_password = input('비밀번호 입력 : ')
    if input_id=='abcd' and input_password=='1234':
        show_main()
    else:
        print('로그인 실패')

def show_main() :
    print('방문을 환영합니다')

login()