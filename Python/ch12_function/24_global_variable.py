# 전역변수
a = 1 # global variable

def show():
    print(a) # 모든 곳에서 사용 가능

def add():
    print(a)

show()
add()
print(a)

#########################

def show1():
    print(x) # 이걸 쓸려면 x가 함수 호출 전에 정의 되어있어야 함!

x = 100
show1() 
