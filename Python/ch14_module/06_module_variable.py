from show_info import *

print(age)

def get_age():
    global age # 전역변수이므로 선언해야 변경이 됨
    age += 10
    print(age)

get_age()

# 변수만 import 하기
from show_info import age
print(age)