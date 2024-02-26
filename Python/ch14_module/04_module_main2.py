name = ''

def input_name():
    global name
    name = input('이름 입력 : ')

def get_name():
    if name == '':
        return '이름 없음'
    else:
        return name
    
# 프로그램 흐름을 제어하기 위한 부분
# 어느 함수를 먼저 수행할 것인지 결정
def main():
    input_name()
    print(get_name())
    
# 이하는 현재 파일이 단독 실행될 시 수행되는 명령문이다
# 다른파일에 import될 시 수행되지 않음
if __name__ == '__main__':
    main()