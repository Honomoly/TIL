# 문자 리터럴
str1 = 'python'
str2 = "파이썬"
str3 = '''파이썬
프로그래밍'''
str4 = """줄바꿈도
    인식함"""

print(str1)
print(str2)
print(str3)
print(str4)

# 논리 리터럴
t, f = True, False
print(t, type(t))

# 특수 리터럴
name = '홍길동'
phone = ''
address = None

print(name, phone, address)
print(type(phone), type(address))

'''따옴표 3개를 연속으로 사용하면
여러줄을 사용하는 주석이 된다'''

# 줄바꿈
a = 1+2+3+\
    4+5+6
b = (1+2+3+
     4+5+6)
print(a, b)

print('대신귀\n여운고\n양이를\n드리겠\n습니다')
print('얼마든지 \\, \', \" 출력하는 것이 가능하다')

# 특수문자 비활성화
print(r'C:\info\name')
print('홍길동'); print('이몽룡')

# 옆으로 출력
print('홍길동', end=""); print('이몽룡')

