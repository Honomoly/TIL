phone = input('전화번호 입력(\'-\' 없이 입력) : ')

if phone.isdigit(): # 순수 숫자인지 확인
    pass
else:
    print('숫자만 입력하세요')
print('입력한 값 : ', phone)

########################

name = input('이름 입력 : ')

if name.isalpha(): # 순수 문자인지 확인
    pass
else:
    print('문자만 입력하세요')

########################

id = input('ID 입력 : ')

if id.isalnum(): # 순수 문자및 숫자인지 확인
    pass
else:
    print('문자및 숫자만 입력하세요')

########################

print('  '.isspace()) # 순수하게 space면 됨
print(' c'.isspace()) # 섞여서 나오면 당연히 안됨