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

# __name__은 해당 파일 내에서 __main__이라는 값을 가진 special variable이다
# 그러나 다른 파일에 모듈로서 import가 되면 해당 모듈명으로 값이 바뀌게 된다! (여기서는 module_main으로)
# 그래서 다른 파일에 import되면 위의 조건문이 실행되지 않는 것이다
