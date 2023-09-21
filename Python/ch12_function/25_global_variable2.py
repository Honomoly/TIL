# 전역변수 사용 선언 없이 해당 변수는 수정은 불가능하다
a = 1 # global variable

def show():
    a = 100 # 위의 전역변수가 아닌 지역변수로 따로 저장됨
    print(a)

show()
print(a)

def show1():
    # a += 10 # 그냥 수정하는것은 불가능
    global a # 전역변수 사용 선언 / 전역변수 가져옴
    a += 10 # 그 후에 변경 가능
    print(a)

show1()
print(a)