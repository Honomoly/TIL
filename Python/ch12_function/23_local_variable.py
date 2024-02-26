# 함수내에서 정의된 변수(지역변수)는 함수 종료후 사라진다
def show():
    a = 1 # local variable
    a += 1
    print(a)

show()
# print(a) # show()을 실행한 후라도 오류

def get_name():
    print(a) # 다른 함수에서도 안됨

get_name()